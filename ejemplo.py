def programa():
    n=0
    x=input("x= ")
    m=0
    for cont in range(0,x):
        if(cont % 3==0):
            n=n+cont
        else:
            m=m+cont
    print n, m
programa()
        
