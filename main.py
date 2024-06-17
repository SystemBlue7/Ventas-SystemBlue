import csv
import sys
import os 

tabla_clientes = '.clientes.csv'
claves_clientes = ['nombre', 'empresa', 'correo', 'cargo']
clientes = []


def _abrir_archivo():
    with open(tabla_clientes, mode='r') as archivo:
        leer = csv.DictReader(archivo, fieldnames=claves_clientes)

        for i in leer:
            clientes.append(i)


def _guardar_archivo():
    tabla_temp = f'{tabla_clientes}.tmp'
    with open(tabla_temp, mode='w') as archivo:
        escribir = csv.DictWriter(archivo, fieldnames= claves_clientes)
        escribir.writerows(clientes)

        os.remove(tabla_clientes)
        os.rename(tabla_temp, tabla_clientes)


def crear_cliente(cliente):
    global clientes
    
    if cliente not in clientes:
        clientes.append(cliente)
        print(f'El Cliente fue agregado exitosamente!\n')
    else:
        print('=> El Cliente Ya Esta Creado en el Sistema')


def mostrar_clientes():

    print('Este Es El Listado De Clientes En el Sistema')
    print("*" * 45, '\n')
    print('Id   '+ "Nombre   "+ "Empresa   "+ 'Correo   '+ 'Cargo')
    for n, c in enumerate(clientes):
        print('{num} | {nombre} | {empresa} | {correo} | {cargo}'.format(
            num = n,
            nombre = c['nombre'],
            empresa = c['empresa'],
            correo = c['correo'],
            cargo = c['cargo']))
    


def actualizar_cliente(cliente1, cliente2):
    global clientes
    if len(clientes) - 1 >= cliente1:
        clientes[cliente1] = cliente2
        print(f'El Cliente {cliente1} se actualizo por {cliente2} exitosamente!!\n')
    else:
        mensaje()


def eliminar_cliente(id):
    global clientes

    if len(clientes) -1 >= id:
        clientes.pop(id)
        print(f'Cliente {id} eliminado Exitosamente!!!\n')
    else:
        print(f'El cliente {id} no esta en el sistema\n')


def buscar_cliente(id):
    if len(clientes) -1 >= id:
        return True
    else:
        return False


def mensaje():
    print(f"El cliente no esta en el Sistema")


def mensaje_2():
    print('=> Debe ingresar el nombre del Cliente\n=> si no quiere ingresar un nombre digite ¡salir!\n')


def _cliente_avanzado(nombre_cliente, message = 'Cual es el {}?\n=> '):
    datos = None

    while not datos:
        datos = input(message.format(nombre_cliente))
        print(datos)
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
    _abrir_archivo()
    bienvenida()

    dato = int(input())

    if dato == 1:
        cliente = _datos_cliente()

        crear_cliente(cliente)
    elif dato == 2:
        mostrar_clientes()
    elif dato == 3:
        cliente_actualizar = int(_cliente_avanzado("id"))
        nombre_cliente = _datos_cliente()
        actualizar_cliente(cliente_actualizar, nombre_cliente)
    elif dato == 4:
        nombre_cliente = int(input('Cual Id quieres eliminar?\n=>  '))
        print("")
        eliminar_cliente(nombre_cliente)
    elif dato == 5:
        nombre_cliente = int(input('Cual Id quieres eliminar?\n=>  '))
        print("")
        formato = buscar_cliente(nombre_cliente)
        if formato:
            print('¡El nombre del cliente esta en la lista!')
            print(clientes[nombre_cliente])
        else:
            mensaje()
    else:
        print('Opcion Incorrecta')

    _guardar_archivo()
        