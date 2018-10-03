#!/usr/bin/python3
# *-* coding: utf-8 *-*
'''
Created on 27 sept. 2018

:author: Eugenio Martínez Cámara
'''

from abc import ABCMeta, abstractmethod

class ABSAllowLabels(metaclass=ABCMeta):
    '''
    classdocs
    '''


    def __init__(self, params):
        '''
        Sole constructor
        '''
        pass
    
    @property
    @abstractmethod
    def number_of_labels(self):
        """
        """
    
    
    @abstractmethod
    def label_index(self):
        """
        """
        
    @abstractmethod
    def get_label_index(self, raw_label):
        """
        """
        
    @abstractmethod
    def get_label_name(self, label_index):
        """
        """
        
    
    
    
        