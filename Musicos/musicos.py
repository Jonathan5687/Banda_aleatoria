from instrumentos import * 
from random import choice 

class Musicos:
    def __init__(self): 
        self.instrumentos = []
    
    def agregar_instrumento(self, instrumento): 
        self.instrumentos.append(instrumento)

    def entregar_instrumento(self): 
        return choice (self.instrumentos)
