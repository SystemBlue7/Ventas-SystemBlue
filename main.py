clientes = "Cristian,David,Marcela,"

def crear_cliente(nombre):
    global clientes
    
    if nombre not in clientes:
        clientes += nombre
        _coma_espacio()
        print(f'El Cliente {nombre} fue agregado exitosamente! ')
    else:
        print('El Cliente Ya Esta Creado en la lista')


def mostrar_clientes():
    global clientes

    clientes = clientes.split(',')
    clientes.pop()
    print('Este Es El Listado De Clientes Registrados\n')
    for n, c in enumerate(clientes, start= 1):
        print(f'Cliente numero {n}: {c}')


def actualizar_cliente(cliente1, cliente2):
    global clientes

    if cliente1 in clientes:
        clientes = clientes.replace(cliente1, cliente2)
    else:
        mensaje()


def eliminar_cliente(nombre):
    global clientes

    if nombre in clientes:
        clientes = clientes.replace(nombre + ",", '')
        

def _coma_espacio():
    global clientes

    clientes += ","


def mensaje():
    print(f"El cliente no esta en la lista")


def _nuevo_cliente():
    return input("Digite el nombre del nuevo cliente: ").capitalize()


def bienvenida():
    bienvenida = """
                    Bienvenido A Ventas BlueSystem
                *************************************

        Digite una opcion de la lista:

        1. Crear Cliente
        2. Ver Cliente
        3. Actualizar Cliente
        4. Eliminar Cliente
    """
    print(bienvenida)


def _listado_clientes():
    global clientes
    print(clientes)


if __name__ == "__main__":
    bienvenida()

    dato = int(input())

    if dato == 1:
        nombre_cliente = _nuevo_cliente()
        crear_cliente(nombre_cliente)
        _listado_clientes()
    elif dato == 2:
        mostrar_clientes()
    elif dato == 3:
        cliente_actualizar = input("Digite el cliente que quiere actualizar: ").capitalize()
        nombre_cliente = _nuevo_cliente()
        actualizar_cliente(cliente_actualizar, nombre_cliente)
        _listado_clientes()
    elif dato == 4:
        nombre_cliente = input('Que cliente desea Eliminar?: ').capitalize()
        eliminar_cliente(nombre_cliente)
        _listado_clientes()
        