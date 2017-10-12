import csv

def leer(archivo1):
        with open(archivo1) as archivo:
            arch_csv = csv.DictReader(archivo)
            listadic=list(arch_csv)
            return(listadic)

def grabar(archivo, dato1, dato2):
    with open(archivo,  "a") as salidacsv:
        campos = ['login', 'usuario']
        salida = csv.DictWriter(salidacsv,lineterminator='\n', fieldnames=campos)
        salida.writerow({'login': dato1, 'usuario': dato2})
