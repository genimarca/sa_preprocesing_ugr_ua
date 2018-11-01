#!/usr/bin/python3
# *-* coding: utf-8 *-*
'''
Created on 4 oct. 2018

:author: Eugenio Martínez Cámara <emcamara@decsai.ugr.es>
'''

from abc import ABCMeta, abstractmethod

class ABSWeightFeatures(metaclass=ABCMeta):
    '''
    classdocs
    '''


    @abstractmethod
    def weight_features(self, raw_documents):
        """
        """
        
    @abstractmethod
    def write_matlab_format(self, path, processed_ids, processed_labels):
        """
        """