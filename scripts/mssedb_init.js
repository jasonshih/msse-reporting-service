var connection = new Mongo('localhost:27017');
var db = connection.getDB('mssedb');

/* MongoDB Collections - Users */
db.users.insert( {user_id: 311, name: 'ppetr', full_name: 'Pavlo Petryk', 
  pword: '$2a$12$fJZxb.uWqSJELiEDfX43TeqqlPyDR8na9DOsfCIUf.aQYfTs1xxI.', created_at: new Date} );
db.users.insert( {user_id: 1288, name: 'admin', full_name: 'Andriy Padun',
  pword: '$2a$12$Fbuef248YzofNoXLiIMVcOBLO6eRSX7MCJUUumG0tnusxaC7nrajK', created_at: new Date} );
db.users.insert( {user_id: 3178, name: 'qwerty', full_name: 'Julya Tymo',
  pword: '$2a$12$sNr1QnZGxz5aO0byaYL2a.z9lCAWiqkJha5ACoX5eL3l4DR900P4u', created_at: new Date} );


/* MongoDB Collections - Projects */
db.projects.insert( {project_id: 1089, name: "Large Web Project", description: "", created_at: new Date} );
db.projects.insert( {project_id: 276, name: "Tiny Mobile Project", description: "", created_at: new Date } );


/* Useful Variables & Functions */
var u1 = db.users.find( {user_id: 1288} ).toArray()[0]['_id'];
var u2 = db.users.find( {user_id: 311} ).toArray()[0]['_id'];
var u3 = db.users.find( {user_id: 3178} ).toArray()[0]['_id'];
var pr1 = db.projects.find( {project_id: 1089} ).toArray()[0]['_id'];
var pr2 = db.projects.find( {project_id: 276} ).toArray()[0]['_id'];


/* MongoDB Collections - ProjectTasks */
db.project_tasks.insert( {project_id: pr1, task_id: 12, name: "Creating User Interface", 
  description: "", created_at: new Date} );
db.project_tasks.insert( {project_id: pr1, task_id: 105, name: "Determinating Database Scheme",
  description: "", created_at: new Date} );
db.project_tasks.insert( {project_id: pr1, task_id: 86, name: "Optimization Server-Side App",
  description: "", created_at: new Date} );
db.project_tasks.insert( {project_id: pr2, task_id: 12, name: "Creating User Interface",
  description: "", created_at: new Date} );
db.project_tasks.insert( {project_id: pr2, task_id: 105, name: "Determinating Database Scheme",
  description: "", created_at: new Date} );


/* Useful Variables & Functions */
var prt1 = db.project_tasks.find( {project_id: pr1, task_id: 12} ).toArray()[0]['_id'];
var prt2 = db.project_tasks.find( {project_id: pr1, task_id: 105} ).toArray()[0]['_id'];
var prt3 = db.project_tasks.find( {project_id: pr1, task_id: 086} ).toArray()[0]['_id'];
var prt4 = db.project_tasks.find( {project_id: pr2, task_id: 12} ).toArray()[0]['_id'];
var prt5 = db.project_tasks.find( {project_id: pr2, task_id: 105} ).toArray()[0]['_id'];

function getDateTimezoneDiff(year, month, day){
  d = new Date(year, month, day);
  offset = - (d.getTimezoneOffset() / 60);
  d.setHours(offset);
  return d;
}


/* Mongo Collections - ProjectsAttached */
db.projects_attached.insert( {user_id: u1, project_id: pr1, created_at: new Date} )
db.projects_attached.insert( {user_id: u1, project_id: pr2, created_at: new Date} )
db.projects_attached.insert( {user_id: u2, project_id: pr2, created_at: new Date} )
db.projects_attached.insert( {user_id: u3, project_id: pr1, created_at: new Date} ) 


/* MongoDB Collections - Reports */
db.reports.insert( {user_id: u1, project_task_id: prt1, date: getDateTimezoneDiff(2013, 7, 15), real_hours: 5, 
  invoiced_hours: 0, reported_hours: 0, start_time: "09:00", end_time: "14:00", created_at: new Date} );
db.reports.insert( {user_id: u1, project_task_id: prt3, date: getDateTimezoneDiff(2013, 7, 15), real_hours: 3, 
  invoiced_hours: 0, reported_hours: 0, start_time: "14:00", end_time: "17:00", created_at: new Date} );
db.reports.insert( {user_id: u1, project_task_id: prt3, date: getDateTimezoneDiff(2013, 7, 16), real_hours: 1, 
  invoiced_hours: 0, reported_hours: 0, start_time: "09:00", end_time: "10:00", created_at: new Date} );
db.reports.insert( {user_id: u1, project_task_id: prt4, date: getDateTimezoneDiff(2013, 7, 16), real_hours: 5, 
  invoiced_hours: 0, reported_hours: 0, start_time: "10:00", end_time: "15:00", created_at: new Date} );
db.reports.insert( {user_id: u1, project_task_id: prt2, date: getDateTimezoneDiff(2013, 7, 16), real_hours: 2, 
  invoiced_hours: 0, reported_hours: 0, start_time: "15:00", end_time: "17:00", created_at: new Date} );
db.reports.insert( {user_id: u1, project_task_id: prt5, date: getDateTimezoneDiff(2013, 7, 19), real_hours: 8, 
  invoiced_hours: 0, reported_hours: 0, start_time: "09:00", end_time: "17:00", created_at: new Date} );
db.reports.insert( {user_id: u2, project_task_id: prt2, date: getDateTimezoneDiff(2013, 7, 21), real_hours: 6, 
  invoiced_hours: 0, reported_hours: 0, start_time: "09:00", end_time: "15:00", created_at: new Date} );
db.reports.insert( {user_id: u2, project_task_id: prt4, date: getDateTimezoneDiff(2013, 7, 21), real_hours: 2, 
  invoiced_hours: 0, reported_hours: 0, start_time: "15:00", end_time: "17:00", created_at: new Date} );


/* MongoDB Collections - Versions */
db.versions.insert( {client_type: 'android', client_version: '1.0.0', server_version: '2.0.0', created_at: new Date} )
