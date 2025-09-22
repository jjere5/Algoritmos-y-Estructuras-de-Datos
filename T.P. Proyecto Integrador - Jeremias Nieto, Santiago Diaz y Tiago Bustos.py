import random
import time
import sys

def slow_print(text, delay=0.06):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(delay)
def show_credits():
    """Muestra los créditos del juego, con un formato mucho más largo y detallado."""
    print("===========================================")
    print("              ✨ CRÉDITOS ✨")
    print("===========================================")
    time.sleep(2)
    
    print("\n--- Dirección y Liderazgo de Proyecto ---")
    print("🎮  Director Creativo y de Producto: Santiago Diaz")
    print("    Visionario principal y encargado de la conceptualización general del proyecto,")
    print("    supervisando la experiencia de usuario y la dirección artística del juego.")
    print("    Lideró las reuniones de estrategia y definió los objetivos a largo plazo.")
    time.sleep(3)

    print("\n--- Departamento de Ingeniería de Software ---")
    print("💻  Arquitecto de Software Principal: Jeremias Nieto")
    print("    Responsable del diseño y la implementación de la estructura central del código.")
    print("    Creó las funciones del juego, optimizó el rendimiento y gestionó la integración de los módulos.")
    print("    Su enfoque en la eficiencia y la limpieza del código fue fundamental para el éxito del proyecto.")
    time.sleep(3)
    
    print("\n--- Producción y Aseguramiento de Calidad ---")
    print("✅  Productor Ejecutivo y QA Lead: Tiago Bustos")
    print("    Coordinó los recursos y los plazos, asegurando que el proyecto se mantuviera en el camino correcto.")
    print("    Dirigió el equipo de pruebas (QA), identificando y resolviendo bugs y errores lógicos.")
    print("    Su atención al detalle garantizó una experiencia de juego fluida y sin fallos para el usuario final.")
    time.sleep(3)

    print("\n--- Agradecimientos Especiales ---")
    print("A la comunidad de programación por sus recursos y apoyo constante.")
    print("A los tutores y mentores que nos guiaron en cada paso del camino.")
    print("Y a todos los jugadores por su entusiasmo y dedicación.")
    time.sleep(2)
    
    print("\n--- Información del Proyecto ---")
    print("🕹️  Título del Proyecto: Colección de Juegos de Terminal")
    print("    Versión: 2.0 (La versión 'Créditos Extendidos')")
    print("    Fecha de Lanzamiento: 2025")
    print("    Desarrollado en Python 3")
    time.sleep(2)
    
    print("\n--- Fin de los Créditos ---")
    print("Gracias por jugar y por ser parte de este viaje.")
    print("===========================================")
    time.sleep(2)

def run_game(palabras):
    """Función unificada para ejecutar una partida de Ahorcado."""
    palabra = random.choice(palabras)
    progreso = ["_"] * len(palabra)
    intentos = 6
    letras_adivinadas = []

    while intentos > 0 and "_" in progreso:
        print("\nPalabra:", " ".join(progreso))
        print("Intentos restantes:", intentos)
        print("Letras adivinadas:", " ".join(letras_adivinadas))

        letra = str(input("Ingresa una letra: ")).lower()

        if len(letra) != 1 or not letra.isalpha():
            print("Por favor, ingresa una sola letra válida.")
            continue

        if letra in letras_adivinadas:
            print("Ya adivinaste esa letra. Intenta con otra.")
            continue

        letras_adivinadas.append(letra)

        if letra in palabra:
            for i, l in enumerate(palabra):
                if l == letra:
                    progreso[i] = letra
        else:
            intentos -= 1
            print("¡Letra incorrecta!")

    if "_" not in progreso:
        print(f"\n¡Ganaste! La palabra era: {palabra}")
    else:
        print(f"\nPerdiste... La palabra era: {palabra}")
    
    input("\nPresiona ENTER para continuar...")

