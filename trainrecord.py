# -*- coding: utf-8 -*-
"""
Created on Fri Mar 23 14:01:58 2018

@author: Lagolas
"""

import pyaudio
import wave
import os.path


def testr(x,RECORD_SECONDS = 31):
        CHUNK = 1024
        FORMAT = pyaudio.paInt16
        CHANNELS = 2
        RATE = 44100
        i=1
        while("TRUE"):
            fname="training_data\\"+x+str(i)+".wav"
            if os.path.isfile(fname):
                i+=1
            else:
                break
        fname ="training_data\\"+x+str(i)+".wav"
        INPUT_DEVICE_INDEX=0
        
        p = pyaudio.PyAudio()
        
        stream = p.open(format=FORMAT,
                        channels=CHANNELS,
                        rate=RATE,
                        input=True,
                        frames_per_buffer=CHUNK,input_device_index=INPUT_DEVICE_INDEX)
        
        print("* recording")
        
        frames = []
        
        for i in range(0, int(RATE / CHUNK * int(RECORD_SECONDS))):
            data = stream.read(CHUNK)
            frames.append(data)
        
        print("* done recording")
        
        stream.stop_stream()
        stream.close()
        p.terminate()
        
        wf = wave.open(fname, 'wb')
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(p.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))
        wf.close()
        i+=1
        return fname
