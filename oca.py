import random

def tiro():
    dado = random.randrange(1, 6)
    dado = str(dado)
    return dado

jugador = input("¿Como te llamas?: ")

lista = ["1", "2", "3", "4", "OCA", "PUENTE", "7", "8", "OCA", "10", "11", "PUENTE", "13", "OCA", "15", "16", "17",
         "OCA", "POSADA", "20", "21", "22", "OCA", "24", "25", "DADOS", "OCA", "28", "29", "30", "POZO", "OCA", "33",
         "34", "35", "OCA", "37", "38", "39", "40", "OCA", "LABERINTO", "43", "44", "OCA", "46", "47", "49", "OCA",
         "51", "52", "DADOS", "OCA", "55", "CARCEL", "57", "CALAVERA", "OCA", "60", "61", "62", "63"]
patata = 0
posc_jugador = 0
posc_maquina = 0
turno = ""
while patata <= 10:
    patata += 1
    lista_tmp = lista
    dado = tiro()
    dado = int(dado)

    if turno == "jugador":
        posc_jugador += dado
        print("%s te ha tocado el número %d" % (jugador, dado))
        print("Este es el tablero")
        lista_tmp[dado-1] = jugador
        print(lista_tmp)
    elif turno == "maquina":
        posc_maquina += dado
        print("A la maquina le ha tocado el número %d" % (dado))
        print("Este es el tablero")
        lista_tmp[dado-1] = "maquina"
        print(lista_tmp)
    else:
        posc_jugador += dado
        print("%s te ha tocado el número %d" % (jugador, dado))
        print("Este es el tablero")
        lista_tmp[dado-1] = jugador
        print(lista_tmp)
