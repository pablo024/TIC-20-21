def mes(num):
    lista_meses = [
        "Enero",
        "Febrero",
        "Marzo",
        "Abril",
        "Mayo",
        "Junio",
        "Julio",
        "Agosto",
        "Septiembre",
        "Octubre",
        "Noviembre",
        "Diciembre"
    ]
    if num > 0 and num < 13:
        return lista_meses[num - 1]
    else:
        return "Tiene que introducir un n�mero entre 1 y 12"

numero_mes = int(input("Introduce el n�mero de un mes: "))
print(mes(numero_mes))
