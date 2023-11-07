# Operadores aritméticos 
# Em Python, os operadores aritméticos funcionam de forma parecida ao C++.
# Suas diferênças são pontuadas com a divisão de inteiros que produz um número de ponto flutuante, e
# a capacidade de representar inteiros muito grandes sem preocupações com bug's. 

# Aqui estão exemplos:

# Operadores aritméticos
a = 10
b = 3

soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b  # Resultado é float
divisao_inteira = a // b
resto = a % b
potencia = a ** b

print(soma)  # 13
print(subtracao)  # 7
print(multiplicacao)  # 30
print(divisao)  # 3.3333333333333335
print(divisao_inteira)  # 3
print(resto)  # 1
print(potencia)  # 1000

# Operadores compostos
c = 5
c += 2
print(c)  # 7

#Python podemos representar números inteiros muito grande
import math

fatorial_30 = math.factorial(30)
print(fatorial_30)

# Em Python as variáveis numéricas são imutáveis - uma vez criadas, elas não podem ser modificadas. 

# Segue exemplo:
a = 5
b = a  # 'b' agora tem o mesmo valor que 'a'
a = 10  # 'a' recebe um novo valor, 'b' não é afetado
print(b)  # Ainda será 5, porque 'b' manteve seu valor original
