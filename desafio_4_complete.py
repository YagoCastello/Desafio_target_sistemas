print("""
      a) 1, 3, 5, 7, 9
      b) 2, 4, 8, 16, 32, 64, 128
      c) 0, 1, 4, 9, 16, 25, 36, 49
      d) 4, 16, 36, 64, 100
      e) 1, 1, 2, 3, 5, 8, 13
      f) 2, 10, 12, 16, 17, 18, 19, 20
      """)
print('Script para a questão a)')
n1 = 1
for c in range(0,5):
    print(f'{n1}',end=' ')
    n1 += 2
    
print(' ')
print(' ')  
print('Script para a questão b)')
n2 = 2 
for c in range(0,7):
    print(f'{n2}',end=' ')
    n2 *= 2
    
print(' ')  
print(' ')   

print('Script para a questão c)')
n3 =0
for c in range(0,8):
    n3 = c ** 2
    print(f'{n3}',end=' ')
    
print(' ')  
print(' ')   

print('Script para a questão d)')
n4 =0
for c in range(2,11):
    if c%2 ==0:
        n4 = c ** 2
        print(f'{n4}',end=' ')
    
print(' ')  
print(' ') 





print('Script para a questão e)')


primeiro = 0
segundo = 1
for c in range(0,6):
    terceiro = primeiro + segundo
    print(primeiro,' + ',segundo,' = ',terceiro)
    primeiro = segundo
    segundo = terceiro
    

print(' ')  
print(' ') 





print('Script para a questão f)')
lista = [2, 10, 12, 16, 17, 18, 19, 20]
for c in range(0,21):
    if c in lista:
        print(f'{c}, ',end=' ')