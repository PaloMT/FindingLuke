import random
import time
import esencial

portal = esencial.necesario()
magic = esencial.magia()


def pelea_tigres():
  print("ALBA-Tengo la sensación de que va a ocurrir algo malo")
  time.sleep(3)
  print("🐯🐯🐯")
  print("Tres tigres se avalanzan hacia tí")
  while portal.tigreA > 0 & portal.tigreB > 0 & portal.tigreC > 0:
    print("¿Que usarás? ¿La espada que quita", portal.espada,
          "de vida?\n¿Tu puños que sus usos son ilimitado pero quita",
          portal.puños, "?\n o la varita que tiene", magic.usos, "y quita",
          magic.varita, "?")
    opt8 = float(input("1 espada, 2 puños, 3 varita : "))
    if opt8 == 1:
      opt9 = int(
          input(
              "A que tigre vas a atacar) (derecha 1, centro 2, izquierda 3)"))
      if opt9 == 1:
        if portal.tigreA > 0:
          portal.tigreA = portal.tigreA - portal.espada
          print("Le has dado un espadazo")
          print("vida restante del zombie: ", portal.tigreA)
          ataque2 = random.randint(1, 2)
          ataque = random.randint(0, 1)
          print("Los tigres atacan")
          print("el tigre de la derecha te quita", ataque)
          print("el tigre del centro te quita", ataque2)
          print("el tigre de la izquierda te quita", ataque)
          portal.alba.salud = portal.alba.salud - ataque - ataque2 - ataque
          print("te queda de vida:", portal.alba.salud)
          time.sleep(3)
        else:
          print("Ya está muesto, le estas ando a un cadáver")
          time.sleep(3)
      if opt9 == 2:
        if portal.tigreB > 0:
          portal.tigreB = portal.tigreB - portal.espada
          print("Le has dado un espadazo")
          print("vida restante del tigre: ", portal.tigreB)
          ataque2 = random.randint(1, 2)
          ataque = random.randint(0, 1)
          print("Los tigres atacan")
          print("el tigre de la derecha te quita", ataque)
          print("el tigre del centro te quita", ataque2)
          print("el tigre de la izquierda te quita", ataque)
          portal.alba.salud = portal.alba.salud - ataque - ataque2 - ataque
          print("te queda de vida:", portal.alba.salud)
          time.sleep(3)
        else:
          print("Ya está muesto, le estas ando a un cadáver")
          time.sleep(3)
      if opt9 == 3:
        if portal.tigreC > 0:
          portal.tigreC = portal.tigreC - portal.espada
          print("Le has dado un espadazo")
          print("vida restante del tigre: ", portal.tigreC)
          ataque2 = random.randint(1, 2)
          ataque = random.randint(0, 1)
          print("Los tigres atacan")
          print("el tigre de la derecha te quita", ataque)
          print("el tigre del centro te quita", ataque2)
          print("el tigre de la izquierda te quita", ataque)
          portal.alba.salud = portal.alba.salud - ataque - ataque2 - ataque
          print("te queda de vida:", portal.alba.salud)
          time.sleep(3)
        else:
          print("Ya está muesto, le estas ando a un cadáver")
          time.sleep(3)
    elif opt8 == 2:
      opt9 = int(
          input(
              "A que tigre vas a atacar) (derecha 1, centro 2, izquierda 3)"))
      if opt9 == 1:
        if portal.tigreA > 0:
          portal.tigreA = portal.tigreA - portal.puños
          print("Le has dado un espadazo")
          print("vida restante del zombie: ", portal.tigreA)
          ataque2 = random.randint(1, 2)
          ataque = random.randint(0, 1)
          print("Los tigres atacan")
          print("el tigre de la derecha te quita", ataque)
          print("el tigre del centro te quita", ataque2)
          print("el tigre de la izquierda te quita", ataque)
          portal.alba.salud = portal.alba.salud - ataque - ataque2 - ataque
          print("te queda de vida:", portal.alba.salud)
          time.sleep(3)
        else:
          print("Ya está muesto, le estas ando a un cadáver")
          time.sleep(3)
      if opt9 == 2:
        if portal.tigreB > 0:
          portal.tigreB = portal.tigreB - portal.puños
          print("Le has dado un espadazo")
          print("vida restante del tigre: ", portal.tigreB)
          ataque2 = random.randint(1, 2)
          ataque = random.randint(0, 1)
          print("Los tigres atacan")
          print("el tigre de la derecha te quita", ataque)
          print("el tigre del centro te quita", ataque2)
          print("el tigre de la izquierda te quita", ataque)
          portal.alba.salud = portal.alba.salud - ataque - ataque2 - ataque
          print("te queda de vida:", portal.alba.salud)
          time.sleep(3)
        else:
          print("Ya está muesto, le estas ando a un cadáver")
          time.sleep(3)
      if opt9 == 3:
        if portal.tigreC > 0:
          portal.tigreC = portal.tigreC - portal.puños
          print("Le has dado un espadazo")
          print("vida restante del tigre: ", portal.tigreC)
          ataque2 = random.randint(1, 2)
          ataque = random.randint(0, 1)
          print("Los tigres atacan")
          print("el tigre de la derecha te quita", ataque)
          print("el tigre del centro te quita", ataque2)
          print("el tigre de la izquierda te quita", ataque)
          portal.alba.salud = portal.alba.salud - ataque - ataque2 - ataque
          print("te queda de vida:", portal.alba.salud)
          time.sleep(3)
        else:
          print("Ya está muesto, le estas ando a un cadáver")
          time.sleep(3)
    elif opt8 == 3:
      if magic.usos > 0:
        magic.usos = magic.usos - 1
      elif magic.usos == 0:
        magic.varita = 0
      print("usos restantes de la varita", magic.usos)
      ataque = random.randint(0, 2)
      ataque2 = random.randint(1, 2)
      print("Le has lanzado un hechizo a todos los tigres")
      print("vida restante de los tigres: ", portal.tigretotal)
      print("El los tigres atacan")
      print("el tigre de la derecha te quita", ataque)
      print("el tigre del centro te quita", ataque2)
      print("el tigre de la izquierda te quita", ataque)
      portal.alba.salud = portal.alba.salud - ataque - ataque2 - ataque
      print("te queda de vida:", portal.alba.salud)
      time.sleep(3)
  if portal.alba.salud <= 0:
    print(
        "  🟥🟥🟥       🟥🟥      🟥      🟥     🟥🟥🟥🟥\n 🟥          🟥    🟥  🟥  🟥 🟥   🟥   🟥\n🟥  🟥🟥     🟥🟥🟥🟥  🟥    🟥     🟥  🟥🟥🟥\n 🟥     🟥   🟥    🟥  🟥           🟥  🟥\n  🟥🟥🟥     🟥    🟥  🟥           🟥  🟥🟥🟥🟥"
    )
    print("")
    print(
        "  🟥🟥🟥   🟥         🟥  🟥🟥🟥🟥   🟥🟥🟥\n🟥      🟥  🟥      🟥    🟥         🟥    🟥\n🟥      🟥   🟥    🟥     🟥🟥🟥     🟥🟥🟥\n🟥      🟥    🟥  🟥      🟥         🟥   🟥\n  🟥🟥🟥        🟥        🟥🟥🟥🟥   🟥    🟥"
    )
    dec = ""
    while dec != "s" or dec != "n":
      dec = input("¿Quieres reperit la pelea? (s o n) ")
      if dec == "s":
        pelea_tigres()
      elif dec == "n":
        print("Alba ha sido derrotada. El juego ha terminado.")
        exit()
      else:
        print("Ha habido un error de teclado")


