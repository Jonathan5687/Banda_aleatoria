from musicos import * 

t = Musicos()

t.agregar_instrumento(Guitarra)
t.agregar_instrumento(guacharaca)
t.agregar_instrumento(caja)
t.agregar_instrumento(acordeon)
t.agregar_instrumento(bajo)

for i in range(5): 
    a = t.entregar_instrumento()
    print(a.afinar(), a.tocar())
