from app import db, bcrypt
from datetime import datetime
from re import compile

class Users(db.Document):
  user_id = db.IntField(min_value = 0, max_value = 9999, required = True)
  name = db.StringField(
    regex         = compile("^[a-z]{5,}$"), 
    required      = True,
    unique        = True
  )
  pword = db.StringField(min_length = 8, required = True)
  full_name = db.StringField(required = True)
  created_at = db.DateTimeField(default = datetime.now(), required = True)

  def is_authenticated(self):
    return True

  def is_active(self):
    return True

  def is_anonymous(self):
    return False

  def get_id(self):
    return unicode(self.id)

  def set_password(self):
    self.validate()
    self.pword = bcrypt.generate_password_hash(self.pword)

  def check_password(self, pw_typed):
    return bcrypt.check_password_hash(self.pword, pw_typed)

  @staticmethod
  def check_credentials(uname, upass):
    temp = Users.objects(name = uname)
    user = None if len(temp) == 0 else temp[0] 
    if not user or not user.check_password(upass):
      return [{
        'success'     : False,
        'message'     : 'Invalid username/password combination',
        'data'        : None
      }, None]
    else:
      return [{
        'success'     : True,
        'message'     : 'OK', 
        'data'        : None
      }, user]

  @staticmethod
  def get_info(user):
    return {
      'success'       : True,
      'message'       : 'OK',
      'data'          : {
        'userId'        : user.user_id,
        'userName'      : user.name,
        'userFullName'  : user.full_name
      }
    }