def piedra_papel_tijera():
    """Juego de Piedra, Papel o Tijera."""
    print("--BIENVENIDO a PIEDRA, PAPEL O TIJERA--")
    print("ELIJA:")
    print("1 -- PIEDRA")
    print("2 -- PAPEL")
    print("3 -- TIJERA")
    print("4 -- Créditos")
    print("5 -- Salir")
    print("-----------")
    
    opcionia = random.randint(1, 3)

    while True:
        try:
            opcionusu = int(input("ELIJA UNA OPCION: "))
            if 1 <= opcionusu <= 5:
                break
            else:
                print("Opción inválida. Por favor, elige un número del 1 al 5.")
        except ValueError:
            print("Por favor, ingresa un número válido.")
    
    if opcionusu == 4:
        show_credits()
        input("\nPresiona ENTER para volver al menú principal...")
        return
    elif opcionusu == 5:
        print("Saliendo del juego de Piedra, Papel o Tijera...")
        time.sleep(1)
        return

    if opcionusu == 1 and opcionia == 1:
        print("EMPATE, la IA eligió PIEDRA")
    elif opcionusu == 1 and opcionia == 2:
        print("PERDISTE, la IA eligió PAPEL")
    elif opcionusu == 1 and opcionia == 3:
        print("GANASTE, la IA eligió TIJERA")
    elif opcionusu == 2 and opcionia == 2:
        print("EMPATE, la IA eligió PAPEL")
    elif opcionusu == 2 and opcionia == 1:
        print("GANASTE, la IA eligió PIEDRA")
    elif opcionusu == 2 and opcionia == 3:
        print("PERDISTE, la IA eligió TIJERA")
    elif opcionusu == 3 and opcionia == 1:
        print("PERDISTE, la IA eligió PIEDRA")
    elif opcionusu == 3 and opcionia == 2:
        print("GANASTE, la IA eligió PAPEL")
    elif opcionusu == 3 and opcionia == 3:
        print("EMPATE, la IA eligió TIJERA")

    input("\nPresiona ENTER para volver al menú principal...")

