from flask import Flask, render_template, redirect
import firebase_admin
from firebase_admin import credentials, db
import random

app = Flask(__name__)

# FIREBASE
cred = credentials.Certificate("firebase.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://cassino-online-e7281-default-rtdb.firebaseio.com'
})

# HOME
@app.route("/")
def home():
    saldo = db.reference("usuarios/Washington/saldo").get()
    if saldo is None:
        saldo = 100
        db.reference("usuarios/Washington/saldo").set(saldo)

    return render_template("index.html", saldo=saldo)

# SLOT
@app.route("/slot")
def slot():
    ref = db.reference("usuarios/Washington/saldo")
    saldo = ref.get() or 100

    ganho = random.choice([0, 10, 20, 50, 100])
    saldo += ganho

    ref.set(saldo)

    return redirect("/")

if __name__ == "__main__":
    app.run()
