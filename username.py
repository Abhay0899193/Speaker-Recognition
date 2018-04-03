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
import mfeatures
import warnings
warnings.filterwarnings("ignore")
import pyaudio
import wave
def record():

    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 2
    RATE = 44100
    RECORD_SECONDS = 10
    WAVE_OUTPUT_FILENAME = "testfile.wav" 
    INPUT_DEVICE_INDEX=1
    
    p = pyaudio.PyAudio()
    
    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK,input_device_index=INPUT_DEVICE_INDEX)
    
    print("* recording")
    
    frames = []
    
    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)
    
    print("* done recording")
    
    stream.stop_stream()
    stream.close()
    p.terminate()
    
    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()


def test1():
    #source   = "testfile.wav"   
    modelpath = "models\\"       
    
    gmm_files = [os.path.join(modelpath,fname) for fname in 
                  os.listdir(modelpath) if fname.endswith('.gmm')]
    
    #Load the Gaussian gender Models
    models    = [pickle.load(open(fname,'rb')) for fname in gmm_files]
    speakers   = [fname.split("\\")[-1].split(".gmm")[0] for fname 
                  in gmm_files]
    # Read the test directory and get the list of test audio files 
      
        
         
    path="testfile.wav"
    #rate,sig = wav.read(source+path)
    rate,sig = wav.read(path)
    mfcc_feat=mfeatures.extract_features(sig,rate)
        
    log_likelihood = np.zeros(len(models)) 
        
    for i in range(len(models)):
        gmm    = models[i]  #checking with each model one by one
        scores = np.array(gmm.score(mfcc_feat))
        log_likelihood[i] = scores.sum()
        print(speakers[i]+str(log_likelihood[i]))
    winner = np.argmax(log_likelihood)
    z=speakers[winner]
    length=len(z)
    i=0
    while i<length:
     y=z[i]
     if y.isdigit():
        break
     i+=1
    result=z[0:i] 
    result=result.upper()
    return result
    
