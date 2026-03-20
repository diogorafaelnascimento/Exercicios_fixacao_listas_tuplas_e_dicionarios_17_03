'''[TUPLE] Contar quantas vezes um número aparece
Tarefa: Leia quatro números inteiros e crie uma tupla. Depois leia um número e diga quantas vezes ele aparece na tupla.
 Orientações: 
método: tuple.count()
tipos: int, tuple'''
n1 = int(input('Digite o 1º número inteiro: '))
n2 = int(input('Digite o 2º número inteiro: '))
n3 = int(input('Digite o 3º número inteiro: '))
n4 = int(input('Digite o 4º número inteiro: '))
lista = (n1, n2, n3, n4)
n5 = int(input('Digite um número para verificar se está na tupla: '))
if n5 in lista:
    print(f'O número {n5} aparece {lista.count(n5)} vezes na lista.')
else:
    print(f'o número {n5} não consta na lista.')