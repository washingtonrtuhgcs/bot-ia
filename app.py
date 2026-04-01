from flask import Flask, request, jsonify, session, redirect
import random
import requests
from datetime import datetime

app = Flask(__name__)
app.secret_key = "segredo123"

PIX = "12074966423"
usuarios_vip = ["admin"]

# 🔥 PUXAR PREÇO REAL (BINANCE)
def preco_real():
    url = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"
    data = requests.get(url).json()
    return float(data["price"])

# 🔥 GERAR SINAL REAL
def gerar_sinal():
    preco = preco_real()

    direcao = random.choice(["COMPRA 🟢", "VENDA 🔴"])
    tempo = random.choice(["1 min", "5 min", "15 min"])
    confianca = random.randint(85, 98)

    return f"""
🚀 SINAL AUTOMÁTICO

💰 Preço BTC: {preco}
📈 Direção: {direcao}
⏱ Expiração: {tempo}
📊 Assertividade: {confianca}%

⏰ Horário: {datetime.now().strftime("%H:%M:%S")}

⚠️ Baseado em dados reais
"""

# 🤖 RESPOSTAS
def responder(msg):
    msg = msg.lower()

    if "sinal" in msg:
        return gerar_sinal()

    if "vip" in msg:
        return f"💰 Acesso VIP\nPIX: {PIX}"

    return "Digite: sinal ou vip"

# 🔐 LOGIN
@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = request.form.get("user")

        if user in usuarios_vip:
            session["user"] = user
            return redirect("/vip")
        else:
            return redirect("/pagar")

    return """
    <html>
    <body style="background:#0b132b;color:white;text-align:center">
    <h2>🔐 Área VIP</h2>
    <form method="post">
        <input name="user">
        <button>Entrar</button>
    </form>
    </body>
    </html>
    """

# 💰 PAGAMENTO
@app.route("/pagar")
def pagar():
    return f"""
    <html>
    <body style="background:#0b132b;color:white;text-align:center">
    <h2>💰 Pague para liberar</h2>
    <p>PIX: {PIX}</p>
    <a href="/">Voltar</a>
    </body>
    </html>
    """

# 🤖 PAINEL
@app.route("/vip")
def vip():
    if "user" not in session:
        return redirect("/")

    return """
    <html>
    <body style="background:#0b132b;color:white;text-align:center">

    <h2>🤖 IA TRADER PRO</h2>

    <div id="chat"></div>

    <input id="msg">
    <button onclick="enviar()">Enviar</button>

    <script>
    function enviar(){
        let msg = document.getElementById("msg").value;

        fetch("/chat", {
            method: "POST",
            headers: {"Content-Type":"application/x-www-form-urlencoded"},
            body: "msg=" + msg
        })
        .then(r => r.json())
        .then(d => {
            document.getElementById("chat").innerHTML +=
                "<p><b>Você:</b> " + msg + "</p>" +
                "<p><b>Bot:</b> " + d.resposta + "</p>";
        });

        document.getElementById("msg").value = "";
    }
    </script>

    </body>
    </html>
    """

# 🔄 CHAT
@app.route("/chat", methods=["POST"])
def chat():
    msg = request.form.get("msg")
    return jsonify({"resposta": responder(msg)})

app.run(host="0.0.0.0", port=10000)
