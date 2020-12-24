from termcolor import colored

print(colored(
    '''1.3 – Citação famosa:\nEncontre uma citação de uma pessoa famosa que você admire.\nExiba a citação e o nome do autor.\nSua saída deverá ter a aparência a seguir, incluindo as aspas:''',
    'yellow'))
print(
    colored('''\tAlbert Einstein certa vez disse: “Uma pessoa que nunca cometeu um erro jamais tentou nada.''', 'blue'))

citacao = input('Digite a citação:')
autor = input('Digite o nome do autor:')

print(colored(' ´´{}´´'.format(citacao), 'green'))
print(colored('\t- {}'.format(autor), 'green'))
