# Video2Sound
Coding while Learning

English Version

This is a file using to extract audio from video files.
It can achieve extraction from a folder of all the video.

To use this program to extract audio from video files,
You just need to double click the Audio_output.exe.
Wait until it shows the guidance.
Drag the file you want to process into the command box.
Wait for it to parse the path.
Input the outputform: mp3 or wav.
Wait for it to finish processing.
That's all.

You can drag Folders or individual video file into the command box.
.mp4,.ogv,.webm,.avi,.mov are supported.

This software is mainly made by using model moviepy.(this environment is not required on your computer)


There are still some problems to be solved.
For example, after the module TQDM is packaged into an executable program, there will be a display problem in the progress bar, which I have no ability to solve. I hope that some big guy can send me the solution, thank you very much.
I haven't learned how to use Python forms modules yet, but they may be added in the future.
This program takes up a lot of storage space: over 100 megabyters, I guess because the Pyinstaller package would write all the Python(in my system's default path) models to the program.Later, I will see if we can find a way not to write all the models into the program.

Thank you for using my software.

@Auther : NNUwdl
@Email  : nnuwxl@gmail.com



             
        

中文版(Chinese version)

此程序实现对于视频文件音频的提取,
实现一次性对单个文件夹下所有视频的提取

使用流程：
您只需要双击Audio_output.exe，
稍等片刻，它便会在屏幕上显示提示信息，
将要处理的文件拖到命令框中，或是填入(相对\绝对)路径，
等待它解析路径，
在命令框中输入想要输出的格式，
等待它全部处理完成即可。


您可以将文件夹或单个视频文件拖到命令框中。
支持的视频格式有：.mp3、.ogv、.webm、.avi、mov

这个软件是基于python的moviepy库（在您电脑上不需要拥有这个环境）

还有一些问题等待解决。
比如在封装成可执行程序后模块tqdm的进度条部分会出现显示问题，这个我还不会解决，希望有大佬能私信我解决方案，十分感谢。
  还没有学会如何使用python的窗体模块，未来可能会添加。
  这个程序占用很大的存储空间：大于100M，我猜是因为pyinstaller的装包会把我系统默认路径下python里所有的库都写入程序。后面看看能不能找个方法不把所有的库都写入进程序。
  
2020/11/1  1:56 am
自己在使用过程中有发现一个小bug，
当文件命名有空格的时候，拖到命令行会出现头尾加双引号，导致输入的字符串也包含了双引号，引起错误
这个机制在以后的过程中值得警惕


感想您使用本软件。

@作者 : NNUwdl
@邮箱 : nnuwxl@gmail.com
