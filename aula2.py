a = int(input('Entre com o primeiro valor: '))
b = int(input('Entre com o segundo valor: '))
print(type(a))
soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b
resto = a % b
resultado = ('Soma: {soma}. \nSubtração: {sub}. \nMultiplicação: {mul}. \nDivisão: {div}. \nResto: {res} '.format(soma=soma,
        sub=subtracao, res = resto, mul=multiplicacao, div = divisao))
print(resultado)

print('subtração: ' + str(subtracao))

# x = "1"
# soma2 = int(x) + 1
# print(soma2)
