lfrom flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Servidor online 🚀"

@app.route('/chat')
def chat():
    return "Chat funcionando 💬"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
