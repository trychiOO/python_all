# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 14:52:42 2018

@author: SoundAI
"""
import os
import shutil
#import datetime
import wave
import numpy as np
import samplerate
import thinkdsp
from scipy import signal
from numpy.fft import fft,ifft
import matplotlib.pyplot as plt
np.seterr(divide='ignore', invalid='ignore')



plt.close('all')
#starttime = datetime.datetime.now()
class TestCase:
    filepath = r'./'
    sndname =  'SaiSND2.wav'   # 'snd' corresponds to Send Signal to SPK
    rcvname =  'SaiSND2_100_SoundPI.wav'   # 'rcv' corresponds to Receive Signal at MIC ARRAY
    micseq = [1,2,3,4,5,6]
    refseq = [8]
    init_t = 15
    # Parameters Initialization
    sndstart = micstart = refstart = \
    sndmono = micmono = refmono = \
    sndchirp1 = micchirp1 = refchirp1 = \
    sndvoice = micvoice = refvoice = \
    sndmusic = micmusic = refmusic = \
    sndnoise = micnoise = refnoise = \
    sndchirp2 = micchirp2 = refchirp2 = \
    sndend = micend = refend = \
    snddata = rcvdata = micdata = refdata =    np.array([])
    fs = rcvfs= sndNch = rcvNch =     int()
    
    def __init__(self):   
        '''
        NOTE:  
        SAVED AUDIO FILE SHOULD BE  -- 16bit PCM or PCM-CODED-WAV --
        WITH SAMPLING FREQUENCY BEYOND 16KHZ
        '''
        self.snddata,self.fs,self.sndNch = self._data_readin(self.filepath, self.sndname)
        self.rcvdata,self.rcvfs,self.rcvNch = self._data_readin(self.filepath, self.rcvname)
        #downsampling when SaiResult signal fs exceeds 16kHz
        if(self.rcvfs != self.fs):
            self.rcvdata = samplerate.resample(self.rcvdata,np.float(self.rcvfs/self.fs),'sinc_best')      
            self.rcvfs = self.fs
        #oops! To make sure data structure conistence to init with 1st colum data
        self.micdata = self.rcvdata[:,self.micseq[0]-1].reshape(len(self.rcvdata[:,self.micseq[0]-1]),1)
        #mic channel rereanked
        for i in range(1,len(self.micseq)):
            tmp = self.rcvdata[:,self.micseq[i]-1].reshape(len(self.rcvdata[:,self.micseq[i]-1]),1)
            self.micdata = np.concatenate((self.micdata,tmp),1)
        #ref channel reranked
        if (len(self.refseq) == 1):
            self.refdata = self.rcvdata[:,self.refseq[0]-1].reshape(len(self.rcvdata[:,self.refseq[0]-1]),1)
        else:
            self.refdata = self.rcvdata[:,self.refseq[0]-1].reshape(len(self.rcvdata[:,self.refseq[0]-1]),1)
            for i in range(1,len(self.refseq)):
                tmp = self.rcvdata[:,self.refseq[i]-1].reshape(len(self.rcvdata[:,self.refseq[i]-1]),1)
                self.refdata = np.concatenate((self.refdata,tmp),1)
        # micsig and refsig alignment
        snd_slice = self.snddata[0:self.init_t*self.fs,0]
        mic_slice = self.micdata[0:self.init_t*self.fs,0]
        ref_slice = self.refdata[0:self.init_t*self.fs,0]

        lagseq_mic = self._fft_xcorr(snd_slice, mic_slice)
        lagseq_ref = self._fft_xcorr(snd_slice, ref_slice)
        # data split 
        self._data_split(lagseq_mic,lagseq_ref)
                
    def _data_readin(self,fp,fn):
        '''
        WAV/PCM audio data readin
        INPUT:
        fp : file_path
        fn : file_name
        RETURN:
        wav_data , fs, Nchannel
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
    
    def _fft_xcorr(self,x,y):
        '''
        More Effective cross-corelation calc method
        Note: x should be longer than y
        '''
        N1 = len(x)
        N2 = len(y)
        y = np.pad(y,(0,N1-N2),'constant')
        xx = np.pad(x,(0,N1),'constant')
        yy = np.pad(y,(0,N1),'constant')    
        yy_inv = np.flipud(yy)
        corrs = ifft(fft(xx)*fft(yy_inv)).real
    
        return corrs    
    
    def _data_split(self,micseqlag,refseqlag):
        '''
        SaiSND and SaiRCV signal splited int special slices for further analysis
        '''
        print('MIC channell received signals are ',(refseqlag.argmax() - micseqlag.argmax())/16,'ms delayed \
               with the REF channel, totally',refseqlag.argmax() - micseqlag.argmax(),'sampling points')
        miclag = 2*self.init_t*self.fs - micseqlag.argmax()
        reflag = 2*self.init_t*self.fs - micseqlag.argmax()
        self.sndstart = self.snddata[0:11*self.fs,:]
        self.micstart = self.micdata[miclag:miclag+11*self.fs,:]
        self.refstart = self.refdata[reflag:reflag+11*self.fs,:]
        self.sndsilence = self.snddata[11*self.fs:14*self.fs,:]  
        self.micsilence = self.micdata[miclag+11*self.fs:miclag+14*self.fs,:]
        self.refsilence = self.refdata[reflag+11*self.fs:reflag+14*self.fs,:]
        self.sndmono = self.snddata[15*self.fs:18*self.fs,:]        
        self.micmono = self.micdata[miclag+15*self.fs:miclag+18*self.fs,:]
        self.refmono = self.refdata[reflag+15*self.fs:reflag+18*self.fs,:]
        self.sndchirp1 = self.snddata[20*self.fs:40*self.fs,:]        
        self.micchirp1 = self.micdata[miclag+20*self.fs:miclag+40*self.fs,:]
        self.refchirp1 = self.refdata[reflag+20*self.fs:reflag+40*self.fs,:]
        self.sndvoice = self.snddata[40*self.fs:43*self.fs,:]        
        self.micvoice = self.micdata[miclag+40*self.fs:miclag+43*self.fs,:]
        self.refvoice = self.refdata[reflag+40*self.fs:reflag+43*self.fs,:]
        self.sndmusic = self.snddata[45*self.fs:104*self.fs,:]        
        self.micmusic = self.micdata[miclag+45*self.fs:miclag+104*self.fs,:]
        self.refmusic = self.refdata[reflag+45*self.fs:reflag+104*self.fs,:]
        self.sndnoise = self.snddata[105*self.fs:135*self.fs,:]        
        self.micnoise = self.micdata[miclag+105*self.fs:miclag+135*self.fs,:]
        self.refnoise = self.refdata[reflag+105*self.fs:reflag+135*self.fs,:]
        self.sndchirp2 = self.snddata[137*self.fs:157*self.fs,:]        
        self.micchirp2 = self.micdata[miclag+137*self.fs:miclag+157*self.fs,:]
        self.refchirp2 = self.refdata[reflag+137*self.fs:reflag+157*self.fs,:]

    def _data_write(self,fp,fn,data,nchannels =1):
        '''
        WAV/PCM audio data write into file
        '''
        f1 = wave.open(fp +fn,'wb')
        f1.setframerate(self.fs)
        f1.setsampwidth(2)
        f1.setnchannels(nchannels)
        wav_vad = data[0:len(data),:].astype(np.int16)
        f1.writeframes(wav_vad.tostring())
        f1.close()
        
    def _data_enframe(self,sig,frame_len,frame_inc,window = 'Hamming',pre_emph_coeff = 0.97):
        '''
        Wavedata truncated into frames with pre-empasizing and windowing
        '''
        sig_len = len(sig)
        if  sig_len < frame_len:
            frame_num = 1
        else:
            frame_num = int(np.ceil((sig_len-frame_len+frame_inc)/frame_inc))
        #    pad_points = frame_inc*frame_num+ frame_len -sig_len
        #    sig = np.concatenate(sig, np.zeros(pad_points))
        sig_matrix = np.zeros([frame_num, frame_len])
        if (window =='Hamming'):
            window_h = np.hamming(frame_len)
        if (window =='Hanning'):
            window_h = np.hanning(frame_len)
       
        for i in range(frame_num):
            single_frame= sig[ (i*frame_len-i*frame_inc) : (i+1)*frame_len-i*frame_inc] #truncated
            single_frame = np.append(single_frame[0], single_frame[:-1] - pre_emph_coeff * single_frame[1:])  #pre-empasizing
            single_frame = window_h * single_frame # windowing
            sig_matrix[i,:] = single_frame      
            
        return frame_num , sig_matrix

    def _aec_exec(self,fmic1,fmic2,fref1,fref2,num):
        if (len(self.refseq) == 1):
            aec_process1 = r'.\sai_aec_process_1spk.exe '+fmic1+' '+fref1+' '+self.filepath +'result/present/aec_calc/voice_after_aec'+str(num+1)+'.wav'
            aec_process2 = r'.\sai_aec_process_1spk.exe '+fmic2+' '+fref2+' '+self.filepath +'result/present/aec_calc/music_after_aec'+str(num+1)+'.wav'
        elif (len(self.refseq) == 2): 
            aec_process1 = r'.\sai_aec_process_2spk.exe '+fmic1+' '+fref1+' '+self.filepath +'result/present/aec_calc/voice_after_aec'+str(num+1)+'.wav'
            aec_process2 = r'.\sai_aec_process_2spk.exe '+fmic2+' '+fref2+' '+self.filepath +'result/present/aec_calc/music_after_aec'+str(num+1)+'.wav'
        os.system(aec_process1)
        os.system(aec_process2)

    def _erle_calc(self,x,y):
        x_Nframe , x_reshape = self._data_enframe(x,256,128)
        y_Nframe , y_reshape = self._data_enframe(y,256,128)
        STEx = np.zeros(x_Nframe)
        STEy = np.zeros(y_Nframe)
        for i in range(x_Nframe):
#            x_reshape[i,:] = x_reshape[i,:]/x_reshape.max()
            STEx[i] = np.sum(x_reshape[i,:] * x_reshape[i,:])
#            y_reshape[i,:] = y_reshape[i,:]/y_reshape.max()
            STEy[i] = np.sum(y_reshape[i,:] * y_reshape[i,:])
        tseq = np.arange(128/self.fs,len(x)/self.fs,128/self.fs)
        return tseq, STEx , STEy

    def _freq_calc(self,x,y):
        spectrum_y = y.make_spectrum()
        spectrum_y.amps[0:200] =np.zeros(200) 
        spectrum_x = x.make_spectrum()
        spectrum_x.amps[0:200] =np.ones(200) 
        spectrum_h = spectrum_y.__mul__(spectrum_x.invert())            
        wav_ir = spectrum_h.make_wave()
        wav_ir.ys = abs(wav_ir.ys)
#        if(self._fft_xcorr(x.ys,y.ys).argmax() > len(x) ):
#            print('Warning: Encountering NonCausal Data Split check the data Cutting Off')
        N_init = wav_ir.ys.argmax()
        wav_ir.ys[:] = np.append(wav_ir.ys[N_init:len(wav_ir.ys)],wav_ir.ys[0:N_init])
#        plt.figure()
#        plt.plot(wav_ir.ts, wav_ir.ys)
        wav_ir_fund = wav_ir.slice(0,int(0.005*self.fs))
        spectrum_tf_fund = wav_ir_fund.make_spectrum()
#        plt.figure()
#        plt.semilogx(spectrum_tf_fund.fs,20*np.log10(spectrum_tf_fund.amps))
        return spectrum_tf_fund.fs ,spectrum_tf_fund.amps
    
    def _thd_calc(self,x,y):
        spectrum_y = y.make_spectrum()
        spectrum_y.amps[0:200] =np.zeros(200) 
        spectrum_x = x.make_spectrum()
        spectrum_x.amps[0:200] =np.ones(200) 
        spectrum_h = spectrum_y.__mul__(spectrum_x.invert())            
        wav_ir = spectrum_h.make_wave()
        wav_ir.ys = abs(wav_ir.ys)  
#        if(self._fft_xcorr(x.ys,y.ys).argmax() > len(x) ):
#            print('Warning: Encountering NonCausal Data Split check the data Cutting Off')
        N_init = wav_ir.ys.argmax()
        wav_ir.ys[:] = np.append(wav_ir.ys[N_init:len(wav_ir.ys)],wav_ir.ys[0:N_init])
        wav_ir_fund = wav_ir.slice(0,int(0.005*self.fs)) 
        spectrum_fund = wav_ir_fund.make_spectrum()
        wav_ir_2nd = wav_ir.slice(int(1.84*self.fs),int(1.86*self.fs))
        wav_ir_3rd = wav_ir.slice(int(1.74*self.fs),int(1.76*self.fs))
        wav_ir_4th = wav_ir.slice(int(1.68*self.fs),int(1.70*self.fs))
        wav_ir_5th = wav_ir.slice(int(1.63*self.fs),int(1.65*self.fs))
        spectrum_tf_2nd = wav_ir_2nd.make_spectrum()
        amp_2nd = spectrum_tf_2nd.amps [np.arange(1,len(spectrum_tf_2nd),2)]
#        fs_2nd = spectrum_tf_2nd.fs[0:len(amp_2nd)]
#        spectrum_2nd = thinkdsp.Spectrum(amp_2nd,fs_2nd,framerate=self.fs,full=False)
        spectrum_tf_3rd = wav_ir_3rd.make_spectrum()
        amp_3rd = spectrum_tf_3rd.amps [np.arange(1,len(spectrum_tf_3rd),3)]
#        fs_3rd = spectrum_tf_3rd.fs[0:len(amp_3rd)]
#        spectrum_3rd = thinkdsp.Spectrum(amp_3rd,fs_3rd,framerate=self.fs,full=False)
        spectrum_tf_4th = wav_ir_4th.make_spectrum()
        amp_4th = spectrum_tf_4th.amps [np.arange(1,len(spectrum_tf_4th),4)]
#        fs_4th = spectrum_tf_4th.fs[0:len(amp_4th)]
#        spectrum_4th = thinkdsp.Spectrum(amp_4th,fs_4th,framerate=self.fs,full=False)
        spectrum_tf_5th = wav_ir_5th.make_spectrum()
        amp_5th = spectrum_tf_5th.amps [np.arange(1,len(spectrum_tf_5th),5)]
        fs_5th = spectrum_tf_5th.fs[0:len(amp_5th)]
#        spectrum_5th = thinkdsp.Spectrum(amp_5th,fs_5th,framerate=self.fs,full=False)
        
        a = np.square(spectrum_fund.amps[0:len(amp_5th)])
        b = np.square(amp_2nd[0:len(amp_5th)])
        c = np.square(amp_3rd[0:len(amp_5th)])
        d = np.square(amp_4th[0:len(amp_5th)])
        e = np.square(amp_5th[0:len(amp_5th)])
        thd = np.sqrt((b+c+d+e)/(a+b+c+d+e))
#        thd_odd  = np.sqrt((c+e)/(a+b+c+d+e))
#        thd_even = np.sqrt((b+d)/(a+b+c+d+e))
        
        return fs_5th, thd             

    def data_display(self,casename):
        '''
        TEST SIGNAL SPLIT INTO FRAGMENTS AND DATA SHOW OFF 
        '''
        filename1 = 'result/' + casename +'/snd'+casename+'.wav'
        filename2 = 'result/' + casename +'/mic'+casename+'.wav'
        filename3 = 'result/' + casename +'/ref'+casename+'.wav'
        if(os.path.exists(self.filepath +'result/' +casename+'/')):
            shutil.rmtree(self.filepath +'result/'+casename+'/')
        if not(os.path.exists(self.filepath +'result/' +casename+'/')):
            os.makedirs(self.filepath +'result/' + casename)
        
        self._data_write(self.filepath,filename1,eval('self.snd' +casename)* 2**15,1)
        self._data_write(self.filepath,filename2,eval('self.mic' +casename)* 2**15,nchannels=len(self.micseq))
        self._data_write(self.filepath,filename3,eval('self.ref' +casename)* 2**15,nchannels=len(self.refseq))
        
    def aec_calc(self):
        '''
        ERLE Calc for voice and music signals
        '''
        #channels splited and data saved into files
        self.data_display('voice')
        self.data_display('music')
        if(os.path.exists(self.filepath +'result/present/aec_calc/')):
            shutil.rmtree(self.filepath +'result/present/aec_calc/')   
        os.mkdir(self.filepath +'result/present/aec_calc/')        
        a = self._data_readin(self.filepath,'result/voice/micvoice.wav')
        b = self._data_readin(self.filepath,'result/voice/refvoice.wav')
        c = self._data_readin(self.filepath,'result/music/micmusic.wav')
        d = self._data_readin(self.filepath,'result/music/refmusic.wav')    
        plt.figure('aec_process')
        AEC_txt = open(r'Result_AEC.txt','w+')
        AEC_txt1 = open(r'Result_AEC1.txt','w+')
        for i in range(len(self.micseq)):
            self._data_write(self.filepath,'result/present/aec_calc/voice_before_aec'+str(i+1)+'.wav',a[0][:,i].reshape(len(a[0][:,0]),1)*2**15,1)
            self._data_write(self.filepath,'result/present/aec_calc/music_before_aec'+str(i+1)+'.wav',c[0][:,i].reshape(len(c[0][:,0]),1)*2**15,1)
            self._data_write(self.filepath,'result/present/aec_calc/voice_before_aec_ref.wav',b[0][:,:].reshape(len(b[0][:,0]),len(self.refseq))*2**15,len(self.refseq))
            self._data_write(self.filepath,'result/present/aec_calc/music_before_aec_ref.wav',d[0][:,:].reshape(len(d[0][:,0]),len(self.refseq))*2**15,len(self.refseq))  
    
    
            fmic1 = self.filepath+'result/present/aec_calc/voice_before_aec'+str(i+1) +'.wav'
            fref1 = self.filepath+'result/present/aec_calc/voice_before_aec_ref' +'.wav'
            fmic2 = self.filepath+'result/present/aec_calc/music_before_aec'+str(i+1) +'.wav'
            fref2 = self.filepath+'result/present/aec_calc/music_before_aec_ref' +'.wav'
            self._aec_exec(fmic1,fmic2,fref1,fref2,i)
            # ERLE calc
            af = self._data_readin(self.filepath,'result/present/aec_calc/voice_after_aec'+str(i+1) +'.wav')
            cf = self._data_readin(self.filepath,'result/present/aec_calc/music_after_aec'+str(i+1) +'.wav')
            tseqv,STEv1,STEv2 = self._erle_calc(a[0][:,i],af[0][:,0])
            tseqm,STEm1,STEm2 = self._erle_calc(c[0][:,i],cf[0][:,0])
            STEm1in_sum = sum(abs(STEm1 - np.mean(STEm1)))
            STEm1out_sum = sum(abs(STEm2)) 
            AEC_result = 20*np.log10(STEm1in_sum/STEm1out_sum)
            print(i+1,'# AEC_result =',AEC_result)
            ERLEv = 10*np.log10(STEv1/STEv2)
            ERLEm = 10*np.log10(STEm1/STEm2)
            ERLEm1 = ERLEm[5000:7200]
            ERLEmean = np.mean(ERLEm1) 
            AEC_txt.write(str(i+1)+'# ERLE '+str(ERLEmean)+'\n')
            AEC_txt1.write(str(i+1)+' '+str(ERLEmean)+'\n') 
            print(i+1,'# ERLE=', ERLEmean)
            if(ERLEmean < 20):
                print(str(i+1)+'# AEC不合格')
                AEC_txt.write(str(i+1)+'# AEC不合格'+'\n')
            else:
                print(str(i+1)+'# AEC合格')
                AEC_txt.write(str(i+1)+'# AEC合格'+'\n')
            plt.subplot(211)
            plt.plot(tseqv,ERLEv,label = 'Channel #'+str(i+1))
            plt.title('ERLE curve for VOICE signal')
            plt.xlabel('time / s')
            plt.ylabel('Echo Retrun Loss Enhancement / dB ')
            plt.legend(loc='lower right')
            plt.subplot(212)
            plt.plot(tseqm,ERLEm,label = 'Channel #'+str(i+1))
            plt.title('ERLE curve for MUSIC signal')
            plt.xlabel('time / s')
            plt.ylabel('Echo Retrun Loss Enhancement / dB ')
            plt.legend(loc='lower right')
            plt.rcParams["figure.figsize"] = (18,12)
            
        AEC_txt.close()
        AEC_txt1.close()
        plt.show()
        plt.savefig(self.filepath+'result/present/aec_calc/aec_result.png') 
        AECdata = np.loadtxt('Result_AEC1.txt') 
        plt.figure('AEC_result')
        plt.bar(AECdata[:,0],AECdata[:,1])
        plt.title('ERLE value')
        plt.xlabel('channel number')
        plt.ylabel('Echo Retrun Loss Enhancement / dB ')
        plt.show()
    
    def noiselevel_calc(self):
        self.data_display('silence')
        if(os.path.exists(self.filepath +'result/present/noiselevel_calc/')):
            shutil.rmtree(self.filepath +'result/present/noiselevel_calc/')
        os.mkdir(self.filepath +'result/present/noiselevel_calc/')
        a = self._data_readin(self.filepath,'result/silence/micsilence.wav')
        b = self._data_readin(self.filepath,'result/silence/refsilence.wav')
        nl = np.zeros(len(self.micseq))
        refnl = np.zeros(len(self.refseq))
        for i in range(len(self.micseq)):
            nl[i] = np.sqrt(np.mean(a[0][:,i]**2))
            nl[i] = 20*np.log10(nl[i])
        for j in range(len(self.refseq)):
            refnl[j] = np.sqrt(np.mean(b[0][:,j]**2))
            if(refnl[j]==0):
                refnl[j] = -96
            else:
                refnl[j] = 20*np.log10(refnl[j])
        # xtick defined
        refstr = np.chararray(len(self.refseq),itemsize = 5)
        if(len(self.refseq) == 2): 
            refstr[:] = [b'ref1',b'ref2']
        else:
            refstr[:] = b'ref'
        #xtick defined
        xtick = np.append(np.arange(1,1+len(self.micseq)).astype(dtype=np.str),' ')
        xtick = np.append(xtick,refstr.astype(dtype=np.str))
        #nl defined
        nl = np.append(nl,-97)
        nl = np.append(nl,refnl)
        nl = 96+np.ones(len(nl))+nl
        print(nl,len(nl))
        print(xtick,len(xtick))
        nl_mic = nl[:-2]
        nl_ref = nl[-2:]
        plt.figure('nl_calc')
        plt.bar(xtick, nl , bottom = -96*np.ones(len(nl))) #96dbSNR for 16bit
        plt.title('Idle Noise Level for each Microphone Channel')
        plt.xlabel('Microphone Channel Number')
        plt.ylabel('Idle Noise Level /dBFS ')
        plt.show()
        plt.savefig(self.filepath+'result/present/noiselevel_calc/nl_result.png') 
        nl_max = np.max(nl_mic)
        ref_max = np.max(nl_ref)
        NL_txt = open(r'Result_NoiseLevel.txt','w+')
        if(nl_max > 41):
            print('MIC本底噪声级超过MIC limit要求，测试不合格，建议更换测试环境重新测试')
            NL_txt.write('MIC本底噪声级超过MIC limit要求，测试不合格，建议更换测试环境重新测试'+'\n')
        else:
            print('MIC本底噪声级测试合格，测试环境底噪满足要求')
            NL_txt.write('MIC本底噪声级测试合格，测试环境底噪满足要求'+'\n')
        if(ref_max > nl_max):
            print('回采电路底噪较大，建议优化')
            NL_txt.write('回采电路底噪较大，建议优化'+'\n')
        else:
            print('回采电路底噪满足要求')
            NL_txt.write('回采电路底噪满足要求'+'\n')
        NL_txt.close()

        
    def transferfunction_calc(self):
        self.data_display('chirp1')
        if(os.path.exists(self.filepath +'result/present/transferfunction_calc/')):
            shutil.rmtree(self.filepath +'result/present/transferfunction_calc/')
        os.mkdir(self.filepath +'result/present/transferfunction_calc/')
        a = self._data_readin(self.filepath,'result/chirp1/sndchirp1.wav')
        b = self._data_readin(self.filepath,'result/chirp1/refchirp1.wav')
        c = self._data_readin(self.filepath,'result/chirp1/micchirp1.wav')
        sndslice = np.zeros([self.fs,1])
        micslice = np.zeros([self.fs,len(self.micseq)])
        refslice = np.zeros([self.fs,len(self.refseq)])
        
        fr_ref  = np.zeros([5,len(self.refseq),41])
        fr_mic = np.zeros([5,len(self.micseq),41])
        thd_ref = np.zeros([5,len(self.refseq),32])
        thd_mic = np.zeros([5,len(self.micseq),32])
        
        for i in range(5):
            sndslice = a[0][2*i*self.fs:(2*i+1)*self.fs,0].reshape(self.fs,1)
            for j in range(len(self.refseq)):
                refslice[:,j] = b[0][2*i*self.fs:(2*i+1)*self.fs,j]
            wav_sndslice = thinkdsp.Wave(sndslice[:,0],framerate=self.fs)
            wav_sndslice.zero_pad(2*self.fs)
            wav_refslice = thinkdsp.Wave(refslice[:,0],framerate=self.fs)
            wav_refslice.zero_pad(2*self.fs)      
            f_fr,fr_ref[i,0,:] = self._freq_calc(wav_sndslice,wav_refslice)    #TF_Calc of ref2snd
            f_thd,thd_ref[i,0,:] = self._thd_calc(wav_sndslice,wav_refslice)    
            for k in range(len(self.micseq)):
                micslice[:,k] = c[0][2*i*self.fs:(2*i+1)*self.fs,k]
                wav_micslice = thinkdsp.Wave(micslice[:,k],framerate=self.fs)
                wav_micslice.zero_pad(2*self.fs)                
                f_fr,fr_mic[i,k,:] = self._freq_calc(wav_refslice,wav_micslice)    #TF_Calc of mic2ref
                f_thd,thd_mic[i,k,:] = self._thd_calc(wav_refslice,wav_micslice)

        plt.figure('fr_calc')
        plt.subplot(211)
        plt.title('Reference Channel Transfer Function with PreEQ Property at Channel #1')
        for m in range(5):
            plt.semilogx(f_fr,20*np.log10(fr_ref[m,0,:]),label = 'Stimulus Amplitude -'+str(6*m)+'dBFS')
            plt.xlim(100,8000)
            plt.xlabel('Frequncy / Hz')
            plt.ylabel('PreEQ Frequency Response / dB')
            plt.legend()
        plt.subplot(212)
        plt.title('SPK-MIC Circuit Transfer Function with Compression Property at Channel #1')
        for m in range(5):
            plt.semilogx(f_fr,20*np.log10(fr_mic[m,0,:]),label = 'Stimulus Amplitude -'+str(6*m)+'dBFS')
            plt.xlim(100,8000)
            plt.xlabel('Frequncy / Hz')
            plt.ylabel('SPK-MIC Circuit Frequency Response / dB')
            plt.legend()
        plt.rcParams["figure.figsize"] = (18,12)
        plt.show()
        plt.savefig(self.filepath+'result/present/transferfunction_calc/fr.png')        

        plt.figure('thd_calc')
        plt.subplot(211)
        plt.title('Reference Channel Pre-Distorted THD Property at Channel #1')
        for m in range(5):
            plt.semilogx(f_thd,100*thd_ref[m,0,:],label =  'Stimulus Amplitude -'+str(6*m)+'dBFS')
            plt.xlim(100,2000)
            plt.xlabel('Frequncy / Hz')
            plt.ylabel('Reference Channel Pre-Distortion / %')
            plt.legend()
        plt.subplot(212)
        plt.title('SPK-MIC Circuit THD Property at Channel #1')
        for m in range(5):
            plt.semilogx(f_thd,100*thd_mic[m,0,:],label =  'Stimulus Amplitude  -'+str(6*m)+'dBFS')
            plt.xlim(100,2000)           
            plt.xlabel('Frequncy / Hz')
            plt.ylabel('SPK-MIC Circuit THD / %')
            plt.legend()
        plt.rcParams["figure.figsize"] = (18,12)
        plt.show()
        plt.savefig(self.filepath+'result/present/transferfunction_calc/thd.png')            
        
        plt.figure('consistency')
        plt.subplot(211)
        plt.title('SPK-MIC Circuit Frequency Response Consistency at Amp 0dBFS')
        for n in range(len(self.micseq)):
            plt.semilogx(f_fr,20*np.log10(fr_mic[0,n,:]),label = 'Channel # '+str(n+1))
            plt.xlim(100,8000)
            plt.xlabel('Frequncy / Hz')
            plt.ylabel('SPK-MIC Circuit Frequency Response / dB')
            plt.legend()
        plt.subplot(212)
        plt.title('SPK-MIC Circuit THD Consistency at Amp 0dBFS')    
        for n in range(len(self.micseq)):        
            plt.semilogx(f_thd,100*thd_mic[0,n,:],label = 'Channel # '+str(n+1))
            plt.xlim(100,2000)           
            plt.xlabel('Frequncy / Hz')
            plt.ylabel('SPK-MIC Circuit THD / %')
            plt.legend()            
            plt.rcParams["figure.figsize"] = (18,12)
            plt.show()
            plt.savefig(self.filepath+'result/present/transferfunction_calc/consistency.png')            

    def delay_calc(self):
        self.data_display('chirp1')
        self.data_display('chirp2')
        if(os.path.exists(self.filepath +'result/present/delay_calc/')):
            shutil.rmtree(self.filepath +'result/present/delay_calc/')
        os.mkdir(self.filepath +'result/present/delay_calc/')
        a = self._data_readin(self.filepath,'result/chirp1/refchirp1.wav')
        b = self._data_readin(self.filepath,'result/chirp1/micchirp1.wav')
        c = self._data_readin(self.filepath,'result/chirp2/refchirp2.wav')
        d = self._data_readin(self.filepath,'result/chirp2/micchirp2.wav')   
        Nframe = 10
        Nlag = np.zeros(2*Nframe)
        Delay_txt = open(r'Result_Delay.txt','w+')
        for i in range(len(self.micseq)):
            refdata1 = a[0][:,-1]
            micdata1 = b[0][:,i]
            refdata2 = c[0][:,-1]
            micdata2 = d[0][:,i]
            for j in range(Nframe):
                refslice = refdata1[2*i*self.fs:(2*i+1)*self.fs]      
                micslice = micdata1[2*i*self.fs:(2*i+1)*self.fs]    
                if (self._fft_xcorr(refslice,micslice).argmax() < self.fs):               
                    Nlag[j] = -1*self._fft_xcorr(refslice,micslice).argmax()  
                else:
                    Nlag[j] = 2*self.fs - self._fft_xcorr(refslice,micslice).argmax()      
            for k in range(Nframe):
                refslice = refdata2[2*i*self.fs:(2*i+1)*self.fs]      
                micslice = micdata2[2*i*self.fs:(2*i+1)*self.fs]    
                if(self._fft_xcorr(refslice,micslice).argmax() < self.fs):
                    Nlag[10+k] = -1*self._fft_xcorr(refslice,micslice).argmax()
                else: 
                    Nlag[10+k] = 2*self.fs - self._fft_xcorr(refslice,micslice).argmax()
            if(Nlag.max()-Nlag.min()<=1 and int(Nlag.max())>0):
                Nlag = Nlag.max()*np.ones(len(Nlag))                
                Delay_txt.write(str(i+1)+'#MIC时延OK'+'\n')
                print(str(i+1) + '#MIC时延OK')
                
            else:
                print('回采减mic的差值为'+str(Nlag.max()))
                print(str(i+1) + '#MIC时延不合格')
                Delay_txt.write(str(i+1)+'#回采减mic的差值为'+str(Nlag.max())+'\n')
                Delay_txt.write(str(i+1)+'#MIC时延不合格'+'\n')
                     
            plt.figure('delay_calc')
            plt.title('Delay consistency with each MIC Channel to REF Channel')
            plt.plot(np.arange(len(Nlag))+1,Nlag,label = 'Channel #'+str(i+1)+' to reference channel')
            plt.xlabel('Triggerd Chirp Number / no.')
            plt.ylabel('Relative Delayed Sampling Frames / Points')
            plt.legend()
            plt.rcParams["figure.figsize"] = (18,12)
            plt.show()
            plt.savefig(self.filepath+'result/present/delay_calc/delay.png') 
        Delay_txt.close()

        
    def coherence_calc(self):
        self.data_display('noise')
        if(os.path.exists(self.filepath +'result/present/coherence_calc/')):
            shutil.rmtree(self.filepath +'result/present/coherence_calc/')
        os.mkdir(self.filepath +'result/present/coherence_calc/')
        a = self._data_readin(self.filepath,'result/noise/refnoise.wav')
        b = self._data_readin(self.filepath,'result/noise/micnoise.wav')   
        plt.figure('coherence_calc')
        plt.subplot(211)
        plt.title('Signal Coherence with each MIC Channel to REF Channel')
        Cohenrence_txt = open(r'Result_Cohenrence.txt','w+')
        freq_txt = open(r'freq.txt','w+')
        for i in range(len(self.micseq)):        
            freq, Cxy = signal.coherence(b[0][:,i],a[0][:,0],self.fs)
            plt.semilogx(freq,Cxy,label='Channel #'+str(i+1)+' to reference channel')
            Cohenrence_txt.write(str(Cxy))
        freq_txt.write(str(freq))
        plt.xlim(100,8000)         
        plt.xlabel('Frequency / Hz')
        plt.ylabel('Nomalized Coherence Coefficient')
        plt.legend()
        plt.rcParams["figure.figsize"] = (18,12)
        plt.show()
        plt.savefig(self.filepath+'result/present/coherence_calc/coherence.png')
        Cohenrence_txt.close()
        freq_txt.close()
        file = open('Result_Cohenrence.txt','r')
        aa = file.read()
        aa = aa.replace('\n',' ')
        aa = aa.replace('    ',' ')
        aa = aa.replace('   ',' ')
        aa = aa.replace('  ',' ')
        bb = aa.split(']')
        cc = len(bb)
        d=[]
        for i in range(cc):
            
            bb[i] = bb[i].replace('[','')
            bb[i]=bb[i].split(' ')
        #print(bb) 
        d=[]
        for i in range(len(bb)-1):
            d1=[]
            for j in range(len(bb[i])):
                if bb[i][j] == '':
                    pass
                else:
                    d1.append(float(bb[i][j]))
            d.append(d1)   
        kk = []
        ss = []
        for j in range(len(d[0])):
            ff = d[0][j]
            gg = d[0][j]
            for i in range(len(d)-1):
                ff = max(ff,d[i][j])
                gg = min(gg,d[i][j])
            hh = ff -gg
            kk.append(hh)
            ss.append(gg)
        file = open('freq.txt','r')
        mm = file.read()
        mm = mm.replace('\n','')
        mm = mm.replace('[','')
        mm = mm.replace(']','')
        mm = mm.split(' ')
        nn = []
        for i in range(len(mm)):
            if mm[i] == '':
                pass
            else:
                nn.append(mm[i])
        pp = []
        for i in range(len(nn)):
            pp.append(float(nn[i]))
        rr = kk[:18]
        tt = ss[2:18]
        rr_max = max(rr)
        tt_min = min(tt)
        print('Delta =',rr_max)
        print('频段最小值 =',tt_min)
        if tt_min < 0.3:
            print('相干性最小值小于0.3，不满足要求')
        else:
            if rr_max < 0.1:
                print('相干性满足要求')
            else:
                print('100Hz~1kHz内相干性差值大于0.1，不满足声智要求') 
        plt.subplot(212)
        plt.title('Cohenrence_Dalta')
        plt.xlabel('Frequency / Hz')
        plt.ylabel('Coherence_Delta')
        plt.semilogx(pp,kk,label='Delta=max-min')
        plt.legend()
        plt.xlim(100,8000)  
        plt.show()

        
        
        


        
        
        
        
    
    
        
def main():            
    tc = TestCase()

    if not(os.path.exists(tc.filepath +'result/')):
        os.mkdir(tc.filepath +'result/')
    if not(os.path.exists(tc.filepath +'result/present/')):
        os.mkdir(tc.filepath +'result/present/')   
    tc.aec_calc()
    tc.noiselevel_calc()
    tc.transferfunction_calc()
    tc.delay_calc()
    tc.coherence_calc()

if __name__=='__main__':
    main()

#endtime = datetime.datetime.now()
#print(endtime - starttime)


 