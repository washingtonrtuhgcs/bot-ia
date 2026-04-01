from flask import Flask, request, jsonify, session, redirect
import random
from datetime import datetime

app = Flask(__name__)
app.secret_key = "segredo_ultra_123"

# 💰 CONFIG
PIX = "12074966423"
VALOR_VIP = "R$30"

usuarios_vip = ["admin", "vip", "cliente1"]

# 📊 ATIVOS
ativos = [
    "BTC/USD", "ETH/USD", "EUR/USD", "GBP/USD",
    "USD/JPY", "AUD/USD", "USD/BRL", "NZD/USD"
]

tempos = ["1 min", "3 min", "5 min", "15 min"]

estrategias = [
    "📊 Tendência forte confirmada (EMA + RSI)",
    "📉 Reversão em zona de suporte",
    "📈 Rompimento de resistência",
    "📊 Pullback confirmado",
    "📉 Sobrecompra (RSI > 70)",
    "📈 Sobrevenda (RSI < 30)"
]

forca = ["🔥 FORTE", "⚡ MÉDIO", "⚠️ FRACO"]
prob = ["82%", "85%", "88%", "90%", "92%", "95%"]

# 🚀 GERAR SINAL
def gerar_sinal():
    return f"""
🚀 SINAL ULTRA VIP

📊 Ativo: {random.choice(ativos)}
📈 Direção: {random.choice(["COMPRA 🟢", "VENDA 🔴"])}
⏱ Expiração: {random.choice(tempos)}

🎯 Probabilidade: {random.choice(prob)}
{random.choice(forca)}

🧠 Análise:
{random.choice(estrategias)}

⏰ Horário: {datetime.now().strftime("%H:%M:%S")}

⚠️ Use gerenciamento de risco
💰 Entrada recomendada: 2% da banca
"""

# 🧠 ANALISE
def analisar():
    return """
🧠 ANÁLISE DO MERCADO

📊 Tendência: Alta
📈 Força: Moderada
📉 Possível correção

📌 Indicadores:
- RSI: 64
- EMA: alinhadas para compra
- Volume: forte

🎯 Conclusão:
Viés de COMPRA no momento
"""

# 🤖 RESPOSTAS
def responder(msg):
    msg = msg.lower()

    if "sinal" in msg:
        return gerar_sinal()

    elif "analisar" in msg:
        return analisar()

    elif "estrateg" in msg:
        return """
📊 ESTRATÉGIA ULTRA

✔ Tendência
✔ Suporte e resistência
✔ Confirmação de vela
✔ RSI + EMA
✔ Volume

🎯 Entrada sempre com confirmação
"""

    elif "vip" in msg or "pagar" in msg:
        return f"💰 VIP: {VALOR_VIP}\nPIX: {PIX}"

    return "Digite: sinal | analisar | estrategia | vip"

# 🔐 LOGIN
@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = request.form.get("user").lower().strip()

        if user in usuarios_vip:
            session["user"] = user
            return redirect("/vip")
        else:
            return redirect("/pagar")

    return """
    <html>
    <body style="background:#0b132b;color:white;text-align:center;font-family:Arial">

    <h2>🔐 ÁREA VIP</h2>

    <form method="post">
        <input name="user" placeholder="Digite seu usuário" style="padding:10px">
        <br><br>
        <button style="padding:10px">Entrar</button>
    </form>

    </body>
    </html>
    """

# 💰 PAGAMENTO
@app.route("/pagar")
def pagar():
    return f"""
    <html>
    <body style="background:#0b132b;color:white;text-align:center;font-family:Arial">

    <h2>💰 ACESSO VIP</h2>

    <p>Valor: {VALOR_VIP}</p>
    <p>PIX: {PIX}</p>

    <br>
    <a href="/" style="color:white">Voltar</a>

    </body>
    </html>
    """

# 🤖 PAINEL
@app.route("/vip")
def vip():
    if "user" not in session:
        return redirect("/")

    return f"""
    <html>
    <body style="background:#0b132b;color:white;font-family:Arial;text-align:center">

    <h2>🤖 IA TRADER ULTRA</h2>
    <p>👤 {session['user']}</p>

    <div id="chat" style="max-width:500px;margin:auto;text-align:left"></div>

    <input id="msg" placeholder="Digite: sinal" style="width:70%;padding:10px">
    <button onclick="enviar()" style="padding:10px">Enviar</button>

    <script>
    function enviar(){{
        let msg = document.getElementById("msg").value;

        fetch("/chat", {{
            method: "POST",
            headers: {{"Content-Type":"application/x-www-form-urlencoded"}},
            body: "msg=" + msg
        }})
        .then(r => r.json())
        .then(d => {{
            document.getElementById("chat").innerHTML +=
                "<p><b>Você:</b> " + msg + "</p>" +
                "<p><b>Bot:</b><br>" + d.resposta + "</p><hr>";
        }});

        document.getElementById("msg").value = "";
    }}
    </script>

    </body>
    </html>
    """

# 🔄 CHAT
@app.route("/chat", methods=["POST"])
def chat():
    msg = request.form.get("msg")
    return jsonify({"resposta": responder(msg)})

# 🚀 START
app.run(host="0.0.0.0", port=10000)
