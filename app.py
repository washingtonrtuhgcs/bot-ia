from flask import Flask, request

app = Flask(__name__)

conversa = []

@app.route('/')
def home():
    chat_html = ''
    for i, msg in enumerate(conversa):
        if i % 2 == 0:
            chat_html += f'''
            <div style="text-align:right;margin:10px;">
                <span style="background:#25D366;color:white;padding:12px;border-radius:15px;display:inline-block;max-width:70%;">
                    {msg}
                </span>
            </div>
            '''
        else:
            chat_html += f'''
            <div style="text-align:left;margin:10px;">
                <span style="background:#ffffff;padding:12px;border-radius:15px;display:inline-block;max-width:70%;">
                    {msg}
                </span>
            </div>
            '''

    return f'''
<html>
<body style="margin:0;font-family:sans-serif;background:#ece5dd;">

    <div style="background:#075E54;color:white;padding:15px;font-size:18px;">
        Atendimento Online 🤖
    </div>

    <div id="chat" style="padding-bottom:80px;max-width:600px;margin:auto;">
        {chat_html}
    </div>

    <form action="/chat" style="position:fixed;bottom:0;width:100%;display:flex;background:#fff;padding:10px;">
        <input name="msg" placeholder="Digite sua mensagem..." 
        style="flex:1;padding:12px;border-radius:25px;border:1px solid #ccc;">
        
        <button style="margin-left:10px;padding:12px 20px;border:none;border-radius:25px;background:#25D366;color:white;">
            Enviar
        </button>
    </form>

    <script>
        var chat = document.getElementById("chat");
        chat.scrollTop = chat.scrollHeight;
    </script>

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
        resp = "🛒 Produtos:\n- Camisa R$50\n- Calça R$100"
    elif msg == '2':
        resp = "📈 Trade: digite sinal ou estrategia"
    elif 'sinal' in texto:
        resp = "📊 Entrada simulada: tendência de alta"
    elif 'estrategia' in texto:
        resp = "📘 Estratégia: usar stop e evitar emoção"
    else:
        resp = "❌ Digite uma opção válida"

    conversa.append(resp)
    return '<meta http-equiv="refresh" content="0; url=/">'

app.run(host='0.0.0.0', port=5000)
