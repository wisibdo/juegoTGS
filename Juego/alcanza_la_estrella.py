import random
import numpy as np

#Tablero principal

print("Jugador 1 = J1, Jugador 2 = J2, Llegada = F")
print("Tablero:")
tablero = np.matrix(np.zeros((4, 5)),dtype=str)
tablero[0,0] = "J1,J2"
tablero[3,4] = "F"
print(tablero)

#Tablero que se muestra cuando el jugador 1 gana

tablero1 = np.matrix(np.zeros((4,5)),dtype=str)
tablero1[3,4] = "J1"

#Tablero que se muestra cuando el jugador 2 gana

tablero2 = np.matrix(np.zeros((4,5)),dtype=str)
tablero2[3,4] = "J2"

preguntas = [
    {
        'pregunta': '¿Cuál es la capital de España?',
        'respuestas': ['a) Madrid', 'b) Barcelona', 'c) Valencia'],
        'respuesta_correcta': 'a'
    },

    {
        'pregunta': '¿Cuál es el lugar más frío de la Tierra??',
        'respuestas': ['a) Antártida', 'b) Finlandia', 'c) Alaska'],
        'respuesta_correcta': 'a'
    },


    {
        'pregunta': '¿Cuál es el organo que consume más energía en el cuerpo humano??',
        'respuestas': ['a) Corazón', 'b) Cerebro', 'c) Pancreas'],
        'respuesta_correcta': 'b'
    },


    {
        'pregunta': '¿Cuál es el país más pequeño del mundo?',
        'respuestas': ['a) Nauru', 'b) Mónaco', 'c) Vaticano'],
        'respuesta_correcta': 'c'
    },



    {
        'pregunta': '¿Cuál es la formula quimica del hierro??',
        'respuestas': ['a) Fe', 'b) CO2.', 'c) H2O'],
        'respuesta_correcta': 'a'
    },



    {
        'pregunta': '¿Quien pinto la Monna Lisa??',
        'respuestas': ['a) Pablo picasso', 'b) Van Gogh.', 'c) Leonardo Da Vinci'],
        'respuesta_correcta': 'c'
    },



    {
        'pregunta': '¿Qué planeta del sistema solar tiene mas lunas?',
        'respuestas': ['a) Jupiter', 'b) Marte.', 'c) Saturno'],
        'respuesta_correcta': 'a'
    },


    {
        'pregunta': '¿Quien fue el auténtico padre de la electricidad?',
        'respuestas': ['a) Thomas Edison', 'b) Nikola Tesla', 'c) Albert Einstein'],
        'respuesta_correcta': 'b'
    },

    {
        'pregunta': '¿Qué colores tiene la bandera de Paraguay, en orden de arriba hacia abajo?',
        'respuestas': ['a)Rojo, azul y blanco ', 'b) blanco, rojo y azul.', 'c)Rojo, blanco y azul'],
        'respuesta_correcta': 'c'
    },


    {
        'pregunta': '¿En qué año fue la revolucion francesa?',
        'respuestas': ['a) 1789', 'b) 1815', 'c) 1848'],
        'respuesta_correcta': 'a'
    },
    {
        'pregunta': '¿Cual es el metal más pesado?',
        'respuestas': ['a) Hierro', 'b) Plomo', 'c) Oro'],
        'respuesta_correcta': 'b'
    },
    {
        'pregunta': '¿En que año se fundo la ciudad de Medellin?',
        'respuestas': ['a) 7809 a.c', 'b) 2023', 'c) 1650'],
        'respuesta_correcta': 'c'
    },
    {
        'pregunta': '¿Cuál es el continente más poblado?',
        'respuestas': ['a) asia', 'b) europa', 'c) america'],
        'respuesta_correcta': 'a'
    },
    {
        'pregunta': '¿En que año finalizó la segunda guerra mundial?',
        'respuestas': ['a) depende', 'b) 236 a.c', 'c) 1945'],
        'respuesta_correcta': 'c'
    },
    {
        'pregunta': '¿Cual es el color que representa la esperanza?',
        'respuestas': ['a) si', 'b) negro', 'c) verde'],
        'respuesta_correcta': 'c'
    },
    {
        'pregunta': '¿Cuantas patas tiene una araña?',
        'respuestas': ['a) 2', 'b) muchas', 'c) 8'],
        'respuesta_correcta': 'c'
    },
    {
        'pregunta': '¿Cuál es el animal terrestre mas rapido del mundo?',
        'respuestas': ['a) Humano', 'b) guepardo', 'c) oso perezoso'],
        'respuesta_correcta': 'b'
    }
]

