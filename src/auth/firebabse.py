import pyrebase

class Fire_Auth:
    def __init__(self):
        super().__init__()

    firebaseConfig={
        'apiKey': "AIzaSyB3eMx3GqqPpytI8rzS-ERXqljevrdQp74",
        'authDomain': "demologin-578df.firebaseapp.com",
        'projectId': "demologin-578df",
        'storageBucket': "demologin-578df.appspot.com",
        'messagingSenderId': "615292014516",
        'appId': "1:615292014516:web:8365ec7211875d05a46ce1",
        'databaseURL':' https://demologin-578df-default-rtdb.firebaseio.com/',
        }

    firebase=pyrebase.initialize_app(firebaseConfig)
    auth=firebase.auth()