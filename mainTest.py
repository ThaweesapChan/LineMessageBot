import time
import random
import requests
import multiprocessing as mp
import pandas as pd
import os
from threading import Timer
from playsound import playsound
from datetime import datetime as dt
from module.AMYModule import AMY
from module.AMYModule import tool
# /Users/thaweesap/CodingProject/LineATM/venv/bin/python -m pip install playsound

Row = 30      #-1 จาก row สุดท้ายที่มีข้อมูล
Col = 15
upd = 0
updn = 20
timeErors = 1800
amy = AMY(r'test.xlsx',Row,Col)
amy.create_custvariable_data()

def handler():
    print('Error ฟังก์ชั่นทำงานนานผิดปกติ') # ส่งเสียงเเจ้งเตือน
    while True:
        url = ('https://notify-api.line.me/api/notify')
        smg1 = "Error ฟังก์ชั่นทำงานนานผิดปกติ"
        token = "LkRJ4vZlhmkDtW7w24GOvOIIHLH77V8BN5EEbEtYYME"
        filename = "/Users/thaweesap/CodingProject/lineATM2/sound/Alarm sound effect (online-audio-converter.com).wav"
        playsound(filename)
        headers = {'Authorization': 'Bearer ' + token}
        r = requests.post(url, headers=headers, data={'message': smg1})

        print("ส่งแล้ว")
        time.sleep(5)
        exec(open(__file__).read())

def set_timer(time):
    t = Timer(time, handler)
    t.start()
    return t

if (__name__ == '__main__'):
    t = None
    queue_second_count = mp.Queue()
    mp_second_count = mp.Process(target=tool().second_count, args=("",queue_second_count))
    mp_second_count.start()
    print("system started !!!")
