
table = [1, -4, -4, 23, 62, 1001, int(1e6), int(6.5e8)]

try:
    input = input("Introduzca un valor para buscar en la lista: ")

    if '.' in input or 'e' in input.lower():
        value = float(input)
    else:
        value = int(input)

    output = False
    for index in range(len(table)):
        if table[index] == value:
            print(f"({value}, {index})")
            output = True
            break

    if not output:
        print("El valor no está en la lista.")

except ValueError:
    print("Entrada no válida, introduzca un valor válido.")
