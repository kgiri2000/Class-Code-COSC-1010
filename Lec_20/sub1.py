# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 18:13:11 2021

@author: kgiri
"""

import re

# re or RegEx or Regular Expression is a sequence of characters that forms a search pattern

# It can be used to check if a string contains the specified search pattern
"""
it have the functions like 
findall -- return a list containing all matches
search  -- return the match object 
split return a list where the string has been split at each match 


"""

s = "128 MPG"
t = re.sub('[^.0-9]', '', str(s))

print ( "s=-->{}<--   t=-->{}<--".format(s,t))

