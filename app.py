from flask import Flask, request
import os
import openai

app = Flask(__name__)

# chave da API
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route('/')
def home():
    return '''
    <html>
    <body style="background:#0f172a;color:white;text-align:center;padding-top:50px;font-family:Arial;">
        <h1>🤖 Bot IA</h1>
        <form action="/chat">
            <input name="msg" placeholder="Digite sua mensagem" style="padding:10px;width:70%;border-radius:10px;border:none;">
            <br><br>
            <button type="submit" style="padding:10px 20px;border-radius:10px;border:none;background:#22c55e;color:white;font-weight:bold;">
                Enviar
            </button>
        </form>
    </body>
    </html>
    '''

@app.route('/chat')
def chat():
    msg = request.args.get("msg")

    try:
        resposta = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": msg}]
        )

        texto = resposta['choices'][0]['message']['content']

    except Exception as e:
        texto = "Erro ao responder 😢"

    return f'''
    <html>
    <body style="background:#0f172a;color:white;text-align:center;padding-top:50px;font-family:Arial;">
        <h1>🤖 Bot IA</h1>
        <p>Você: {msg}</p>
        <p>IA: {texto}</p>
        <br>
        <a href="/" style="color:#22c55e;">⬅ Voltar</a>
    </body>
    </html>
    '''

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
