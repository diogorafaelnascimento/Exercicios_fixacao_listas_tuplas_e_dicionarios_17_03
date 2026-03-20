'''[DICT  - desafio] Agenda (CRUD simples) com ordenação de nomes
Tarefa: Comece com agenda = {"Ana": "1111-1111", "Bruno": "2222-2222"}. 
Adicionar um novo contato (nome→telefone)
Atualizar o telefone de um contato informado (se existir)
Remover um contato pelo nome (se existir)
Exibir a lista ordenada de nomes de contatos
Tipos: str, dict, list (para a lista ordenada, 
se desejar armazenar).Conceitos: CRUD em dicionários, teste de existência, ordenação de chaves.Use: input(), 
acesso/atribuição agenda[nome] = tel, in, pop(), sorted(agenda.keys()), print()'''
agenda = {'Ana': '1111-1111',
          'Bruno': '2222-2222'
          }
print(agenda)
nome = input('Digite o nome que será adicinado na agenda: ')
tel = input(f'Digite o número de contato de {nome}: ')
agenda[nome] = tel
print(agenda)
remover = input('Digite um contato para remover da lista: ')
if remover in agenda:
    remover = agenda.pop(remover)
else:
    print('O contato informado não está na agenda')
print(agenda)
atualizar = input('Qual contato deseja alterar o número?')
if atualizar in agenda:
    agenda[atualizar] = input(f'Digite o novo número de {atualizar}: ')
else:
    print('O contato informado não está na agenda')
print(sorted(agenda.keys()))        