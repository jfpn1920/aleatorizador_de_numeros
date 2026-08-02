import random
ids = []
numeros = []
categorias = []
tipos = []
rangos = []
fechas = []
observaciones = []
#---------------------------------------------#
#--|menu_principal_aleatorizador_de_números|--#
#---------------------------------------------#
while True:
    print("menu principal aleatorizador de números")
    print("1) crear número")
    print("2) editar número")
    print("3) eliminar número")
    print("4) buscar número")
    print("5) lista de datos")
    print("6) salir")
    opcion = input("seleccione una opción: ")
    #------------------#
    #--|crear_numero|--#
    #------------------#
    if opcion == "1":
        if len(ids) == 0:
            id_numero = 1
        else:
            id_numero = ids[-1] + 1
        numero = int(input("número: "))
        categoria = input("categoría (positivo, negativo o cero): ")
        tipo = input("tipo (par o impar): ")
        rango = input("rango: ")
        fecha = input("fecha: ")
        observacion = input("observación: ")
        ids.append(id_numero)
        numeros.append(numero)
        categorias.append(categoria)
        tipos.append(tipo)
        rangos.append(rango)
        fechas.append(fecha)
        observaciones.append(observacion)
        print("número registrado correctamente.")
        print("id:", id_numero)
    #-------------------#
    #--|editar_numero|--#
    #-------------------#
    elif opcion == "2":
        if len(ids) == 0:
            print("no existen registros.")
        else:
            print("editar número")
            for i in range(len(ids)):
                print(f"{ids[i]} | {numeros[i]} | {categorias[i]} | {tipos[i]} | {rangos[i]} | {fechas[i]} | {observaciones[i]}")
            id_buscar = int(input("ingrese la id del registro: "))
            if id_buscar in ids:
                posicion = ids.index(id_buscar)
                print("datos actuales")
                print(f"{ids[posicion]} | {numeros[posicion]} | {categorias[posicion]} | {tipos[posicion]} | {rangos[posicion]} | {fechas[posicion]} | {observaciones[posicion]}")
                numeros[posicion] = int(input("nuevo número: "))
                categorias[posicion] = input("nueva categoría: ")
                tipos[posicion] = input("nuevo tipo: ")
                rangos[posicion] = input("nuevo rango: ")
                fechas[posicion] = input("nueva fecha: ")
                observaciones[posicion] = input("nueva observación: ")
                print("registro actualizado correctamente.")
            else:
                print("id no encontrada.")
    #---------------------#
    #--|eliminar_numero|--#
    #---------------------#
    elif opcion == "3":
        if len(ids) == 0:
            print("no existen registros.")
        else:
            print("eliminar número")
            for i in range(len(ids)):
                print(f"{ids[i]} | {numeros[i]} | {categorias[i]} | {tipos[i]} | {rangos[i]} | {fechas[i]} | {observaciones[i]}")
            id_buscar = int(input("ingrese la id del registro: "))
            if id_buscar in ids:
                posicion = ids.index(id_buscar)
                print("datos del registro")
                print(f"{ids[posicion]} | {numeros[posicion]} | {categorias[posicion]} | {tipos[posicion]} | {rangos[posicion]} | {fechas[posicion]} | {observaciones[posicion]}")
                respuesta = input("¿desea eliminar este registro? (s/n): ")
                if respuesta.upper() == "S":
                    ids.pop(posicion)
                    numeros.pop(posicion)
                    categorias.pop(posicion)
                    tipos.pop(posicion)
                    rangos.pop(posicion)
                    fechas.pop(posicion)
                    observaciones.pop(posicion)
                    print("registro eliminado correctamente.")
                else:
                    print("el registro no fue eliminado.")
            else:
                print("id no encontrada.")
    #-------------------#
    #--|buscar_numero|--#
    #-------------------#
    elif opcion == "4":
        if len(ids) == 0:
            print("no existen registros.")
        else:
            print("buscar número")
            id_buscar = int(input("ingrese la id del registro: "))
            if id_buscar in ids:
                posicion = ids.index(id_buscar)
                print("datos del registro")
                print(f"{ids[posicion]} | {numeros[posicion]} | {categorias[posicion]} | {tipos[posicion]} | {rangos[posicion]} | {fechas[posicion]} | {observaciones[posicion]}")
            else:
                print("id no encontrada.")
    #-----------------#
    #--|lista_datos|--#
    #-----------------#
    elif opcion == "5":
        if len(ids) == 0:
            print("no existen registros.")
        else:
            suma = 0
            mayor = numeros[0]
            menor = numeros[0]
            print("lista de datos")
            for i in range(len(ids)):
                print(f"{ids[i]} | {numeros[i]} | {categorias[i]} | {tipos[i]} | {rangos[i]} | {fechas[i]} | {observaciones[i]}")
                suma += numeros[i]
                if numeros[i] > mayor:
                    mayor = numeros[i]
                if numeros[i] < menor:
                    menor = numeros[i]
            promedio = suma / len(ids)
            print("estadísticas aleatorizador de números")
            print("cantidad de números:", len(ids))
            print("suma de números:", suma)
            print("promedio:", round(promedio, 2))
            print("mayor número:", mayor)
            print("menor número:", menor)
            posicion = random.randint(0, len(ids) - 1)
            print("número seleccionado aleatoriamente")
            print(f"{ids[posicion]} | {numeros[posicion]} | {categorias[posicion]} | {tipos[posicion]} | {rangos[posicion]} | {fechas[posicion]} | {observaciones[posicion]}")
    #------------------------------#
    #--|salir_del_menu_principal|--#
    #------------------------------#
    elif opcion == "6":
        print("gracias por utilizar el aleatorizador de números.")
        break
    else:
        print("opción no válida.")