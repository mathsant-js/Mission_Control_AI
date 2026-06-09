# 🚀 Mission Control AI — ConnectSat

Sistema inteligente de monitoramento e análise operacional de satélites para conectividade rural utilizando Inteligência Artificial Generativa.

Desenvolvido para a Global Solution 2026.1 da FIAP na trilha ConnectSat.

<br>

# 👥 Integrantes

* Guilherme Vinciguerra Carvalho — RM: 571951 — Turma: 1CCPI
* Marcos Peterson Martins Pereira — RM: XXXXXX — Turma: 1CCPI
* Matheus Jorge Santana — RM: 574166 — Turma: 1CCPI

<br>

# 📖 O que o projeto faz

O Mission Control AI simula o monitoramento de um satélite responsável por fornecer conectividade para regiões rurais.

O sistema coleta dados de telemetria, identifica alertas operacionais automaticamente e utiliza Inteligência Artificial Generativa para produzir análises técnicas sobre o estado da missão.

Além da análise do ciclo atual, o sistema mantém um histórico dos últimos ciclos operacionais, permitindo que a IA identifique tendências de degradação ou melhoria dos indicadores monitorados.

<br>

# 🎯 Persona atendida

## Operador de Satélite

O sistema foi projetado para apoiar operadores responsáveis pelo monitoramento de satélites de telecomunicações.

A IA atua como um assistente operacional, auxiliando na identificação de riscos, análise de alertas, tomada de decisão e avaliação dos impactos causados por falhas técnicas na população atendida.

<br>

# 🛠 Tecnologias utilizadas

* Python 3.10+
* Ollama Cloud API
* Modelo gpt-oss:120b
* Rich
* Prompt Toolkit
* PyFiglet
* Python Dotenv

### Bibliotecas principais

```bash
ollama
python-dotenv
rich
prompt-toolkit
pyfiglet
```

<br>

# ✨ Funcionalidades

* Coleta de telemetria simulada
* Sistema automático de alertas
* Respostas automáticas para situações críticas
* Análise operacional por IA generativa
* Histórico dos últimos ciclos monitorados
* Identificação de tendências temporais
* Interface visual em terminal utilizando Rich
* Cenários de demonstração controlados para testes

<br>

# 🧠 Diferenciais Implementados

## Few-Shot Prompting

O prompt principal contém exemplos completos de entrada e saída para orientar o comportamento da IA.

## Memória de Contexto

Os últimos ciclos de telemetria são armazenados e enviados ao modelo para análise temporal.

A IA consegue identificar:

* Crescimento de latência
* Queda de throughput
* Aumento de temperatura
* Degradação da antena

## Interface Visual

Implementada utilizando Rich:

* Banner ASCII personalizado
* Tabelas de telemetria
* Barras de progresso
* Painéis de alertas
* Histórico visual dos ciclos

<br>

# 🌎 Problema Real e Impacto Terrestre

A conectividade rural ainda representa um desafio em diversas regiões do Brasil e do mundo. Comunidades afastadas dos grandes centros frequentemente possuem acesso limitado à internet, dificultando o acesso à educação, saúde, serviços públicos e oportunidades econômicas.

O projeto ConnectSat busca simular a operação de um satélite responsável por fornecer conectividade para essas regiões, permitindo que operadores identifiquem rapidamente falhas técnicas que possam comprometer a disponibilidade do serviço.

Ao utilizar Inteligência Artificial Generativa para apoiar a tomada de decisão operacional, o sistema contribui para reduzir o tempo de resposta diante de incidentes e aumentar a confiabilidade da infraestrutura de comunicação.

<br>

# 💼 Proposta de Valor / Modelo de Negócio
## 1. Qual problema real terrestre esta missão resolve?

O ConnectSat tem como objetivo minimizar interrupções em serviços de conectividade rural fornecidos por satélites de telecomunicação.

Quando ocorrem falhas como aumento de latência, degradação de antenas ou superaquecimento de equipamentos, comunidades inteiras podem perder acesso à internet, afetando atividades essenciais como aulas remotas, telemedicina, serviços bancários digitais e comunicação de emergência.

