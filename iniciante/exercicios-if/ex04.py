#Verifique se os 3 números formam um triângulo

print("Irei verificar se os números citados formam um triângulo")

n1 = int(input('Diga o valor do 1° lado: '))
n2 = int(input('Diga o valor do 2° lado: '))
b = int(input("Diga o valor do 3° lado(base): "))
l = n1 + n2

if l > b:
    print("Formam um triângulo.")
else:
    print("Não é um triângulo.")