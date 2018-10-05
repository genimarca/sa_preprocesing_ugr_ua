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
    
    USE_RAW_WORDS = "USE_RAW_WORDS"
    
    USE_LEMMA_WORDS = "USE_LEMMA_WORDS"
    
    USE_STEMMER_WORDS = "USE_STEMMER_WORDS"
    
    REMOVE_ACCENTS = "REMOVE_ACCENTS"
    
    USE_STOPPER = "USE_STOPPER"
    
    TO_LOWERCASE = "TO_LOWERCASE"
    
    TRANS_DIGITS = "TRANS_DIGITS"
    
    MIN_GRAM = "MIN_GRAM"
    
    MAX_GRAM = "MAX_GRAM"
    
    FEAUTRES_GENERATOR_NAME = "FEATURES_GENERATOR_NAME"
    
    FIELD_TO_PROCESS = "FIELD_TO_PROCESS" #title|body|title_body
    
    OUTPUT_MATLAB_PATH = "OUTPUT_MATLAB_PATH"
        