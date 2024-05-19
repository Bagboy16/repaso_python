'''

Guardar datos de personas con la siguiente estructura:

Cedula ---> Clave
Datos personales: {
    Nombre: 
    Apellido:
}

Cargos ---> Lista

'''

lista_personas = []


while True:
    cedula = input('Ingrese la cedula (vacío para terminar): ')
    if cedula == '':
        break
    nombre = input('Ingrese el nombre: ')
    apellido = input('Ingrese el apellido: ')
    cargos = []
    while True:
        print("Cargos actuales: ")
        for i in cargos:
            print(i)
        cargo = input('Ingrese el cargo (vacío para terminar): ')
        if cargo == '':
            break
        cargos.append(cargo)
    persona = {
        'cedula': cedula,
        'datos_personales': {
            'nombre': nombre,
            'apellido': apellido
        },
        'cargos': cargos
    }
    lista_personas.append(persona)

for persona in lista_personas:
    print(f'{persona["datos_personales"]["nombre"]} {persona["datos_personales"]["apellido"]}')
    print("========")
    print(f'Cedula: V-{persona["cedula"]}')
    print("Cargos:")
    for cargo in persona["cargos"]:
        print(cargo)
    print("")



    