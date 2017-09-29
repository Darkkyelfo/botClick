'''
Created on Sep 8, 2017

@author: raul1
'''
from ctypes import Structure, c_long

class POINT(Structure):
    _fields_ = [("x", c_long), ("y", c_long)]
        