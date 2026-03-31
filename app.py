from flask import Flask, request, jsonify

app = Flask(__name__)

def responder(msg):
    msg = msg.lower()

    if "comprar" in msg or "preço" in msg:
        return "🛒 Planos:\nBásico: R$10\nPremium: R$25\n\nPIX: 120.749.664-23 💸"

    elif "trade" in msg:
        return "📊 Sinal:\nBTC/USDT\nEntrada: 61.200\nSaída: 62.000\nStop: 60.800"

    elif "oi" in msg or "olá" in msg:
        return "Fala 👋\nDigite:\n1 comprar 🛒\n2 trade 📊"

    else:
        return "Digite 1 ou 2 😉"

@app.route('/')
def home():
    return '''
    <html>
    <head>
        <title>Chat IA</title>
        <style>
            body { font-family: Arial; background: #0f172a; color: white; text-align: center; }
            #chat { max-width: 400px; margin: auto; background: #1e293b; padding: 10px; border-radius: 10px; height: 400px; overflow-y: auto; }
            .msg { margin: 10px; padding: 8px; border-radius: 8px; }
            .user { background: #22c55e; text-align: right; }
            .bot { background: #334155; text-align: left; }
            input { width: 70%; padding: 10px; }
            button { padding: 10px; background: #22c55e; border: none; }
        </style>
    </head>
    <body>

    <h2>🤖 Chat IA Loja + Trade</h2>

    <div id="chat"></div>

    <input id="msg" placeholder="Digite..." />
    <button onclick="enviar()">Enviar</button>

    <script>
        async function enviar() {
            let input = document.getElementById("msg");
            let texto = input.value;
            if (!texto) return;

            adicionar(texto, "user");

            let res = await fetch("/api/chat", {
                method: "POST",
                headers: {"Content-Type": "application/json"},
                body: JSON.stringify({msg: texto})
            });

            let data = await res.json();
            adicionar(data.resposta, "bot");

            input.value = "";
        }

        function adicionar(texto, tipo) {
            let chat = document.getElementById("chat");
            let div = document.createElement("div");
            div.className = "msg " + tipo;
            div.innerText = texto;
            chat.appendChild(div);
            chat.scrollTop = chat.scrollHeight;
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
