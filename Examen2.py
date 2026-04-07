# EXAMEN  - UNIDAD 3 (Basado en 30-Days-Of-Python)

# IMPORTANTE:
# 1. La salida debe ser ÚNICAMENTE el resultado. No agregues texto extra.
# 2. No modifiques las condiciones del menú (if/elif).
# 3. Usa solo una función print() por ejercicio.

problema = int(input("Número del problema (1-4): "))

if problema == 1:
    # Problema 1 (Día 5 - Listas): 
    # Concatena las listas 'front_end' y 'back_end'.
    # Imprime la lista resultante 'full_stack'.
    front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
    back_end = ['Node','Express', 'MongoDB']
    # Tu código aquí

elif problema == 2:
    # Problema 2 (Día 7 - Sets):
    # Del ejercicio de sets: Une los sets A y B (Unión).
    # Imprime el set resultante.
    A = {19, 22, 24, 20, 25, 26}
    B = {19, 22, 20, 25, 26, 24, 28, 27}
    # Tu código aquí

elif problema == 3:
    # Problema 3 (Día 10 - Loops):
    # Del ejercicio de bucles: Usa un ciclo 'for' para iterar de 0 a 100 
    # y suma solo los números impares. Imprime solo el resultado final.
    suma_impares = 0
    # Tu código aquí

elif problema == 4:
    # Problema 4 (Día 11 - Funciones):
    # Del ejercicio de funciones: Crea una función 'convert_celsius_to_fahrenheit'.
    # Debe recibir (celsius). Fórmula: (C * 9/5) + 32.
    # Llama a la función con 25 e imprime el resultado.
    # Tu código aquí

else:
    print("Ingresa un número entre 1 y 4.")