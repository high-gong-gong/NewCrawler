from pytube import YouTube
from moviepy.editor import *
import speech_recognition as sr
from os import path
import time
import os
import shutil

def trans_text():
    path = r".\w"
    files = os.listdir(path)
    files = [path + "\\" + f for f in files if f.endswith('.wav')]
    freq_wav = len(files)

    for freq in range(1,freq_wav):
        if freq%2==0:
            time.sleep(30)
            print("SLEEP30")
        r = sr.Recognizer()
        with sr.WavFile("./w/test-{}.wav".format(freq)) as source:
            audio = r.record(source)

        f = open('test.txt','a')

        try:
            respones = r.recognize_google(audio, language='zh-tw')
            print("Transcription: " + r.recognize_google(audio,language='zh-tw'))
            #print(type(respones))
            f.write(respones)
        except LookupError:
            print("Could not understand audio")
        time.sleep(30)

    shutil.rmtree('./w')
    os.makedirs("../test", exist_ok =True)

if __name__ == '__main__':
    trans_text()