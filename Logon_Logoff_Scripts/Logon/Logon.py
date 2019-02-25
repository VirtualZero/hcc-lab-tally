from time import strftime
import os
import socket

def write_user_info(user_info, name, station_wo_room):
    login_temp = open('\\\\DTEC462-GHOST-3\\Users\\Public\\headcount\\logintemp.' + name + '.txt', 'w+')  
    login_temp.write(user_info)
    login_temp.close()

    login_temp_two = open('\\\\DTEC462-GHOST-3\\Users\\Public\\stationstatus\\' + station_wo_room + '.txt', 'w+')
    login_temp_two.close()

def main():
    name = str(os.getlogin())
    
    date = strftime("%m/%d/%Y")
    time = strftime("%H:%M:%S")
    station = str(socket.gethostname())
    station_wo_room = station.split('-')
    station_wo_room = station_wo_room[1] + '-' + station_wo_room[2]
    print(station_wo_room)
    
    user_info = (station + "\t" + name +
                "\t" + date + '\t' + time)

    write_user_info(user_info, name, station_wo_room)

if __name__ == '__main__':
    main()
