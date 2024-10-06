nome = input('Digite uma palavra ou frase: ').upper().strip()
if 'A' not in nome:
    print(f'Não existe a letra "a", no que você digitou')
else:
    print(f'A palavra digitada foi {nome} e ela contem {nome.count('A')} "a" .')