# coding:gbk
# GetLink.py
# hbxcyz.cn
import os
import pythoncom
from win32com.shell import shell
from win32com.shell import shellcon

#从.lnk文件中获取文件路径

def GetpathFromLink(lnkpath):
    shortcut = pythoncom.CoCreateInstance(
        shell.CLSID_ShellLink, None,
        pythoncom.CLSCTX_INPROC_SERVER, shell.IID_IShellLink)
    shortcut.QueryInterface( pythoncom.IID_IPersistFile ).Load(lnkpath)
    path = shortcut.GetPath(shell.SLGP_SHORTPATH)[0]
    return path

#创建快捷方式

def CreateLnkpath(filename,lnkname):
    shortcut = pythoncom.CoCreateInstance(
        shell.CLSID_ShellLink, None,
        pythoncom.CLSCTX_INPROC_SERVER, shell.IID_IShellLink)
    shortcut.SetPath(filename)
    if os.path.splitext(lnkname)[-1] != '.lnk':
        lnkname += ".lnk"
    shortcut.QueryInterface(pythoncom.IID_IPersistFile).Save(lnkname,0)

#创建url快捷方式

def CreateURLShortcut(url,name):
    shortcut = pythoncom.CoCreateInstance(
        shell.CLSID_InternetShortcut,None,
        pythoncom.CLSCTX_INPROC_SERVER,shell.IID_IUniformResourceLocator)
    shortcut.SetURL(url)
    if os.path.splitext(name)[-1] != '.url':
        name += '.url'
    shortcut.QueryInterface(pythoncom.IID_IPersistFile).Save(name,0)

#从.url快捷方式获取url连接地址
def GetURLFromShortcut(url):
    shortcut = pythoncom.CoCreateInstance(
        shell.CLSID_InternetShortcut,None,
        pythoncom.CLSCTX_INPROC_SERVER,shell.IID_IUniformResourceLocator)
    shortcut.QueryInterface(pythoncom.IID_IPersistFile).Load(url)
    url = shortcut.GetURL()
    return url
#获取桌面路径

def GetDesktoppath():
    ilist = shell.SHGetSpecialFolderLocation(0,shellcon.CSIDL_DESKTOP)
    dtpath = shell.SHGetPathFromIDList(ilist)
    #dtpath = dtpath.decode('gbk')
    return dtpath

