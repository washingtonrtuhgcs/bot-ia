@app.route('/')
def home():
    chat_html = ''

    for i, msg in enumerate(conversa):
        if i % 2 == 0:
            chat_html += f'<p>{msg}</p>'
        else:
            chat_html += f'<p>{msg}</p>'

    return f'''
    <html>
    <body style="margin:0;font-family:sans-serif;background:#ece5dd;">

    <div style="background:#075E54;color:white;padding:15px;">
        💼 Washington IA
    </div>

    <div style="padding:10px;">
        {chat_html}
    </div>

    <form action="/chat" style="position:fixed;bottom:0;width:100%;display:flex;background:#fff;padding:10px;">
        <input name="msg" placeholder="Digite..." style="flex:1;">
        <button>Enviar</button>
    </form>

    </body>
    </html>
    '''
