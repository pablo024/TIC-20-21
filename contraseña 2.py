'''Introduce un nombre y un apellido. Genera una contrase�a a partir
de 3 letras del nombre y 3 del apellido'''
def contrasena_2():
    nombre=raw_input=("Nombre: ")
    apellido=raw_input("Apellido: ")
    contrasena=nombre[-3:]+apellido[-3:]
    print("Contrasena: ",contrasena)



    
