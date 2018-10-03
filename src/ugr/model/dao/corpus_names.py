'''
Created on 3 oct. 2018

:author: Eugenio Martínez Cámara <emcamara@decsai.ugr.es>
'''

from enum import Enum, unique

@unique
class CorpusNames(Enum):
    
    
    REST_TRIP_CHILE = "ugr.model.dao.corpus_rest_tripadvisor_chile.CorpusRestTripadvisor"
    
    MUCHOCINE = "ugr.model.dao.corpus_muchocine.CorpusMuchoCine"
    
    COAH = "ugr.model.dao.corpus_coah.CorpusCOAH"
        