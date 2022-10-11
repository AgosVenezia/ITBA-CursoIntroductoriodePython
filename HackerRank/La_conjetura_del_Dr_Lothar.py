""" 
La conjetura del Dr. Lothar

Escriba un programa que reciba un numero del usuario y repita el siguiente proceso usando un while:

Si el numero es par, se debe dividir por 2.
Si el numero es impar, se debe multiplicar por 3 y sumar 1.
Este proceso se repite hasta llegar al numero 1 y luego muestra en pantalla la cantidad de pasos que tardó en llegar.

El input se recibe utilizando el comando input() sin ningún mensaje dentro de los paréntesis. El output se muestra usando print() y mostrándo ÚNICAMENTE el resultado, sin ningún texto adicional.

Input Format
El programa recibe un número natural N.

Output Format
El programa imprime la cantidad de pasos usados para llegar al número 1.

Sample Input 0
6

Sample Output 0
8

Explanation 0
Los pasos a seguir son: 6, 3, 10, 5, 16, 8, 4, 2, 1

Sample Input 1
13

Sample Output 1
9

Explanation 1
Los pasos a seguir son: 13, 40, 20, 10, 5, 16, 8, 4, 2, 1
"""

def lothar(number):
    counter = int(0)
    while number != 1:
        if number % 2 == 0:
            number = number/2
        else:
            number = number*3+1
        counter += 1
    return counter

number = int(input())
print(lothar(number))
