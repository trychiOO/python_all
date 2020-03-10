import soundfile as sf
import numpy as np
import os
import time
import winsound
import subprocess


def findendpoint(x, point, sample_rate):
    while (1):
        eng = sum(x[point:point + int(sample_rate / 4)])
        if eng == 0:
            if sum(x[point:point + sample_rate * 1]) == 0:
                return point + sample_rate * 1
            else:
                return point
        else:
            point = point + int(sample_rate / 4)


def split_file(wav_name, split_time):
    record_time = []
    sig, sample_rate = sf.read(wav_name)
    x = np.array(sig)
    print()
    split_num = int(x.shape[0] / sample_rate / split_time)
    time_begin = 0
    for j in range(split_num + 1):
        if time_begin == 0:
            time_end = split_time * sample_rate
        else:
            time_end = split_time * sample_rate * (j + 1)

        if time_end > x.shape[0]:
            sf.write(wav_name + str(j) + '.wav', x[time_begin:], sample_rate)
            record_time.append(int((x.shape[0] - time_begin) / sample_rate))
        else:
            time_end = findendpoint(x, time_end, sample_rate)
            sf.write(wav_name + str(j) + '.wav', x[time_begin:time_end], sample_rate)
            record_time.append(int((time_end - time_begin) / sample_rate))
        time_begin = time_end
        print(j)

    return record_time


def record(record_time, wav_name, save_path='.\\record'):
    # record_time = [153,150,143,153,151,146,151,141,150,150,152,148,150,100]
    if os.path.exists(save_path):
        pass
    else:
        mkdir = 'mkdir ' + save_path
        os.system(mkdir)
    rmpcm = 'adb shell rm /tmp/*.pcm '
    sample_basex = input('请输入录音命令:')
    if not sample_basex:
        for i in range(len(record_time)):
            subprocess.call(rmpcm)
            # start_record = 'adb shell cd /tmp/sai_test/&&LD_LIBRARY_PATH=. ./sample_basex ' + str((record_time[i] + 3) * 1000 / 16) + ' ' + recmd[1]
            start_record = 'adb shell touch /tmp/savebasex.pcm'
            print(start_record)
            p = subprocess.Popen(start_record)
            time.sleep(1)
            winsound.PlaySound(wav_name + str(i) + ".wav", winsound.SND_ALIAS)

            time.sleep(2)
            pull = 'adb pull /tmp/savebasex.pcm ' + save_path + '\\' + str(i) + '.pcm'
            p1 = subprocess.Popen(pull)
            p1.wait()
            time.sleep(1)
    else:
        if 'arecord' in sample_basex:
            recmd = sample_basex
            for i in range(len(record_time)):
                subprocess.call(rmpcm)
                # start_record = 'adb shell cd /tmp/sai_test/&&LD_LIBRARY_PATH=. ./sample_basex ' + str((record_time[i] + 3) * 1000 / 16) + ' ' + recmd[1]
                start_record = 'adb shell ' + recmd + ' -d ' + str(record_time[i] + 3) + ' /tmp/record.pcm'
                print(start_record)
                p = subprocess.Popen(start_record)
                time.sleep(1)
                winsound.PlaySound(wav_name + str(i) + ".wav", winsound.SND_ALIAS)

                time.sleep(2)
                pull = 'adb pull /tmp/record.pcm ' + save_path + '\\' + str(i) + '.pcm'
                p1 = subprocess.Popen(pull)
                p1.wait()
                time.sleep(1)

        elif 'sample_basex' in sample_basex:

            recmd = sample_basex.split('9999 ')
            # ./sample_basex 99999 4,5,7,6,0,3,1,2 16000 32 14 14 default 0
            for i in range(len(record_time)):
                subprocess.call(rmpcm)
                start_record = 'adb shell cd /tmp/&&LD_LIBRARY_PATH=. ./sample_basex ' + str(
                    (record_time[i] + 3) * 1000 / 16) + ' ' + recmd[1]
                print(start_record)
                p = subprocess.Popen(start_record)
                time.sleep(1)
                winsound.PlaySound(wav_name + str(i) + ".wav", winsound.SND_ALIAS)
                time.sleep(3)
                pull = 'adb pull /tmp/record.pcm ' + save_path + '\\' + str(i) + '.pcm'
                p1 = subprocess.Popen(pull)
                p1.wait()
                time.sleep(1)

    chann = int(input('录音通道数：'))
    if chann:
        combine(save_path, chann)
    else:
        combine(save_path)


