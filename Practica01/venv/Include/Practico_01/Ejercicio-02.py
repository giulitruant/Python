x = int(input('Ingrese primer numero'))
y = int(input('Ingrese segundo numero'))
z = int(input('Ingrese tercer numero'))
numeroMaximo = max(x,y,z)

assert (max(x,y,z) == x)

assert (max(x,y,z) == y)

assert (max(x,y,z) == z)

print('El numero maximo es : {}' .format(numeroMaximo))
