#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/29 10:28
# @Author  : Xilun Wu
# @email   : nnuwxl@gmail.com
# @File    : MoviepyTest.py

"""
我想用此程序实现对于视频文件音频的提取,
实现一次性对单个文件夹下所有视频的提取
因为现有的软件单个单个提取很麻烦。对！说的就是你Pr
基于moviepy库
"""

from moviepy.editor import *
import os
import LnkTest
import sys
from sys import argv
import moviepy
import time

if __name__=="__main__":
    """主函数部分"""
    print("请输入需要转换的文件(夹)地址(支持快捷方式)：",end='')
    filepath = input()
    # 当为快捷方式的时候
    if os.path.exists(filepath)==False:
        filepath = filepath + ".lnk"
        if os.path.exists(filepath) == False:
            filepath = filepath.split('.')[0] + ".mp4"
            if os.path.exists(filepath) == False:
                filepath = filepath.split('.')[0] + ".avi"
                if os.path.exists(filepath) == False:
                    filepath = filepath.split('.')[0] + ".webm"
                    if os.path.exists(filepath) == False:
                        filepath = filepath.split('.')[0] + ".mov"
                        if os.path.exists(filepath) == False:
                            filepath = filepath.split('.')[0] + ".ogv"
                            if os.path.exists(filepath) == False:
                                print("输入文件夹有误,检查后再重试")
                                time.sleep(3)
                                sys.exit(0)

    videolist = []
    if len(filepath.split('.'))==2 and filepath.split('.')[-1]=="lnk":
        print("正在访问快捷方式的路径")
        time.sleep(1)
        a = inkTest.GetpathFromLink(filepath)
        # 函数返回这个快捷方式的地点
        print("路径改为:{}".format(a))
        time.sleep(1)
    elif len(filepath.split('.'))==2 and filepath.split('.')[-1] in ["mp4","ogv","webm","mov","avi"]:
        videolist = [filepath.split('\\')[-1]]
        print("文件为：{}".format(filepath))
    else:
        a = filepath
        print("路径为:{}".format(a))
        time.sleep(1)

    if len(videolist) ==0:
        videolist = os.listdir(a)
        outputpath = os.path.join(a,"音频提取")
    else:
        a = os.path.dirname(filepath)
        outputpath = os.path.join(a, "Audio_output")
    if os.path.exists(outputpath) == False:
        print("正在新建输出文件夹\"音频提取\"")
        time.sleep(1)
        os.mkdir(outputpath)

    print("即将对以下文件进行转换：")
    for a2 in videolist:
        if len(a2.split('.')) == 2 and a2.split('.')[1] in ["mp4","ogv","webm","mov","avi"]:
            print("--" + a2)
    time.sleep(3)
    print("请输入转出格式，支持mp3(轻量)、wav(无损)：",end='')
    outputform = input()

    for i in videolist:
        if len(i.split('.')) == 2 and i.split('.')[1] in ["mp4","ogv","webm","mov","avi"]:
            path2 = os.path.join(a,i)
            video = VideoFileClip(path2)
            audio = video.audio
            outputsound = i.split('.')[0] + '.' + outputform
            outputpath2 = os.path.join(outputpath,outputsound)
            audio.write_audiofile(outputpath2)
            print("{} 输出完成".format(outputsound))
    print("\n所有文件转换完毕。\n")
    print("感谢您使用本软件\n作者：NNUwdl\n有其他问题可发送至作者邮箱nnuwxl@gmail.com")
    input()


