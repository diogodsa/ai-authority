#!/usr/bin/env python3
"""
Script para verificar se a API key da OpenAI está válida
"""
import os
from openai import OpenAI


def check_api_key():
    """Verifica se a API key está funcionando"""

    # Obter API key da variável de ambiente
    api_key = os.environ.get('OPENAI_API_KEY')

    if not api_key:
        print("❌ Erro: OPENAI_API_KEY não encontrada!")
        print("   Defina a variável de ambiente antes de executar:")
        print("   export OPENAI_API_KEY='sua-chave-aqui'")
        return

    print("🔍 Verificando API key da OpenAI...\n")

    try:
        client = OpenAI(api_key=api_key)

        # Tentar listar os modelos disponíveis
        print("📋 Tentando listar modelos disponíveis...")
        models = client.models.list()

        print("✅ API key válida!")
        print(f"\n📦 Modelos disponíveis: {len(list(models.data))} encontrados")

        # Listar alguns modelos
        print("\nPrimeiros modelos:")
        for i, model in enumerate(list(models.data)[:5]):
            print(f"  {i+1}. {model.id}")

    except Exception as e:
        print(f"❌ Erro ao verificar API key:")
        print(f"   Tipo: {type(e).__name__}")
        print(f"   Mensagem: {str(e)}")
        print("\n💡 Possíveis causas:")
        print("   - API key expirada ou inválida")
        print("   - Conta sem créditos disponíveis")
        print("   - Restrições de uso na conta")
        print("   - Problemas de conexão com a OpenAI")
        print("\n🔗 Verifique sua conta em: https://platform.openai.com/account/api-keys")


if __name__ == "__main__":
    check_api_key()
