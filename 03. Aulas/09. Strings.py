''' Strings é um tipo de dado em que se armazena coleções de caracteres (Texto)
São Declaraas entre aspas
Var1 = 1
Var2 = "2"

Nesse exemplo Var1 é um numeral, enquanto Var2 é uma String (Texto)'''

a = 2
b = 3
Var1 = 1
Var2 = 2
concatenar1 = a + b
concatenar2 = Var1 + Var2

print(concatenar1)
print(concatenar2)

x = "Leonardo"
y = "Teixeira"

concatenar3 = x + " " + y

print(concatenar3) # Junta x + y = Leonardo Teixeira

print(x[0]) # imprime so o caractere 0
print(x[1]) # imprime so o caractere 1
print(x[2]) # imprime so o caractere 2

print(concatenar3[0:5]) # imprime do caractere 0 ao 5

print(concatenar3.lower()) # Imprime em minusculo

print(concatenar3.upper()) # Imprime em Maiusculo

z = "\n" # Caracter especial de quebra de linha

minha_string = "O rato roeu a roupa do rei de Roma"

minha_lista = minha_string.split("r") # vai imprimir sem os r, letras maiuculas e minusculas sao diferentes
print(minha_lista)

#Case sensitive


busca = minha_string.find("rei") # vai buscar onde aparece a palavra rei
print(busca)

print(minha_string[busca:])