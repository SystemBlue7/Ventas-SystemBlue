clientes = "Cristian,David"
lista_clientes = clientes.split(",")
for n, c in enumerate(lista_clientes, start= 1):
    print(f'Cliente numero {n}: {c}')
    