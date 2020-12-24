from termcolor import colored

print(colored('''1.2 – Letras maiúsculas e minúsculas em nomes:\nArmazene o nome de uma pessoa em uma variável e 
então apresente o nome dessa pessoa em letras minúsculas,\nem letras maiúsculas e somente com a primeira letra 
maiúscula.''', 'yellow'))

nome = input('Digite seu nome:')
print(nome.title())
print(nome.lower())
print(nome.upper())
