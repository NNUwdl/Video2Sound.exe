#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/29 10:28
# @Author  : Xilun Wu
# @email   : nnuwxl@gmail.com
# @File    : MoviepyTest.py

"""
I want to use this program to extract audio from video files,
Achieve extraction from a folder of all the video
Because existing software is very cumbersome to extract. Right! It's your fault, adobe PR!
Based on model moviepy
"""

from moviepy.editor import *
import os
import LnkTest
import sys
from sys import argv
import moviepy
import time

if __name__=="__main__":
    """Main function part"""
    print("Please enter the folder (or MP4 file) address you want to convert (shortcuts are supported)：",end='')
    filepath = input()
    # When the input is a shortcut or in a wrong format
    if os.path.exists(filepath)==False:
        filepath = filepath + ".lnk"
        if os.path.exists(filepath) == False:
            filepath = filepath.split('.')[0] + ".mp4"
            if os.path.exists(filepath) == False:
                print("Incorrect folder Path. \nCheck and try again later.")
                time.sleep(3)
                sys.exit(0)

    videolist = []
    if len(filepath.split('.'))==2 and filepath.split('.')[-1]=="lnk":
        print("The path shortcut referring to is being accessed")
        time.sleep(1)
        a = inkTest.GetpathFromLink(filepath)
        # The function returns the location of this shortcut
        print("Change the path to :{}".format(a))
        time.sleep(1)
    elif len(filepath.split('.'))==2 and filepath.split('.')[-1]=="mp4":
        videolist = [filepath.split('\\')[-1]]
        print("MP4 File：{}".format(filepath))
    else:
        a = filepath
        print("Path :{}".format(a))
        time.sleep(1)

    if len(videolist) == 0:
        videolist = os.listdir(a)
        outputpath = os.path.join(a,"Audio_output")
    else:
        a = os.path.dirname(filepath)
        outputpath = os.path.join(a,"Audio_output")
    if os.path.exists(outputpath) == False:
        print("Creating the output folder:\"Audio_output\"")
        time.sleep(1)
        os.mkdir(outputpath)

    print("The following files will be processed：")
    for a2 in videolist:
        if len(a2.split('.')) == 2 and a2.split('.')[1] in ["mp4"]:
            print("--" + a2)
    time.sleep(3)
    print("")

    for i in videolist:
        if len(i.split('.')) == 2 and i.split('.')[1] in ["mp4"]:
            path2 = os.path.join(a,i)
            video = VideoFileClip(path2)
            audio = video.audio
            outputsound = i.split('.')[0] + ".mp3"
            outputpath2 = os.path.join(outputpath,outputsound)
            audio.write_audiofile(outputpath2)
            print("{} process complete.".format(outputsound))
    print("\nAll files done。\n")
    print("Thank you for using this software.\n@Author : NNUwxl\n"
          "Having additional question can email me at : nnuwxl@gmail.com")
    input()