def ahorcado():
    """Juego del Ahorcado."""
    while True:
        print("=====================================")
        print("      🎮  JUEGO DEL AHORCADO 🎮")
        print("=====================================")
        print("1. Jugar")
        print("2. Créditos")
        print("3. Salir")
        print("=====================================")

        try:
            opcion = int(input("> "))
        except ValueError:
            print("Por favor, ingresa un número válido.")
            continue

        if opcion == 1:
            while True:
                print("=====================================")
                print("      🎮  JUEGO DEL AHORCADO 🎮")
                print("=====================================")
                print("ELIJA UNA CATEGORIA: ")
                print("=====================================")
                print("1. CATEGORIA RANDOM ")
                print("2. FRUTAS ")
                print("3. VERDURAS ")
                print("4. ANIMALES ")
                print("5. PALABRAS EN INGLES ")
                print("6. Salir")
                print("=====================================")

                try:
                    opcion1 = int(input("> "))
                except ValueError:
                    print("Por favor, ingresa un número válido.")
                    continue
                
                palabras = []

                if opcion1 == 1:
                    palabras = [
                        "abecedario", "abeja", "abismo", "abrigo", "abril", "abuelo", "acantilado", "aceituna",
                        "acero", "actor", "actriz", "agua", "aguila", "ahorcado", "aire", "ajedrez", "albahaca",
                        "alcachofa", "aldea", "alegria", "algoritmo", "alicate", "almohada", "almuerzo", "alondra",
                        "alpaca", "alumno", "amapola", "amigo", "amor", "ancla", "andamio", "anillo", "anochecer",
                        "antena", "antilope", "anuncio", "apagador", "arandano", "arbol", "archivo", "arena",
                        "armario", "aro", "arte", "artista", "asado", "ascensor", "asesino", "asno", "aspiradora",
                        "astro", "atardecer", "atleta", "atmósfera", "atomico", "atraccion", "avalancha", "ave",
                        "avellana", "avion", "aviso", "azar", "azucar", "azulejo", "bacteria", "bailar", "bala",
                        "balcon", "ballena", "bambu", "banana", "bandera", "banco", "barba", "barco", "barniz",
                        "barra", "barrio", "basura", "baston", "batalla", "bateria", "bebida", "becerro", "bebe",
                        "biblioteca", "bicho", "bicicleta", "billetera", "billete", "biologia", "blanco", "bloque",
                        "boca", "bolsa", "bomba", "bombero", "bondad", "bosque", "botella", "boton", "bravo",
                        "brazo", "brisa", "brocha", "bruja", "brujula", "bronce", "brote", "buey", "buho",
                        "burbuja", "burro", "caballo", "cabra", "cacao", "cactus", "cadena", "cadera", "cafetera",
                        "caja", "cajon", "calabaza", "calcio", "calle", "calor", "camaleon", "camarero", "cambiar",
                        "camello", "camino", "campana", "campo", "canario", "cancion", "cangrejo", "cansancio",
                        "canto", "cañon", "capitan", "cara", "caracol", "caramelo", "caravana", "carbon", "carcaj",
                        "cardumen", "carga", "caricia", "carne", "carpa", "carreta", "carro", "carta", "cascada",
                        "casco", "casa", "casco", "castillo", "castor", "catorce", "cava", "caverna", "cebolla",
                        "cedro", "ceja", "celebrar", "celeste", "celula", "cemento", "cena", "ceniza", "centella",
                        "centro", "ceramica", "cereal", "cereza", "cerdo", "cerebro", "cerradura", "cerro", "cesped",
                        "chacal", "chaleco", "champu", "charco", "cheque", "chico", "chocolate", "chofer", "chorro",
                        "chuleta", "cielo", "cigarra", "cigüeña", "cima", "cine", "cinta", "circo", "ciruela",
                        "cisne", "ciudad", "clamor", "claridad", "clase", "clave", "clavo", "cliente", "clima",
                        "coche", "cocina", "coco", "colador", "colchon", "colegio", "colibri", "colina", "colmena",
                        "color", "cometa", "comida", "compas", "computadora", "conejo", "confeti", "congreso",
                        "consejo", "constelacion", "contorno", "corazon", "corcho", "cordero", "cordillera", "coro",
                        "corona", "correr", "corteza", "cortina", "cosa", "cosecha", "cosmos", "craneo", "crema",
                        "criatura", "cristal", "cruz", "cuadro", "cuaderno", "cuerda", "cuerno", "cuento", "cuerpo",
                        "cuestion", "cueva", "cuna", "cupo", "cura", "curiosidad", "curso", "dado", "dama", "danza",
                        "dardo", "delfin", "delgado", "demora", "dentista", "deporte", "derrota", "desafio", "desierto",
                        "despensa", "destino", "diente", "dificil", "dinosaurio", "dinero", "disco", "diseño", "dormir",
                        "dragon", "drama", "dulce", "duque", "eco", "edificio", "educacion", "efecto", "ejemplo",
                        "elefante", "elevador", "elote", "embarcacion", "emblema", "empanada", "empleado", "energia",
                        "enfermedad", "ensalada", "entusiasmo", "equipo", "escalera", "escoba", "escuela", "esfera",
                        "esfuerzo", "espada", "espantapajaros", "espejo", "espejismo", "esponja", "esposa", "estrella",
                        "estructura", "estudiante", "eterno", "examen", "exito"
                    ]
                elif opcion1 == 2:
                    palabras = [
                        "aguacate", "albaricoque", "arandano", "babaco", "banana", "caqui", "cereza",
                        "chirimoya", "ciruela", "coco", "dátil", "durazno", "feijoa", "fresa", "frambuesa",
                        "granada", "guayaba", "higo", "jacarandá", "kiwi", "lima", "limon", "litchi",
                        "mamon", "mandarina", "mango", "manzana", "maracuya", "melocoton", "melon",
                        "membrillo", "mora", "naranja", "nectarina", "nispero", "papaya", "pera", "piña",
                        "pitahaya", "platano", "pomelo", "sandía", "tamarindo", "toronja", "uva", "yaca",
                        "zarzamora"
                    ]
                elif opcion1 == 3:
                    palabras = [
                        "acelga", "ajo", "alcachofa", "apio", "berenjena", "brocoli", "calabacin",
                        "calabaza", "cebolla", "col", "coliflor", "esparrago", "espinaca", "judia",
                        "lechuga", "maiz", "nabo", "papa", "pepino", "pimiento", "rabano", "remolacha",
                        "repollo", "zanahoria", "batata", "boniato", "champiñon", "coles de bruselas",
                        "endibia", "guisante", "hongo", "jengibre", "kale", "ñame", "patata", "puerro",
                        "rucula", "tomate", "yuca"
                    ]
                elif opcion1 == 4:
                    palabras = [
                        "abeja", "aguila", "ajolote", "alce", "antilope", "araña", "avestruz", "ballena",
                        "bisonte", "buho", "caballo", "cabra", "camello", "canguro", "caracol", "cebra",
                        "cerdo", "chimpance", "cisne", "cocodrilo", "colibri", "conejo", "delfin",
                        "elefante", "erizo", "escorpion", "flamenco", "foca", "gallina", "gato", "guepardo",
                        "gorila", "hipopotamo", "hormiga", "jaguar", "jirafa", "koala", "leon", "leopardo",
                        "lobo", "loro", "mariposa", "medusa", "mono", "murcielago", "nutria", "oso",
                        "oveja", "panda", "pantera", "pato", "pelicano", "pinguino", "polilla", "puma",
                        "rana", "raton", "rinoceronte", "salmon", "serpiente", "tiburon", "tigre", "topo",
                        "tortuga", "vaca", "zorro"
                    ]
                elif opcion1 == 5:
                    palabras = [
                        "avocado", "apricot", "blueberry", "babaco", "banana", "persimmon", "cherry",
                        "cherimoya", "plum", "coconut", "date", "peach", "feijoa", "strawberry",
                        "raspberry", "pomegranate", "guava", "fig", "jacaranda", "kiwi", "lime",
                        "lemon", "lychee", "mamón", "mandarin", "mango", "apple", "passion fruit",
                        "nectarine", "melon", "quince", "blackberry", "orange", "papaya", "pear",
                        "pineapple", "dragon fruit", "plantain", "grapefruit", "watermelon", "tamarind",
                        "grape", "jackfruit", "beetroot", "spinach", "artichoke", "asparagus", "lettuce",
                        "corn", "potato", "radish", "rhubarb", "beet", "cabbage", "cauliflower", "carrot",
                        "celery", "onion", "garlic", "acorn", "almond", "pecan", "walnut", "apricot",
                        "cashew", "chestnut", "pistachio", "squash", "zucchini", "cucumber", "pumpkin",
                        "eggplant", "broccoli", "bean", "lentil", "pea", "chickpea", "mushroom",
                        "ginger", "kale", "yam", "leek", "arugula", "tomato", "yucca", "acorn", "almond",
                        "pecan", "walnut", "bee", "eagle", "axolotl", "moose", "antelope", "spider",
                        "ostrich", "whale", "bison", "owl", "horse", "goat", "camel", "kangaroo",
                        "snail", "zebra", "pig", "chimpanzee", "swan", "crocodile", "hummingbird",
                        "rabbit", "dolphin", "elephant", "hedgehog", "scorpion", "flamingo", "seal",
                        "chicken", "cat", "cheetah", "gorilla", "hippopotamus", "ant", "jaguar",
                        "giraffe", "koala", "lion", "leopard", "wolf", "parrot", "butterfly", "jellyfish",
                        "monkey", "bat", "otter", "bear", "sheep", "panda", "panther", "duck",
                        "pelican", "penguin", "moth", "cougar", "frog", "mouse", "rhino", "salmon",
                        "snake", "shark", "tiger", "mole", "turtle", "cow", "fox"
                    ]
                elif opcion1 == 6:
                    break
                else:
                    print("Opción no válida. Por favor, elige una opción de 1-6.")
                    continue
                
                if palabras:
                    run_game(palabras)

        elif opcion == 2:
            show_credits()
            input("\nPresiona ENTER para volver al menú principal...")
            
        elif opcion == 3:
            print("Saliendo del Ahorcado...")
            time.sleep(1)
            break
        
        else:
            print("Opción no válida. Por favor, elige 1, 2 o 3.")

