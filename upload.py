import time
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import csv
# Use a service account.
cred = credentials.Certificate('firestore/serviceAccountKey2.json')

app = firebase_admin.initialize_app(cred)

db = firestore.client()


doc_ref = db.collection("hestia-24")
 
with open('firestore/newl.csv', mode='r') as file:
    csv_reader = csv.DictReader(file)
    data_list = []
 
    for row in csv_reader:
        data_list.append(row)
 
# Print the list of dictionaries
for data in data_list:
    doc_ref.document().set(data)
    print(data)
    time.sleep(0.5)
