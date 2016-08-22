#!/usr/bin/env python
#_*_ coding: utf-8 _*_

import os
import sys
sys.path.append(os.path.dirname(os.path.abspath( __file__ ))+"/Checker")
from Freak import *
from Freak_Scapy import *

class SSLCheckManager:
    def __init__(self):
        self.target = ''
        
def SSLCheck(sslCheckManager):
#    FreakCheck(sslCheckManager.target)
    ScapyFreakCheck(sslCheckManager.target)
        
def main():
    sslCheckManager = SSLCheckManager()
    
    sslCheckManager.target = raw_input('INPUT TEST Target(IP:PORT) : ')
    SSLCheck(sslCheckManager)
    
if __name__=="__main__":
    main()