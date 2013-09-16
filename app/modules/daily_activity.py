#
# MongoDB collections
#
from .collections.users import *
from .collections.projects import *
from .collections.project_tasks import *
from .collections.reports import *

from datetime import datetime


class DailyActivity(object):
  def __init__(self, uid, date):
    self.uid, self.date = uid, date

  def get_data(self):
    try:
      datetime.strptime(self.date, "%Y-%m-%d")
    except:
      return {
        'success'         : False,
        'message'         : 'Incorrect date format',
        'data'            : None
      }
    else:
      return self.__data()

  def __data(self):
    report, count = [], 0 
    data_from_db = Reports.objects(
      user_id = self.uid, 
      date = datetime.strptime(self.date, "%Y-%m-%d") 
    )
    for item in data_from_db: 
      report.append(self.__form(item, self.date) )
      count += item.real_hours 
    return {
      'success'         : True,
      'message'         : 'OK',
      'data'            : {
        'expectedHours'   : 8,
        'actualHours'     : count if count != 0 else None,
        'date'            : self.__convert(self.date),
        'day'             : report if len(report) != 0 else None
      }
    }

  def __form(self, item, date_text):
    prt = ProjectTasks.objects(id = item.project_task_id)[0]
    return {
      'projectId'       : Projects.objects(id = prt.project_id)[0].project_id,
      'projectName'     : Projects.objects(id = prt.project_id)[0].name,
      'projectTask'     : prt.name,
      'startTime'       : item.start_time,
      'endTime'         : item.end_time,
      'realHours'       : item.real_hours,
      'invoicedHours'   : None if item.invoiced_hours == 0 else item.invoiced_hours,
      'reportedHours'   : None if item.reported_hours == 0 else item.reported_hours
    }

  def __convert(self, date_text): # from 2013-08-15 to 08/15/2013
    temp = date_text.split('-')
    return "{0}/{1}/{2}".format(temp[2], temp[1], temp[0])
