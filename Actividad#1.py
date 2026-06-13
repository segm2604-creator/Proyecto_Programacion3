#una tienda vende cuadernos a 3$ y lapices  1$
#un estudiante tiene 20$, si compra 4 cuadernos 
#Cuanto dinero le queda?
#cuantos lapices puede comprar?

cuadernos = 3
lapices = 1
dinero = 20
cuadernos_comprados = 4

gasto_cuadernos = cuadernos * cuadernos_comprados
dinero_restante = dinero - gasto_cuadernos
lapices_comprables = dinero_restante

print(f"Dinero restante despues de la compra de cuaderno es: {dinero_restante}$")
print(f"El estudiante puede comprar {lapices_comprables} lapices con el dinero restante.")
