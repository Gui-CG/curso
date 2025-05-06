produtos = ['arroz', 'café', 'feijão', 'pipoca']

while True:
    opcao = str(input('''
                  [1] Cadastrar novo produto
                  [2] Remover produto
                  [3] Alterar nome do produto
                  [4] Ver todos os produtos
                  [5] Sair
                  Opção: ''')).lower()
    if '1' in opcao:
        novo_produto = str(input('Nome do produto a ser cadastrado: '))
        produtos.append(novo_produto)
    elif '2' in opcao:
        remover_produto = str(input('Produto que irá ser removido: '))
        produtos.remove(remover_produto)
    elif '3' in opcao:
        trocar_produto = str(input('Produto a ser trocado: '))
        produtos.remove(trocar_produto)
        novo_nome = str(input('Nome do produto: '))
        produtos.append(novo_nome)
    elif '4' in opcao:
        print('Produtos da lista atual')
        for produto in produtos:
            print(produto)
    elif '5' in opcao:
        break
    else:
        print('Opção inválida.')