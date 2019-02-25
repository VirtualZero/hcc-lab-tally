from pathlib import Path
from time import strftime
import os
import socket

def main():
    name = str(os.getlogin())
    path = Path('\\\\DTEC462-GHOST-3\\Users\\Public\\headcount\\logintemp.' + name + '.txt')
    
    station = str(socket.gethostname())
    station_wo_room = station.split('-')
    station_wo_room = station_wo_room[1] + '-' + station_wo_room[2]
    os.remove('\\\\DTEC462-GHOST-3\\Users\\Public\\stationstatus\\' + station_wo_room + '.txt')

    
    if path.is_file():
        login = open(path)
        login_data = login.read()
        login_data= login_data.strip()

        string_time = strftime('%H:%M:%S')
        formatted_time = '\t' + string_time

        logPath = open('\\\\DTEC462-GHOST-3\\Users\\Public\\headcount\\Session_Log.txt', 'a+')
        logPath.write('\n' + login_data + formatted_time)
        logPath.close()
        login.close()

        os.remove(path)

if __name__ == '__main__':
    main()
