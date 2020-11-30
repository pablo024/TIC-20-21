def operar(num1, num2, operacion):
    operaciones = {
        "S": "+",
        "R": "-",
        "M": "*",
        "D": "/",
    }
    if operacion == "D" and num2 == 0:
        return "Error. El denominador no puede ser 0"
    else:
        return eval(str(num1)+operaciones[operacion]+str(num2))

print(operar(5,0,"D"))
