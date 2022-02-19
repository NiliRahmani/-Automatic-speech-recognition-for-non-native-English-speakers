# -*- coding: utf-8 -*-
# code which converts all audio files into 1 second length files and saves them.

import os
import librosa   #for audio processing
import IPython.display as ipd
import matplotlib.pyplot as plt
import numpy as np
from scipy.io import wavfile #for audio processing
import warnings
from math import floor

from pydub import AudioSegment
from pydub.playback import play

import pickle

warnings.filterwarnings("ignore")
train_audio_path = 'F:\\Niloo\\freelancer\\python_codes\\audio_2'  # Replace the directory of word folders in your PC

labels=os.listdir(train_audio_path) 

for label in labels:
    waves = [f for f in os.listdir(train_audio_path + '\\'+ label) if f.endswith('.wav')]
    for wav in waves:  
        try:
            #---------------------------------------
            # train_audio_path = 'F:\\Niloo\\freelancer\\python_codes\\audio_2\\around\\1_A.wav'    
            # audio_in_file = "in_sine.wav"
            sample_rate, samples = wavfile.read(train_audio_path + '\\' + label + '\\' + wav)
            slic_len = float( (sample_rate - len(samples))/sample_rate) * 1000 + 10 #in milliseconds
         
            audio_out_file = train_audio_path + '\\'+ label+'\\'+ 'WithScilence'+'\\'+wav[:-4]+"_silc.wav"
            
            # create 1 sec of silence audio segment
            one_sec_segment = AudioSegment.silent(duration = floor(slic_len/2))   #duration in milliseconds
            one_sec_segment2 = AudioSegment.silent(duration = floor(slic_len/2))  #duration in milliseconds
            
            #read wav file to an audio segment
            song = AudioSegment.from_wav(train_audio_path + '\\' + label + '\\' + wav)
            
            #Add above two audio segments    
            final_song = one_sec_segment + song + one_sec_segment2
            
            try:
                #Either save modified audio
                final_song.export(audio_out_file, format="wav")
            except:
                os.mkdir( train_audio_path + '\\'+ label + '\\' + 'WithScilence' )
                final_song.export(audio_out_file, format="wav")
                
            # sample_rate2, samples2 = wavfile.read(audio_out_file)
            
            #---------------------------------------
        except:
                print(wav) 

for label in labels:
    waves = [f for f in os.listdir(train_audio_path + '\\'+ label) if f.endswith('.wav')]
    for wav in waves:  
        try:
            #---------------------------------------
            # train_audio_path = 'F:\\Niloo\\freelancer\\python_codes\\audio_2\\around\\1_A.wav'    
            # audio_in_file = "in_sine.wav"
            sample_rate, samples = wavfile.read(train_audio_path + '\\' + label + '\\' + wav)
            slic_len = float( (sample_rate - len(samples))/sample_rate) * 1000 + 10
         
            audio_out_file = train_audio_path + '\\'+ label+'\\'+ 'WithScilence'+'\\'+wav[:-4]+"_silc1.wav"
            audio_out_file2 = train_audio_path + '\\'+ label+'\\'+ 'WithScilence'+'\\'+wav[:-4]+"_silc2.wav"
            
            # create 1 sec of silence audio segment
            one_sec_segment = AudioSegment.silent(duration = slic_len)  #duration in milliseconds
            # one_sec_segment2 = AudioSegment.silent(duration = floor(slic_len/2))  #duration in milliseconds
            
            #read wav file to an audio segment
            song = AudioSegment.from_wav(train_audio_path + '\\' + label + '\\' + wav)
            
            #Add above two audio segments    
            final_song = one_sec_segment + song 
            final_song2 = song + one_sec_segment
            # try:
            #Either save modified audio
            final_song.export(audio_out_file, format="wav")
            final_song2.export(audio_out_file2, format="wav")
            # except:
            #     os.mkdir( train_audio_path + '\\'+ label + '\\' + 'WithScilence' )
            #     final_song.export(audio_out_file, format="wav")
                
            # sample_rate2, samples2 = wavfile.read(audio_out_file)
            
            # #Or Play modified audio
            # play(final_song)
            #---------------------------------------
        except:
                print(wav) 

