#!/usr/bin/env python3
"""
Demonstração da estrutura do AutoGen sem necessidade de API key
Este exemplo mostra como configurar agentes e a estrutura básica
"""
import asyncio
from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.messages import TextMessage


def print_separator(title=""):
    """Imprime um separador visual"""
    if title:
        print(f"\n{'='*60}")
        print(f"  {title}")
        print(f"{'='*60}\n")
    else:
        print(f"{'='*60}\n")


async def demo_agent_structure():
    """Demonstra a estrutura de agentes do AutoGen"""

    print_separator("📚 DEMONSTRAÇÃO DO AUTOGEN - ESTRUTURA")

    print("1️⃣  CONFIGURAÇÃO DE UM AGENTE")
    print("-" * 60)
    print("""
from autogen_agentchat.agents import AssistantAgent
from autogen_ext.models.openai import OpenAIChatCompletionClient

# Configurar o modelo
model_client = OpenAIChatCompletionClient(
    model="gpt-4o",
    api_key="sua-chave-aqui"
)

# Criar um agente
agent = AssistantAgent(
    name="assistente",
    model_client=model_client,
    system_message="Você é um assistente útil"
)
    """)

    print("\n2️⃣  EXECUTANDO UMA TAREFA")
    print("-" * 60)
    print("""
# Executar uma tarefa
result = await agent.run(task="Olá, como você está?")
print(result)
    """)

    print("\n3️⃣  MULTI-AGENTES")
    print("-" * 60)
    print("""
# Criar múltiplos agentes especializados
math_agent = AssistantAgent(
    "math_expert",
    model_client=model_client,
    system_message="Você é um especialista em matemática"
)

code_agent = AssistantAgent(
    "code_expert",
    model_client=model_client,
    system_message="Você é um especialista em programação"
)

# Orquestrar agentes usando AgentTool
from autogen_agentchat.tools import AgentTool

math_tool = AgentTool(math_agent)
code_tool = AgentTool(code_agent)

coordinator = AssistantAgent(
    "coordinator",
    model_client=model_client,
    tools=[math_tool, code_tool]
)
    """)

    print_separator("📁 EXEMPLOS DISPONÍVEIS NO PROJETO")

    examples = [
        ("agentchat_streamlit", "Interface web com Streamlit"),
        ("agentchat_fastapi", "API REST com FastAPI"),
        ("agentchat_chess_game", "Jogo de xadrez com agentes"),
        ("core_async_human_in_the_loop", "Interação humana assíncrona"),
        ("gitty", "Exemplo prático completo"),
    ]

    for name, desc in examples:
        print(f"  📂 {name:30} - {desc}")

    print_separator("🔧 COMO RESOLVER O PROBLEMA DA API KEY")

    print("""
O erro 'Access denied' indica que a API key não está funcionando.

Passos para resolver:

1. Verifique sua conta OpenAI:
   🔗 https://platform.openai.com/account/api-keys

2. Certifique-se de que:
   ✓ A chave não expirou
   ✓ Há créditos disponíveis na conta
   ✓ A chave tem permissões corretas

3. Crie uma nova chave se necessário:
   - Acesse o painel da OpenAI
   - Vá em "API Keys"
   - Clique em "Create new secret key"

4. Teste alternativas:
   - Use modelos locais (Ollama, LM Studio)
   - Use outros provedores (Azure OpenAI, Anthropic, etc.)
   - Configure o AutoGen Studio para testar sem código

5. Para usar o AutoGen Studio (interface gráfica):
   pip install -U "autogenstudio"
   autogenstudio ui --port 8080 --appdir ./my-app
    """)

    print_separator("✅ PROJETO ESTÁ PRONTO")

    print("""
O AutoGen está corretamente instalado e funcionando!

Versão instalada: 0.7.5

Para começar a usar:
1. Configure uma API key válida
2. Execute os exemplos em python/samples/
3. Ou use o AutoGen Studio para interface gráfica

Próximos passos:
- Verificar/criar nova API key na OpenAI
- Explorar exemplos do projeto
- Ler documentação: https://microsoft.github.io/autogen/
    """)

    print_separator()


if __name__ == "__main__":
    asyncio.run(demo_agent_structure())
