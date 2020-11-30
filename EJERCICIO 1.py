def  multiplicar ():
    multiplicacion  =  1
    para  i  en el  rango ( 4 ):
        num  =  input ( "Introduce el número" + str ( i + 1 ) + ":" )
        si  tipo ( num ) ==  int :
            multiplicacion  =  multiplicacion * num
        otra cosa :
            imprimir  "No has introducido un número"
    imprimir  "Producto:"  +  str ( multiplicacion )
        
multiplicar ()
