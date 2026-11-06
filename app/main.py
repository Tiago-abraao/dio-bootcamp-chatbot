def identificar_solicitacao(mensagem):

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

mensagem = input("Como podemos ajudar? ")

mensagem = mensagem.lower()

resposta = identificar_solicitacao(mensagem)

print(resposta)