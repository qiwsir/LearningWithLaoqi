#coding:utf-8

import datetime, calendar

def last_friday_1(today):
    last_Friday = today
    one_day = datetime.timedelta(days=1)
    while last_Friday.weekday() != calendar.FRIDAY:
        last_Friday -= one_day
    return last_Friday.strftime("%A, %Y-%b-%d")    #Friday, year-month-date

def last_friday_2(today):
    last_Friday = today
    while last_Friday.weekday() != calendar.FRIDAY:
        last_Friday -= datetime.date.resolution    #datetime.date.resolution == 1 day
    return last_Friday.strftime("%A, %Y-%b-%d")    

def last_friday_3(today):
    target_day = calendar.FRIDAY
    this_day = today.weekday()
    delta_to_target = (this_day - target_day) % 7
    last_Friday = today - datetime.timedelta(days=delta_to_target)
    return last_Friday.strftime("%A, %Y-%b-%d")


if __name__ == "__main__":
    today = datetime.date.today()
    lastFriday = last_friday_3(today)
    print(lastFriday)