poblacion = {
    'Poblacion': 0,
    'COCoins': 1500,
    'Comida': {'Pan': 0, 'Carne': 0, 'Pollo': 0},
    'Felicidad': 90,
    'Hambre': 50
}

META_POBLACION = 500 

def elevento_ciudad(p):
    eventos = ["Incendio", "Inundación", "Fiesta popular",
               "Plaga de ratas", "Crisis económica", "Guerra",
               "Cosecha abundante", "Descubrimiento de oro"]

    if random.random() < 0.3:
        evento = random.choice(eventos)
        print(f"\n>>> EVENTO ALEATORIO: {evento}! <<<")

        if evento == "Incendio":
            p['Poblacion'] = max(0, p['Poblacion'] - 10)
            p['Felicidad'] = max(0, p['Felicidad'] - 10)
            print("Un incendio destruyó parte de la ciudad (-10 población, -10 felicidad).")

        elif evento == "Inundación":
            p['COCoins'] = max(0, p['COCoins'] - 100)
            p['Comida']['Pan'] = max(0, int(p['Comida']['Pan'] * 0.8))
            print("Las lluvias arrasaron los cultivos (-100 COCoins y -20% Pan).")

        elif evento == "Fiesta popular":
            p['Felicidad'] = min(100, p['Felicidad'] + 20)
            p['COCoins'] = max(0, p['COCoins'] - 50)
            print("Una fiesta alegró a la gente (+20 felicidad, -50 COCoins).")

        elif evento == "Plaga de ratas":
            for comida in p['Comida']:
                p['Comida'][comida] = max(0, p['Comida'][comida] - 5)
            print("Una plaga de ratas devoró la comida (-5 a todos los alimentos).")

        elif evento == "Crisis económica":
            p['COCoins'] = max(0, p['COCoins'] - 200)
            p['Felicidad'] = max(0, p['Felicidad'] - 15)
            print("Una crisis sacudió la ciudad (-200 COCoins, -15 felicidad).")

        elif evento == "Guerra":
            p['Poblacion'] = max(0, p['Poblacion'] - 15)
            p['COCoins'] = max(0, p['COCoins'] - 150)
            p['Felicidad'] = max(0, p['Felicidad'] - 10)
            print("Estalló una guerra (-15 población, -150 COCoins, -10 felicidad).")

        elif evento == "Cosecha abundante":
            p['Comida']["Pan"] += 20
            p['Comida']["Carne"] += 10
            p['Comida']["Pollo"] += 10
            p['Hambre'] = max(0, p['Hambre'] - 10)
            print("Una cosecha abundante llenó los graneros (+20 Pan, +10 Carne, +10 Pollo).")

        elif evento == "Descubrimiento de oro":
            p['COCoins'] += 300
            print("¡Descubrieron oro en las minas! (+300 COCoins).")

        p['Felicidad'] = max(0, min(100, p['Felicidad']))
    else:
        print("\nNo ocurrió ningún evento este turno.")

