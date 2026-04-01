from flask import Flask, request, jsonify, session, redirect

app = Flask(__name__)
app.secret_key = "segredo123"

PIX = "12074966423"

usuarios_vip = ["admin", "cliente1", "vip123"]

def gerar_sinal():
    return "🚀 SINAL: BTC/USD → COMPRA ⏱ 5min ⚠️ Use gerenciamento!"

def estrategia():
    return """📊 Estratégia PRO:
✔ Tendência
✔ Suporte e resistência
✔ Confirmação de vela
✔ Gestão de risco"""

def responder(msg):
    msg = msg.lower()

    if "sinal" in msg or "trade" in msg:
        return gerar_sinal()

    if "estrateg" in msg:
        return estrategia()

    if "pix" in msg or "valor" in msg:
        return f"💰 VIP R$30\nPIX: {PIX}"

    return "🤖 Digite: sinal ou estratégia"

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
    <html><body style="background:#0b132b;color:white;text-align:center">
    <h2>🔐 Área VIP</h2>
    <form method="post">
        <input name="user">
        <button>Entrar</button>
    </form>
    </body></html>
    """

@app.route("/pagar")
def pagar():
    return f"""
    <html><body style="background:#0b132b;color:white;text-align:center">
    <h2>💰 Acesso VIP</h2>
    <p>R$30</p>
    <p>PIX: {PIX}</p>
    <a href="/">Voltar</a>
    </body></html>
    """

@app.route("/vip")
def vip():
    if "user" not in session:
        return redirect("/")

    return f"""
    <html>
    <body style="background:#0b132b;color:white;font-family:Arial;text-align:center">

    <h2>🤖 IA Trader VIP</h2>
    <p>👤 {session['user']}</p>

    <div id="msgs"></div>

    <input id="msg">
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

app.run(host="0.0.0.0", port=10000)
