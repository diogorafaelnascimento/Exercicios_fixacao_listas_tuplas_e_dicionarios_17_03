'''[TUPLE] Exibir maior e menor valor
Tarefa: Leia quatro números inteiros, coloque em uma tupla e exiba o maior e o menor.
 Orientações: 
funções: max(), min()
tipos: int, tuple
conceito: operações básicas de agregação'''
n1 = int(input('Digite o 1º número inteiro: '))
n2 = int(input('Digite o 2º número inteiro: '))
n3 = int(input('Digite o 3º número inteiro: '))
n4 = int(input('Digite o 4º número inteiro: '))
lista = (n1, n2, n3, n4)
menor = min(lista)
maior = max(lista)
print(f'O menor valor da lista é {menor} e o maior valor é {maior}')