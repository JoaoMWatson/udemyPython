# Caso tenha uma variavel que n esteja sendo usada, coloca _ no nome da variavel

def fibonacci(quantidade):
    resultado = [0, 1]
    for _ in range (2, quantidade):
   #for _ in range (quantidade - 2) Segunda possibilidade
        resultado.append(sum(resultado[-2:]))
    return resultado

if __name__ == '__main__':
    #listas os 20 primeiros numeros da sequencia
    for fib in fibonacci(20):
        print(fib, end=',')  
