#Exercício 03 - if Escreva um programa que peça uma nota de 0 a 10 e verifique se a nota é maior ou igual a 7. Se for, exiba "Aprovado". Caso contrário, exiba "Reprovado".

n = int(input('Diga uma nota de 0 a 10: '))

if n >= 7:
    print("aprovado")
else:
    print("reprovado")