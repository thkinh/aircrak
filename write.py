import sys
from io import StringIO
import os
import subprocess
bssid = ""
chanel = ""
cmd = ""
choose = 0
buffer = StringIO()
wifi_card = []
def pause_func(time):
    for i in range(time):
        print("",end = "")

def get_wificard():
    for line in buffer.getvalue().splitlines():
        if line.startswith(" ") == True:
            continue
        data = line.split()
        if data:
            wifi_card.append(str(data[0]))
    return wifi_card

def get_buffer():
    cmd = 'iwconfig'
    result = subprocess.run(cmd, capture_output=True, text=True)
    buffer.write(result.stdout)
    print(buffer.getvalue())
    print("Succesfully wrote into buffer: ")
    cmd = input("Press ENTER key...")


get_buffer()
while(choose!=-1):
    subprocess.run('clear')
    choose = int(input("nhap lenh: ")) 
    if choose == 1: 
        get_wificard()
        if len(wifi_card) == 0:
            print("No wifi card captured")
        for card in wifi_card:
            print(card)
        whichcard = int(input("Nhap card can chon: "))
        cmd = "ifconfig " + str(wifi_card[whichcard]) + " up"
        choose = 0
        #Sau sua thanh subprocess.run()
        print(cmd)
        pause_func(1090000)
    if choose == 2:
        if wifi_card:
            for card in wifi_card:
                print(card)
            whichcard = int(input("Nhap card can chon: "))
            cmd = "airmon-ng start " + str(wifi_card[whichcard])
            print(cmd)
            pause_func(8888888)
        else:
            print("No wifi card captured")
            pause_func(7777777)
    if choose ==  3:
        
buffer.close()
