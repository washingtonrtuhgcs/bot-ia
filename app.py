from flask import Flask, request

app = Flask(__name__)

conversa = []

PIX = "120.749.664-23"

@app.route('/')
def home():
    return f'''
    <html>
    <body style="margin:0;font-family:sans-serif;background:#ece5dd;">

    <div style="background:#075E54;color:white;padding:15px;text-align:center;">
        💼 Washington IA
    </div>

    <div style="padding:20px;text-align:center;">
        <h3>Escolha uma opção 👇</h3>

        <a href="/chat?msg=1">
            <button style="padding:15px;margin:10px;background:#25D366;color:white;border:none;border-radius:10px;">
                🛒 Loja
            </button>
        </a>

        <a href="/chat?msg=2">
            <button style="padding:15px;margin:10px;background:#128C7E;color:white;border:none;border-radius:10px;">
                📈 Trade
            </button>
        </a>
    </div>

    </body>
    </html>
    '''

@app.route('/chat')
def chat():
    msg = request.args.get('msg')

    if msg == '1':
        return f'''
        <html><body style="font-family:sans-serif;text-align:center;background:#ece5dd;">
        <h2>🛒 Produtos</h2>

        <a href="/chat?msg=11">
            <button style="padding:15px;margin:10px;background:#25D366;color:white;border:none;border-radius:10px;">
                Camisa R$50
            </button>
        </a>

        <a href="/chat?msg=22">
            <button style="padding:15px;margin:10px;background:#25D366;color:white;border:none;border-radius:10px;">
                Calça R$100
            </button>
        </a>

        </body></html>
        '''

    elif msg == '11':
        return f'''
        <html><body style="font-family:sans-serif;text-align:center;background:#ece5dd;">
        <h2>💳 Camisa R$50</h2>

        <p>PIX: {PIX}</p>

        <button onclick="navigator.clipboard.writeText('{PIX}')">
            📋 Copiar PIX
        </button>

        <p>Após pagar, envie o comprovante ✅</p>

        </body></html>
        '''

    elif msg == '22':
        return f'''
        <html><body style="font-family:sans-serif;text-align:center;background:#ece5dd;">
        <h2>💳 Calça R$100</h2>

        <p>PIX: {PIX}</p>

        <button onclick="navigator.clipboard.writeText('{PIX}')">
            📋 Copiar PIX
        </button>

        <p>Após pagar, envie o comprovante ✅</p>

        </body></html>
        '''

    elif msg == '2':
        return '''
        <html><body style="font-family:sans-serif;text-align:center;">
        <h2>📈 Trade</h2>
        <p>Digite 'sinal' ou 'estrategia'</p>
        </body></html>
        '''

    return '<meta http-equiv="refresh" content="0; url=/">'

app.run(host='0.0.0.0', port=5000)
