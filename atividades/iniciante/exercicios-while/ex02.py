#Exercício 02 Escreva um programa que peça ao usuário 5 números e calcule a soma deles.

c = s = 0
print("Irei pedir para que você me fale 5 números para eu somar todos eles.")
while c != 5:
    n = int(input("Número: "))
    c += 1
    s += n
print(f'A soma dos seus 5 números é: {s}')