def avaliar(dados):

    alertas = []

    if dados["latencia"] > 100:
        alertas.append(
            "CRÍTICO: Latência elevada."
        )

    if dados["throughput"] < 100:
        alertas.append(
            "ALERTA: Throughput abaixo do ideal."
        )

    if dados["saude_antena"] < 70:
        alertas.append(
            "CRÍTICO: Antena degradada."
        )

    if dados["beam_steering"] < 80:
        alertas.append(
            "ALERTA: Erro de apontamento."
        )

    if dados["temperatura"] > 75:
        alertas.append(
            "CRÍTICO: Superaquecimento do transponder."
        )

    return alertas

def resposta_automatica(dados):

    acoes = []

    if dados["temperatura"] > 75:
        acoes.append(
            "Modo resfriamento ativado."
        )

    if dados["saude_antena"] < 70:
        acoes.append(
            "Reconfiguração automática da antena."
        )

    if dados["latencia"] > 100:
        acoes.append(
            "Redistribuição de tráfego."
        )

    return acoes