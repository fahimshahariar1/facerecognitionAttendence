import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://facerecogrtdb-test-default-rtdb.firebaseio.com/"
})

ref = db.reference('Students')

data = {
    "190201370":
        {
            "name": "Fahim Shahariar",
            "major": "Comp. Sci.",
            "starting_year": 2019,
            "total_attendance": 8,
            "standing": "Good",
            "last_attendance_time": "2023-03-04 09:00:00"
        },
    "190201365":
        {
            "name": "Faiyaz Ashrafie",
            "major": "Comp. Sci.",
            "starting_year": 2019,
            "total_attendance": 10,
            "standing": "Good",
            "last_attendance_time": "2023-03-04 09:00:00"
        },
    "190201321":
        {
            "name": "Sajan Ahmed",
            "major": "Comp. Sci.",
            "starting_year": 2019,
            "total_attendance": 6,
            "standing": "Okay",
            "last_attendance_time": "2023-03-04 09:00:00"
        },
    "190201852":
        {
            "name": "Emily Blunt",
            "major": "English",
            "starting_year": 2019,
            "total_attendance": 2,
            "standing": "Bad",
            "last_attendance_time": "2023-03-04 09:00:00"
        },
    "190201963":
        {
            "name": "Elon Musk",
            "major": "Business",
            "starting_year": 2019,
            "total_attendance": 3,
            "standing": "Bad",
            "last_attendance_time": "2023-03-04 09:00:00"
        }

}

for key, value in data.items():
    ref.child(key).set(value)