def pelea_zombies():
  print("🧟‍♂️")
  print("Steve - ¡CUIDADO!")
  opt1 = int(
      input(
          "Alba ha sido atacado por un zombie ¿Que vas a hacer? 1 para irte, 2 para atacar :"
      ))
  if opt1 == 1:
    print("has dejado que se coman a tu compañera, luego te comieron a tí")
    print(
        "  🟥🟥🟥       🟥🟥      🟥      🟥     🟥🟥🟥🟥\n 🟥          🟥    🟥  🟥  🟥 🟥   🟥   🟥\n🟥  🟥🟥     🟥🟥🟥🟥  🟥    🟥     🟥  🟥🟥🟥\n 🟥     🟥   🟥    🟥  🟥           🟥  🟥\n  🟥🟥🟥     🟥    🟥  🟥           🟥  🟥🟥🟥🟥"
    )
    print("")
    print(
        "  🟥🟥🟥   🟥         🟥  🟥🟥🟥🟥   🟥🟥🟥\n🟥      🟥  🟥      🟥    🟥         🟥    🟥\n🟥      🟥   🟥    🟥     🟥🟥🟥     🟥🟥🟥\n🟥      🟥    🟥  🟥      🟥         🟥   🟥\n  🟥🟥🟥        🟥        🟥🟥🟥🟥   🟥    🟥"
    )
    exit()
  elif opt1 == 2:
    print("¡Has decidido pelear!")
    while portal.zombie_vida > 0:
      print("¿Que usarás? ¿La espada que quita", portal.espada,
            "de vida?\n¿Tu puños que sus usos son ilimitado pero quita",
            portal.puños, "?\n o la varita que tiene", magic.usos, "y quita",
            magic.varita, "?")
      opt2 = float(input("1 espada, 2 puños, 3 varita : "))
      if opt2 == 1:
        ataque = random.randint(0, 3)
        portal.zombie_vida = portal.zombie_vida - portal.espada
        ataque = random.randint(0, 3)
        print("Le has dado un espadazo")
        print("vida restante del zombie: ", portal.zombie_vida)
        print("El zombie ataca")
        print("el zombie te quita", ataque)
        portal.alba.salud = portal.alba.salud - ataque
        print("te queda de vida:", portal.alba.salud)
        time.sleep(3)
      elif opt2 == 2:
        ataque = random.randint(0, 3)
        portal.zombie_vida = portal.zombie_vida - portal.puños
        ataque = random.randint(0, 3)
        print("Le has dado un puñetazo")
        print("vida restante del zombie: ", portal.zombie_vida)
        print("El zombie ataca")
        print("el zombie te quita", ataque)
        portal.alba.salud = portal.alba.salud - ataque
        print("te queda de vida:", portal.alba.salud)
        time.sleep(3)
      elif opt2 == 3:
        if magic.usos > 0:
          magic.usos = magic.usos - 1
        elif magic.usos == 0:
          magic.varita = 0
        print("usos restantes de la varita", magic.usos)
        ataque = random.randint(0, 3)
        print("Le has lanzado un hechizo")
        print("vida restante del zombie: ", portal.zombie_vida)
        print("El zombie ataca")
        print("el zombie te quita", ataque)
        portal.alba.salud = portal.alba.salud - ataque
        print("te queda de vida:", portal.alba.salud)
        time.sleep(3)
  if portal.alba.salud <= 0:
    print(
        "  🟥🟥🟥       🟥🟥      🟥      🟥     🟥🟥🟥🟥\n 🟥          🟥    🟥  🟥  🟥 🟥   🟥   🟥\n🟥  🟥🟥     🟥🟥🟥🟥  🟥    🟥     🟥  🟥🟥🟥\n 🟥     🟥   🟥    🟥  🟥           🟥  🟥\n  🟥🟥🟥     🟥    🟥  🟥           🟥  🟥🟥🟥🟥"
    )
    print("")
    print(
        "  🟥🟥🟥   🟥         🟥  🟥🟥🟥🟥   🟥🟥🟥\n🟥      🟥  🟥      🟥    🟥         🟥    🟥\n🟥      🟥   🟥    🟥     🟥🟥🟥     🟥🟥🟥\n🟥      🟥    🟥  🟥      🟥         🟥   🟥\n  🟥🟥🟥        🟥        🟥🟥🟥🟥   🟥    🟥"
    )
    dec = ""
    while dec != "s" or dec != "n":
      dec = input("¿Quieres reperit la pelea? (s o n) ")
      if dec == "s":
        pelea_zombies()
      elif dec == "n":
        print("Alba ha sido derrotada. El juego ha terminado.")
        exit()
      else:
        print("Ha habido un error de teclado")


