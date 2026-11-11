import sqlite3
from database import conectar


def buscar_pedido(numero_pedido):
    conexao = None
    pedido = None

    try:
        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute(
            "SELECT * FROM pedidos WHERE numero = ?",
            (numero_pedido,),
        )

        pedido = cursor.fetchone()
    finally:
        if conexao is not None:
            conexao.close()

    return pedido


def consultar_pedido(numero_pedido):
    pedido = buscar_pedido(numero_pedido)

    # Verifique se o pedido não foi encontrado
    if pedido is None:
        return "Pedido não encontrado."

    # Se encontrou, retorne produto e status
    return f"Encontrei o seu pedido {pedido[0]}!\nProduto: {pedido[1]}\nStatus: {pedido[2]}"


def realizar_consulta():
    while True:
        try:
            entrada_dados = input("Digite o número do pedido: ")
            print(consultar_pedido(int(entrada_dados)))
            break
        except ValueError:
            print("Número inválido. Tente novamente.")


if __name__ == "__main__":
    realizar_consulta()
