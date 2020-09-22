import os
import time
import sys
from datetime import datetime
from datetime import date

def getRAMinfo():
    p = os.popen('free') # CPU informatiom 
    i = 0
    while 1:
        i = i + 1
        line = p.readline() # RAM information 
        if i == 2:
            return(line.split()[1:4])

def main():
    try:
        my_file = open("test-print.txt", 'a')
    except FileNotFoundError:
        print("Permissions prohibit. Program aborted.")
        sys.exit()
        
    RAM_stats0 = getRAMinfo()
    RAM_total0 = str(round(int(RAM_stats0[0]) / 1000,1))
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    
    my_file.write("\nThis file is the log of RAM usage.")
    my_file.write("\n" + str(now))
    my_file.write("\nRAM Total = " + str(RAM_total0)+" MB")
    my_file.write("\n {:12} {:12} {:18}".format("Used(MB)", "Used(%)", "Time"))
    
    while True:
        time.sleep(2)
        
        RAM_stats = getRAMinfo()
        RAM_total = str(round(int(RAM_stats[0]) / 1000,1))
        RAM_used = str(round(int(RAM_stats[1]) / 1000,1)) 
        RAM_free = str(round(int(RAM_stats[2]) / 1000,1))
        RAM_perc = str(round(float(RAM_stats[1])/float(RAM_stats[0]) * 100, 2))
        now = str(datetime.now())
        
        print('')
        print('RAM Total = ' + str(RAM_total)+' MB, ' + 'RAM Used = '+str(RAM_used)+' MB, ' + 'RAM Free = '+str(RAM_free)+' MB')
        print(now)
    
        my_file = open("test-print.txt", 'a')
        my_file.write("\n{:12} {:12} {:18}".format(RAM_used, RAM_perc, now))

if __name__ == '__main__':
    main()
