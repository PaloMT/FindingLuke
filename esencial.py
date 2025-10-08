class personaje:

  def __init__(self, salud, fuerza, inteligencia):
    self.salud = salud
    self.fuerza = fuerza
    self.inteligencia = inteligencia

class necesario:

  def __init__(self):
    self.dragovida = 10
    self.monedas = 0
    self.lobovida = 6.75
    self.espada = 2
    self.puños = 0.5
    self.alba = personaje(9, 4, 8)
    self.steve = personaje(8, 5, 6)
    self.inventario = ["⚔️", "🪄"]
    self.zombie_vida = 7
    self.jj_vida = 12
    self.condición = True
    self.tigreA = 2
    self.tigreB = 2
    self.tigreC = 2
    self.tigretotal = self.tigreA + self.tigreB + self.tigreC

class magia:

  def __init__(self):
    self.usos = 0
    self.varita = 0
