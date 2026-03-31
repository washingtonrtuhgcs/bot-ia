from flask import Flask, request, jsonify

app = Flask(__name__)

def responder(msg):
    msg = msg.lower().strip()

    if msg == "1" or "comprar" in msg:
        return "🛒 Planos:\nBásico: R$10\nPremium: R$25\n\nPIX: 120.749.664-23 💸"

    elif msg == "2" or "trade" in msg:
        return "📊 Sinal:\nBTC/USDT\nEntrada: 61.200\nSaída: 62.000\nStop: 60.800"

    elif "oi" in msg or "olá" in msg:
        return "Fala 👋\nDigite:\n1 comprar 🛒\n2 trade 📊"

    else:
        return "Digite:\n1 🛒 Comprar\n2 📊 Trade"

@app.route('/')
def home():
    return '''
    <html>
    <body style="background:#0f172a;color:white;text-align:center;font-family:Arial">
    <h2>🤖 Chat IA</h2>
    <div id="chat"></div>
    <input id="msg" placeholder="Digite..." />
    <button onclick="enviar()">Enviar</button>

    <script>
    async function enviar(){
        let texto = document.getElementById("msg").value;
        if(!texto) return;

        let chat = document.getElementById("chat");
        chat.innerHTML += "<p><b>Você:</b> "+texto+"</p>";

        let res = await fetch("/api/chat",{
            method:"POST",
            headers:{"Content-Type":"application/json"},
            body:JSON.stringify({msg:texto})
        });

        let data = await res.json();
        chat.innerHTML += "<p><b>Bot:</b> "+data.resposta+"</p>";
    }
    </script>
    </body>
    </html>
    '''

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.get_json()
    msg = data.get("msg", "")
    resposta = responder(msg)
    return jsonify({"resposta": resposta})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
