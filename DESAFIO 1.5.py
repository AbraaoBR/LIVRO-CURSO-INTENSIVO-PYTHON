from termcolor import colored

print(colored('''2.7 – Removendo caracteres em branco de nomes:\nArmazene o nome de uma pessoa e inclua alguns caracteres em branco no início e no final do nome.\nLembre-se de usar cada combinação de caracteres, "\ t" e "\ n", pelo menos uma vez.
Exiba o nome uma vez, de modo que os espaços em branco em torno do nome sejam mostrados.\nEm seguida, exiba o nome usando cada uma das três funções de remoção de espaços: lstrip(), rstrip() e strip().''','yellow'))

nome ='   Abraao    '
nome2 = '    Abraao'
nome3 = 'Abraao     '
print(nome)
#SEM ESPAÇOS
print(colored(nome.strip(), 'green'))

#SEM ESPAÇOS NA ESQUERDA
print(colored(nome2.lstrip()))

# SEM ESPAÇOS NA DIREITA
print(colored(nome3.rstrip(), 'red'))