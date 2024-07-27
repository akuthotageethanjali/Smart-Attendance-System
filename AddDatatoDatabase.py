import firebase_admin
from firebase_admin import credentials
from firebase_admin import db


cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL':"https://faceattendancerealtime-dd5e5-default-rtdb.firebaseio.com/"
})
ref = db.reference('Students')
data = {
    "321654":
        {
            "name": "Bhoomika",
            "course": "b.tech",
            "starting_year": 2021,
            "total_attendance": 7,
            "gender": "f",
            "year": 3,
            "mark":"absent",
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "852741":
        {
            "name": "Akshitha",
            "course": "b.tech",
            "starting_year": 2022,
            "total_attendance": 12,
            "gender": "f",
            "year": 3,
            "mark":"absent",
            "last_attendance_time": "2022-11-11 00:54:34"
        },
    "963852":
        {
            "name": "geetha",
            "course": "b.tech",
            "starting_year": 2021,
            "total_attendance": 7,
            "gender": "f",
            "year": 3,
            "mark":"absent",
            "last_attendance_time": "2022-06-11 00:54:34"
        },
    "769273":
       {
             "name": "sahiti",
             "course": "b.tech",
             "starting_year": 2021,
             "total_attendance": 10,
             "gender": "f",
             "year": 3,
             "mark": "absent",
             "last_attendance_time": "2022-12-10 00:54:34"
        },
    "367482":
        {
            "name": "Ramya",
            "course": "b.tech",
            "starting_year": 2021,
            "total_attendance": 10,
            "gender": "f",
            "year": 3,
            "mark":"absent",
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "568215":
        {
            "name": "sahithya",
            "course": "b.tech",
            "starting_year": 2021,
            "total_attendance": 7,
            "gender": "f",
            "year": 3,
            "mark":"absent",
            "last_attendance_time": "2022-12-10 00:54:34"
        },
    "672381":
        {
            "name": "Sai charan",
            "course": "b.tech",
            "starting_year": 2021,
            "total_attendance": 7,
            "gender": "m",
            "year": 3,
            "mark":"absent",
            "last_attendance_time": "2022-06-18 00:50:00"
        },
    "769573":
        {
            "name": "Sreeja",
            "course": "b.tech",
            "starting_year": 2021,
            "total_attendance": 7,
            "gender": "f",
            "year": 3,
            "mark":"absent",
            "last_attendance_time": "2022-12-16 00:54:20"
        },
    "824567":
        {
            "name": "Roshan",
            "course": "b.tech",
            "starting_year": 2021,
            "total_attendance": 12,
            "gender": "m",
            "year": 3,
            "mark":"absent",
            "last_attendance_time": "2022-06-17 00:50:34"
        },
    "967234":
        {
            "name": "Navya",
            "course": "b.tech",
            "starting_year": 2021,
            "total_attendance": 7,
            "gender": "f",
            "year": 3,
            "mark":"absent",
            "last_attendance_time": "2022-12-13 00:24:34"
        },
}
for key, value in data.items():
    ref.child(key).set(value)