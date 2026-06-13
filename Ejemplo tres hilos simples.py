import threading
import time

def entregar_tarea(estudiante):
    print(f"Estudiante {estudiante} está entregando la tarea")
    time.sleep(2)
    print(f"Estudiante {estudiante} ha entregado la tarea.")

hilos = []

for i in range(1,4):
    hilo = threading.Thread(target=entregar_tarea, args=(i,))
    hilos.append(hilo)
    hilo.start()

for hilo in hilos:
    hilo.join()


print("Todos los hilos terminaron")