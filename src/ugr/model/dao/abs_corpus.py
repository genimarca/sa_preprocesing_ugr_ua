#!/usr/bin/python3
# *-* coding: utf-8 *-*
'''
Created on 27 sept. 2018

@author: Eugenio Martínez Cámara
'''

from abc import ABCMeta, abstractmethod

class ABSCorpus(metaclass=ABCMeta):
    '''
    Abstra class for the defintiion of the method for a corpus
    '''

    @abstractmethod
    def __init__(self):
        '''
        Sole constructor
        '''


    @property
    @abstractmethod
    def allow_labels(self):
        """
        """
        
        
    @allow_labels.setter
    @abstractmethod
    def allow_labels(self, a_allow_labels):
        """
        """
        
    
    
        
    
        