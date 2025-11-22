from __future__ import print_function
import locale
import threading
#import PySimpleGUI as sg

#locale.setlocale(locale.LC_ALL, 'C-UTF-8')
import cv2 as cv
from camera_test import camOn
from time import sleep
from dofbot_config import *
from ipywidgets import interact, interactive, fixed, interact_manual
import ipywidgets as widgets
from IPython.display import display

camOn()
#creating and updating hsv instance
update_hsv = update_hsv()
#initalize num parameter
num=0
#initialize mode
model = "General"
#initialize name
HSV_name=None
#initialize default HSV values
color_hsv = {"red" : ((0,143, 163), (11, 255, 255)),
	"green" : ((55, 80, 66), (78, 255, 255)),
	"blue" : ((110, 100, 121), (117, 255, 255)),
	"yellow": ((26, 100, 91), (32, 255, 255))}
#pathway for hsv parameters
HSV_path="/home/pi/PCC_Hackathon/HSV_config.txt"
#attempt to read and write
try: read_HSV(HSV_path, color_hsv)
except Exception: print("No HSV_config file!!")
button_layout = widgets.Layout(width='320px',height='55px',align_self='center')
output = widgets.Output()
#Color update buttons
HSV_update_red= widgets.Button(description='HSV_update_red',button_style='success',layout=button_layout)
H_min_slider=widgets.IntSlider(description='H_min:',value=0,min=0,max=255,step=1, orientation='horizontal')


exit_button=widgets.Button(description='Exit',button_style='danger',layout=button_layout)
window = sg.Window('HSV config', layout)
while True:
	event, values = window.read()
	if event == sg.WIN_CLOSED or event == 'Exit':
		break
	elif event == 'Success':
		pass

window.close()
