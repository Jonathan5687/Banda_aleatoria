from musicos import * 

t = Musicos()

t.agregar_animal(Guitarra)
t.agregar_animal(guacharaca)
t.agregar_animal(caja)
t.agregar_animal(acordeon)

for i in range(4): 
    a = t.entregar_instrumento()
    print(a.afinar(), a.tocar())
