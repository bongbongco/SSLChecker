#!/usr/bin/env python
#_*_ coding: utf-8 _*_
import sys
import subprocess
from socket import *


class FreakCheckTarget:
    def __init__(self):
        self.ip = ''
        self.port = ''

    def set(self, targetInfo):
        self.ip, self.port = targetInfo.split(':')

class FreakChecker:
    def __init__(self):        
        self.judge = ''
        self.platform = sys.platform
        
    def run(self, ip, port):
        try:
            if 'win32' in self.platform:
                return 'Please Using linux'
            else:    
                self.judge = subprocess.Popen(['openssl', 's_client', '-connect', ip+':'+str(port),'-cipher','EXPORT'], stderr=subprocess.STDOUT, stdout=subprocess.PIPE)
            self.judge = self.judge.communicate()[0]
            return self.judge
        except:
            return 'Error Freak Check'


def FreakCheck(targetInfo):
    freakCheckTarget = FreakCheckTarget()
    freakChecker = FreakChecker()

    freakCheckTarget.set(targetInfo)
    
    checkResult = freakChecker.run(freakCheckTarget.ip, freakCheckTarget.port)
    
    if 'Please Using linux' in checkResult:
        print 'Not Support Windows'
    elif 'Error Freak Check' in checkResult:
        print '[Error] Failed Freak check'
    elif 'Cipher is EXP' in checkResult:
        print '수출용 RSA를 지원하고 있습니다.'
    else: 
        print '수출용 RSA를 지원하고 있지 않습니다.'
        