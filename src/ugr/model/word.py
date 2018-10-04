#!/usr/bin/python3
# *-* coding: utf-8 *-*

'''
Created on 3 oct. 2018

:author: Eugenio Martínez Cámara <emcamara@decsai.ugr.es>
'''

class Word:
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.__w_raw_form = None
        self.__w_raw_form_no_accent = None
        self.__w_raw_form_lc = None
        self.__w_raw_form_lc_no_accent = None
        self.__w_lemma = None
        self.__w_lemma_no_accent = None
        self.__w_stem = None
        self.__is_digit = False
        self.__is_stopword = False
        
        
        
    @property
    def w_raw_form(self):
        return self.__w_raw_form
    
    @w_raw_form.setter
    def w_raw_form(self, a_w_raw_form):
        self.__w_raw_form = a_w_raw_form
        
    @property
    def w_raw_form_no_accent(self):
        return self.__w_raw_form_no_accent
    
    @w_raw_form_no_accent.setter
    def w_raw_form_no_accent(self, a_w_raw_form_no_accent):
        self.__w_raw_form_no_accent = a_w_raw_form_no_accent
        
    @property
    def w_raw_form_lc(self):
        return self.__w_raw_form_lc
    
    @w_raw_form_lc.setter
    def w_raw_form_lc(self, a_w_raw_form_lc):
        self.__w_raw_form_lc = a_w_raw_form_lc
        
    @property
    def w_raw_form_lc_no_accent(self):
        return self.__w_raw_form_lc_no_accent
    
    @w_raw_form_lc_no_accent.setter
    def w_raw_form_lc_no_accent(self, a_w_raw_form_lc_no_accent):
        self.__w_raw_form_lc_no_accent = a_w_raw_form_lc_no_accent
        
    @property
    def w_lemma(self):
        return self.__w_lemma
    
    @w_lemma.setter
    def w_lemma(self, a_w_lemma):
        self.__w_lemma = a_w_lemma
        
    @property
    def w_lemma_no_accent(self):
        return self.__w_lemma_no_accent
    
    @w_lemma_no_accent.setter
    def w_lemma_no_accent(self, a_w_lemma_no_accent):
        self.__w_lemma_no_accent = a_w_lemma_no_accent
        
    @property
    def w_stem(self):
        return self.__w_stem
    
    @w_stem.setter
    def w_stem(self, a_w_stem):
        self.__w_stem = a_w_stem        
        
    @property
    def is_digit(self):
        return self.__is_digit
    
    @is_digit.setter
    def is_digit(self, a_is_digit):
        self.__is_digit = a_is_digit
        
    @property
    def is_stopword(self):
        return self.__is_stopword
    
    @is_stopword.setter
    def is_stopword(self, a_is_stopword):
        self.__is_stopword = a_is_stopword
        
    @classmethod
    def raw_form(cls, word):
        return word.w_raw_form
    
    @classmethod
    def raw_form_no_accent(cls, word):
        return word.w_raw_form_no_accent
    
    @classmethod
    def raw_form_lc(cls, word):
        return word.w_raw_form_lc
    
    @classmethod
    def raw_form_lc_no_accent(cls, word):
        return word.w_raw_form_lc_no_accent
    
    @classmethod
    def lemma(cls, word):
        return word.w_lemma
    
    @classmethod
    def lemma_no_accent(cls, word):
        return word.w_lemma_no_accent
    
    @classmethod
    def stem(cls, word):
        return word.w_stem