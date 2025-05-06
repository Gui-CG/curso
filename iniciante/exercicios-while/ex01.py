#Exercício 01 Escreva um programa que peça ao usuário números inteiros positivos repetidamente, até que o usuário digite um número negativo. Quando isso acontecer, exiba a soma de todos os números digitados.

print("Me diga diversos números e eu irei fazer a soma de todos eles quando você encerrar o programa digitando um número negativo")

s = n = 0
while True:
    n = int(input("Me diga o número: "))
    if n < 0:
        print(f"A soma de todos os números digitados são {s}.")
        break
    s += n