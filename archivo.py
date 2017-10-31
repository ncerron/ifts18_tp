import csv

class MiError (Exception) :
    """Se crea la excepcion MiError"""
    pass

def lista_clientes(archivo1) :
    """funcion que lee  un archivo y retorna una lista de Clientes sin duplicados"""
    with open(archivo1) as archivo :
        arch_csv = csv.DictReader(archivo)
        listadic = list(arch_csv)
        lista_consulta = []
        for l in listadic :
            if l['CLIENTE'] not in lista_consulta :
               lista_consulta.append(l['CLIENTE'])
        return lista_consulta

def lista_producto(archivo1):
    """funcion que lee  un archivo y retorna una lista de Productos sin duplicados"""
    with open(archivo1) as archivo:
        arch_csv = csv.DictReader(archivo)
        listadic = list(arch_csv)
        lista_consulta = []
        for l in listadic :
            if l['PRODUCTO'] not in lista_consulta:
                lista_consulta.append(l['PRODUCTO'])
        return lista_consulta

def leer(archivo1) :
    """lee arhivo y lo guarda como un diccionario el cual es asignado a la variable listadic, se retorna la misma"""
    with open(archivo1) as archivo :
         arch_csv = csv.DictReader(archivo)
         listadic = list(arch_csv)
         return listadic

def grabar(archivo, dato1, dato2) :
    """"se guarda los dato1 y dato2 al archivo en formato de diccionario"""
    with open(archivo,  "a") as salidacsv:
        campos = ['login', 'usuario']
        salida = csv.DictWriter(salidacsv,lineterminator='\n', fieldnames = campos)
        salida.writerow({'login': dato1, 'usuario': dato2})

def validar(archivo) :
    """lee el archivo asignando en la variable listadic la informacion del archivo, para poder ser validados
    los campos del mismo. En caso de no ser exitosa la validacion se enviara el mensaje por el motivo, y el
    menaje 'No se puede procesar el archivo' """
    try:
        with open(archivo) as archivo:
            arch_csv = csv.DictReader(archivo)
            listadic = list(arch_csv)
            msj = False

            ##valida la cantidad de columnas
            for item in listadic :
                if len(item) != 5 :
                    raise MiError("verifique el nro de columnas del archivo")

                #verifica que el codigo sea un numero entero y que no sea nulo
                if type(int(item['CODIGO'])) != int and item['CODIGO'] is not None :
                   pass
                else :
                    msj = True

                #verifica que el campo no debe contener numeros en la mayoria de los caracteres
                if str(item['PRODUCTO']).isnumeric():
                    raise MiError("el campo no debe contener numeros")
                else :
                    msj = True

                #verifica que el campo no debe contener numeros en la mayoria de los caracteres
                if str(item['CLIENTE']).isnumeric():
                    raise MiError("el campo no debe contener numeros")
                else :
                    msj = True

                #verifica que el campo contenga numeros enteros
                if float(item['CANTIDAD']) % 1 == 0 :
                    msj = True
                else :
                    raise MiError("La cantidad debe ser un numero entero")

                #verifica que el campo contenga numeros reales
                if float(item['PRECIO']) % 1 == 0 or float(item['PRECIO']) % 1 != 0 :
                     msj = True
                else:
                    raise MiError("El precio debe ser un numero")
        if msj:
             return True

    except MiError as error :
        print(error)
        print("")
        print("-No se puede procesar el archivo-")
    except ValueError:
        print("error en el tipo de valor del campo")
        print("")
        print("-No se puede procesar el archivo-")
    except FileNotFoundError:
        print("No se puede leer el archivo")
        print("")
        print("-No se puede procesar el archivo-")





