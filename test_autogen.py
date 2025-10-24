#!/usr/bin/env python3
"""
Exemplo básico para testar a instalação do AutoGen
"""
import asyncio

# Teste de importação dos módulos principais
try:
    from autogen_agentchat.agents import AssistantAgent
    from autogen_ext.models.openai import OpenAIChatCompletionClient
    from autogen_core import __version__ as core_version
    from autogen_agentchat import __version__ as agentchat_version
    from autogen_ext import __version__ as ext_version

    print("✓ AutoGen instalado com sucesso!")
    print(f"  - autogen-core: {core_version}")
    print(f"  - autogen-agentchat: {agentchat_version}")
    print(f"  - autogen-ext: {ext_version}")
    print()

    print("Módulos importados com sucesso:")
    print("  ✓ AssistantAgent")
    print("  ✓ OpenAIChatCompletionClient")
    print()

    print("Para usar o AutoGen com modelos de IA, você precisará:")
    print("  1. Configurar uma API key (OpenAI, Azure, etc.)")
    print("  2. Criar um client de modelo (ex: OpenAIChatCompletionClient)")
    print("  3. Criar agentes usando o client")
    print()

    print("Exemplo de uso:")
    print("""
    # Defina sua API key
    import os
    os.environ['OPENAI_API_KEY'] = 'sua-api-key-aqui'

    # Crie um client
    model_client = OpenAIChatCompletionClient(model="gpt-4o")

    # Crie um agente
    agent = AssistantAgent("assistant", model_client=model_client)

    # Execute uma tarefa
    result = await agent.run(task="Olá, AutoGen!")
    print(result)
    """)

except ImportError as e:
    print(f"✗ Erro ao importar módulos do AutoGen: {e}")
    exit(1)
