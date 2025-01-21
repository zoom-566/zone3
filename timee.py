import os    
from requests import get,post
try:
  from urllib.parse import urlencode
except:
  os.system('pip install pycryptodome')
try:
  import MedoSigner
except:
  os.system('pip install MedoSigner')
from random import choice,randrange
import http.client
import requests
import re
from time import sleep,time
from user_agent import generate_user_agent
from random import choice,randrange
import os,re
import requests 
try:
	import telebot 
except:
	os.system('pip install telebot')
	os.system('pip install Pytelegrambotapi==3.7.7')
	os.system('clear')
	import telebot
from telebot import types
from uuid import uuid4
import random
from re import *
import json
from user_agent import generate_user_agent
import sys
from datetime import datetime
from bs4 import BeautifulSoup
import datetime
import secrets
import uuid
import binascii,sys
import webbrowser
webbrowser.open('https://t.me/Zzz_9k')
import secrets
try:
	import binascii
except:
	os.system('pip install binascii')
from concurrent.futures import ThreadPoolExecutor
import string
import threading
import time
def compare_phone_time():
    try:
        phone_datetime = datetime.now()
        response = requests.get('http://worldtimeapi.org/api/ip') # HIDE
        data = response.json()
        datetime_str = data['datetime'] # HIDE
        datetime_obj = datetime.strptime(datetime_str, '%Y-%m-%dT%H:%M:%S.%f%z') # HIDE
        timezone_str = data['timezone']
        timezone = pytz.timezone(timezone_str)
        world_datetime = datetime_obj.astimezone(timezone)
        if phone_datetime.date() == world_datetime.date() and phone_datetime.time().replace(second=0, microsecond=0) == world_datetime.time().replace(second=0, microsecond=0):
            os.system("clear")
        else:
            print("ليش مرجع تاريخ الجهاز؟ 🐧")
            sys.exit()
    except Exception as e:
        print(f"حدث خطأ: {e}")
compare_phone_time()
import requests,time,pyfiglet,datetime
now = datetime.datetime.today() # HIDE
now = datetime.datetime.today()
mm = str(now.month) # HIDE
dd = str(now.day)
yyyy = str(now.year) # HIDE
hour = str(now.hour)
mi = str(now.minute)
ss = str(now.second)
t=(mm + "/" + dd + "/" + yyyy + " " + hour + ":" + mi + ":" + ss) # HIDE
hours = (now.hour)
x = datetime.datetime.now()
g= datetime.datetime(2025, 1, 22, 12, 0 ,0) # HIDE
if (x.strftime("%x"))>(g.strftime("%x")): # HIDE
 print('\033[1;32m تم ايقاف الاداه راسل المطوره ࢪيفن') # HIDE
 exit()
else:
 	print(" ")
 	os.system("clear")
