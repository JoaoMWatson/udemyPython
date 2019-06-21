# Quando for usar constantes usa maiuscula
PALAVRAS_PROIBIDAS = ('Futebo', 'religião', 'politica')

textos = [
    'joão gosta de futebol e politica',
    'a priava foi divertida',
]

for texto in textos:
    found = False
    for palavra in texto.lower().split():
        if palavra in PALAVRAS_PROIBIDAS:
            print('Texto possui pelo menos uma palavra proibida: ', palavra)
            found = True
            break

    if not found:
        print('Texto autorizado', texto)
