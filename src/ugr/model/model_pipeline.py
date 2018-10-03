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
from ugr.model.nlp_utils import NLPUtils

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
        
        
    def initilization(self, conf_path):
        
        PropertiesManager.load_properties(conf_path)
        
        self.__encoding = PropertiesManager.get_prop_value(PropertiesNames.ENCODING)
        self.__lang = PropertiesManager.get_prop_value(PropertiesNames.LANG)
        
        corpus_name = PropertiesManager.get_prop_value(PropertiesNames.CORPUS_NAME)
        if corpus_name is None:
            raise ValueError("You must define the corpus type.")
        
        self.__corpus_handler = FactoryCorpus.creator(corpus_name)
        
        allow_labels_name = PropertiesManager.get_prop_value(PropertiesNames.ALLOW_LABELS)
        if allow_labels_name is None:
            raise ValueError("You must define the number of labels of the output data.")
        
        self.__allow_labels = FactoryAllowLabels.creator(allow_labels_name)
        
        self.__nlp_utils = NLPUtils()
        self.__nlp_utils.lang = self.__lang
        self.__nlp_utils.encoding = self.__encoding
        self.__nlp_utils.conf_path = PropertiesManager.get_prop_value(PropertiesNames.NLP_LIBRARY_PATH)
        self.__nlp_utils.initialization()
        
    def __make_features(self):
        pass
    
    def proc_pipeline(self):
        
        self.__corpus_handler.load()
        
        self.__nlp_utils.config_pipeline()
        self.__nlp_utils.initialize_pipeline()
        
        for doc_id in self.__corpus_handler.corpus:
            doc = self.__corpus_handler.get_document(doc_id)
            doc.proc_title = self.__nlp_utils.nlp_analize(doc.raw_title)
            doc.proc_body = self.__nlp_utils.nlp_analize(doc.raw_body)
            
        self.__make_features()
        
            
        