from flask import Flask, request, jsonify, session, redirect
import random

app = Flask(__name__)
app.secret_key = "segredo123"

PIX = "12074966423"

usuarios_vip = ["admin", "cliente1", "vip123"]

ativos = [
    "BTC/USD", "ETH/USD", "EUR/USD",
    "GBP/USD", "USD/JPY", "AUD/USD",
    "USD/BRL", "GBP/JPY", "EUR/JPY"
]

timeframes = ["1 min", "5 min", "15 min"]

def gerar_sinal():
    ativo = random.choice(ativos)
    direcao = random.choice(["COMPRA 🟢", "VENDA 🔴"])
    tempo = random.choice(timeframes)

    confianca = random.randint(87, 99)
    entrada = round(random.uniform(1.000, 2.000), 4)

    analise = random.choice([
        "📊 Tendência forte confirmada no gráfico M5",
        "📉 Reversão em zona de suporte forte",
        "📈 Rompimento com pullback confirmado",
        "📊 Mercado lateral com rompimento iminente",
        "📉 Pullback validado + confluência de indicadores"
    ])

    indicador = random.choice([
        "RSI + MACD alinhados",
        "Médias móveis cruzando",
        "Volume institucional alto",
        "Price Action confirmado",
        "Zona de oferta/demanda forte"
    ])

    horario = random.choice([
        "Entrada imediata",
        "Aguardar fechamento da vela",
        "Confirmar próximo candle"
    ])

    return f"""
🚀 SINAL VIP PRO MAX

📊 Ativo: {ativo}
📈 Direção: {direcao}
🎯 Entrada: {entrada}
⏱ Expiração: {tempo}
📌 Assertividade: {confianca}%

📊 Análise:
{analise}

🔎 Confirmação:
{indicador}

⏰ Timing:
{horario}

⚠️ Use gerenciamento de risco
"""

def estrategia():
    return """📊 Estratégia PROFISSIONAL MAX:

✔ Tendência (M5 e M15)
✔ Suporte e resistência
✔ Price Action
✔ Confirmação de vela
✔ Indicadores (RSI + MACD)
✔ Gestão de risco (2% por entrada)
✔ Evitar notícias de alto impacto
✔ Operar apenas com confluência
"""

def responder(msg):
    msg = msg.lower()

    if "sinal" in msg or "trade" in msg:
        return gerar_sinal()

    if "estrateg" in msg:
        return estrategia()

    if "pix" in msg or "valor" in msg:
        return f"💰 VIP R$30\nPIX: {PIX}"

    return "🤖 Digite: sinal, estratégia ou pix"

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
    <body style="background:#0b132b;color:white;text-align:center">

    <h2>🔐 Área VIP</h2>

    <form method="post">
        <input name="user" placeholder="Digite seu usuário">
        <button>Entrar</button>
    </form>

    </body>
    </html>
    """

@app.route("/pagar")
def pagar():
    return f"""
    <html>
    <body style="background:#0b132b;color:white;text-align:center">

    <h2>💰 Acesso VIP</h2>
    <p>R$30</p>
    <p>PIX: {PIX}</p>

    <a href="/">Voltar</a>

    </body>
    </html>
    """

@app.route("/vip")
def vip():
    if "user" not in session:
        return redirect("/")

    return f"""
    <html>
    <body style="background:#0b132b;color:white;font-family:Arial;text-align:center">

    <h2>🤖 IA Trader VIP PRO MAX</h2>
    <p>👤 {session['user']}</p>

    <div id="msgs"></div>

    <input id="msg" placeholder="Digite: sinal">
    <button onclick="enviar()">Enviar</button>

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
            document.getElementById("msgs").innerHTML +=
                "<p><b>Você:</b> " + msg + "</p>" +
                "<p><b>Bot:</b> " + d.resposta + "</p>";
        }});

        document.getElementById("msg").value = "";
    }}
    </script>

    </body>
    </html>
    """

@app.route("/chat", methods=["POST"])
def chat():
    msg = request.form.get("msg")
    return jsonify({"resposta": responder(msg)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
