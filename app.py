@app.route('/chat')
def chat():
    msg = request.args.get('msg')

    if not msg:
        return '<meta http-equiv="refresh" content="0; url=/">'

    conversa.append(msg)
    texto = msg.lower()

    # MENU PRINCIPAL
    if 'oi' in texto:
        resp = "Olá! 👋 Eu sou Washington IA\nDigite:\n1 - Loja 🛒\n2 - Trade 📈"

    # LOJA
    elif msg == '1':
        resp = "🛒 Produtos:\nDigite:\n11 - Camisa R$50\n22 - Calça R$100"

    # COMPRA CAMISA
    elif msg == '11':
        resp = "💳 Camisa R$50\nPIX: seuemail@pix.com\nEnvie o comprovante"

    # COMPRA CALÇA
    elif msg == '22':
        resp = "💳 Calça R$100\nPIX: seuemail@pix.com\nEnvie o comprovante"

    # TRADE
    elif msg == '2':
        resp = "📈 Trade:\nDigite:\n'sinal' ou 'estrategia'"

    elif 'sinal' in texto:
        resp = "📊 Tendência de alta"

    elif 'estrategia' in texto:
        resp = "📘 Use stop e controle risco"

    # ERRO
    else:
        resp = "❌ Não entendi 😅\nDigite 'oi' para começar"

    conversa.append(resp)

    return '<meta http-equiv="refresh" content="0; url=/">'
