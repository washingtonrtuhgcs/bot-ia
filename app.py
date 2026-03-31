def responder(msg):
    msg = msg.lower().strip()

    # LOJA
    if msg == "1" or "comprar" in msg or "preço" in msg:
        return "🛒 Planos:\nBásico: R$10\nPremium: R$25\n\nPIX: 120.749.664-23 💸"

    # TRADE
    elif msg == "2" or "trade" in msg:
        return "📊 Sinal:\nBTC/USDT\nEntrada: 61.200\nSaída: 62.000\nStop: 60.800"

    # INÍCIO
    elif "oi" in msg or "olá" in msg:
        return "Fala 👋\nDigite:\n1 comprar 🛒\n2 trade 📊"

    # PADRÃO
    else:
        return "Digite:\n1 🛒 Comprar\n2 📊 Trade"
