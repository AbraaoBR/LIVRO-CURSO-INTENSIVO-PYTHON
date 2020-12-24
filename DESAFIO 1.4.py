from termcolor import colored
print(colored('''1.4 – Citação famosa 2:\nRepita o Exercício 1.4, porém, desta vez, armazene o nome da pessoa famosa em uma variável chamada:\nPessoa_famosa.\nEm seguida, componha sua mensagem e armazene-a em uma nova variável chamada message.\nExiba sua mensagem.''', 'yellow'))

pessoa_famosa = input('Digite o autor da frase famosa:')
frase = input('Digite a frase dessa pessoa:')

print(colored('Frase de {}'.format(pessoa_famosa),'blue'))
print(colored('´´{}´´'.format(frase),'blue'))