from app import db
from datetime import datetime

class ProjectTasks(db.Document):
  project_id = db.ObjectIdField(required = True)
  task_id = db.IntField(min_value = 0, max_value = 9999, required = True)
  name = db.StringField(required = True)
  description = db.StringField(default = "", required = True)
  created_at = db.DateTimeField(default = datetime.now(), required = True)
