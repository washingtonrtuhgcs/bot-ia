xzfrom flask import Flask, request
import os
from openai import OpenAI

app = Flask(__name__)

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@app.route('/')
def home():
    return '''
    <html>
    <body style="background:#0f172a;color:white;text-align:center;padding-top:50px;font-family:Arial;">
        <h1>🤖 Bot IA</h1>
        <form action="/chat">
            <input name="msg" placeholder="Digite algo..." style="padding:10px;width:70%;">
            <br><br>
            <button type="submit">Enviar</button>
        </form>
    </body>
    </html>
    '''

@app.route('/chat')
def chat():
    msg = request.args.get('msg')

    resposta = "Erro..."

    if msg:
        try:
            resposta_ia = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "user", "content": msg}
                ]
            )
            resposta = resposta_ia.choices[0].message.content
        except:
            resposta = "Erro ao responder"

    return f'''
    <html>
    <body style="background:#0f172a;color:white;text-align:center;padding-top:50px;font-family:Arial;">
        <h1>🤖 Bot IA</h1>
        <p>{resposta}</p>
        <br>
        <a href="/" style="color:#22c55e;">⬅️ Voltar</a>
    </body>
    </html>
    '''

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=10000)
