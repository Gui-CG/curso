nums = [
    [],
    []
    ]

for linha in range(len(nums)):
    for c in range(2):
        l1 = input(f'Digite um valor para a posição [{linha}][{c}]: ')
        nums[linha].append(l1)


for linha in range(len(nums)):
    for coluna in range(len(nums[linha])):
        print(f'{nums[linha][coluna]}', end=' ')
    print('')
