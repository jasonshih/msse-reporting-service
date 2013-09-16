#
# MongoDB Collections
#

from .collections.projects import *
from .collections.project_tasks import *
from .collections.projects_attached import *

from datetime import datetime


class ProjectList(object):
  def get_data(self, uid):
    data_from_db, report = ProjectsAttached.objects(user_id = uid), []      
    for item in data_from_db:
      report.append(self.__form(item) )
    return {
      'success'       : True,
      'message'       : 'OK',
      'data'          : report if len(report) != 0 else None
    }

  def __form(self, data):
    tasks, task_info = ProjectTasks.objects(project_id = data.project_id), []
    for item in tasks:
      task_info.append({
        'taskId'        : item.task_id,
        'taskName'      : item.name
      })   
    return {     
      'projectId'     : Projects.objects(id = data.project_id)[0].project_id,
      'projectName'   : Projects.objects(id = data.project_id)[0].name,
      'projectTasks'  : task_info
    }
