#Parametro ARGS
import threading
def tarea(nombre):
    print(nombre)

hilo = threading.Thread(target = tarea, args = ("proceso 1 ",))