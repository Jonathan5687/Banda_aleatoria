from musicos import * 

t = Musicos()

t.agregar_instrumento(guitarra)
t.agregar_instrumento(guacharaca)
t.agregar_instrumento(caja)
t.agregar_instrumento(acordeon)
t.agregar_instrumento(bajo)

for i in range(3): 
    a = t.entregar_instrumento()
    print(a.afinar(), a.tocar())
