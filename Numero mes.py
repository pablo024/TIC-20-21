'''Me va apedir el numero de un mes'''
def mes():
    abreviaMes="EneFebMarMayJunJulAgoSepOctNovDic"
    numeroMes=input("Introduce mes: ")
    pos=(numeroMes-1)*3
    print "El mes es: ", abreviaMes[pos:pos+3]
    

mes()
    