def mostrar_estado_ciudad(p):
    print(f"\n------ ESTADO DE {nombreciudad.upper()} ------")
    print(f"\tPOBLACION: {p['Poblacion']}")
    print(f"\tCOCOINS: {p['COCoins']}")
    print(f"\tFELICIDAD: {p['Felicidad']}%")
    print(f"\tHAMBRE: {p['Hambre']}%")
    print("\tCOMIDA:")
    for i, e in p["Comida"].items():
        print(f"\t  {i}: {e}")
    print("-----------------------------------------")

def construir_casa_ciudad(p):
    if p['COCoins'] >= 200:
        p['COCoins'] -= 200
        p['Poblacion'] += 20
        print("Construiste una casa (+20 población, -200 COCoins).")
    else:
        print("No tienes suficientes COCoins para construir.")
    chequear_estado_ciudad(p)

def cobrar_impuestos_ciudad(p):
    if p['Poblacion'] > 0:
        dinero = p['Poblacion'] * 2
        p['COCoins'] += dinero
        p['Felicidad'] = max(0, p['Felicidad'] - 15)
        print(f"Cobraste impuestos (+{dinero} COCoins, -15 felicidad).")
    else:
        print("No hay población para cobrar impuestos.")
    chequear_estado_ciudad(p)

def comprar_comida_ciudad(p):
    precios = {"Pan": 5, "Carne": 20, "Pollo": 15}
    opciones = list(precios.keys())

    print("\n--- MERCADO ---")
    for i, comida in enumerate(opciones, start=1):
        print(f"{i}. {comida} - {precios[comida]} COCoins c/u")
    print(f"{len(opciones)+1}. Salir")

    try:
        eleccion = int(input("Elige una opción: "))
    except ValueError:
        print("Opción inválida.")
        return

    if 1 <= eleccion <= len(opciones):
        comida_elegida = opciones[eleccion - 1]
        try:
            cantidad = int(input(f"¿Cuántos {comida_elegida} desea comprar?: "))
        except ValueError:
            print("Cantidad inválida.")
            return

        costo = precios[comida_elegida] * cantidad
        if p['COCoins'] >= costo:
            p['COCoins'] -= costo
            p['Comida'][comida_elegida] += cantidad
            print(f"Compraste {cantidad} {comida_elegida} por {costo} COCoins.")
        else:
            print("No tienes suficiente dinero.")
    elif eleccion == len(opciones) + 1:
        print("Volviendo al menú principal...")
    else:
        print("Opción inválida.")

    chequear_estado_ciudad(p)

