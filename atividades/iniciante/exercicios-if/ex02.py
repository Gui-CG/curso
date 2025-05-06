#Exercício 02 - if Escreva um programa que peça a idade de uma pessoa e verifique se ela tem 18 anos ou mais. Se tiver, exiba a mensagem "Maior de idade". Caso contrário, exiba "Menor de idade".

age = int(input("Me diga sua idade: "))

if age >= 18:
    print("Maior de idade")
else:
    print("Menor de idade")