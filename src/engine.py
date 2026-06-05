"""Motor de análise da Mission Control AI."""

import os
from ollama import Client
from dotenv import load_dotenv
from pathlib import Path
from src.telemetria import coletar
from src.alertas import avaliar, resposta_automatica

load_dotenv()

TRILHA = "connectsat"

client = Client(
    host="https://ollama.com",
    headers={"Authorization": "Bearer " + os.environ.get("OLLAMA_API_KEY", "")},
)


def llm(prompt, system=None, max_tokens=800, temperature=0.3):
    """Envia prompt ao gpt-oss:120b via Ollama Cloud."""
    messages = []
    if system:
        messages.append({"role": "system", "content": system})
        messages.append({"role": "user", "content": prompt})

    try:
        return client.chat(
            model="gpt-oss:120b",
            messages=messages,
            options={"num_predict": max_tokens, "temperature": temperature},
            stream=False,
        )["message"]["content"].strip()
    except Exception as e:
        return f"⚠️ Erro ao consultar IA: {e}"


def load_system_prompt():
    """Lê o system prompt do arquivo prompts/system_prompt.md"""
    path = Path("prompts/system_prompt.md")
    if path.exists():
        return path.read_text(encoding="utf-8")
    return "Você é um assistente."  # fallback genérico


class MissionEngine:
    """Motor de análise — vocês completam os métodos abaixo."""

    def __init__(self):
        self.trilha = TRILHA
        self.system_prompt = load_system_prompt()

    def is_ready(self):
        return True

    def status_snapshot(self):
        dados = coletar()
        
        return (
            f"Latência: {dados['latencia']} ms\n"
            f"Throughput: {dados['throughput']} Mbps\n"
            f"Saúde Antena: {dados['saude_antena']}%\n"
            f"Beam Steering: {dados['beam_steering']}%\n"
            f"Temperatura: {dados['temperatura']}°C"
        )


    def analyze(self, pergunta_usuario):
        dados = coletar()
        
        alertas = avaliar(dados)
        
        acoes = resposta_automatica(dados)
        
        prompt = f"""
        TELEMETRIA:

        {dados}

        ALERTAS:

        {alertas}

        AÇÕES AUTOMÁTICAS EXECUTADAS
        
        {acoes}

        PERGUNTA:
        {pergunta_usuario}
        """
        
        return llm(prompt, system=self.system_prompt)
