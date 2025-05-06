from random import choice
import os
opcoes = {
    'carro': ['camaro', 'porshe', 'skyline', 'supra', 'corsa', 'golf', 'gol', 'palio', 'corvette', 'ferrari'],
    'série': ['chaves', 'icarly', 'lucifer', 'friends', 'vikings'],
    'marca': ['nike', 'adidas', 'gucci', 'lacoste', 'zara', 'supreme', 'prada']
}
dica = choice(list(opcoes.keys()))
palavra = choice(opcoes[dica])
letras_certas = []
tentativas = 10
def cabecalho():
  print('-=' * 30)
  print('JOGO DA FORCA'.center(60))
  print('-=' * 30)
  print(f'Dica: é um(a) {dica}')
cabecalho()
while True:
  esquema = [letra if letra in letras_certas else '_' for letra in palavra]
  print(' '.join(esquema))
  
  if '_' not in esquema:
    print(f'Você acertou o {dica}! Parabéns.')
    break  
  
  letra = input('Letra: ').lower()
  if letra in palavra:
    letras_certas.append(letra)
    os.system('cls' if os.name == 'nt' else 'clear')
    cabecalho()
  else:
    os.system('cls' if os.name == 'nt' else 'clear')
    cabecalho()    
    tentativas -= 1
    print(f'Não tem essa letra! Tentativas restantes: {tentativas}')
  if tentativas == 0:
    print('_' * len(palavra))
    print(f'Você perdeu! o/a {dica} era {palavra}')
    break
