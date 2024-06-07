import sys
clientes = [
    {
        'nombre': 'Cristian',
        'empresa': 'Google',
        'correo': 'cristian@google.com',
        'cargo': 'Gerente',
    },
    {
        'nombre': 'David',
        'empresa': 'Amazon',
        'correo': 'david@Amazon.com',
        'cargo': 'Desarrollador',
    }
]


def crear_cliente(cliente):
    global clientes
    
    if cliente not in clientes:
        clientes.append(cliente)
        print(f'El Cliente fue agregado exitosamente!\n')
    else:
        print('=> El Cliente Ya Esta Creado en el Sistema')


def mostrar_clientes():
    global clientes

    print('Este Es El Listado De Clientes En el Sistema')
    print("*" * 45, '\n')
    print('Id   '+ "Nombre   "+ "Empresa   "+ 'Correo   '+ 'Cargo')
    for n, c in enumerate(clientes, start= 1):
        print('{num} | {nombre} | {empresa} | {correo} | {cargo}'.format(
            num = n,
            nombre = c['nombre'],
            empresa = c['empresa'],
            correo = c['correo'],
            cargo = c['cargo']))
    print("")


def actualizar_cliente(cliente1, cliente2):
    global clientes

    if cliente1 in clientes:
        index = clientes.index(cliente1)
        clientes[index] = cliente2
        print(f'El Cliente {cliente1} se actualizo por {cliente2} exitosamente!!\n')
    else:
        mensaje()


def eliminar_cliente(nombre):
    global clientes

    if nombre in clientes:
        clientes.remove(nombre)
        print(f'Cliente {nombre} eliminado Exitosamente!!!\n')
    else:
        print(f'El cliente {nombre} no esta en el sistema\n')


def buscar_cliente(nombre):
    if nombre in clientes:
        return True
    else:
        return False


def mensaje():
    print(f"El cliente no esta en el Sistema")


def mensaje_2():
    print('=> Debe ingresar el nombre del Cliente\n=> si no quiere ingresar un nombre digite ¡salir!\n')


def _cliente_avanzado(nombre_cliente):
    datos = None

    while not datos:
        datos = input(f'Cual es el {nombre_cliente}\n=>')

        return datos


def _datos_cliente():
    cliente = {
          'nombre':_cliente_avanzado('nombre'),
          'empresa':_cliente_avanzado('empresa'),
          'correo':_cliente_avanzado('correo'),
          'cargo':_cliente_avanzado('cargo'),
    }
    return cliente


def _nuevo_cliente():
    nombre_cliente = None

    while not nombre_cliente:
        mensaje_2()
        nombre_cliente = input("Digite el nombre del nuevo cliente \n=> ").capitalize()
        print("")
        if nombre_cliente == "Salir":
            nombre_cliente = None
            break
    if not nombre_cliente:
        sys.exit()
    
    return nombre_cliente


def bienvenida():
    bienvenida = """
                    Bienvenido A Ventas BlueSystem
                *************************************

        Digite una opcion de la lista:

        1. Crear Cliente
        2. Ver Cliente
        3. Actualizar Cliente
        4. Eliminar Cliente
        5. Buscar Cliente
    """
    print(bienvenida)


if __name__ == "__main__":
    bienvenida()

    dato = int(input())

    if dato == 1:
        cliente = _datos_cliente()

        crear_cliente(cliente)
        mostrar_clientes()
    elif dato == 2:
        mostrar_clientes()
    elif dato == 3:
        cliente_actualizar = input("Digite el cliente que quiere actualizar: \n=> ").capitalize()
        print("")
        nombre_cliente = _nuevo_cliente()
        actualizar_cliente(cliente_actualizar, nombre_cliente)
        mostrar_clientes()
    elif dato == 4:
        nombre_cliente = input('Que cliente desea Eliminar?\n=>  ').capitalize()
        print("")
        eliminar_cliente(nombre_cliente)
        mostrar_clientes()
    elif dato == 5:
        nombre_cliente = input('Digite el nombre del cliente:\n=>').capitalize()
        print("")
        formato = buscar_cliente(nombre_cliente)

        if formato:
            index = clientes.index(nombre_cliente)
            print('¡El nombre del cliente esta en la lista!')
            print(f'Cliente # {index}: {nombre_cliente}')  
        else:
            mensaje()
    else:
        print('Opcion Incorrecta')
        