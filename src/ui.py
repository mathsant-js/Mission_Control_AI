"""Interface CLI estilo Claude Code — usa Rich + prompt-toolkit."""

from rich.console import Console
from rich.align import Align
from rich.panel import Panel
from rich.text import Text
from rich.rule import Rule
from rich.table import Table
from rich.progress_bar import ProgressBar
from prompt_toolkit import PromptSession
from prompt_toolkit.styles import Style
import pyfiglet
from datetime import datetime

console = Console()
session = PromptSession(style=Style.from_dict({"prompt": "#06B6D4 bold"}))

def banner_design():
    console.print()
    
    titulo = pyfiglet.figlet_format(
        "Mission Control AI",
        font="ansi_shadow"
    )

    texto_global_solution = "GLOBAL SOLUTION 2026.1 • CONNECTSAT"
    modelo_ia = "gpt-oss:120b"
    
    ciano = "#06B6D4"
    ciano_negrito = "bold #06B6D4"
    cinza_azulado = "#94A3B8"
    cinza_aluzado_medio_italico = "italic #64748B"
    cinza_arroxeado_italico = "italic #8484A0"
    
    console.print()

    console.print(
            Align.center(
                Text(
                    titulo,
                    style = ciano_negrito
                )
            )
        )

    console.print(
            Align.center(
                Text(
                    texto_global_solution,
                    style = ciano_negrito
                )
            )
        )

    console.print(
            Align.center(
                Text(
                    "Monitoramento Inteligente de Satélites para Conectividade Rural",
                    style = cinza_azulado
                )
            )
        )

    console.print()

    console.print(
            Panel.fit(
                "[bold]Recursos implementados[/bold]\n\n"
                "📡 Telemetria simulada em tempo real\n"
                "⚠️  Sistema de alertas automáticos\n"
                "🧠 IA generativa para análise operacional\n"
                "📈 Histórico de ciclos para análise temporal\n"
                "🌎 Correlação entre falhas técnicas e impacto social\n\n"
                "[bold]/help[/bold] para listar comandos disponíveis",
                title="◆ CONNECTSAT MISSION CONTROL",
                border_style = ciano,
                padding=(1, 2)
            )
        )

    console.print(
            Align.center(
                Text(
                    f"Modelo: {modelo_ia} via Ollama Cloud",
                    style = cinza_aluzado_medio_italico
                )
            )
        )

    console.print()

    console.print(
            Align.center(
                Text(
                    f"── 2026.1 · Prompt Engineering and AI · FIAP ──",
                    style = cinza_arroxeado_italico
                )
            )
        )

    console.print()

def show_banner():
    """Exibe banner ASCII colorido no início."""
    banner_design()

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
        console.print(
                Panel(
                    "Nenhum alerta identificado.",
                    title=f"✓ Ciclo sem Alertas",
                    border_style="green"
                )
            )
    else:

        texto = "\n".join(alertas)

        console.print(
            Panel(
                texto,
                title="⚠ ALERTAS",
                border_style="red"
            )
        )
    
def render_historico(historico):

    console.print()
    console.print()
    console.print()
    
    if not historico:

        console.print(
            Panel(
                "Nenhum ciclo registrado.",
                border_style="yellow"
            )
        )

        return

    console.print(
        Rule(
            "[bold #06B6D4]HISTÓRICO DOS ÚLTIMOS CICLOS"
        )
    )

    for indice, ciclo in enumerate(historico, start=1):

        dados = ciclo["dados"]

        alertas = ciclo["alertas"]

        tabela = Table(
            title=f"📡 Ciclo {indice}",
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

        console.print()
        console.print()
        console.print(tabela)
        
        console.print("\nLatência")
        console.print(
            ProgressBar(
                total=150,
                completed=dados["latencia"]
            )
        )

        console.print("\nThroughput")
        console.print(
            ProgressBar(
                total=500,
                completed=dados["throughput"]
            )
        )

        console.print("\nSaúde Antena")
        console.print(
            ProgressBar(
                total=100,
                completed=dados["saude_antena"]
            )
        )

        console.print("\nBeam Steering")
        console.print(
            ProgressBar(
                total=100,
                completed=dados["beam_steering"]
            )
        )

        console.print("\nTemperatura")
        console.print(
            ProgressBar(
                total=100,
                completed=dados["temperatura"]
            )
        )
        
        if alertas:

            console.print(
                Panel(
                    "\n".join(alertas),
                    title=f"⚠ Alertas do Ciclo {indice}",
                    border_style="red"
                )
            )
        
        else:

            console.print(
                Panel(
                    "Nenhum alerta identificado.",
                    title=f"✓ Ciclo {indice}",
                    border_style="green"
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
            console.print(
                Panel.fit(
                    "[bold]/help[/bold]      → Lista de comandos\n"
                    "[bold]/status[/bold]    → Telemetria atual\n"
                    "[bold]/history[/bold]   → Histórico dos ciclos\n"
                    "[bold]/about[/bold]     → Informações do projeto\n"
                    "[bold]/clear[/bold]     → Limpar tela\n"
                    "[bold]/exit[/bold]      → Encerrar aplicação",
                    title="◆ COMANDOS",
                    border_style="#06B6D4"
                )
            )
            continue
        if user_input == "/status":
            status = engine.status_snapshot()
            
            render_status(status["dados"])
            render_barras(status["dados"])
            console.print()
            render_alertas(status["alertas"])
            continue
        if user_input == "/history":
            historico = engine.mostrar_historico()
            render_historico(historico)
        if user_input == "/about":
            console.print(
                Panel.fit(
                    "[bold]Mission Control AI[/bold]\n\n"
                    "Trilha: ConnectSat\n"
                    "Global Solution 2026.1\n\n"
                    "Modelo: gpt-oss:120b\n"
                    "Provider: Ollama Cloud\n\n"
                    "Recursos implementados:\n"
                    "• Telemetria simulada\n"
                    "• Alertas automáticos\n"
                    "• Memória de contexto\n"
                    "• Interface visual com Rich\n"
                    "• IA generativa para análise operacional",
                    title="◆ SOBRE O PROJETO",
                    border_style="#06B6D4"
                )
            )
            continue
        if user_input == "/clear":
            console.clear()
            show_banner()
            continue
        # Qualquer outra entrada vai para o motor de análise
        resposta = engine.analyze(user_input)
        show_response(resposta)
