import time
import peleas_tía
import esencial

portal = esencial.necesario()


def cocina():
  print(
      "En la cocina no había nada más que pizza con piña, cerveza caliente y un menú de MacFish"
  )
  time.sleep(6)


def sala():
  opt10 = input(
      "Hay algo raro en el centro de mesa ¿deseas mirar que es?(s o n): ")
  if opt10 == "s":
    print("¡Feliciades! ¡Has encontrado la llave!")
    portal.inventario.append("🗝️")
    print(portal.inventario)


def baño():
  print(
      "Entras a baño, el pestillo no cierra bien, el papel es fino y con textura rugosa y con un inodoro chino"
  )
  time.sleep(6)


def jardin():
  print(
      "Solo hay un casillo inchable pinchado, un tobogán sin escaleras y una piscina de color amarillo que no te atreves a preguntar de que está llena"
  )
  time.sleep(6)


class villano():

  def jj():
    huevo = "UN HUEVO"
    print("🌳🌳🌳🌳🌳🌳🌳🌳🌳\n🌳🌳  👫    🧙🏰🌳\n🌳🌳        🌳🌳🌳")
    time.sleep(1)
    print(
        "ALBA-¿Que es eso?\nRIONO-¡os habeís robado mi varita!\nSTEVEN-¿Que varita?\nALBA-¿Esta baratija?"
        + portal.inventario[1] +
        "\nRIONO-Os vais a enterar, haber como pasaís ahora")
    time.sleep(5)
    print("💥💥💥💥💥💥💥💥💥\n💥💥💥💥💥💥💥💥💥\n💥💥💥💥💥💥💥💥💥")
    time.sleep(0.5)
    print("🌳🌳🌳🌳🌳🌳🌳🌳🌳\n🌳🌳  👫    🦏🏰🌳\n🌳🌳        🌳🌳🌳")
    time.sleep(1)
    print("RINO-Responder a la siguiente pregunta y os dejaré marchar")
    egg = ""
    while huevo != egg:
      egg = input(
          "¿Qué es más útil roto que intacto? (respuesta en mayúsculas): ")
      if egg != huevo:
        print("Respuesta incorrecta")
    print("RINO-Respuesta correcta, podeís pasar")
    print(
        "ALBA-Pues no era tan dificíl\nSTEVEN-Sigamos, ahí está Romina\nROMINA-¡Ahí están ustedes! Pero no se confíen, porque mi jefe es re astuto y los va a atrapar. Y yo voy a estar para verlo. Con el fierro tienen que volar la puerta"
    )
    time.sleep(7)
    yes = "s"
    si = ""
    while yes != si:
      si = input("¿Derribar la puerta? (s o n): ")
      if yes != si:
        print("No, espera, así no debería de ir, repetimos")
        time.sleep(3.5)
    print("Tardas 20 minutos a espadazos y consigues derribar la puerta")
    print(
        "STEVE-Jones, ríndete, te atraparemos.\nROMINA- No lo conseguireis, aunque encontréis a Luke necesitas la llave para entrar a la mazmorra."
    )
    habs = []
    while "🗝️" not in portal.inventario:
      room = input(
          "¿A donde quieres ir primero? ¿a la sala principal(s)? ¿A la cocina(c)? ¿Al baño(b)? ¿O al jardín(j)? "
      )
      if room == "c":
        if room in habs:
          print("Ya has estado en esta habitación")
        else:
          cocina()
          habs.append(room)
      if room == "j":
        if room in habs:
          print("Ya has estado en esta habitación")
        else:
          jardin()
          habs.append(room)
      if room == "b":
        if room in habs:
          print("Ya has estado en esta habitación")
        else:
          baño()
          habs.append(room)
      if room == "s":
        sala()
    print("ALBA-¡Por fin podremos salvar a Luke!\nJJ-¡No tan rápido!")
    time.sleep(3)
    print("")
    final = peleas_tía.pelea_final
    final()
    print(
        "JJ-Me habeís derrotado, habeis ganado la batalla¡Pero no la guerra!\nALBA-Se ha esfumado\nSTEVEN-Vamos a sacar a Luke"
    )
    time.sleep(5)
    print("👫  🧍")
    time.sleep(1)
    print("STEVEN-¡Luke!¿Estás bien?\nLUKE-Sisi, muchas gracias chicos")
    time.sleep(5)
    repeticiones = 4
    mensajes = [
        ".",
        "..",
        "...",
        "ALBA-¿Ahora  que?",
    ]
    for i in range(repeticiones):
      mensaje_actual = mensajes[i % len(mensajes)]
      time.sleep(1)
      print("\r" + "\r" + " " * 25, end='', flush=True)
      print("\r" + mensaje_actual, end='', flush=True)
      time.sleep(1)
    print("")
    print("LUKE-¿Alguien tiene hambre?")
    time.sleep(4)
    print(
        "🟥🟥🟥    🟥🟥🟥   🟥      🟥  🟥🟥🟥    🟥🟥🟥   🟥      🟥    🟥🟥🟥   \n🟥          🟥     🟥🟥    🟥  🟥   🟥     🟥     🟥🟥    🟥  🟥         \n🟥🟥🟥      🟥     🟥  🟥  🟥  🟥   🟥     🟥     🟥  🟥  🟥 🟥     🟥🟥\n🟥          🟥     🟥    🟥🟥  🟥   🟥     🟥     🟥    🟥🟥  🟥      🟥\n🟥        🟥🟥🟥   🟥      🟥  🟥🟥🟥    🟥🟥🟥   🟥      🟥    🟥🟥🟥  "
    )
    time.sleep(1.5)
    print(
        "🟦        🟦    🟦   🟦    🟦  🟦🟦🟦🟦\n🟦        🟦    🟦   🟦  🟦    🟦       \n🟦        🟦    🟦   🟦🟦      🟦🟦🟦  \n🟦        🟦    🟦   🟦   🟦   🟦       \n🟦🟦🟦      🟦🟦     🟦     🟦 🟦🟦🟦🟦"
    )
    time.sleep(3)