O Mission Control AI auxilia operadores na identificação precoce desses problemas, permitindo respostas mais rápidas e reduzindo o impacto social causado por indisponibilidades prolongadas.

<br>

## 2. Quem paga pela solução?

O modelo pode ser adotado por diferentes setores.

**Setor Público**

Órgãos governamentais responsáveis pela inclusão digital e conectividade regional podem utilizar a solução para monitorar satélites que atendem escolas, postos de saúde e comunidades isoladas.

**Exemplos:**

- Governo Federal
- Governos Estaduais
- Programas de inclusão digital
- Agências reguladoras e de infraestrutura
- Setor Privado

**Empresas de telecomunicações, operadoras de satélite e provedores de internet rural podem utilizar o sistema para aumentar a eficiência operacional e reduzir custos causados por falhas.**

**Exemplos:**

- Operadoras de telecomunicações
- Empresas de satélites
- Provedores regionais de internet
- Cooperativas rurais
- Modelo Híbrido

O cenário mais provável é uma operação híbrida, onde governos contratam empresas privadas para fornecer conectividade a regiões remotas, utilizando ferramentas de monitoramento inteligente como apoio operacional.

<br>

## 3. Métrica de Impacto

Caso um satélite operasse com disponibilidade próxima de 100% durante um ano inteiro, o impacto poderia ser percebido diretamente pela população atendida.

Como estimativa plausível para um único satélite regional:

Mais de 500 escolas rurais conectadas continuamente
Aproximadamente 200 postos de saúde com acesso estável à telemedicina
Mais de 50 mil pessoas beneficiadas por conectividade confiável
Redução significativa de interrupções em serviços digitais essenciais

Além do benefício social, a manutenção preventiva e a rápida identificação de falhas contribuem para reduzir custos operacionais e aumentar a vida útil dos equipamentos de telecomunicação.

<br>

## 4. Modelo de Negócio

O modelo mais adequado para o Mission Control AI é o de Software as a Service (SaaS).

Nesse formato, operadoras de satélite e organizações contratantes pagariam uma assinatura para utilizar a plataforma de monitoramento inteligente, recebendo análises automáticas, identificação de alertas e apoio à tomada de decisão operacional.

Uma evolução futura poderia incluir o modelo Data as a Service (DaaS), fornecendo indicadores históricos, métricas operacionais e relatórios analíticos para gestores, órgãos reguladores e empresas do setor de telecomunicações.

A receita seria baseada em assinaturas mensais ou anuais, variando de acordo com a quantidade de satélites monitorados e o volume de dados processados.

<br>

## 🎯 Beneficiários da Solução

Os principais beneficiários da missão são:

Estudantes de regiões rurais que dependem da internet para atividades educacionais.
Profissionais da saúde que utilizam telemedicina para atendimento remoto.
Pequenos produtores rurais que necessitam de conectividade para gestão e comercialização.
Comunidades isoladas que dependem de serviços digitais para comunicação e acesso a serviços públicos.
Operadoras de telecomunicações que precisam garantir qualidade e disponibilidade do serviço.

Ao melhorar a confiabilidade da infraestrutura de conectividade rural, o ConnectSat gera impacto econômico, social e educacional para milhares de pessoas que dependem da comunicação via satélite.

<br>

# 🚀 Como executar

## 1. Clone o repositório

```bash
git clone https://github.com/mathsant-js/Mission_Control_AI.git

cd Mission_Control_AI
```

## 2. Crie um ambiente virtual

Linux/Mac:

```bash
python -m venv .venv

source .venv/bin/activate
```

Windows:

```bash
python -m venv .venv

.venv\Scripts\activate
```

## 3. Instale as dependências

```bash
pip install -r requirements.txt
```

## 4. Configure a API Key

Crie um arquivo `.env` na raiz do projeto:

```env
OLLAMA_API_KEY=sua_chave_aqui
```

## 5. Execute a aplicação

```bash
python main.py
```

<br>

# 💻 Comandos disponíveis

| Comando    | Descrição                   |
| ---------- | --------------------------- |
| `/help`    | Lista de comandos           |
| `/status`  | Exibe telemetria atual      |
| `/history` | Mostra histórico dos ciclos |
| `/about`   | Informações sobre o projeto |
| `/clear`   | Limpa a tela                |
| `/exit`    | Encerra a aplicação         |

