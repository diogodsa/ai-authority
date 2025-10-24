#!/usr/bin/env python3
"""
Exemplo funcional do AutoGen com um agente assistente
"""
import asyncio
import os
from autogen_agentchat.agents import AssistantAgent
from autogen_ext.models.openai import OpenAIChatCompletionClient


async def main() -> None:
    """Exemplo básico de uso do AutoGen"""

    # Configurar API key (defina como variável de ambiente antes de executar)
    # export OPENAI_API_KEY='sua-chave-aqui'
    if 'OPENAI_API_KEY' not in os.environ:
        print("❌ Erro: OPENAI_API_KEY não encontrada!")
        print("   Defina a variável de ambiente antes de executar:")
        print("   export OPENAI_API_KEY='sua-chave-aqui'")
        return

    print("🚀 Iniciando AutoGen...\n")

    # Criar o cliente do modelo
    model_client = OpenAIChatCompletionClient(
        model="gpt-3.5-turbo",  # Usando modelo padrão
    )

    # Criar o agente assistente
    agent = AssistantAgent(
        name="assistant",
        model_client=model_client,
        system_message="Você é um assistente útil e amigável que responde em português."
    )

    # Executar uma tarefa simples
    print("📝 Tarefa: Diga 'Olá, mundo!' em 3 idiomas diferentes\n")

    result = await agent.run(task="Diga 'Olá, mundo!' em 3 idiomas diferentes (português, inglês e espanhol)")

    print("✅ Resposta do agente:")
    print("-" * 50)
    print(result)
    print("-" * 50)

    # Fechar o cliente
    await model_client.close()

    print("\n✨ Teste concluído com sucesso!")


if __name__ == "__main__":
    asyncio.run(main())
