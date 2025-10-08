import time
import random
import esencial
import Random_Adventuresb
import peleas_tío
import finalconseteve

aleatorio = Random_Adventuresb.aaws()
Misiones = [aleatorio.ancianas, aleatorio.hadas, aleatorio.vendedores]
Misión_elegida = random.choice(Misiones)
portal = esencial.necesario()
magic = esencial.magia()


def SteneU():
  while portal.steve.salud > 0:
    print("Has elegido a Steve, ¡Que comience la aventura!")
    print(portal.inventario)
    time.sleep(4)
    
    n= Misión_elegida()
    print(n)
    Misiones.remove(n)
    
    print(
        "🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳\n🌳 🌳 🏚️ 🏚️ 🌿        🌿  🏚️ 🏚️ 🏚️🌳🌳\n🌳  🏚️ 🏚️ 🌿       🌿     👫🌳🏚️ 🏚️ 🏚️🌳"
    )
    time.sleep(4)
    print(
        "STEVEN-  Mira Alba, estamos en la ciudad abandonada. Hay que tener cuidado, ya sabes los rumores sobre este lugar.\nALBA- Sí, dice que toda su población se convirtió en Zombies hace décadas."
    )
    time.sleep(4)
    zombie = peleas_tío.pelea_zombies
    zombie()
    print("Lo has conseguido! Tu inteligencia ha subido un punto")
    portal.steve.salud = 9
    portal.steve.inteligencia = portal.steve.inteligencia + 1
    print(
        "Alba- Gracias por salvarme , aquí no está Luke. Sigamos nuestro camino"
    )
    time.sleep(4)
    p= Misión_elegida()
    print(p)
    Misiones.remove(p)
    
    tiger = peleas_tío.pelea_tigres
    tiger()
    portal.steve.salud = 9
    
    o= Misión_elegida()
    print(o)
    Misiones.remove(o)
    
    portal.steve.salud = 9
    chao = finalconseteve.villano
    chao.jj()
    portal.alba.salud = 9