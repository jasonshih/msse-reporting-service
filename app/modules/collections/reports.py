from app import db
from datetime import datetime, timedelta

class Reports(db.Document):
  user_id = db.ObjectIdField(required = True)
  project_task_id = db.ObjectIdField(required = True)
  date = db.DateTimeField(required = True)
  real_hours = db.IntField(min_value = 1, max_value = 8, required = True)
  invoiced_hours = db.IntField(min_value = 0, max_value = 8, required = True)
  reported_hours = db.IntField(min_value = 0, max_value = 8, required = True)
  start_time = db.StringField(default = "", required = True)
  end_time = db.StringField(default = "", required = True)
  created_at = db.DateTimeField(default = datetime.now(), required = True)
  