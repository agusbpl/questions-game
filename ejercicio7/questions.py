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

# El usuario deberá contestar 3 preguntas
puntaje = 0
for _ in range(3):
    # Se selecciona una pregunta aleatoria
    question_index = random.randint(0, len(questions) - 1)

    # Se muestra la pregunta y las respuestas posibles
    print(questions[question_index])
    for i, answer in enumerate(answers[question_index]):
        print(f"{i + 1}. {answer}")

    # El usuario tiene 2 intentos para responder correctamente
    for intento in range(2):
        user_answer = input("Respuesta: ")
        if user_answer.isdigit() and (int(user_answer)) in [1, 2, 3, 4]:
            if int(user_answer) - 1 == correct_answers_index[question_index]:
                print("¡Correcto!")
                puntaje += 1
                break
            else:
                print("¡Incorrecto!")
                puntaje -= 0.5
        else:
            print("Respuesta inválida")
            exit(1)
    else:
        # Si el usuario no responde correctamente después de 2 intentos,
        # se muestra la respuesta correcta
        print("La respuesta correcta es:")
        print(answers[question_index][correct_answers_index[question_index]])

    # Se imprime un blanco al final de la pregunta
    
print(f"\n puntaje final: {puntaje}")


questions_to_ask = random.choices(list(zip(questions, answers, correct_answers_index)), k=3)


print()
print()
for quest,answ,corr in questions_to_ask:
    print(quest)
    for i,ans in enumerate(answ):
        print(f"{i+1}.{ans}") 
    user_choice = input("su respuesta: ")
    if int(user_choice) - 1 == corr:
        print("correcto")
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