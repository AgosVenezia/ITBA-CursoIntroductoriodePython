"""
Ahorcado

Les proponemos programar el famoso juego "Ahorcado" donde un jugador ingresa una palabra y otro jugador intenta adivinarla. En cada turno, el segundo jugador indica una letra que cree que se encuentra en la palabra elegida.

Una vez que el segundo jugador adivina todas las letras que se encuentran en la palabra, el juego termina y se muestra la cantidad de intentos que fueron necesarios. En esta versión del juego, si se adivina una letra que aparece varias veces en la palabra, todas las ocurrencias cuentan como adivinadas.

Tip: Pueden eliminar todas las ocurrencias de cierto caracter en un string utilizando el método .replace():

palabra = palabra.replace( "A", "" )

Formato del input:
Primero se recibe la palabra que se debe adivinar (por defecto vendrá en mayúsculas).
Luego se reciben cierta cantidad de letras, una por línea, sin repetir. (por defecto vendrán en mayúsculas)
Una vez que se haya adivinado la palabra del ahorcado, ya no se recibirán más letras. Su tarea es determinar la cantidad de intentos que fueron necesarios para adivinar la palabra completa, e imprimir ese número.

Sample Input 0
PYTHON
A
B
C
P
Y
T
H
O
N

Sample Output 0
9

Explanation 0
El programa imprime la cantidad de turnos que se tardaron en adivinar la palabra, a pesar de que tuvo tres intentos erróneos ('A','B' y 'C').

Sample Input 1
IEEE
X
Y
E
I

Sample Output 1
4

Explanation 1
La palabra original tiene letras repetidas, por lo cual al adivinar las letras 'I' y 'E' alcanza para completar la palabra.
"""

palabra = input("")
i = 0
while len(palabra) != 0:
    letra = input("")
    i+=1
    if letra in palabra:
        palabra = palabra.replace(letra, '')
    elif len(palabra) == 0:
        print(i)
print(i)