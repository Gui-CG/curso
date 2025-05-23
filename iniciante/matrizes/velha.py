preview = [
    ['-', '-', '-'],
    ['-', '-', '-'],
    ['-', '-', '-']
]

def esquema():
    for linha in range(len(preview)):
        for coluna in range(len(preview[linha])):
            print(preview[linha][coluna], end='|')
        print('')
        
esquema()

while True:
    print("Vez do Player1.")
    l1 = int(input('Linha: ')) -1
    c1 = int(input('Coluna: ')) -1
    preview[l1][c1] = 'x'
    esquema()
    print('Vez do Player2.')
    l2 = int(input('Linha: ')) -1
    c2 = int(input('Coluna: ')) -1
    preview[l2][c2] = '0'
    esquema()
