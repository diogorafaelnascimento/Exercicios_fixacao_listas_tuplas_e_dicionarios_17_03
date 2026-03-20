'''[TUPLE - desafio] Organizar valores sem mexer na tupla original
Tarefa: Leia quatro números em uma tupla e exiba: 
a tupla original
uma lista ordenada apenas para visualização
o tipo da variável ordenada
Objetivo: mostrar diferença entre tupla e lista sem precisar modificar nada.Use: sorted(), print(), type()'''
n1 = int(input('Digite o 1º número inteiro: '))
n2 = int(input('Digite o 2º número inteiro: '))
n3 = int(input('Digite o 3º número inteiro: '))
n4 = int(input('Digite o 4º número inteiro: '))
lista = (n1, n2, n3, n4)
print(lista, type(lista))
print(sorted(lista), type(sorted(lista)))