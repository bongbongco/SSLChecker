#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from scapy import *
from scapy_ssl_tls.ssl_tls import *
from scapy_ssl_tls.ssl_tls_crypto import *
import socket

BUFFER_SIZE = 1024
TLS_EXPORT_CIPHERS = [
    TLSCipherSuite.RSA_EXPORT_WITH_RC4_40_MD5
    ,TLSCipherSuite.RSA_EXPORT_WITH_RC2_CBC_40_MD5
    ,TLSCipherSuite.RSA_EXPORT_WITH_DES40_CBC_SHA
    ,TLSCipherSuite.RSA_EXPORT1024_WITH_RC4_56_MD5
    ,TLSCipherSuite.RSA_EXPORT1024_WITH_RC2_CBC_56_MD5
    ,TLSCipherSuite.RSA_EXPORT1024_WITH_DES_CBC_SHA
    ,TLSCipherSuite.RSA_EXPORT1024_WITH_RC4_56_SHA  
    ]

class ScapyFreakCheckTarget:
    def __init__(self, targetInfo):
        self.ip, self.port = targetInfo.split(':')
        self.target = (self.ip, int(self.port))

class ScapyFreakChecker:
    def __init__(self):
        self.checker = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.message = ''
        self.response = ''

    def Connect(self,destination):
        self.checker.connect(destination)
        
    def Send(self):
        self.checker.sendall(str(self.message))    
        self.response = self.checker.recv(BUFFER_SIZE*8)
        
    def CommunicationView(self):
        self.message.show()
        SSL(str(self.message)).show()
        print 'Payload'
        print 'received, %d -- %s' %(len(self.response), repr(self.response))
        SSL(str(repr(self.response))).show()
        
    def Close(self):
        self.checker.close()
                    
 
def ScapyFreakCheck(targetInfo):
    scapyFreakCheckTarget = ScapyFreakCheckTarget(targetInfo)
    scapyFreakChecker = ScapyFreakChecker() 

    
    scapyFreakChecker.Connect(scapyFreakCheckTarget.target)
    
    for tlsExportCipher in TLS_EXPORT_CIPHERS:
        scapyFreakChecker.message = TLSRecord(version=TLSVersion.TLS_1_1)/TLSHandshake()/TLSClientHello(version=TLSVersion.TLS_1_1, cipher_suites=tlsExportCipher)
        scapyFreakChecker.Send()
        #scapyFreakChecker.CommunicationView()
        print '\n=====================================================\n'
        
        if not len(scapyFreakChecker.response) < 10:
            print 'Server is Supported ' + TLS_CIPHER_SUITES.get(tlsExportCipher)
        else:
            print 'Server is not Supported ' + TLS_CIPHER_SUITES.get(tlsExportCipher)
            print '\n=====================================================\n'

    scapyFreakChecker.Close()