# Bucles [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 2.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

'''
Enunciado:
Realice una calculadora:
Dentro de un bucle se debe ingresar por línea de comando dos números
Luego se ingresará como tercera entrada al programa el símbolo de la operación
que se desea ejecutar:
- Suma (+)
- Resta (-)
- Multiplicación (*)
- División (/)
- Exponente/Potencia (**)
Se debe efectuar el cálculo correcto según la operación ingresada por consola
Imprimir en pantalla la operación realizada y el resultado

El programa se debe repetir dentro del bucle hasta que como operador
se ingrese la palabra "FIN", en ese momento debe terminar el programa

Se debe debe imprimir un cartel de error si el operador ingresado no es
alguno de lo soportados o no es la palabra "FIN".
'''
print("Mi Calculadora (^_^)")
# Empezar aquí la resolución del ejercicio

while True:
    numero_1 = float(input("Ingrese el primer numero:"))
    numero_2 = float(input("Ingrese el segundo numero:"))
    operacion = str(input("Ingrese operacion:"))
    if operacion == "+" :
        print("El resultado de sumar ", numero_1 ," y ", numero_2, " es ", numero_1 + numero_2)
    elif operacion == "-" :
        print("El resultado de restar ", numero_1 ," y ", numero_2, " es ", numero_1 - numero_2)
    elif operacion == "/" :
        print("El resultado de dividir ", numero_1 ," y ", numero_2, " es ", numero_1 / numero_2 )
    elif operacion == "*" :
        print("El resultado de multiplicar ", numero_1 ," y ", numero_2, " es ", numero_1 * numero_2)
    elif operacion == "**" :    
        print("El resultado de potenciar ", numero_1 ," a la ", numero_2, " es ", numero_1 ** numero_2)
    elif operacion == "FIN" :
        break
    else:
        print("operacion invalida")
        
