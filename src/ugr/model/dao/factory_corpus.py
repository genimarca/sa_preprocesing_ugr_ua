#!/usr/bin/python3
# *-* coding: utf-8 *-*
'''
Created on 3 oct. 2018

:author: Eugenio Martínez Cámara <emcamara@decsai.ugr.es>
'''
from ugr.model.dao.corpus_names import CorpusNames

class FactoryCorpus(object):
    '''
    classdocs
    '''


    @classmethod
    def creator(cls, corpus_name):
        
        cl = None
        if corpus_name in CorpusNames.__members__.keys():
            corpus_class_path = CorpusNames.__members__[corpus_name]
            corpus_class_fields = corpus_class_path.rsplit(".", 1)
            module = __import__(corpus_class_fields[0], fromlist=corpus_class_fields[-1])
            cl = getattr(module, corpus_class_fields[-1])()
        
        return cl