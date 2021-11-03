# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 17:56:35 2021

@author: kgiri
"""


import re

cRe = re.compile('ab*')
print ( cRe )

iRe = re.compile('ab*',re.IGNORECASE)
print ( iRe )

if cRe.match ( "aaxaabXabY" ) : 
    print ("matched 1" )

if cRe.match ( "aaXaabXAbY" ) : 
    print ("matched 2 " )