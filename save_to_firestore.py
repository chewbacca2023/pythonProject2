import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import firestore


cred = credentials.Certificate('/Users/josephrambow/PycharmProjects/aim_builder/firebase_config.json')
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://rn-testing-ae88d-default-rtdb.firebaseio.com/'
})
ref = db.reference('prospect')


fire = firestore.client()

doc_ref = fire.collection('prospect').document('contactinfo')

def save_data (email, fname, lname, phone):
    doc_ref.set({
        'email': f'{email}',
        'etype': 'home',
        'firstname': f'{fname}',
        'lastname': f'{lname}',
        'phonenumber': f'{phone}',
        'ptype': 'mobile'
    })
    return

