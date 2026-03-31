from flask import Flask, request

app = Flask(__name__)

conversa = []

@app.route('/')
def home():
    chat_html = ''
    for i, msg in enumerate(conversa):
        if i % 2 == 0:
            chat_html += f'<p><b>Você:</b> {msg}</p>'
        else:
            chat_html += f'<p><b>Washington IA:</b> {msg}</p>'

    return f'''
    <html>
    <body>
        <h2>💼 Washington IA</h2>
        {chat_html}
        <form action="/chat">
            <input name="msg" placeholder="Digite aqui">
            <button>Enviar</button>
        </form>
    </body>
    </html>
    '''

@app.route('/chat')
def chat():
    msg = request.args.get('msg')
    conversa.append(msg)
    texto = msg.lower()

    if 'oi' in texto:
        resp = "Olá! 👋 Digite 1 para Loja ou 2 para Trade"
    elif msg == '1':
        resp = "🛒 Produtos: Camisa R$50 | Calça R$100"
    elif msg == '2':
        resp = "📈 Trade: digite 'sinal' ou 'estrategia'"
    elif 'sinal' in texto:
        resp = "📊 Tendência de alta"
    elif 'estrategia' in texto:
        resp = "📘 Use stop e controle risco"
    else:
        resp = "❌ Opção inválida"

    conversa.append(resp)
    return '<meta http-equiv="refresh" content="0; url=/">'

app.run(host='0.0.0.0', port=5000)
