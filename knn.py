import math
import random

# import scanf
archivo = open("GOLF.dat")
a, n1, saver, var, r, conjunto, z, ord, arr, vp, p = [
], [], [], [], [], [], [], [], [], [], []
cont = 0
k = 5
while True:
    # leemos el archivo linea por linea
    documento = archivo.readline()
    # elimina los saltos de linea
    documento = documento.replace("\n", "")

    if not documento:
        break
    else:
        # separamos los a limitados por una coma
        b = documento.split(",")
        documento = documento.split(",")
        if b[4] == 'FALSE':
            b[4] = 1
        else:
            b[4] = 0
        if b[1] == 'sunny':
            s, s1 = b[2], b[3]
            b[2], b[3] = int(float(s)), int(float(s1))

            # asignamos los valores a n y x, en x damos solo los enteros
            n, x = [b[0], 1, 0, 0, b[2], b[3], b[4], b[5]], [
                1, 0, 0, b[2], b[3], b[4]]
        if b[1] == 'overcast':
            s, s1 = b[2], b[3]
            b[2], b[3] = int(float(s)), int(float(s1))

            n, x = [b[0], 0, 1, 0, b[2], b[3], b[4], b[5]], [
                0, 1, 0, b[2], b[3], b[4]]
        if b[1] == 'rainy':
            s, s1 = b[2], b[3]
            b[2], b[3] = int(float(s)), int(float(s1))

            n, x = [b[0], 0, 0, 1, b[2], b[3], b[4], b[5]], [
                0, 0, 1, b[2], b[3], b[4]]
        # agregamos los a a una lista
        conjunto.append(documento)
        n1.append(n)
        a.append(x)

L = list(range(0, 14))
random.shuffle(L)
print('\n')
print('Conjunto de Datos Forma Nominal\n')
f = ['No.', 'outlook', 'temperature', 'humidity', 'windy', 'play']
print(f)

for i in range(len(conjunto)):
    print(conjunto[i])
print('\n')
print('Conjunto de Datos en Forma Numerica\n')
for i in range(len(n1)):
    print(n1[i])
print('\n')

entrenamiento = []
for i in range(0, 10):
    posicion = L[i]
    dato = a[int(posicion)]
    entrenamiento.append(dato)
print('entrenamiento')
for i in range(10):
    print(entrenamiento[i])
print('\n')

# generamos la lista de prueba
prueba = []
for i in range(10, 14):
    posicion = L[i]
    dato = a[int(posicion)]
    prueba.append(dato)
print('prueba')
for i in range(4):
    print(prueba[i])
print('\n')


def distancia(vp, p):

    m = []
    suma = 0
    for j in range(4):
        for i1 in range(10):
            for i in range(6):
                # restamos los valores P-Q en su respectiva posicion y lo elvamos al cuadrado
                cuadrado = ((vp[i1][i]-p[j][i])**2)
                suma = suma+cuadrado
            if i == 5:
                cuadrado = ((vp[i1][i]-p[j][i])**2)
                suma = suma+cuadrado
                m = (math.sqrt(suma))
                r.append(round(m, 2))
                suma = 0


def orden(z):
    copy = []
    for i in z:
        copy.append(i)
    for i in range(4-1):
        for j in range(10-i-1):
            if copy[j] > copy[j+1]:
                copy[j],copy[j+1] = copy[j+1],copy[j]
    return copy


def position(u, o):
    for i1 in range(k):
        ord.extend([None]*1)
        ord[i1] = o[i1]
    print(ord, '\n')
    for j1 in range(k):
        arr.extend([None]*1)
        for i2 in range(10):
            if ord[j1] == u[i2]:
                arr[j1] = i2+1
    # print(arr,'\n')
    return arr


distancia(entrenamiento, prueba)

print('distancias')
print(r)
print('\n')
c = orden(r)
print('distacia ordenada')
print(c, '\n')
print("position")
p = position(r, c)
print(p)


def kmenor(u):
    print('posicion ordenada')
    
    for i in range(u-1):
        for j in range(u-i-1):
            if p[j] > p[j+1]:
                p[j], p[j+1] = p[j+1], p[j]
    print(p)
    for i in range(u):
        print(n1[p[i]-1])


kmenor(k)
print('\n')
