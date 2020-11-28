from pytube import YouTube
from moviepy.editor import *
import speech_recognition as sr
from os import path
import time
import os
import shutil

url = 'https://www.youtube.com/watch?v=LuuyiS96uvA'
title = '『蔡昌憲來減脂-外傳』兩個月減10%體脂是怎麼辦到的？｜詳細課表分享'

def download_youtube(url,title):
    try:
        YouTube(url).streams.first().download()

        video = VideoFileClip(title+'.mp4')
        video.audio.write_audiofile('test.wav')

        os.makedirs("../test", exist_ok =True)
        shutil.move("test.wav", "../test")
        video.close()
        os.remove(title+'.mp4')
    except:
        pass


if __name__ == '__main__':
    download_youtube(url,title)