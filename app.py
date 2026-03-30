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
                <span style="background:#25D366;color:white;padding:12px 16px;border-radius:15px;display:inline-block;max-width:70%;box-shadow:0 2px 5px rgba(0,0,0,0.2);">
                    {msg}
                </span>
            </div>
            '''
        else:
            chat_html += f'''
            <div style="text-align:left;margin:10px;">
                <span style="background:#ffffff;padding:12px 16px;border-radius:15px;display:inline-block;max-width:70%;box-shadow:0 2px 5px rgba(0,0,0,0.2);">
                    {msg}
                </span>
            </div>
            '''

    return f'''
<html>
<body style="margin:0;font-family:sans-serif;background:linear-gradient(to bottom,#075E54,#128C7E);">

    <!-- CONTAINER -->
    <div style="max-width:600px;margin:auto;height:100vh;display:flex;flex-direction:column;">

        <!-- TOPO -->
        <div style="background:#075E54;color:white;padding:15px;font-size:18px;border-bottom:2px solid #128C7E;">
            🤖 Atendimento Profissional
        </div>

        <!-- CHAT -->
        <div id="chat" style="flex:1;overflow-y:auto;padding:10px;background:#ece5dd;">
            {chat_html}
        </div>

        <!-- INPUT -->
        <form action="/chat" style="display:flex;padding:10px;background:#fff;">
            <input name="msg" placeholder="Digite sua mensagem..." 
            style="flex:1;padding:12px;border-radius:25px;border:1px solid #ccc;">
            
            <button style="margin-left:10px;padding:12px 20px;border:none;border-radius:25px;background:#25D366;color:white;font-weight:bold;">
                Enviar
            </button>
        </form>

    </div>

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
        resp = "Olá! 👋 Bem-vindo ao atendimento profissional.\nDigite 1 para Loja ou 2 para Trade"
    elif msg == '1':
        resp = "🛒 Produtos disponíveis:\n- Camisa R$50\n- Calça R$100"
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

app.run(host='0.0.0.0', port=5000)
