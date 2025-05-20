matriz = [
    [],
    []
    ]
nums = []
for linha in range(len(matriz)):
    for c in range(2):
        l1 = int(input(f'Digite um valor para a posição [{linha}][{c}]: '))
        matriz[linha].append(l1)
        nums.append(l1)

for linha in range(len(matriz)):
    for coluna in range(len(matriz[linha])):
        print(f'{matriz[linha][coluna]}', end=' ')
    print('')

soma = 0

for num in nums:
    soma += num

print("A soma de tudo isso é: ", soma)