#!/usr/bin/python3
# *-* coding: utf-8 *-*
'''
Created on 1 oct. 2018

@author: Eugenio Martínez Cámara
'''
from ugr.model.dao.abs_corpus import ABSCorpus
from ugr.model.dao.document import Document
from collections import OrderedDict

class CorpusRestTripadvisor(ABSCorpus):
    '''Implementation of the abstract class ugr.model.dao.abs_corpus
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.__encoding = "utf-8"
        self.__allow_labels = None
        self.__corpus = OrderedDict()
        self.__doc_x_labels = None
        self.__SEP_CHAR = "\t"
        
        
    @property
    def allow_labels(self):
        """
        """
        return self.__allow_labels
        
        
    @allow_labels.setter
    def allow_labels(self, a_allow_labels):
        """
        """
        self.__allow_labels = a_allow_labels
        
    @property
    def encoding(self):
        """
        """
        return self.__encoding
        
    @encoding.setter
    def encoding(self, a_encoding):
        """
        """
        self.__encoding = a_encoding
        
    @property
    def corpus(self):
        """
        """
        return self.__corpus
        
    def doc_ids(self):
        """
        """
        
        return list(self.__corpus.keys())
        
    @property
    def doc_x_labels(self):
        """
        """
        if self.__doc_x_labels is None:
            self.__doc_x_labels = {self.__corpus[doc_id].raw_label:0 
                                   if self.__corpus[doc_id].raw_label not in self.__doc_x_labels else self.__doc_x_labels[self.__corpus[doc_id].raw_label]+1 
                                   for doc_id in self.__corpus.keys()}
            
        return self.__doc_x_labels
        
    
    def __remove_quotations(self, text):
        no_quatations = text
        if text[0] == "\"" and text[-1] == "\"":
            no_quatations = text[1:-1]
            
        return no_quatations
    
    def __add_document(self, line):
        """
        """
        doc = Document()
        doc.id = int(line[1][1:-1])
        doc.raw_title = self.__remove_quotations(line[2])
        doc.raw_body = self.__remove_quotations(line[4])
        doc.raw_label = int(line[3])
        doc.allow_label = self.__allow_labels.get_label_index(doc.raw_label)
        self.__corpus[doc.id] = doc
        print("INFO: READ doc: {}".format(doc.id))
        
    
    def load(self, path):
        """
        """
        with open(path, 'r', encoding=self.__encoding) as hand_file:
            hand_file.readline()
            own_split = str.split
            own_strip = str.strip
            for line in hand_file:
                line = own_split(own_strip(line), self.__SEP_CHAR)
                self.__add_document(line)
                
        
        
    def get_document(self, doc_id):
        """
        """
        return self.__corpus.get(doc_id, None)
        
    def get_size(self):
        """
        """
        return len(self.__corpus)
        
    def clear(self):
        """
        """
        self.__corpus.clear()
        