#pip install moviepy
#pip install matplotlib
#coding=gbk
import os
import wave
import numpy as np
import pylab as plt
import shutil

CutTimeDef = 60 #以1s截斷檔案
# CutFrameNum =0


path = r"..\test"
files = os.listdir(path)
files = [path + "\\" + f for f in files if f.endswith('.wav')]

# def SetFileName(WavFileName):
#     for i in range(len(files)):
#         FileName = files[i]
#         print("SetFileName File Name is ", FileName)
#         FileName = WavFileName;


def CutFile():
    for i in range(len(files)):
        FileName = files[i]
        print("CutFile File Name is ",FileName)
        f = wave.open(r"" + FileName, "rb")
        params = f.getparams()
        print(params)
        nchannels, sampwidth, framerate, nframes = params[:4]
        CutFrameNum = framerate * CutTimeDef
         # 讀取格式資訊
         # 一次性返回所有的WAV檔案的格式資訊，它返回的是一個組元(tuple)：聲道數, 量化位數（byte    單位）, 採
         # 樣頻率, 取樣點數, 壓縮型別, 壓縮型別的描述。wave模組只支援非壓縮的資料，因此可以忽略最後兩個資訊

        print("CutFrameNum=%d" % (CutFrameNum))
        print("nchannels=%d" % (nchannels))
        print("sampwidth=%d" % (sampwidth))
        print("framerate=%d" % (framerate))
        print("nframes=%d" % (nframes))
        str_data = f.readframes(nframes)
        f.close()# 將波形資料轉換成陣列
        # Cutnum =nframes/framerate/CutTimeDef
        # 需要根據聲道數和量化單位，將讀取的二進位制資料轉換為一個可以計算的陣列
        wave_data = np.fromstring(str_data, dtype=np.short)
        wave_data.shape = -1, 2
        wave_data = wave_data.T
        temp_data = wave_data.T
        # StepNum = int(nframes/200)
        StepNum = CutFrameNum
        StepTotalNum = 0;
        haha = 0
        while StepTotalNum < nframes:
        # for j in range(int(Cutnum)):
            print("Stemp=%d" % (haha))
            FileName = "..\\testcutresults\\" + files[i][-17:-4] +"-"+ str(haha+1) + ".wav"
            print(FileName)
            temp_dataTemp = temp_data[StepNum * (haha):StepNum * (haha + 1)]
            haha = haha + 1;
            StepTotalNum = haha * StepNum;
            temp_dataTemp.shape = 1, -1
            temp_dataTemp = temp_dataTemp.astype(np.short)# 開啟WAV文件
            f = wave.open(FileName, "wb")#
            # 配置聲道數、量化位數和取樣頻率
            f.setnchannels(nchannels)
            f.setsampwidth(sampwidth)
            f.setframerate(framerate)
             # 將wav_data轉換為二進位制資料寫入檔案
            f.writeframes(temp_dataTemp.tostring())
            f.close()

    shutil.copytree('../test', './w')
    shutil.rmtree('../test')
    os.makedirs("../test", exist_ok=True)

if __name__ == '__main__' :
    CutFile()

    print("Run Over")