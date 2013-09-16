from app import db
from datetime import datetime

class ProjectsAttached(db.Document):
  user_id = db.ObjectIdField(required = True)
  project_id = db.ObjectIdField(required = True)
  created_at = db.DateTimeField(default = datetime.now(), required = True)
