#!
'''
Created on 4 oct. 2018

:author: Eugenio Martínez Cámara <emcamara@decsai.ugr.es>
'''

from ugr.model.feature_weights_names import FeatureWeightsNames

class FactoryWeightFeatures:
    '''
    classdocs
    '''


    @classmethod
    def creator(cls, feature_weights_name_key):
        cl = None
        if feature_weights_name_key in FeatureWeightsNames.__members__.keys():
            feature_weights_class_path = FeatureWeightsNames.__members__[feature_weights_name_key].value
            feature_weights_class_fields = feature_weights_class_path.rsplit(".", 1)
            module = __import__(feature_weights_class_fields[0], fromlist=feature_weights_class_fields[-1])
            cl = getattr(module, feature_weights_class_fields[-1])()
            
        return cl