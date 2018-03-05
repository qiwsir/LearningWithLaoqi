#coding:utf-8

import datetime
from dateutil import rrule

def work_days(start, end, holidays=0, days_off=None):
    """
    . start: the date of start;
    . end: the date of end;
    . holidays: the holidays between 'start' and 'end'
    . days_off: days not to work, as weekends, for example, days_off=(5,6), 
                means that Satday and Sunday are the weekends.
                or other days that you do not work.
    """
    if not days_off:
        days_off = 5, 6
    workdays = [x for x in range(7) if x not in days_off]
    days = rrule.rrule(rrule.DAILY, dtstart=start, until=end,byweekday=workdays)
    return days.count() - holidays

if __name__ == "__main__":
    start = datetime.date(2018, 3, 1)
    end = datetime.date(2018, 3, 31)
    wd = work_days(start, end)
    print(wd)