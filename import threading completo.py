import threading
import time

def tarea(nombre):
    for i in range(5):
        print(nombre)
        time.sleep(1)

t1 = threading.Thread(target = tarea, args=("Hilo 1",))
t2 = threading.Thread(target = tarea, args=("Hilo 2",))

t1.start()
t2.start()

t1.join()
t2.join()

print("Todos los hilos terminaron")