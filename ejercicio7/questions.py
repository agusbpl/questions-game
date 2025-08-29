import random

# Preguntas para el juego
questions = [
    "¿Qué función se usa para obtener la longitud de una cadena en Python?",
    "¿Cuál de las siguientes opciones es un número entero en Python?",
    "¿Cómo se solicita entrada del usuario en Python?",
    "¿Cuál de las siguientes expresiones es un comentario válido en Python?",
    "¿Cuál es el operador de comparación para verificar si dos valores son iguales?",
]
# Respuestas posibles para cada pregunta, en el mismo orden que las preguntas
answers = [
    ("size()", "len()", "length()", "count()"),
    ("3.14", "'42'", "10", "True"),
    ("input()", "scan()", "read()", "ask()"),
    (
        "// Esto es un comentario",
        "/* Esto es un comentario */",
        "-- Esto es un comentario",
        "# Esto es un comentario",
    ),
    ("=", "==", "!=", "==="),
]
# Índice de la respuesta correcta para cada pregunta, en el mismo orden que las preguntas
correct_answers_index = [1, 2, 0, 3, 1]

questions_to_ask = random.choices(list(zip(questions, answers, correct_answers_index)), k=3)

print("\n")
score = 0
for quest,answ,corr in questions_to_ask:
    print(quest)
    for i,ans in enumerate(answ):
        print(f"{i+1}.{ans}") 
    for intento in range(2):
        print(f"intento numero {intento+1}")
        user_choice = input("su respuesta: ")
        if (user_choice in [str(i) for i in range(1,5)]):
            if int(user_choice) - 1 == corr:
                print("correcto")
                score += 1
                break
            else:
                print("incorrecto")
                score -= 0.5
        else:
            print("respuesta invalida")
            exit(1)  
    else:
        print(f"la respuesta era {answ[corr]}") 
print(f"\nsumaste {score} puntos")
"""
* Comience un repositorio **local** y agregue el archivo recientemente creado.
* Crea tu propio repositorio **remoto** en [Github](https://github.com/) y suba el archivo al repositorio remoto.
* Agrega el `README.md` con tu nombre y número de estudiante.
* Modifique el programa anterior con las siguientes funcionalidades:
    - El juego tiene un bug. Si el usuario ingresa un número de respuesta no válido por ejemplo 42 o 
    "huevos con spam" el programa falla con un error. Modifica el mismo para que si la respuesta no
    es un número o bien no está en el rango de las respuestas posibles muestre un mensaje diciendo: 
    "Respuesta no válida" y termine de inmediato con exit status igual a 1. 
    - Modifique el juego para que al final de la partida se muestre el puntaje del jugador o
    jugadora. El puntaje se calcula de la siguiente forma, cada intento fallido descuenta 0.5 puntos
    y cada acierto suma 1 punto.
    - Modifique el juego para, en lo posible, no acceder a las 3 listas usando índices. Ayuda:
    ```python
    questions_to_ask = random.choices(list(zip(questions, answers, correct_answers_index)), k=3)
    ```
    - Modifique el juego para que no muestre preguntas repetidas (investigue la función
    `random.sample()`)

<div style="page-break-after: always;"></div>

"""