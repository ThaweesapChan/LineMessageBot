import time
import random
import requests
import multiprocessing as mp
import pandas as pd
from datetime import datetime as dt
import os


picture_path = "/Users/thaweesap/codingProject/LineATM/picture"  # ตั้งค่า path ของโฟลเดอร์ที่มีรูปภาพ
list_name_img = os.listdir(picture_path)  # ดึงชื่อไฟล์รูปภาพทั้งหมดจากโฟลเดอร์

class tool:
    def __init__(self):
        pass

    def ToList(self, args):
        export = list(args.split(" "))
        return export

    def second_count(self,str_blank, queue):
        second = 0
        while True:
            second += 1
            time.sleep(1)
            if (second == 60):
                second = 0
            queue.put(second)

class AMY:
    def __init__(self, file_xlsx, run_rows, run_column):
        self.file_xlsx  = file_xlsx
        self.run_rows   = run_rows
        self.run_column = run_column

    def create_custvariable_data(self):
        dataframe = pd.read_excel(self.file_xlsx)
        index_row = -1
        for row in range(self.run_rows):
            index_column = -1
            index_row += 1
            check_var = str(dataframe.iloc[index_row, 0])

            if check_var != "nan":
                for column in range(self.run_column):  # run_column =8
                    index_column += 1
                    dataframe.iloc[index_row, index_column]
                    if column == 0:
                        value1 = dataframe.iloc[index_row, index_column]
                    if column == 1:
                        value2 = dataframe.iloc[index_row, index_column]
                    if column == 2:
                        value3 = dataframe.iloc[index_row, index_column]
                    if column == 3:
                        value4 = dataframe.iloc[index_row, index_column]
                    if column == 4:
                        value5 = dataframe.iloc[index_row, index_column]
                    if column == 5:
                        value6 = dataframe.iloc[index_row, index_column]
                    if column == 6:
                        value7 = dataframe.iloc[index_row, index_column]
                    if column == 7:
                        value8 = dataframe.iloc[index_row, index_column]
                    if column == 8:
                        value9 = dataframe.iloc[index_row, index_column]
                    if column == 9:
                        value10 = dataframe.iloc[index_row, index_column]
                    if column == 10:
                        value11 = dataframe.iloc[index_row, index_column]
                    if column == 11:
                        value12 = dataframe.iloc[index_row, index_column]
                    if column == 12:
                        value13 = dataframe.iloc[index_row, index_column]
                    if column == 13:
                        value14 = dataframe.iloc[index_row, index_column]
                    if column == 14:
                        value15 = dataframe.iloc[index_row, index_column]
                        value16 = 0
                        value17 = random.randint(1, value4)
                        cust_command = {'cust_name':value2,'status':value1,'time_0':value16,'time_setup':value17,'min_rand':value3,'max_rand':value4,
                                        'start_time':value6,'end_time':value7,'off_on_day':value5,'cust_contact':value8,
                                        'ref_token':value9,'list_Tokens':value10,'str_mesage1':value11,'str_mesage2':value12,
                                        'str_mesage3':value13,'str_name_img':value14,'linkID':value15
                                        }
                        globals()[f"cust_command{row}"] = cust_command

    def cust_gb_dt(self,i):
        global status, cust_name, ref_token, start_time, end_time, off_on_day, list_Tokens, str_mesage1,str_mesage2,str_mesage3, list_name_img, linkID, time_setup, time_0
        status          = str(globals()[f"cust_command{i}"]['status'])
        cust_name       = str(globals()[f"cust_command{i}"]['cust_name'])
        str_ref_token   = str(globals()[f"cust_command{i}"]['ref_token'])
        start_time      = int(globals()[f"cust_command{i}"]['start_time'])
        end_time        = int(globals()[f"cust_command{i}"]['end_time'])
        str_mesage2     = str(globals()[f"cust_command{i}"]['str_mesage2']).format(Enter='\n')
        str_mesage3     = str(globals()[f"cust_command{i}"]['str_mesage3']).format(Enter='\n')
        str_name_img    = str(globals()[f"cust_command{i}"]['str_name_img'])
        list_name_img   = tool().ToList(str_name_img)
        linkID          = str(globals()[f"cust_command{i}"]['linkID']).format( Enter = '\n')
        time_0          = int(globals()[f"cust_command{i}"]['time_0'])


        if status == "on":
            srt_list_Tokens = str(globals()[f"cust_command{i}"]['list_Tokens'])
            ref_token   = tool().ToList(str_ref_token)
            list_Tokens = tool().ToList(srt_list_Tokens)
            time_setup  = int(globals()[f"cust_command{i}"]['time_setup'])

        if status == "test":
            ref_token   = ['LkRJ4vZlhmkDtW7w24GOvOIIHLH77V8BN5EEbEtYYME']
            list_Tokens = ['FW55n2DQYhVaKBiKnQhdn6ybQ5P1WoUl6YU8uDjAvja']
            time_setup  = 1
            globals()[f"cust_command{i}"].update({'time_0': time_setup})
            globals()[f"cust_command{i}"].update({'time_setup': time_setup})

            # s9f33OMb6t6pPLQDY06sn8m8WAlUfRStb4TpH8Eftx3 2OT2D2E96U62xAAq3El14T1CKaNckOfX1MbdpGGWpxb FW55n2DQYhVaKBiKnQhdn6ybQ5P1WoUl6YU8uDjAvja
            # OsqC7Y8T55DM4Htc0IqwyJs0pxOeLxOzj7xob6ecrj0 fJkVMMZg4QHUUOXDUQ0IgITiCsThcCQZdzvNQdiqoqI UUqjiMKxdeIHuZ0jdNHQ3Pa8Q6fsUSdIHxjT2GTQJeW
        if status != "on" and status != "test":
            ref_token = ['JYd6po7Ejcb3v4YOhhhTGeVzYoLbkpJq3OIZacaxCnz']
            list_Tokens = ['']
            time_setup = 1
            globals()[f"cust_command{i}"].update({'time_0': time_setup})
            globals()[f"cust_command{i}"].update({'time_setup': time_setup})

        return status, cust_name, ref_token, start_time, end_time, off_on_day, list_Tokens, str_mesage1, str_mesage2, str_mesage3, list_name_img, linkID, time_setup, time_0

    def datetime(self):
        global date_time, int_date_time_Hour, date_time_is_the_day
        Gtime = dt.now()
        date_time = Gtime.strftime("%d/%m/%y %H.%M ")
        date_time_is_the_day = Gtime.strftime("%A")
        date_time_Hour = Gtime.strftime("%H")
        int_date_time_Hour = int(date_time_Hour)

    def time_0(self, i):
        globals()[f"cust_command{i}"].update({'time_0': 0})

    def time_01(self,i):
        time_counters = int(globals()[f"cust_command{i}"]['time_0'])
        update_time_counters = time_counters + 1
        globals()[f"cust_command{i}"].update({'time_0': update_time_counters})

    def time_setup_new(self,i):
        min_rand = int(globals()[f"cust_command{i}"]['min_rand'])
        max_rand = int(globals()[f"cust_command{i}"]['max_rand'])
        update_time_setup = random.randint(min_rand, max_rand)
        globals()[f"cust_command{i}"].update({'time_setup': update_time_setup})

    def conditionsMethod(self):
        list_on_of_day  = set(off_on_day)
        to_day_is       = set(tool().ToList(date_time_is_the_day))
        lenn            = len(to_day_is.intersection(list_on_of_day))
        if time_0 >= time_setup and status == "on" or status == "test":
            #17/10/65 เพิ่ม try except จุดนี้ คือถ้าผิดพลาดให้ return false แต่ถ้ายังแก้ไม่ได้ให้ลอง return ture หมายถึงให้รีเลขนับเวลาใหม่

            try:
                # เวลาเริ่ม เท่ากับ เวลาจบ = ส่งตลอด 24 ชม.
                if lenn == 0 and start_time == end_time:
                    print(date_time, cust_name," ",status,"ส่ง 24 ชม.")
                    sentmessage().SentMSG()
                    sentmessage().Notify()
                    print(date_time, " ส่งข้อความข้อง ", cust_name,"จำนวน : ",count_sent+1," กลุ่ม","\n")
                    return True
                # เวลาเริ่ม มากกว่า เวลาจบ = ส่งภายในวันนั้น ๆ ไม่เกินเที่ยงคืน ให้ส่งหลังเวลาเริ่มและหยุดที่เวลาจบ
                if lenn == 0 and start_time <= int_date_time_Hour < end_time :
                    print(date_time, cust_name," ",status,"ส่งภายในวันนั้น")
                    sentmessage().SentMSG()
                    sentmessage().Notify()
                    print(date_time, " ส่งข้อความข้อง ", cust_name,"จำนวน : ",count_sent+1," กลุ่ม","\n")
                    return True
                # เวลาเริ่ม น้อยกว่า เวลาจบ = ส่งข้ามระหว่างคืน ส่วนของช่วงเช้าให้ส่งหลังเวลาเริ่ม str - 23
                if lenn == 0 and start_time >= end_time and int_date_time_Hour >= start_time:
                    print(date_time, cust_name," ",status,"ส่งข้ามคืน ส่วนของก่อนเที่ยงคืน")
                    sentmessage().SentMSG()
                    sentmessage().Notify()
                    print(date_time, " ส่งข้อความข้อง ", cust_name,"จำนวน : ",count_sent+1," กลุ่ม","\n")
                    return True
                # เวลาเริ่ม น้อยกว่า เวลาจบ = ส่งข้ามระหว่างคืน ส่วนของหลังเที่ยงคืนให้ส่งก่่อนเวลาจบ 0 - end
                if lenn == 0 and start_time >= end_time and int_date_time_Hour < end_time:
                    print(date_time, cust_name," ",status,"ส่งข้ามคืน ส่วนของหลังเที่ยงคืน")
                    sentmessage().SentMSG()
                    sentmessage().Notify()
                    print(date_time, " ส่งข้อความข้อง ", cust_name,"จำนวน : ",count_sent+1," กลุ่ม","\n")
                    return True
            except:
                print("!!!!!!!!!!!!!!!!! Error !!!!!!!!!!!!!!!!! \n",date_time,"error : ",cust_name,"ส่งไป : ",count_sent," กลุ่มก่อน error","\n\n")
                return True

    def update_status(self):
        while True:
            dataframe = pd.read_excel(self.file_xlsx)
            index_row = -1
            for row in range(self.run_rows):
                index_column = -1
                index_row += 1
                check_var = str(dataframe.iloc[index_row, 0])
                if check_var != "nan":
                    for column in range(self.run_column):  # run_column =8
                        index_column += 1
                        dataframe.iloc[index_row, index_column]
                        if column == 0:
                            value1 = dataframe.iloc[index_row, index_column]
                        if column == 1:
                            value2 = dataframe.iloc[index_row, index_column]
                        if column == 2:
                            value3 = dataframe.iloc[index_row, index_column]
                        if column == 3:
                            value4 = dataframe.iloc[index_row, index_column]
                        if column == 4:
                            value5 = dataframe.iloc[index_row, index_column]
                        if column == 5:
                            value6 = dataframe.iloc[index_row, index_column]
                        if column == 6:
                            value7 = dataframe.iloc[index_row, index_column]
                        if column == 7:
                            value8 = dataframe.iloc[index_row, index_column]
                        if column == 8:
                            value9 = dataframe.iloc[index_row, index_column]
                        if column == 9:
                            value10 = dataframe.iloc[index_row, index_column]
                        if column == 10:
                            value11 = dataframe.iloc[index_row, index_column]
                        if column == 11:
                            value12 = dataframe.iloc[index_row, index_column]
                        if column == 12:
                            value13 = dataframe.iloc[index_row, index_column]
                        if column == 13:
                            value14 = dataframe.iloc[index_row, index_column]
                        if column == 14:
                            value15 = dataframe.iloc[index_row, index_column]
                            cust_command = {
                                'cust_name' :value2,'status':value1,'start_time':value6,'end_time':value7,'min_rand':value3,
                                'max_rand':value4,'off_on_day':value5,'cust_contact':value8,'ref_token': value9,'list_Tokens': value10,
                                'str_mesage1': value11,'str_mesage2':value12,'str_mesage3':value13,'str_name_img':value14,'linkID':value15
                            }
                            globals()[f"cust_command{row}"].update({'cust_name' :value2})
                            globals()[f"cust_command{row}"].update({'status':value1})
                            globals()[f"cust_command{row}"].update({'start_time':value6})
                            globals()[f"cust_command{row}"].update({'end_time':value7})
                            globals()[f"cust_command{row}"].update({'min_rand':value3})
                            globals()[f"cust_command{row}"].update({'max_rand':value4})
                            globals()[f"cust_command{row}"].update({'off_on_day':value5})
                            globals()[f"cust_command{row}"].update({'cust_contact':value8})
                            globals()[f"cust_command{row}"].update({'ref_token': value9})
                            globals()[f"cust_command{row}"].update({'list_Tokens': value10})
                            globals()[f"cust_command{row}"].update({'str_mesage1': value11})
                            globals()[f"cust_command{row}"].update({'str_mesage2':value12})
                            globals()[f"cust_command{row}"].update({'str_mesage3':value13})
                            globals()[f"cust_command{row}"].update({'str_name_img':value14})
                            globals()[f"cust_command{row}"].update({'linkID':value15})
                            print (globals()[f"cust_command{row}"])
            print("\n",date_time," update status complete !!! ","\n")
            break

