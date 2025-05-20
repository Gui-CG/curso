nums = [
    [0,1,2],
    [3,4,5],
    [6,7,8]
    ]

for linha in range(len(nums)):
    for coluna in range(len(nums[linha])):
        print(f'{nums[linha][coluna]}', end=' ')
    print('')
