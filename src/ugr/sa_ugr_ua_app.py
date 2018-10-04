#!/usr/bin/python3
# *-* coding: utf-8 *-*

'''
Created on 4 oct. 2018

@author: Eugenio Martínez Cámara <emcamara@decsai.ugr.es>
'''

from ugr.model.model_pipeline import ModelPipeline

import sys

if __name__ == '__main__':
    
    
    if len(sys.argv) != 2:
        print("The input must be: sa_ugr_ua_app conf_path")
    else:
        model = ModelPipeline()
        model.initilization(sys.argv[1])
        model.proc_pipeline()
        print("Goodbye")