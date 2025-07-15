# if / elif / else
# se / se não se / se não

entrada = input('Você quer "entrar" ou "sair"? ')

if entrada.upper() == 'ENTRAR':
    print('Você entrou no sistema')
elif entrada.upper() == 'SAIR':
    print('Você saiu do sistema')
else:
    print('Você não digitou nem "entrar" nem "sair"')
