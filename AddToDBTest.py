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
        self.setWindowTitle('Add Data to Firebase')
        self.initUI()

    def initUI(self):
        # Create labels and input fields for data
        self.name_label = QLabel('Name:')
        self.name_input = QLineEdit()
        self.age_label = QLabel('Age:')
        self.age_input = QLineEdit()

        # Create a button to add data to Firebase
        self.add_data_button = QPushButton('Add Data')
        self.add_data_button.clicked.connect(self.add_data)

        # Create a layout for the window
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.name_label)
        self.layout.addWidget(self.name_input)
        self.layout.addWidget(self.age_label)
        self.layout.addWidget(self.age_input)
        self.layout.addWidget(self.add_data_button)
        self.setLayout(self.layout)

    def add_data(self):
        # Get the data from the input fields
        name = self.name_input.text()
        age = int(self.age_input.text())

        # Create a new node with the data in the Firebase Realtime Database
        ref = db.reference('people')
        new_person_ref = ref.push()
        new_person_ref.set({
            'name': name,
            'age': age
        })

        # Clear the input fields after data is added
        self.name_input.setText('')
        self.age_input.setText('')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = AddDataWindow()
    window.show()
    sys.exit(app.exec_())
