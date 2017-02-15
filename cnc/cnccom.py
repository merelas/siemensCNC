#!/usr/bin/env python
#-*- coding:utf-8 -*-

import socket
from tkinter import *

#Siemens communication
# India, Bangalore
# 2017/02/15

__author__ = "Daniel Merelas"
__license__ = "GNU3"
__version__ = "1.0"
__email__ = "daniel@merelas.es"

#Instancia
window = Tk()
window.title('Siemens RPC' + __version__)
window.resizable(False, False)

#Centering the window in the screen
w = window.winfo_reqwidth()
h = window.winfo_reqheight()
ws = window.winfo_screenwidth()
hs = window.winfo_screenheight()
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)
window.geometry('+%d+%d' % (x, y))
