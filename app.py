from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <html>
    <head>
        <title>Bot IA</title>
        <style>
            body {
                background: #0f172a;
                color: white;
                font-family: Arial;
                text-align: center;
                padding-top: 50px;
            }
            input {
                padding: 10px;
                width: 70%;
                border-radius: 10px;
                border: none;
            }
            button {
                padding: 10px 20px;
                border-radius: 10px;
                border: none;
                background: #22c55e;
                color: white;
                font-weight: bold;
            }
        </style>
    </head>
    <body>
        <h1>🤖 Bot IA</h1>
        <form action="/chat">
            <input name="msg" placeholder="Digite algo...">
            <br><br>
            <button type="submit">Enviar</button>
        </form>
    </body>
    </html>
    '''

@app.route('/chat')
def chat():
    msg = request.args.get('msg')

    if msg:
        resposta = f"Você disse: {msg}"
    else:
        resposta = "Digite algo!"

    return f'''
    <html>
    <body style="background:#0f172a;color:white;text-align:center;padding-top:50px;font-family:Arial;">
        <h1>🤖 Bot IA</h1>
        <p style="font-size:20px;">{resposta}</p>
        <br>
        <a href="/" style="color:#22c55e;">⬅️ Voltar</a>
    </body>
    </html>
    '''

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=10000)
