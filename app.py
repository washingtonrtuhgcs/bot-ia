from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return "🔥 FUNCIONANDO AGORA"

@app.route('/chat')
def chat():
    msg = request.args.get('msg')
    return f"Você disse: {msg}"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=10000)
