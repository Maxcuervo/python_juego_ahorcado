
import random
from re import A


def obtener_palabra_secreta() -> str:
    palabras = ["perro", "gato", "elefante", "mono", "gorila", "jirafa"]
    return random.choice(palabras)

def mostrar_progreso(palabra_secreta, letras_adivinadas):
    adivinado = ""
    
    for letra in palabra_secreta:
        if letra in letras_adivinadas:
            adivinado += letra
        else:
            adivinado += "_"
    return adivinado

def juego_ahorcado(): 
    palabra_secreta = obtener_palabra_secreta()
    letras_adivinadas = []
    intentos = 7
    juego_terminado = False
    
    print("¡Bienvenido al juego del ahorcado!")
    print(f"Tienes ``{intentos}´´ intentos para adivinar la palabra")
    print(mostrar_progreso(palabra_secreta, letras_adivinadas), "La palabra tiene:", len(palabra_secreta),"letras")
    
    while not juego_terminado and intentos > 0:
        adivinanza = input("Introduzca una letra: ").lower()
        
        if len(adivinanza) != 1 or not adivinanza.isalpha():
            print("Por favor introduzca una letra válida(solo escribir una letra)")
        elif adivinanza in letras_adivinadas:
            print("Ya utilizastes esa letra, prueba con otra")
        else:
            letras_adivinadas.append(adivinanza)
            
            if adivinanza in palabra_secreta:
                print(f"¡Muy bien acertastes, la letra ``{adivinanza}´´ se encuentra en la palabra")
            else:
                intentos -= 1
                print(f"Lo siento, la letra ``{adivinanza}´´ no se encuentra en la palabra")
                print(f" Te quedan ``{intentos}´´ intentos")
        
        progreso_actual = mostrar_progreso(palabra_secreta, letras_adivinadas)
        print(progreso_actual)
        
        if "_" not in progreso_actual:
            juego_terminado = True
            palabra_secreta = palabra_secreta.capitalize()
            print(f"¡Felicitaciones ganastes! La palabra era``.{palabra_secreta}´´")
            
    if intentos == 0:
        palabra_secreta = palabra_secreta.capitalize()
        print(f" Lo siento mucho, te quedastes sin intentos; la palabra era``{palabra_secreta}´´")
        
        

juego_ahorcado()
                
                