from flask import Flask, request, jsonify, render_template_string

app = Flask(__name__)

PIX = "120.749.664-23"

html = """
<!DOCTYPE html>
<html>
<head>
<title>IA Trader</title>
<style>
body {
    background: #0f172a;
    color: white;
    font-family: Arial;
}
.chat {
    max-width: 400px;
    margin: auto;
    margin-top: 30px;
}
.msg {
    padding: 10px;
    margin: 5px;
    border-radius: 10px;
}
.user { background: #2563eb; text-align: right; }
.bot { background: #1e293b; }
button {
    padding: 10px;
    margin: 5px;
    border: none;
    border-radius: 8px;
    background: #22c55e;
    color: white;
}
</style>
</head>

<body>
<div class="chat" id="chat">
    <div class="msg bot">Fala 👋 Escolha uma opção:</div>
    <button onclick="send('comprar')">🛒 Comprar</button>
    <button onclick="send('sinal')">📊 Sinais</button>
</div>

<script>
function send(text){
    let chat = document.getElementById("chat");

    chat.innerHTML += `<div class="msg user">${text}</div>`;

    fetch("/chat", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({msg: text})
    })
    .then(res => res.json())
    .then(data => {
        chat.innerHTML += `<div class="msg bot">${data.resposta}</div>`;
        chat.scrollTop = chat.scrollHeight;
    });
}
</script>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(html)

@app.route("/chat", methods=["POST"])
def chat():
    user = request.json.get("msg").lower()

    if "comprar" in user:
        resposta = f"🛒 Planos:\\nBásico: R$10\\nPremium: R$25\\nPIX: {PIX} 💸"
    elif "sinal" in user:
        resposta = "📊 Sinal BTC/USDT\\nEntrada: 61.200\\nSaída: 62.000\\nStop: 60.800"
    else:
        resposta = "🤖 Clique nos botões acima."

    return jsonify({"resposta": resposta})

if __name__ == "__main__":
    app.run()
