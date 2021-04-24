from src.logica.ecuacionSegundoGrado import ecuacionSegundoGrado


def solucionarEcuacion ( a , b , c ) :
    solucion.definirParametros ( a , b , c )
    solucion.solucionECS ( )
    solucion.imprimirSolución ( )


if __name__ == '__main__' :
    solucion = ecuacionSegundoGrado ( )

    solucionarEcuacion ( 1 , 2 , 1 )
    solucionarEcuacion ( 3 , -5 , 1 )
    solucionarEcuacion ( 1 , 4 , 4 )
    solucionarEcuacion ( 1 , 1 , 1)
    solucionarEcuacion ( 1 , 2 , 3 )
