from flask import Flask, render_template_string
import requests
import random
import threading
import time
import os

app = Flask(__name__)

TOKEN = "8635303327:AAF9UHY5R4dM_PqPv2675OEO1yOg31GaJMc"
CHAT_ID = "5778693963"

URL = f"https://api.telegram.org/bot{TOKEN}"

ultimo_sinal = "Aguardando sinal..."

def enviar_mensagem(msg):
    try:
        requests.get(f"{URL}/sendMessage?chat_id={CHAT_ID}&text={msg}")
    except:
        pass

def gerar_sinais():
    global ultimo_sinal
    while True:
        direcao = random.choice(["COMPRA 🟢", "VENDA 🔴"])
        tempo = random.choice(["1 MIN", "5 MIN"])
        msg = f"SINAL: {direcao} | TEMPO: {tempo}"

        ultimo_sinal = msg
        enviar_mensagem(msg)

        time.sleep(60)

@app.route('/')
def home():
    return render_template_string(f"""
    <h1>BOT ONLINE 🤖</h1>
    <p>{ultimo_sinal}</p>
    """)

def iniciar():
    t = threading.Thread(target=gerar_sinais)
    t.daemon = True
    t.start()

if __name__ == "__main__":
    iniciar()
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
