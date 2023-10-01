import threading

# Define a function that takes an integer parameter
def mi_funcion(valor):
    for i in range(valor):
        print(f'Hilo 1: Iteración {i}')

# Create a thread and pass the parameter as a tuple
parametro = 3  # Replace this with the integer value you want to pass
hilo = threading.Thread(target=mi_funcion, args=(parametro,))

# Start the thread
hilo.start()

# The main thread continues running its code in parallel
for i in range(5):
    print(f'Hilo principal: Iteración {i}')

# Wait for the thread to finish before the main program exits
hilo.join()

print("Programa principal terminado")
