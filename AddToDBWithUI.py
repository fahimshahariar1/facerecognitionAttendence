import sys

import firebase_admin
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout
from firebase_admin import credentials
from firebase_admin import db

# Initialize Firebase Admin SDK with your credentials
cred = credentials.Certificate('serviceAccountKey.json')
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://facerecogrtdb-test-default-rtdb.firebaseio.com/"
})


class AddDataWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Add Data to Database')
        self.initUI()

    def initUI(self):
        # Create labels and input fields for data
        self.student_Id_label = QLabel('Student ID:')
        self.student_Id_input = QLineEdit()
        self.name_label = QLabel('Name:')
        self.name_input = QLineEdit()
        self.major_label = QLabel('Major:')
        self.major_input = QLineEdit()
        self.starting_year_label = QLabel('Starting Year:')
        self.starting_year_input = QLineEdit()
        self.total_attendance_label = QLabel('Total Attendance:')
        self.total_attendance_input = QLineEdit()
        self.standing_label = QLabel('Standing:')
        self.standing_input = QLineEdit()
        self.last_attendance_time_label = QLabel('Last Attendance Time:')
        self.last_attendance_time_input = QLineEdit()

        # Create a button to add data to Firebase
        self.add_data_button = QPushButton('Add Data')
        self.add_data_button.clicked.connect(self.add_data)

        # Create a layout for the window
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.student_Id_label)
        self.layout.addWidget(self.student_Id_input)
        self.layout.addWidget(self.name_label)
        self.layout.addWidget(self.name_input)
        self.layout.addWidget(self.major_label)
        self.layout.addWidget(self.major_input)
        self.layout.addWidget(self.starting_year_label)
        self.layout.addWidget(self.starting_year_input)
        self.layout.addWidget(self.total_attendance_label)
        self.layout.addWidget(self.total_attendance_input)
        self.layout.addWidget(self.standing_label)
        self.layout.addWidget(self.standing_input)
        self.layout.addWidget(self.last_attendance_time_label)
        self.layout.addWidget(self.last_attendance_time_input)
        self.layout.addWidget(self.add_data_button)
        self.setLayout(self.layout)

    def add_data(self):
        # Get the data from the input fields
        student_Id = self.student_Id_input.text()
        name = self.name_input.text()
        major = self.major_input.text()
        starting_year = int(self.starting_year_input.text())
        total_attendance = int(self.total_attendance_input.text())
        standing = self.standing_input.text()
        last_attendance_time = self.last_attendance_time_input.text()

        # Create a new node with the data and date/time in the Firebase Realtime Database
        ref = db.reference('students')
        new_student_ref = ref.push()
        new_student_ref.set({
            student_Id: {
                'name': name,
                'major': major,
                'starting_year': starting_year,
                'total_attendance': total_attendance,
                'standing': standing,
                'last_attendance_time': last_attendance_time,
            }})

        # Clear the input fields after data is added
        self.student_Id_input.setText('')
        self.name_input.setText('')
        self.major_input.setText('')
        self.starting_year_input.setText('')
        self.total_attendance_input.setText('')
        self.standing_input.setText('')
        self.last_attendance_time_input.setText('')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = AddDataWindow()
    window.show()
    sys.exit(app.exec_())
