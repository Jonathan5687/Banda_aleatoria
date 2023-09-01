class Instrumento: 
	def afinar(self): 
		pass

	def tocar(self): 
		pass
        

class Guitarra (Instrumento): 
	
	def afinar(self): 
		print("Afinando guitarra") 

	def tocar(self): 
		print("Tocando guitarra") 


class guacharaca (Instrumento): 
	
	def afinar(self): 
		print("guacharaca no necesita ser afinada") 

	def tocar(self): 
		print("Tocando guacharaca") 


class caja(Instrumento): 
	
	def afinar(self): 
		print("caja no necesita ser afinada") 

	def tocar(self): 
		print("Tocando caja") 


class Acordeon (Instrumento): 
	
	def afinar(self): 
		print("Afinando acordeon") 

	def tocar(self): 
		print("Tocando acordeon") 

