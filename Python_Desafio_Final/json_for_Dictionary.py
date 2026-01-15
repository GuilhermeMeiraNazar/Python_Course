import json

def converter_json_para_lista(texto_json):
    """
    Recebe uma string em formato JSON e retorna uma lista de dicionários.
    """
    try:
        # A função loads transforma a string em estrutura Python (lista/dicionário)
        lista_resultado = json.loads(texto_json)
        return lista_resultado
    except json.JSONDecodeError as e:
        print(f"Erro ao converter JSON: {e}")
        return None