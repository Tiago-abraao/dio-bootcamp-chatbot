
pedidos = [
    {
        "numero": 1001,
        "produto": "Mouse sem fio",
        "status": "Entregue"
    },
    {
        "numero": 1002,
        "produto": "Headset sem fio",
        "status": "Em transporte"
    },
    {
        "numero": 1003,
        "produto": "Teclado mecânico",
        "status": "Preparando envio"
    }
]


def buscar_pedido(numero_pedido):

    for pedido in pedidos:

        if pedido["numero"] == numero_pedido:
            return pedido

    return None



def consultar_pedido(numero_pedido):

    pedido = buscar_pedido(numero_pedido)

    # Verifique se o pedido não foi encontrado
    if pedido is None:
        return "Pedido não encontrado."

    # Se encontrou, retorne produto e status
    return f"Encontrei o seu pedido {pedido['numero']}!\nProduto: {pedido['produto']}\nStatus: {pedido['status']}" 



def realizar_consulta():

 while True:

    try:
        entrada_dados = input("Digite o número do pedido: ")

        print(consultar_pedido(int(entrada_dados)))

        break

    except ValueError:
        print("Número inválido. Tente novamente.")

 
realizar_consulta()
