'''
dime un numero al azar entre 1 y 1000 y lo adivino
'''
import random

def adivino_2():
    maxn=1000
    numero=random.randint(1,maxn)
    intento=input("intentalo: ")
    while intento!= numero:
        if intento>numero:
            print "Demasiado grande"
        if intento<numero:
            print "Demasiado pequeño"
        intento=input("intentalo: ")
    print "Ahora has acertado"


adivino_2()
