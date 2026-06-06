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


def llm(prompt, system=None, max_tokens=1500, temperature=0.3):
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
        self.historico = []
        self.dados_atuais = None

    def is_ready(self):
        return True

    def status_snapshot(self):
        self.dados_atuais = coletar()
        
        self.atualizar_historico(self.dados_atuais)
        
        return {
            "dados": self.dados_atuais,
            "alertas": avaliar(self.dados_atuais)
        }

    def mostrar_historico(self):

        if not self.historico:
            return []

        historico = []

        for ciclo in self.historico:

            historico.append({
                "dados": ciclo,
                "alertas": avaliar(ciclo)
            })

        return historico

    def atualizar_historico(self, dados):
        self.historico.append(dados.copy())

        if len(self.historico) > 5:
            self.historico.pop(0)

    def analyze(self, pergunta_usuario):        
        if self.dados_atuais is None:

            return (
                "Nenhuma telemetria disponível.\n\n"
                "Execute o comando /status antes de solicitar "
                "uma análise da missão."
            )
        
        alertas = avaliar(self.dados_atuais)
        
        acoes = resposta_automatica(self.dados_atuais)
        
        prompt = f"""
        CONTEXTO
        
        Você está analisando um satélite ConnectSat.
        
        HISTÓRICO DOS ÚLTIMOS CICLOS
        
        {self.historico}
        
        TELEMETRIA ATUAL

        {self.dados_atuais}

        ALERTAS IDENTIFICADOS

        {alertas}

        AÇÕES AUTOMÁTICAS EXECUTADAS
        
        {acoes}
        
        IMPORTANTE
        
        Analise tendências entre os ciclos anteriores e o ciclo atual.

        Se um parâmetro estiver piorando ao longo dos ciclos, destaque essa tendência.

        PERGUNTA DO OPERADOR
        {pergunta_usuario}
        """
        
        return llm(prompt, system=self.system_prompt)
