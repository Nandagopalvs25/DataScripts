import time
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import csv
# Use a service account.
cred = credentials.Certificate('firestore/serviceAccountKey2.json')

app = firebase_admin.initialize_app(cred)

db = firestore.client()

#reading a list of ids and deleting it
with open('firestore/sty.csv', mode='r') as file:
     csvr= csv.reader(file)
     for line in csvr:
          print(line[0])
          doc= db.collection("hestia-24").document(line[0])
          doc.delete()
          time.sleep(2)




#print("Deleted")
#doc.delete()



