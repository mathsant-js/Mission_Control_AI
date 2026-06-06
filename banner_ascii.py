import pyfiglet
from rich.console import Console
from rich.align import Align
from rich.text import Text
from rich.panel import Panel

console = Console()

titulo = pyfiglet.figlet_format(
        "Mission Control AI",
        font="ansi_shadow"
)

texto_global_solution = "GLOBAL SOLUTION 2026.1 • CONNECTSAT"

ciano = "#06B6D4"

ciano_negrito = "bold #06B6D4"

cinza_azulado = "#94A3B8"

cinza_aluzado_medio_italico = "italic #64748B"

cinza_arroxeado_italico = "italic #8484A0"

modelo_ia = "gpt-oss:120b"

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
