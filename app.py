from flask import Flask, request
import urllib.parse

app = Flask(__name__)

PIX = "120.749.664-23"
NOME = "Washington Luiz Marinho Araújo Filho"

pedidos = []

def gerar_qr_pix(valor):
    payload = f"PIX:{PIX}|NOME:{NOME}|VALOR:{valor}"
    url = "https://api.qrserver.com/v1/create-qr-code/?size=200x200&data=" + urllib.parse.quote(payload)
    return url

@app.route('/')
def home():
    return '''
    <html>
    <body style="margin:0;font-family:sans-serif;background:#ece5dd;text-align:center;">

    <div style="background:#075E54;color:white;padding:15px;">
        💼 Washington IA
    </div>

    <h3>Escolha 👇</h3>

    <a href="/chat?msg=1">
        <button style="padding:15px;margin:10px;background:#25D366;color:white;border:none;border-radius:10px;">
            🛒 Loja
        </button>
    </a>

    <a href="/chat?msg=pedidos">
        <button style="padding:15px;margin:10px;background:#128C7E;color:white;border:none;border-radius:10px;">
            📦 Ver Pedidos
        </button>
    </a>

    </body>
    </html>
    '''

@app.route('/chat')
def chat():
    msg = request.args.get('msg')

    if not msg:
        return '<meta http-equiv="refresh" content="0; url=/">'

    if msg == '1':
        return '''
        <html><body style="text-align:center;">
        <h2>🛒 Produtos</h2>

        <a href="/chat?msg=11"><button>Camisa R$50</button></a><br><br>
        <a href="/chat?msg=22"><button>Calça R$100</button></a>

        </body></html>
        '''

    elif msg == '11':
        qr = gerar_qr_pix("50")
        pedidos.append("Camisa R$50")

        return f'''
        <html><body style="text-align:center;">
        <h2>💳 Camisa R$50</h2>

        <p>PIX: {PIX}</p>

        <img src="{qr}"><br><br>

        <button onclick="navigator.clipboard.writeText('{PIX}')">
        📋 Copiar PIX
        </button>

        <p>Após pagar, envie o comprovante ✅</p>

        </body></html>
        '''

    elif msg == '22':
        qr = gerar_qr_pix("100")
        pedidos.append("Calça R$100")

        return f'''
        <html><body style="text-align:center;">
        <h2>💳 Calça R$100</h2>

        <p>PIX: {PIX}</p>

        <img src="{qr}"><br><br>

        <button onclick="navigator.clipboard.writeText('{PIX}')">
        📋 Copiar PIX
        </button>

        <p>Após pagar, envie o comprovante ✅</p>

        </body></html>
        '''

    elif msg == 'pedidos':
        lista = "<br>".join(pedidos) if pedidos else "Nenhum pedido ainda"

        return f'''
        <html><body style="text-align:center;">
        <h2>📦 Pedidos</h2>
        <p>{lista}</p>
        </body></html>
        '''

    return '<meta http-equiv="refresh" content="0; url=/">'

app.run(host='0.0.0.0', port=5000)
