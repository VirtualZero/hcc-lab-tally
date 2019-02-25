from collections import OrderedDict, Counter
import os
from pathlib import Path
from timesort import calculate_hours_logged_on
from threading import Thread


file_by_day_path_list = []

def start_parse():
    
    global file_by_day_path_list

    with open('Session_Log.txt') as session_log:
        reader = session_log.readlines()
        session_log.close()

    date_list = []

    for each_line in reader:
        each_line_split = each_line.split()
        date = each_line_split[2]

        file_path = (date[:2] + '-' + 
                        date[3:5] + '-' + 
                        date[6:] + '.txt') 

        if date not in date_list:
            date_list.append(date)    
            file_by_day_path_list.append(file_path) 

            with open(file_path, 'w+') as daily_log:
                daily_log.write(each_line)
                daily_log.close()

        else:
            with open(file_path, 'a+') as daily_log:
                daily_log.write(each_line)
                daily_log.close()

def crunch(i):
    global file_by_day_path_list

    with open(file_by_day_path_list[i], 'r') as session_log:
        reader = session_log.readlines()
        session_log.close()

    in_and_out_times = extract_times(reader)
    formatted_time = format_time(in_and_out_times)
    sorted_times = calculate_hours_logged_on(formatted_time)

    busy_times = list(sorted_times.keys())
    count = list(sorted_times.values())

    with open('count.' + file_by_day_path_list[i], 'w+') as count_log:
        for i in range(0, len(busy_times)):
            count_log.write(str(busy_times[i]) + '\t' + str(count[i]) + '\n')
        
    count_log.close()  

def find_busy():
    
    global file_by_day_path_list

    crunch_threads = []

    for i in range(len(file_by_day_path_list)):
        process = Thread(target=crunch, kwargs=({"i":i}))
        process.daemon = True
        crunch_threads.append(process)
        process.start()

    [thread.join() for thread in crunch_threads]

    def delete_temp_files(ii):
        os.remove(ii)

    delete_threads = []
    
    for ii in file_by_day_path_list:
        process = Thread(target=delete_temp_files, kwargs={"ii":ii})
        process.daemon = True
        delete_threads.append(process)
        process.start()

    [thread.join() for thread in delete_threads]

def format_time(in_and_out_times):
    formatted_time = []

    for ontime, offtime in in_and_out_times:
        finished_format = [[int(ontime[:2]), int(ontime[3:5])],
                           [int(offtime[:2]), int(offtime[3:5])]]
        formatted_time.append(finished_format)

    return formatted_time

def extract_times(reader):

    only_times = []

    for row in reader:
        times = row.split()[3], row.split()[4]
        only_times.append(times)

    return only_times

def main():
    start_parse()
    find_busy()


if __name__ == '__main__':
    main()