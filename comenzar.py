import time


def principio():
  print("  🌲🌲🌲🌄🌲🌲🌲\n  🌲🌲        🌲🌲\n🌲🏡           🌲🌲")
  time.sleep(1)
  print(
      "   🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧\n🟧 🛏️         🖼️          🟧\n🟫 🛏️ 🛏️ 👫  🧍🚪   🪑🪑🪑🟫\n   🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫"
  )
  time.sleep(3)
  print("LUKE: Voy a tomar el aire, que tengo calor")
  time.sleep(1)
  print("  🌲🌲🌲🌄🌲🌲🌲\n  🌲🌲        🌲🌲\n🌲🏡🧍​           🌲🌲")
  time.sleep(2)
  print("  🌲🌲🌲🌄🌲🌲🌲\n  🌲🌲       🕴️​ 🌲🌲\n🌲🏡🧍​           🌲🌲")
  print(
      "JEFFREY JONES: Ahí está el ingenuo de Luke, ese me las pagará por cazar en mi bosque."
  )
  time.sleep(4)
  print(" ")

  repeticiones = 10
  mensajes = [
      "  🌲🌲       🕴️ 🌲🌲\n🌲🏡🧍           🌲🌲",
      "  🌲🌲       🌲🌲\n🌲🏡🧍           🕴️🌲🌲",
      "  🌲🌲       🌲🌲\n🌲🏡🧍      🕴️      🌲🌲",
      "  🌲🌲        🌲🌲\n🌲🏡🧍  🕴️         🌲🌲",
      "  🌲🌲        🌲🌲\n🌲🏡🧍🕴️          🌲🌲",
      "  🌲🌲        🌲🌲\n🌲🏡   🧍🕴️        🌲🌲",
      "  🌲🌲       🌲🌲\n🌲🏡        🧍🕴️   🌲🌲",
      "  🌲🌲       🌲🌲\n🌲🏡          🧍🕴️  🌲🌲",
      "  🌲🌲        🌲🌲\n🌲🏡            🧍🌲🌲", "  🌲🌲        🌲🌲\n🌲🏡             🌲🌲"
  ]

  for i in range(repeticiones):
    mensaje_actual = mensajes[i % len(mensajes)]
    time.sleep(0.25)
    print("\r" + "\r" + " " * 50, end='', flush=True)
    print("\033[F" + "\r" + " " * 50, end='', flush=True)
    print("\r" + mensaje_actual, end='', flush=True)
    print("\033[F" + "\r" + mensaje_actual, end='', flush=True)
    time.sleep(0.25)

  time.sleep(2)
  repeticiones = 9
  mensajes = ["🌑", "🌒", "🌓", "🌔", "🌕", "🌖", "🌗", "🌘", "🌑"]

  for i in range(repeticiones):
    mensaje_actual = mensajes[i % len(mensajes)]

    time.sleep(0.25)

    print("\r" + " " * 40, end='', flush=True)  # Borra la línea actual
    print(f"\r{mensaje_actual}.", end='', flush=True)
    time.sleep(0.25)

  print("")
  print(
      "   🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧\n🟧 🛏️         🖼️         🟧\n🟫 🛏️ 🛏️ 🙎  🚪🤵  🪑🪑🪑🟫\n   🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫"
  )
  time.sleep(2)
  print(
      "STEVE- ¡Luke! ¡Luke!... ALBA, Luke no está \n ALBA- ¿Cómo que no está? Busca bien \nSTEVE- Ya he buscado por los alrededores, no está, yo creo que es obra del Cazador de Cazadores. Ya sabes lo mucho que nos odia."
  )
  time.sleep(10)
  print("📱")
  print(
      "ALBA- ¿Quién será?\nSTEVEN- Lo cojo yo ¿Decime Arturo?\nROMINA- No soy Arturo, soy la mano derecha de Jeffrey Jones, me llamo Romina. El señor Cazador dice que se ha llevado preso a un boludo llamado Luke,\npor romper la norma de no cazar en su terreno, y que no le devolverá, sino que tendrá que venir vos.\nALBA- Hermano, ¿qué dice?\nSTEVEN- Jones tiene a Luke, hay que rescatarlo.\nALBA- Sí, vayamos pues."
  )
  time.sleep(20)
  print(
      "🟥🟥🟥    🟥🟥🟥   🟥      🟥  🟥🟥🟥    🟥🟥🟥   🟥      🟥    🟥🟥🟥   \n🟥          🟥     🟥🟥    🟥  🟥   🟥     🟥     🟥🟥    🟥  🟥         \n🟥🟥🟥      🟥     🟥  🟥  🟥  🟥   🟥     🟥     🟥  🟥  🟥 🟥     🟥🟥\n🟥          🟥     🟥    🟥🟥  🟥   🟥     🟥     🟥    🟥🟥  🟥      🟥\n🟥        🟥🟥🟥   🟥      🟥  🟥🟥🟥    🟥🟥🟥   🟥      🟥    🟥🟥🟥  "
  )
  print(
      "🟦        🟦    🟦   🟦    🟦  🟦🟦🟦🟦\n🟦        🟦    🟦   🟦  🟦    🟦       \n🟦        🟦    🟦   🟦🟦      🟦🟦🟦  \n🟦        🟦    🟦   🟦   🟦   🟦       \n🟦🟦🟦      🟦🟦     🟦     🟦 🟦🟦🟦🟦"
  )
  time.sleep(3)