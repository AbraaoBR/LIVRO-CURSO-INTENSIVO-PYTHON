from termcolor import colored
# FAÇA VOCÊ MESMO

print(colored('''1 – Mensagem pessoal:\nArmazene o nome de uma pessoa em uma variável e apresente uma mensagem a essa pessoa.\nSua mensagem deve ser simples.\nComo: 'Alô Eric, você gostaria de aprender um pouco de Python hoje?'.''', 'yellow'))

nome = input('Qual o nome da pessoa?')
print(colored('Alô {}, gostaria de aprender PYTHON 3 ?'.format(nome), 'blue'))