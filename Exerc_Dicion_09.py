'''[DICT - desafio] Atualizar preço e quantidade; calcular o total 
Tarefa: Leia produto = {"nome": str, "preco": float, "quantidade": int}. Aplique aumento percentual ao preço e some 2 unidades na quantidade. 
Calcule total = preco * quantidade e exiba.
 Use: float(), int(), input(), acesso/atribuição por chave, print()
 Tipos: str, float, int, dict.
 Conceitos: operadores aritméticos (*, +), atualização de valores no dict.'''
produto = {'nome': '',
        'preco': 0,
        'quantidade': 0
        }
produto['nome'] = input('Digite o nome do produto: ')
produto['preco'] = float(input('Digite o valor do produto: '))
produto['quantidade'] = int(input('Digite a quantidade: '))
print(produto)
percentual = float(input('Digite o percentual de aumento do produto: '))
percentual = 1 + (percentual / 100)
soma = int(input('Quantos itens serão inseridos no estoque? '))
produto['quantidade'] = produto['quantidade'] + soma
produto['preco'] = produto['preco'] * percentual 
print(produto)