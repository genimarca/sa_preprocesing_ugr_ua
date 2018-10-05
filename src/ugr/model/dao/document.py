#!/usr/bin/python3
# *-* coding: utf-8 *-*

'''
Created on 27 sept. 2018

@author: Eugenio Martínez Cámara
'''

class Document:
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.__id = ""
        self.__raw_title = ""
        self.__raw_body = ""
        self.__proc_title = ""
        self.__proc_body = ""
        self.__raw_label = None
        self.__allow_label = None
        
        
    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id (self, a_id):
        self.__id = a_id
        
    @property
    def raw_title(self):
        return self.__raw_title
    
    @raw_title.setter
    def raw_title(self, a_raw_title):
        self.__raw_title = a_raw_title
        
    @property
    def raw_body(self):
        return self.__raw_body
    
    @raw_body.setter
    def raw_body(self, a_raw_body):
        self.__raw_body = a_raw_body
        
    @property
    def proc_title(self):
        return self.__proc_title
    
    @proc_title.setter
    def proc_title(self, a_proc_title):
        self.__proc_title = a_proc_title
    
    @property
    def proc_body(self):
        return self.__proc_body
    
    @proc_body.setter
    def proc_body(self, a_proc_body):
        self.__proc_body = a_proc_body
    
    @property
    def raw_label(self):
        return self.__raw_label
    
    @raw_label.setter
    def raw_label(self, a_raw_label):
        self.__raw_label = a_raw_label
        
    @property
    def allow_label(self):
        return self.__allow_label
    
    @allow_label.setter
    def allow_label(self, a_allow_label):
        self.__allow_label = a_allow_label
        