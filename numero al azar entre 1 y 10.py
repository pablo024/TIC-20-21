'''
dime un numero al azar entre 1 y 10 y lo adivino
'''
def adivino():
    numero=input("Dime un numero del 1 al 10: ")
    intento=input("intentalo: ")
    while intento!= numero:
        if intento>numero:
            print "Demasiado grande"
        if intento<numero:
            print "Demasiado pequeño"
        intento=input("intentalo: ")
    print "Ahora has acertado"


adivino()
