# -*- coding: utf-8 -*-
"""
Created on Sun Sep 19 19:47:53 2021

@author: hossi
"""
f=open("C:/Users/hossi/Desktop/centralisetroisneudtailleun.txt","r")
f_new=open("C:/Users/hossi/Desktop/resultatcentralisetroisneudtailleun.txt","wt")
for s in f:
    f_new.write((((((s.replace(', (','; (')).replace(', ',',')).replace(': ',';')).replace('; ',';\n'))))
#    f_new.write(s.replace(', ',','))
#    f_new.write(s.replace(': ',';'))  
#    f_new.write(s.replace('; ',';\n'))
f.close()
f_new.close()
