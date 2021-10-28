import os
import pyaudio
import threading
import wave
from datetime import datetime

class Recorder():
    def __init__(self, chunk=1024, channels=2, rate=44100, isMic = True):
        self.CHUNK = chunk
        self.FORMAT = pyaudio.paInt16
        self.CHANNELS = channels
        self.RATE = rate
        self._running = True
        self._frames = []
        self.isMic = isMic

#Find audio devices
    def findInternalRecordingDevice(self, p):
        if self.isMic:
            return 0
        target = 'Stereo Mix'
        for i in range(p.get_device_count()):
            devInfo = p.get_device_info_by_index(i)
            print(devInfo)
            if devInfo['name'].find(target) >= 0 and devInfo['hostApi'] == 0:
                return i
        print('Cannot find internal recording device')
        return -1

#Realize recording function
    def __record(self):
        self._running = True
        self._frames = []

        p = pyaudio.PyAudio()
        dev_idx = self.findInternalRecordingDevice(p)
        if dev_idx < 0:
            return
        stream = p.open(
                        input_device_index=dev_idx,
                        format=self.FORMAT,
                        channels=self.CHANNELS,
                        rate=self.RATE,
                        input=True,
                        frames_per_buffer=self.CHUNK)
        while (self._running):
            data = stream.read(self.CHUNK)
            self._frames.append(data)

        stream.stop_stream()
        stream.close()
        p.terminate()
        return

    def start(self):
        print("Start Recording")
        threading._start_new_thread(self.__record, ())

#Stop recording & Recording file preservation
    def stop(self):
        print("End Recording")
        self._running = False
        mic_str = "mic_"
        if self.isMic == False:
            mic_str = "piano_"
        if not os.path.exists('record'):
            os.makedirs('record')
        self.save("record/rec_"+mic_str + datetime.now().strftime("%Y-%m-%d_%H-%M-%S") + ".wav")

    def save(self, fileName):
        p = pyaudio.PyAudio()
        wf = wave.open(fileName, 'wb')
        wf.setnchannels(self.CHANNELS)
        wf.setsampwidth(p.get_sample_size(self.FORMAT))
        wf.setframerate(self.RATE)
        wf.writeframes(b''.join(self._frames))
        wf.close()
        p.terminate()



