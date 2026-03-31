from flask import Flask, request, jsonify

app = Flask(__name__)

def responder(msg):
    msg = msg.lower()

    if "comprar" in msg or "preço" in msg:
        return "Plano básico R$10 | Premium R$25 💸 PIX: 120.749.664-23"

    elif "trade" in msg:
        return "📊 BTC/USDT\nEntrada: 61.200\nSaída: 62.000\nStop: 60.800"

    elif "oi" in msg or "olá" in msg:
        return "Fala 👋\nDigite:\n1 comprar 🛒\n2 trade 📊"

    else:
        return "Digite 1 ou 2 😉"

@app.route('/')
def home():
    return "Servidor online 🚀"

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.get_json()
    msg = data.get("msg", "")
    resposta = responder(msg)
    return jsonify({"resposta": resposta})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
