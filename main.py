from datetime import datetime
print("¡Bienvenido a este programa!")
nombre = input("Ingresa tu nombre: ")
curso = input("Ingresa tu curso: ")
prog = input("¿Cuál es tu lenguaje de programación favorito? ")
while not all([nombre, curso, prog]):
    print("No escribiste nada. Por favor, ingresa un valor.")
    nombre = input("Ingresa tu nombre: ").strip()
    curso = input("Ingresa tu curso: ").strip()
    prog = input("¿Cuál es tu lenguaje de programación favorito? ").strip()
    if nombre and curso and prog:
        break
hoy = datetime.now().date()
print(f"{hoy} - Hola, te llamas {nombre}, eres del {curso} y tu lenguaje de programación favorito es {prog}")


