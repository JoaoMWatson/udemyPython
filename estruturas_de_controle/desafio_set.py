# Quando for usar constantes usa maiuscula
PALAVRAS_PROIBIDAS = {'Futebo', 'religião', 'politica'}

textos = [
    'joão gosta de futebol e politica',
    'a priava foi divertida',
]

for texto in textos:
    intersecao = PALAVRAS_PROIBIDAS.intersection(set(texto.lower().split()))
    if intersecao:
        print('Texto possui palavras proibidas:'. intersecao)
    else:
        print('Texto autorizado:', texto)