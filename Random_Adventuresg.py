import time
import esencial
import random

portal = esencial.necesario()
magic = esencial.magia()


class aawa:

  def hada(self):
    print("🌳 🌳🌳🌳🌳     🌳🌳🌳🌳\n🌳🌳  🧚     👫    🌳🌳🌳\n🌳🌳🌳🌳🌳🌳🌳         🌳🌳")
    print("STEVEN-¿Que es eso?\nALBA-Creo que eso no eran hierbas de té")
    time.sleep(5)
    print(
        "HADA-Soy un hada de los bosques más profundos, la espada que porte en mis manos tiene un valor incalculable, devolverme mis riquezas apresadas en aquella cueva y el arma será toda vuestra"
    )
    
    elec = float(input("Aceptas la misión? (1 sí, 2 no)  "))
    
    if elec == 1:
      print("HADA-Muchas gracias por ayudarme, la cueva es aquella de allá")
      time.sleep(3)
      print(
          "🟫🟫🟫🟫🟫🟫🟫\n🟫🪨         🪨 🟫\n🟫🐉             \n🟫🪨       🪨 👫🟫                                          \n🟫🟫🟫🟫🟫🟫🟫"
      )
      print(
          "ALBA-Revuerdame por que estamos haciento esto, ya que por si no te has dado cuenta...\nSTEVE-¡¡ESO ES UN PUTO DRAGÓN!!"
      )
      time.sleep(5)
      
      def dragstica():
        print("¡Has decidido pelear!")
        while portal.dragovida > 0:
          print("¿Que usarás? ¿La espada que quita", portal.espada,
                "de vida?\n¿Tu puños que sus usos son ilimitado pero quita",
                portal.puños, "?\n o la varita que tiene", magic.usos, "y quita",
                magic.varita, "?")
          opt3 = float(input("1 espada, 2 puños, 3 varita : "))
          
          if opt3 == 1:
            ataque = random.randint(1, 4)
            portal.dragovida = portal.dragovida - portal.espada
            print("Le has dado un espadazo")
            print("vida restante del dragón: ", portal.dragovida)
            print("El dragón ataca")
            print("el dragón te quita", ataque)
            portal.alba.salud = portal.alba.salud - ataque
            print("te queda de vida:", portal.alba.salud)
            time.sleep(3)
            
          elif opt3 == 2:
            ataque = random.randint(1, 4)
            portal.dragovida = portal.dragovida - portal.puños
            print("Le has dado un puñetazo")
            print("vida restante del dragón: ", portal.dragovida)
            print("El dragón ataca")
            print("el dragón te quita", ataque)
            portal.alba.salud = portal.alba.salud - ataque
            print("te queda de vida:", portal.alba.salud)
            time.sleep(3)
            
          elif opt3 == 3:
            ataque = random.randint(1, 4)
            if magic.usos > 0:
              magic.usos = magic.usos - 1
            elif magic.usos == 0:
              magic.varita = 0
            print("usos restantes de la varita", magic.usos)
            portal.dragovida = portal.dragovida - magic.varita
            print("Le has lanzado un hechizo")
            print("vida restante del dragón: ", portal.dragovida)
            print("El dragón ataca")
            print("el dragón te quita", ataque)
            portal.alba.salud = portal.alba.salud - ataque
            print("te queda de vida:", portal.alba.salud)
            time.sleep(3)
        print("¡Has derrotado al dragón!")
        
        if portal.steve.salud <= 0:
          print(
              "  🟥🟥🟥       🟥🟥      🟥      🟥     🟥🟥🟥🟥\n 🟥          🟥    🟥  🟥  🟥 🟥   🟥   🟥\n🟥  🟥🟥     🟥🟥🟥🟥  🟥    🟥     🟥  🟥🟥🟥\n 🟥     🟥   🟥    🟥  🟥           🟥  🟥\n  🟥🟥🟥     🟥    🟥  🟥           🟥  🟥🟥🟥🟥"
          )
          print("")
          print(
              "  🟥🟥🟥   🟥         🟥  🟥🟥🟥🟥   🟥🟥🟥\n🟥      🟥  🟥      🟥    🟥         🟥    🟥\n🟥      🟥   🟥    🟥     🟥🟥🟥     🟥🟥🟥\n🟥      🟥    🟥  🟥      🟥         🟥   🟥\n  🟥🟥🟥        🟥        🟥🟥🟥🟥   🟥    🟥"
          )
          dec= ""
          while dec != "s" or dec != "n":
            dec= input("¿Quieres reperit la pelea? (s o n) ")
            if dec == "s":
              dragstica()
            elif dec == "n":
              print("Alba ha sido derrotada. El juego ha terminado.")
              exit()
          else:
            print("Ha habido un error de teclado")
      dragstica()
      
      portal.alba.salud = 9
      print(
          "ALBA-La proxima vez no grites, ¿Ok?\nSTEVEN-Ok ok, volvamos con el hada"
      )
      time.sleep(3)
      print("🌳 🌳🌳🌳🌳     🌳🌳🌳🌳\n🌳🌳  🧚🪙     👫   🌳🌳🌳\n🌳🌳🌳🌳🌳🌳🌳         🌳🌳")
      print("HADA-Muchas gracias, aquí teneis vuestra parte del trato")
      print("Ahora la espara pegará 3,5 en vez de 2")
      portal.espada = portal.espada + 1, 5
      time.sleep(5)

  def anciana(self):
    print("🌳🌳      👵           💁‍♀️🤵  🌳🌳🌳")
    time.sleep(1.5)
    print("ALBA- Steve, es la abuela, esa que va siempre a ver a su nieta, la de la capucha roja.")
    opt4 = int(input("Se la ve perdida ¿Deseas ayudarla?(1 para sí, otro número para no)"))
    if opt4 == 1:
      print("ANCIANA-Necesito ayuda, iba a ir a merendar con mi nieta pero se me ha olvidado la ruta. Vosostros pareceís conocerla ¿me podriaís acompañar?\nSTEVEN-¡Claro! No será problema, nos pilla de camino y no es mucho tiempo")
      time.sleep(8)
      print("ANCIANA-Muchas gracias jovénes , se nota que teneís un corazón de oro")
      time.sleep(3)
      print("Estuvieron caminando los tres por el bosque durante unos minutos, se empezaron a oir unos ruidos extraño")
      time.sleep(4)
      print("ALBA-¿Que es eso que se escucha?")
      time.sleep(2)
      
      def lobitos():
        print("AUUUUUUU!")
        print("¡El lobo se avalanza contra tí!")
        while portal.lobovida > 0:
  
          print("¿Que usarás? ¿La espada que quita", portal.espada,
                "de vida?\n¿Tu puños que sus usos son ilimitado pero quita",
                portal.puños, "?\n o la varita que tiene", magic.usos, "y quita",
                magic.varita, "?")
          opt5 = float(input("1 espada, 2 puños, 3 varita : "))
          
          if opt5 == 1:
            ataque = random.randint(0, 3)
            portal.lobovida = portal.lobovida - portal.espada
            print("Le has dado un espadazo")
            print("vida restante del lobo: ", portal.lobovida)
            print("El lobo te muerde")
            print("el lobo te quita", ataque)
            portal.alba.salud = portal.alba.salud - ataque
            print("te queda de vida:", portal.alba.salud)
            time.sleep(3)
            
          elif opt5 == 2:
            ataque = random.randint(0, 3)
            portal.lobovida = portal.lobovida - portal.puños
            print("Le has dado un puñetazo")
            print("vida restante del lobo: ", portal.lobovida)
            print("El lobo te muerde")
            print("el lobo te quita", ataque)
            portal.alba.salud = portal.alba.salud - ataque
            print("te queda de vida:", portal.alba.salud)
            time.sleep(3)
            
          elif opt5 == 3:
            ataque = random.randint(2, 3)
            if magic.usos > 0:
              magic.usos = magic.usos - 1
            elif magic.usos == 0:
              magic.varita = 0
            portal.lobovida = portal.lobovida - magic.varita
            print("usos restantes de la varita", magic.usos)
            print("Le lanzado un hechizo")
            print("vida restante del dragón: ", portal.lobovida)
            print("El lobo te muerde")
            print("el lobo te quita", ataque)
            portal.alba.salud = portal.alba.salud - ataque
            print("te queda de vida:", portal.alba.salud)
            time.sleep(3)
            
        if portal.steve.salud <= 0:
          print(
              "  🟥🟥🟥       🟥🟥      🟥      🟥     🟥🟥🟥🟥\n 🟥          🟥    🟥  🟥  🟥 🟥   🟥   🟥\n🟥  🟥🟥     🟥🟥🟥🟥  🟥    🟥     🟥  🟥🟥🟥\n 🟥     🟥   🟥    🟥  🟥           🟥  🟥\n  🟥🟥🟥     🟥    🟥  🟥           🟥  🟥🟥🟥🟥"
          )
          print("")
          print(
              "  🟥🟥🟥   🟥         🟥  🟥🟥🟥🟥   🟥🟥🟥\n🟥      🟥  🟥      🟥    🟥         🟥    🟥\n🟥      🟥   🟥    🟥     🟥🟥🟥     🟥🟥🟥\n🟥      🟥    🟥  🟥      🟥         🟥   🟥\n  🟥🟥🟥        🟥        🟥🟥🟥🟥   🟥    🟥"
          )
          dec= ""
          while dec != "s" or dec != "n":
            dec= input("¿Quieres reperit la pelea? (s o n) ")
            if dec == "s":
              lobitos()
            elif dec == "n":
              print("Alba ha sido derrotada. El juego ha terminado.")
              exit()
          else:
            print("Ha habido un error de teclado")
        print("¡Has derrotado al lobo!")
        
      lobitos()
      portal.alba.salud = 9
      print("Tu fuerza ha subido un punto y medio")
      portal.puños = portal.puños + 1.5
      print(
          "NIETA-¡Abuela!\nANCIANA-¡Cariño!Muchas gracias aventureros por vuestra ayuda, podeis venir a merendar a mi casa cuando querais"
      )
      print("La anciana te ha dado 7 monedas")
      portal.monedas = portal.monedas + 7
      time.sleep(5)

  def vendedor(self):
    print(
        "carpitero-¡Muy buenas aventureros!, teneis una varita muy interesante ahí ¿Quereís que la arregle por 7 monedas?"
    )
    if portal.monedas >= 7:
      opt7 = int(input("¿Te gustaría reparar la varita? (1 para sí) "))
      if opt7 == 1:
        print("Aquí tienen, que pasen buena tarde")
        print("La varita ha sido reparada")
        magic.varita = 5
        magic.usos = 5
        time.sleep(7)
    else:
      print(
          "STEVEN-No tenemos suficiente dinero, gracia por su oferta igualmente \nCARPINTERO-Que pena, otra vez será, suerte en vuestra aventura"
      )
      time.sleep(7)