def record_noise(record_time, sample_basex, save_path='.\\noise'):
    if os.path.exists(save_path):
        pass
    else:
        mkdir = 'mkdir ' + save_path
        os.system(mkdir)
    rmpcm = 'adb shell rm /tmp/*.pcm '
    # sample_basex = 'LD_LIBRARY_PATH=. ./sample_basex 9999 multi 6 8 0,1,2,3,4,5,6,7 16 48000 16 16 0 512 2048'
    if not sample_basex:
        for i in range(len(record_time)):
            subprocess.call(rmpcm)
            # start_record = 'adb shell cd /tmp/sai_test/&&LD_LIBRARY_PATH=. ./sample_basex ' + str((record_time[i] + 3) * 1000 / 16) + ' ' + recmd[1]
            start_record = 'adb shell touch /tmp/savebasex.pcm'
            print(start_record)
            p = subprocess.Popen(start_record)
            time.sleep(1 + record_time[i])
            pull = 'adb pull /tmp/savebasex.pcm ' + save_path + '\\' + str(i) + '.pcm'
            p1 = subprocess.Popen(pull)
            p1.wait()
            time.sleep(1)
    else:
        if 'arecord' in sample_basex:
            recmd = sample_basex
            for i in range(len(record_time)):
                subprocess.call(rmpcm)
                # start_record = 'adb shell cd /tmp/sai_test/&&LD_LIBRARY_PATH=. ./sample_basex ' + str((record_time[i] + 3) * 1000 / 16) + ' ' + recmd[1]
                start_record = 'adb shell ' + recmd + ' -d ' + str(record_time[i] + 3) + ' /tmp/record.pcm'
                print(start_record)
                p = subprocess.Popen(start_record)
                time.sleep(record_time[i] + 3)
                pull = 'adb pull /tmp/record.pcm ' + save_path + '\\' + str(i) + '.pcm'
                p1 = subprocess.Popen(pull)
                p1.wait()
                time.sleep(1)

        elif 'sample_basex' in sample_basex:

            recmd = sample_basex.split('9999 ')
            for i in range(len(record_time)):
                subprocess.call(rmpcm)
                start_record = 'adb shell cd /tmp/&&LD_LIBRARY_PATH=. ./sample_basex ' + str(
                    (record_time[i] + 3) * 1000 / 16) + ' ' + recmd[1]
                print(start_record)
                p = subprocess.Popen(start_record)
                time.sleep(record_time[i] + 3)
                pull = 'adb pull /tmp/record.pcm ' + save_path + '\\' + str(i) + '.pcm'
                p1 = subprocess.Popen(pull)
                p1.wait()
                time.sleep(1)

    chann = int(input('录音通道数：'))
    if chann:
        combine(save_path, chann)
    else:
        combine(save_path)


def combine(save_path, chann=8):
    print('combining... ')
    from pydub import AudioSegment
    p_arr = []
    for root, dirs, files in os.walk(save_path):
        for name in files:
            if name.endswith('.pcm'):
                p_arr.append(os.path.join(root, name))
    f2 = open(save_path + '/all.pcm', 'ab')
    p_arr.sort()
    for i in range(len(p_arr)):
        try:
            pcm_name = p_arr[i]
            sound = AudioSegment.from_file(pcm_name, format="pcm", frame_rate=16000, channels=1, sample_width=2)
            raw_audio_data = sound.raw_data
            waveData = np.fromstring(raw_audio_data, dtype=np.int16)
            print(waveData.shape[0] / chann)
            waveData = waveData[:chann * int(waveData.shape[0] / chann)].reshape(int(waveData.shape[0] / chann), chann)
            print(waveData.shape)
            newData = np.zeros([waveData.shape[0] - 576, waveData.shape[1]], dtype=np.int16)
            print(newData.shape)
            for j in range(waveData.shape[1]):
                newData[:, j] = waveData[576:chann * int(waveData.shape[0] / chann), j]

            print(newData.shape)
            # filename = filename.replace('.pcm', '')
            newData.tofile(pcm_name)
        except:
            pass

    for i in range(len(p_arr)):
        print(i)
        with open(p_arr[i], 'rb')as f1:
            f2.write(f1.read())
    f2.close()


if __name__ == '__main__':

    split_switch = int(input('是否切割音频(是(1)，否(0))：'))
    if split_switch:
        wav_name = input('要切割的音频名称：')
        split_time = int(input('切割时长(s)：'))
        record_time = split_file(wav_name, split_time)
        record(record_time, wav_name)

    else:
        times = 80  # 往下拉的次数
        record_time = [10]  # 单位s
        record_time = record_time * times
        # for i in range(times):
        sample_basex = input('请输入录音命令:')
        record_noise(record_time, sample_basex)