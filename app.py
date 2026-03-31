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
    <body style="margin:0;font-family:sans-serif;background:#ece5dd;">

    <div style="background:#075E54;color:white;padding:15px;">
        💼 Washington IA
    </div>

    <div style="padding:10px;">
        {chat_html}
    </div>

    <form action="/chat" style="position:fixed;bottom:0;width:100%;display:flex;background:#fff;padding:10px;">
        <input name="msg" placeholder="Digite..." style="flex:1;padding:10px;">
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
