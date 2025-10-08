import time
import random
import esencial
import Random_Adventuresg
import peleas_tía
import finalconalba

aleatorio = Random_Adventuresg.aawa()
Misiones = [aleatorio.anciana, aleatorio.hada, aleatorio.vendedor]
Misión_elegida = random.choice(Misiones)

portal = esencial.necesario()
magic = esencial.magia()


def aruba():
  global available_missions
  while portal.alba.salud > 0:
    print("Has elegido a Alba, ¡Que comience la aventura!")
    print(portal.inventario)
    time.sleep(4)
    Misiones.remove(Misión_elegida)
    print(
        "🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳\n🌳 🌳 🏚️ 🏚️ 🌿        🌿  🏚️ 🏚️ 🏚️🌳🌳\n🌳  🏚️ 🏚️ 🌿       🌿     👫🌳🏚️ 🏚️ 🏚️🌳"
    )
    time.sleep(4)
    print(
        "Alba-  Mira alba, estamos en la ciudad abandonada. Hay que tener cuidado, ya sabes los rumores sobre este lugar.\nALBA- Sí, dice que toda su población se convirtió en Zombies hace décadas."
    )
    time.sleep(4)
    zombie = peleas_tía.pelea_zombies
    zombie()
    print("Lo has conseguido! Tu inteligencia ha subido un punto")
    portal.alba.inteligencia = portal.alba.inteligencia + 1
    portal.alba.salud = 9
    
    print(
        "Alba- Gracias por salvarme , aquí no está Luke. Sigamos nuestro camino"
    )
    
    Misión_elegida()
    
    
    portal.alba.salud = 9
    
    tiger = peleas_tía.pelea_tigres
    tiger()
    
    portal.alba.salud = 9
    Misión_elegida()
    Misiones.remove(Misión_elegida)
    
    portal.alba.salud = 9
    chao = finalconalba.villano
    chao.jj()
    portal.alba.salud = 9