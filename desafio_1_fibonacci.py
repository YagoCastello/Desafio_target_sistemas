primeiro = 0
segundo = 1
contador = 0
lista = []
resposta = int(input('Você deseja ver quantos número da sequência de fibonacci? '))
numero = int(input('Você deseja saber encontrar algum número nessa sequência?'))
while True:
    contador +=1
    terceiro = primeiro + segundo
    lista.append(terceiro)
    print(primeiro,' + ',segundo,' = ',terceiro)
    primeiro = segundo
    lista.append(primeiro)
    segundo = terceiro
    lista.append(segundo)
    if contador == resposta:
        break 

if numero in lista:
    print(f'O número {numero} existe na sequência!!')
else:
    print(f'O número {numero} NÃO existe na sequência!!')