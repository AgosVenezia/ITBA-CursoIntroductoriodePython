"""
Las Elecciones

El programa debe calcular el ganador de unas elecciones e imprimir su nombre, para este ejemplo se asume que no hay empates.

Los nombres y la cantidad de candidatos es desconocida.

Input Format
El programa primero recibe un número N, la cantidad de votos totales que se realizaron. Luego recibe N votos en formato string, cada uno consiste en el nombre del candidato seleccionado.

Constraints
1 ≤ N ≤ 100

Output Format
El programa debe calcular el ganador de las elecciones e imprimir su nombre.

Sample Input 0
12
Mickey
Donald
Mickey
Minnie
Mickey
Goofy
Daisy
Goofy
Goofy
Minnie
Goofy
Donald

Sample Output 0
Goofy

Explanation 0
El resultado es Goofy ya que este recibe 4 votos, la cual es la mayor cantidad de votos.
"""

def CalcularGanador(total_votos):
    candidatos = {}
    for i in range(total_votos):
        new_voto = input()

        if new_voto not in candidatos:
            candidatos[new_voto] = 1
        else:
            candidatos[new_voto] += 1

    return max(candidatos, key = candidatos.get)

total_votos = int(input())
print(CalcularGanador(total_votos))