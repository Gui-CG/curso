#Exercício 02 Escreva um programa que peça ao usuário um número. Verifique se o número é par. Se for, verifique se é maior que 10. Se for maior que 10, exiba "Número par e maior que 10". Caso contrário, exiba "Número par e menor ou igual a 10".

n = int(input("Me diga um número e eu irei verificar se é par e maior que 10 ou se ele é impar"))

if n % 2 == 0:
    if n > 10:
       print("par e maior que 10")
    else:
        print('par e menor ou igual a 10')
else:
    print("impar")