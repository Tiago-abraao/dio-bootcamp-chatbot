import json
from orders import buscar_pedido_completo


def executar_ferramenta(nome, argumentos):

    if nome == "buscar_pedido_completo":

        resultado = buscar_pedido_completo(
            argumentos["numero_pedido"]
        )

        return json.dumps(resultado, ensure_ascii=False)

    return json.dumps(
        {"erro": "Ferramenta não encontrada."},
        ensure_ascii=False
    )