def lanzar_dado():
    return random.randint(1, 6)

def hacer_pregunta():
    pregunta = random.choice(preguntas)
    preguntas.remove(pregunta)  # Eliminar la pregunta elegida de la lista de preguntas para que no se repita
    print(pregunta['pregunta'])
    for respuesta in pregunta['respuestas']:
        print(respuesta)
    respuesta_jugador = ''

    # Verificar que la respesta del jugador es a, b o c

    while respuesta_jugador not in ['a', 'b', 'c']:
        respuesta_jugador = input('Elige una respuesta (a, b o c): ')
        if respuesta_jugador not in ['a', 'b', 'c']:
            print('Respuesta inválida. Por favor, elige "a", "b" o "c".')
    if respuesta_jugador == pregunta['respuesta_correcta']:
        print('¡Correcto!')
        return True
    else:
        print('¡Incorrecto!')
        return False


def aplicar_castigo(posicion_jugador, tipo_castigo):

    castigos = ['puente', 'resbalon', 'calavera']
    tipo_castigo = random.choice(castigos)

    if tipo_castigo == 'puente':
        nueva_posicion = posicion_jugador - 3
    elif tipo_castigo == 'resbalon':
        nueva_posicion = posicion_jugador - 2
    elif tipo_castigo == 'calavera':
        nueva_posicion = 1

    # Si la nueva posición es menor que 1, el jugador se devuelve a la casilla 1
    if nueva_posicion < 1:
        nueva_posicion = 1

    print(f'{tipo_castigo}! pasas de la posicion {posicion_jugador} a la posicion {nueva_posicion}')
    return nueva_posicion

jugador1 = {'nombre': 'Jugador 1', 'posicion': 0, 'aciertos': 0}
jugador2 = {'nombre': 'Jugador 2', 'posicion': 0, 'aciertos': 0}

while True:
    # Turno del jugador 1
    print(f'Turno de {jugador1["nombre"]}')
    lanzamiento = lanzar_dado()
    print(f'Lanzamiento: {lanzamiento}')
    if hacer_pregunta():
        jugador1['aciertos'] += 1
        jugador1['posicion'] += lanzamiento
        if jugador1['posicion'] > 20:
            jugador1['posicion'] = 20
    else:
        jugador1['posicion'] = aplicar_castigo(jugador1['posicion'], 2)
    print(f'Posición actual: {jugador1["posicion"]}, Aciertos: {jugador1["aciertos"]}')
    if jugador1['posicion'] >= 20:
        jugador1['posicion'] = 20
        print(f'{jugador1["nombre"]} ha ganado!')
        print(tablero1)
        break

    # Turno del jugador 2
    print(f'Turno de {jugador2["nombre"]}')
    lanzamiento = lanzar_dado()
    print(f'Lanzamiento: {lanzamiento}')
    if hacer_pregunta():
        jugador2['aciertos'] += 1
        jugador2['posicion'] += lanzamiento
        if jugador2['posicion'] > 20:
            jugador2['posicion'] = 20
    else:
        jugador2['posicion'] = aplicar_castigo(jugador2['posicion'], 2)
    print(f'Posición actual: {jugador2["posicion"]}, Aciertos: {jugador2["aciertos"]}')
    if jugador2['posicion'] >= 20:
        jugador2['posicion'] = 20
        print(f'{jugador2["nombre"]} ha ganado!')
        print(tablero2)
        break
