from flask import Flask, request, jsonify
import random
from datetime import datetime

app = Flask(__name__)
app.secret_key = "segredo123"

# 🔐 Config
PIX = "12074966423"

usuarios_vip = ["admin", "cliente1", "vip"]

# 📊 Ativos
ativos = [
    "BTC/USD", "ETH/USD", "EUR/USD", "GBP/USD",
    "USD/JPY", "AUD/USD", "NZD/USD", "USD/CAD"
]

# ⏱ Tempos
tempos = ["1 min", "3 min", "5 min", "15 min"]

# 📈 Estratégias
estrategias = [
    "📊 Tendência forte confirmada (EMA + RSI)",
    "📉 Reversão em zona de suporte",
    "📈 Rompimento de resistência",
    "📊 Mercado lateral (pullback)",
    "📉 Sobrecompra (RSI > 70)",
    "📈 Sobrevenda (RSI < 30)"
]

# 🔍 Força do sinal
forca = ["🔥 FORTE", "⚡ MÉDIO", "⚠️ FRACO"]

# 🎯 Probabilidade
probabilidade = ["82%", "85%", "88%", "90%", "92%"]


def gerar_sinal():
    ativo = random.choice(ativos)
    direcao = random.choice(["COMPRA", "VENDA"])
    tempo = random.choice(tempos)
    estrategia = random.choice(estrategias)
    nivel = random.choice(forca)
    chance = random.choice(probabilidade)

    horario = datetime.now().strftime("%H:%M:%S")

    return f"""
🚀 SINAL VIP PRO

📊 Ativo: {ativo}
📈 Direção: {direcao}
⏱ Expiração: {tempo}
🎯 Probabilidade: {chance}
{nivel}

🧠 Análise:
{estrategia}

⏰ Horário: {horario}

⚠️ Use gerenciamento de risco
💰 Entrada recomendada: 2% da banca
"""


def analisar_mercado():
    return """
🧠 ANÁLISE DO MERCADO

📊 Tendência geral: Alta
📈 Força: Moderada
📉 Correção possível

🔎 Indicadores:
- RSI: 63 (neutro)
- EMA: alinhadas para compra
- Volume: crescente

📌 Conclusão:
Mercado com viés de COMPRA
"""


def responder(msg):
    msg = msg.lower()

    if "sinal" in msg:
        return gerar_sinal()

    elif "analisar" in msg:
        return analisar_mercado()

    elif "estrategia" in msg:
        return """
📊 ESTRATÉGIA PRO

✔️ Tendência
✔️ Suporte e resistência
✔️ Confirmação de vela
✔️ Volume
✔️ RSI + EMA

🎯 Entrada sempre com confirmação
"""

    elif "vip" in msg:
        return f"""
🔒 ACESSO VIP

💰 Chave PIX:
{PIX}

Após pagamento envie comprovante.
"""

    else:
        return "Digite: sinal | analisar | estrategia | vip"


# 🌐 Rotas
@app.route("/")
def home():
    return """
    <h2>🤖 IA Trader VIP PRO</h2>
    <form action="/chat" method="post">
        <input name="msg" placeholder="Digite aqui..." />
        <button type="submit">Enviar</button>
    </form>
    """


@app.route("/chat", methods=["POST"])
def chat():
    msg = request.form.get("msg")
    resposta = responder(msg)

    return f"""
    <h3>Você: {msg}</h3>
    <h3>Bot: {resposta}</h3>
    <a href="/">Voltar</a>
    """


if __name__ == "__main__":
    app.run()
