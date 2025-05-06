#Exercício 03Escreva um programa que peça uma senha ao usuário. Se a senha for "admin", peça uma segunda verificação para confirmar a senha. Se a confirmação também for "admin", exiba "Acesso permitido". Caso contrário, exiba "Senha incorreta".

s = str(input("Me diga a senha: "))

if s == 'admin':
    v = str(input("Confirme a senha: "))
    if v == 'admin':
        print("Acesso liberado")
    else:
        print('Acesso negado')
else:
    print('Acesso negado')