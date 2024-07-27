import firebase_admin
from firebase_admin import credentials, db
import pandas as pd
from openpyxl import load_workbook
import threading

# Initialize the Firebase app
cred = credentials.Certificate('serviceAccountKey.json')
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://faceattendancerealtime-dd5e5-default-rtdb.firebaseio.com/'
})

# Reference to your database path
ref = db.reference('Students')

# Function to update Excel file
'''def update_excel(data):
    df = pd.DataFrame.from_dict(data, orient='index')
    df.to_excel('output.xlsx', index=True)'''
def update_excel(data):
    # Filter the data to include only 'student' and 'marked'
    filtered_data = {key: {'Student': value.get('name'), 'mark': value.get('mark')} for key, value in data.items()}
    df = pd.DataFrame.from_dict(filtered_data, orient='index')
    df.to_excel('output.xlsx', index=True)

# Listener callback function
def listener(event):
    print('Data changed!')
    data = ref.get()
    update_excel(data)

# Attach listener to database reference
ref.listen(listener)

# Keep the script running
threading.Event().wait()