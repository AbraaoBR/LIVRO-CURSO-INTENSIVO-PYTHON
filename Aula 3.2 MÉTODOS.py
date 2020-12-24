from termcolor import colored

nome =  '     ''Abraao Wendel''       '
nome2 = 'Abraao Wendel         '
nome3 = '    Abraao Wendel'
print(colored(nome.strip(), 'yellow'))
print(colored(nome2.rstrip(), 'yellow'))
print(colored(nome3.lstrip(), 'yellow'))

# O Método .strip remove espaços em branco das variaveis.
# O Método r.strip remove espaços em branco do lado direito.
# O Método l.strip remove espaços em branco do lado esquerdo.


# DICA, para quebrar uma linha digite \n junto a string.
print('Python é a melhor\nJava é a segunda melhor\nC é terceira melhor')

# DICA, para fazer tabulação digite \t junto a string.
print('\tPython é a melhor')

