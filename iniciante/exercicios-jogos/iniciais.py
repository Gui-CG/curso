import string

letras = list(string.ascii_lowercase)
palavras = [
    "amor",     
    "bola",     
    "casa",     
    "dado",     
    "elefante", 
    "fogo",     
    "gato",     
    "homem",    
    "igreja",   
    "janela",   
    "kiwi",     
    "luz",      
    "mesa",   
    "navio",
    "olho",     
    "pato",     
    "queijo",   
    "rosa",     
    "sapato",   
    "tigre",    
    "urso",     
    "vaca",     
    "watt",     
    "xadrez",   
    "yeti",   
    "zebra"     
]
letra = str(input('Letra: '))
for palavra in palavras:
  inicial = palavra[0]
  if inicial == letra:
    print(palavra)