# Configuração do AutoGen

Este guia explica como configurar e rodar o projeto AutoGen.

## Pré-requisitos

- Python 3.10 ou superior ✓ (instalado: 3.11.14)
- AutoGen 0.7.5 ✓ (instalado)

## Instalação

Os pacotes já foram instalados:
```bash
pip install -U "autogen-agentchat" "autogen-ext[openai]"
```

## Configuração da API Key

### ⚠️ IMPORTANTE: Segurança da API Key

**NUNCA** commite sua API key no repositório!

### Como configurar:

1. **Usando variável de ambiente (recomendado):**
   ```bash
   export OPENAI_API_KEY='sua-chave-aqui'
   ```

2. **Usando arquivo .env (alternativa):**
   ```bash
   echo "OPENAI_API_KEY='sua-chave-aqui'" > .env
   ```

3. **Verificar se a chave está funcionando:**
   ```bash
   python3 check_api_key.py
   ```

## Scripts Disponíveis

### 1. test_autogen.py
Verifica se o AutoGen está instalado corretamente.
```bash
python3 test_autogen.py
```

### 2. check_api_key.py
Valida se sua API key da OpenAI está funcionando.
```bash
export OPENAI_API_KEY='sua-chave-aqui'
python3 check_api_key.py
```

### 3. hello_autogen.py
Exemplo funcional de uso do AutoGen com agente real.
```bash
export OPENAI_API_KEY='sua-chave-aqui'
python3 hello_autogen.py
```

### 4. autogen_demo.py
Demonstração da estrutura e recursos do AutoGen.
```bash
python3 autogen_demo.py
```

## Problemas Comuns

### "Access denied" ao usar API key

Possíveis causas:
- API key expirada ou inválida
- Conta sem créditos disponíveis
- Restrições de uso na conta

**Solução:**
1. Acesse https://platform.openai.com/account/api-keys
2. Verifique se há créditos disponíveis
3. Crie uma nova API key se necessário

## Alternativas sem API Key

### AutoGen Studio (Interface Gráfica)
```bash
pip install -U "autogenstudio"
autogenstudio ui --port 8080 --appdir ./my-app
```

### Modelos Locais
- Ollama
- LM Studio
- LocalAI

## Exemplos do Projeto

Explore os exemplos em `python/samples/`:
- `agentchat_streamlit` - Interface web
- `agentchat_fastapi` - API REST
- `agentchat_chess_game` - Jogo de xadrez
- E muito mais!

## Recursos

- [Documentação Oficial](https://microsoft.github.io/autogen/)
- [Guia de Instalação](https://microsoft.github.io/autogen/stable/user-guide/agentchat-user-guide/installation.html)
- [Tutoriais](https://microsoft.github.io/autogen/stable/user-guide/agentchat-user-guide/tutorial/index.html)
