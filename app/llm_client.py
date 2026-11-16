import json
import os
from tools import executar_ferramenta
from dotenv import load_dotenv
from groq import Groq


# Carrega as variáveis de ambiente
load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

client = Groq(api_key=api_key)


# Instruções principais do agente
SYSTEM_PROMPT = """
Você é o atendente virtual da TopTech, uma loja fictícia de eletrônicos.

Seja cordial, objetivo e profissional.

REGRAS:
- Nunca invente prazos, descontos ou políticas comerciais.
- Nunca prometa reembolso ou reenvio.
- Nunca afirme que consultou um pedido sem utilizar uma ferramenta real.
- Encaminhe solicitações de reembolso para atendimento humano.
- Não invente transportadoras ou códigos de rastreamento.
"""


# Descrição das ferramentas disponíveis para a IA
tools = [
    {
        "type": "function",
        "function": {
            "name": "buscar_pedido_completo",
            "description": "Consulta um pedido pelo número e retorna seus dados.",
            "parameters": {
                "type": "object",
                "properties": {
                    "numero_pedido": {
                        "type": "integer",
                        "description": "Número do pedido do cliente."
                    }
                },
                "required": ["numero_pedido"]
            }
        }
    }
]


# Histórico da conversa
historico = [
    {
        "role": "system",
        "content": SYSTEM_PROMPT
    }
]



# Consulta a IA

def consultar_ia(mensagem):

    historico.append({
        "role": "user",
        "content": mensagem
    })

    resposta = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=historico,
        tools=tools,
        tool_choice="auto"
    )

    mensagem_resposta = resposta.choices[0].message

    # Verifica se a IA solicitou alguma ferramenta
    if mensagem_resposta.tool_calls:

        # Guarda a solicitação da IA no histórico
        historico.append(
            mensagem_resposta.model_dump(exclude_none=True)
        )

        # Percorre as ferramentas solicitadas
        for ferramenta in mensagem_resposta.tool_calls:

            nome = ferramenta.function.name

            argumentos = json.loads(
                ferramenta.function.arguments
            )

            print("Executando ferramenta:", nome)
            print("Argumentos:", argumentos)

            # Executa a função Python
            resultado = executar_ferramenta(
                nome,
                argumentos
            )

            print("Resultado:", resultado)

            # Devolve o resultado para a IA
            historico.append({
                "role": "tool",
                "tool_call_id": ferramenta.id,
                "content": resultado
            })

        # Solicita à IA uma resposta usando o resultado
        resposta_final = client.chat.completions.create(
            model="openai/gpt-oss-20b",
            messages=historico,
            tools=tools,
            tool_choice="auto"
        )

        conteudo = resposta_final.choices[0].message.content

        historico.append({
            "role": "assistant",
            "content": conteudo
        })

        return conteudo

    # Caso a IA não solicite ferramentas
    conteudo = mensagem_resposta.content

    historico.append({
        "role": "assistant",
        "content": conteudo
    })

    return conteudo
