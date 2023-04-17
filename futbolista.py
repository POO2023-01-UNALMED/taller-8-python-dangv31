from persona import Persona
from deportista import Deportista

class Futbolista (Persona, Deportista):
    listaFutbolistas = []
    def __init__(self, nombre, edad, altura, sexo, añosPracticando, golesMarcados, tarjetasRojas, piernaHabil):
        Persona.__init__(self, nombre, edad, altura, sexo)
        Deportista.__init__(self, "Futbol", añosPracticando)
        self._golesMarcados = golesMarcados
        self._tarjetasRojas = tarjetasRojas
        self._piernaHabil = piernaHabil
        Futbolista.listaFutbolistas(self)
    
    def __str__(self):
        return f"Mi nombre es {self.getNombre} soy profesional en el deporte {self.getDeporte} Tengo {self.getEdad} años de edad y llevo {self.getAñosPracticando} años en el deporte"
    
    def setGolesMarcados(self, golesMarcados):
        self._golesMarcados=golesMarcados
    def setTarjetasRojas(self, tarjetasRojas):
        self._tarjetasRojas=tarjetasRojas
    def setPiernaHabil(self, piernaHabil):
        self._piernaHabil=piernaHabil
    @classmethod
    def setListaFutbolistas(cls, list):
        cls.listaFutbolistas = list
    
    def getGolesMarcados(self):
        return self._golesMarcados
    def getTarjetasRojas(self):
        return self._tarjetasRojas
    def getPiernaHabil(self):
        return self._piernaHabil   
    @classmethod
    def getListaFutbolistas(cls):
        return cls.listaFutbolistas 