def pelea_final():
  opt11 = int(
      input("JJ quiere pelear ¿Que vas a hacer? 1 para irte, 2 para atacar :"))
  if opt11 == 1:
    print("Es la pelea final, no puedes huir. Te has muerto")
    print(
        "  🟥🟥🟥       🟥🟥      🟥      🟥     🟥🟥🟥🟥\n 🟥          🟥    🟥  🟥  🟥 🟥   🟥   🟥\n🟥  🟥🟥     🟥🟥🟥🟥  🟥    🟥     🟥  🟥🟥🟥\n 🟥     🟥   🟥    🟥  🟥           🟥  🟥\n  🟥🟥🟥     🟥    🟥  🟥           🟥  🟥🟥🟥🟥"
    )
    print("")
    print(
        "  🟥🟥🟥   🟥         🟥  🟥🟥🟥🟥   🟥🟥🟥\n🟥      🟥  🟥      🟥    🟥         🟥    🟥\n🟥      🟥   🟥    🟥     🟥🟥🟥     🟥🟥🟥\n🟥      🟥    🟥  🟥      🟥         🟥   🟥\n  🟥🟥🟥        🟥        🟥🟥🟥🟥   🟥    🟥"
    )
    exit()
  elif opt11 == 2:
    print("¡Has decidido pelear!")
    while portal.jj_vida > 0:
      print("¿Que usarás? ¿La espada que quita", portal.espada,
            "de vida?\n¿Tu puños que sus usos son ilimitado pero quita",
            portal.puños, "?\n o la varita que tiene", magic.usos, "y quita",
            magic.varita, "?")
      opt12 = float(input("1 espada, 2 puños, 3 varita : "))
      if opt12 == 1:
        ataque = random.randint(0, 2)
        portal.jj_vida = portal.jj_vida - portal.espada
        print("Le has dado un espadazo")
        print("vida restante de JJ: ", portal.jj_vida)
        print("JJ te ataca")
        print("JJ te quita", ataque)
        portal.alba.salud = portal.alba.salud - ataque
        print("te queda de vida:", portal.alba.salud)
        time.sleep(3)
      elif opt12 == 2:
        ataque = random.randint(0, 2)
        portal.jj_vida = portal.jj_vida - portal.puños
        print("Le has dado un puñetazo")
        print("vida restante del JJ: ", portal.jj_vida)
        print("JJ te ataca")
        print("JJ te quita", ataque)
        portal.alba.salud = portal.alba.salud - ataque
        print("te queda de vida:", portal.alba.salud)
        time.sleep(3)
      elif opt12 == 3:
        if magic.usos > 0:
          magic.usos = magic.usos - 1
        elif magic.usos == 0:
          magic.varita = 0
        print("usos restantes de la varita", magic.usos)
        ataque = random.randint(0, 2)
        print("Le has lanzado un hechizo")
        portal.jj_vida = portal.jj_vida - magic.varita
        print("vida restante de JJ: ", portal.jj_vida)
        print("JJ te ataca")
        print("JJ te quita", ataque)
        portal.alba.salud = portal.alba.salud - ataque
        print("te queda de vida:", portal.alba.salud)
        time.sleep(3)

  if portal.alba.salud <= 0:
    print(
        "  🟥🟥🟥       🟥🟥      🟥      🟥     🟥🟥🟥🟥\n 🟥          🟥    🟥  🟥  🟥 🟥   🟥   🟥\n🟥  🟥🟥     🟥🟥🟥🟥  🟥    🟥     🟥  🟥🟥🟥\n 🟥     🟥   🟥    🟥  🟥           🟥  🟥\n  🟥🟥🟥     🟥    🟥  🟥           🟥  🟥🟥🟥🟥"
    )
    print("")
    print(
        "  🟥🟥🟥   🟥         🟥  🟥🟥🟥🟥   🟥🟥🟥\n🟥      🟥  🟥      🟥    🟥         🟥    🟥\n🟥      🟥   🟥    🟥     🟥🟥🟥     🟥🟥🟥\n🟥      🟥    🟥  🟥      🟥         🟥   🟥\n  🟥🟥🟥        🟥        🟥🟥🟥🟥   🟥    🟥"
    )
    dec = ""
    while dec != "s" or dec != "n":
      dec = input("¿Quieres reperit la pelea? (s o n) ")
      if dec == "s":
        pelea_final()
      elif dec == "n":
        print("Alba ha sido derrotada. El juego ha terminado.")
        exit()
      else:
        print("Ha habido un error de teclado")
