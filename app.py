from flask import Flask, request
import requests
import os

app = Flask(__name__)

# COLOQUE SEU TOKEN E ID AQUI
TOKEN = "8635303327:AAH5wDWbAz1PAJPccuNdu_5qHszwbx2MOX4"
CHAT_ID = "5778693963"

@app.route("/")
def home():
    return open("index.html").read()

@app.route("/enviar", methods=["POST"])
def enviar():
    data = request.json
    msg = data.get("msg")

    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(url, json={
        "chat_id": CHAT_ID,
        "text": msg
    })

    return "ok"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
