def convertir_dol_a_eur():
    dolares = input("Introduce el n�mero de d�lares que quieres convertir a euros: ")
    if type(dolares) == int or type(dolares) == float:
        print str(dolares*0.85) + " �"
    else:
        print "No has introducido un n�mero v�lido"

convertir_dol_a_eur()
