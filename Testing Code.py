# -*- coding: utf-8 -*-
# Testing Code

import os
import numpy as np
import IPython.display as ipd
import pickle
import librosa  
from scipy.io import wavfile #for audio processing
from pydub import AudioSegment

a = eval(input('Test from validation data -> 1 OR from a new file -> 2 ? '))

# Loading the Trained Model:
with open('model.pkl' , 'rb') as f:  
      classes2, x_val2, y_val2, model2 = pickle.load(f)
    
def predict(audio):
    prob=model2.predict(audio.reshape(1,8000,1))
    index=np.argmax(prob[0])
    return classes2[index]
    
if a==1:
    
    import random
    index=random.randint(0,len(x_val2)-1)
    samples=x_val2[index].ravel()
    print("Audio:",classes2[np.argmax(y_val2[index])])
    ipd.Audio(samples, rate=8000)
    print("Text:",predict(samples))
else:
    wav_path = input('path to audio <1 sec length file : ')
    sample_rate, samples = wavfile.read(wav_path)
    slic_len = float( (sample_rate - len(samples))/sample_rate) * 1000 + 10 #in milliseconds
 
    audio_out_file = wav_path[:-4]+"_silc.wav"
    
    # create 1 sec of silence audio segment
    one_sec_segment = AudioSegment.silent(duration = slic_len)   #duration in milliseconds
    
    #read wav file to an audio segment
    song = AudioSegment.from_wav(wav_path)
    
    #Add above two audio segments    
    final_song = song + one_sec_segment
    
    #Either save modified audio
    final_song.export(audio_out_file, format="wav")
    samples, sample_rate = librosa.load(audio_out_file , sr = 16000)
    samples = librosa.resample(samples, sample_rate, 8000)
    samples = samples[0:8000]
    all_wave = samples
    # all_label.append(label)
        
    all_wave = np.array(all_wave).reshape(-1,8000,1)
    print("Predicted Text:",predict(all_wave))
