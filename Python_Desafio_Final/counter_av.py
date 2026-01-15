from collections import Counter

def counter_avaliacao(entrada):
    avaliacoes = [item['Avaliacao'] for item in entrada]
    contador = Counter(avaliacoes)
    return contador