from flask import Flask, request

app = Flask(__name__)

conversa = []

@app.route('/')
def home():
    chat_html = ''
    for i, msg in enumerate(conversa):
        if i % 2 == 0:
            chat_html += f'<div style="text-align:right;margin:10px;"><span style="background:#25D366;color:white;padding:10px;border-radius:10px;display:inline-block;">{msg}</span></div>'
        else:
            chat_html += f'<div style="text-align:left;margin:10px;"><span style="background:#ffffff;padding:10px;border-radius:10px;display:inline-block;">{msg}</span></div>'

    return f'''
    <html>
    <body style="margin:0;font-family:sans-serif;background:#ece5dd;">
        <div style="padding-bottom:70px;">
            {chat_html}
        </div>

        <form action="/chat" style="position:fixed;bottom:0;width:100%;display:flex;background:#fff;padding:10px;">
            <input name="msg" placeholder="Digite sua mensagem..." style="flex:1;padding:10px;border-radius:20px;border:1px solid #ccc;">
            <button style="margin-left:10px;padding:10px 20px;border:none;border-radius:20px;background:#25D366;color:white;">Enviar</button>
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
        resp = "Ola! Digite 1 para Loja ou 2 para Trade"
    elif msg == '1':
        resp = "Produtos: Camisa 50, Calca 100"
    elif msg == '2':
        resp = "Trade: digite sinal ou estrategia"
    elif 'sinal' in texto:
        resp = "Entrada simulada: tendencia de alta"
    elif 'estrategia' in texto:
        resp = "Estrategia: usar stop loss e evitar emocao"
    else:
        resp = "Digite uma opcao valida"

    conversa.append(resp)
    return '<meta http-equiv="refresh" content="0; url=/">'

app.run(host='0.0.0.0', port=5000)
