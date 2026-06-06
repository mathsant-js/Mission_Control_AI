import random
import json

MODO_DEMO = False

indice_demo = 0

def coletar():
    global indice_demo
    
    if MODO_DEMO:
        with open("data/cenarios.json", "r") as arquivo:
            cenarios_demo = json.load(arquivo)

        dados = cenarios_demo[indice_demo]

        if indice_demo < len(cenarios_demo) - 1:
            indice_demo += 1

        return dados

    return {
        "latencia": random.randint(20, 150),
        "throughput": random.randint(50, 500),
        "saude_antena": random.randint(50, 100),
        "beam_steering": random.randint(60, 100),
        "temperatura": random.randint(20, 90)
    }