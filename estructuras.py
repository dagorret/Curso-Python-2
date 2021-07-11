import sys #usado para la función sys.exit

target_int = input("¿Cuantos enteros?")

# tratar de convertir el texto de target_int a entero. Y capturar el error con una excepción.

try:
    target_int = int(target_int)
except ValueError:
    sys.exit("Debe ingresar un entero")

ints = list()
count = 1

while count <= target_int:
    new_int = input("Ingrese un entero {0}:".format(count))
    count += 1
    isint = False
    try:
        new_int = int(new_int)
    except:
        print("Debe ingresar un entero")

print(type(new_int))
