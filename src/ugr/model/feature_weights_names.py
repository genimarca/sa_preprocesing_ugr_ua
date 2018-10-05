#!/usr/bin/python3
# *-* coding: utf-8 *-*
'''
Created on 4 oct. 2018

:author: Eugenio Martínez Cámara <emcamara@decsai.ugr.es>
'''

from enum import Enum, unique

class FeatureWeightsNames(Enum):
    '''
    classdocs
    '''


    FREQ_WEIGHTS = "ugr.model.frequency_features.FrequencyFeatures"
    
    TFIDF_WEIGHTS = "ugr.model.tfidf_features.TFIDFFeatures"
        