from flask import Flask, request
import unicodedata

app = Flask(__name__)

conversa = []
nome_cliente = ''
pedidos = []
etapa = 'inicio'

@app.route('/')
def home():
    chat_html = ''

    for i, msg in enumerate(conversa):
        if i % 2 == 0:
            chat_html += '<div style="text-align:right;background:#25D366;color:white;padding:10px;margin:5px;border-radius:10px;">'+msg+'</div>'
        else:
            chat_html += '<div style="text-align:left;background:#ffffff;padding:10px;margin:5px;border-radius:10px;">'+msg+'</div>'

    return "<html><body style='margin:0;font-family:sans-serif;background:#ece5dd;'>" + \
           "<div style='background:#075E54;color:white;padding:15px;text-align:center;'>Atendimento</div>" + \
           "<div style='height:80vh;overflow:auto;padding:10px;'>" + chat_html + "</div>" + \
           "<form action='/chat' style='position:fixed;bottom:0;width:100%;display:flex;background:#f0f0f0;padding:10px;'>" + \
           "<input name='msg' style='flex:1;padding:10px;border-radius:20px;border:1px solid #ccc;'>" + \
           "<button style='margin-left:10px;padding:10px;background:#25D366;color:white;border:none;border-radius:20px;'>Enviar</button>" + \
           "</form></body></html>"

@app.route('/chat')
def chat():
    global nome_cliente, etapa

    msg = request.args.get('msg')
    conversa.append(msg)

    texto = unicodedata.normalize('NFKD', msg).encode('ASCII', 'ignore').decode('ASCII').lower()

    if etapa == 'inicio':
        nome_cliente = msg
        etapa = 'menu'
        resp = 'Ola ' + nome_cliente + '. Digite 1 Produtos, 2 Pedidos ou 3 Trade'

    elif msg == '1':
        resp = 'Produtos: Camisa 50 reais, Calca 100 reais. Digite o nome'

    elif 'camisa' in texto:
        pedidos.append('Camisa')
        resp = 'Pedido de camisa registrado'

    elif 'calca' in texto:
        pedidos.append('Calca')
        resp = 'Pedido de calca registrado'

    elif msg == '2':
        if len(pedidos) == 0:
            resp = 'Nenhum pedido ainda'
        else:
            resp = nome_cliente + ' seus pedidos: ' + ', '.join(pedidos)

    elif msg == '3':
        resp = 'Trade: digite sinal ou estrategia'

    elif 'sinal' in texto:
        resp = 'Possivel tendencia de alta'

    elif 'estrategia' in texto:
        resp = 'Usar stop e controlar risco'

    elif 'nao' in texto or texto == 'n':
        resp = 'Atendimento finalizado'

    else:
        resp = 'Digite uma opcao valida'

    conversa.append(resp)

    return '<meta http-equiv="refresh" content="0; url=/">'

app.run(host='0.0.0.0', port=5000)
