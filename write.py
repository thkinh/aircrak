import subprocess
from io import StringIO

bssid = ""
chanel = ""
cmd = ""
choose = 0
buffer = StringIO()
wifi_card = []

def pause_func(time):
    for i in range(time):
        print("", end="")

def get_wificard():
    for line in buffer.getvalue().splitlines():
        if line.startswith(" "):
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
    print("Successfully wrote into buffer: ")
    input("Press ENTER key...")

def Run_With_timeout(cmd, time):
    try:
        subprocess.run(cmd, shell=True, timeout=time)
    except subprocess.TimeoutExpired:
        print(f"Timeout expired for command: {cmd}")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        print("End")

get_buffer()

while choose != -1:
    subprocess.run('clear', shell=True)
    choose = int(input("Nhap lenh: ")) 

    if choose == 1: 
        get_wificard()
        if len(wifi_card) == 0:
            print("No wifi card captured")
        for card in wifi_card:
            print(card)
        whichcard = int(input("Nhap card can chon: "))
        cmd = f"ifconfig {wifi_card[whichcard]} up"
        subprocess.run(cmd, shell=True)

    if choose == 2:
        if wifi_card:
            for card in wifi_card:
                print(card)
            whichcard = int(input("Nhap card can chon: "))
            cmd = f"airmon-ng start {wifi_card[whichcard]}"
            subprocess.run(cmd, shell=True)
            wifi_card[whichcard] += "mon"
        else:
            print("No wifi card captured")
            pause_func(999999)

    if choose == 3:
        if wifi_card:
            for card in wifi_card:
                print(card)
            whichcard = int(input("Nhap card can chon: "))
            cmd = f"airodump-ng {wifi_card[whichcard]}"
            Run_With_timeout(cmd, 5)

        choose = 0
        print("Da toi day")
        pause_func(1234567)

buffer.close()
