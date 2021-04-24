import math


class ecuacionSegundoGrado ( ) :

    def __init__ ( self ) :
        self.a = 0
        self.b = 0
        self.c = 0

    def solucionECS ( self ) :
        self.x1 = ""
        self.x2 = ""
        d = self.b * self.b - 4 * self.a * self.c
        if d >= 0 :
            r1 = (-self.b + math.sqrt ( d )) / (2 * self.a)
            r2 = (-self.b - math.sqrt ( d )) / (2 * self.a)
            self.x1 = "{0:.2f}".format ( r1 )
            self.x2 = "{0:.2f}".format ( r2 )

        return self.x1 , self.x2

    def definirParametros ( self , a , b , c ) :
        self.a = a
        self.b = b
        self.c = c

    def imprimirSolución ( self ) :
        print ( "\nEcuación de segundo grado" )
        print ( "{0:.2f}X^2 + {1:.2f}X + {2:.2f}".format ( self.a , self.b , self.c ) )
        print ( "\nSolución:" )
        x1 , x2 = self.solucionECS ( )
        print ( f"X1 = {x1}" )
        print ( f"X2 = {x2}" )
