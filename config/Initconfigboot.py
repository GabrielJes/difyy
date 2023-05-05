import os
import subprocess
import time
import sys
import DetectDevice
import tqdm


print('Welcome to Diffy \nconnect your pendrive to laptop !')
time.sleep(0.5)
print('Has the USB stick been connected and recognized? (Y/N) ')
UserResponse = input(':').lower()
print()
print('-'*40)
Confirm = DetectDevice.Confirm(UserResponse)
if Confirm == True :
    localdisk = DetectDevice.PendriveDetect().lower()
    FileSystem = DetectDevice.IdentifyFileSystem().lower()
    comand = DetectDevice.FormatDisk(localdisk,FileSystem)
    if comand == True :
        Identify = DetectDevice.IsoIdentify()
    else:
        sys.exit(1)
    
        
    