<br>

# 📁 Estrutura do Projeto

```text
Mission_Control_AI/
│
├── assets/
│   ├── screenshot_analise_parte1.png
|   ├── screenshot_analise_parte1.png
|   └── screenshot.png
|
├── data/
│   └── cenarios.json
│
├── prompts/
│   └── system_prompt.md
│
├── src/
│   ├── alertas.py
│   ├── engine.py
│   ├── telemetria.py
│   ├── ui.py
│   └── banner_ascii.py
│
├── main.py
├── requirements.txt
├── .env.example
└── README.md
```

---

# 📸 Demonstração

### Tela Inicial

![Tela Inicial](assets/screenshot_banner.png)

### Telemetria Operacional

![Telemetria - Parte 1](assets/screenshot_telemetria1.png)

![Telemetria - Parte 2](assets/screenshot_telemetria2.png)

![Telemetria - Parte 3](assets/screenshot_telemetria3.png)

![Telemetria - Parte 4](assets/screenshot_telemetria4.png)

![Telemetria - Parte 5](assets/screenshot_telemetria5.png)

<br>

### Alerta Crítico

Exemplo de exibição de alerta crítico

![Alerta Crítico](assets/screenshot_alerta_critico.png)

### Histórico dos Ciclos

![Histórico - Parte 1](assets/screenshot_historico1.png)
![Histórico - Parte 2](assets/screenshot_historico2.png)
![Histórico - Parte 3](assets/screenshot_historico3.png)
![Histórico - Parte 4](assets/screenshot_historico4.png)
![Histórico - Parte 5](assets/screenshot_historico5.png)


### Análise completa da missão

![Análise - Parte 1](assets/screenshot_analise1.png)
![Análise - Parte 2](assets/screenshot_analise2.png)

<br>

# 📄 System Prompt

O prompt principal utilizado pelo modelo está disponível em:

> [System Prompt](prompts/system_prompt.md)

<br>

# 🧪 Cenários de Teste Demonstrados

## 1. Operação Normal

* Latência dentro do esperado
* Throughput adequado
* Temperatura estável

Resultado esperado:

```text
Nível de risco: BAIXO
```

<br>

## 2. Latência Elevada

Condição:

```text
Latência > 100 ms
```

Resultado esperado:

```text
CRÍTICO: Latência elevada
```

<br>

## 3. Throughput Reduzido

Condição:

```text
Throughput < 100 Mbps
```

Resultado esperado:

```text
ALERTA: Throughput abaixo do ideal
```

<br>

## 4. Antena Degradada

Condição:

```text
Saúde da antena < 70%
```

Resultado esperado:

```text
CRÍTICO: Antena degradada
```

<br>

## 5. Superaquecimento

Condição:

```text
Temperatura > 75°C
```

Resultado esperado:

```text
CRÍTICO: Superaquecimento do transponder
```

<br>

## 6. Cenário Crítico Completo

Condições simultâneas:

* Alta latência
* Throughput reduzido
* Antena degradada
* Temperatura elevada

Resultado esperado:

```text
Nível de risco: CRÍTICO
```

<br>

## 7. Análise Temporal

Após múltiplos ciclos:

```text
/history
```

A IA identifica:

* Tendências de degradação
* Evolução dos alertas
* Crescimento contínuo da latência
* Queda progressiva de throughput
* Aumento da temperatura

<br>

# ⚠️ Limitações Conhecidas

* A telemetria é totalmente simulada.
* Não existe conexão com satélites reais.
* O sistema não executa ações reais sobre equipamentos.
* O histórico é armazenado apenas em memória.
* Não existe persistência em banco de dados.
* Não há autenticação de usuários.
* Não há integração com APIs espaciais ou meteorológicas.
* A classificação de risco depende da interpretação do modelo de IA.

<br>

# 🎥 Vídeo de Demonstração

🎥 Assistir no YouTube:

*Será adicionado...*

<br>

# 🎓 Projeto Acadêmico

Projeto desenvolvido para a disciplina de Prompt Engineering and AI.

Global Solution 2026.1 — FIAP

Trilha ConnectSat.
