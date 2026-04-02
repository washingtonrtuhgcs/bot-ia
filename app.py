from flask import Flask, request
import requests
import random
import threading
import time

app = Flask(__name__)

# 🔐 CONFIG
TOKEN = "SEU_TOKEN_AQUI"
CHAT_ID = "SEU_CHAT_ID_AQUI"

URL = f"https://api.telegram.org/bot{TOKEN}"

ativos = [
    "BTC/USDT", "ETH/USDT", "EUR/USD",
    "GBP/USD", "USD/JPY", "AUD/USD"
]

timeframes = ["1 min", "5 min", "15 min"]

# 🎯 GERAR SINAL
def gerar_sinal():
    ativo = random.choice(ativos)
    direcao = random.choice(["COMPRA 🟢", "VENDA 🔴"])
    tempo = random.choice(timeframes)
    confianca = random.randint(87, 99)

    return f"""
🚨 SINAL AUTOMÁTICO 🚨

💰 Ativo: {ativo}
📈 Direção: {direcao}
⏱ Tempo: {tempo}
🔥 Confiança: {confianca}%

⚠️ Use gerenciamento de risco
"""

# 📩 ENVIAR MSG
def enviar():
    while True:
        msg = gerar_sinal()
        requests.post(f"{URL}/sendMessage", json={
            "chat_id": CHAT_ID,
            "text": msg
        })
        time.sleep(300)  # envia a cada 5 minutos

# 🌐 HOME
@app.route("/")
def home():
    return "BOT AUTOMÁTICO ONLINE 🚀"

# 🔁 INICIAR THREAD
def iniciar_bot():
    t = threading.Thread(target=enviar)
    t.start()

if __name__ == "__main__":
    iniciar_bot()
    app.run(host="0.0.0.0", port=3000)
