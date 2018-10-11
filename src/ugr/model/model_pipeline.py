#!/usr/bin/python3
#! *-* coding: utf-8 *-*
'''
Created on 3 oct. 2018

:author: Eugenio Martínez Cámara <emcamara@decsai.ugr.es>
'''
from ugr.model.properties_manager import PropertiesManager
from ugr.model.properties_names import PropertiesNames
from ugr.model.dao.factory_corpus import FactoryCorpus
from ugr.model.factory_allow_labels import FactoryAllowLabels
from ugr.model.nlp.nlp_utils import NLPUtils
from ugr.model.factory_weight_features import FactoryWeightFeatures
from ugr.model.word import Word

class ModelPipeline:
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        
        self.__encoding = None
        self.__lang = None
        self.__corpus_handler = None
        self.__nlp_utils = None
        self.__allow_labels = None
        self.__features_generator = None
        self.__field_to_process = None
        self.__get_word_info_method = None
        self.__output_matlab_path = None
        self.__remove_stopwords = None
        self.__transform_digits = None
        
        
    def __select_word_info_method(self):
        
        use_raw_words = PropertiesManager.get_prop_value(PropertiesNames.USE_RAW_WORDS.value)
        use_lemma_words = PropertiesManager.get_prop_value(PropertiesNames.USE_LEMMA_WORDS.value)
        use_stem_words = PropertiesManager.get_prop_value(PropertiesNames.USE_STEMMER_WORDS.value)
        remove_accents = PropertiesManager.get_prop_value(PropertiesNames.REMOVE_ACCENTS.value)
        to_lower_case = PropertiesManager.get_prop_value(PropertiesNames.TO_LOWERCASE.value)
        
        if use_raw_words is True and use_lemma_words is False and use_stem_words is False:
            if to_lower_case is False:
                if remove_accents is False:
                    self.__get_word_info_method = Word.raw_form
                else:
                    self.__get_word_info_method = Word.raw_form_no_accent
            else:
                if remove_accents is False:
                    self.__get_word_info_method = Word.raw_form_lc
                else:
                    self.__get_word_info_method = Word.raw_form_lc_no_accent
        elif use_raw_words is False and use_lemma_words is True and use_stem_words is False:
            if remove_accents is False:
                self.__get_word_info_method = Word.lemma
            else:
                self.__get_word_info_method = Word.lemma_no_accent
        elif use_raw_words is False and use_lemma_words is False and use_stem_words is True:
            self.__get_word_info_method = Word.stem
        else:
            raise ValueError("The configuration of the preprocesing is not right. Check it!")
    
    def initilization(self, conf_path):
        
        PropertiesManager.load_properties(conf_path)
        
        self.__encoding = PropertiesManager.get_prop_value(PropertiesNames.ENCODING.value)
        self.__lang = PropertiesManager.get_prop_value(PropertiesNames.LANG.value)
        
        allow_labels_name = PropertiesManager.get_prop_value(PropertiesNames.ALLOW_LABELS.value)
        if allow_labels_name is None:
            raise ValueError("You must define the number of labels of the output data.")
        
        self.__allow_labels = FactoryAllowLabels.creator(allow_labels_name)
        
        corpus_name = PropertiesManager.get_prop_value(PropertiesNames.CORPUS_NAME.value)
        if corpus_name is None:
            raise ValueError("You must define the corpus type.")
        
        self.__corpus_handler = FactoryCorpus.creator(corpus_name)
        self.__corpus_handler.allow_labels = self.__allow_labels
        
        self.__nlp_utils = NLPUtils()
        self.__nlp_utils.lang = self.__lang
        self.__nlp_utils.encoding = self.__encoding
        self.__nlp_utils.conf_path = PropertiesManager.get_prop_value(PropertiesNames.NLP_LIBRARY_PATH.value)
        self.__nlp_utils.initialization()
        
        features_generator_name = PropertiesManager.get_prop_value(PropertiesNames.FEAUTRES_GENERATOR_NAME.value)
        if features_generator_name is None:
            raise ValueError("You must define the features generator.")
        
        self.__features_generator = FactoryWeightFeatures.creator(features_generator_name)
        
        self.__field_to_process = PropertiesManager.get_prop_value(PropertiesNames.FIELD_TO_PROCESS.value)
        if self.__field_to_process is None:
            self.__field_to_process = "title_body"
            
            
        output_matlab_path = PropertiesManager.get_prop_value(PropertiesNames.OUTPUT_MATLAB_PATH.value)
        if output_matlab_path is None:
            raise ValueError("You must set an output matlab file path.")
        self.__output_matlab_path = output_matlab_path
        
        self.__select_word_info_method()
        
        self.__remove_stopwords = PropertiesManager.get_prop_value(PropertiesNames.USE_STOPPER.value)
        self.__transform_digits = PropertiesManager.get_prop_value(PropertiesNames.TRANS_DIGITS.value)
        
    
    def __select_field_to_process(self, doc):
        
        doc_processed = None
        
        if self.__field_to_process == "title":
            doc_processed = doc.proc_title
        elif self.__field_to_process == "body":
            doc_processed = doc.proc_body
        else:
            if doc.proc_title is None and doc.proc_body is None:
                doc_processed = None
            elif doc.proc_title is not None and doc.proc_body is None:
                doc_processed = doc.proc_title
            else:
                doc_processed = doc.proc_body
            
        return doc_processed
    
    
    def __make_features(self):
        
        text_corpus = []
        for doc_id in self.__corpus_handler.corpus:
            doc = self.__corpus_handler.get_document(doc_id)
            doc_processed = self.__select_field_to_process(doc)
            if doc_processed is not None:
                text_doc = []
                
                for sent in doc_processed:
                    for word in sent:
                        proc_word = ""
                        if self.__remove_stopwords is True:
                            if word.is_stopword is False:
                                if self.__transform_digits is True and word.is_digit is True:
                                    proc_word = "__DIGIT__"
                                else:
                                    proc_word = self.__get_word_info_method(word)
                                text_doc.append(proc_word)
                        else:
                            if self.__transform_digits is True and word.is_digit is True:
                                proc_word = "__DIGIT__"
                            else:
                                proc_word = self.__get_word_info_method(word)
                            
                            text_doc.append(proc_word)
                
                text_corpus.append(text_doc)
        self.__features_generator.weight_features(text_corpus)
            
            
            
    
    def proc_pipeline(self):
        
        self.__corpus_handler.load(PropertiesManager.get_prop_value(PropertiesNames.CORPUS_PATH.value))
        
        self.__nlp_utils.config_pipeline()
        self.__nlp_utils.initialize_pipeline()
        
        for doc_id in self.__corpus_handler.corpus:
            doc = self.__corpus_handler.get_document(doc_id)
            if self.__field_to_process == "title":
                doc.proc_title = self.__nlp_utils.nlp_analize(doc.raw_title)
            elif self.__field_to_process == "body":
                doc.proc_body = self.__nlp_utils.nlp_analize(doc.raw_body)
            else:
                doc.proc_title = self.__nlp_utils.nlp_analize(doc.raw_title)
                doc.proc_body = self.__nlp_utils.nlp_analize(doc.raw_body)
            print("INFO: Proc. doc: {}".format(doc.id))
            
        self.__make_features()
        self.__features_generator.write_matlab_format(self.__output_matlab_path, self.__corpus_handler)
        
            
        