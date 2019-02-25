from collections import OrderedDict, Counter


def calculate_hours_logged_on(formatted_time):
    time_dictionary = {'7:30': 0, '8:00': 0, '8:30': 0, '9:00': 0,
                       '9:30': 0, '10:00': 0, '10:30': 0, '11:00': 0,
                       '11:30': 0, '12:00': 0, '12:30': 0, '13:00': 0,
                       '13:30': 0, '14:00': 0, '14:30': 0, '15:00': 0,
                       '15:30': 0, '16:00': 0, '16:30': 0, '17:00': 0,
                       '17:30': 0, '18:00': 0, '18:30': 0, '19:00': 0,
                       '19:30': 0, '20:00': 0, '20:30': 0, '21:00': 0,
                       '21:30': 0}

    for logon, logoff in formatted_time:
        if logon[0] == 7 and 30 <= logon[1] < 60:
            time_dictionary['7:30'] += 1

            if logoff[0] == logon[0] + 1:
                if 30 > logoff[1] >= 0:
                    time_dictionary['8:00'] += 1

                elif 30 <= logon[1] < 60:
                    time_dictionary['8:00'] += 1
                    time_dictionary['8:30'] += 1

            elif logoff[0] == logon[0] + 2:
                if 30 > logoff[1] >= 0:
                    time_dictionary['8:00'] += 1
                    time_dictionary['8:30'] += 1
                    time_dictionary['9:00'] += 1

                elif 30 <= logon[1] < 60:
                    time_dictionary['8:00'] += 1
                    time_dictionary['8:30'] += 1
                    time_dictionary['9:00'] += 1
                    time_dictionary['9:30'] += 1

            elif logoff[0] == logon[0] + 3:
                if 30 > logoff[1] >= 0:
                    time_dictionary['8:00'] += 1
                    time_dictionary['8:30'] += 1
                    time_dictionary['9:00'] += 1
                    time_dictionary['9:30'] += 1
                    time_dictionary['10:00'] += 1

                elif 30 <= logon[1] < 60:
                    time_dictionary['8:00'] += 1
                    time_dictionary['8:30'] += 1
                    time_dictionary['9:00'] += 1
                    time_dictionary['9:30'] += 1
                    time_dictionary['10:00'] += 1
                    time_dictionary['10:30'] += 1

            elif logoff[0] == logon[0] + 4:
                if 30 > logoff[1] >= 0:
                    time_dictionary['8:00'] += 1
                    time_dictionary['8:30'] += 1
                    time_dictionary['9:00'] += 1
                    time_dictionary['9:30'] += 1
                    time_dictionary['10:00'] += 1
                    time_dictionary['10:30'] += 1
                    time_dictionary['11:00'] += 1

                elif 30 <= logon[1] < 60:
                    time_dictionary['8:00'] += 1
                    time_dictionary['8:30'] += 1
                    time_dictionary['9:00'] += 1
                    time_dictionary['9:30'] += 1
                    time_dictionary['10:00'] += 1
                    time_dictionary['10:30'] += 1
                    time_dictionary['11:00'] += 1
                    time_dictionary['11:30'] += 1

            elif logoff[0] == logon[0] + 5:
                if 30 > logoff[1] >= 0:
                    time_dictionary['8:00'] += 1
                    time_dictionary['8:30'] += 1
                    time_dictionary['9:00'] += 1
                    time_dictionary['9:30'] += 1
                    time_dictionary['10:00'] += 1
                    time_dictionary['10:30'] += 1
                    time_dictionary['11:00'] += 1
                    time_dictionary['11:30'] += 1
                    time_dictionary['12:00'] += 1

                elif 30 <= logon[1] < 60:
                    time_dictionary['8:00'] += 1
                    time_dictionary['8:30'] += 1
                    time_dictionary['9:00'] += 1
                    time_dictionary['9:30'] += 1
                    time_dictionary['10:00'] += 1
                    time_dictionary['10:30'] += 1
                    time_dictionary['11:00'] += 1
                    time_dictionary['11:30'] += 1
                    time_dictionary['12:00'] += 1
                    time_dictionary['12:30'] += 1

            elif logoff[0] == logon[0] + 6:
                if 30 > logoff[1] >= 0:
                    time_dictionary['8:00'] += 1
                    time_dictionary['8:30'] += 1
                    time_dictionary['9:00'] += 1
                    time_dictionary['9:30'] += 1
                    time_dictionary['10:00'] += 1
                    time_dictionary['10:30'] += 1
                    time_dictionary['11:00'] += 1
                    time_dictionary['11:30'] += 1
                    time_dictionary['12:00'] += 1
                    time_dictionary['12:30'] += 1
                    time_dictionary['13:00'] += 1

                elif 30 <= logon[1] < 60:
                    time_dictionary['8:00'] += 1
                    time_dictionary['8:30'] += 1
                    time_dictionary['9:00'] += 1
                    time_dictionary['9:30'] += 1
                    time_dictionary['10:00'] += 1
                    time_dictionary['10:30'] += 1
                    time_dictionary['11:00'] += 1
                    time_dictionary['11:30'] += 1
                    time_dictionary['12:00'] += 1
                    time_dictionary['12:30'] += 1
                    time_dictionary['13:00'] += 1
                    time_dictionary['13:30'] += 1

            elif logoff[0] == logon[0] + 7:
                if 30 > logoff[1] >= 0:
                    time_dictionary['8:00'] += 1
                    time_dictionary['8:30'] += 1
                    time_dictionary['9:00'] += 1
                    time_dictionary['9:30'] += 1
                    time_dictionary['10:00'] += 1
                    time_dictionary['10:30'] += 1
                    time_dictionary['11:00'] += 1
                    time_dictionary['11:30'] += 1
                    time_dictionary['12:00'] += 1
                    time_dictionary['12:30'] += 1
                    time_dictionary['13:00'] += 1
                    time_dictionary['13:30'] += 1
                    time_dictionary['14:00'] += 1

                elif 30 <= logon[1] < 60:
                    time_dictionary['8:00'] += 1
                    time_dictionary['8:30'] += 1
                    time_dictionary['9:00'] += 1
                    time_dictionary['9:30'] += 1
                    time_dictionary['10:00'] += 1
                    time_dictionary['10:30'] += 1
                    time_dictionary['11:00'] += 1
                    time_dictionary['11:30'] += 1
                    time_dictionary['12:00'] += 1
                    time_dictionary['12:30'] += 1
                    time_dictionary['13:00'] += 1
                    time_dictionary['13:30'] += 1
                    time_dictionary['14:00'] += 1
                    time_dictionary['14:30'] += 1

            elif logoff[0] == logon[0] + 8:
                if 30 > logoff[1] >= 0:
                    time_dictionary['8:00'] += 1
                    time_dictionary['8:30'] += 1
                    time_dictionary['9:00'] += 1
                    time_dictionary['9:30'] += 1
                    time_dictionary['10:00'] += 1
                    time_dictionary['10:30'] += 1
                    time_dictionary['11:00'] += 1
                    time_dictionary['11:30'] += 1
                    time_dictionary['12:00'] += 1
                    time_dictionary['12:30'] += 1
                    time_dictionary['13:00'] += 1
                    time_dictionary['13:30'] += 1
                    time_dictionary['14:00'] += 1
                    time_dictionary['14:30'] += 1
                    time_dictionary['15:00'] += 1

                elif 30 <= logon[1] < 60:
                    time_dictionary['8:00'] += 1
                    time_dictionary['8:30'] += 1
                    time_dictionary['9:00'] += 1
                    time_dictionary['9:30'] += 1
                    time_dictionary['10:00'] += 1
                    time_dictionary['10:30'] += 1
                    time_dictionary['11:00'] += 1
                    time_dictionary['11:30'] += 1
                    time_dictionary['12:00'] += 1
                    time_dictionary['12:30'] += 1
                    time_dictionary['13:00'] += 1
                    time_dictionary['13:30'] += 1
                    time_dictionary['14:00'] += 1
                    time_dictionary['14:30'] += 1
                    time_dictionary['15:00'] += 1
                    time_dictionary['15:30'] += 1

            elif logoff[0] == logon[0] + 9:
                if 30 > logoff[1] >= 0:
                    time_dictionary['8:00'] += 1
                    time_dictionary['8:30'] += 1
                    time_dictionary['9:00'] += 1
                    time_dictionary['9:30'] += 1
                    time_dictionary['10:00'] += 1
                    time_dictionary['10:30'] += 1
                    time_dictionary['11:00'] += 1
                    time_dictionary['11:30'] += 1
                    time_dictionary['12:00'] += 1
                    time_dictionary['12:30'] += 1
                    time_dictionary['13:00'] += 1
                    time_dictionary['13:30'] += 1
                    time_dictionary['14:00'] += 1
                    time_dictionary['14:30'] += 1
                    time_dictionary['15:00'] += 1
                    time_dictionary['15:30'] += 1
                    time_dictionary['16:00'] += 1

                elif 30 <= logon[1] < 60:
                    time_dictionary['8:00'] += 1
                    time_dictionary['8:30'] += 1
                    time_dictionary['9:00'] += 1
                    time_dictionary['9:30'] += 1
                    time_dictionary['10:00'] += 1
                    time_dictionary['10:30'] += 1
                    time_dictionary['11:00'] += 1
                    time_dictionary['11:30'] += 1
                    time_dictionary['12:00'] += 1
                    time_dictionary['12:30'] += 1
                    time_dictionary['13:00'] += 1
                    time_dictionary['13:30'] += 1
                    time_dictionary['14:00'] += 1
                    time_dictionary['14:30'] += 1
                    time_dictionary['15:00'] += 1
                    time_dictionary['15:30'] += 1
                    time_dictionary['16:00'] += 1
                    time_dictionary['16:30'] += 1

            elif logoff[0] == logon[0] + 10:
                if 30 > logoff[1] >= 0:
                    time_dictionary['8:00'] += 1
                    time_dictionary['8:30'] += 1
                    time_dictionary['9:00'] += 1
                    time_dictionary['9:30'] += 1
                    time_dictionary['10:00'] += 1
                    time_dictionary['10:30'] += 1
                    time_dictionary['11:00'] += 1
                    time_dictionary['11:30'] += 1
                    time_dictionary['12:00'] += 1
                    time_dictionary['12:30'] += 1
                    time_dictionary['13:00'] += 1
                    time_dictionary['13:30'] += 1
                    time_dictionary['14:00'] += 1
                    time_dictionary['14:30'] += 1
                    time_dictionary['15:00'] += 1
                    time_dictionary['15:30'] += 1
                    time_dictionary['16:00'] += 1
                    time_dictionary['16:30'] += 1
                    time_dictionary['17:00'] += 1

                elif 30 <= logon[1] < 60:
                    time_dictionary['8:00'] += 1
                    time_dictionary['8:30'] += 1
                    time_dictionary['9:00'] += 1
                    time_dictionary['9:30'] += 1
                    time_dictionary['10:00'] += 1
                    time_dictionary['10:30'] += 1
                    time_dictionary['11:00'] += 1
                    time_dictionary['11:30'] += 1
                    time_dictionary['12:00'] += 1
                    time_dictionary['12:30'] += 1
                    time_dictionary['13:00'] += 1
                    time_dictionary['13:30'] += 1
                    time_dictionary['14:00'] += 1
                    time_dictionary['14:30'] += 1
                    time_dictionary['15:00'] += 1
                    time_dictionary['15:30'] += 1
                    time_dictionary['16:00'] += 1
                    time_dictionary['16:30'] += 1
                    time_dictionary['17:00'] += 1
                    time_dictionary['17:30'] += 1

            elif logoff[0] == logon[0] + 11:
                if 30 > logoff[1] >= 0:
                    time_dictionary['8:00'] += 1
                    time_dictionary['8:30'] += 1
                    time_dictionary['9:00'] += 1
                    time_dictionary['9:30'] += 1
                    time_dictionary['10:00'] += 1
                    time_dictionary['10:30'] += 1
                    time_dictionary['11:00'] += 1
                    time_dictionary['11:30'] += 1
                    time_dictionary['12:00'] += 1
                    time_dictionary['12:30'] += 1
                    time_dictionary['13:00'] += 1
                    time_dictionary['13:30'] += 1
                    time_dictionary['14:00'] += 1
                    time_dictionary['14:30'] += 1
                    time_dictionary['15:00'] += 1
                    time_dictionary['15:30'] += 1
                    time_dictionary['16:00'] += 1
                    time_dictionary['16:30'] += 1
                    time_dictionary['17:00'] += 1
                    time_dictionary['17:30'] += 1
                    time_dictionary['18:00'] += 1

                elif 30 <= logon[1] < 60:
                    time_dictionary['8:00'] += 1
                    time_dictionary['8:30'] += 1
                    time_dictionary['9:00'] += 1
                    time_dictionary['9:30'] += 1
                    time_dictionary['10:00'] += 1
                    time_dictionary['10:30'] += 1
                    time_dictionary['11:00'] += 1
                    time_dictionary['11:30'] += 1
                    time_dictionary['12:00'] += 1
                    time_dictionary['12:30'] += 1
                    time_dictionary['13:00'] += 1
                    time_dictionary['13:30'] += 1
                    time_dictionary['14:00'] += 1
                    time_dictionary['14:30'] += 1
                    time_dictionary['15:00'] += 1
                    time_dictionary['15:30'] += 1
                    time_dictionary['16:00'] += 1
                    time_dictionary['16:30'] += 1
                    time_dictionary['17:00'] += 1
                    time_dictionary['17:30'] += 1
                    time_dictionary['18:00'] += 1
                    time_dictionary['18:30'] += 1

            elif logoff[0] == logon[0] + 12:
                if 30 > logoff[1] >= 0:
                    time_dictionary['8:00'] += 1
                    time_dictionary['8:30'] += 1
                    time_dictionary['9:00'] += 1
                    time_dictionary['9:30'] += 1
                    time_dictionary['10:00'] += 1
                    time_dictionary['10:30'] += 1
                    time_dictionary['11:00'] += 1
                    time_dictionary['11:30'] += 1
                    time_dictionary['12:00'] += 1
                    time_dictionary['12:30'] += 1
                    time_dictionary['13:00'] += 1
                    time_dictionary['13:30'] += 1
                    time_dictionary['14:00'] += 1
                    time_dictionary['14:30'] += 1
                    time_dictionary['15:00'] += 1
                    time_dictionary['15:30'] += 1
                    time_dictionary['16:00'] += 1
                    time_dictionary['16:30'] += 1
                    time_dictionary['17:00'] += 1
                    time_dictionary['17:30'] += 1
                    time_dictionary['18:00'] += 1
                    time_dictionary['18:30'] += 1
                    time_dictionary['19:00'] += 1

                elif 30 <= logon[1] < 60:
                    time_dictionary['8:00'] += 1
                    time_dictionary['8:30'] += 1
                    time_dictionary['9:00'] += 1
                    time_dictionary['9:30'] += 1
                    time_dictionary['10:00'] += 1
                    time_dictionary['10:30'] += 1
                    time_dictionary['11:00'] += 1
                    time_dictionary['11:30'] += 1
                    time_dictionary['12:00'] += 1
                    time_dictionary['12:30'] += 1
                    time_dictionary['13:00'] += 1
                    time_dictionary['13:30'] += 1
                    time_dictionary['14:00'] += 1
                    time_dictionary['14:30'] += 1
                    time_dictionary['15:00'] += 1
                    time_dictionary['15:30'] += 1
                    time_dictionary['16:00'] += 1
                    time_dictionary['16:30'] += 1
                    time_dictionary['17:00'] += 1
                    time_dictionary['17:30'] += 1
                    time_dictionary['18:00'] += 1
                    time_dictionary['18:30'] += 1
                    time_dictionary['19:00'] += 1
                    time_dictionary['19:30'] += 1

            elif logoff[0] == logon[0] + 13:
                if 30 > logoff[1] >= 0:
                    time_dictionary['8:00'] += 1
                    time_dictionary['8:30'] += 1
                    time_dictionary['9:00'] += 1
                    time_dictionary['9:30'] += 1
                    time_dictionary['10:00'] += 1
                    time_dictionary['10:30'] += 1
                    time_dictionary['11:00'] += 1
                    time_dictionary['11:30'] += 1
                    time_dictionary['12:00'] += 1
                    time_dictionary['12:30'] += 1
                    time_dictionary['13:00'] += 1
                    time_dictionary['13:30'] += 1
                    time_dictionary['14:00'] += 1
                    time_dictionary['14:30'] += 1
                    time_dictionary['15:00'] += 1
                    time_dictionary['15:30'] += 1
                    time_dictionary['16:00'] += 1
                    time_dictionary['16:30'] += 1
                    time_dictionary['17:00'] += 1
                    time_dictionary['17:30'] += 1
                    time_dictionary['18:00'] += 1
                    time_dictionary['18:30'] += 1
                    time_dictionary['19:00'] += 1
                    time_dictionary['19:30'] += 1
                    time_dictionary['20:00'] += 1

                elif 30 <= logon[1] < 60:
                    time_dictionary['8:00'] += 1
                    time_dictionary['8:30'] += 1
                    time_dictionary['9:00'] += 1
                    time_dictionary['9:30'] += 1
                    time_dictionary['10:00'] += 1
                    time_dictionary['10:30'] += 1
                    time_dictionary['11:00'] += 1
                    time_dictionary['11:30'] += 1
                    time_dictionary['12:00'] += 1
                    time_dictionary['12:30'] += 1
                    time_dictionary['13:00'] += 1
                    time_dictionary['13:30'] += 1
                    time_dictionary['14:00'] += 1
                    time_dictionary['14:30'] += 1
                    time_dictionary['15:00'] += 1
                    time_dictionary['15:30'] += 1
                    time_dictionary['16:00'] += 1
                    time_dictionary['16:30'] += 1
                    time_dictionary['17:00'] += 1
                    time_dictionary['17:30'] += 1
                    time_dictionary['18:00'] += 1
                    time_dictionary['18:30'] += 1
                    time_dictionary['19:00'] += 1
                    time_dictionary['19:30'] += 1
                    time_dictionary['20:00'] += 1
                    time_dictionary['20:30'] += 1

            elif logoff[0] == logon[0] + 14:
                if 30 > logoff[1] >= 0:
                    time_dictionary['8:00'] += 1
                    time_dictionary['8:30'] += 1
                    time_dictionary['9:00'] += 1
                    time_dictionary['9:30'] += 1
                    time_dictionary['10:00'] += 1
                    time_dictionary['10:30'] += 1
                    time_dictionary['11:00'] += 1
                    time_dictionary['11:30'] += 1
                    time_dictionary['12:00'] += 1
                    time_dictionary['12:30'] += 1
                    time_dictionary['13:00'] += 1
                    time_dictionary['13:30'] += 1
                    time_dictionary['14:00'] += 1
                    time_dictionary['14:30'] += 1
                    time_dictionary['15:00'] += 1
                    time_dictionary['15:30'] += 1
                    time_dictionary['16:00'] += 1
                    time_dictionary['16:30'] += 1
                    time_dictionary['17:00'] += 1
                    time_dictionary['17:30'] += 1
                    time_dictionary['18:00'] += 1
                    time_dictionary['18:30'] += 1
                    time_dictionary['19:00'] += 1
                    time_dictionary['19:30'] += 1
                    time_dictionary['20:00'] += 1
                    time_dictionary['20:30'] += 1
                    time_dictionary['21:00'] += 1

                elif 30 <= logon[1] < 60:
                    time_dictionary['8:00'] += 1
                    time_dictionary['8:30'] += 1
                    time_dictionary['9:00'] += 1
                    time_dictionary['9:30'] += 1
                    time_dictionary['10:00'] += 1
                    time_dictionary['10:30'] += 1
                    time_dictionary['11:00'] += 1
                    time_dictionary['11:30'] += 1
                    time_dictionary['12:00'] += 1
                    time_dictionary['12:30'] += 1
                    time_dictionary['13:00'] += 1
                    time_dictionary['13:30'] += 1
                    time_dictionary['14:00'] += 1
                    time_dictionary['14:30'] += 1
                    time_dictionary['15:00'] += 1
                    time_dictionary['15:30'] += 1
                    time_dictionary['16:00'] += 1
                    time_dictionary['16:30'] += 1
                    time_dictionary['17:00'] += 1
                    time_dictionary['17:30'] += 1
                    time_dictionary['18:00'] += 1
                    time_dictionary['18:30'] += 1
                    time_dictionary['19:00'] += 1
                    time_dictionary['19:30'] += 1
                    time_dictionary['20:00'] += 1
                    time_dictionary['20:30'] += 1
                    time_dictionary['21:00'] += 1
                    time_dictionary['21:30'] += 1

        elif logon[0] == 8 and 30 > logon[1] >= 0:
            time_dictionary['8:00'] += 1

            if logoff[0] == logon[0]:
                if 30 <= logoff[1] < 60:
                    time_dictionary['8:30'] += 1

            elif logoff[0] == logon[0] + 1:
                if 30 > logoff[1] >= 0:
                    time_dictionary['8:30'] += 1
                    time_dictionary['9:00'] += 1

                elif 30 <= logoff[1] < 60:
                    time_dictionary['8:30'] += 1
                    time_dictionary['9:00'] += 1
                    time_dictionary['9:30'] += 1

            elif logoff[0] == logon[0] + 2:
                if 30 > logoff[1] >= 0:
                    time_dictionary['8:30'] += 1
                    time_dictionary['9:00'] += 1
                    time_dictionary['9:30'] += 1
                    time_dictionary['10:00'] += 1

                elif 30 <= logoff[1] < 60:
                    time_dictionary['8:30'] += 1
                    time_dictionary['9:00'] += 1
                    time_dictionary['9:30'] += 1
                    time_dictionary['10:00'] += 1
                    time_dictionary['10:30'] += 1

            elif logoff[0] == logon[0] + 3:
                if 30 > logoff[1] >= 0:
                    time_dictionary['8:30'] += 1
                    time_dictionary['9:00'] += 1
                    time_dictionary['9:30'] += 1
                    time_dictionary['10:00'] += 1
                    time_dictionary['10:30'] += 1
                    time_dictionary['11:00'] += 1

                elif 30 <= logoff[1] < 60:
                    time_dictionary['8:30'] += 1
                    time_dictionary['9:00'] += 1
                    time_dictionary['9:30'] += 1
                    time_dictionary['10:00'] += 1
                    time_dictionary['10:30'] += 1
                    time_dictionary['11:00'] += 1
                    time_dictionary['11:30'] += 1

            elif logoff[0] == logon[0] + 4:
                if 30 > logoff[1] >= 0:
                    time_dictionary['8:30'] += 1
                    time_dictionary['9:00'] += 1
                    time_dictionary['9:30'] += 1
                    time_dictionary['10:00'] += 1
                    time_dictionary['10:30'] += 1
                    time_dictionary['11:00'] += 1
                    time_dictionary['11:30'] += 1
                    time_dictionary['12:00'] += 1

                elif 30 <= logoff[1] < 60:
                    time_dictionary['8:30'] += 1
                    time_dictionary['9:00'] += 1
                    time_dictionary['9:30'] += 1
                    time_dictionary['10:00'] += 1
                    time_dictionary['10:30'] += 1
                    time_dictionary['11:00'] += 1
                    time_dictionary['11:30'] += 1
                    time_dictionary['12:00'] += 1
                    time_dictionary['12:30'] += 1

            elif logoff[0] == logon[0] + 5:
                if 30 > logoff[1] >= 0:
                    time_dictionary['8:30'] += 1
                    time_dictionary['9:00'] += 1
                    time_dictionary['9:30'] += 1
                    time_dictionary['10:00'] += 1
                    time_dictionary['10:30'] += 1
                    time_dictionary['11:00'] += 1
                    time_dictionary['11:30'] += 1
                    time_dictionary['12:00'] += 1
                    time_dictionary['12:30'] += 1
                    time_dictionary['13:00'] += 1

                elif 30 <= logoff[1] < 60:
                    time_dictionary['8:30'] += 1
                    time_dictionary['9:00'] += 1
                    time_dictionary['9:30'] += 1
                    time_dictionary['10:00'] += 1
                    time_dictionary['10:30'] += 1
                    time_dictionary['11:00'] += 1
                    time_dictionary['11:30'] += 1
                    time_dictionary['12:00'] += 1
                    time_dictionary['12:30'] += 1
                    time_dictionary['13:00'] += 1
                    time_dictionary['13:30'] += 1
            #
            elif logoff[0] == logon[0] + 6:
                if 30 > logoff[1] >= 0:
                    time_dictionary['8:30'] += 1
                    time_dictionary['9:00'] += 1
                    time_dictionary['9:30'] += 1
                    time_dictionary['10:00'] += 1
                    time_dictionary['10:30'] += 1
                    time_dictionary['11:00'] += 1
                    time_dictionary['11:30'] += 1
                    time_dictionary['12:00'] += 1
                    time_dictionary['12:30'] += 1
                    time_dictionary['13:00'] += 1
                    time_dictionary['13:30'] += 1
                    time_dictionary['14:00'] += 1

                elif 30 <= logoff[1] < 60:
                    time_dictionary['8:30'] += 1
                    time_dictionary['9:00'] += 1
                    time_dictionary['9:30'] += 1
                    time_dictionary['10:00'] += 1
                    time_dictionary['10:30'] += 1
                    time_dictionary['11:00'] += 1
                    time_dictionary['11:30'] += 1
                    time_dictionary['12:00'] += 1
                    time_dictionary['12:30'] += 1
                    time_dictionary['13:00'] += 1
                    time_dictionary['13:30'] += 1
                    time_dictionary['14:00'] += 1
                    time_dictionary['14:30'] += 1

            elif logoff[0] == logon[0] + 7:
                if 30 > logoff[1] >= 0:
                    time_dictionary['8:30'] += 1
                    time_dictionary['9:00'] += 1
                    time_dictionary['9:30'] += 1
                    time_dictionary['10:00'] += 1
                    time_dictionary['10:30'] += 1
                    time_dictionary['11:00'] += 1
                    time_dictionary['11:30'] += 1
                    time_dictionary['12:00'] += 1
                    time_dictionary['12:30'] += 1
                    time_dictionary['13:00'] += 1
                    time_dictionary['13:30'] += 1
                    time_dictionary['14:00'] += 1
                    time_dictionary['14:30'] += 1
                    time_dictionary['15:00'] += 1

                elif 30 <= logoff[1] < 60:
                    time_dictionary['8:30'] += 1
                    time_dictionary['9:00'] += 1
                    time_dictionary['9:30'] += 1
                    time_dictionary['10:00'] += 1
                    time_dictionary['10:30'] += 1
                    time_dictionary['11:00'] += 1
                    time_dictionary['11:30'] += 1
                    time_dictionary['12:00'] += 1
                    time_dictionary['12:30'] += 1
                    time_dictionary['13:00'] += 1
                    time_dictionary['13:30'] += 1
                    time_dictionary['14:00'] += 1
                    time_dictionary['14:30'] += 1
                    time_dictionary['15:00'] += 1
                    time_dictionary['15:30'] += 1

            elif logoff[0] == logon[0] + 8:
                if 30 > logoff[1] >= 0:
                    time_dictionary['8:30'] += 1
                    time_dictionary['9:00'] += 1
                    time_dictionary['9:30'] += 1
                    time_dictionary['10:00'] += 1
                    time_dictionary['10:30'] += 1
                    time_dictionary['11:00'] += 1
                    time_dictionary['11:30'] += 1
                    time_dictionary['12:00'] += 1
                    time_dictionary['12:30'] += 1
                    time_dictionary['13:00'] += 1
                    time_dictionary['13:30'] += 1
                    time_dictionary['14:00'] += 1
                    time_dictionary['14:30'] += 1
                    time_dictionary['15:00'] += 1
                    time_dictionary['15:30'] += 1
                    time_dictionary['16:00'] += 1

                elif 30 <= logoff[1] < 60:
                    time_dictionary['8:30'] += 1
                    time_dictionary['9:00'] += 1
                    time_dictionary['9:30'] += 1
                    time_dictionary['10:00'] += 1
                    time_dictionary['10:30'] += 1
                    time_dictionary['11:00'] += 1
                    time_dictionary['11:30'] += 1
                    time_dictionary['12:00'] += 1
                    time_dictionary['12:30'] += 1
                    time_dictionary['13:00'] += 1
                    time_dictionary['13:30'] += 1
                    time_dictionary['14:00'] += 1
                    time_dictionary['14:30'] += 1
                    time_dictionary['15:00'] += 1
                    time_dictionary['15:30'] += 1
                    time_dictionary['16:00'] += 1
                    time_dictionary['16:30'] += 1

            elif logoff[0] == logon[0] + 9:
                if 30 > logoff[1] >= 0:
                    time_dictionary['8:30'] += 1
                    time_dictionary['9:00'] += 1
                    time_dictionary['9:30'] += 1
                    time_dictionary['10:00'] += 1
                    time_dictionary['10:30'] += 1
                    time_dictionary['11:00'] += 1
                    time_dictionary['11:30'] += 1
                    time_dictionary['12:00'] += 1
                    time_dictionary['12:30'] += 1
                    time_dictionary['13:00'] += 1
                    time_dictionary['13:30'] += 1
                    time_dictionary['14:00'] += 1
                    time_dictionary['14:30'] += 1
                    time_dictionary['15:00'] += 1
                    time_dictionary['15:30'] += 1
                    time_dictionary['16:00'] += 1
                    time_dictionary['16:30'] += 1
                    time_dictionary['17:00'] += 1

                elif 30 <= logoff[1] < 60:
                    time_dictionary['8:30'] += 1
                    time_dictionary['9:00'] += 1
                    time_dictionary['9:30'] += 1
                    time_dictionary['10:00'] += 1
                    time_dictionary['10:30'] += 1
                    time_dictionary['11:00'] += 1
                    time_dictionary['11:30'] += 1
                    time_dictionary['12:00'] += 1
                    time_dictionary['12:30'] += 1
                    time_dictionary['13:00'] += 1
                    time_dictionary['13:30'] += 1
                    time_dictionary['14:00'] += 1
                    time_dictionary['14:30'] += 1
                    time_dictionary['15:00'] += 1
                    time_dictionary['15:30'] += 1
                    time_dictionary['16:00'] += 1
                    time_dictionary['16:30'] += 1
                    time_dictionary['17:00'] += 1
                    time_dictionary['17:30'] += 1

            elif logoff[0] == logon[0] + 10:
                if 30 > logoff[1] >= 0:
                    time_dictionary['8:30'] += 1
                    time_dictionary['9:00'] += 1
                    time_dictionary['9:30'] += 1
                    time_dictionary['10:00'] += 1
                    time_dictionary['10:30'] += 1
                    time_dictionary['11:00'] += 1
                    time_dictionary['11:30'] += 1
                    time_dictionary['12:00'] += 1
                    time_dictionary['12:30'] += 1
                    time_dictionary['13:00'] += 1
                    time_dictionary['13:30'] += 1
                    time_dictionary['14:00'] += 1
                    time_dictionary['14:30'] += 1
                    time_dictionary['15:00'] += 1
                    time_dictionary['15:30'] += 1
                    time_dictionary['16:00'] += 1
                    time_dictionary['16:30'] += 1
                    time_dictionary['17:00'] += 1
                    time_dictionary['17:30'] += 1
                    time_dictionary['18:00'] += 1

                elif 30 <= logoff[1] < 60:
                    time_dictionary['8:30'] += 1
                    time_dictionary['9:00'] += 1
                    time_dictionary['9:30'] += 1
                    time_dictionary['10:00'] += 1
                    time_dictionary['10:30'] += 1
                    time_dictionary['11:00'] += 1
                    time_dictionary['11:30'] += 1
                    time_dictionary['12:00'] += 1
                    time_dictionary['12:30'] += 1
                    time_dictionary['13:00'] += 1
                    time_dictionary['13:30'] += 1
                    time_dictionary['14:00'] += 1
                    time_dictionary['14:30'] += 1
                    time_dictionary['15:00'] += 1
                    time_dictionary['15:30'] += 1
                    time_dictionary['16:00'] += 1
                    time_dictionary['16:30'] += 1
                    time_dictionary['17:00'] += 1
                    time_dictionary['17:30'] += 1
                    time_dictionary['18:00'] += 1
                    time_dictionary['18:30'] += 1

            elif logoff[0] == logon[0] + 11:
                if 30 > logoff[1] >= 0:
                    time_dictionary['8:30'] += 1
                    time_dictionary['9:00'] += 1
                    time_dictionary['9:30'] += 1
                    time_dictionary['10:00'] += 1
                    time_dictionary['10:30'] += 1
                    time_dictionary['11:00'] += 1
                    time_dictionary['11:30'] += 1
                    time_dictionary['12:00'] += 1
                    time_dictionary['12:30'] += 1
                    time_dictionary['13:00'] += 1
                    time_dictionary['13:30'] += 1
                    time_dictionary['14:00'] += 1
                    time_dictionary['14:30'] += 1
                    time_dictionary['15:00'] += 1
                    time_dictionary['15:30'] += 1
                    time_dictionary['16:00'] += 1
                    time_dictionary['16:30'] += 1
                    time_dictionary['17:00'] += 1
                    time_dictionary['17:30'] += 1
                    time_dictionary['18:00'] += 1
                    time_dictionary['18:30'] += 1
                    time_dictionary['19:00'] += 1

                elif 30 <= logoff[1] < 60:
                    time_dictionary['8:30'] += 1
                    time_dictionary['9:00'] += 1
                    time_dictionary['9:30'] += 1
                    time_dictionary['10:00'] += 1
                    time_dictionary['10:30'] += 1
                    time_dictionary['11:00'] += 1
                    time_dictionary['11:30'] += 1
                    time_dictionary['12:00'] += 1
                    time_dictionary['12:30'] += 1
                    time_dictionary['13:00'] += 1
                    time_dictionary['13:30'] += 1
                    time_dictionary['14:00'] += 1
                    time_dictionary['14:30'] += 1
                    time_dictionary['15:00'] += 1
                    time_dictionary['15:30'] += 1
                    time_dictionary['16:00'] += 1
                    time_dictionary['16:30'] += 1
                    time_dictionary['17:00'] += 1
                    time_dictionary['17:30'] += 1
                    time_dictionary['18:00'] += 1
                    time_dictionary['18:30'] += 1
                    time_dictionary['19:00'] += 1
                    time_dictionary['19:30'] += 1

            elif logoff[0] == logon[0] + 12:
                if 30 > logoff[1] >= 0:
                    time_dictionary['8:30'] += 1
                    time_dictionary['9:00'] += 1
                    time_dictionary['9:30'] += 1
                    time_dictionary['10:00'] += 1
                    time_dictionary['10:30'] += 1
                    time_dictionary['11:00'] += 1
                    time_dictionary['11:30'] += 1
                    time_dictionary['12:00'] += 1
                    time_dictionary['12:30'] += 1
                    time_dictionary['13:00'] += 1
                    time_dictionary['13:30'] += 1
                    time_dictionary['14:00'] += 1
                    time_dictionary['14:30'] += 1
                    time_dictionary['15:00'] += 1
                    time_dictionary['15:30'] += 1
                    time_dictionary['16:00'] += 1
                    time_dictionary['16:30'] += 1
                    time_dictionary['17:00'] += 1
                    time_dictionary['17:30'] += 1
                    time_dictionary['18:00'] += 1
                    time_dictionary['18:30'] += 1
                    time_dictionary['19:00'] += 1
                    time_dictionary['19:30'] += 1
                    time_dictionary['20:00'] += 1

                elif 30 <= logoff[1] < 60:
                    time_dictionary['8:30'] += 1
                    time_dictionary['9:00'] += 1
                    time_dictionary['9:30'] += 1
                    time_dictionary['10:00'] += 1
                    time_dictionary['10:30'] += 1
                    time_dictionary['11:00'] += 1
                    time_dictionary['11:30'] += 1
                    time_dictionary['12:00'] += 1
                    time_dictionary['12:30'] += 1
                    time_dictionary['13:00'] += 1
                    time_dictionary['13:30'] += 1
                    time_dictionary['14:00'] += 1
                    time_dictionary['14:30'] += 1
                    time_dictionary['15:00'] += 1
                    time_dictionary['15:30'] += 1
                    time_dictionary['16:00'] += 1
                    time_dictionary['16:30'] += 1
                    time_dictionary['17:00'] += 1
                    time_dictionary['17:30'] += 1
                    time_dictionary['18:00'] += 1
                    time_dictionary['18:30'] += 1
                    time_dictionary['19:00'] += 1
                    time_dictionary['19:30'] += 1
                    time_dictionary['20:00'] += 1
                    time_dictionary['20:30'] += 1

            elif logoff[0] == logon[0] + 13:
                if 30 > logoff[1] >= 0:
                    time_dictionary['8:30'] += 1
                    time_dictionary['9:00'] += 1
                    time_dictionary['9:30'] += 1
                    time_dictionary['10:00'] += 1
                    time_dictionary['10:30'] += 1
                    time_dictionary['11:00'] += 1
                    time_dictionary['11:30'] += 1
                    time_dictionary['12:00'] += 1
                    time_dictionary['12:30'] += 1
                    time_dictionary['13:00'] += 1
                    time_dictionary['13:30'] += 1
                    time_dictionary['14:00'] += 1
                    time_dictionary['14:30'] += 1
                    time_dictionary['15:00'] += 1
                    time_dictionary['15:30'] += 1
                    time_dictionary['16:00'] += 1
                    time_dictionary['16:30'] += 1
                    time_dictionary['17:00'] += 1
                    time_dictionary['17:30'] += 1
                    time_dictionary['18:00'] += 1
                    time_dictionary['18:30'] += 1
                    time_dictionary['19:00'] += 1
                    time_dictionary['19:30'] += 1
                    time_dictionary['20:00'] += 1
                    time_dictionary['20:30'] += 1
                    time_dictionary['21:00'] += 1

                elif 30 <= logoff[1] < 60:
                    time_dictionary['8:30'] += 1
                    time_dictionary['9:00'] += 1
                    time_dictionary['9:30'] += 1
                    time_dictionary['10:00'] += 1
                    time_dictionary['10:30'] += 1
                    time_dictionary['11:00'] += 1
                    time_dictionary['11:30'] += 1
                    time_dictionary['12:00'] += 1
                    time_dictionary['12:30'] += 1
                    time_dictionary['13:00'] += 1
                    time_dictionary['13:30'] += 1
                    time_dictionary['14:00'] += 1
                    time_dictionary['14:30'] += 1
                    time_dictionary['15:00'] += 1
                    time_dictionary['15:30'] += 1
                    time_dictionary['16:00'] += 1
                    time_dictionary['16:30'] += 1
                    time_dictionary['17:00'] += 1
                    time_dictionary['17:30'] += 1
                    time_dictionary['18:00'] += 1
                    time_dictionary['18:30'] += 1
                    time_dictionary['19:00'] += 1
                    time_dictionary['19:30'] += 1
                    time_dictionary['20:00'] += 1
                    time_dictionary['20:30'] += 1
                    time_dictionary['21:00'] += 1
                    time_dictionary['21:30'] += 1

        elif logon[0] == 8 and 30 <= logon[1] < 60:
            time_dictionary['8:30'] += 1

            if logoff[0] == logon[0] + 1:
                if 30 > logoff[1] >= 0:
                    time_dictionary['9:00'] += 1

                elif 30 <= logon[1] < 60:
                    time_dictionary['9:00'] += 1
                    time_dictionary['9:30'] += 1

            if logoff[0] == logon[0] + 2:
                if 30 > logoff[1] >= 0:
                    time_dictionary['9:00'] += 1
                    time_dictionary['9:30'] += 1
                    time_dictionary['10:00'] += 1

                elif 30 <= logon[1] < 60:
                    time_dictionary['9:00'] += 1
                    time_dictionary['9:30'] += 1
                    time_dictionary['10:00'] += 1
                    time_dictionary['10:30'] += 1

            if logoff[0] == logon[0] + 3:
                if 30 > logoff[1] >= 0:
                    time_dictionary['9:00'] += 1
                    time_dictionary['9:30'] += 1
                    time_dictionary['10:00'] += 1
                    time_dictionary['10:30'] += 1
                    time_dictionary['11:00'] += 1

                elif 30 <= logon[1] < 60:
                    time_dictionary['9:00'] += 1
                    time_dictionary['9:30'] += 1
                    time_dictionary['10:00'] += 1
                    time_dictionary['10:30'] += 1
                    time_dictionary['11:00'] += 1
                    time_dictionary['11:30'] += 1

            if logoff[0] == logon[0] + 4:
                if 30 > logoff[1] >= 0:
                    time_dictionary['9:00'] += 1
                    time_dictionary['9:30'] += 1
                    time_dictionary['10:00'] += 1
                    time_dictionary['10:30'] += 1
                    time_dictionary['11:00'] += 1
                    time_dictionary['11:30'] += 1
                    time_dictionary['12:00'] += 1

                elif 30 <= logon[1] < 60:
                    time_dictionary['9:00'] += 1
                    time_dictionary['9:30'] += 1
                    time_dictionary['10:00'] += 1
                    time_dictionary['10:30'] += 1
                    time_dictionary['11:00'] += 1
                    time_dictionary['11:30'] += 1
                    time_dictionary['12:00'] += 1
                    time_dictionary['12:30'] += 1

            if logoff[0] == logon[0] + 5:
                if 30 > logoff[1] >= 0:
                    time_dictionary['9:00'] += 1
                    time_dictionary['9:30'] += 1
                    time_dictionary['10:00'] += 1
                    time_dictionary['10:30'] += 1
                    time_dictionary['11:00'] += 1
                    time_dictionary['11:30'] += 1
                    time_dictionary['12:00'] += 1
                    time_dictionary['12:30'] += 1
                    time_dictionary['13:00'] += 1

                elif 30 <= logon[1] < 60:
                    time_dictionary['9:00'] += 1
                    time_dictionary['9:30'] += 1
                    time_dictionary['10:00'] += 1
                    time_dictionary['10:30'] += 1
                    time_dictionary['11:00'] += 1
                    time_dictionary['11:30'] += 1
                    time_dictionary['12:00'] += 1
                    time_dictionary['12:30'] += 1
                    time_dictionary['13:00'] += 1
                    time_dictionary['13:30'] += 1

            if logoff[0] == logon[0] + 6:
                if 30 > logoff[1] >= 0:
                    time_dictionary['9:00'] += 1
                    time_dictionary['9:30'] += 1
                    time_dictionary['10:00'] += 1
                    time_dictionary['10:30'] += 1
                    time_dictionary['11:00'] += 1
                    time_dictionary['11:30'] += 1
                    time_dictionary['12:00'] += 1
                    time_dictionary['12:30'] += 1
                    time_dictionary['13:00'] += 1
                    time_dictionary['13:30'] += 1
                    time_dictionary['14:00'] += 1

                elif 30 <= logon[1] < 60:
                    time_dictionary['9:00'] += 1
                    time_dictionary['9:30'] += 1
                    time_dictionary['10:00'] += 1
                    time_dictionary['10:30'] += 1
                    time_dictionary['11:00'] += 1
                    time_dictionary['11:30'] += 1
                    time_dictionary['12:00'] += 1
                    time_dictionary['12:30'] += 1
                    time_dictionary['13:00'] += 1
                    time_dictionary['13:30'] += 1
                    time_dictionary['14:00'] += 1
                    time_dictionary['14:30'] += 1

            if logoff[0] == logon[0] + 7:
                if 30 > logoff[1] >= 0:
                    time_dictionary['9:00'] += 1
                    time_dictionary['9:30'] += 1
                    time_dictionary['10:00'] += 1
                    time_dictionary['10:30'] += 1
                    time_dictionary['11:00'] += 1
                    time_dictionary['11:30'] += 1
                    time_dictionary['12:00'] += 1
                    time_dictionary['12:30'] += 1
                    time_dictionary['13:00'] += 1
                    time_dictionary['13:30'] += 1
                    time_dictionary['14:00'] += 1
                    time_dictionary['14:30'] += 1
                    time_dictionary['15:00'] += 1

                elif 30 <= logon[1] < 60:
                    time_dictionary['9:00'] += 1
                    time_dictionary['9:30'] += 1
                    time_dictionary['10:00'] += 1
                    time_dictionary['10:30'] += 1
                    time_dictionary['11:00'] += 1
                    time_dictionary['11:30'] += 1
                    time_dictionary['12:00'] += 1
                    time_dictionary['12:30'] += 1
                    time_dictionary['13:00'] += 1
                    time_dictionary['13:30'] += 1
                    time_dictionary['14:00'] += 1
                    time_dictionary['14:30'] += 1
                    time_dictionary['15:00'] += 1
                    time_dictionary['15:30'] += 1

            if logoff[0] == logon[0] + 8:
                if 30 > logoff[1] >= 0:
                    time_dictionary['9:00'] += 1
                    time_dictionary['9:30'] += 1
                    time_dictionary['10:00'] += 1
                    time_dictionary['10:30'] += 1
                    time_dictionary['11:00'] += 1
                    time_dictionary['11:30'] += 1
                    time_dictionary['12:00'] += 1
                    time_dictionary['12:30'] += 1
                    time_dictionary['13:00'] += 1
                    time_dictionary['13:30'] += 1
                    time_dictionary['14:00'] += 1
                    time_dictionary['14:30'] += 1
                    time_dictionary['15:00'] += 1
                    time_dictionary['15:30'] += 1
                    time_dictionary['16:00'] += 1

                elif 30 <= logon[1] < 60:
                    time_dictionary['9:00'] += 1
                    time_dictionary['9:30'] += 1
                    time_dictionary['10:00'] += 1
                    time_dictionary['10:30'] += 1
                    time_dictionary['11:00'] += 1
                    time_dictionary['11:30'] += 1
                    time_dictionary['12:00'] += 1
                    time_dictionary['12:30'] += 1
                    time_dictionary['13:00'] += 1
                    time_dictionary['13:30'] += 1
                    time_dictionary['14:00'] += 1
                    time_dictionary['14:30'] += 1
                    time_dictionary['15:00'] += 1
                    time_dictionary['15:30'] += 1
                    time_dictionary['16:00'] += 1
                    time_dictionary['16:30'] += 1

            if logoff[0] == logon[0] + 9:
                if 30 > logoff[1] >= 0:
                    time_dictionary['9:00'] += 1
                    time_dictionary['9:30'] += 1
                    time_dictionary['10:00'] += 1
                    time_dictionary['10:30'] += 1
                    time_dictionary['11:00'] += 1
                    time_dictionary['11:30'] += 1
                    time_dictionary['12:00'] += 1
                    time_dictionary['12:30'] += 1
                    time_dictionary['13:00'] += 1
                    time_dictionary['13:30'] += 1
                    time_dictionary['14:00'] += 1
                    time_dictionary['14:30'] += 1
                    time_dictionary['15:00'] += 1
                    time_dictionary['15:30'] += 1
                    time_dictionary['16:00'] += 1
                    time_dictionary['16:30'] += 1
                    time_dictionary['17:00'] += 1

                elif 30 <= logon[1] < 60:
                    time_dictionary['9:00'] += 1
                    time_dictionary['9:30'] += 1
                    time_dictionary['10:00'] += 1
                    time_dictionary['10:30'] += 1
                    time_dictionary['11:00'] += 1
                    time_dictionary['11:30'] += 1
                    time_dictionary['12:00'] += 1
                    time_dictionary['12:30'] += 1
                    time_dictionary['13:00'] += 1
                    time_dictionary['13:30'] += 1
                    time_dictionary['14:00'] += 1
                    time_dictionary['14:30'] += 1
                    time_dictionary['15:00'] += 1
                    time_dictionary['15:30'] += 1
                    time_dictionary['16:00'] += 1
                    time_dictionary['16:30'] += 1
                    time_dictionary['17:00'] += 1
                    time_dictionary['17:30'] += 1

            if logoff[0] == logon[0] + 10:
                if 30 > logoff[1] >= 0:
                    time_dictionary['9:00'] += 1
                    time_dictionary['9:30'] += 1
                    time_dictionary['10:00'] += 1
                    time_dictionary['10:30'] += 1
                    time_dictionary['11:00'] += 1
                    time_dictionary['11:30'] += 1
                    time_dictionary['12:00'] += 1
                    time_dictionary['12:30'] += 1
                    time_dictionary['13:00'] += 1
                    time_dictionary['13:30'] += 1
                    time_dictionary['14:00'] += 1
                    time_dictionary['14:30'] += 1
                    time_dictionary['15:00'] += 1
                    time_dictionary['15:30'] += 1
                    time_dictionary['16:00'] += 1
                    time_dictionary['16:30'] += 1
                    time_dictionary['17:00'] += 1
                    time_dictionary['17:30'] += 1
                    time_dictionary['18:00'] += 1

                elif 30 <= logon[1] < 60:
                    time_dictionary['9:00'] += 1
                    time_dictionary['9:30'] += 1
                    time_dictionary['10:00'] += 1
                    time_dictionary['10:30'] += 1
                    time_dictionary['11:00'] += 1
                    time_dictionary['11:30'] += 1
                    time_dictionary['12:00'] += 1
                    time_dictionary['12:30'] += 1
                    time_dictionary['13:00'] += 1
                    time_dictionary['13:30'] += 1
                    time_dictionary['14:00'] += 1
                    time_dictionary['14:30'] += 1
                    time_dictionary['15:00'] += 1
                    time_dictionary['15:30'] += 1
                    time_dictionary['16:00'] += 1
                    time_dictionary['16:30'] += 1
                    time_dictionary['17:00'] += 1
                    time_dictionary['17:30'] += 1
                    time_dictionary['18:00'] += 1
                    time_dictionary['18:30'] += 1

            if logoff[0] == logon[0] + 11:
                if 30 > logoff[1] >= 0:
                    time_dictionary['9:00'] += 1
                    time_dictionary['9:30'] += 1
                    time_dictionary['10:00'] += 1
                    time_dictionary['10:30'] += 1
                    time_dictionary['11:00'] += 1
                    time_dictionary['11:30'] += 1
                    time_dictionary['12:00'] += 1
                    time_dictionary['12:30'] += 1
                    time_dictionary['13:00'] += 1
                    time_dictionary['13:30'] += 1
                    time_dictionary['14:00'] += 1
                    time_dictionary['14:30'] += 1
                    time_dictionary['15:00'] += 1
                    time_dictionary['15:30'] += 1
                    time_dictionary['16:00'] += 1
                    time_dictionary['16:30'] += 1
                    time_dictionary['17:00'] += 1
                    time_dictionary['17:30'] += 1
                    time_dictionary['18:00'] += 1
                    time_dictionary['18:30'] += 1
                    time_dictionary['19:00'] += 1

                elif 30 <= logon[1] < 60:
                    time_dictionary['9:00'] += 1
                    time_dictionary['9:30'] += 1
                    time_dictionary['10:00'] += 1
                    time_dictionary['10:30'] += 1
                    time_dictionary['11:00'] += 1
                    time_dictionary['11:30'] += 1
                    time_dictionary['12:00'] += 1
                    time_dictionary['12:30'] += 1
                    time_dictionary['13:00'] += 1
                    time_dictionary['13:30'] += 1
                    time_dictionary['14:00'] += 1
                    time_dictionary['14:30'] += 1
                    time_dictionary['15:00'] += 1
                    time_dictionary['15:30'] += 1
                    time_dictionary['16:00'] += 1
                    time_dictionary['16:30'] += 1
                    time_dictionary['17:00'] += 1
                    time_dictionary['17:30'] += 1
                    time_dictionary['18:00'] += 1
                    time_dictionary['18:30'] += 1
                    time_dictionary['19:00'] += 1
                    time_dictionary['19:30'] += 1

            if logoff[0] == logon[0] + 12:
                if 30 > logoff[1] >= 0:
                    time_dictionary['9:00'] += 1
                    time_dictionary['9:30'] += 1
                    time_dictionary['10:00'] += 1
                    time_dictionary['10:30'] += 1
                    time_dictionary['11:00'] += 1
                    time_dictionary['11:30'] += 1
                    time_dictionary['12:00'] += 1
                    time_dictionary['12:30'] += 1
                    time_dictionary['13:00'] += 1
                    time_dictionary['13:30'] += 1
                    time_dictionary['14:00'] += 1
                    time_dictionary['14:30'] += 1
                    time_dictionary['15:00'] += 1
                    time_dictionary['15:30'] += 1
                    time_dictionary['16:00'] += 1
                    time_dictionary['16:30'] += 1
                    time_dictionary['17:00'] += 1
                    time_dictionary['17:30'] += 1
                    time_dictionary['18:00'] += 1
                    time_dictionary['18:30'] += 1
                    time_dictionary['19:00'] += 1
                    time_dictionary['19:30'] += 1
                    time_dictionary['20:00'] += 1

                elif 30 <= logon[1] < 60:
                    time_dictionary['9:00'] += 1
                    time_dictionary['9:30'] += 1
                    time_dictionary['10:00'] += 1
                    time_dictionary['10:30'] += 1
                    time_dictionary['11:00'] += 1
                    time_dictionary['11:30'] += 1
                    time_dictionary['12:00'] += 1
                    time_dictionary['12:30'] += 1
                    time_dictionary['13:00'] += 1
                    time_dictionary['13:30'] += 1
                    time_dictionary['14:00'] += 1
                    time_dictionary['14:30'] += 1
                    time_dictionary['15:00'] += 1
                    time_dictionary['15:30'] += 1
                    time_dictionary['16:00'] += 1
                    time_dictionary['16:30'] += 1
                    time_dictionary['17:00'] += 1
                    time_dictionary['17:30'] += 1
                    time_dictionary['18:00'] += 1
                    time_dictionary['18:30'] += 1
                    time_dictionary['19:00'] += 1
                    time_dictionary['19:30'] += 1
                    time_dictionary['20:00'] += 1
                    time_dictionary['20:30'] += 1

            if logoff[0] == logon[0] + 13:
                if 30 > logoff[1] >= 0:
                    time_dictionary['9:00'] += 1
                    time_dictionary['9:30'] += 1
                    time_dictionary['10:00'] += 1
                    time_dictionary['10:30'] += 1
                    time_dictionary['11:00'] += 1
                    time_dictionary['11:30'] += 1
                    time_dictionary['12:00'] += 1
                    time_dictionary['12:30'] += 1
                    time_dictionary['13:00'] += 1
                    time_dictionary['13:30'] += 1
                    time_dictionary['14:00'] += 1
                    time_dictionary['14:30'] += 1
                    time_dictionary['15:00'] += 1
                    time_dictionary['15:30'] += 1
                    time_dictionary['16:00'] += 1
                    time_dictionary['16:30'] += 1
                    time_dictionary['17:00'] += 1
                    time_dictionary['17:30'] += 1
                    time_dictionary['18:00'] += 1
                    time_dictionary['18:30'] += 1
                    time_dictionary['19:00'] += 1
                    time_dictionary['19:30'] += 1
                    time_dictionary['20:00'] += 1
                    time_dictionary['20:30'] += 1
                    time_dictionary['21:00'] += 1

                elif 30 <= logon[1] < 60:
                    time_dictionary['9:00'] += 1
                    time_dictionary['9:30'] += 1
                    time_dictionary['10:00'] += 1
                    time_dictionary['10:30'] += 1
                    time_dictionary['11:00'] += 1
                    time_dictionary['11:30'] += 1
                    time_dictionary['12:00'] += 1
                    time_dictionary['12:30'] += 1
                    time_dictionary['13:00'] += 1
                    time_dictionary['13:30'] += 1
                    time_dictionary['14:00'] += 1
                    time_dictionary['14:30'] += 1
                    time_dictionary['15:00'] += 1
                    time_dictionary['15:30'] += 1
                    time_dictionary['16:00'] += 1
                    time_dictionary['16:30'] += 1
                    time_dictionary['17:00'] += 1
                    time_dictionary['17:30'] += 1
                    time_dictionary['18:00'] += 1
                    time_dictionary['18:30'] += 1
                    time_dictionary['19:00'] += 1
                    time_dictionary['19:30'] += 1
                    time_dictionary['20:00'] += 1
                    time_dictionary['20:30'] += 1
                    time_dictionary['21:00'] += 1
                    time_dictionary['21:30'] += 1

        elif logon[0] == 9 and 30 > logon[1] >= 0:
            time_dictionary['9:00'] += 1

            if logoff[0] == logon[0]:
                if 30 <= logoff[1] < 60:
                    time_dictionary['9:30'] += 1

            elif logoff[0] == logon[0] + 1:
                if 30 > logoff[1] >= 0:
                    time_dictionary['9:30'] += 1
                    time_dictionary['10:00'] += 1

                elif 30 <= logoff[1] < 60:
                    time_dictionary['9:30'] += 1
                    time_dictionary['10:00'] += 1
                    time_dictionary['10:30'] += 1

            elif logoff[0] == logon[0] + 2:
                if 30 > logoff[1] >= 0:
                    time_dictionary['9:30'] += 1
                    time_dictionary['10:00'] += 1
                    time_dictionary['10:30'] += 1
                    time_dictionary['11:00'] += 1

                elif 30 <= logoff[1] < 60:
                    time_dictionary['9:30'] += 1
                    time_dictionary['10:00'] += 1
                    time_dictionary['10:30'] += 1
                    time_dictionary['11:00'] += 1
                    time_dictionary['11:30'] += 1

            elif logoff[0] == logon[0] + 3:
                if 30 > logoff[1] >= 0:
                    time_dictionary['9:30'] += 1
                    time_dictionary['10:00'] += 1
                    time_dictionary['10:30'] += 1
                    time_dictionary['11:00'] += 1
                    time_dictionary['11:30'] += 1
                    time_dictionary['12:00'] += 1

                elif 30 <= logoff[1] < 60:
                    time_dictionary['9:30'] += 1
                    time_dictionary['10:00'] += 1
                    time_dictionary['10:30'] += 1
                    time_dictionary['11:00'] += 1
                    time_dictionary['11:30'] += 1
                    time_dictionary['12:00'] += 1
                    time_dictionary['12:30'] += 1

            elif logoff[0] == logon[0] + 4:
                if 30 > logoff[1] >= 0:
                    time_dictionary['9:30'] += 1
                    time_dictionary['10:00'] += 1
                    time_dictionary['10:30'] += 1
                    time_dictionary['11:00'] += 1
                    time_dictionary['11:30'] += 1
                    time_dictionary['12:00'] += 1
                    time_dictionary['12:30'] += 1
                    time_dictionary['13:00'] += 1

                elif 30 <= logoff[1] < 60:
                    time_dictionary['9:30'] += 1
                    time_dictionary['10:00'] += 1
                    time_dictionary['10:30'] += 1
                    time_dictionary['11:00'] += 1
                    time_dictionary['11:30'] += 1
                    time_dictionary['12:00'] += 1
                    time_dictionary['12:30'] += 1
                    time_dictionary['13:00'] += 1
                    time_dictionary['13:30'] += 1

            elif logoff[0] == logon[0] + 5:
                if 30 > logoff[1] >= 0:
                    time_dictionary['9:30'] += 1
                    time_dictionary['10:00'] += 1
                    time_dictionary['10:30'] += 1
                    time_dictionary['11:00'] += 1
                    time_dictionary['11:30'] += 1
                    time_dictionary['12:00'] += 1
                    time_dictionary['12:30'] += 1
                    time_dictionary['13:00'] += 1
                    time_dictionary['13:30'] += 1
                    time_dictionary['14:00'] += 1

                elif 30 <= logoff[1] < 60:
                    time_dictionary['9:30'] += 1
                    time_dictionary['10:00'] += 1
                    time_dictionary['10:30'] += 1
                    time_dictionary['11:00'] += 1
                    time_dictionary['11:30'] += 1
                    time_dictionary['12:00'] += 1
                    time_dictionary['12:30'] += 1
                    time_dictionary['13:00'] += 1
                    time_dictionary['13:30'] += 1
                    time_dictionary['14:00'] += 1
                    time_dictionary['14:30'] += 1

            elif logoff[0] == logon[0] + 6:
                if 30 > logoff[1] >= 0:
                    time_dictionary['9:30'] += 1
                    time_dictionary['10:00'] += 1
                    time_dictionary['10:30'] += 1
                    time_dictionary['11:00'] += 1
                    time_dictionary['11:30'] += 1
                    time_dictionary['12:00'] += 1
                    time_dictionary['12:30'] += 1
                    time_dictionary['13:00'] += 1
                    time_dictionary['13:30'] += 1
                    time_dictionary['14:00'] += 1
                    time_dictionary['14:30'] += 1
                    time_dictionary['15:00'] += 1

                elif 30 <= logoff[1] < 60:
                    time_dictionary['9:30'] += 1
                    time_dictionary['10:00'] += 1
                    time_dictionary['10:30'] += 1
                    time_dictionary['11:00'] += 1
                    time_dictionary['11:30'] += 1
                    time_dictionary['12:00'] += 1
                    time_dictionary['12:30'] += 1
                    time_dictionary['13:00'] += 1
                    time_dictionary['13:30'] += 1
                    time_dictionary['14:00'] += 1
                    time_dictionary['14:30'] += 1
                    time_dictionary['15:00'] += 1
                    time_dictionary['15:30'] += 1

            elif logoff[0] == logon[0] + 7:
                if 30 > logoff[1] >= 0:
                    time_dictionary['9:30'] += 1
                    time_dictionary['10:00'] += 1
                    time_dictionary['10:30'] += 1
                    time_dictionary['11:00'] += 1
                    time_dictionary['11:30'] += 1
                    time_dictionary['12:00'] += 1
                    time_dictionary['12:30'] += 1
                    time_dictionary['13:00'] += 1
                    time_dictionary['13:30'] += 1
                    time_dictionary['14:00'] += 1
                    time_dictionary['14:30'] += 1
                    time_dictionary['15:00'] += 1
                    time_dictionary['15:30'] += 1
                    time_dictionary['16:00'] += 1

                elif 30 <= logoff[1] < 60:
                    time_dictionary['9:30'] += 1
                    time_dictionary['10:00'] += 1
                    time_dictionary['10:30'] += 1
                    time_dictionary['11:00'] += 1
                    time_dictionary['11:30'] += 1
                    time_dictionary['12:00'] += 1
                    time_dictionary['12:30'] += 1
                    time_dictionary['13:00'] += 1
                    time_dictionary['13:30'] += 1
                    time_dictionary['14:00'] += 1
                    time_dictionary['14:30'] += 1
                    time_dictionary['15:00'] += 1
                    time_dictionary['15:30'] += 1
                    time_dictionary['16:00'] += 1
                    time_dictionary['16:30'] += 1

            elif logoff[0] == logon[0] + 8:
                if 30 > logoff[1] >= 0:
                    time_dictionary['9:30'] += 1
                    time_dictionary['10:00'] += 1
                    time_dictionary['10:30'] += 1
                    time_dictionary['11:00'] += 1
                    time_dictionary['11:30'] += 1
                    time_dictionary['12:00'] += 1
                    time_dictionary['12:30'] += 1
                    time_dictionary['13:00'] += 1
                    time_dictionary['13:30'] += 1
                    time_dictionary['14:00'] += 1
                    time_dictionary['14:30'] += 1
                    time_dictionary['15:00'] += 1
                    time_dictionary['15:30'] += 1
                    time_dictionary['16:00'] += 1
                    time_dictionary['16:30'] += 1
                    time_dictionary['17:00'] += 1

                elif 30 <= logoff[1] < 60:
                    time_dictionary['9:30'] += 1
                    time_dictionary['10:00'] += 1
                    time_dictionary['10:30'] += 1
                    time_dictionary['11:00'] += 1
                    time_dictionary['11:30'] += 1
                    time_dictionary['12:00'] += 1
                    time_dictionary['12:30'] += 1
                    time_dictionary['13:00'] += 1
                    time_dictionary['13:30'] += 1
                    time_dictionary['14:00'] += 1
                    time_dictionary['14:30'] += 1
                    time_dictionary['15:00'] += 1
                    time_dictionary['15:30'] += 1
                    time_dictionary['16:00'] += 1
                    time_dictionary['16:30'] += 1
                    time_dictionary['17:00'] += 1
                    time_dictionary['17:30'] += 1

            elif logoff[0] == logon[0] + 9:
                if 30 > logoff[1] >= 0:
                    time_dictionary['9:30'] += 1
                    time_dictionary['10:00'] += 1
                    time_dictionary['10:30'] += 1
                    time_dictionary['11:00'] += 1
                    time_dictionary['11:30'] += 1
                    time_dictionary['12:00'] += 1
                    time_dictionary['12:30'] += 1
                    time_dictionary['13:00'] += 1
                    time_dictionary['13:30'] += 1
                    time_dictionary['14:00'] += 1
                    time_dictionary['14:30'] += 1
                    time_dictionary['15:00'] += 1
                    time_dictionary['15:30'] += 1
                    time_dictionary['16:00'] += 1
                    time_dictionary['16:30'] += 1
                    time_dictionary['17:00'] += 1
                    time_dictionary['17:30'] += 1
                    time_dictionary['18:00'] += 1

                elif 30 <= logoff[1] < 60:
                    time_dictionary['9:30'] += 1
                    time_dictionary['10:00'] += 1
                    time_dictionary['10:30'] += 1
                    time_dictionary['11:00'] += 1
                    time_dictionary['11:30'] += 1
                    time_dictionary['12:00'] += 1
                    time_dictionary['12:30'] += 1
                    time_dictionary['13:00'] += 1
                    time_dictionary['13:30'] += 1
                    time_dictionary['14:00'] += 1
                    time_dictionary['14:30'] += 1
                    time_dictionary['15:00'] += 1
                    time_dictionary['15:30'] += 1
                    time_dictionary['16:00'] += 1
                    time_dictionary['16:30'] += 1
                    time_dictionary['17:00'] += 1
                    time_dictionary['17:30'] += 1
                    time_dictionary['18:00'] += 1
                    time_dictionary['18:30'] += 1

            elif logoff[0] == logon[0] + 10:
                if 30 > logoff[1] >= 0:
                    time_dictionary['9:30'] += 1
                    time_dictionary['10:00'] += 1
                    time_dictionary['10:30'] += 1
                    time_dictionary['11:00'] += 1
                    time_dictionary['11:30'] += 1
                    time_dictionary['12:00'] += 1
                    time_dictionary['12:30'] += 1
                    time_dictionary['13:00'] += 1
                    time_dictionary['13:30'] += 1
                    time_dictionary['14:00'] += 1
                    time_dictionary['14:30'] += 1
                    time_dictionary['15:00'] += 1
                    time_dictionary['15:30'] += 1
                    time_dictionary['16:00'] += 1
                    time_dictionary['16:30'] += 1
                    time_dictionary['17:00'] += 1
                    time_dictionary['17:30'] += 1
                    time_dictionary['18:00'] += 1
                    time_dictionary['18:30'] += 1
                    time_dictionary['19:00'] += 1

                elif 30 <= logoff[1] < 60:
                    time_dictionary['9:30'] += 1
                    time_dictionary['10:00'] += 1
                    time_dictionary['10:30'] += 1
                    time_dictionary['11:00'] += 1
                    time_dictionary['11:30'] += 1
                    time_dictionary['12:00'] += 1
                    time_dictionary['12:30'] += 1
                    time_dictionary['13:00'] += 1
                    time_dictionary['13:30'] += 1
                    time_dictionary['14:00'] += 1
                    time_dictionary['14:30'] += 1
                    time_dictionary['15:00'] += 1
                    time_dictionary['15:30'] += 1
                    time_dictionary['16:00'] += 1
                    time_dictionary['16:30'] += 1
                    time_dictionary['17:00'] += 1
                    time_dictionary['17:30'] += 1
                    time_dictionary['18:00'] += 1
                    time_dictionary['18:30'] += 1
                    time_dictionary['19:00'] += 1
                    time_dictionary['19:30'] += 1

            elif logoff[0] == logon[0] + 11:
                if 30 > logoff[1] >= 0:
                    time_dictionary['9:30'] += 1
                    time_dictionary['10:00'] += 1
                    time_dictionary['10:30'] += 1
                    time_dictionary['11:00'] += 1
                    time_dictionary['11:30'] += 1
                    time_dictionary['12:00'] += 1
                    time_dictionary['12:30'] += 1
                    time_dictionary['13:00'] += 1
                    time_dictionary['13:30'] += 1
                    time_dictionary['14:00'] += 1
                    time_dictionary['14:30'] += 1
                    time_dictionary['15:00'] += 1
                    time_dictionary['15:30'] += 1
                    time_dictionary['16:00'] += 1
                    time_dictionary['16:30'] += 1
                    time_dictionary['17:00'] += 1
                    time_dictionary['17:30'] += 1
                    time_dictionary['18:00'] += 1
                    time_dictionary['18:30'] += 1
                    time_dictionary['19:00'] += 1
                    time_dictionary['19:30'] += 1
                    time_dictionary['20:00'] += 1

                elif 30 <= logoff[1] < 60:
                    time_dictionary['9:30'] += 1
                    time_dictionary['10:00'] += 1
                    time_dictionary['10:30'] += 1
                    time_dictionary['11:00'] += 1
                    time_dictionary['11:30'] += 1
                    time_dictionary['12:00'] += 1
                    time_dictionary['12:30'] += 1
                    time_dictionary['13:00'] += 1
                    time_dictionary['13:30'] += 1
                    time_dictionary['14:00'] += 1
                    time_dictionary['14:30'] += 1
                    time_dictionary['15:00'] += 1
                    time_dictionary['15:30'] += 1
                    time_dictionary['16:00'] += 1
                    time_dictionary['16:30'] += 1
                    time_dictionary['17:00'] += 1
                    time_dictionary['17:30'] += 1
                    time_dictionary['18:00'] += 1
                    time_dictionary['18:30'] += 1
                    time_dictionary['19:00'] += 1
                    time_dictionary['19:30'] += 1
                    time_dictionary['20:00'] += 1
                    time_dictionary['20:30'] += 1

            elif logoff[0] == logon[0] + 12:
                if 30 > logoff[1] >= 0:
                    time_dictionary['9:30'] += 1
                    time_dictionary['10:00'] += 1
                    time_dictionary['10:30'] += 1
                    time_dictionary['11:00'] += 1
                    time_dictionary['11:30'] += 1
                    time_dictionary['12:00'] += 1
                    time_dictionary['12:30'] += 1
                    time_dictionary['13:00'] += 1
                    time_dictionary['13:30'] += 1
                    time_dictionary['14:00'] += 1
                    time_dictionary['14:30'] += 1
                    time_dictionary['15:00'] += 1
                    time_dictionary['15:30'] += 1
                    time_dictionary['16:00'] += 1
                    time_dictionary['16:30'] += 1
                    time_dictionary['17:00'] += 1
                    time_dictionary['17:30'] += 1
                    time_dictionary['18:00'] += 1
                    time_dictionary['18:30'] += 1
                    time_dictionary['19:00'] += 1
                    time_dictionary['19:30'] += 1
                    time_dictionary['20:00'] += 1
                    time_dictionary['20:30'] += 1
                    time_dictionary['21:00'] += 1

                elif 30 <= logoff[1] < 60:
                    time_dictionary['9:30'] += 1
                    time_dictionary['10:00'] += 1
                    time_dictionary['10:30'] += 1
                    time_dictionary['11:00'] += 1
                    time_dictionary['11:30'] += 1
                    time_dictionary['12:00'] += 1
                    time_dictionary['12:30'] += 1
                    time_dictionary['13:00'] += 1
                    time_dictionary['13:30'] += 1
                    time_dictionary['14:00'] += 1
                    time_dictionary['14:30'] += 1
                    time_dictionary['15:00'] += 1
                    time_dictionary['15:30'] += 1
                    time_dictionary['16:00'] += 1
                    time_dictionary['16:30'] += 1
                    time_dictionary['17:00'] += 1
                    time_dictionary['17:30'] += 1
                    time_dictionary['18:00'] += 1
                    time_dictionary['18:30'] += 1
                    time_dictionary['19:00'] += 1
                    time_dictionary['19:30'] += 1
                    time_dictionary['20:00'] += 1
                    time_dictionary['20:30'] += 1
                    time_dictionary['21:00'] += 1
                    time_dictionary['21:30'] += 1

        elif logon[0] == 9 and 30 <= logon[1] < 60:
            time_dictionary['9:30'] += 1

            if logoff[0] == logon[0] + 1:
                if 30 > logoff[1] >= 0:
                    time_dictionary['10:00'] += 1

                elif 30 <= logon[1] < 60:
                    time_dictionary['10:00'] += 1
                    time_dictionary['10:30'] += 1

            if logoff[0] == logon[0] + 2:
                if 30 > logoff[1] >= 0:
                    time_dictionary['10:00'] += 1
                    time_dictionary['10:30'] += 1
                    time_dictionary['11:00'] += 1

                elif 30 <= logon[1] < 60:
                    time_dictionary['10:00'] += 1
                    time_dictionary['10:30'] += 1
                    time_dictionary['11:00'] += 1
                    time_dictionary['11:30'] += 1

            if logoff[0] == logon[0] + 3:
                if 30 > logoff[1] >= 0:
                    time_dictionary['10:00'] += 1
                    time_dictionary['10:30'] += 1
                    time_dictionary['11:00'] += 1
                    time_dictionary['11:30'] += 1
                    time_dictionary['12:00'] += 1

                elif 30 <= logon[1] < 60:
                    time_dictionary['10:00'] += 1
                    time_dictionary['10:30'] += 1
                    time_dictionary['11:00'] += 1
                    time_dictionary['11:30'] += 1
                    time_dictionary['12:00'] += 1
                    time_dictionary['12:30'] += 1

            if logoff[0] == logon[0] + 4:
                if 30 > logoff[1] >= 0:
                    time_dictionary['10:00'] += 1
                    time_dictionary['10:30'] += 1
                    time_dictionary['11:00'] += 1
                    time_dictionary['11:30'] += 1
                    time_dictionary['12:00'] += 1
                    time_dictionary['12:30'] += 1
                    time_dictionary['13:00'] += 1

                elif 30 <= logon[1] < 60:
                    time_dictionary['10:00'] += 1
                    time_dictionary['10:30'] += 1
                    time_dictionary['11:00'] += 1
                    time_dictionary['11:30'] += 1
                    time_dictionary['12:00'] += 1
                    time_dictionary['12:30'] += 1
                    time_dictionary['13:00'] += 1
                    time_dictionary['13:30'] += 1

            if logoff[0] == logon[0] + 5:
                if 30 > logoff[1] >= 0:
                    time_dictionary['10:00'] += 1
                    time_dictionary['10:30'] += 1
                    time_dictionary['11:00'] += 1
                    time_dictionary['11:30'] += 1
                    time_dictionary['12:00'] += 1
                    time_dictionary['12:30'] += 1
                    time_dictionary['13:00'] += 1
                    time_dictionary['13:30'] += 1
                    time_dictionary['14:00'] += 1

                elif 30 <= logon[1] < 60:
                    time_dictionary['10:00'] += 1
                    time_dictionary['10:30'] += 1
                    time_dictionary['11:00'] += 1
                    time_dictionary['11:30'] += 1
                    time_dictionary['12:00'] += 1
                    time_dictionary['12:30'] += 1
                    time_dictionary['13:00'] += 1
                    time_dictionary['13:30'] += 1
                    time_dictionary['14:00'] += 1
                    time_dictionary['14:30'] += 1

            if logoff[0] == logon[0] + 6:
                if 30 > logoff[1] >= 0:
                    time_dictionary['10:00'] += 1
                    time_dictionary['10:30'] += 1
                    time_dictionary['11:00'] += 1
                    time_dictionary['11:30'] += 1
                    time_dictionary['12:00'] += 1
                    time_dictionary['12:30'] += 1
                    time_dictionary['13:00'] += 1
                    time_dictionary['13:30'] += 1
                    time_dictionary['14:00'] += 1
                    time_dictionary['14:30'] += 1
                    time_dictionary['15:00'] += 1

                elif 30 <= logon[1] < 60:
                    time_dictionary['10:00'] += 1
                    time_dictionary['10:30'] += 1
                    time_dictionary['11:00'] += 1
                    time_dictionary['11:30'] += 1
                    time_dictionary['12:00'] += 1
                    time_dictionary['12:30'] += 1
                    time_dictionary['13:00'] += 1
                    time_dictionary['13:30'] += 1
                    time_dictionary['14:00'] += 1
                    time_dictionary['14:30'] += 1
                    time_dictionary['15:00'] += 1
                    time_dictionary['15:30'] += 1

            if logoff[0] == logon[0] + 7:
                if 30 > logoff[1] >= 0:
                    time_dictionary['10:00'] += 1
                    time_dictionary['10:30'] += 1
                    time_dictionary['11:00'] += 1
                    time_dictionary['11:30'] += 1
                    time_dictionary['12:00'] += 1
                    time_dictionary['12:30'] += 1
                    time_dictionary['13:00'] += 1
                    time_dictionary['13:30'] += 1
                    time_dictionary['14:00'] += 1
                    time_dictionary['14:30'] += 1
                    time_dictionary['15:00'] += 1
                    time_dictionary['15:30'] += 1
                    time_dictionary['16:00'] += 1

                elif 30 <= logon[1] < 60:
                    time_dictionary['10:00'] += 1
                    time_dictionary['10:30'] += 1
                    time_dictionary['11:00'] += 1
                    time_dictionary['11:30'] += 1
                    time_dictionary['12:00'] += 1
                    time_dictionary['12:30'] += 1
                    time_dictionary['13:00'] += 1
                    time_dictionary['13:30'] += 1
                    time_dictionary['14:00'] += 1
                    time_dictionary['14:30'] += 1
                    time_dictionary['15:00'] += 1
                    time_dictionary['15:30'] += 1
                    time_dictionary['16:00'] += 1
                    time_dictionary['16:30'] += 1

            if logoff[0] == logon[0] + 8:
                if 30 > logoff[1] >= 0:
                    time_dictionary['10:00'] += 1
                    time_dictionary['10:30'] += 1
                    time_dictionary['11:00'] += 1
                    time_dictionary['11:30'] += 1
                    time_dictionary['12:00'] += 1
                    time_dictionary['12:30'] += 1
                    time_dictionary['13:00'] += 1
                    time_dictionary['13:30'] += 1
                    time_dictionary['14:00'] += 1
                    time_dictionary['14:30'] += 1
                    time_dictionary['15:00'] += 1
                    time_dictionary['15:30'] += 1
                    time_dictionary['16:00'] += 1
                    time_dictionary['16:30'] += 1
                    time_dictionary['17:00'] += 1

                elif 30 <= logon[1] < 60:
                    time_dictionary['10:00'] += 1
                    time_dictionary['10:30'] += 1
                    time_dictionary['11:00'] += 1
                    time_dictionary['11:30'] += 1
                    time_dictionary['12:00'] += 1
                    time_dictionary['12:30'] += 1
                    time_dictionary['13:00'] += 1
                    time_dictionary['13:30'] += 1
                    time_dictionary['14:00'] += 1
                    time_dictionary['14:30'] += 1
                    time_dictionary['15:00'] += 1
                    time_dictionary['15:30'] += 1
                    time_dictionary['16:00'] += 1
                    time_dictionary['16:30'] += 1
                    time_dictionary['17:00'] += 1
                    time_dictionary['17:30'] += 1

            if logoff[0] == logon[0] + 9:
                if 30 > logoff[1] >= 0:
                    time_dictionary['10:00'] += 1
                    time_dictionary['10:30'] += 1
                    time_dictionary['11:00'] += 1
                    time_dictionary['11:30'] += 1
                    time_dictionary['12:00'] += 1
                    time_dictionary['12:30'] += 1
                    time_dictionary['13:00'] += 1
                    time_dictionary['13:30'] += 1
                    time_dictionary['14:00'] += 1
                    time_dictionary['14:30'] += 1
                    time_dictionary['15:00'] += 1
                    time_dictionary['15:30'] += 1
                    time_dictionary['16:00'] += 1
                    time_dictionary['16:30'] += 1
                    time_dictionary['17:00'] += 1
                    time_dictionary['17:30'] += 1
                    time_dictionary['18:00'] += 1

                elif 30 <= logon[1] < 60:
                    time_dictionary['10:00'] += 1
                    time_dictionary['10:30'] += 1
                    time_dictionary['11:00'] += 1
                    time_dictionary['11:30'] += 1
                    time_dictionary['12:00'] += 1
                    time_dictionary['12:30'] += 1
                    time_dictionary['13:00'] += 1
                    time_dictionary['13:30'] += 1
                    time_dictionary['14:00'] += 1
                    time_dictionary['14:30'] += 1
                    time_dictionary['15:00'] += 1
                    time_dictionary['15:30'] += 1
                    time_dictionary['16:00'] += 1
                    time_dictionary['16:30'] += 1
                    time_dictionary['17:00'] += 1
                    time_dictionary['17:30'] += 1
                    time_dictionary['18:00'] += 1
                    time_dictionary['18:30'] += 1

            if logoff[0] == logon[0] + 10:
                if 30 > logoff[1] >= 0:
                    time_dictionary['10:00'] += 1
                    time_dictionary['10:30'] += 1
                    time_dictionary['11:00'] += 1
                    time_dictionary['11:30'] += 1
                    time_dictionary['12:00'] += 1
                    time_dictionary['12:30'] += 1
                    time_dictionary['13:00'] += 1
                    time_dictionary['13:30'] += 1
                    time_dictionary['14:00'] += 1
                    time_dictionary['14:30'] += 1
                    time_dictionary['15:00'] += 1
                    time_dictionary['15:30'] += 1
                    time_dictionary['16:00'] += 1
                    time_dictionary['16:30'] += 1
                    time_dictionary['17:00'] += 1
                    time_dictionary['17:30'] += 1
                    time_dictionary['18:00'] += 1
                    time_dictionary['18:30'] += 1
                    time_dictionary['19:00'] += 1

                elif 30 <= logon[1] < 60:
                    time_dictionary['10:00'] += 1
                    time_dictionary['10:30'] += 1
                    time_dictionary['11:00'] += 1
                    time_dictionary['11:30'] += 1
                    time_dictionary['12:00'] += 1
                    time_dictionary['12:30'] += 1
                    time_dictionary['13:00'] += 1
                    time_dictionary['13:30'] += 1
                    time_dictionary['14:00'] += 1
                    time_dictionary['14:30'] += 1
                    time_dictionary['15:00'] += 1
                    time_dictionary['15:30'] += 1
                    time_dictionary['16:00'] += 1
                    time_dictionary['16:30'] += 1
                    time_dictionary['17:00'] += 1
                    time_dictionary['17:30'] += 1
                    time_dictionary['18:00'] += 1
                    time_dictionary['18:30'] += 1
                    time_dictionary['19:00'] += 1
                    time_dictionary['19:30'] += 1

            if logoff[0] == logon[0] + 11:
                if 30 > logoff[1] >= 0:
                    time_dictionary['10:00'] += 1
                    time_dictionary['10:30'] += 1
                    time_dictionary['11:00'] += 1
                    time_dictionary['11:30'] += 1
                    time_dictionary['12:00'] += 1
                    time_dictionary['12:30'] += 1
                    time_dictionary['13:00'] += 1
                    time_dictionary['13:30'] += 1
                    time_dictionary['14:00'] += 1
                    time_dictionary['14:30'] += 1
                    time_dictionary['15:00'] += 1
                    time_dictionary['15:30'] += 1
                    time_dictionary['16:00'] += 1
                    time_dictionary['16:30'] += 1
                    time_dictionary['17:00'] += 1
                    time_dictionary['17:30'] += 1
                    time_dictionary['18:00'] += 1
                    time_dictionary['18:30'] += 1
                    time_dictionary['19:00'] += 1
                    time_dictionary['19:30'] += 1
                    time_dictionary['20:00'] += 1

                elif 30 <= logon[1] < 60:
                    time_dictionary['10:00'] += 1
                    time_dictionary['10:30'] += 1
                    time_dictionary['11:00'] += 1
                    time_dictionary['11:30'] += 1
                    time_dictionary['12:00'] += 1
                    time_dictionary['12:30'] += 1
                    time_dictionary['13:00'] += 1
                    time_dictionary['13:30'] += 1
                    time_dictionary['14:00'] += 1
                    time_dictionary['14:30'] += 1
                    time_dictionary['15:00'] += 1
                    time_dictionary['15:30'] += 1
                    time_dictionary['16:00'] += 1
                    time_dictionary['16:30'] += 1
                    time_dictionary['17:00'] += 1
                    time_dictionary['17:30'] += 1
                    time_dictionary['18:00'] += 1
                    time_dictionary['18:30'] += 1
                    time_dictionary['19:00'] += 1
                    time_dictionary['19:30'] += 1
                    time_dictionary['20:00'] += 1
                    time_dictionary['20:30'] += 1

            if logoff[0] == logon[0] + 12:
                if 30 > logoff[1] >= 0:
                    time_dictionary['10:00'] += 1
                    time_dictionary['10:30'] += 1
                    time_dictionary['11:00'] += 1
                    time_dictionary['11:30'] += 1
                    time_dictionary['12:00'] += 1
                    time_dictionary['12:30'] += 1
                    time_dictionary['13:00'] += 1
                    time_dictionary['13:30'] += 1
                    time_dictionary['14:00'] += 1
                    time_dictionary['14:30'] += 1
                    time_dictionary['15:00'] += 1
                    time_dictionary['15:30'] += 1
                    time_dictionary['16:00'] += 1
                    time_dictionary['16:30'] += 1
                    time_dictionary['17:00'] += 1
                    time_dictionary['17:30'] += 1
                    time_dictionary['18:00'] += 1
                    time_dictionary['18:30'] += 1
                    time_dictionary['19:00'] += 1
                    time_dictionary['19:30'] += 1
                    time_dictionary['20:00'] += 1
                    time_dictionary['20:30'] += 1
                    time_dictionary['21:00'] += 1

                elif 30 <= logon[1] < 60:
                    time_dictionary['10:00'] += 1
                    time_dictionary['10:30'] += 1
                    time_dictionary['11:00'] += 1
                    time_dictionary['11:30'] += 1
                    time_dictionary['12:00'] += 1
                    time_dictionary['12:30'] += 1
                    time_dictionary['13:00'] += 1
                    time_dictionary['13:30'] += 1
                    time_dictionary['14:00'] += 1
                    time_dictionary['14:30'] += 1
                    time_dictionary['15:00'] += 1
                    time_dictionary['15:30'] += 1
                    time_dictionary['16:00'] += 1
                    time_dictionary['16:30'] += 1
                    time_dictionary['17:00'] += 1
                    time_dictionary['17:30'] += 1
                    time_dictionary['18:00'] += 1
                    time_dictionary['18:30'] += 1
                    time_dictionary['19:00'] += 1
                    time_dictionary['19:30'] += 1
                    time_dictionary['20:00'] += 1
                    time_dictionary['20:30'] += 1
                    time_dictionary['21:00'] += 1
                    time_dictionary['21:30'] += 1

        elif logon[0] == 10 and 30 > logon[1] >= 0:
            time_dictionary['10:00'] += 1

            if logoff[0] == logon[0]:
                if 30 <= logoff[1] < 60:
                    time_dictionary['10:30'] += 1

            elif logoff[0] == logon[0] + 1:
                if 30 > logoff[1] >= 0:
                    time_dictionary['10:30'] += 1
                    time_dictionary['11:00'] += 1

                elif 30 <= logoff[1] < 60:
                    time_dictionary['10:30'] += 1
                    time_dictionary['11:00'] += 1
                    time_dictionary['11:30'] += 1

            elif logoff[0] == logon[0] + 2:
                if 30 > logoff[1] >= 0:
                    time_dictionary['10:30'] += 1
                    time_dictionary['11:00'] += 1
                    time_dictionary['11:30'] += 1
                    time_dictionary['12:00'] += 1

                elif 30 <= logoff[1] < 60:
                    time_dictionary['10:30'] += 1
                    time_dictionary['11:00'] += 1
                    time_dictionary['11:30'] += 1
                    time_dictionary['12:00'] += 1
                    time_dictionary['12:30'] += 1

            elif logoff[0] == logon[0] + 3:
                if 30 > logoff[1] >= 0:
                    time_dictionary['10:30'] += 1
                    time_dictionary['11:00'] += 1
                    time_dictionary['11:30'] += 1
                    time_dictionary['12:00'] += 1
                    time_dictionary['12:30'] += 1
                    time_dictionary['13:00'] += 1

                elif 30 <= logoff[1] < 60:
                    time_dictionary['10:30'] += 1
                    time_dictionary['11:00'] += 1
                    time_dictionary['11:30'] += 1
                    time_dictionary['12:00'] += 1
                    time_dictionary['12:30'] += 1
                    time_dictionary['13:00'] += 1
                    time_dictionary['13:30'] += 1

            elif logoff[0] == logon[0] + 4:
                if 30 > logoff[1] >= 0:
                    time_dictionary['10:30'] += 1
                    time_dictionary['11:00'] += 1
                    time_dictionary['11:30'] += 1
                    time_dictionary['12:00'] += 1
                    time_dictionary['12:30'] += 1
                    time_dictionary['13:00'] += 1
                    time_dictionary['13:30'] += 1
                    time_dictionary['14:00'] += 1

                elif 30 <= logoff[1] < 60:
                    time_dictionary['10:30'] += 1
                    time_dictionary['11:00'] += 1
                    time_dictionary['11:30'] += 1
                    time_dictionary['12:00'] += 1
                    time_dictionary['12:30'] += 1
                    time_dictionary['13:00'] += 1
                    time_dictionary['13:30'] += 1
                    time_dictionary['14:00'] += 1
                    time_dictionary['14:30'] += 1

            elif logoff[0] == logon[0] + 5:
                if 30 > logoff[1] >= 0:
                    time_dictionary['10:30'] += 1
                    time_dictionary['11:00'] += 1
                    time_dictionary['11:30'] += 1
                    time_dictionary['12:00'] += 1
                    time_dictionary['12:30'] += 1
                    time_dictionary['13:00'] += 1
                    time_dictionary['13:30'] += 1
                    time_dictionary['14:00'] += 1
                    time_dictionary['14:30'] += 1
                    time_dictionary['15:00'] += 1

                elif 30 <= logoff[1] < 60:
                    time_dictionary['10:30'] += 1
                    time_dictionary['11:00'] += 1
                    time_dictionary['11:30'] += 1
                    time_dictionary['12:00'] += 1
                    time_dictionary['12:30'] += 1
                    time_dictionary['13:00'] += 1
                    time_dictionary['13:30'] += 1
                    time_dictionary['14:00'] += 1
                    time_dictionary['14:30'] += 1
                    time_dictionary['15:00'] += 1
                    time_dictionary['15:30'] += 1

            elif logoff[0] == logon[0] + 6:
                if 30 > logoff[1] >= 0:
                    time_dictionary['10:30'] += 1
                    time_dictionary['11:00'] += 1
                    time_dictionary['11:30'] += 1
                    time_dictionary['12:00'] += 1
                    time_dictionary['12:30'] += 1
                    time_dictionary['13:00'] += 1
                    time_dictionary['13:30'] += 1
                    time_dictionary['14:00'] += 1
                    time_dictionary['14:30'] += 1
                    time_dictionary['15:00'] += 1
                    time_dictionary['15:30'] += 1
                    time_dictionary['16:00'] += 1

                elif 30 <= logoff[1] < 60:
                    time_dictionary['10:30'] += 1
                    time_dictionary['11:00'] += 1
                    time_dictionary['11:30'] += 1
                    time_dictionary['12:00'] += 1
                    time_dictionary['12:30'] += 1
                    time_dictionary['13:00'] += 1
                    time_dictionary['13:30'] += 1
                    time_dictionary['14:00'] += 1
                    time_dictionary['14:30'] += 1
                    time_dictionary['15:00'] += 1
                    time_dictionary['15:30'] += 1
                    time_dictionary['16:00'] += 1
                    time_dictionary['16:30'] += 1

            elif logoff[0] == logon[0] + 7:
                if 30 > logoff[1] >= 0:
                    time_dictionary['10:30'] += 1
                    time_dictionary['11:00'] += 1
                    time_dictionary['11:30'] += 1
                    time_dictionary['12:00'] += 1
                    time_dictionary['12:30'] += 1
                    time_dictionary['13:00'] += 1
                    time_dictionary['13:30'] += 1
                    time_dictionary['14:00'] += 1
                    time_dictionary['14:30'] += 1
                    time_dictionary['15:00'] += 1
                    time_dictionary['15:30'] += 1
                    time_dictionary['16:00'] += 1
                    time_dictionary['16:30'] += 1
                    time_dictionary['17:00'] += 1

                elif 30 <= logoff[1] < 60:
                    time_dictionary['10:30'] += 1
                    time_dictionary['11:00'] += 1
                    time_dictionary['11:30'] += 1
                    time_dictionary['12:00'] += 1
                    time_dictionary['12:30'] += 1
                    time_dictionary['13:00'] += 1
                    time_dictionary['13:30'] += 1
                    time_dictionary['14:00'] += 1
                    time_dictionary['14:30'] += 1
                    time_dictionary['15:00'] += 1
                    time_dictionary['15:30'] += 1
                    time_dictionary['16:00'] += 1
                    time_dictionary['16:30'] += 1
                    time_dictionary['17:00'] += 1
                    time_dictionary['17:30'] += 1

            elif logoff[0] == logon[0] + 8:
                if 30 > logoff[1] >= 0:
                    time_dictionary['10:30'] += 1
                    time_dictionary['11:00'] += 1
                    time_dictionary['11:30'] += 1
                    time_dictionary['12:00'] += 1
                    time_dictionary['12:30'] += 1
                    time_dictionary['13:00'] += 1
                    time_dictionary['13:30'] += 1
                    time_dictionary['14:00'] += 1
                    time_dictionary['14:30'] += 1
                    time_dictionary['15:00'] += 1
                    time_dictionary['15:30'] += 1
                    time_dictionary['16:00'] += 1
                    time_dictionary['16:30'] += 1
                    time_dictionary['17:00'] += 1
                    time_dictionary['17:30'] += 1
                    time_dictionary['18:00'] += 1

                elif 30 <= logoff[1] < 60:
                    time_dictionary['10:30'] += 1
                    time_dictionary['11:00'] += 1
                    time_dictionary['11:30'] += 1
                    time_dictionary['12:00'] += 1
                    time_dictionary['12:30'] += 1
                    time_dictionary['13:00'] += 1
                    time_dictionary['13:30'] += 1
                    time_dictionary['14:00'] += 1
                    time_dictionary['14:30'] += 1
                    time_dictionary['15:00'] += 1
                    time_dictionary['15:30'] += 1
                    time_dictionary['16:00'] += 1
                    time_dictionary['16:30'] += 1
                    time_dictionary['17:00'] += 1
                    time_dictionary['17:30'] += 1
                    time_dictionary['18:00'] += 1
                    time_dictionary['18:30'] += 1

            elif logoff[0] == logon[0] + 9:
                if 30 > logoff[1] >= 0:
                    time_dictionary['10:30'] += 1
                    time_dictionary['11:00'] += 1
                    time_dictionary['11:30'] += 1
                    time_dictionary['12:00'] += 1
                    time_dictionary['12:30'] += 1
                    time_dictionary['13:00'] += 1
                    time_dictionary['13:30'] += 1
                    time_dictionary['14:00'] += 1
                    time_dictionary['14:30'] += 1
                    time_dictionary['15:00'] += 1
                    time_dictionary['15:30'] += 1
                    time_dictionary['16:00'] += 1
                    time_dictionary['16:30'] += 1
                    time_dictionary['17:00'] += 1
                    time_dictionary['17:30'] += 1
                    time_dictionary['18:00'] += 1
                    time_dictionary['18:30'] += 1
                    time_dictionary['19:00'] += 1

                elif 30 <= logoff[1] < 60:
                    time_dictionary['10:30'] += 1
                    time_dictionary['11:00'] += 1
                    time_dictionary['11:30'] += 1
                    time_dictionary['12:00'] += 1
                    time_dictionary['12:30'] += 1
                    time_dictionary['13:00'] += 1
                    time_dictionary['13:30'] += 1
                    time_dictionary['14:00'] += 1
                    time_dictionary['14:30'] += 1
                    time_dictionary['15:00'] += 1
                    time_dictionary['15:30'] += 1
                    time_dictionary['16:00'] += 1
                    time_dictionary['16:30'] += 1
                    time_dictionary['17:00'] += 1
                    time_dictionary['17:30'] += 1
                    time_dictionary['18:00'] += 1
                    time_dictionary['18:30'] += 1
                    time_dictionary['19:00'] += 1
                    time_dictionary['19:30'] += 1

            elif logoff[0] == logon[0] + 10:
                if 30 > logoff[1] >= 0:
                    time_dictionary['10:30'] += 1
                    time_dictionary['11:00'] += 1
                    time_dictionary['11:30'] += 1
                    time_dictionary['12:00'] += 1
                    time_dictionary['12:30'] += 1
                    time_dictionary['13:00'] += 1
                    time_dictionary['13:30'] += 1
                    time_dictionary['14:00'] += 1
                    time_dictionary['14:30'] += 1
                    time_dictionary['15:00'] += 1
                    time_dictionary['15:30'] += 1
                    time_dictionary['16:00'] += 1
                    time_dictionary['16:30'] += 1
                    time_dictionary['17:00'] += 1
                    time_dictionary['17:30'] += 1
                    time_dictionary['18:00'] += 1
                    time_dictionary['18:30'] += 1
                    time_dictionary['19:00'] += 1
                    time_dictionary['19:30'] += 1
                    time_dictionary['20:00'] += 1

                elif 30 <= logoff[1] < 60:
                    time_dictionary['10:30'] += 1
                    time_dictionary['11:00'] += 1
                    time_dictionary['11:30'] += 1
                    time_dictionary['12:00'] += 1
                    time_dictionary['12:30'] += 1
                    time_dictionary['13:00'] += 1
                    time_dictionary['13:30'] += 1
                    time_dictionary['14:00'] += 1
                    time_dictionary['14:30'] += 1
                    time_dictionary['15:00'] += 1
                    time_dictionary['15:30'] += 1
                    time_dictionary['16:00'] += 1
                    time_dictionary['16:30'] += 1
                    time_dictionary['17:00'] += 1
                    time_dictionary['17:30'] += 1
                    time_dictionary['18:00'] += 1
                    time_dictionary['18:30'] += 1
                    time_dictionary['19:00'] += 1
                    time_dictionary['19:30'] += 1
                    time_dictionary['20:00'] += 1
                    time_dictionary['20:30'] += 1

            elif logoff[0] == logon[0] + 11:
                if 30 > logoff[1] >= 0:
                    time_dictionary['10:30'] += 1
                    time_dictionary['11:00'] += 1
                    time_dictionary['11:30'] += 1
                    time_dictionary['12:00'] += 1
                    time_dictionary['12:30'] += 1
                    time_dictionary['13:00'] += 1
                    time_dictionary['13:30'] += 1
                    time_dictionary['14:00'] += 1
                    time_dictionary['14:30'] += 1
                    time_dictionary['15:00'] += 1
                    time_dictionary['15:30'] += 1
                    time_dictionary['16:00'] += 1
                    time_dictionary['16:30'] += 1
                    time_dictionary['17:00'] += 1
                    time_dictionary['17:30'] += 1
                    time_dictionary['18:00'] += 1
                    time_dictionary['18:30'] += 1
                    time_dictionary['19:00'] += 1
                    time_dictionary['19:30'] += 1
                    time_dictionary['20:00'] += 1
                    time_dictionary['20:30'] += 1
                    time_dictionary['21:00'] += 1

                elif 30 <= logoff[1] < 60:
                    time_dictionary['10:30'] += 1
                    time_dictionary['11:00'] += 1
                    time_dictionary['11:30'] += 1
                    time_dictionary['12:00'] += 1
                    time_dictionary['12:30'] += 1
                    time_dictionary['13:00'] += 1
                    time_dictionary['13:30'] += 1
                    time_dictionary['14:00'] += 1
                    time_dictionary['14:30'] += 1
                    time_dictionary['15:00'] += 1
                    time_dictionary['15:30'] += 1
                    time_dictionary['16:00'] += 1
                    time_dictionary['16:30'] += 1
                    time_dictionary['17:00'] += 1
                    time_dictionary['17:30'] += 1
                    time_dictionary['18:00'] += 1
                    time_dictionary['18:30'] += 1
                    time_dictionary['19:00'] += 1
                    time_dictionary['19:30'] += 1
                    time_dictionary['20:00'] += 1
                    time_dictionary['20:30'] += 1
                    time_dictionary['21:00'] += 1
                    time_dictionary['21:30'] += 1

        elif logon[0] == 10 and 30 <= logon[1] < 60:
            time_dictionary['10:30'] += 1

            if logoff[0] == logon[0] + 1:
                if 30 > logoff[1] >= 0:
                    time_dictionary['11:00'] += 1

                elif 30 <= logon[1] < 60:
                    time_dictionary['11:00'] += 1
                    time_dictionary['11:30'] += 1

            if logoff[0] == logon[0] + 2:
                if 30 > logoff[1] >= 0:
                    time_dictionary['11:00'] += 1
                    time_dictionary['11:30'] += 1
                    time_dictionary['12:00'] += 1

                elif 30 <= logon[1] < 60:
                    time_dictionary['11:00'] += 1
                    time_dictionary['11:30'] += 1
                    time_dictionary['12:00'] += 1
                    time_dictionary['12:30'] += 1

            if logoff[0] == logon[0] + 3:
                if 30 > logoff[1] >= 0:
                    time_dictionary['11:00'] += 1
                    time_dictionary['11:30'] += 1
                    time_dictionary['12:00'] += 1
                    time_dictionary['12:30'] += 1
                    time_dictionary['13:00'] += 1

                elif 30 <= logon[1] < 60:
                    time_dictionary['11:00'] += 1
                    time_dictionary['11:30'] += 1
                    time_dictionary['12:00'] += 1
                    time_dictionary['12:30'] += 1
                    time_dictionary['13:00'] += 1
                    time_dictionary['13:30'] += 1

            if logoff[0] == logon[0] + 4:
                if 30 > logoff[1] >= 0:
                    time_dictionary['11:00'] += 1
                    time_dictionary['11:30'] += 1
                    time_dictionary['12:00'] += 1
                    time_dictionary['12:30'] += 1
                    time_dictionary['13:00'] += 1
                    time_dictionary['13:30'] += 1
                    time_dictionary['14:00'] += 1

                elif 30 <= logon[1] < 60:
                    time_dictionary['11:00'] += 1
                    time_dictionary['11:30'] += 1
                    time_dictionary['12:00'] += 1
                    time_dictionary['12:30'] += 1
                    time_dictionary['13:00'] += 1
                    time_dictionary['13:30'] += 1
                    time_dictionary['14:00'] += 1
                    time_dictionary['14:30'] += 1

            if logoff[0] == logon[0] + 5:
                if 30 > logoff[1] >= 0:
                    time_dictionary['11:00'] += 1
                    time_dictionary['11:30'] += 1
                    time_dictionary['12:00'] += 1
                    time_dictionary['12:30'] += 1
                    time_dictionary['13:00'] += 1
                    time_dictionary['13:30'] += 1
                    time_dictionary['14:00'] += 1
                    time_dictionary['14:30'] += 1
                    time_dictionary['15:00'] += 1

                elif 30 <= logon[1] < 60:
                    time_dictionary['11:00'] += 1
                    time_dictionary['11:30'] += 1
                    time_dictionary['12:00'] += 1
                    time_dictionary['12:30'] += 1
                    time_dictionary['13:00'] += 1
                    time_dictionary['13:30'] += 1
                    time_dictionary['14:00'] += 1
                    time_dictionary['14:30'] += 1
                    time_dictionary['15:00'] += 1
                    time_dictionary['15:30'] += 1

            if logoff[0] == logon[0] + 6:
                if 30 > logoff[1] >= 0:
                    time_dictionary['11:00'] += 1
                    time_dictionary['11:30'] += 1
                    time_dictionary['12:00'] += 1
                    time_dictionary['12:30'] += 1
                    time_dictionary['13:00'] += 1
                    time_dictionary['13:30'] += 1
                    time_dictionary['14:00'] += 1
                    time_dictionary['14:30'] += 1
                    time_dictionary['15:00'] += 1
                    time_dictionary['15:30'] += 1
                    time_dictionary['16:00'] += 1

                elif 30 <= logon[1] < 60:
                    time_dictionary['11:00'] += 1
                    time_dictionary['11:30'] += 1
                    time_dictionary['12:00'] += 1
                    time_dictionary['12:30'] += 1
                    time_dictionary['13:00'] += 1
                    time_dictionary['13:30'] += 1
                    time_dictionary['14:00'] += 1
                    time_dictionary['14:30'] += 1
                    time_dictionary['15:00'] += 1
                    time_dictionary['15:30'] += 1
                    time_dictionary['16:00'] += 1
                    time_dictionary['16:30'] += 1

            if logoff[0] == logon[0] + 7:
                if 30 > logoff[1] >= 0:
                    time_dictionary['11:00'] += 1
                    time_dictionary['11:30'] += 1
                    time_dictionary['12:00'] += 1
                    time_dictionary['12:30'] += 1
                    time_dictionary['13:00'] += 1
                    time_dictionary['13:30'] += 1
                    time_dictionary['14:00'] += 1
                    time_dictionary['14:30'] += 1
                    time_dictionary['15:00'] += 1
                    time_dictionary['15:30'] += 1
                    time_dictionary['16:00'] += 1
                    time_dictionary['16:30'] += 1
                    time_dictionary['17:00'] += 1

                elif 30 <= logon[1] < 60:
                    time_dictionary['11:00'] += 1
                    time_dictionary['11:30'] += 1
                    time_dictionary['12:00'] += 1
                    time_dictionary['12:30'] += 1
                    time_dictionary['13:00'] += 1
                    time_dictionary['13:30'] += 1
                    time_dictionary['14:00'] += 1
                    time_dictionary['14:30'] += 1
                    time_dictionary['15:00'] += 1
                    time_dictionary['15:30'] += 1
                    time_dictionary['16:00'] += 1
                    time_dictionary['16:30'] += 1
                    time_dictionary['17:00'] += 1
                    time_dictionary['17:30'] += 1

            if logoff[0] == logon[0] + 8:
                if 30 > logoff[1] >= 0:
                    time_dictionary['11:00'] += 1
                    time_dictionary['11:30'] += 1
                    time_dictionary['12:00'] += 1
                    time_dictionary['12:30'] += 1
                    time_dictionary['13:00'] += 1
                    time_dictionary['13:30'] += 1
                    time_dictionary['14:00'] += 1
                    time_dictionary['14:30'] += 1
                    time_dictionary['15:00'] += 1
                    time_dictionary['15:30'] += 1
                    time_dictionary['16:00'] += 1
                    time_dictionary['16:30'] += 1
                    time_dictionary['17:00'] += 1
                    time_dictionary['17:30'] += 1
                    time_dictionary['18:00'] += 1

                elif 30 <= logon[1] < 60:
                    time_dictionary['11:00'] += 1
                    time_dictionary['11:30'] += 1
                    time_dictionary['12:00'] += 1
                    time_dictionary['12:30'] += 1
                    time_dictionary['13:00'] += 1
                    time_dictionary['13:30'] += 1
                    time_dictionary['14:00'] += 1
                    time_dictionary['14:30'] += 1
                    time_dictionary['15:00'] += 1
                    time_dictionary['15:30'] += 1
                    time_dictionary['16:00'] += 1
                    time_dictionary['16:30'] += 1
                    time_dictionary['17:00'] += 1
                    time_dictionary['17:30'] += 1
                    time_dictionary['18:00'] += 1
                    time_dictionary['18:30'] += 1

            if logoff[0] == logon[0] + 9:
                if 30 > logoff[1] >= 0:
                    time_dictionary['11:00'] += 1
                    time_dictionary['11:30'] += 1
                    time_dictionary['12:00'] += 1
                    time_dictionary['12:30'] += 1
                    time_dictionary['13:00'] += 1
                    time_dictionary['13:30'] += 1
                    time_dictionary['14:00'] += 1
                    time_dictionary['14:30'] += 1
                    time_dictionary['15:00'] += 1
                    time_dictionary['15:30'] += 1
                    time_dictionary['16:00'] += 1
                    time_dictionary['16:30'] += 1
                    time_dictionary['17:00'] += 1
                    time_dictionary['17:30'] += 1
                    time_dictionary['18:00'] += 1
                    time_dictionary['18:30'] += 1
                    time_dictionary['19:00'] += 1

                elif 30 <= logon[1] < 60:
                    time_dictionary['11:00'] += 1
                    time_dictionary['11:30'] += 1
                    time_dictionary['12:00'] += 1
                    time_dictionary['12:30'] += 1
                    time_dictionary['13:00'] += 1
                    time_dictionary['13:30'] += 1
                    time_dictionary['14:00'] += 1
                    time_dictionary['14:30'] += 1
                    time_dictionary['15:00'] += 1
                    time_dictionary['15:30'] += 1
                    time_dictionary['16:00'] += 1
                    time_dictionary['16:30'] += 1
                    time_dictionary['17:00'] += 1
                    time_dictionary['17:30'] += 1
                    time_dictionary['18:00'] += 1
                    time_dictionary['18:30'] += 1
                    time_dictionary['19:00'] += 1
                    time_dictionary['19:30'] += 1

            if logoff[0] == logon[0] + 10:
                if 30 > logoff[1] >= 0:
                    time_dictionary['11:00'] += 1
                    time_dictionary['11:30'] += 1
                    time_dictionary['12:00'] += 1
                    time_dictionary['12:30'] += 1
                    time_dictionary['13:00'] += 1
                    time_dictionary['13:30'] += 1
                    time_dictionary['14:00'] += 1
                    time_dictionary['14:30'] += 1
                    time_dictionary['15:00'] += 1
                    time_dictionary['15:30'] += 1
                    time_dictionary['16:00'] += 1
                    time_dictionary['16:30'] += 1
                    time_dictionary['17:00'] += 1
                    time_dictionary['17:30'] += 1
                    time_dictionary['18:00'] += 1
                    time_dictionary['18:30'] += 1
                    time_dictionary['19:00'] += 1
                    time_dictionary['19:30'] += 1
                    time_dictionary['20:00'] += 1

                elif 30 <= logon[1] < 60:
                    time_dictionary['11:00'] += 1
                    time_dictionary['11:30'] += 1
                    time_dictionary['12:00'] += 1
                    time_dictionary['12:30'] += 1
                    time_dictionary['13:00'] += 1
                    time_dictionary['13:30'] += 1
                    time_dictionary['14:00'] += 1
                    time_dictionary['14:30'] += 1
                    time_dictionary['15:00'] += 1
                    time_dictionary['15:30'] += 1
                    time_dictionary['16:00'] += 1
                    time_dictionary['16:30'] += 1
                    time_dictionary['17:00'] += 1
                    time_dictionary['17:30'] += 1
                    time_dictionary['18:00'] += 1
                    time_dictionary['18:30'] += 1
                    time_dictionary['19:00'] += 1
                    time_dictionary['19:30'] += 1
                    time_dictionary['20:00'] += 1
                    time_dictionary['20:30'] += 1

            if logoff[0] == logon[0] + 11:
                if 30 > logoff[1] >= 0:
                    time_dictionary['11:00'] += 1
                    time_dictionary['11:30'] += 1
                    time_dictionary['12:00'] += 1
                    time_dictionary['12:30'] += 1
                    time_dictionary['13:00'] += 1
                    time_dictionary['13:30'] += 1
                    time_dictionary['14:00'] += 1
                    time_dictionary['14:30'] += 1
                    time_dictionary['15:00'] += 1
                    time_dictionary['15:30'] += 1
                    time_dictionary['16:00'] += 1
                    time_dictionary['16:30'] += 1
                    time_dictionary['17:00'] += 1
                    time_dictionary['17:30'] += 1
                    time_dictionary['18:00'] += 1
                    time_dictionary['18:30'] += 1
                    time_dictionary['19:00'] += 1
                    time_dictionary['19:30'] += 1
                    time_dictionary['20:00'] += 1
                    time_dictionary['20:30'] += 1
                    time_dictionary['21:00'] += 1

                elif 30 <= logon[1] < 60:
                    time_dictionary['11:00'] += 1
                    time_dictionary['11:30'] += 1
                    time_dictionary['12:00'] += 1
                    time_dictionary['12:30'] += 1
                    time_dictionary['13:00'] += 1
                    time_dictionary['13:30'] += 1
                    time_dictionary['14:00'] += 1
                    time_dictionary['14:30'] += 1
                    time_dictionary['15:00'] += 1
                    time_dictionary['15:30'] += 1
                    time_dictionary['16:00'] += 1
                    time_dictionary['16:30'] += 1
                    time_dictionary['17:00'] += 1
                    time_dictionary['17:30'] += 1
                    time_dictionary['18:00'] += 1
                    time_dictionary['18:30'] += 1
                    time_dictionary['19:00'] += 1
                    time_dictionary['19:30'] += 1
                    time_dictionary['20:00'] += 1
                    time_dictionary['20:30'] += 1
                    time_dictionary['21:00'] += 1
                    time_dictionary['21:30'] += 1

        elif logon[0] == 11 and 30 > logon[1] >= 0:
            time_dictionary['11:00'] += 1

            if logoff[0] == logon[0]:
                if 30 <= logoff[1] < 60:
                    time_dictionary['11:30'] += 1

            elif logoff[0] == logon[0] + 1:
                if 30 > logoff[1] >= 0:
                    time_dictionary['11:30'] += 1
                    time_dictionary['12:00'] += 1

                elif 30 <= logoff[1] < 60:
                    time_dictionary['11:30'] += 1
                    time_dictionary['12:00'] += 1
                    time_dictionary['12:30'] += 1

            elif logoff[0] == logon[0] + 2:
                if 30 > logoff[1] >= 0:
                    time_dictionary['11:30'] += 1
                    time_dictionary['12:00'] += 1
                    time_dictionary['12:30'] += 1
                    time_dictionary['13:00'] += 1

                elif 30 <= logoff[1] < 60:
                    time_dictionary['11:30'] += 1
                    time_dictionary['12:00'] += 1
                    time_dictionary['12:30'] += 1
                    time_dictionary['13:00'] += 1
                    time_dictionary['13:30'] += 1

            elif logoff[0] == logon[0] + 3:
                if 30 > logoff[1] >= 0:
                    time_dictionary['11:30'] += 1
                    time_dictionary['12:00'] += 1
                    time_dictionary['12:30'] += 1
                    time_dictionary['13:00'] += 1
                    time_dictionary['13:30'] += 1
                    time_dictionary['14:00'] += 1

                elif 30 <= logoff[1] < 60:
                    time_dictionary['11:30'] += 1
                    time_dictionary['12:00'] += 1
                    time_dictionary['12:30'] += 1
                    time_dictionary['13:00'] += 1
                    time_dictionary['13:30'] += 1
                    time_dictionary['14:00'] += 1
                    time_dictionary['14:30'] += 1

            elif logoff[0] == logon[0] + 4:
                if 30 > logoff[1] >= 0:
                    time_dictionary['11:30'] += 1
                    time_dictionary['12:00'] += 1
                    time_dictionary['12:30'] += 1
                    time_dictionary['13:00'] += 1
                    time_dictionary['13:30'] += 1
                    time_dictionary['14:00'] += 1
                    time_dictionary['14:30'] += 1
                    time_dictionary['15:00'] += 1

                elif 30 <= logoff[1] < 60:
                    time_dictionary['11:30'] += 1
                    time_dictionary['12:00'] += 1
                    time_dictionary['12:30'] += 1
                    time_dictionary['13:00'] += 1
                    time_dictionary['13:30'] += 1
                    time_dictionary['14:00'] += 1
                    time_dictionary['14:30'] += 1
                    time_dictionary['15:00'] += 1
                    time_dictionary['15:30'] += 1

            elif logoff[0] == logon[0] + 5:
                if 30 > logoff[1] >= 0:
                    time_dictionary['11:30'] += 1
                    time_dictionary['12:00'] += 1
                    time_dictionary['12:30'] += 1
                    time_dictionary['13:00'] += 1
                    time_dictionary['13:30'] += 1
                    time_dictionary['14:00'] += 1
                    time_dictionary['14:30'] += 1
                    time_dictionary['15:00'] += 1
                    time_dictionary['15:30'] += 1
                    time_dictionary['16:00'] += 1

                elif 30 <= logoff[1] < 60:
                    time_dictionary['11:30'] += 1
                    time_dictionary['12:00'] += 1
                    time_dictionary['12:30'] += 1
                    time_dictionary['13:00'] += 1
                    time_dictionary['13:30'] += 1
                    time_dictionary['14:00'] += 1
                    time_dictionary['14:30'] += 1
                    time_dictionary['15:00'] += 1
                    time_dictionary['15:30'] += 1
                    time_dictionary['16:00'] += 1
                    time_dictionary['16:30'] += 1

            elif logoff[0] == logon[0] + 6:
                if 30 > logoff[1] >= 0:
                    time_dictionary['11:30'] += 1
                    time_dictionary['12:00'] += 1
                    time_dictionary['12:30'] += 1
                    time_dictionary['13:00'] += 1
                    time_dictionary['13:30'] += 1
                    time_dictionary['14:00'] += 1
                    time_dictionary['14:30'] += 1
                    time_dictionary['15:00'] += 1
                    time_dictionary['15:30'] += 1
                    time_dictionary['16:00'] += 1
                    time_dictionary['16:30'] += 1
                    time_dictionary['17:00'] += 1

                elif 30 <= logoff[1] < 60:
                    time_dictionary['11:30'] += 1
                    time_dictionary['12:00'] += 1
                    time_dictionary['12:30'] += 1
                    time_dictionary['13:00'] += 1
                    time_dictionary['13:30'] += 1
                    time_dictionary['14:00'] += 1
                    time_dictionary['14:30'] += 1
                    time_dictionary['15:00'] += 1
                    time_dictionary['15:30'] += 1
                    time_dictionary['16:00'] += 1
                    time_dictionary['16:30'] += 1
                    time_dictionary['17:00'] += 1
                    time_dictionary['17:30'] += 1

            elif logoff[0] == logon[0] + 7:
                if 30 > logoff[1] >= 0:
                    time_dictionary['11:30'] += 1
                    time_dictionary['12:00'] += 1
                    time_dictionary['12:30'] += 1
                    time_dictionary['13:00'] += 1
                    time_dictionary['13:30'] += 1
                    time_dictionary['14:00'] += 1
                    time_dictionary['14:30'] += 1
                    time_dictionary['15:00'] += 1
                    time_dictionary['15:30'] += 1
                    time_dictionary['16:00'] += 1
                    time_dictionary['16:30'] += 1
                    time_dictionary['17:00'] += 1
                    time_dictionary['17:30'] += 1
                    time_dictionary['18:00'] += 1

                elif 30 <= logoff[1] < 60:
                    time_dictionary['11:30'] += 1
                    time_dictionary['12:00'] += 1
                    time_dictionary['12:30'] += 1
                    time_dictionary['13:00'] += 1
                    time_dictionary['13:30'] += 1
                    time_dictionary['14:00'] += 1
                    time_dictionary['14:30'] += 1
                    time_dictionary['15:00'] += 1
                    time_dictionary['15:30'] += 1
                    time_dictionary['16:00'] += 1
                    time_dictionary['16:30'] += 1
                    time_dictionary['17:00'] += 1
                    time_dictionary['17:30'] += 1
                    time_dictionary['18:00'] += 1
                    time_dictionary['18:30'] += 1

            elif logoff[0] == logon[0] + 8:
                if 30 > logoff[1] >= 0:
                    time_dictionary['11:30'] += 1
                    time_dictionary['12:00'] += 1
                    time_dictionary['12:30'] += 1
                    time_dictionary['13:00'] += 1
                    time_dictionary['13:30'] += 1
                    time_dictionary['14:00'] += 1
                    time_dictionary['14:30'] += 1
                    time_dictionary['15:00'] += 1
                    time_dictionary['15:30'] += 1
                    time_dictionary['16:00'] += 1
                    time_dictionary['16:30'] += 1
                    time_dictionary['17:00'] += 1
                    time_dictionary['17:30'] += 1
                    time_dictionary['18:00'] += 1
                    time_dictionary['18:30'] += 1
                    time_dictionary['19:00'] += 1

                elif 30 <= logoff[1] < 60:
                    time_dictionary['11:30'] += 1
                    time_dictionary['12:00'] += 1
                    time_dictionary['12:30'] += 1
                    time_dictionary['13:00'] += 1
                    time_dictionary['13:30'] += 1
                    time_dictionary['14:00'] += 1
                    time_dictionary['14:30'] += 1
                    time_dictionary['15:00'] += 1
                    time_dictionary['15:30'] += 1
                    time_dictionary['16:00'] += 1
                    time_dictionary['16:30'] += 1
                    time_dictionary['17:00'] += 1
                    time_dictionary['17:30'] += 1
                    time_dictionary['18:00'] += 1
                    time_dictionary['18:30'] += 1
                    time_dictionary['19:00'] += 1
                    time_dictionary['19:30'] += 1

            elif logoff[0] == logon[0] + 9:
                if 30 > logoff[1] >= 0:
                    time_dictionary['11:30'] += 1
                    time_dictionary['12:00'] += 1
                    time_dictionary['12:30'] += 1
                    time_dictionary['13:00'] += 1
                    time_dictionary['13:30'] += 1
                    time_dictionary['14:00'] += 1
                    time_dictionary['14:30'] += 1
                    time_dictionary['15:00'] += 1
                    time_dictionary['15:30'] += 1
                    time_dictionary['16:00'] += 1
                    time_dictionary['16:30'] += 1
                    time_dictionary['17:00'] += 1
                    time_dictionary['17:30'] += 1
                    time_dictionary['18:00'] += 1
                    time_dictionary['18:30'] += 1
                    time_dictionary['19:00'] += 1
                    time_dictionary['19:30'] += 1
                    time_dictionary['20:00'] += 1

                elif 30 <= logoff[1] < 60:
                    time_dictionary['11:30'] += 1
                    time_dictionary['12:00'] += 1
                    time_dictionary['12:30'] += 1
                    time_dictionary['13:00'] += 1
                    time_dictionary['13:30'] += 1
                    time_dictionary['14:00'] += 1
                    time_dictionary['14:30'] += 1
                    time_dictionary['15:00'] += 1
                    time_dictionary['15:30'] += 1
                    time_dictionary['16:00'] += 1
                    time_dictionary['16:30'] += 1
                    time_dictionary['17:00'] += 1
                    time_dictionary['17:30'] += 1
                    time_dictionary['18:00'] += 1
                    time_dictionary['18:30'] += 1
                    time_dictionary['19:00'] += 1
                    time_dictionary['19:30'] += 1
                    time_dictionary['20:00'] += 1
                    time_dictionary['20:30'] += 1

            elif logoff[0] == logon[0] + 10:
                if 30 > logoff[1] >= 0:
                    time_dictionary['11:30'] += 1
                    time_dictionary['12:00'] += 1
                    time_dictionary['12:30'] += 1
                    time_dictionary['13:00'] += 1
                    time_dictionary['13:30'] += 1
                    time_dictionary['14:00'] += 1
                    time_dictionary['14:30'] += 1
                    time_dictionary['15:00'] += 1
                    time_dictionary['15:30'] += 1
                    time_dictionary['16:00'] += 1
                    time_dictionary['16:30'] += 1
                    time_dictionary['17:00'] += 1
                    time_dictionary['17:30'] += 1
                    time_dictionary['18:00'] += 1
                    time_dictionary['18:30'] += 1
                    time_dictionary['19:00'] += 1
                    time_dictionary['19:30'] += 1
                    time_dictionary['20:00'] += 1
                    time_dictionary['20:30'] += 1
                    time_dictionary['21:00'] += 1

                elif 30 <= logoff[1] < 60:
                    time_dictionary['11:30'] += 1
                    time_dictionary['12:00'] += 1
                    time_dictionary['12:30'] += 1
                    time_dictionary['13:00'] += 1
                    time_dictionary['13:30'] += 1
                    time_dictionary['14:00'] += 1
                    time_dictionary['14:30'] += 1
                    time_dictionary['15:00'] += 1
                    time_dictionary['15:30'] += 1
                    time_dictionary['16:00'] += 1
                    time_dictionary['16:30'] += 1
                    time_dictionary['17:00'] += 1
                    time_dictionary['17:30'] += 1
                    time_dictionary['18:00'] += 1
                    time_dictionary['18:30'] += 1
                    time_dictionary['19:00'] += 1
                    time_dictionary['19:30'] += 1
                    time_dictionary['20:00'] += 1
                    time_dictionary['20:30'] += 1
                    time_dictionary['21:00'] += 1
                    time_dictionary['21:30'] += 1

        elif logon[0] == 11 and 30 <= logon[1] < 60:
            time_dictionary['11:30'] += 1

            if logoff[0] == logon[0] + 1:
                if 30 > logoff[1] >= 0:
                    time_dictionary['12:00'] += 1

                elif 30 <= logon[1] < 60:
                    time_dictionary['12:00'] += 1
                    time_dictionary['12:30'] += 1

            if logoff[0] == logon[0] + 2:
                if 30 > logoff[1] >= 0:
                    time_dictionary['12:00'] += 1
                    time_dictionary['12:30'] += 1
                    time_dictionary['13:00'] += 1

                elif 30 <= logon[1] < 60:
                    time_dictionary['12:00'] += 1
                    time_dictionary['12:30'] += 1
                    time_dictionary['13:00'] += 1
                    time_dictionary['13:30'] += 1

            if logoff[0] == logon[0] + 3:
                if 30 > logoff[1] >= 0:
                    time_dictionary['12:00'] += 1
                    time_dictionary['12:30'] += 1
                    time_dictionary['13:00'] += 1
                    time_dictionary['13:30'] += 1
                    time_dictionary['14:00'] += 1

                elif 30 <= logon[1] < 60:
                    time_dictionary['12:00'] += 1
                    time_dictionary['12:30'] += 1
                    time_dictionary['13:00'] += 1
                    time_dictionary['13:30'] += 1
                    time_dictionary['14:00'] += 1
                    time_dictionary['14:30'] += 1

            if logoff[0] == logon[0] + 4:
                if 30 > logoff[1] >= 0:
                    time_dictionary['12:00'] += 1
                    time_dictionary['12:30'] += 1
                    time_dictionary['13:00'] += 1
                    time_dictionary['13:30'] += 1
                    time_dictionary['14:00'] += 1
                    time_dictionary['14:30'] += 1
                    time_dictionary['15:00'] += 1

                elif 30 <= logon[1] < 60:
                    time_dictionary['12:00'] += 1
                    time_dictionary['12:30'] += 1
                    time_dictionary['13:00'] += 1
                    time_dictionary['13:30'] += 1
                    time_dictionary['14:00'] += 1
                    time_dictionary['14:30'] += 1
                    time_dictionary['15:00'] += 1
                    time_dictionary['15:30'] += 1

            if logoff[0] == logon[0] + 5:
                if 30 > logoff[1] >= 0:
                    time_dictionary['12:00'] += 1
                    time_dictionary['12:30'] += 1
                    time_dictionary['13:00'] += 1
                    time_dictionary['13:30'] += 1
                    time_dictionary['14:00'] += 1
                    time_dictionary['14:30'] += 1
                    time_dictionary['15:00'] += 1
                    time_dictionary['15:30'] += 1
                    time_dictionary['16:00'] += 1

                elif 30 <= logon[1] < 60:
                    time_dictionary['12:00'] += 1
                    time_dictionary['12:30'] += 1
                    time_dictionary['13:00'] += 1
                    time_dictionary['13:30'] += 1
                    time_dictionary['14:00'] += 1
                    time_dictionary['14:30'] += 1
                    time_dictionary['15:00'] += 1
                    time_dictionary['15:30'] += 1
                    time_dictionary['16:00'] += 1
                    time_dictionary['16:30'] += 1

            if logoff[0] == logon[0] + 6:
                if 30 > logoff[1] >= 0:
                    time_dictionary['12:00'] += 1
                    time_dictionary['12:30'] += 1
                    time_dictionary['13:00'] += 1
                    time_dictionary['13:30'] += 1
                    time_dictionary['14:00'] += 1
                    time_dictionary['14:30'] += 1
                    time_dictionary['15:00'] += 1
                    time_dictionary['15:30'] += 1
                    time_dictionary['16:00'] += 1
                    time_dictionary['16:30'] += 1
                    time_dictionary['17:00'] += 1

                elif 30 <= logon[1] < 60:
                    time_dictionary['12:00'] += 1
                    time_dictionary['12:30'] += 1
                    time_dictionary['13:00'] += 1
                    time_dictionary['13:30'] += 1
                    time_dictionary['14:00'] += 1
                    time_dictionary['14:30'] += 1
                    time_dictionary['15:00'] += 1
                    time_dictionary['15:30'] += 1
                    time_dictionary['16:00'] += 1
                    time_dictionary['16:30'] += 1
                    time_dictionary['17:00'] += 1
                    time_dictionary['17:30'] += 1

            if logoff[0] == logon[0] + 7:
                if 30 > logoff[1] >= 0:
                    time_dictionary['12:00'] += 1
                    time_dictionary['12:30'] += 1
                    time_dictionary['13:00'] += 1
                    time_dictionary['13:30'] += 1
                    time_dictionary['14:00'] += 1
                    time_dictionary['14:30'] += 1
                    time_dictionary['15:00'] += 1
                    time_dictionary['15:30'] += 1
                    time_dictionary['16:00'] += 1
                    time_dictionary['16:30'] += 1
                    time_dictionary['17:00'] += 1
                    time_dictionary['17:30'] += 1
                    time_dictionary['18:00'] += 1

                elif 30 <= logon[1] < 60:
                    time_dictionary['12:00'] += 1
                    time_dictionary['12:30'] += 1
                    time_dictionary['13:00'] += 1
                    time_dictionary['13:30'] += 1
                    time_dictionary['14:00'] += 1
                    time_dictionary['14:30'] += 1
                    time_dictionary['15:00'] += 1
                    time_dictionary['15:30'] += 1
                    time_dictionary['16:00'] += 1
                    time_dictionary['16:30'] += 1
                    time_dictionary['17:00'] += 1
                    time_dictionary['17:30'] += 1
                    time_dictionary['18:00'] += 1
                    time_dictionary['18:30'] += 1

            if logoff[0] == logon[0] + 8:
                if 30 > logoff[1] >= 0:
                    time_dictionary['12:00'] += 1
                    time_dictionary['12:30'] += 1
                    time_dictionary['13:00'] += 1
                    time_dictionary['13:30'] += 1
                    time_dictionary['14:00'] += 1
                    time_dictionary['14:30'] += 1
                    time_dictionary['15:00'] += 1
                    time_dictionary['15:30'] += 1
                    time_dictionary['16:00'] += 1
                    time_dictionary['16:30'] += 1
                    time_dictionary['17:00'] += 1
                    time_dictionary['17:30'] += 1
                    time_dictionary['18:00'] += 1
                    time_dictionary['18:30'] += 1
                    time_dictionary['19:00'] += 1

                elif 30 <= logon[1] < 60:
                    time_dictionary['12:00'] += 1
                    time_dictionary['12:30'] += 1
                    time_dictionary['13:00'] += 1
                    time_dictionary['13:30'] += 1
                    time_dictionary['14:00'] += 1
                    time_dictionary['14:30'] += 1
                    time_dictionary['15:00'] += 1
                    time_dictionary['15:30'] += 1
                    time_dictionary['16:00'] += 1
                    time_dictionary['16:30'] += 1
                    time_dictionary['17:00'] += 1
                    time_dictionary['17:30'] += 1
                    time_dictionary['18:00'] += 1
                    time_dictionary['18:30'] += 1
                    time_dictionary['19:00'] += 1
                    time_dictionary['19:30'] += 1

            if logoff[0] == logon[0] + 9:
                if 30 > logoff[1] >= 0:
                    time_dictionary['12:00'] += 1
                    time_dictionary['12:30'] += 1
                    time_dictionary['13:00'] += 1
                    time_dictionary['13:30'] += 1
                    time_dictionary['14:00'] += 1
                    time_dictionary['14:30'] += 1
                    time_dictionary['15:00'] += 1
                    time_dictionary['15:30'] += 1
                    time_dictionary['16:00'] += 1
                    time_dictionary['16:30'] += 1
                    time_dictionary['17:00'] += 1
                    time_dictionary['17:30'] += 1
                    time_dictionary['18:00'] += 1
                    time_dictionary['18:30'] += 1
                    time_dictionary['19:00'] += 1
                    time_dictionary['19:30'] += 1
                    time_dictionary['20:00'] += 1

                elif 30 <= logon[1] < 60:
                    time_dictionary['12:00'] += 1
                    time_dictionary['12:30'] += 1
                    time_dictionary['13:00'] += 1
                    time_dictionary['13:30'] += 1
                    time_dictionary['14:00'] += 1
                    time_dictionary['14:30'] += 1
                    time_dictionary['15:00'] += 1
                    time_dictionary['15:30'] += 1
                    time_dictionary['16:00'] += 1
                    time_dictionary['16:30'] += 1
                    time_dictionary['17:00'] += 1
                    time_dictionary['17:30'] += 1
                    time_dictionary['18:00'] += 1
                    time_dictionary['18:30'] += 1
                    time_dictionary['19:00'] += 1
                    time_dictionary['19:30'] += 1
                    time_dictionary['20:00'] += 1
                    time_dictionary['20:30'] += 1

            if logoff[0] == logon[0] + 10:
                if 30 > logoff[1] >= 0:
                    time_dictionary['12:00'] += 1
                    time_dictionary['12:30'] += 1
                    time_dictionary['13:00'] += 1
                    time_dictionary['13:30'] += 1
                    time_dictionary['14:00'] += 1
                    time_dictionary['14:30'] += 1
                    time_dictionary['15:00'] += 1
                    time_dictionary['15:30'] += 1
                    time_dictionary['16:00'] += 1
                    time_dictionary['16:30'] += 1
                    time_dictionary['17:00'] += 1
                    time_dictionary['17:30'] += 1
                    time_dictionary['18:00'] += 1
                    time_dictionary['18:30'] += 1
                    time_dictionary['19:00'] += 1
                    time_dictionary['19:30'] += 1
                    time_dictionary['20:00'] += 1
                    time_dictionary['20:30'] += 1
                    time_dictionary['21:00'] += 1

                elif 30 <= logon[1] < 60:
                    time_dictionary['12:00'] += 1
                    time_dictionary['12:30'] += 1
                    time_dictionary['13:00'] += 1
                    time_dictionary['13:30'] += 1
                    time_dictionary['14:00'] += 1
                    time_dictionary['14:30'] += 1
                    time_dictionary['15:00'] += 1
                    time_dictionary['15:30'] += 1
                    time_dictionary['16:00'] += 1
                    time_dictionary['16:30'] += 1
                    time_dictionary['17:00'] += 1
                    time_dictionary['17:30'] += 1
                    time_dictionary['18:00'] += 1
                    time_dictionary['18:30'] += 1
                    time_dictionary['19:00'] += 1
                    time_dictionary['19:30'] += 1
                    time_dictionary['20:00'] += 1
                    time_dictionary['20:30'] += 1
                    time_dictionary['21:00'] += 1
                    time_dictionary['21:30'] += 1

        elif logon[0] == 12 and 30 > logon[1] >= 0:
            time_dictionary['12:00'] += 1

            if logoff[0] == logon[0]:
                if 30 <= logoff[1] < 60:
                    time_dictionary['12:30'] += 1

            elif logoff[0] == logon[0] + 1:
                if 30 > logoff[1] >= 0:
                    time_dictionary['12:30'] += 1
                    time_dictionary['13:00'] += 1

                elif 30 <= logoff[1] < 60:
                    time_dictionary['12:30'] += 1
                    time_dictionary['13:00'] += 1
                    time_dictionary['13:30'] += 1

            elif logoff[0] == logon[0] + 2:
                if 30 > logoff[1] >= 0:
                    time_dictionary['12:30'] += 1
                    time_dictionary['13:00'] += 1
                    time_dictionary['13:30'] += 1
                    time_dictionary['14:00'] += 1

                elif 30 <= logoff[1] < 60:
                    time_dictionary['12:30'] += 1
                    time_dictionary['13:00'] += 1
                    time_dictionary['13:30'] += 1
                    time_dictionary['14:00'] += 1
                    time_dictionary['14:30'] += 1

            elif logoff[0] == logon[0] + 3:
                if 30 > logoff[1] >= 0:
                    time_dictionary['12:30'] += 1
                    time_dictionary['13:00'] += 1
                    time_dictionary['13:30'] += 1
                    time_dictionary['14:00'] += 1
                    time_dictionary['14:30'] += 1
                    time_dictionary['15:00'] += 1

                elif 30 <= logoff[1] < 60:
                    time_dictionary['12:30'] += 1
                    time_dictionary['13:00'] += 1
                    time_dictionary['13:30'] += 1
                    time_dictionary['14:00'] += 1
                    time_dictionary['14:30'] += 1
                    time_dictionary['15:00'] += 1
                    time_dictionary['15:30'] += 1

            elif logoff[0] == logon[0] + 4:
                if 30 > logoff[1] >= 0:
                    time_dictionary['12:30'] += 1
                    time_dictionary['13:00'] += 1
                    time_dictionary['13:30'] += 1
                    time_dictionary['14:00'] += 1
                    time_dictionary['14:30'] += 1
                    time_dictionary['15:00'] += 1
                    time_dictionary['15:30'] += 1
                    time_dictionary['16:00'] += 1

                elif 30 <= logoff[1] < 60:
                    time_dictionary['12:30'] += 1
                    time_dictionary['13:00'] += 1
                    time_dictionary['13:30'] += 1
                    time_dictionary['14:00'] += 1
                    time_dictionary['14:30'] += 1
                    time_dictionary['15:00'] += 1
                    time_dictionary['15:30'] += 1
                    time_dictionary['16:00'] += 1
                    time_dictionary['16:30'] += 1

            elif logoff[0] == logon[0] + 5:
                if 30 > logoff[1] >= 0:
                    time_dictionary['12:30'] += 1
                    time_dictionary['13:00'] += 1
                    time_dictionary['13:30'] += 1
                    time_dictionary['14:00'] += 1
                    time_dictionary['14:30'] += 1
                    time_dictionary['15:00'] += 1
                    time_dictionary['15:30'] += 1
                    time_dictionary['16:00'] += 1
                    time_dictionary['16:30'] += 1
                    time_dictionary['17:00'] += 1

                elif 30 <= logoff[1] < 60:
                    time_dictionary['12:30'] += 1
                    time_dictionary['13:00'] += 1
                    time_dictionary['13:30'] += 1
                    time_dictionary['14:00'] += 1
                    time_dictionary['14:30'] += 1
                    time_dictionary['15:00'] += 1
                    time_dictionary['15:30'] += 1
                    time_dictionary['16:00'] += 1
                    time_dictionary['16:30'] += 1
                    time_dictionary['17:00'] += 1
                    time_dictionary['17:30'] += 1

            elif logoff[0] == logon[0] + 6:
                if 30 > logoff[1] >= 0:
                    time_dictionary['12:30'] += 1
                    time_dictionary['13:00'] += 1
                    time_dictionary['13:30'] += 1
                    time_dictionary['14:00'] += 1
                    time_dictionary['14:30'] += 1
                    time_dictionary['15:00'] += 1
                    time_dictionary['15:30'] += 1
                    time_dictionary['16:00'] += 1
                    time_dictionary['16:30'] += 1
                    time_dictionary['17:00'] += 1
                    time_dictionary['17:30'] += 1
                    time_dictionary['18:00'] += 1

                elif 30 <= logoff[1] < 60:
                    time_dictionary['12:30'] += 1
                    time_dictionary['13:00'] += 1
                    time_dictionary['13:30'] += 1
                    time_dictionary['14:00'] += 1
                    time_dictionary['14:30'] += 1
                    time_dictionary['15:00'] += 1
                    time_dictionary['15:30'] += 1
                    time_dictionary['16:00'] += 1
                    time_dictionary['16:30'] += 1
                    time_dictionary['17:00'] += 1
                    time_dictionary['17:30'] += 1
                    time_dictionary['18:00'] += 1
                    time_dictionary['18:30'] += 1

            elif logoff[0] == logon[0] + 7:
                if 30 > logoff[1] >= 0:
                    time_dictionary['12:30'] += 1
                    time_dictionary['13:00'] += 1
                    time_dictionary['13:30'] += 1
                    time_dictionary['14:00'] += 1
                    time_dictionary['14:30'] += 1
                    time_dictionary['15:00'] += 1
                    time_dictionary['15:30'] += 1
                    time_dictionary['16:00'] += 1
                    time_dictionary['16:30'] += 1
                    time_dictionary['17:00'] += 1
                    time_dictionary['17:30'] += 1
                    time_dictionary['18:00'] += 1
                    time_dictionary['18:30'] += 1
                    time_dictionary['19:00'] += 1

                elif 30 <= logoff[1] < 60:
                    time_dictionary['12:30'] += 1
                    time_dictionary['13:00'] += 1
                    time_dictionary['13:30'] += 1
                    time_dictionary['14:00'] += 1
                    time_dictionary['14:30'] += 1
                    time_dictionary['15:00'] += 1
                    time_dictionary['15:30'] += 1
                    time_dictionary['16:00'] += 1
                    time_dictionary['16:30'] += 1
                    time_dictionary['17:00'] += 1
                    time_dictionary['17:30'] += 1
                    time_dictionary['18:00'] += 1
                    time_dictionary['18:30'] += 1
                    time_dictionary['19:00'] += 1
                    time_dictionary['19:30'] += 1

            elif logoff[0] == logon[0] + 8:
                if 30 > logoff[1] >= 0:
                    time_dictionary['12:30'] += 1
                    time_dictionary['13:00'] += 1
                    time_dictionary['13:30'] += 1
                    time_dictionary['14:00'] += 1
                    time_dictionary['14:30'] += 1
                    time_dictionary['15:00'] += 1
                    time_dictionary['15:30'] += 1
                    time_dictionary['16:00'] += 1
                    time_dictionary['16:30'] += 1
                    time_dictionary['17:00'] += 1
                    time_dictionary['17:30'] += 1
                    time_dictionary['18:00'] += 1
                    time_dictionary['18:30'] += 1
                    time_dictionary['19:00'] += 1
                    time_dictionary['19:30'] += 1
                    time_dictionary['20:00'] += 1

                elif 30 <= logoff[1] < 60:
                    time_dictionary['12:30'] += 1
                    time_dictionary['13:00'] += 1
                    time_dictionary['13:30'] += 1
                    time_dictionary['14:00'] += 1
                    time_dictionary['14:30'] += 1
                    time_dictionary['15:00'] += 1
                    time_dictionary['15:30'] += 1
                    time_dictionary['16:00'] += 1
                    time_dictionary['16:30'] += 1
                    time_dictionary['17:00'] += 1
                    time_dictionary['17:30'] += 1
                    time_dictionary['18:00'] += 1
                    time_dictionary['18:30'] += 1
                    time_dictionary['19:00'] += 1
                    time_dictionary['19:30'] += 1
                    time_dictionary['20:00'] += 1
                    time_dictionary['20:30'] += 1

            elif logoff[0] == logon[0] + 9:
                if 30 > logoff[1] >= 0:
                    time_dictionary['12:30'] += 1
                    time_dictionary['13:00'] += 1
                    time_dictionary['13:30'] += 1
                    time_dictionary['14:00'] += 1
                    time_dictionary['14:30'] += 1
                    time_dictionary['15:00'] += 1
                    time_dictionary['15:30'] += 1
                    time_dictionary['16:00'] += 1
                    time_dictionary['16:30'] += 1
                    time_dictionary['17:00'] += 1
                    time_dictionary['17:30'] += 1
                    time_dictionary['18:00'] += 1
                    time_dictionary['18:30'] += 1
                    time_dictionary['19:00'] += 1
                    time_dictionary['19:30'] += 1
                    time_dictionary['20:00'] += 1
                    time_dictionary['20:30'] += 1
                    time_dictionary['21:00'] += 1

                elif 30 <= logoff[1] < 60:
                    time_dictionary['12:30'] += 1
                    time_dictionary['13:00'] += 1
                    time_dictionary['13:30'] += 1
                    time_dictionary['14:00'] += 1
                    time_dictionary['14:30'] += 1
                    time_dictionary['15:00'] += 1
                    time_dictionary['15:30'] += 1
                    time_dictionary['16:00'] += 1
                    time_dictionary['16:30'] += 1
                    time_dictionary['17:00'] += 1
                    time_dictionary['17:30'] += 1
                    time_dictionary['18:00'] += 1
                    time_dictionary['18:30'] += 1
                    time_dictionary['19:00'] += 1
                    time_dictionary['19:30'] += 1
                    time_dictionary['20:00'] += 1
                    time_dictionary['20:30'] += 1
                    time_dictionary['21:00'] += 1
                    time_dictionary['21:30'] += 1

        elif logon[0] == 12 and 30 <= logon[1] < 60:
            time_dictionary['12:30'] += 1

            if logoff[0] == logon[0] + 1:
                if 30 > logoff[1] >= 0:
                    time_dictionary['13:00'] += 1

                elif 30 <= logon[1] < 60:
                    time_dictionary['13:00'] += 1
                    time_dictionary['13:30'] += 1

            if logoff[0] == logon[0] + 2:
                if 30 > logoff[1] >= 0:
                    time_dictionary['13:00'] += 1
                    time_dictionary['13:30'] += 1
                    time_dictionary['14:00'] += 1

                elif 30 <= logon[1] < 60:
                    time_dictionary['13:00'] += 1
                    time_dictionary['13:30'] += 1
                    time_dictionary['14:00'] += 1
                    time_dictionary['14:30'] += 1

            if logoff[0] == logon[0] + 3:
                if 30 > logoff[1] >= 0:
                    time_dictionary['13:00'] += 1
                    time_dictionary['13:30'] += 1
                    time_dictionary['14:00'] += 1
                    time_dictionary['14:30'] += 1
                    time_dictionary['15:00'] += 1

                elif 30 <= logon[1] < 60:
                    time_dictionary['13:00'] += 1
                    time_dictionary['13:30'] += 1
                    time_dictionary['14:00'] += 1
                    time_dictionary['14:30'] += 1
                    time_dictionary['15:00'] += 1
                    time_dictionary['15:30'] += 1

            if logoff[0] == logon[0] + 4:
                if 30 > logoff[1] >= 0:
                    time_dictionary['13:00'] += 1
                    time_dictionary['13:30'] += 1
                    time_dictionary['14:00'] += 1
                    time_dictionary['14:30'] += 1
                    time_dictionary['15:00'] += 1
                    time_dictionary['15:30'] += 1
                    time_dictionary['16:00'] += 1

                elif 30 <= logon[1] < 60:
                    time_dictionary['13:00'] += 1
                    time_dictionary['13:30'] += 1
                    time_dictionary['14:00'] += 1
                    time_dictionary['14:30'] += 1
                    time_dictionary['15:00'] += 1
                    time_dictionary['15:30'] += 1
                    time_dictionary['16:00'] += 1
                    time_dictionary['16:30'] += 1

            if logoff[0] == logon[0] + 5:
                if 30 > logoff[1] >= 0:
                    time_dictionary['13:00'] += 1
                    time_dictionary['13:30'] += 1
                    time_dictionary['14:00'] += 1
                    time_dictionary['14:30'] += 1
                    time_dictionary['15:00'] += 1
                    time_dictionary['15:30'] += 1
                    time_dictionary['16:00'] += 1
                    time_dictionary['16:30'] += 1
                    time_dictionary['17:00'] += 1

                elif 30 <= logon[1] < 60:
                    time_dictionary['13:00'] += 1
                    time_dictionary['13:30'] += 1
                    time_dictionary['14:00'] += 1
                    time_dictionary['14:30'] += 1
                    time_dictionary['15:00'] += 1
                    time_dictionary['15:30'] += 1
                    time_dictionary['16:00'] += 1
                    time_dictionary['16:30'] += 1
                    time_dictionary['17:00'] += 1
                    time_dictionary['17:30'] += 1

            if logoff[0] == logon[0] + 6:
                if 30 > logoff[1] >= 0:
                    time_dictionary['13:00'] += 1
                    time_dictionary['13:30'] += 1
                    time_dictionary['14:00'] += 1
                    time_dictionary['14:30'] += 1
                    time_dictionary['15:00'] += 1
                    time_dictionary['15:30'] += 1
                    time_dictionary['16:00'] += 1
                    time_dictionary['16:30'] += 1
                    time_dictionary['17:00'] += 1
                    time_dictionary['17:30'] += 1
                    time_dictionary['18:00'] += 1

                elif 30 <= logon[1] < 60:
                    time_dictionary['13:00'] += 1
                    time_dictionary['13:30'] += 1
                    time_dictionary['14:00'] += 1
                    time_dictionary['14:30'] += 1
                    time_dictionary['15:00'] += 1
                    time_dictionary['15:30'] += 1
                    time_dictionary['16:00'] += 1
                    time_dictionary['16:30'] += 1
                    time_dictionary['17:00'] += 1
                    time_dictionary['17:30'] += 1
                    time_dictionary['18:00'] += 1
                    time_dictionary['18:30'] += 1

            if logoff[0] == logon[0] + 7:
                if 30 > logoff[1] >= 0:
                    time_dictionary['13:00'] += 1
                    time_dictionary['13:30'] += 1
                    time_dictionary['14:00'] += 1
                    time_dictionary['14:30'] += 1
                    time_dictionary['15:00'] += 1
                    time_dictionary['15:30'] += 1
                    time_dictionary['16:00'] += 1
                    time_dictionary['16:30'] += 1
                    time_dictionary['17:00'] += 1
                    time_dictionary['17:30'] += 1
                    time_dictionary['18:00'] += 1
                    time_dictionary['18:30'] += 1
                    time_dictionary['19:00'] += 1

                elif 30 <= logon[1] < 60:
                    time_dictionary['13:00'] += 1
                    time_dictionary['13:30'] += 1
                    time_dictionary['14:00'] += 1
                    time_dictionary['14:30'] += 1
                    time_dictionary['15:00'] += 1
                    time_dictionary['15:30'] += 1
                    time_dictionary['16:00'] += 1
                    time_dictionary['16:30'] += 1
                    time_dictionary['17:00'] += 1
                    time_dictionary['17:30'] += 1
                    time_dictionary['18:00'] += 1
                    time_dictionary['18:30'] += 1
                    time_dictionary['19:00'] += 1
                    time_dictionary['19:30'] += 1

            if logoff[0] == logon[0] + 8:
                if 30 > logoff[1] >= 0:
                    time_dictionary['13:00'] += 1
                    time_dictionary['13:30'] += 1
                    time_dictionary['14:00'] += 1
                    time_dictionary['14:30'] += 1
                    time_dictionary['15:00'] += 1
                    time_dictionary['15:30'] += 1
                    time_dictionary['16:00'] += 1
                    time_dictionary['16:30'] += 1
                    time_dictionary['17:00'] += 1
                    time_dictionary['17:30'] += 1
                    time_dictionary['18:00'] += 1
                    time_dictionary['18:30'] += 1
                    time_dictionary['19:00'] += 1
                    time_dictionary['19:30'] += 1
                    time_dictionary['20:00'] += 1

                elif 30 <= logon[1] < 60:
                    time_dictionary['13:00'] += 1
                    time_dictionary['13:30'] += 1
                    time_dictionary['14:00'] += 1
                    time_dictionary['14:30'] += 1
                    time_dictionary['15:00'] += 1
                    time_dictionary['15:30'] += 1
                    time_dictionary['16:00'] += 1
                    time_dictionary['16:30'] += 1
                    time_dictionary['17:00'] += 1
                    time_dictionary['17:30'] += 1
                    time_dictionary['18:00'] += 1
                    time_dictionary['18:30'] += 1
                    time_dictionary['19:00'] += 1
                    time_dictionary['19:30'] += 1
                    time_dictionary['20:00'] += 1
                    time_dictionary['20:30'] += 1

            if logoff[0] == logon[0] + 9:
                if 30 > logoff[1] >= 0:
                    time_dictionary['13:00'] += 1
                    time_dictionary['13:30'] += 1
                    time_dictionary['14:00'] += 1
                    time_dictionary['14:30'] += 1
                    time_dictionary['15:00'] += 1
                    time_dictionary['15:30'] += 1
                    time_dictionary['16:00'] += 1
                    time_dictionary['16:30'] += 1
                    time_dictionary['17:00'] += 1
                    time_dictionary['17:30'] += 1
                    time_dictionary['18:00'] += 1
                    time_dictionary['18:30'] += 1
                    time_dictionary['19:00'] += 1
                    time_dictionary['19:30'] += 1
                    time_dictionary['20:00'] += 1
                    time_dictionary['20:30'] += 1
                    time_dictionary['21:00'] += 1

                elif 30 <= logon[1] < 60:
                    time_dictionary['13:00'] += 1
                    time_dictionary['13:30'] += 1
                    time_dictionary['14:00'] += 1
                    time_dictionary['14:30'] += 1
                    time_dictionary['15:00'] += 1
                    time_dictionary['15:30'] += 1
                    time_dictionary['16:00'] += 1
                    time_dictionary['16:30'] += 1
                    time_dictionary['17:00'] += 1
                    time_dictionary['17:30'] += 1
                    time_dictionary['18:00'] += 1
                    time_dictionary['18:30'] += 1
                    time_dictionary['19:00'] += 1
                    time_dictionary['19:30'] += 1
                    time_dictionary['20:00'] += 1
                    time_dictionary['20:30'] += 1
                    time_dictionary['21:00'] += 1
                    time_dictionary['21:30'] += 1

        elif logon[0] == 13 and 30 > logon[1] >= 0:
            time_dictionary['13:00'] += 1

            if logoff[0] == logon[0]:
                if 30 <= logoff[1] < 60:
                    time_dictionary['13:30'] += 1

            elif logoff[0] == logon[0] + 1:
                if 30 > logoff[1] >= 0:
                    time_dictionary['13:30'] += 1
                    time_dictionary['14:00'] += 1

                elif 30 <= logoff[1] < 60:
                    time_dictionary['13:30'] += 1
                    time_dictionary['14:00'] += 1
                    time_dictionary['14:30'] += 1

            elif logoff[0] == logon[0] + 2:
                if 30 > logoff[1] >= 0:
                    time_dictionary['13:30'] += 1
                    time_dictionary['14:00'] += 1
                    time_dictionary['14:30'] += 1
                    time_dictionary['15:00'] += 1

                elif 30 <= logoff[1] < 60:
                    time_dictionary['13:30'] += 1
                    time_dictionary['14:00'] += 1
                    time_dictionary['14:30'] += 1
                    time_dictionary['15:00'] += 1
                    time_dictionary['15:30'] += 1

            elif logoff[0] == logon[0] + 3:
                if 30 > logoff[1] >= 0:
                    time_dictionary['13:30'] += 1
                    time_dictionary['14:00'] += 1
                    time_dictionary['14:30'] += 1
                    time_dictionary['15:00'] += 1
                    time_dictionary['15:30'] += 1
                    time_dictionary['16:00'] += 1

                elif 30 <= logoff[1] < 60:
                    time_dictionary['13:30'] += 1
                    time_dictionary['14:00'] += 1
                    time_dictionary['14:30'] += 1
                    time_dictionary['15:00'] += 1
                    time_dictionary['15:30'] += 1
                    time_dictionary['16:00'] += 1
                    time_dictionary['16:30'] += 1

            elif logoff[0] == logon[0] + 4:
                if 30 > logoff[1] >= 0:
                    time_dictionary['13:30'] += 1
                    time_dictionary['14:00'] += 1
                    time_dictionary['14:30'] += 1
                    time_dictionary['15:00'] += 1
                    time_dictionary['15:30'] += 1
                    time_dictionary['16:00'] += 1
                    time_dictionary['16:30'] += 1
                    time_dictionary['17:00'] += 1

                elif 30 <= logoff[1] < 60:
                    time_dictionary['13:30'] += 1
                    time_dictionary['14:00'] += 1
                    time_dictionary['14:30'] += 1
                    time_dictionary['15:00'] += 1
                    time_dictionary['15:30'] += 1
                    time_dictionary['16:00'] += 1
                    time_dictionary['16:30'] += 1
                    time_dictionary['17:00'] += 1
                    time_dictionary['17:30'] += 1

            elif logoff[0] == logon[0] + 5:
                if 30 > logoff[1] >= 0:
                    time_dictionary['13:30'] += 1
                    time_dictionary['14:00'] += 1
                    time_dictionary['14:30'] += 1
                    time_dictionary['15:00'] += 1
                    time_dictionary['15:30'] += 1
                    time_dictionary['16:00'] += 1
                    time_dictionary['16:30'] += 1
                    time_dictionary['17:00'] += 1
                    time_dictionary['17:30'] += 1
                    time_dictionary['18:00'] += 1

                elif 30 <= logoff[1] < 60:
                    time_dictionary['13:30'] += 1
                    time_dictionary['14:00'] += 1
                    time_dictionary['14:30'] += 1
                    time_dictionary['15:00'] += 1
                    time_dictionary['15:30'] += 1
                    time_dictionary['16:00'] += 1
                    time_dictionary['16:30'] += 1
                    time_dictionary['17:00'] += 1
                    time_dictionary['17:30'] += 1
                    time_dictionary['18:00'] += 1
                    time_dictionary['18:30'] += 1

            elif logoff[0] == logon[0] + 6:
                if 30 > logoff[1] >= 0:
                    time_dictionary['13:30'] += 1
                    time_dictionary['14:00'] += 1
                    time_dictionary['14:30'] += 1
                    time_dictionary['15:00'] += 1
                    time_dictionary['15:30'] += 1
                    time_dictionary['16:00'] += 1
                    time_dictionary['16:30'] += 1
                    time_dictionary['17:00'] += 1
                    time_dictionary['17:30'] += 1
                    time_dictionary['18:00'] += 1
                    time_dictionary['18:30'] += 1
                    time_dictionary['19:00'] += 1

                elif 30 <= logoff[1] < 60:
                    time_dictionary['13:30'] += 1
                    time_dictionary['14:00'] += 1
                    time_dictionary['14:30'] += 1
                    time_dictionary['15:00'] += 1
                    time_dictionary['15:30'] += 1
                    time_dictionary['16:00'] += 1
                    time_dictionary['16:30'] += 1
                    time_dictionary['17:00'] += 1
                    time_dictionary['17:30'] += 1
                    time_dictionary['18:00'] += 1
                    time_dictionary['18:30'] += 1
                    time_dictionary['19:00'] += 1
                    time_dictionary['19:30'] += 1

            elif logoff[0] == logon[0] + 7:
                if 30 > logoff[1] >= 0:
                    time_dictionary['13:30'] += 1
                    time_dictionary['14:00'] += 1
                    time_dictionary['14:30'] += 1
                    time_dictionary['15:00'] += 1
                    time_dictionary['15:30'] += 1
                    time_dictionary['16:00'] += 1
                    time_dictionary['16:30'] += 1
                    time_dictionary['17:00'] += 1
                    time_dictionary['17:30'] += 1
                    time_dictionary['18:00'] += 1
                    time_dictionary['18:30'] += 1
                    time_dictionary['19:00'] += 1
                    time_dictionary['19:30'] += 1
                    time_dictionary['20:00'] += 1

                elif 30 <= logoff[1] < 60:
                    time_dictionary['13:30'] += 1
                    time_dictionary['14:00'] += 1
                    time_dictionary['14:30'] += 1
                    time_dictionary['15:00'] += 1
                    time_dictionary['15:30'] += 1
                    time_dictionary['16:00'] += 1
                    time_dictionary['16:30'] += 1
                    time_dictionary['17:00'] += 1
                    time_dictionary['17:30'] += 1
                    time_dictionary['18:00'] += 1
                    time_dictionary['18:30'] += 1
                    time_dictionary['19:00'] += 1
                    time_dictionary['19:30'] += 1
                    time_dictionary['20:00'] += 1
                    time_dictionary['20:30'] += 1

            elif logoff[0] == logon[0] + 8:
                if 30 > logoff[1] >= 0:
                    time_dictionary['13:30'] += 1
                    time_dictionary['14:00'] += 1
                    time_dictionary['14:30'] += 1
                    time_dictionary['15:00'] += 1
                    time_dictionary['15:30'] += 1
                    time_dictionary['16:00'] += 1
                    time_dictionary['16:30'] += 1
                    time_dictionary['17:00'] += 1
                    time_dictionary['17:30'] += 1
                    time_dictionary['18:00'] += 1
                    time_dictionary['18:30'] += 1
                    time_dictionary['19:00'] += 1
                    time_dictionary['19:30'] += 1
                    time_dictionary['20:00'] += 1
                    time_dictionary['20:30'] += 1
                    time_dictionary['21:00'] += 1

                elif 30 <= logoff[1] < 60:
                    time_dictionary['13:30'] += 1
                    time_dictionary['14:00'] += 1
                    time_dictionary['14:30'] += 1
                    time_dictionary['15:00'] += 1
                    time_dictionary['15:30'] += 1
                    time_dictionary['16:00'] += 1
                    time_dictionary['16:30'] += 1
                    time_dictionary['17:00'] += 1
                    time_dictionary['17:30'] += 1
                    time_dictionary['18:00'] += 1
                    time_dictionary['18:30'] += 1
                    time_dictionary['19:00'] += 1
                    time_dictionary['19:30'] += 1
                    time_dictionary['20:00'] += 1
                    time_dictionary['20:30'] += 1
                    time_dictionary['21:00'] += 1
                    time_dictionary['21:30'] += 1

        elif logon[0] == 13 and 30 <= logon[1] < 60:
            time_dictionary['13:30'] += 1

            if logoff[0] == logon[0] + 1:
                if 30 > logoff[1] >= 0:
                    time_dictionary['14:00'] += 1

                elif 30 <= logon[1] < 60:
                    time_dictionary['14:00'] += 1
                    time_dictionary['14:30'] += 1

            if logoff[0] == logon[0] + 2:
                if 30 > logoff[1] >= 0:
                    time_dictionary['14:00'] += 1
                    time_dictionary['14:30'] += 1
                    time_dictionary['15:00'] += 1

                elif 30 <= logon[1] < 60:
                    time_dictionary['14:00'] += 1
                    time_dictionary['14:30'] += 1
                    time_dictionary['15:00'] += 1
                    time_dictionary['15:30'] += 1

            if logoff[0] == logon[0] + 3:
                if 30 > logoff[1] >= 0:
                    time_dictionary['14:00'] += 1
                    time_dictionary['14:30'] += 1
                    time_dictionary['15:00'] += 1
                    time_dictionary['15:30'] += 1
                    time_dictionary['16:00'] += 1

                elif 30 <= logon[1] < 60:
                    time_dictionary['14:00'] += 1
                    time_dictionary['14:30'] += 1
                    time_dictionary['15:00'] += 1
                    time_dictionary['15:30'] += 1
                    time_dictionary['16:00'] += 1
                    time_dictionary['16:30'] += 1

            if logoff[0] == logon[0] + 4:
                if 30 > logoff[1] >= 0:
                    time_dictionary['14:00'] += 1
                    time_dictionary['14:30'] += 1
                    time_dictionary['15:00'] += 1
                    time_dictionary['15:30'] += 1
                    time_dictionary['16:00'] += 1
                    time_dictionary['16:30'] += 1
                    time_dictionary['17:00'] += 1

                elif 30 <= logon[1] < 60:
                    time_dictionary['14:00'] += 1
                    time_dictionary['14:30'] += 1
                    time_dictionary['15:00'] += 1
                    time_dictionary['15:30'] += 1
                    time_dictionary['16:00'] += 1
                    time_dictionary['16:30'] += 1
                    time_dictionary['17:00'] += 1
                    time_dictionary['17:30'] += 1

            if logoff[0] == logon[0] + 5:
                if 30 > logoff[1] >= 0:
                    time_dictionary['14:00'] += 1
                    time_dictionary['14:30'] += 1
                    time_dictionary['15:00'] += 1
                    time_dictionary['15:30'] += 1
                    time_dictionary['16:00'] += 1
                    time_dictionary['16:30'] += 1
                    time_dictionary['17:00'] += 1
                    time_dictionary['17:30'] += 1
                    time_dictionary['18:00'] += 1

                elif 30 <= logon[1] < 60:
                    time_dictionary['14:00'] += 1
                    time_dictionary['14:30'] += 1
                    time_dictionary['15:00'] += 1
                    time_dictionary['15:30'] += 1
                    time_dictionary['16:00'] += 1
                    time_dictionary['16:30'] += 1
                    time_dictionary['17:00'] += 1
                    time_dictionary['17:30'] += 1
                    time_dictionary['18:00'] += 1
                    time_dictionary['18:30'] += 1

            if logoff[0] == logon[0] + 6:
                if 30 > logoff[1] >= 0:
                    time_dictionary['14:00'] += 1
                    time_dictionary['14:30'] += 1
                    time_dictionary['15:00'] += 1
                    time_dictionary['15:30'] += 1
                    time_dictionary['16:00'] += 1
                    time_dictionary['16:30'] += 1
                    time_dictionary['17:00'] += 1
                    time_dictionary['17:30'] += 1
                    time_dictionary['18:00'] += 1
                    time_dictionary['18:30'] += 1
                    time_dictionary['19:00'] += 1

                elif 30 <= logon[1] < 60:
                    time_dictionary['14:00'] += 1
                    time_dictionary['14:30'] += 1
                    time_dictionary['15:00'] += 1
                    time_dictionary['15:30'] += 1
                    time_dictionary['16:00'] += 1
                    time_dictionary['16:30'] += 1
                    time_dictionary['17:00'] += 1
                    time_dictionary['17:30'] += 1
                    time_dictionary['18:00'] += 1
                    time_dictionary['18:30'] += 1
                    time_dictionary['19:00'] += 1
                    time_dictionary['19:30'] += 1

            if logoff[0] == logon[0] + 7:
                if 30 > logoff[1] >= 0:
                    time_dictionary['14:00'] += 1
                    time_dictionary['14:30'] += 1
                    time_dictionary['15:00'] += 1
                    time_dictionary['15:30'] += 1
                    time_dictionary['16:00'] += 1
                    time_dictionary['16:30'] += 1
                    time_dictionary['17:00'] += 1
                    time_dictionary['17:30'] += 1
                    time_dictionary['18:00'] += 1
                    time_dictionary['18:30'] += 1
                    time_dictionary['19:00'] += 1
                    time_dictionary['19:30'] += 1
                    time_dictionary['20:00'] += 1

                elif 30 <= logon[1] < 60:
                    time_dictionary['14:00'] += 1
                    time_dictionary['14:30'] += 1
                    time_dictionary['15:00'] += 1
                    time_dictionary['15:30'] += 1
                    time_dictionary['16:00'] += 1
                    time_dictionary['16:30'] += 1
                    time_dictionary['17:00'] += 1
                    time_dictionary['17:30'] += 1
                    time_dictionary['18:00'] += 1
                    time_dictionary['18:30'] += 1
                    time_dictionary['19:00'] += 1
                    time_dictionary['19:30'] += 1
                    time_dictionary['20:00'] += 1
                    time_dictionary['20:30'] += 1

            if logoff[0] == logon[0] + 8:
                if 30 > logoff[1] >= 0:
                    time_dictionary['14:00'] += 1
                    time_dictionary['14:30'] += 1
                    time_dictionary['15:00'] += 1
                    time_dictionary['15:30'] += 1
                    time_dictionary['16:00'] += 1
                    time_dictionary['16:30'] += 1
                    time_dictionary['17:00'] += 1
                    time_dictionary['17:30'] += 1
                    time_dictionary['18:00'] += 1
                    time_dictionary['18:30'] += 1
                    time_dictionary['19:00'] += 1
                    time_dictionary['19:30'] += 1
                    time_dictionary['20:00'] += 1
                    time_dictionary['20:30'] += 1
                    time_dictionary['21:00'] += 1

                elif 30 <= logon[1] < 60:
                    time_dictionary['14:00'] += 1
                    time_dictionary['14:30'] += 1
                    time_dictionary['15:00'] += 1
                    time_dictionary['15:30'] += 1
                    time_dictionary['16:00'] += 1
                    time_dictionary['16:30'] += 1
                    time_dictionary['17:00'] += 1
                    time_dictionary['17:30'] += 1
                    time_dictionary['18:00'] += 1
                    time_dictionary['18:30'] += 1
                    time_dictionary['19:00'] += 1
                    time_dictionary['19:30'] += 1
                    time_dictionary['20:00'] += 1
                    time_dictionary['20:30'] += 1
                    time_dictionary['21:00'] += 1
                    time_dictionary['21:30'] += 1

        elif logon[0] == 14 and 30 > logon[1] >= 0:
            time_dictionary['14:00'] += 1

            if logoff[0] == logon[0]:
                if 30 <= logoff[1] < 60:
                    time_dictionary['14:30'] += 1

            elif logoff[0] == logon[0] + 1:
                if 30 > logoff[1] >= 0:
                    time_dictionary['14:30'] += 1
                    time_dictionary['15:00'] += 1

                elif 30 <= logoff[1] < 60:
                    time_dictionary['14:30'] += 1
                    time_dictionary['15:00'] += 1
                    time_dictionary['15:30'] += 1

            elif logoff[0] == logon[0] + 2:
                if 30 > logoff[1] >= 0:
                    time_dictionary['14:30'] += 1
                    time_dictionary['15:00'] += 1
                    time_dictionary['15:30'] += 1
                    time_dictionary['16:00'] += 1

                elif 30 <= logoff[1] < 60:
                    time_dictionary['14:30'] += 1
                    time_dictionary['15:00'] += 1
                    time_dictionary['15:30'] += 1
                    time_dictionary['16:00'] += 1
                    time_dictionary['16:30'] += 1

            elif logoff[0] == logon[0] + 3:
                if 30 > logoff[1] >= 0:
                    time_dictionary['14:30'] += 1
                    time_dictionary['15:00'] += 1
                    time_dictionary['15:30'] += 1
                    time_dictionary['16:00'] += 1
                    time_dictionary['16:30'] += 1
                    time_dictionary['17:00'] += 1

                elif 30 <= logoff[1] < 60:
                    time_dictionary['14:30'] += 1
                    time_dictionary['15:00'] += 1
                    time_dictionary['15:30'] += 1
                    time_dictionary['16:00'] += 1
                    time_dictionary['16:30'] += 1
                    time_dictionary['17:00'] += 1
                    time_dictionary['17:30'] += 1

            elif logoff[0] == logon[0] + 4:
                if 30 > logoff[1] >= 0:
                    time_dictionary['14:30'] += 1
                    time_dictionary['15:00'] += 1
                    time_dictionary['15:30'] += 1
                    time_dictionary['16:00'] += 1
                    time_dictionary['16:30'] += 1
                    time_dictionary['17:00'] += 1
                    time_dictionary['17:30'] += 1
                    time_dictionary['18:00'] += 1

                elif 30 <= logoff[1] < 60:
                    time_dictionary['14:30'] += 1
                    time_dictionary['15:00'] += 1
                    time_dictionary['15:30'] += 1
                    time_dictionary['16:00'] += 1
                    time_dictionary['16:30'] += 1
                    time_dictionary['17:00'] += 1
                    time_dictionary['17:30'] += 1
                    time_dictionary['18:00'] += 1
                    time_dictionary['18:30'] += 1

            elif logoff[0] == logon[0] + 5:
                if 30 > logoff[1] >= 0:
                    time_dictionary['14:30'] += 1
                    time_dictionary['15:00'] += 1
                    time_dictionary['15:30'] += 1
                    time_dictionary['16:00'] += 1
                    time_dictionary['16:30'] += 1
                    time_dictionary['17:00'] += 1
                    time_dictionary['17:30'] += 1
                    time_dictionary['18:00'] += 1
                    time_dictionary['18:30'] += 1
                    time_dictionary['19:00'] += 1

                elif 30 <= logoff[1] < 60:
                    time_dictionary['14:30'] += 1
                    time_dictionary['15:00'] += 1
                    time_dictionary['15:30'] += 1
                    time_dictionary['16:00'] += 1
                    time_dictionary['16:30'] += 1
                    time_dictionary['17:00'] += 1
                    time_dictionary['17:30'] += 1
                    time_dictionary['18:00'] += 1
                    time_dictionary['18:30'] += 1
                    time_dictionary['19:00'] += 1
                    time_dictionary['19:30'] += 1

            elif logoff[0] == logon[0] + 6:
                if 30 > logoff[1] >= 0:
                    time_dictionary['14:30'] += 1
                    time_dictionary['15:00'] += 1
                    time_dictionary['15:30'] += 1
                    time_dictionary['16:00'] += 1
                    time_dictionary['16:30'] += 1
                    time_dictionary['17:00'] += 1
                    time_dictionary['17:30'] += 1
                    time_dictionary['18:00'] += 1
                    time_dictionary['18:30'] += 1
                    time_dictionary['19:00'] += 1
                    time_dictionary['19:30'] += 1
                    time_dictionary['20:00'] += 1

                elif 30 <= logoff[1] < 60:
                    time_dictionary['14:30'] += 1
                    time_dictionary['15:00'] += 1
                    time_dictionary['15:30'] += 1
                    time_dictionary['16:00'] += 1
                    time_dictionary['16:30'] += 1
                    time_dictionary['17:00'] += 1
                    time_dictionary['17:30'] += 1
                    time_dictionary['18:00'] += 1
                    time_dictionary['18:30'] += 1
                    time_dictionary['19:00'] += 1
                    time_dictionary['19:30'] += 1
                    time_dictionary['20:00'] += 1
                    time_dictionary['20:30'] += 1

            elif logoff[0] == logon[0] + 7:
                if 30 > logoff[1] >= 0:
                    time_dictionary['14:30'] += 1
                    time_dictionary['15:00'] += 1
                    time_dictionary['15:30'] += 1
                    time_dictionary['16:00'] += 1
                    time_dictionary['16:30'] += 1
                    time_dictionary['17:00'] += 1
                    time_dictionary['17:30'] += 1
                    time_dictionary['18:00'] += 1
                    time_dictionary['18:30'] += 1
                    time_dictionary['19:00'] += 1
                    time_dictionary['19:30'] += 1
                    time_dictionary['20:00'] += 1
                    time_dictionary['20:30'] += 1
                    time_dictionary['21:00'] += 1

                elif 30 <= logoff[1] < 60:
                    time_dictionary['14:30'] += 1
                    time_dictionary['15:00'] += 1
                    time_dictionary['15:30'] += 1
                    time_dictionary['16:00'] += 1
                    time_dictionary['16:30'] += 1
                    time_dictionary['17:00'] += 1
                    time_dictionary['17:30'] += 1
                    time_dictionary['18:00'] += 1
                    time_dictionary['18:30'] += 1
                    time_dictionary['19:00'] += 1
                    time_dictionary['19:30'] += 1
                    time_dictionary['20:00'] += 1
                    time_dictionary['20:30'] += 1
                    time_dictionary['21:00'] += 1
                    time_dictionary['21:30'] += 1

        elif logon[0] == 14 and 30 <= logon[1] < 60:
            time_dictionary['14:30'] += 1

            if logoff[0] == logon[0] + 1:
                if 30 > logoff[1] >= 0:
                    time_dictionary['15:00'] += 1

                elif 30 <= logon[1] < 60:
                    time_dictionary['15:00'] += 1
                    time_dictionary['15:30'] += 1

            if logoff[0] == logon[0] + 2:
                if 30 > logoff[1] >= 0:
                    time_dictionary['15:00'] += 1
                    time_dictionary['15:30'] += 1
                    time_dictionary['16:00'] += 1

                elif 30 <= logon[1] < 60:
                    time_dictionary['15:00'] += 1
                    time_dictionary['15:30'] += 1
                    time_dictionary['16:00'] += 1
                    time_dictionary['16:30'] += 1

            if logoff[0] == logon[0] + 3:
                if 30 > logoff[1] >= 0:
                    time_dictionary['15:00'] += 1
                    time_dictionary['15:30'] += 1
                    time_dictionary['16:00'] += 1
                    time_dictionary['16:30'] += 1
                    time_dictionary['17:00'] += 1

                elif 30 <= logon[1] < 60:
                    time_dictionary['15:00'] += 1
                    time_dictionary['15:30'] += 1
                    time_dictionary['16:00'] += 1
                    time_dictionary['16:30'] += 1
                    time_dictionary['17:00'] += 1
                    time_dictionary['17:30'] += 1

            if logoff[0] == logon[0] + 4:
                if 30 > logoff[1] >= 0:
                    time_dictionary['15:00'] += 1
                    time_dictionary['15:30'] += 1
                    time_dictionary['16:00'] += 1
                    time_dictionary['16:30'] += 1
                    time_dictionary['17:00'] += 1
                    time_dictionary['17:30'] += 1
                    time_dictionary['18:00'] += 1

                elif 30 <= logon[1] < 60:
                    time_dictionary['15:00'] += 1
                    time_dictionary['15:30'] += 1
                    time_dictionary['16:00'] += 1
                    time_dictionary['16:30'] += 1
                    time_dictionary['17:00'] += 1
                    time_dictionary['17:30'] += 1
                    time_dictionary['18:00'] += 1
                    time_dictionary['18:30'] += 1

            if logoff[0] == logon[0] + 5:
                if 30 > logoff[1] >= 0:
                    time_dictionary['15:00'] += 1
                    time_dictionary['15:30'] += 1
                    time_dictionary['16:00'] += 1
                    time_dictionary['16:30'] += 1
                    time_dictionary['17:00'] += 1
                    time_dictionary['17:30'] += 1
                    time_dictionary['18:00'] += 1
                    time_dictionary['18:30'] += 1
                    time_dictionary['19:00'] += 1

                elif 30 <= logon[1] < 60:
                    time_dictionary['15:00'] += 1
                    time_dictionary['15:30'] += 1
                    time_dictionary['16:00'] += 1
                    time_dictionary['16:30'] += 1
                    time_dictionary['17:00'] += 1
                    time_dictionary['17:30'] += 1
                    time_dictionary['18:00'] += 1
                    time_dictionary['18:30'] += 1
                    time_dictionary['19:00'] += 1
                    time_dictionary['19:30'] += 1

            if logoff[0] == logon[0] + 6:
                if 30 > logoff[1] >= 0:
                    time_dictionary['15:00'] += 1
                    time_dictionary['15:30'] += 1
                    time_dictionary['16:00'] += 1
                    time_dictionary['16:30'] += 1
                    time_dictionary['17:00'] += 1
                    time_dictionary['17:30'] += 1
                    time_dictionary['18:00'] += 1
                    time_dictionary['18:30'] += 1
                    time_dictionary['19:00'] += 1
                    time_dictionary['19:30'] += 1
                    time_dictionary['20:00'] += 1

                elif 30 <= logon[1] < 60:
                    time_dictionary['15:00'] += 1
                    time_dictionary['15:30'] += 1
                    time_dictionary['16:00'] += 1
                    time_dictionary['16:30'] += 1
                    time_dictionary['17:00'] += 1
                    time_dictionary['17:30'] += 1
                    time_dictionary['18:00'] += 1
                    time_dictionary['18:30'] += 1
                    time_dictionary['19:00'] += 1
                    time_dictionary['19:30'] += 1
                    time_dictionary['20:00'] += 1
                    time_dictionary['20:30'] += 1

            if logoff[0] == logon[0] + 7:
                if 30 > logoff[1] >= 0:
                    time_dictionary['15:00'] += 1
                    time_dictionary['15:30'] += 1
                    time_dictionary['16:00'] += 1
                    time_dictionary['16:30'] += 1
                    time_dictionary['17:00'] += 1
                    time_dictionary['17:30'] += 1
                    time_dictionary['18:00'] += 1
                    time_dictionary['18:30'] += 1
                    time_dictionary['19:00'] += 1
                    time_dictionary['19:30'] += 1
                    time_dictionary['20:00'] += 1
                    time_dictionary['20:30'] += 1
                    time_dictionary['21:00'] += 1

                elif 30 <= logon[1] < 60:
                    time_dictionary['15:00'] += 1
                    time_dictionary['15:30'] += 1
                    time_dictionary['16:00'] += 1
                    time_dictionary['16:30'] += 1
                    time_dictionary['17:00'] += 1
                    time_dictionary['17:30'] += 1
                    time_dictionary['18:00'] += 1
                    time_dictionary['18:30'] += 1
                    time_dictionary['19:00'] += 1
                    time_dictionary['19:30'] += 1
                    time_dictionary['20:00'] += 1
                    time_dictionary['20:30'] += 1
                    time_dictionary['21:00'] += 1
                    time_dictionary['21:30'] += 1

        elif logon[0] == 15 and 30 > logon[1] >= 0:
            time_dictionary['15:00'] += 1

            if logoff[0] == logon[0]:
                if 30 <= logoff[1] < 60:
                    time_dictionary['15:30'] += 1

            elif logoff[0] == logon[0] + 1:
                if 30 > logoff[1] >= 0:
                    time_dictionary['15:30'] += 1
                    time_dictionary['16:00'] += 1

                elif 30 <= logoff[1] < 60:
                    time_dictionary['15:30'] += 1
                    time_dictionary['16:00'] += 1
                    time_dictionary['16:30'] += 1

            elif logoff[0] == logon[0] + 2:
                if 30 > logoff[1] >= 0:
                    time_dictionary['15:30'] += 1
                    time_dictionary['16:00'] += 1
                    time_dictionary['16:30'] += 1
                    time_dictionary['17:00'] += 1

                elif 30 <= logoff[1] < 60:
                    time_dictionary['15:30'] += 1
                    time_dictionary['16:00'] += 1
                    time_dictionary['16:30'] += 1
                    time_dictionary['17:00'] += 1
                    time_dictionary['17:30'] += 1

            elif logoff[0] == logon[0] + 3:
                if 30 > logoff[1] >= 0:
                    time_dictionary['15:30'] += 1
                    time_dictionary['16:00'] += 1
                    time_dictionary['16:30'] += 1
                    time_dictionary['17:00'] += 1
                    time_dictionary['17:30'] += 1
                    time_dictionary['18:00'] += 1

                elif 30 <= logoff[1] < 60:
                    time_dictionary['15:30'] += 1
                    time_dictionary['16:00'] += 1
                    time_dictionary['16:30'] += 1
                    time_dictionary['17:00'] += 1
                    time_dictionary['17:30'] += 1
                    time_dictionary['18:00'] += 1
                    time_dictionary['18:30'] += 1

            elif logoff[0] == logon[0] + 4:
                if 30 > logoff[1] >= 0:
                    time_dictionary['15:30'] += 1
                    time_dictionary['16:00'] += 1
                    time_dictionary['16:30'] += 1
                    time_dictionary['17:00'] += 1
                    time_dictionary['17:30'] += 1
                    time_dictionary['18:00'] += 1
                    time_dictionary['18:30'] += 1
                    time_dictionary['19:00'] += 1

                elif 30 <= logoff[1] < 60:
                    time_dictionary['15:30'] += 1
                    time_dictionary['16:00'] += 1
                    time_dictionary['16:30'] += 1
                    time_dictionary['17:00'] += 1
                    time_dictionary['17:30'] += 1
                    time_dictionary['18:00'] += 1
                    time_dictionary['18:30'] += 1
                    time_dictionary['19:00'] += 1
                    time_dictionary['19:30'] += 1

            elif logoff[0] == logon[0] + 5:
                if 30 > logoff[1] >= 0:
                    time_dictionary['15:30'] += 1
                    time_dictionary['16:00'] += 1
                    time_dictionary['16:30'] += 1
                    time_dictionary['17:00'] += 1
                    time_dictionary['17:30'] += 1
                    time_dictionary['18:00'] += 1
                    time_dictionary['18:30'] += 1
                    time_dictionary['19:00'] += 1
                    time_dictionary['19:30'] += 1
                    time_dictionary['20:00'] += 1

                elif 30 <= logoff[1] < 60:
                    time_dictionary['15:30'] += 1
                    time_dictionary['16:00'] += 1
                    time_dictionary['16:30'] += 1
                    time_dictionary['17:00'] += 1
                    time_dictionary['17:30'] += 1
                    time_dictionary['18:00'] += 1
                    time_dictionary['18:30'] += 1
                    time_dictionary['19:00'] += 1
                    time_dictionary['19:30'] += 1
                    time_dictionary['20:00'] += 1
                    time_dictionary['20:30'] += 1

            elif logoff[0] == logon[0] + 6:
                if 30 > logoff[1] >= 0:
                    time_dictionary['15:30'] += 1
                    time_dictionary['16:00'] += 1
                    time_dictionary['16:30'] += 1
                    time_dictionary['17:00'] += 1
                    time_dictionary['17:30'] += 1
                    time_dictionary['18:00'] += 1
                    time_dictionary['18:30'] += 1
                    time_dictionary['19:00'] += 1
                    time_dictionary['19:30'] += 1
                    time_dictionary['20:00'] += 1
                    time_dictionary['20:30'] += 1
                    time_dictionary['21:00'] += 1

                elif 30 <= logoff[1] < 60:
                    time_dictionary['15:30'] += 1
                    time_dictionary['16:00'] += 1
                    time_dictionary['16:30'] += 1
                    time_dictionary['17:00'] += 1
                    time_dictionary['17:30'] += 1
                    time_dictionary['18:00'] += 1
                    time_dictionary['18:30'] += 1
                    time_dictionary['19:00'] += 1
                    time_dictionary['19:30'] += 1
                    time_dictionary['20:00'] += 1
                    time_dictionary['20:30'] += 1
                    time_dictionary['21:00'] += 1
                    time_dictionary['21:30'] += 1

        elif logon[0] == 15 and 30 <= logon[1] < 60:
            time_dictionary['15:30'] += 1

            if logoff[0] == logon[0] + 1:
                if 30 > logoff[1] >= 0:
                    time_dictionary['16:00'] += 1

                elif 30 <= logon[1] < 60:
                    time_dictionary['16:00'] += 1
                    time_dictionary['16:30'] += 1

            if logoff[0] == logon[0] + 2:
                if 30 > logoff[1] >= 0:
                    time_dictionary['16:00'] += 1
                    time_dictionary['16:30'] += 1
                    time_dictionary['17:00'] += 1

                elif 30 <= logon[1] < 60:
                    time_dictionary['16:00'] += 1
                    time_dictionary['16:30'] += 1
                    time_dictionary['17:00'] += 1
                    time_dictionary['17:30'] += 1

            if logoff[0] == logon[0] + 3:
                if 30 > logoff[1] >= 0:
                    time_dictionary['16:00'] += 1
                    time_dictionary['16:30'] += 1
                    time_dictionary['17:00'] += 1
                    time_dictionary['17:30'] += 1
                    time_dictionary['18:00'] += 1

                elif 30 <= logon[1] < 60:
                    time_dictionary['16:00'] += 1
                    time_dictionary['16:30'] += 1
                    time_dictionary['17:00'] += 1
                    time_dictionary['17:30'] += 1
                    time_dictionary['18:00'] += 1
                    time_dictionary['18:30'] += 1

            if logoff[0] == logon[0] + 4:
                if 30 > logoff[1] >= 0:
                    time_dictionary['16:00'] += 1
                    time_dictionary['16:30'] += 1
                    time_dictionary['17:00'] += 1
                    time_dictionary['17:30'] += 1
                    time_dictionary['18:00'] += 1
                    time_dictionary['18:30'] += 1
                    time_dictionary['19:00'] += 1

                elif 30 <= logon[1] < 60:
                    time_dictionary['16:00'] += 1
                    time_dictionary['16:30'] += 1
                    time_dictionary['17:00'] += 1
                    time_dictionary['17:30'] += 1
                    time_dictionary['18:00'] += 1
                    time_dictionary['18:30'] += 1
                    time_dictionary['19:00'] += 1
                    time_dictionary['19:30'] += 1

            if logoff[0] == logon[0] + 5:
                if 30 > logoff[1] >= 0:
                    time_dictionary['16:00'] += 1
                    time_dictionary['16:30'] += 1
                    time_dictionary['17:00'] += 1
                    time_dictionary['17:30'] += 1
                    time_dictionary['18:00'] += 1
                    time_dictionary['18:30'] += 1
                    time_dictionary['19:00'] += 1
                    time_dictionary['19:30'] += 1
                    time_dictionary['20:00'] += 1

                elif 30 <= logon[1] < 60:
                    time_dictionary['16:00'] += 1
                    time_dictionary['16:30'] += 1
                    time_dictionary['17:00'] += 1
                    time_dictionary['17:30'] += 1
                    time_dictionary['18:00'] += 1
                    time_dictionary['18:30'] += 1
                    time_dictionary['19:00'] += 1
                    time_dictionary['19:30'] += 1
                    time_dictionary['20:00'] += 1
                    time_dictionary['20:30'] += 1

            if logoff[0] == logon[0] + 6:
                if 30 > logoff[1] >= 0:
                    time_dictionary['16:00'] += 1
                    time_dictionary['16:30'] += 1
                    time_dictionary['17:00'] += 1
                    time_dictionary['17:30'] += 1
                    time_dictionary['18:00'] += 1
                    time_dictionary['18:30'] += 1
                    time_dictionary['19:00'] += 1
                    time_dictionary['19:30'] += 1
                    time_dictionary['20:00'] += 1
                    time_dictionary['20:30'] += 1
                    time_dictionary['21:00'] += 1

                elif 30 <= logon[1] < 60:
                    time_dictionary['16:00'] += 1
                    time_dictionary['16:30'] += 1
                    time_dictionary['17:00'] += 1
                    time_dictionary['17:30'] += 1
                    time_dictionary['18:00'] += 1
                    time_dictionary['18:30'] += 1
                    time_dictionary['19:00'] += 1
                    time_dictionary['19:30'] += 1
                    time_dictionary['20:00'] += 1
                    time_dictionary['20:30'] += 1
                    time_dictionary['21:00'] += 1
                    time_dictionary['21:30'] += 1

        elif logon[0] == 16 and 30 > logon[1] >= 0:
            time_dictionary['16:00'] += 1

            if logoff[0] == logon[0]:
                if 30 <= logoff[1] < 60:
                    time_dictionary['16:30'] += 1

            elif logoff[0] == logon[0] + 1:
                if 30 > logoff[1] >= 0:
                    time_dictionary['16:30'] += 1
                    time_dictionary['17:00'] += 1

                elif 30 <= logoff[1] < 60:
                    time_dictionary['16:30'] += 1
                    time_dictionary['17:00'] += 1
                    time_dictionary['17:30'] += 1

            elif logoff[0] == logon[0] + 2:
                if 30 > logoff[1] >= 0:
                    time_dictionary['16:30'] += 1
                    time_dictionary['17:00'] += 1
                    time_dictionary['17:30'] += 1
                    time_dictionary['18:00'] += 1

                elif 30 <= logoff[1] < 60:
                    time_dictionary['16:30'] += 1
                    time_dictionary['17:00'] += 1
                    time_dictionary['17:30'] += 1
                    time_dictionary['18:00'] += 1
                    time_dictionary['18:30'] += 1

            elif logoff[0] == logon[0] + 3:
                if 30 > logoff[1] >= 0:
                    time_dictionary['16:30'] += 1
                    time_dictionary['17:00'] += 1
                    time_dictionary['17:30'] += 1
                    time_dictionary['18:00'] += 1
                    time_dictionary['18:30'] += 1
                    time_dictionary['19:00'] += 1

                elif 30 <= logoff[1] < 60:
                    time_dictionary['16:30'] += 1
                    time_dictionary['17:00'] += 1
                    time_dictionary['17:30'] += 1
                    time_dictionary['18:00'] += 1
                    time_dictionary['18:30'] += 1
                    time_dictionary['19:00'] += 1
                    time_dictionary['19:30'] += 1

            elif logoff[0] == logon[0] + 4:
                if 30 > logoff[1] >= 0:
                    time_dictionary['16:30'] += 1
                    time_dictionary['17:00'] += 1
                    time_dictionary['17:30'] += 1
                    time_dictionary['18:00'] += 1
                    time_dictionary['18:30'] += 1
                    time_dictionary['19:00'] += 1
                    time_dictionary['19:30'] += 1
                    time_dictionary['20:00'] += 1

                elif 30 <= logoff[1] < 60:
                    time_dictionary['16:30'] += 1
                    time_dictionary['17:00'] += 1
                    time_dictionary['17:30'] += 1
                    time_dictionary['18:00'] += 1
                    time_dictionary['18:30'] += 1
                    time_dictionary['19:00'] += 1
                    time_dictionary['19:30'] += 1
                    time_dictionary['20:00'] += 1
                    time_dictionary['20:30'] += 1

            elif logoff[0] == logon[0] + 5:
                if 30 > logoff[1] >= 0:
                    time_dictionary['16:30'] += 1
                    time_dictionary['17:00'] += 1
                    time_dictionary['17:30'] += 1
                    time_dictionary['18:00'] += 1
                    time_dictionary['18:30'] += 1
                    time_dictionary['19:00'] += 1
                    time_dictionary['19:30'] += 1
                    time_dictionary['20:00'] += 1
                    time_dictionary['20:30'] += 1
                    time_dictionary['21:00'] += 1

                elif 30 <= logoff[1] < 60:
                    time_dictionary['16:30'] += 1
                    time_dictionary['17:00'] += 1
                    time_dictionary['17:30'] += 1
                    time_dictionary['18:00'] += 1
                    time_dictionary['18:30'] += 1
                    time_dictionary['19:00'] += 1
                    time_dictionary['19:30'] += 1
                    time_dictionary['20:00'] += 1
                    time_dictionary['20:30'] += 1
                    time_dictionary['21:00'] += 1
                    time_dictionary['21:30'] += 1

        elif logon[0] == 16 and 30 <= logon[1] < 60:
            time_dictionary['16:30'] += 1

            if logoff[0] == logon[0] + 1:
                if 30 > logoff[1] >= 0:
                    time_dictionary['17:00'] += 1

                elif 30 <= logon[1] < 60:
                    time_dictionary['17:00'] += 1
                    time_dictionary['17:30'] += 1

            if logoff[0] == logon[0] + 2:
                if 30 > logoff[1] >= 0:
                    time_dictionary['17:00'] += 1
                    time_dictionary['17:30'] += 1
                    time_dictionary['18:00'] += 1

                elif 30 <= logon[1] < 60:
                    time_dictionary['17:00'] += 1
                    time_dictionary['17:30'] += 1
                    time_dictionary['18:00'] += 1
                    time_dictionary['18:30'] += 1

            if logoff[0] == logon[0] + 3:
                if 30 > logoff[1] >= 0:
                    time_dictionary['17:00'] += 1
                    time_dictionary['17:30'] += 1
                    time_dictionary['18:00'] += 1
                    time_dictionary['18:30'] += 1
                    time_dictionary['19:00'] += 1

                elif 30 <= logon[1] < 60:
                    time_dictionary['17:00'] += 1
                    time_dictionary['17:30'] += 1
                    time_dictionary['18:00'] += 1
                    time_dictionary['18:30'] += 1
                    time_dictionary['19:00'] += 1
                    time_dictionary['19:30'] += 1

            if logoff[0] == logon[0] + 4:
                if 30 > logoff[1] >= 0:
                    time_dictionary['17:00'] += 1
                    time_dictionary['17:30'] += 1
                    time_dictionary['18:00'] += 1
                    time_dictionary['18:30'] += 1
                    time_dictionary['19:00'] += 1
                    time_dictionary['19:30'] += 1
                    time_dictionary['20:00'] += 1

                elif 30 <= logon[1] < 60:
                    time_dictionary['17:00'] += 1
                    time_dictionary['17:30'] += 1
                    time_dictionary['18:00'] += 1
                    time_dictionary['18:30'] += 1
                    time_dictionary['19:00'] += 1
                    time_dictionary['19:30'] += 1
                    time_dictionary['20:00'] += 1
                    time_dictionary['20:30'] += 1

            if logoff[0] == logon[0] + 5:
                if 30 > logoff[1] >= 0:
                    time_dictionary['17:00'] += 1
                    time_dictionary['17:30'] += 1
                    time_dictionary['18:00'] += 1
                    time_dictionary['18:30'] += 1
                    time_dictionary['19:00'] += 1
                    time_dictionary['19:30'] += 1
                    time_dictionary['20:00'] += 1
                    time_dictionary['20:30'] += 1
                    time_dictionary['21:00'] += 1

                elif 30 <= logon[1] < 60:
                    time_dictionary['17:00'] += 1
                    time_dictionary['17:30'] += 1
                    time_dictionary['18:00'] += 1
                    time_dictionary['18:30'] += 1
                    time_dictionary['19:00'] += 1
                    time_dictionary['19:30'] += 1
                    time_dictionary['20:00'] += 1
                    time_dictionary['20:30'] += 1
                    time_dictionary['21:00'] += 1
                    time_dictionary['21:30'] += 1

        elif logon[0] == 17 and 30 > logon[1] >= 0:
            time_dictionary['17:00'] += 1

            if logoff[0] == logon[0]:
                if 30 <= logoff[1] < 60:
                    time_dictionary['17:30'] += 1

            elif logoff[0] == logon[0] + 1:
                if 30 > logoff[1] >= 0:
                    time_dictionary['17:30'] += 1
                    time_dictionary['18:00'] += 1

                elif 30 <= logoff[1] < 60:
                    time_dictionary['17:30'] += 1
                    time_dictionary['18:00'] += 1
                    time_dictionary['18:30'] += 1

            elif logoff[0] == logon[0] + 2:
                if 30 > logoff[1] >= 0:
                    time_dictionary['17:30'] += 1
                    time_dictionary['18:00'] += 1
                    time_dictionary['18:30'] += 1
                    time_dictionary['19:00'] += 1

                elif 30 <= logoff[1] < 60:
                    time_dictionary['17:30'] += 1
                    time_dictionary['18:00'] += 1
                    time_dictionary['18:30'] += 1
                    time_dictionary['19:00'] += 1
                    time_dictionary['19:30'] += 1

            elif logoff[0] == logon[0] + 3:
                if 30 > logoff[1] >= 0:
                    time_dictionary['17:30'] += 1
                    time_dictionary['18:00'] += 1
                    time_dictionary['18:30'] += 1
                    time_dictionary['19:00'] += 1
                    time_dictionary['19:30'] += 1
                    time_dictionary['20:00'] += 1

                elif 30 <= logoff[1] < 60:
                    time_dictionary['17:30'] += 1
                    time_dictionary['18:00'] += 1
                    time_dictionary['18:30'] += 1
                    time_dictionary['19:00'] += 1
                    time_dictionary['19:30'] += 1
                    time_dictionary['20:00'] += 1
                    time_dictionary['20:30'] += 1

            elif logoff[0] == logon[0] + 4:
                if 30 > logoff[1] >= 0:
                    time_dictionary['17:30'] += 1
                    time_dictionary['18:00'] += 1
                    time_dictionary['18:30'] += 1
                    time_dictionary['19:00'] += 1
                    time_dictionary['19:30'] += 1
                    time_dictionary['20:00'] += 1
                    time_dictionary['20:30'] += 1
                    time_dictionary['21:00'] += 1

                elif 30 <= logoff[1] < 60:
                    time_dictionary['17:30'] += 1
                    time_dictionary['18:00'] += 1
                    time_dictionary['18:30'] += 1
                    time_dictionary['19:00'] += 1
                    time_dictionary['19:30'] += 1
                    time_dictionary['20:00'] += 1
                    time_dictionary['20:30'] += 1
                    time_dictionary['21:00'] += 1
                    time_dictionary['21:30'] += 1

        elif logon[0] == 17 and 30 <= logon[1] < 60:
            time_dictionary['17:30'] += 1

            if logoff[0] == logon[0] + 1:
                if 30 > logoff[1] >= 0:
                    time_dictionary['18:00'] += 1

                elif 30 <= logon[1] < 60:
                    time_dictionary['18:00'] += 1
                    time_dictionary['18:30'] += 1

            if logoff[0] == logon[0] + 2:
                if 30 > logoff[1] >= 0:
                    time_dictionary['18:00'] += 1
                    time_dictionary['18:30'] += 1
                    time_dictionary['19:00'] += 1

                elif 30 <= logon[1] < 60:
                    time_dictionary['18:00'] += 1
                    time_dictionary['18:30'] += 1
                    time_dictionary['19:00'] += 1
                    time_dictionary['19:30'] += 1

            if logoff[0] == logon[0] + 3:
                if 30 > logoff[1] >= 0:
                    time_dictionary['18:00'] += 1
                    time_dictionary['18:30'] += 1
                    time_dictionary['19:00'] += 1
                    time_dictionary['19:30'] += 1
                    time_dictionary['20:00'] += 1

                elif 30 <= logon[1] < 60:
                    time_dictionary['18:00'] += 1
                    time_dictionary['18:30'] += 1
                    time_dictionary['19:00'] += 1
                    time_dictionary['19:30'] += 1
                    time_dictionary['20:00'] += 1
                    time_dictionary['20:30'] += 1

            if logoff[0] == logon[0] + 4:
                if 30 > logoff[1] >= 0:
                    time_dictionary['18:00'] += 1
                    time_dictionary['18:30'] += 1
                    time_dictionary['19:00'] += 1
                    time_dictionary['19:30'] += 1
                    time_dictionary['20:00'] += 1
                    time_dictionary['20:30'] += 1
                    time_dictionary['21:00'] += 1

                elif 30 <= logon[1] < 60:
                    time_dictionary['18:00'] += 1
                    time_dictionary['18:30'] += 1
                    time_dictionary['19:00'] += 1
                    time_dictionary['19:30'] += 1
                    time_dictionary['20:00'] += 1
                    time_dictionary['20:30'] += 1
                    time_dictionary['21:00'] += 1
                    time_dictionary['21:30'] += 1

        elif logon[0] == 18 and 30 > logon[1] >= 0:
            time_dictionary['18:00'] += 1

            if logoff[0] == logon[0]:
                if 30 <= logoff[1] < 60:
                    time_dictionary['18:30'] += 1

            elif logoff[0] == logon[0] + 1:
                if 30 > logoff[1] >= 0:
                    time_dictionary['18:30'] += 1
                    time_dictionary['19:00'] += 1

                elif 30 <= logoff[1] < 60:
                    time_dictionary['18:30'] += 1
                    time_dictionary['19:00'] += 1
                    time_dictionary['19:30'] += 1

            elif logoff[0] == logon[0] + 2:
                if 30 > logoff[1] >= 0:
                    time_dictionary['18:30'] += 1
                    time_dictionary['19:00'] += 1
                    time_dictionary['19:30'] += 1
                    time_dictionary['20:00'] += 1

                elif 30 <= logoff[1] < 60:
                    time_dictionary['18:30'] += 1
                    time_dictionary['19:00'] += 1
                    time_dictionary['19:30'] += 1
                    time_dictionary['20:00'] += 1
                    time_dictionary['20:30'] += 1

            elif logoff[0] == logon[0] + 3:
                if 30 > logoff[1] >= 0:
                    time_dictionary['18:30'] += 1
                    time_dictionary['19:00'] += 1
                    time_dictionary['19:30'] += 1
                    time_dictionary['20:00'] += 1
                    time_dictionary['20:30'] += 1
                    time_dictionary['21:00'] += 1

                elif 30 <= logoff[1] < 60:
                    time_dictionary['18:30'] += 1
                    time_dictionary['19:00'] += 1
                    time_dictionary['19:30'] += 1
                    time_dictionary['20:00'] += 1
                    time_dictionary['20:30'] += 1
                    time_dictionary['21:00'] += 1
                    time_dictionary['21:30'] += 1

        elif logon[0] == 18 and 30 <= logon[1] < 60:
            time_dictionary['18:30'] += 1

            if logoff[0] == logon[0] + 1:
                if 30 > logoff[1] >= 0:
                    time_dictionary['19:00'] += 1

                elif 30 <= logon[1] < 60:
                    time_dictionary['19:00'] += 1
                    time_dictionary['19:30'] += 1

            if logoff[0] == logon[0] + 2:
                if 30 > logoff[1] >= 0:
                    time_dictionary['19:00'] += 1
                    time_dictionary['19:30'] += 1
                    time_dictionary['20:00'] += 1

                elif 30 <= logon[1] < 60:
                    time_dictionary['19:00'] += 1
                    time_dictionary['19:30'] += 1
                    time_dictionary['20:00'] += 1
                    time_dictionary['20:30'] += 1

            if logoff[0] == logon[0] + 3:
                if 30 > logoff[1] >= 0:
                    time_dictionary['19:00'] += 1
                    time_dictionary['19:30'] += 1
                    time_dictionary['20:00'] += 1
                    time_dictionary['20:30'] += 1
                    time_dictionary['21:00'] += 1

                elif 30 <= logon[1] < 60:
                    time_dictionary['19:00'] += 1
                    time_dictionary['19:30'] += 1
                    time_dictionary['20:00'] += 1
                    time_dictionary['20:30'] += 1
                    time_dictionary['21:00'] += 1
                    time_dictionary['21:30'] += 1

        elif logon[0] == 19 and 30 > logon[1] >= 0:
            time_dictionary['19:00'] += 1

            if logoff[0] == logon[0]:
                if 30 <= logoff[1] < 60:
                    time_dictionary['19:30'] += 1

            elif logoff[0] == logon[0] + 1:
                if 30 > logoff[1] >= 0:
                    time_dictionary['19:30'] += 1
                    time_dictionary['20:00'] += 1

                elif 30 <= logoff[1] < 60:
                    time_dictionary['19:30'] += 1
                    time_dictionary['20:00'] += 1
                    time_dictionary['20:30'] += 1

            elif logoff[0] == logon[0] + 2:
                if 30 > logoff[1] >= 0:
                    time_dictionary['19:30'] += 1
                    time_dictionary['20:00'] += 1
                    time_dictionary['20:30'] += 1
                    time_dictionary['21:00'] += 1

                elif 30 <= logoff[1] < 60:
                    time_dictionary['19:30'] += 1
                    time_dictionary['20:00'] += 1
                    time_dictionary['20:30'] += 1
                    time_dictionary['21:00'] += 1
                    time_dictionary['21:30'] += 1

        elif logon[0] == 19 and 30 <= logon[1] < 60:
            time_dictionary['19:30'] += 1

            if logoff[0] == logon[0] + 1:
                if 30 > logoff[1] >= 0:
                    time_dictionary['20:00'] += 1

                elif 30 <= logon[1] < 60:
                    time_dictionary['20:00'] += 1
                    time_dictionary['20:30'] += 1

            if logoff[0] == logon[0] + 2:
                if 30 > logoff[1] >= 0:
                    time_dictionary['20:00'] += 1
                    time_dictionary['20:30'] += 1
                    time_dictionary['21:00'] += 1

                elif 30 <= logon[1] < 60:
                    time_dictionary['20:00'] += 1
                    time_dictionary['20:30'] += 1
                    time_dictionary['21:00'] += 1
                    time_dictionary['21:30'] += 1

        elif logon[0] == 20 and 30 > logon[1] >= 0:
            time_dictionary['20:00'] += 1

            if logoff[0] == logon[0]:
                if 30 <= logoff[1] < 60:
                    time_dictionary['20:30'] += 1

            elif logoff[0] == logon[0] + 1:
                if 30 > logoff[1] >= 0:
                    time_dictionary['20:30'] += 1
                    time_dictionary['21:00'] += 1

                elif 30 <= logoff[1] < 60:
                    time_dictionary['20:30'] += 1
                    time_dictionary['21:00'] += 1
                    time_dictionary['21:30'] += 1

        elif logon[0] == 20 and 30 <= logon[1] < 60:
            time_dictionary['20:30'] += 1

            if logoff[0] == logon[0] + 1:
                if 30 > logoff[1] >= 0:
                    time_dictionary['21:00'] += 1

                elif 30 <= logon[1] < 60:
                    time_dictionary['21:00'] += 1
                    time_dictionary['21:30'] += 1

        elif logon[0] == 21 and 30 > logon[1] >= 0:
            time_dictionary['21:00'] += 1

            if logoff[0] == logon[0]:
                if 30 <= logoff[1] < 60:
                    time_dictionary['21:30'] += 1

        elif logon[0] == 21 and 30 <= logon[1] < 60:
            time_dictionary['21:30'] += 1


    sorted_times = Counter(time_dictionary)
    sorted_times = OrderedDict(sorted_times.most_common())

    return sorted_times
