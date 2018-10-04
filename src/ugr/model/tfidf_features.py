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


    def __init__(self, params):
        '''
        Constructor
        '''
        self.__vectorizer = None
        self.__features_weights = None
        
        
        
    def weight_features(self, raw_documents):
        """
        """
        min_gram = int(PropertiesManager.get_prop_value(PropertiesNames.MIN_GRAM))
        max_gram = int(PropertiesManager.get_prop_value(PropertiesNames.MAX_GRAM))
        ngrams = (min_gram, max_gram)
        self.__vectorizer = TfidfVectorizer(
            analyzer="word",
            tokenizer=lambda x: x,
            preprocessor=lambda x: x,
            token_pattern=None,
            ngram_range=ngrams,
            lowercase=None,
            )
        self.__features_weights = self.__vectorizer.fit_transform(raw_documents)
        
        
        
    def write_matlab_format(self, path):
        """
        """
        savemat(path, {"features":self.__features_weights})
        
        