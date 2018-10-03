#!/usr/bin/python3
# *-* coding: utf-8 *-*
'''
Created on 3 oct. 2018

:author: Eugenio Martínez Cámara <emcamara@decsai.ugr.es>
'''

from ugr.model.word import Word
from nltk.stem.snowball import SnowballStemmer
from nltk.corpus import stopwords

import os
import ugr.model.nlp.pyfreeling as nlp_handler



class NLPUtils:
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        
        self.__lang = None
        self.__encoding = "default"
        self.__conf_path = ""
        self.__nlp_analyzer = None
        self.__stemmer = None
        self.__stopwords = None
         
        
    @property
    def lang(self):
        """
        """
        return self.__lang
    
    
    @lang.setter
    def lang(self, a_lang):
        self.__lang = a_lang
        
    @property
    def encoding(self):
        """
        """
        return self.__encoding
    
    @encoding.setter
    def encoding(self, a_encoding):
        self.__encoding = a_encoding
        
    @property
    def conf_path(self):
        return self.__conf_path
    
    @conf_path.setter
    def conf_path(self, a_conf_path):
        self.__conf_path = a_conf_path    
    
    
    def initialization(self):
        
        nlp_handler.util_init_locale(self.__encoding)
        
    def config_pipeline(self):
        
        conf_options = nlp_handler.config_options()
        conf_options.Lang = self.__lang
        
        language_conf_path = os.path.join(self.__conf_path, conf_options.Lang)
        language_conf_path = "{}{}".format(language_conf_path, os.sep)
        
        conf_options.TOK_TokenizerFile = "{}{}".format(language_conf_path, "tokenizer.dat")
        conf_options.SPLIT_SplitterFile = "{}{}".format(language_conf_path, "splitter.dat")
        conf_options.MACO_LocutionsFile = "{}{}".format(language_conf_path, "locutions.dat")
        conf_options.MACO_QuantitiesFile = "{}{}".format(language_conf_path, "quantities.dat")
        conf_options.MACO_AffixFile = "{}{}".format(language_conf_path, "afixos.dat")
        conf_options.MACO_ProbabilityFile = "{}{}".format(language_conf_path, "probabilities.dat")
        conf_options.MACO_DictionaryFile = "{}{}".format(language_conf_path, "dicc.src")
        conf_options.MACO_NPDataFile = "{}{}".format(language_conf_path, "np.dat")
        conf_options.MACO_PunctuationFile = "{}{}".format(language_conf_path, "../common/punct.dat")
        conf_options.MACO_ProbabilityThreshold = 0.001
        
        conf_options.TAGGER_HMMFile = "{}{}".format(language_conf_path, "tagger.dat")
        conf_options.TAGGER_ForceSelect = nlp_handler.TAGGER
        
        self.__nlp_analyzer = nlp_handler.analyzer(conf_options)
         
    def initialize_pipeline(self):
        
        init_pipeline = nlp_handler.invoke_options()
        init_pipeline.InputLevel = nlp_handler.TEXT
        init_pipeline.OutputLevel = nlp_handler.TAGGED
        
        init_pipeline.MACO_UserMap = False
        init_pipeline.MACO_AffixAnalysis = True
        init_pipeline.MACO_MultiwordsDetection = False
        init_pipeline.MACO_NumbersDetection = True
        init_pipeline.MACO_PunctuationDetection = True
        init_pipeline.MACO_DatesDetection = True
        init_pipeline.MACO_QuantitiesDetection = True
        init_pipeline.MACO_DictionarySearch = True
        init_pipeline.MACO_ProbabilityAssignment = True
        init_pipeline.MACO_CompoundAnalysis = False
        init_pipeline.MACO_NERecognition = False
        init_pipeline.MACO_RetokContractions=False
        
        init_pipeline.TAGGER_which = nlp_handler.HMM
        
        self.__nlp_analyzer.set_current_invoke_options(self.__init_pipeline)
        
        self.__stemmer = SnowballStemmer("spanish")
        self.__stopwords = stopwords.words("spanish")
        
    
    def __is_filter_word(self, word_tag):
        
        is_filter = False
        if word_tag[0] == "F":
            is_filter = True
        
        return is_filter
    
    def __delete_accents(self, str_word):
        str_word_no_accents = str_word
        
        if "á" in str_word_no_accents:
            str_word_no_accents=str_word_no_accents.replace("á", "a")
        elif "Á" in str_word_no_accents:
            str_word_no_accents=str_word_no_accents.replace("Á", "A")
        elif "é" in str_word_no_accents:
            str_word_no_accents=str_word_no_accents.replace("é", "e")
        elif "É" in str_word_no_accents:
            str_word_no_accents=str_word_no_accents.replace("É", "E")
        elif "í" in str_word_no_accents:
            str_word_no_accents=str_word_no_accents.replace("í", "i")
        elif "Í" in str_word_no_accents:
            str_word_no_accents=str_word_no_accents.replace("Í", "I")
        elif "ó" in str_word_no_accents:
            str_word_no_accents=str_word_no_accents.replace("ó", "o")
        elif "Ó" in str_word_no_accents:
            str_word_no_accents=str_word_no_accents.replace("Ó", "O")
        elif "ú" in str_word_no_accents:
            str_word_no_accents=str_word_no_accents.replace("ú", "u")
        elif "Ú" in str_word_no_accents:
            str_word_no_accents=str_word_no_accents.replace("Ú", "U")
            
        
        return str_word_no_accents
    
    
    
    def __filter_nlp_info(self, sentences):
        """
        """
        
        meta_sentences = []
        
        for sent in sentences:
            meta_sent = []
            for word in sent:
                if not self.__is_filter_word(word.get_tag()):
                    meta_word = Word()
                    if (word.get_tag()[0]=="Z"):
                        meta_word.is_digit = True
                        meta_word.w_raw_form = word.get_form()
                    else:
                        meta_word.w_raw_form = word.get_form()
                        meta_word.w_raw_form_no_accent = self.__delete_accents(meta_word.w_raw_form)
                        meta_word.w_raw_form_lc = word.get_lc_form()
                        meta_word.w_raw_form_lc_no_accent = self.__delete_accents(meta_word.w_raw_form_lc)
                        meta_word.w_lemma = word.get_lemma()
                        meta_word.w_lemma_no_accent = self.__delete_accents(meta_word.w_lemma)
                        meta_word.w_stem = self.__stemmer.stem(meta_word.w_raw_form)
                        if meta_word.w_raw_form_lc in self.__stopwords:
                            meta_word.is_stopword = True
                    meta_sent.append(meta_word)
            meta_sentences.append(meta_sent)
                    
    
    
    def nlp_analize(self, text):
        
        sentences = self.__nlp_analyzer.analyze(text, True)
        
        meta_sentences = self.__filter_nlp_info(sentences)
        
        return meta_sentences
        
        
        
        