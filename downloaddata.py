import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import csv
# Use a service account.
cred = credentials.Certificate('firestore/serviceAccountKey2.json')

app = firebase_admin.initialize_app(cred)

db = firestore.client()


doc_ref = db.collection("hestia-24").where("type","==","Coordinator").get()



mydicts=[]

for i in doc_ref:
    mydict= i.to_dict()
    mydicts.append(mydict)

header = ["email","event","mobile_no","name","type"]
with open('sty2.csv', 'w',newline='') as file:
    writer = csv.DictWriter(file, fieldnames=header)
    writer.writeheader()
    for row in mydicts:
        writer.writerow(row)  
        

        


    

#doc_ref.set({"first": "Ada", "last": "Lovelace", "born": 1815})
