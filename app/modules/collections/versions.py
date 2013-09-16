from app import db
from datetime import datetime

class Versions(db.Document):
  client_type = db.StringField(required = True)
  client_version = db.StringField(required = True)
  server_version =  db.StringField(required = True)
  created_at = db.DateTimeField(default = datetime.now(), required = True)

  @staticmethod
  def check(client_type, client_version):
    version = Versions.objects(client_type = client_type, client_version = client_version)
    supported = False if len(version) == 0 else True
    server_version = None if supported == False else version[0].server_version
    return {
      'success'       : True,
      'message'       : 'OK',
      'data'          : {
        'clientType'    : client_type,
        'clientVersion' : client_version,
        'supported'     : supported,
        'serverVersion' : server_version
      }
    }
    