import random
import os
import time

def clear():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

def tiro():
    dado = random.randrange(1, 6)
    dado = str(dado)
    return dado

def lista_mapa():
    lista = ["1", "2", "3", "4", "OCA", "PUENTE", "7", "8", "OCA", "10", "11", "PUENTE", "13", "OCA", "15", "16", "17",
         "OCA", "POSADA", "20", "21", "22", "OCA", "24", "25", "DADOS", "OCA", "28", "29", "30", "POZO", "OCA", "33",
         "34", "35", "OCA", "37", "38", "39", "40", "OCA", "LABERINTO", "43", "44", "OCA", "46", "47", "49", "OCA",
         "51", "52", "DADOS", "OCA", "55", "CARCEL", "57", "CALAVERA", "OCA", "60", "61", "62", "63"]
    return lista
def oca(posicion, turno):
    mod_oca = 0
    lista_tmp = lista_mapa()
    for i in lista_tmp:
        mod_oca += 1
        if i == "OCA":
            if (mod_oca) > (posicion):
                posc_uno = mod_oca
                break
            else:
                continue
    print("te ha tocado la oca---")
    return posc_uno, turno

def puente(posicion):
    mod_oca = 0
    lista_tmp = lista_mapa()
    for i in lista_tmp:
        mod_oca += 1
        if i == "OCA":
            if (mod_oca) > (posicion):
                posc_uno = mod_oca
                break
            else:
                continue
    print("te ha tocado la oca---")
    return posc_uno, "jugador"
jugador = input("¿Como te llamas?: ")
maquina = ""

patata = 0
posc_jugador = 0
posc_maquina = 0
turno = ""


while True:
    lista_tmp = lista_mapa()
    dado = tiro()
    dado = int(dado)

    if turno == "jugador":
        if (posc_jugador + dado) > len(lista_tmp):
            turno = "maquina"
            print("te has pasado de valor, consigue el valor exacto")
            pass
        elif (posc_jugador + dado) == len(lista_tmp):
            posc_jugador += dado
            lista_tmp[posc_jugador-1] = jugador.upper()
            lista_tmp[posc_maquina-1] = "MAQUINA"
            print("%s te ha tocado el número %d" % (jugador, dado))
            print("Este es el tablero")
            pass
        elif (posc_jugador + dado) < len(lista_tmp):
            posc_jugador += dado
            clear()
            print("%s te ha tocado el número %d" % (jugador, dado))
            print("Este es el tablero")
            #Se comprueba la casilla oca
            if lista_tmp[posc_jugador-1] == "OCA":
                posc_jugador, turno = oca(posc_jugador)
               
            #Se comprueba la casilla puente
            elif lista_tmp[posc_jugador-1] == "PUENTE":
                pass
            else:
                turno = "maquina"

            #Aquí es donde se imprime el tablero  
            if posc_jugador == posc_maquina:
                lista_tmp[posc_jugador-1] = "MAQUINA + " + jugador
            elif posc_jugador != posc_maquina:
                    lista_tmp[posc_jugador-1] = jugador.upper()
                    lista_tmp[posc_maquina-1] = "MAQUINA"
            print(lista_tmp)
            #time.sleep(0.8)
       
    elif turno == "maquina":
        if (posc_maquina + dado) > len(lista_tmp):
            turno = "jugador"
            print("la maquina se ha pasado de valor")
            pass
        elif (posc_maquina + dado) == len(lista_tmp):
            posc_maquina += dado
            lista_tmp[posc_jugador-1] = jugador.upper()
            lista_tmp[posc_maquina-1] = "MAQUINA"
            print("A la maquina le ha tocado el número %d" %(dado))
            print("Este es el tablero")
            pass
        elif (posc_maquina + dado) < len(lista_tmp):
            posc_maquina += dado
            clear()
            print("A la maquina le ha tocado el número %d" %(dado))
            print("Este es el tablero")
            if lista_tmp[posc_maquina-1] == "OCA":
                posc_maquina, turno = oca(posc_maquina)
            else:
                pass

           
            if posc_jugador == posc_maquina:
                lista_tmp[posc_jugador-1] = "MAQUINA + " + jugador
            elif posc_jugador != posc_maquina:
                    lista_tmp[posc_jugador-1] = jugador.upper()
                    lista_tmp[posc_maquina-1] = "MAQUINA"
            print(lista_tmp)
            turno = "jugador"
            #time.sleep(0.8)
    else:
        clear()
        posc_jugador += dado
        print("%s te ha tocado el número %d" % (jugador, dado))
        print("Este es el tablero")
        if lista_tmp[posc_jugador-1] == "OCA":
                posc_jugador, turno = oca(posc_jugador)
        else:
            turno = "maquina"
        lista_tmp[dado-1] = jugador.upper()
        print(lista_tmp)

        #time.sleep(0.8)
   
    if posc_jugador == len(lista_mapa()):
        clear()
        print(lista_tmp)
        print("Has ganado---------")
        break
    elif posc_maquina == len(lista_mapa()):
        clear()
        print(lista_tmp)
        print("Ha ganado la maquina---------")
        break
