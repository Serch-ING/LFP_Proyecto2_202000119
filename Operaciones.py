
def ObtencionTokens(texto):
    repetir = True
    estado = 0
    txtTemp = ""
    columna = 1
    fila = 1


    for txt in texto:
        repetir = True
        while repetir:
            if estado==0:
                if isLetra(txt):
                    estado = 1
                    txtTemp += txt
                elif isNumero(txt):
                    estado = 4
                    txtTemp += txt
                elif ord(txt) == 34: # "
                    estado = 3
                    txtTemp += txt
                elif isSimbolo(txt):
                    estado = 2
                    txtTemp += txt
                elif ord(txt) == 35: # #
                    estado = 5
                    txtTemp += txt
                elif ord(txt) == 39: # '
                    estado = 6
                    txtTemp += txt
                else:

                    if ord(txt) == 32 or ord(txt) == 10 or ord(txt) == 9 or txt == '~':
                        pass
                    else: 
                        print("Error Lexico, se detecto " + txt + " en S0  F: " + str(fila) + ", C: " + str(columna))
                        errortipo= 'Caracter inesperado, esperaba L|D|#|S|"|@' 
            elif estado == 1:
                if (isLetra(txt)):
                    txtTemp += txt
                    estado = 1
                
                elif (ord(txt) == 95 ): # _
                    txtTemp += txt
                    estado = 1
                
                elif (isNumero(txt)):
                    txtTemp +=   txt
                    estado = 1
                else:
                    print("se reconocio en S1: '" + txtTemp + "' F: " + str(fila) + ", C: " + str(columna - len(txtTemp)))
                    txtTemp = ""
                    estado = 0
                    continue
            elif estado ==2:
                
                print("se reconocio en S2: '" + txtTemp + "' F: " + str(fila) + ", C: " + str(columna - len(txtTemp)))
                txtTemp = ""
                estado = 0
                continue
            elif estado ==3:
                if ord(txt) != 34: # "
                    txtTemp += txt
                else:
                    txtTemp += txt
                    estado = 2
                    



            # Salto de Linea
            if (ord(txt) == 10):
                columna = 1
                fila += 1
                repetir = False
                continue
            # Tab Horizontal
            elif (ord(txt) == 9):
                columna += 4
                repetir = False
                continue
            # Espacio
            elif (ord(txt) == 32):
                columna += 1
                repetir = False
                continue
            repetir = False
            columna += 1               
                       
       



def isLetra(txt):
    if((ord(txt) >= 65 and ord(txt) <= 90) or (ord(txt) >= 97 and ord(txt) <= 122) or ord(txt) == 164 or ord(txt) == 165):
        return True
    else:
        return False

def isSimbolo(txt):
    #           =                    ;              {                   }                   [               ]                   ,    
    if(ord(txt) == 61 or ord(txt) == 59 or ord(txt) == 123 or ord(txt) == 125  or ord(txt) == 91 or ord(txt) == 93 or ord(txt) == 44):
        return True
    else:
        return False

def isNumero(txt):
    if ((ord(txt) >= 48 and ord(txt) <= 57)):
        return True
    else:
        return False