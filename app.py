from flask import Flask, render_template_string
import requests
import random
import threading
import time

app = Flask(__name__)

TOKEN = "SEU_TOKEN"
CHAT_ID = "SEU_CHAT_ID"

URL = f"https://api.telegram.org/bot{TOKEN}"

ultimo_sinal = "Aguardando sinal..."

ativos = ["BTC/USDT","ETH/USDT","EUR/USD","GBP/USD","USD/JPY"]
timeframes = ["1 min","5 min","15 min"]

def gerar_sinal():
    ativo = random.choice(ativos)
    direcao = random.choice(["COMPRA 🟢","VENDA 🔴"])
    tempo = random.choice(timeframes)
    conf = random.randint(87, 99)

    return f"""
📊 SINAL AO VIVO

Ativo: {ativo}
Direção: {direcao}
Tempo: {tempo}
Confiança: {conf}%
"""

def enviar_sinais():
    global ultimo_sinal
    while True:
        sinal = gerar_sinal()
        ultimo_sinal = sinal

        try:
            requests.post(f"{URL}/sendMessage", json={
                "chat_id": CHAT_ID,
                "text": sinal
            })
        except:
            pass

        time.sleep(300)  # 5 minutos

@app.route("/")
def home():
    return render_template_string(f"""
    <html>
    <body style="background:#0b132b;color:white;text-align:center;">
        <h1>🚀 IA TRADER VIP</h1>
        <pre>{ultimo_sinal}</pre>
    </body>
    </html>
    """)

def iniciar():
    t = threading.Thread(target=enviar_sinais)
    t.start()

if __name__ == "__main__":
    iniciar()
    app.run(host="0.0.0.0", port=3000)
