def dia_de_la_semana(num):
    if num >= 1 and num <= 7:
        dias = ["lunes","martes","mi�rcoles","jueves","viernes","s�bado","domingo"]
        return dias[num - 1]
    else:
        return "no_valido"

dia_semana = dia_de_la_semana(input("Introduce un n�mero entre 1 y 7: "))
if dia_semana  == "no_valido":
    print "No has introducido un valor v�lido"
else:
    print "Es " + dia_semana
