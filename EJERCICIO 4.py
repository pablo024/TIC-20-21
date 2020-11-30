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
        return "Tiene que introducir un número entre 1 y 12"

numero_mes = int(input("Introduce el número de un mes: "))
print(mes(numero_mes))
