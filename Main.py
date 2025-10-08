import esencial
import comenzar
import chica
import chico

mostrar = esencial.necesario()

class Juego:
  def main(self):
    chose = int(input("¿Quien serás en esta aventura? 1 para alba, 2 para steve: "))
    if chose == 1:
      alma = chica.aruba
      alma()
    elif chose == 2:
      esteban = chico.SteneU
      esteban()

  def mostrar_estado_personajes(self):
    print("Alba:", vars(mostrar.alba))
    print("Steve:", vars(mostrar.steve))


print(comenzar.principio())
juego = Juego()
juego.mostrar_estado_personajes()
juego.main()

