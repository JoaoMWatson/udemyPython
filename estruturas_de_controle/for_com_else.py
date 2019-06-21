# Quando for usar constantes usa maiuscula
PALAVRAS_PROIBIDAS = ('Futebol', 'religião', 'politica')

textos = [
    'joão gosta de futebol e politica',
    'a prai foi divertida',
]

for texto in textos:
    for palavra in texto.lower().split():
        if palavra in PALAVRAS_PROIBIDAS:
            print('Texto possui pelo menos uma palavra proibida: ', palavra)
            break

    else:
        print('Texto autorizado', texto)
