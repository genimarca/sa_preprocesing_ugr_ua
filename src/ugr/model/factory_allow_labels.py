#!/usr/bin/python3
# *-* coding: utf-8 *-*
'''
Created on 3 oct. 2018

:author: Eugenio Martínez Cámara <emcamara@decsai.ugr.es>
'''
from ugr.model.allow_labels_names import AllowLabelsName

class FactoryAllowLabels:
    '''
    classdocs
    '''


    @classmethod
    def creator(cls, allow_labels_name_key):
        cl = None
        if allow_labels_name_key in AllowLabelsName.__members__.keys():
            allow_labels_class_path = AllowLabelsName.__members__[allow_labels_name_key].value
            allow_labels_class_fields = allow_labels_class_path.rsplit(".", 1)
            module = __import__(allow_labels_class_fields[0], fromlist=allow_labels_class_fields[-1])
            cl = getattr(module, allow_labels_class_fields[-1])()
            
        return cl