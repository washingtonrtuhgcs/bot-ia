from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <h1>🔥 Bot Online</h1>
    <form action="/chat">
        <input name="msg" placeholder="Digite algo">
        <button type="submit">Enviar</button>
    </form>
    '''

@app.route('/chat')
def chat():
    msg = request.args.get('msg')
    return f"Você disse: {msg}"

app.run(host='0.0.0.0', port=10000)
