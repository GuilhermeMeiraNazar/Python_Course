from llm_client import buscar_analise_llm
from json_for_Dictionary import converter_json_para_lista
from counter_av import counter_avaliacao 

caminho_arquivo = "data/Resenhas_App_ChatGPT.txt"

with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
    conteudo_input = arquivo.read()

resultado_json = buscar_analise_llm(conteudo_input)
resultado_dicionario = converter_json_para_lista(resultado_json)
resultado_counter = counter_avaliacao(resultado_dicionario)

resultado_final = f"{resultado_counter}\n\n{resultado_dicionario}"
print(resultado_final)
