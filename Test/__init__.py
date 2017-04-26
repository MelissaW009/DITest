# coding:utf-8
import sys
from configparser import ConfigParser


def readConf(filepath):
    cf = ConfigParser()
    cf.read(filepath,encoding="utf-8")
    s = cf.sections()
    print(s)
    b = cf.options("common")
    print(b)
    c=cf.get("common", "browsername")
    print(c)


if __name__ == "__main__":
    #myargs = sys.argv[1:]
    fileint_path ="/home/melissa/A/PythonTest/test1.txt" #sys.argv[1]
    filein = open(fileint_path)

    fileout_path = "/home/melissa/A/PythonTest/test2.txt"
    fileout = open(fileout_path, 'w')
    try:
        alltext = filein.read()
        fileout.write(alltext)
    finally:
        filein.close()
        fileout.close()
