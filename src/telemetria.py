import random

def coletar():

    return {
        "latencia": random.randint(20, 150),
        "throughput": random.randint(50, 500),
        "saude_antena": random.randint(50, 100),
        "beam_steering": random.randint(60, 100),
        "temperatura": random.randint(20, 90)
    }