class sentmessage:

    def SentMSG(self):
        global count_sent
        url = ('https://notify-api.line.me/api/notify')
        messsage = [str_mesage1,str_mesage2,str_mesage3]
        count_sent = 0
        # ข้อความ
        if list_name_img == ['nan']:
            print("# ข้อความ")
            for i, token in enumerate(list_Tokens):
                count_sent += 1
                for i, smg in enumerate(messsage):
                    if smg != "nan":
                        headers = {'Authorization': 'Bearer ' + token}
                        r = requests.post(url, headers=headers, data={'message': smg})

        # ข้อความ + รูป
        if list_name_img != ['nan'] and linkID == 'nan':
            print("# ข้อความ + รูป")
            for i, token in enumerate(list_Tokens):
                count_sent += 1
                for i, smg in enumerate(messsage):
                    if smg != "nan":
                        headers = {'Authorization': 'Bearer ' + token}
                        r = requests.post(url, headers=headers, data={'message': smg})
                for i, picture in enumerate(list_name_img):
                    r = requests.post(url, headers=headers, data={'message': " "},
                                      files={'imageFile': open(os.path.join(picture_path, picture), 'rb')})

        # ข้อความ + รูป + ลิงค์ปิดท้าย
        if list_name_img != ['nan'] and linkID != 'nan':
            print("# ข้อความ + รูป + ลิงค์ปิดท้าย")
            num_img = len(list_name_img) - 1
            for i, token in enumerate(list_Tokens):
                count_sent += 1
                for i, smg in enumerate(messsage):
                    if smg != "nan":
                        headers = {'Authorization': 'Bearer ' + token}
                        r = requests.post(url, headers=headers, data={'message': smg})
                for i, picture in enumerate(list_name_img):
                    if i == num_img:
                        r = requests.post(url, headers=headers, data={'message': linkID},
                                          files={'imageFile': open(os.path.join(picture_path, picture), 'rb')})
                    else:
                        r = requests.post(url, headers=headers, data={'message': " "},
                                          files={'imageFile': open(os.path.join(picture_path, picture), 'rb')})

    def Notify(self):
        url  = ('https://notify-api.line.me/api/notify')
        smg1 = "\nส่งข้อความเรียบร้อยค่ะ คุณสามารถตรวจสอบข้อความได้ในกลุ่มของคุณ"
        smg2 = "เริ่มส่งข้อความของวันนี้ค่ะ"
        smg3 = "สิ้นสุดการทำงานของวันนี้ค่ะ"
        for i, token in enumerate(ref_token):
            headers = {'Authorization': 'Bearer ' + token}
            r = requests.post(url, headers=headers, data={'message': smg1})
        print('แจ้งเตือน Notify!!!')