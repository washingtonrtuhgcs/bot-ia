def responder(msg):
    msg = msg.lower()

    # 🔹 LOJA / VENDAS
    if "comprar" in msg or "preço" in msg or "produto" in msg:
        return "Temos vários produtos disponíveis 🛒\n\nPlano básico: R$10\nPlano premium: R$25\n\nPara comprar, envie PIX: 120.749.664-23 💸"

    elif "pix" in msg or "pagar" in msg:
        return "Pagamento via PIX 👇\n\nChave: 120.749.664-23\n\nApós pagar, envie o comprovante ✅"

    elif "entrega" in msg:
        return "Entrega imediata após confirmação do pagamento ⚡"

    # 🔹 TRADE
    elif "trade" in msg or "sinal" in msg:
        return "📊 SINAL DE TRADE:\n\nAtivo: BTC/USDT\nEntrada: 61.200\nSaída: 62.000\nStop: 60.800\n\nGerenciamento é tudo ⚠️"

    elif "mercado" in msg:
        return "📉 O mercado está lateral no momento.\n\nEvite entradas arriscadas e espere confirmação."

    elif "estratégia" in msg:
        return "📈 Estratégia recomendada:\n\n- Suporte e resistência\n- Rompimento com volume\n- Gestão de risco (1-2%)"

    # 🔹 PADRÃO
    elif "oi" in msg or "olá" in msg:
        return "Fala! 👋\n\nVocê quer:\n\n1️⃣ Comprar produto 🛒\n2️⃣ Receber sinal de trade 📊\n\nDigite o número 😉"

    else:
        return "Não entendi 🤔\n\nDigite:\n1 para comprar 🛒\n2 para trade 📊"
