return f'''
<html>
<body style="margin:0;font-family:sans-serif;background:#ece5dd;">

<div style="background:#075E54;color:white;padding:15px;font-size:18px;">
    💼 Washington IA
</div>

<div style="padding:10px;">
    {chat_html}
</div>

<form action="/chat" style="position:fixed;bottom:0;width:100%;display:flex;background:#fff;padding:10px;">
    <input name="msg" placeholder="Digite..." 
    style="flex:1;padding:12px;border-radius:20px;border:1px solid #ccc;">
    
    <button style="margin-left:10px;padding:12px;border:none;border-radius:20px;background:#25D366;color:white;">
        Enviar
    </button>
</form>

</body>
</html>
'''
