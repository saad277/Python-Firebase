#pip install firebase_admin

import firebase_admin

from firebase_admin import credentials 

from firebase_admin import firestore 


cred=credentials.Certificate("service_account.json")

firebase_admin.initialize_app(cred)

db=firestore.client();

ref=db.collection("food");

docs=ref.stream()


data=[]

for doc in docs:
    #print(doc.id)
    data.append(doc.to_dict())



print(data[0]['image'])
