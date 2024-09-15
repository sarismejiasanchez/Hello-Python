# Variables

"""
Por convención del lenguaje:
- Cada palabra en minuscula debe estar separada por guión bajo (snake_case)
- Pueden comenzar por letras o por guión bajo
- No pueden comenzar por números
- Puede contener caracteres alfanuméricos
"""

my_string_variable = "Esta es una variable"
print(my_string_variable)

my_other_string_variable = 'Esta tambien es una variable string'
print(my_other_string_variable)

my_int_variable = 5
print(my_int_variable)

my_bool_variable = True
print(my_bool_variable)

# Concatenación de variables en un print
print(my_string_variable, my_int_variable, my_bool_variable) # Las variables son los argumentos
print("Este es el valor de my_bool_variable:", my_bool_variable)

# Funciones del sistema (Built-in Functions)
print(len(my_string_variable))                  # Retorna la dimension de la cadena
print(list(my_string_variable))                 # Convierte la cadena a lista
my_int_to_str_variable = str(my_int_variable)   # Convierte el valor a str
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))

# Variables en una sola línea ¡Cuidado con abusar de esta sintaxis!
name, surname, alias, age = "Sara", "Mejia", "sarismejiasanchez", 31
print(f"Me llamo {name} {surname}, tengo {age} años. Mi alias es {alias}.")

# Inputs (su uso no es muy habitual)
name = input("¿Cuál es tu nombre?: ")
age = input("¿Cuántos años tienes?: ")
print(f"{name} tiene {age} años")

# Cambiamos el tipo
name = 31
age = "Sara"
print(name)
print(age)

# ¿Forzamos el tipo?
address: str = "Mi dirección"
address = True
address = 5
address = 1.2
print(type(address))