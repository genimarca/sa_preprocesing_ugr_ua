#!/usr/bin/python3
# *-* coding: utf-8 *-*
'''
Created on 3 oct. 2018

:author: Eugenio Martínez Cámara <emcamara@decsai.ugr.es>
'''

from enum import Enum, unique

@unique
class PropertiesNames(Enum):
    
    ENCODING = "ENCODING"
    
    LANG = "LANG"
    
    NLP_LIBRARY_PATH = "NLP_LIBRARY_PATH"
    
    CORPUS_NAME = "CORPUS_NAME"
    
    CORPUS_PATH = "CORPUS_PATH"
    
    ALLOW_LABELS = "ALLOW_LABELS"
    
    PREPROCESSING = "PREPROCESSING"
    
    USE_STOPPER = "USE_STOPPER"
    
    USE_STEMMER = "USE_STEMMER"
    
    TO_LOWERCASE = "TO_LOWERCASE"
    
    TRANS_DIGITS = "TRANS_DIGITS"
    
    
        