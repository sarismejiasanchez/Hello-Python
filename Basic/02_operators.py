# Operadores

## Operadores Aritméticos ##

# Operaciones con Enteros
print(3 + 4)    # Adicion
print(3 - 4)    # Sustracción
print(3 * 4)    # Multiplicación
print(3 / 4)    # División
print(10 % 2)   # Modulo
print(10 // 3)  # División Entera
print(3 ** 4)   # Exponenciación
print(2 ** 3 + 3 - 7 / 1 // 4)

# Operaciones con Cadenas de Texto
print("Hola" + "Python")
print("Hola " +  str(5))    # Convertimos a str el entero

# Operaciones Mixtas
print("Hola " * 5)
print("Hola " * (2 ** 3))
#print("Hola " * 2.5)       # TypeError: can't multiply sequence by non-int of type 'float'
#print("Hola " + 5)         # TypeError: can only concatenate str (not "int") to str

my_float = 2.5 * 2
print("Hola " * int(my_float))

## Operadores de Comparacion ##

# Operaciones con enteros
print(3 == 4)       # False
print(3 != 4)       # True
print(3 > 4)        # False
print(3 < 4)        # True
print(3 >= 4)       # False
print(3 <= 4)       # True
print(3 > 4 == 2)   # False

# Operaciones con cadenas de texto
# Comprueba ordenación alfabética teniendo en cuenta las mayúsculas
print(f"Hola > Python: {"Hola" > "Python"}")        # False
print(f"Hola < Python: {"Hola" < "Python"}")        # True
print(f"Hola >= Python: {"Hola" >= "Python"}")      # False
print(f"Hola <= Python: {"Hola" <= "Python"}")      # True
print(f"Hola == Python: {"Hola" == "Python"}")      # False
print(f"Hola != Python: {"Hola" != "Python"}")      # True
print(f"aaa >= abaa: {"aaaa" >= "abaa"}")           # Ordenación alfabética por ASCII
print(f"{len("aaaa")} >= {len("abaa")}: {len("aaaa") >= len("abaa")}")  # Cuenta caracteres

## Operadores Lógicos ##
print(3 > 2 and 4 > 3) # True - because both statements are true
print(3 > 2 and 4 < 3) # False - because the second statement is false
print(3 < 2 and 4 < 3) # False - because both statements are false
print('True and True: ', True and True)
print(3 > 2 or 4 > 3)  # True - because both statements are true
print(3 > 2 or 4 < 3)  # True - because one of the statements is true
print(3 < 2 or 4 < 3)  # False - because both statements are false
print('True or False:', True or False)
print(not 3 > 2)     # False - because 3 > 2 is true, then not True gives False
print(not True)      # False - Negation, the not operator turns true to false
print(not False)     # True
print(not not True)  # True
print(not not False) # False