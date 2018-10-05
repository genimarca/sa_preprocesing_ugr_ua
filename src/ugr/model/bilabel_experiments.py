#!/usr/bin/python3
# *-* coding: utf-8 *-*
'''
Created on 3 oct. 2018

:author: Eugenio Martínez Cámara <emcamara@decsai.ugr.es>
'''
from ugr.model.abs_allow_labels import ABSAllowLabels



class BilabelExperiments(ABSAllowLabels):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        
        self.__number_of_labels = 2
        self.__labels = {
            0:("NEGATIVE",[-1,1,2]),
            1:("POSITIVE",[5,4,"5","4"])
            }
        
    @property
    def number_of_labels(self):
        """
        """
        return self.__number_of_labels
    
    
    def label_index(self):
        """
        """
        return list(self.__labels.keys())
        
    def get_label_index(self, raw_label):
        """It returns NONE in case the @raw_label is not allowed.
        
        """
        
        i=0
        stop=False
        label_index=None
        while i < self.__number_of_labels and not stop:
            if raw_label in self.__labels[i][-1]:
                label_index = i
                stop = True
            else:
                i+=1
                
        return label_index
        
        
    def get_label_name(self, label_index):
        """
        """
        
        label_name = None
        if label_index in self.__labels:
            label_name = self.__labels[label_index][0]
        
        return label_name
        
        
        
        