def pasar_turno_ciudad(p):
    consumo = p['Poblacion'] // 10
    if consumo == 0:
        print("No hay suficiente población para consumir comida.")
    else:
        if p['Comida']['Carne'] >= consumo:
            p['Comida']['Carne'] -= consumo
            print(f"La población consumió {consumo} de Carne.")
        elif p['Comida']['Pollo'] >= consumo:
            p['Comida']['Pollo'] -= consumo
            print(f"La población consumió {consumo} de Pollo.")
        elif p['Comida']['Pan'] >= consumo:
            p['Comida']['Pan'] -= consumo
            print(f"La población consumió {consumo} de Pan.")
        else:
            p['Poblacion'] = max(0, p['Poblacion'] - 5)
            p['Felicidad'] = max(0, p['Felicidad'] - 10)
            p['Hambre'] = min(100, p['Hambre'] + 10)
            print("No hay suficiente comida. La gente pasa hambre (Hambre ↑10, Población ↓5, Felicidad ↓10).")

    elevento_ciudad(p)

    if p['Felicidad'] <= 0 and p['Poblacion'] > 0:
        muertos = max(1, p['Poblacion'] // 10)
        p['Poblacion'] = max(0, p['Poblacion'] - muertos)
        print(f"La felicidad llegó a 0. Hubo desorden y murieron {muertos} personas.")

    chequear_estado_ciudad(p)

def celebrar_fiesta_ciudad(p):
    if p['COCoins'] < 150:
        print("No hay suficientes COCoins para celebrar una fiesta.")
        return
    else:
        p['COCoins'] -= 150
        p['Felicidad'] = min(100, p['Felicidad'] + 20)
        p['Hambre'] = max(0, p['Hambre'] - 5)
        print("Fiesta celebrada con éxito (+20 Felicidad, -150 COCoins).")
    chequear_estado_ciudad(p)

def fin_juego_ciudad(p, victoria):
    print("\n===== FIN DE LA PARTIDA =====")
    if victoria:
        print(f"🎉 ¡Ganaste! Alcanzaste {p['Poblacion']} habitantes.")
    else:
        print("💀 Tu ciudad colapsó.")
    print(f"Monedas finales: {p['COCoins']}")
    print(f"Comida almacenada: {p['Comida']}")
    print(f"Felicidad final: {p['Felicidad']}%")
    print(f"Hambre final: {p['Hambre']}%")
    print("=============================")
    exit()

def chequear_estado_ciudad(p):
    p['Felicidad'] = max(0, min(100, p['Felicidad']))
    p['Hambre'] = max(0, min(100, p['Hambre']))

    if p['Poblacion'] >= META_POBLACION:
        fin_juego_ciudad(p, victoria=True)

    if p['Felicidad'] <= 20 and p['Poblacion'] > 0:
        print("Advertencia: la felicidad está muy baja. Si llega a 0, morirán habitantes.")

def menu_ciudades():
    global nombreciudad
    slow_print("1969. Ciudad de Verona. Eres un rey al cuál desterraron de sus tierras.")
    print()
    slow_print("Pudiste escapar con un poco de tus riquezas.")
    print()
    slow_print("Has encontrado amplio terreno en el que deseas volver a gobernar una ciudad y poder ser un rey respetado.")
    print()
    slow_print("...")
    print()
    input("\n(Presiona Enter para comenzar)\n")

    print("---------- MI CIUDAD ----------")
    print("RECURSOS INICIALES")
    print(f"\tPOBLACION: {poblacion['Poblacion']}")
    print(f"\tCOCOINS: {poblacion['COCoins']}")
    print(f"\tFELICIDAD: {poblacion['Felicidad']}%")
    print(f"\tHAMBRE: {poblacion['Hambre']}%")
    print("\tCOMIDA:")
    for alimento, cantidad in poblacion["Comida"].items():
        print(f"\t  {alimento}: {cantidad}")

    print("-----------------------------\n")
    print("ELIJA EL NOMBRE DE SU CIUDAD")
    nombreciudad = input("> ")
    print("Los datos se han ingresado correctamente.")
    print("-----------------------------\n")
    print(f'BIENVENIDO A "{nombreciudad.upper()}"')

    while True:
        mostrar_estado_ciudad(poblacion)
        print("\n¿Qué quiere hacer?")
        print("1 - Construir casas (Población ↑20, COCoins ↓200)")
        print("2 - Cobrar impuestos (COCoins ↑, Felicidad ↓15)")
        print("3 - Comprar comida (Pan/Carne/Pollo)")
        print("4 - Celebrar una fiesta (Felicidad ↑20, COCoins ↓150)")
        print("5 - Pasar de turno (la población consume comida / pueden ocurrir eventos)")
        print("6 - Salir")

        opcion = input("> ").strip()
        if opcion == "1":
            construir_casa_ciudad(poblacion)
        elif opcion == "2":
            cobrar_impuestos_ciudad(poblacion)
        elif opcion == "3":
            comprar_comida_ciudad(poblacion)
        elif opcion == "4":
            celebrar_fiesta_ciudad(poblacion)
        elif opcion == "5":
            pasar_turno_ciudad(poblacion)
        elif opcion == "6":
            print("Volviendo al menú principal...")
            break
        else:
            print("Opción no válida, intenta de nuevo.")

def main_menu():
    while True:
        print("\n=====================================")
        print("        🎮  MENÚ DE JUEGOS 🎮")
        print("=====================================")
        print("1. Piedra, Papel o Tijera")
        print("2. Ahorcado")
        print("3. Creación de Ciudades")
        print("4. Créditos")
        print("5. Salir")
        print("=====================================")

        try:
            opcion = int(input("> "))
        except ValueError:
            print("Por favor, ingresa un número válido.")
            continue

        if opcion == 1:
            piedra_papel_tijera()
        elif opcion == 2:
            ahorcado()
        elif opcion == 3:
            menu_ciudades()
        elif opcion == 4:
            show_credits()
            input("\nPresiona ENTER para volver al menú principal...")
        elif opcion == 5:
            print("Saliendo del programa...")
            time.sleep(1)
            break
        else:
            print("Opción no válida. Por favor, elige 1-5.")

if __name__ == "__main__":
    main_menu()
