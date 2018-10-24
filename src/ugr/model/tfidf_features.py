#!/usr/bin/python
# *-* coding: utf-8 *-*

'''
Created on 4 oct. 2018

:author: Eugenio Martínez Cámara <emcamara@decsai.ugr.es>
'''
from sklearn.feature_extraction.text import TfidfVectorizer
from scipy.io import savemat

from ugr.model.abs_weight_features import ABSWeightFeatures
from ugr.model.properties_manager import PropertiesManager
from ugr.model.properties_names import PropertiesNames



class TFIDFFeatures(ABSWeightFeatures):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.__vectorizer = None
        self.__features_weights = None
        
        
        
    def weight_features(self, raw_documents):
        """
        """
        min_gram = int(PropertiesManager.get_prop_value(PropertiesNames.MIN_GRAM.value))
        max_gram = int(PropertiesManager.get_prop_value(PropertiesNames.MAX_GRAM.value))
        ngrams = (min_gram, max_gram)
        self.__vectorizer = TfidfVectorizer(
            analyzer="word",
            tokenizer=lambda x: x,
            preprocessor=lambda x: x,
            token_pattern=None,
            ngram_range=ngrams,
            lowercase=None,
            dtype='double'
            )
        self.__features_weights = self.__vectorizer.fit_transform(raw_documents)
        
        
        
    def write_matlab_format(self, path, corpus):
        """
        """
        labels = [corpus.get_document(id).allow_label for id in corpus.doc_ids()]
        dict_meta_corpus = {
            "n_docs":corpus.get_size(),
            "doc_ids":corpus.doc_ids(),
            "labels":labels,
            "features_names":self.__vectorizer.get_feature_names(),
            "features_weights":self.__features_weights
            }
        savemat(path, dict_meta_corpus)
        
        
