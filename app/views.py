from flask import request, jsonify, make_response 
from flask.ext.login import login_user, logout_user, current_user, login_required
from app import app, lm
from models import *


@lm.user_loader
def load_user(user_id):
  user = Users.objects(id = user_id)
  return None if len(user) == 0 else user[0]


@lm.unauthorized_handler
def unauthorized():
  return make_response(jsonify({
    'success'     : False,
    'message'     : 'Unauthorized access',
    'data'        : None
  }), 401)


@app.route('/checkVersion', methods = ['POST'])
def check_version():
  client_type = request.json.get('clientType')
  client_version = request.json.get('clientVersion')
  report = Versions.check(client_type, client_version)
  return jsonify(report)


@app.route('/login', methods = ['POST'])
def login():
  if current_user.is_authenticated():
    return make_response(jsonify({
      'success'     : False,
      'message'     : 'Re-Authentic conflict',
      'data'        : None
    }), 400)
  uname, upass = request.json.get('username'), request.json.get('password')
  report, user = Users.check_credentials(uname, upass)
  if user:
    login_user(user)
  return jsonify(report)


@app.route('/logout', methods = ['GET'])
@login_required
def logout():
  logout_user()
  return jsonify({
    'success'     : True,
    'message'     : 'Signed out successfully',
    'data'        : None 
  })


@app.route('/day/<date>', methods = ['GET','PUT'])
@login_required
def get_day_activity(date):
  report = DailyActivity(current_user.get_id(), date).get_data()
  return jsonify(report)


@app.route('/week/<date>', methods = ['GET'])
@login_required
def get_week_activity(date):
  report = WeeklyActivity(current_user.get_id(), date).get_data()
  return jsonify(report)


@app.route('/projects', methods = ['GET'])
@login_required
def get_attached_projects():
  report = ProjectList().get_data(current_user.get_id() )
  return jsonify(report)


@app.route('/user/info', methods = ['GET'])
@login_required
def get_info():
  report = Users.get_info(current_user)
  return jsonify(report)
