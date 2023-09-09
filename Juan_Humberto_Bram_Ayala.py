diccionario_frutas = {
    'manzana': "Roja",
    'banano': "Amarillo",
    'naranja': "Naranja",
    'uva': "Morado",
    'kiwi': "Verde"
}

# Variable para almacenar los cambios
cambios = []

# Función para agregar un elemento
def agregar_elemento(diccionario):
    clave = input("Ingresa la clave del nuevo elemento: ")
    valor = input("Ingresa el valor del nuevo elemento: ")
    diccionario[clave] = valor
    cambios.append(f"Elemento '{clave}' agregado al diccionario con valor '{valor}'.")

# Función para eliminar un elemento
def eliminar_elemento(diccionario):
    clave = input("Ingresa la clave del elemento que deseas eliminar: ")
    if clave in diccionario:
        valor_eliminado = diccionario.pop(clave)
        cambios.append(f"Elemento '{clave}' eliminado del diccionario con valor '{valor_eliminado}'.")
    else:
        print(f"La clave '{clave}' no se encuentra en el diccionario.")

# Función para editar un elemento
def editar_elemento(diccionario):
    clave = input("Ingresa la clave del elemento que deseas editar: ")
    if clave in diccionario:
        nuevo_valor = input(f"Ingresa el nuevo valor para '{clave}': ")
        diccionario[clave] = nuevo_valor
        print(f"Elemento '{clave}' editado. Nuevo valor: '{nuevo_valor}'.")
    else:
        print(f"La clave '{clave}' no se encuentra en el diccionario.")

# Función para mostrar el diccionario actual
def mostrar_diccionario(diccionario):
    print("-------------------------")
    print("CONTENIDO DEL DICCIONARIO")
    print("-------------------------")
    for clave, valor in diccionario.items():
        print(f"{clave}: {valor}")

while True:
    # Solicitar al usuario que elija una acción
    print("-------------------------")
    print("LISTA DE FRUTAS Y COLOR")
    print("-------------------------")
    accion = input("¿Qué deseas hacer? (agregar/editar/eliminar/mostrar/salir): ").lower()

    if accion == 'agregar':
        agregar_elemento(diccionario_frutas)
    elif accion == 'eliminar':
        eliminar_elemento(diccionario_frutas)
    elif accion == 'editar':
        editar_elemento(diccionario_frutas)
    elif accion == 'mostrar':
        mostrar_diccionario(diccionario_frutas)
    elif accion == 'salir':
        break
    else:
        print("Opción no válida. Por favor, elige 'agregar', 'eliminar', 'editar', 'mostrar' o 'salir'.")

# Mostrar los cambios realizados
for cambio in cambios:
    print(cambio)

print("Diccionario final:")
print(diccionario_frutas)
