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

questions_to_ask = random.sample(list(zip(questions, answers, correct_answers_index)), k=3)

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
