import os
import time

print("WARNING:YOU NEED 10MB OF FREE DISK SPACE FOR THIS INSTALLATION")
print("downloading...")
time.sleep(2)
os.system("wget https://bootstrap.pypa.io/2.7/get-pip.py -O get-pip27.py")
os.system("sudo python2 get-pip27.py")
os.system("wget https://bootstrap.pypa.io/get-pip.py -O get-pip.py")
os.system("sudo python3.9 get-pip.py")
time.sleep(5)
os.system("python3.9 -m pip install numpy")
os.system("python3.9 -m pip show numpy")
os.system("import numpy as np")
os.system("pip3 install --upgrade numpy")
