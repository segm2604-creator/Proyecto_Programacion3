import threading

def tarea():
    print("Hola desde el hilo")

hilo = threading.Thread(target=tarea)
hilo.start()
