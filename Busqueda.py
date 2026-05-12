import time

def leer(nombre):
    try:
        with open(nombre, "r") as f:
            return [int(x.strip()) for x in f]
    except:
        return []

def secuencial(lista, x):
    for i in range(len(lista)):
        if lista[i] == x:
            return i
    return -1

datos = leer("datos.txt")

print("=" * 40)
print("   BUSQUEDA SECUENCIAL")
print("=" * 40)
print("Datos cargados:", len(datos))
print()

while True:
    entrada = input("Numero a buscar: ")
    try:
        num = int(entrada)
        break
    except:
        print("Entrada invalida, intenta de nuevo\n")

t1 = time.time()
resultado = secuencial(datos, num)
t2 = time.time()

print("\n" + "-" * 40)

if resultado != -1:
    print("Resultado: Encontrado en la posicion", resultado)
else:
    print("Resultado: No se encontro el numero")

print("Tiempo de busqueda: {:.6f} segundos".format(t2 - t1))
print("-" * 40)