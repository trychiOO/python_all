# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 11:52:00 2018

@author: soundai

"""

import wave
import numpy as np
import thinkdsp

class TestSignal:
    
    def __init__(self,fp = './' ,fn = 'SaiTest1111111.wav',fs = 16000):
        '''
        SaiTestWav Gen
        '''
        self.filepath = fp
        self.filename = fn
        self.fs =fs

    def data_readin(self,fp,fn):
        '''
        WAV/PCM audio data readin
        '''
        filepath = fp
        filename = fn
        wavread = wave.open(filepath + filename,'rb')
        fs = wavread.getframerate() #sampling freqency
        Nwavlen = wavread.getnframes() #num of total audio data points
        Nchannel = wavread.getnchannels() #num of channels
        wav_str = wavread.readframes(Nwavlen)
        wav_int = np.frombuffer(wav_str, dtype=np.int16)
        wav_data = np.reshape(wav_int,[Nwavlen,Nchannel]) #audio data on channels
        wav_data = wav_data/2**15
        return wav_data, fs, Nchannel

    
    def _chirp_gen(self,f1=100,f2=8000,duration=1,amp = 0.99):
        '''
        ExpoChirp_signal_gen
        '''
        signal = thinkdsp.ExpoChirp(f1,f2,amp) 
        wave = signal.make_wave(duration, 0, self.fs)
        return wave

    def _chirp_bank_gen(self):
        s1 = self._chirp_gen(amp =1)
        s2 = self._chirp_gen(amp =1/2)
        s3 = self._chirp_gen(amp =1/4)
        s4 = self._chirp_gen(amp =1/8)
        s5 = self._chirp_gen(amp =1/16)
        s1.zero_pad(2*self.fs)
        s2.zero_pad(2*self.fs)
        s3.zero_pad(2*self.fs)
        s4.zero_pad(2*self.fs)
        s5.zero_pad(2*self.fs)
        wave = s1.__or__(s2).__or__(s3).__or__(s4).__or__(s5)
        wave = wave.__or__(wave)
        return wave
    
    def _wgn_gen(self,duration=8):
        '''
        WhiteGuassianNoise_signal_gen
        '''
        signal = thinkdsp.UncorrelatedGaussianNoise(amp = 0.2)
        wave = signal.make_wave(duration,0,self.fs)
        wave.zero_pad(10*self.fs)
        return wave

    def _start_gen(self):
        ys,f,n = self.data_readin(self.filepath , 'sai_start.wav')
        wave = thinkdsp.Wave(ys[:,0],framerate = self.fs)
        wave.zero_pad(10*self.fs)
        return wave
    
    def _voice_gen(self):
        ys,f,n = self.data_readin(self.filepath , 'sai_voice.wav')
        wave = thinkdsp.Wave(ys[:,0],framerate = self.fs)
        wave.zero_pad(10*self.fs)
        return wave

    def _music_gen(self):
        ys,f,n = self.data_readin(self.filepath , 'sai_music.wav')
        wave = thinkdsp.Wave(ys[:,0],framerate = self.fs)
        wave.zero_pad(60*self.fs)
        return wave

    def _end_gen(self):
        ys,f,n = self.data_readin(self.filepath , 'sai_end.wav')
        wave = thinkdsp.Wave(ys[:,0],framerate = self.fs)
        wave.zero_pad(2*self.fs)
        return wave    
       
    
    
# =============================================================================
# Test Signal Defination
# =============================================================================
def main():
    
    str_id = '0111111'
#    ERLE/NL/DLY/COH/FR/DIS/CONS    fs = 16000

    fp = './'    
    fn = 'HelloWorld'+str_id+'.wav'
    s = TestSignal(fp,fn,fs)     
    
    slice1 = s._start_gen()
    slice2 = s._end_gen()
    if((str_id[2]=='1')|(str_id[4]=='1')|(str_id[5]=='1')|(str_id[6]=='1')):
        slice1 = slice1.__or__(s._chirp_bank_gen())
        slice2 = s._chirp_bank_gen().__or__(slice2)
    if(str_id[0]=='1'):
        slice1 = slice1.__or__(s._voice_gen()).__or__(s._music_gen())
    if(str_id[3]=='1'):
        slice1 = slice1.__or__(s._wgn_gen())
         
    wav_joint = slice1.__or__(slice2)
    wav_joint.write(filename=fn)
if __name__=='__main__': 
    main()






