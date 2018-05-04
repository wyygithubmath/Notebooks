import plistlib

fileName = '.\\library.xml'

try:
    trackNames = plistlib.readPlist(fileName)
    print('Sucessful')
except:
    print('File is not exsited')


