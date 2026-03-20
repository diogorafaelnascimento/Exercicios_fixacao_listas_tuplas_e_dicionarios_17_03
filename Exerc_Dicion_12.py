'''[TUPLE] Acessar elementos da tupla
Tarefa: Leia três frutas e coloque em uma tupla. Depois leia uma fruta e diga se ela está ou não na tupla.
 Orientações: 
usar in
usar input()
tipo: str, tuple
conceito: operador de pertinência'''
fruta1 = input('Digite o nome da primeira fruta: ')
fruta2 = input('Digite o nome da segunda fruta: ')
fruta3 = input('Digite o nome da terceira fruta: ')
lista = (fruta1, fruta2, fruta3)
print(lista)
fruta4 = input('Digite uma fruta para verificar se está na lista: ')
if fruta4 in lista:
    print(f'{fruta4} está na lista!')
else:
    print(f'{fruta4} não está na lista!')