def  multiplicar ():
    multiplicacion  =  1
    para  i  en el  rango ( 4 ):
        num  =  input ( "Introduce el n�mero" + str ( i + 1 ) + ":" )
        si  tipo ( num ) ==  int :
            multiplicacion  =  multiplicacion * num
        otra cosa :
            imprimir  "No has introducido un n�mero"
    imprimir  "Producto:"  +  str ( multiplicacion )
        
multiplicar ()
