#Exercício 01 Escreva um programa que peça a idade de uma pessoa. Se a idade for maior ou igual a 18, verifique se é menor que 60. Se for, exiba "Adulto". Se for 60 ou mais, exiba "Idoso". Se a idade for menor que 18, exiba "Menor de idade".

age = int(input("Me diga sua idade: "))

if age >= 18 and age < 60:
    print("Você é adulto")
elif age > 60:
    print("Você é idoso")
else:
    print("Menor de idade")