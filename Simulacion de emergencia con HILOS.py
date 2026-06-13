import threading
import time
import random

Tipo_incidente = [
    'Incendio', 
    'Accidente de trancito',
    'Emergencia médica',
    'Seguridad Ciudadana',

]


def atender_llamada(id_llamada, tipo_emergencia):
    print(f"Llamada {id_llamada}: emergencia reportada ({tipo_emergencia}).")
    print(f"Llamada {id_llamada}: operador registrando informacion")
    time.sleep(random.uniform(1, 3))
    print(f"\nLlamada {id_llamada}: asignando recursos de repuesta ({tipo_emergencia}).\n")
    time.sleep(random.uniform(2, 5))
    print(f"\nLlamada {id_llamada}: emergencia atendida ({tipo_emergencia}).\n")


print("============================================================")
print("START SIMULACIÓN DE UN SISTEMA DE ATENCIÓN DE EMERGENCIAS")
print("============================================================")

hilos = []
for i in range(1, 7):
    tipo_emergencia = random.choice(Tipo_incidente)
    hilo = threading.Thread(target=atender_llamada, args=(i, tipo_emergencia))
    hilos.append(hilo)

for hilo in hilos:
    hilo.start()

for hilo in hilos:
    hilo.join()

print("============================================================")
print("Simulación de un sistema de atención de emergencias terminada.")
print("============================================================")

