#Peça um valor inteiro de 1 a 7 e diga qual é o dia da semana, sendo 1 domingo e 7 sábado.

semana = (
    'domingo',
    'segunda',
    'terça',
    'quarta'
    'quinta'
    'sexta'
    'sábado'
)
n = int(input('Diga um número: '))

if n == 1:
    d = semana[0]
elif n == 2:
    d = semana[1]
elif n == 3:
    d = semana[2]
elif n == 4:
    d = semana[3]
elif n == 5:
    d = semana[4]
elif n == 6:
    d = semana[5]
elif n == 7:
    d = semana[6]
else:
    print("Dia da semana inválido")
print(f'O dia da semana é {d}')