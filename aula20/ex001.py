primeiroValor = input('Digite um valor: ')
segundoValor = input('Digite outro valor: ')

if primeiroValor > segundoValor:
    print(f'O primeiro valor ({primeiroValor}) é maior que o segundo valor ({segundoValor})')
elif segundoValor > primeiroValor:
    print(f'O segundo valor ({segundoValor}) é maior que o primeiro valor ({primeiroValor})')
else:
    print('Os valores são iguais')