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

#Python podemos representar números inteiros muito grande sem apresentar problemas (como em C++).
import math

fatorial_30 = math.factorial(30)
print(fatorial_30)

# Em Python as variáveis numéricas são imutáveis - uma vez criadas, elas não podem ser modificadas. 

# Segue exemplo:
a = 5
b = a  # 'b' agora tem o mesmo valor que 'a'
a = 10  # 'a' recebe um novo valor, 'b' não é afetado
print(b)  # Ainda será 5, porque 'b' manteve seu valor original

# Métodos Disponíveis para Variáveis Inteiras:
# Variáveis inteiras em Python pertencem à classe int,
# Elas têm métodos associados a elas. 
# Seguem alguns exemplos de métodos disponíveis:

x = 42

# Converter para string
str_x = str(x)
print(str_x)  # '42'

# Verificar se é par
is_even = x % 2 == 0
print(is_even)  # True

# Calcular o valor absoluto
abs_x = abs(x)
print(abs_x)  # 42

# Obter o tamanho em bytes
size_in_bytes = x.bit_length() // 8
print(size_in_bytes)  # 1 (para 42)

# Método para converter para hexadecimal
hex_x = hex(x)
print(hex_x)  # '0x2a'

# Método para converter para binário
bin_x = bin(x)
print(bin_x)  # '0b101010'

# Método para converter para octal
oct_x = oct(x)
print(oct_x)  # '0o52'

# Método para verificar se o número é ímpar
is_odd = x.__bool__()  # Retorna True para números ímpares e False para números pares
print(is_odd)  # True

# Método para encontrar o máximo com outro número
y = 30
max_value = x.__max__(y)
print(max_value)  # 42

# Método para encontrar o mínimo com outro número
min_value = x.__min__(y)
print(min_value)  # 30

# Método para arredondar o número para cima
rounded_up = x.__ceil__()
print(rounded_up)  # 42

# Método para arredondar o número para baixo
rounded_down = x.__floor__()
print(rounded_down)  # 42

# Método para verificar se o número é negativo
is_negative = x.__neg__()  # Retorna x se for positivo, caso contrário, -x
print(is_negative)  # -42

