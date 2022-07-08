import os
from sys import platform as _platform


def getOS():
    if _platform == "darwin":
        return "Mac OS"
    elif _platform == "win64":
        return "Windows"


def getRootPath():
    if _platform == "darwin":
        return os.path.dirname(os.getcwd())
    elif _platform == "win64":
        return os.path.dirname(os.getcwd())