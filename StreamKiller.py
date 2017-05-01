# -*- coding: utf-8 -*-
"""
Created on Sat Jul 16 13:58:49 2016

@author: 进击的樊
"""

import sys
import os
import time
python=sys.executable

time.sleep(10)

print ("restart")
os.execl(python,python,*sys.argv)