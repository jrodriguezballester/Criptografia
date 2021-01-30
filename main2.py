import argparse
import os

filas=[]

def read_file():
    global filas
    headers = []
    first = True
    linea = 0
    with open('selled_policies.csv', 'r') as f:
        lineas = f.readlines()
        for line in lineas:
            filas.append(line)
            if first:
                headers = line.rstrip('\n').split(',')
                first = False
            else:
                dato = ''
                datos = line.split(',')
                datos[len(datos) - 1] = datos[len(datos) - 1].rstrip('\n')

                for j in range(0, len(headers)):
                    datos[0] = datos[0].strip('"')
                    while len(datos[2]) < 19:
                        datos[2] = datos[2].strip('"') + ' '
                    while len(datos[3]) < 21:
                        datos[3] = datos[3].strip('"') + ' '
                    dato += headers[j].strip('"') + ': ' + datos[j] + '   '
                print(str(linea) + ":  " + dato)
            linea += 1
    return True


def escribir():
    global filas
    f = open('selled_policies.csv', "a")
    print("**** ", filas[len(filas)-1])
    f.write('\n'+filas[len(filas)-1])
    f.close()


if __name__ == '__main__':

    parser = argparse.ArgumentParser()

    parser.add_argument('-l', '--lectura', help=' Modo lectura')
    parser.add_argument('-e', '--lectoEscritura', help='Modo lectura y escritura')
    parser.add_argument('-w', '--escritura', help='Modo lectura y escritura')
# TODO corregir argumentos
    args = parser.parse_args()


    if args.lectura:
        read = read_file()
        print('mi lectura:*****', read)

    if args.lectoEscritura:
        read = read_file()
        print('mi lectura:*****', read)
        #print('mi ultimo dato:*', dato)
        escribir()


    #