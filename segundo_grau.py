#inserindo os valores dos coeficientes da equação do segundo grau

print('########################################  CALCULANDO AS EQUAÇÕES DE UMA EQUAÇÃO DO SEGUNDO GRAU  ########################################')

nome = input('Como gostaria de ser chamado?   ')
print('{} deverá serguir as orientações do programa para determinar as soluções da equação do segundo grau, caso elas existem'.format(nome))

print('##########################################################################')
a = float(input('Digite o valor do coeficiente a : '))

if a != 0:
    print('Excelente ! Para que existe uma equação do segundo grau é necessário que o coeficiente a seja diferente de zero')
else:
    print('A condição de existência de uma equação do segundo grau é que o coeficiente a seja diferente de zero. Por favor, insira outro valor. ')
    a = float(input('Insira o valor do coeficiente a: '))
print('##########################################################################')
b = float (input('Insira o valor do coeficiente b: '))
print('##########################################################################')
c = float (input('Insira o valor do coeficiente c: '))
print('##########################################################################')
#considerando que os coeficientes b e c sejam iguais a zero
if b == c == 0:
    print('É uma equação do segundo grau especial, cuja  solução é zero')
    quit()
#considerando que a equação tenha o coeficiente c igual a zero:
    if  b != 0 and c != 0:
        print('É uma equação do segundo grau incompleto, cujo coefiente c vale zero. Essa equação possui duas raízes reais')
#calculando o valor do discriminante (delta)
print('{}, o próximo passo será calcular o valor do Delta'.format(nome))
delta = float(b**2-4*a*c)
print('Delta é igual a {}'.format(delta))
if delta == 0:
    print('Como Delta é igual a zero, sua equação possui apenas uma raíz real')
elif delta > 0:
    print('Como Delta é maior que zero, sua equação possui duas raízes reais.')
else:
    print('Como sua raíz é negativa, sua equação do segundo grau não possui solução real')
    print('{}, o programa será finalizado. Obrigado por utilizar'.format(nome))
    quit()

#calculando as raízes da equação do segundo grau
print('Calculando a raiz, ou raízes da equação dada: ')
x1 = float((-b+delta**0.5)/(2*a))
x2 = float((-b-delta**0.5)/(2*a))
if x1 == x2:
    print('Como Delta é igual a zero, a equação dada possui uma raiz real, sendo igual a {}'.format(x1))
else:
    print('Como Delta é diferente de zero, a equação dada possui duas raízes reais, sendo  {} e {} suas respectivas soluções reais'.format(x1,x2,x2))