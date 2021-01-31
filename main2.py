import argparse
import os

lineas=[]

def read_file(modOpen):
    global lineas
    headers = []
    first = True
    linea = 0
    with open('selled_policies.csv', modOpen) as f:
        try:
            lineas = f.readlines()
        except IOError:
            print("Error de lectura del archivo")
            exit()
        for line in lineas:
         #   filas.append(line.rstrip(('\n')))   # guarda cada fila en filas sin salto de linea
                                                # registro lineas ---> "2020-12-31", 2, "quecoches", "AMV", 2\n
                                                # registro filas  ---> "2020-12-31", 2, "quecoches", "AMV", 2

            if first:
                headers = line.rstrip('\n').split(',')
                first = False
            else:
                dato = ''
                datos = line.split(',')

                for j in range(0, len(headers)):
                    try:
                        # presentacion (quitar comillas, dejar mismo hueco columnas,salto de linea)
                        datos[0] = datos[0].strip('"')
                        while len(datos[2]) < 19:
                            datos[2] = datos[2].strip('"') + ' '
                        while len(datos[3]) < 21:
                            datos[3] = datos[3].strip('"') + ' '
                        # quitar salto de linea al final
                        datos[-1] = datos[-1].rstrip('\n')

                        dato += headers[j].strip('"') + ': ' + datos[j] + '   '
                    except:
                        print("error en formato en la linea ", linea, " del archivo" )
                print(str(linea) + ":  " + dato)
            linea += 1
    return linea - 1


def escribir(modOpen):
    global lineas
    # Posicionar al final con modOpen='a' o con seek()
    f = open('selled_policies.csv', modOpen)

    f.seek(0, 2)

    print("registro a guardar: ", lineas[-1])
    f.write(lineas[-1])

    f.close()


if __name__ == '__main__':
    # global lineas
    parser = argparse.ArgumentParser()
    my_group = parser.add_mutually_exclusive_group(required=True)

    my_group.add_argument('-l', '--lectura', action='store_true', help=' Modo lectura')
    my_group.add_argument('-e', '--lectoEscritura', action='store_true', help='Modo lectura y escritura')
    my_group.add_argument('-w', '--escritura', action='store_true', help='Modo lectura y escritura')

    args = parser.parse_args()


    if args.lectura:

        modOpen = 'r'   # modo apertura fichero segun enunciado

        registros = read_file(modOpen)
        print('Numero de registros: ', registros)


    if args.lectoEscritura:

        modOpen = 'r+'  # modo apertura fichero segun enunciado

        registros = read_file(modOpen)
        print('Numero de registros: ', registros)

        escribir(modOpen)


    if args.escritura:

        modOpen = 'w'  # modo apertura fichero segun enunciado

        registros = read_file(modOpen) # Dará error por el tipo de apertura
        print('Numero de registros: ', registros)

        escribir(modOpen)
