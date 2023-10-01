import threading

# Define una función que se ejecutará en el hilo


def mi_funcion():
    for i in range(5):
        print(f'Hilo 1: Iteración {i}')


def main():
    # Crea un objeto Thread y proporciona la función que se ejecutará en ese
    # hilo
    hilo = threading.Thread(target=mi_funcion)

    # Inicia la ejecución del hilo
    hilo.start()

    # El hilo principal sigue ejecutando su código mientras que el hilo
    # secundario se ejecuta en paralelo
    for i in range(5):
        print(f'Hilo principal: Iteración {i}')

    # Espera a que el hilo secundario termine antes de que el programa principal termine
    # hilo.join()

    print("Programa principal terminado")


if __name__ == "__main__":
    main()
