# lap_timer_client.py
# Programa cliente que lee tiempos de vuelta de un archivo
# e imprime la racha decreciente mas larga.

import lap_timer


def main():
    # TODO: Pedir el nombre del archivo al usuario usando input()
    filename = input("Ingrese el nombre del archivo: ")
    
    # TODO: Abrir el archivo y leer el numero de vueltas n
    with open(filename, "r") as file:
        n = int(file.readline().strip())
    
    # TODO: Crear el cronometro usando lap_timer.init(n)
    timer = lap_timer.init(n)
    
    # TODO: Leer los n tiempos de vuelta y agregarlos con lap_timer.add_lap()
    with open(filename, "r") as file:
        file.readline()  
        for i in range(n):
            time = float(file.readline().strip())
            timer = lap_timer.add_lap(timer, time)
    
    # TODO: Imprimir la racha decreciente mas larga
    #       usando lap_timer.longest_decreasing_streak()
    print("Racha decreciente más larga =", lap_timer.longest_decreasing_streak(timer))


if __name__ == "__main__":
    main()
