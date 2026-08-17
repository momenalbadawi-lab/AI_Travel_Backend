import firebase_admin
import os
import json
from firebase_admin import credentials, firestore


# الاتصال مع Firebase
def initialize_firebase():
    if not firebase_admin._apps:
        firebase_credentials = os.getenv("FIREBASE_CREDENTIALS")

        if firebase_credentials:
            cred_dict = json.loads(firebase_credentials)
            cred = credentials.Certificate(cred_dict)
        else:
            cred = credentials.Certificate("firebase_key.json")

        firebase_admin.initialize_app(cred)

    return firestore.client()


# الاتصال مع Firestore Database
db = initialize_firebase()