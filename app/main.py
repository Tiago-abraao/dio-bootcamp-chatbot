
from llm_client import consultar_ia


def identificar_solicitacao(mensagem):
    mensagem = mensagem.lower()

    if "atendente" in mensagem:
        return "Você deseja atendimento humano."
    elif "atrasado" in mensagem:
        return "Identificamos um problema com a entrega."
    elif "cancelar" in mensagem:
        return "Sua solicitação envolve um cancelamento."
    elif "diferente" in mensagem:
        return "Vamos verificar o produto recebido."
    elif "quebrado" in mensagem:
        return "Vamos verificar o problema com seu produto."
    else:
        return "Não conseguimos identificar sua solicitação."


if __name__ == "__main__":
    print("TopTech AI — Atendimento iniciado!")
    print("Digite 'sair' para encerrar.\n")

    while True:
        mensagem = input("Você: ")

        if mensagem.lower() == "sair":
            print("Atendimento encerrado!")
            break

        resposta = consultar_ia(mensagem)
        print(f"\nTopTech AI: {resposta}\n")
