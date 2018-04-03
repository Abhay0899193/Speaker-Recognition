# -*- coding: utf-8 -*-
"""
@author: GENESIS
"""
import numpy as np
import scipy
from python_speech_features import mfcc
from python_speech_features import logfbank
import scipy.io.wavfile as wav
from sklearn.mixture import GMM 
import pickle
import os
import warnings
import mfeatures
warnings.filterwarnings("ignore")


def traine(x):
    file_paths=open("development_set_enroll.txt" ,'w')
    i=1
    while i<6:
        file_paths.write(x+str(i)+".wav\n")
        i+=1
    file_paths.close()
     
    #path to training data
    source   = r"training_data/"
    #path where training speakers will be saved
    dest = r"models/"
    train_file = "development_set_enroll.txt"        
    file_paths = open(train_file,'r')
    
    count = 1
    # Extracting features for each speaker (5 files per speakers)
    features = np.asarray(())
    for path in file_paths:    
        path = path.strip()
        # read the audio
        rate,sig = wav.read(source+path)
        mfcc_feat=mfeatures.extract_features(sig,rate)
        # extract MFCC 
        
        if features.size == 0:
            features = mfcc_feat
        else:
            features = np.vstack((features, mfcc_feat))
        # when features of 5 files of speaker are concatenated, then do model training
        if count == 5:    
            gmm = GMM(n_components = 16, n_iter = 200, covariance_type='diag',n_init = 10)
            gmm.fit(features)
            
            # dumping the trained gaussian model
            picklefile = path.split("-")[0]+".gmm"
            pickle.dump(gmm,open(dest + picklefile,'wb'))
            features = np.asarray(())
            count = 0
        count = count + 1

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
