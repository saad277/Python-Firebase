#pip install pyrebase
import pyrebase
config = {
    "apiKey": "AIzaSyCmeM4Kyk9giFFksxCIso7kEfozDNQCaqU",
    "authDomain": "native-firebase-6eb6c.firebaseapp.com",
    "databaseURL": "https://native-firebase-6eb6c.firebaseio.com",
    "projectId": "native-firebase-6eb6c",
    "storageBucket": "native-firebase-6eb6c.appspot.com",
    "messagingSenderId": "877280431920",
    "appId": "1:877280431920:web:cd151a69dcf23a50fc42f5"
  };

email="python@gmail.com";
password="123456";


firebase = pyrebase.initialize_app(config)

storage=firebase.storage();

auth=firebase.auth();

user = auth.sign_in_with_email_and_password(email, password)

#print(user['idToken'])

#user = auth.refresh(user['refreshToken'])   refresh tokens

path_on_cloud="python/images";              #name saved to storage

path_local="Capture.PNG"

x=storage.child(path_on_cloud).put(path_local)

url=storage.child(path_on_cloud).get_url(user['idToken'])

print(url)

