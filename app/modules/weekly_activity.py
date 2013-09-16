#
# MongoDB collections
#
from .collections.users import *
from .collections.reports import *

from datetime import datetime, timedelta


class WeeklyActivity(object):
  def __init__(self, uid, date):
    self.uid, self.date = uid, date

  def get_data(self):
    try:
      datetime.strptime(self.date, "%Y-%m-%d")
    except:
      return {
        'success'     : False,
        'message'     : 'Incorrect date format',
        'data'        : None
      }
    else:
      return self.__data()
  
  def __data(self):
    report, count = [], 0
    week = self.__weekdays(self.date)
    for index, item in enumerate(week):
      data = Reports.objects(user_id = self.uid, date = item['date'])
      hours = self.__summarize(data)
      count += hours 
      report.append({
        'date'        : item['date'].strftime("%d/%m/%Y"),
        'dayName'     : item['day_name'],
        'hours'       : hours if hours != 0 else None
      })
    return {
      'success'     : True,
      'message'     : 'OK',
      'data'        : {
        'expectedHours'   : 40,
        'actualHours'     : count if count != 0 else None,
        'weekDays'        : report if len(report) != 0 else None
      }
    }

  def __weekdays(self, date_text):
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    temp, full_week = date_text.split('-'), []
    date = datetime(int(temp[0]), int(temp[1]), int(temp[2]) )
    first_weekday = date - timedelta(days = date.weekday() )
    for index, item in enumerate(days):
      d = first_weekday + timedelta(days = index)
      full_week.append( {'day_name': item, 'date': d } )
    return full_week

  def __summarize(self, data):
    hours = 0
    for item in data:
      hours += item.real_hours
    return hours
