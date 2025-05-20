#Exercício 03 Escreva um programa que peça ao usuário um número e calcule o fatorial desse número.".

print("Calculo Fatorial")

n = int(input("Número: "))

r = 1
c = 1

while c <= n:
    r *= c
    c += 1
print(f"O resultado da fatoriação do número {n} é: {r}")