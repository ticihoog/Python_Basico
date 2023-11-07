# Parte 1: Imprimir caracteres numéricos e seus códigos numéricos
print("Parte 1:")
for i in range(10):
    char = chr(48 + i)
    code = ord(char)
    print(f"'{char}' - {code}")
