def operar(num1, num2, operacion):
    operaciones = {
        "S": "+",
        "R": "-",
        "M": "*",
        "D": "/",
    }
    return eval(str(num1)+operaciones[operacion]+str(num2))

print(operar(5,3,"D"))
