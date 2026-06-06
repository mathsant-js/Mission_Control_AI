"""Interface CLI estilo Claude Code — usa Rich + prompt-toolkit."""

from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.table import Table
from rich.progress_bar import ProgressBar
from prompt_toolkit import PromptSession
from prompt_toolkit.styles import Style
import pyfiglet
from datetime import datetime

console = Console()
session = PromptSession(style=Style.from_dict({"prompt": "#06B6D4 bold"}))


def show_banner():
    """Exibe banner ASCII colorido no início."""
    banner = pyfiglet.figlet_format("Mission Control", font="ansi_shadow")
    console.print(Text(banner, style="bold #06B6D4"))
    console.print(
        Panel.fit(
            "Sistema de monitoramento e análise por IA generativa.\n"
            "Use /help para ver os comandos · /exit para sair.\n"
            "Modelo: gpt-oss:120b via Ollama Cloud",
            title="◆ MISSION CONTROL",
            border_style="#06B6D4",
        )
    )

def render_status(dados):

    tabela = Table(
        title="📡 CONNECTSAT TELEMETRY",
        border_style="#06B6D4"
    )

    tabela.add_column("Parâmetro")
    tabela.add_column("Valor")

    tabela.add_row(
        "Latência",
        f"{dados['latencia']} ms"
    )

    tabela.add_row(
        "Throughput",
        f"{dados['throughput']} Mbps"
    )

    tabela.add_row(
        "Saúde Antena",
        f"{dados['saude_antena']} %"
    )

    tabela.add_row(
        "Beam Steering",
        f"{dados['beam_steering']} %"
    )

    tabela.add_row(
        "Temperatura",
        f"{dados['temperatura']} °C"
    )

    console.print(tabela)
    
def render_barras(dados):

    console.print("\n[bold]Latência[/bold]")
    console.print(
        ProgressBar(
            total=150,
            completed=dados["latencia"]
        )
    )

    console.print("\n[bold]Throughput[/bold]")
    console.print(
        ProgressBar(
            total=500,
            completed=dados["throughput"]
        )
    )

    console.print("\n[bold]Saúde Antena[/bold]")
    console.print(
        ProgressBar(
            total=100,
            completed=dados["saude_antena"]
        )
    )

    console.print("\n[bold]Beam Steering[/bold]")
    console.print(
        ProgressBar(
            total=100,
            completed=dados["beam_steering"]
        )
    )

    console.print("\n[bold]Temperatura[/bold]")
    console.print(
        ProgressBar(
            total=100,
            completed=dados["temperatura"]
        )
    )

def render_alertas(alertas):

    if not alertas:
        return

    texto = "\n".join(alertas)

    console.print(
        Panel(
            texto,
            title="⚠ ALERTAS",
            border_style="red"
        )
    )

def show_response(text):
    """Renderiza resposta da IA em painel com timestamp."""
    now = datetime.now().strftime("%H:%M")
    console.print(
        Panel(text, title="◆ Mission Control", subtitle=now, border_style="#06B6D4")
    )


def run_cli(engine):
    """Loop principal da CLI."""
    show_banner()
    if not engine.is_ready():
        console.print(" ⚠ Engine status: AGUARDANDO IMPLEMENTAÇÃO ✗\n", style="yellow")
    while True:
        try:
            user_input = session.prompt("❯ ").strip()
        except (KeyboardInterrupt, EOFError):
            break
        if not user_input:
            continue
        if user_input == "/exit":
            break
        if user_input == "/help":
            console.print("Comandos: /help /status /history /about /clear /exit")
            continue
        if user_input == "/status":
            status = engine.status_snapshot()
            
            render_status(status["dados"])
            render_barras(status["dados"])
            render_alertas(status["alertas"])
            continue
        if user_input == "/history":
            show_response(
                engine.mostrar_historico()
            )
        if user_input == "/clear":
            console.clear()
            show_banner()
            continue
        # Qualquer outra entrada vai para o motor de análise
        resposta = engine.analyze(user_input)
        show_response(resposta)
