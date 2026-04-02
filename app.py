from flask import Flask, request
import requests
import random

app = Flask(__name__)

# 🔐 CONFIG
TOKEN = "SEU_TOKEN_AQUI"
URL = f"https://api.telegram.org/bot{TOKEN}"

usuarios_vip = [123456789]  # coloque seu ID aqui

PIX = "12074966423"

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
📊 SINAL VIP

💰 Ativo: {ativo}
📈 Direção: {direcao}
⏱ Tempo: {tempo}
🔥 Confiança: {confianca}%

🚀 Entre agora!
"""

# 📩 ENVIAR MSG
def enviar(chat_id, texto):
    requests.post(f"{URL}/sendMessage", json={
        "chat_id": chat_id,
        "text": texto
    })

# 🤖 WEBHOOK TELEGRAM
@app.route(f"/{TOKEN}", methods=["POST"])
def bot():
    data = request.json

    if "message" in data:
        chat_id = data["message"]["chat"]["id"]
        texto = data["message"].get("text", "")

        if texto == "/start":
            enviar(chat_id, "🔥 Bem-vindo ao BOT DE SINAIS!\nDigite /vip para acessar")

        elif texto == "/vip":
            if chat_id in usuarios_vip:
                enviar(chat_id, gerar_sinal())
            else:
                enviar(chat_id, f"🔒 Acesso VIP\n\n💳 Pagamento via PIX:\n{PIX}")

    return "ok"

# 🌐 HOME
@app.route("/")
def home():
    return "BOT ONLINE 🚀"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
