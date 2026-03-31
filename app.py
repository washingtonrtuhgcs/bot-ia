@app.route('/chat')
def chat():
    msg = request.args.get('msg')
    conversa.append(msg)
    texto = msg.lower()

    if 'oi' in texto:
        resp = "Olá! 👋 Eu sou Washington IA 🤖\nDigite 1 para Loja ou 2 para Trade"

    elif msg == '1':
        resp = "🛒 Produtos:\n1 - Camisa R$50\n2 - Calça R$100\nDigite 1 ou 2 para comprar"

    elif msg == '2':
        resp = "📈 Trade:\nDigite 'sinal' ou 'estrategia'"

    elif 'sinal' in texto:
        resp = "📊 Entrada simulada: tendência de alta"

    elif 'estrategia' in texto:
        resp = "📘 Estratégia:\n- usar stop\n- controlar risco"

    else:
        resp = "❌ Opção inválida"

    conversa.append(resp)
    return '<meta http-equiv="refresh" content="0; url=/">'
