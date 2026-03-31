from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <h1>🤖 Bot IA</h1>
    <form action="/chat">
        <input name="msg" placeholder="Digite algo">
        <button type="submit">Enviar</button>
    </form>
    '''

@app.route('/chat')
def chat():
    msg = request.args.get('msg')

    if msg:
        resposta = f"Você disse: {msg}"
    else:
        resposta = "Digite algo!"

    return f'''
    <h1>🤖 Bot IA</h1>
    <p>{resposta}</p>
    <a href="/">Voltar</a>
    '''

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=10000)
