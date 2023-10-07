import random

print('Bem-vindes ao GERADOR DE SENHA.')

chars = 'abcdefghijklmnopqrstuvwxyzQWERTYUIOPASDFGHJKLZXCVBNM!@#$%&*()_+'

number = input('Quantas senhas devo gerar pra vc: ')
number = int(number)

length = input('Quantos caracteres para cada senha: ')
length = int(length)

print('\nSenhas criadas: ')

for pwd in range(number):
    passwords = ''
    for c in range(length):
        passwords += random.choice(chars)
    print(passwords)

