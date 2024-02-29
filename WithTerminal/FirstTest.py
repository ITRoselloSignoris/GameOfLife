""" 

COMENTARIOS EXPLICANDO EN QUE SE DIFERENCIA CON EL OTRO PROGRAMA, Y QUE SE PUEDE HACER CON ESTE




"""

import random
import time 
from os import system, listdir

#Creacion de la matriz y asignacion de valores
def BoardState(width,height):
    ls = []
    for j in range(0,height):
        ls1 = []
        for k in range(0,width):
            ls1.append(random.randint(0,1))
        ls.append(ls1)
    return ls

def DeadState(width,height):
    return [[0 for i in range(width)]for j in range(height)]

def FileReading(Choice):
    with open(f"WithTerminal\PatronesPreestablecidos\{Choice}.txt", "r") as File:
        lines = [l.rstrip() for l in File.readlines()]

    height = len(lines)
    width = len(lines[0])
    board = DeadState(width, height)

    for x, line in enumerate(lines):
        for y, char in enumerate(line):
            board[x][y] = int(char)

    return board

def Render(Matriz):
    s = "-" * ((len(Matriz[0])) + 2)
    print(s)
    for i in Matriz:
        print("|", end = "")
        for l in i:
            if l == 1:
                print(u"\u2588", end = "")
            else:
                print(".",end = "")
        print("|")
    print(s)

def NextState(InitialState,NewState):
    for y in range(0,len(InitialState)):
        for x in range(0,len(InitialState[y])):
            ContadorVivos = 0
            for x1 in range((x-1),(x+2)):
                if x1 < 0 or x1 >= len(InitialState[y]):
                    x1 = 5
                    continue
                for y1 in range((y-1),(y+2)):
                    if y1 < 0 or y1 >= len(InitialState) or (x1 == x and y1 == y):
                        y1 = 5
                        continue
                    ContadorVivos += InitialState[y1][x1]
                    
            if InitialState[y][x] == 1:
                #Se muere por despoblacion o por sobrepoblacion
                if ContadorVivos < 2 or ContadorVivos > 3:
                    NewState[y][x] = 0
                #Se mantiene vivo
                elif ContadorVivos <= 3 and ContadorVivos >= 2:
                    NewState[y][x] = 1
                
            else:
                #Cobra vida por la reproduccion
                if ContadorVivos == 3:
                    NewState[y][x] = 1
        
    return NewState

def main(CurrentState):
    Render(CurrentState)

    while True:
        time.sleep(0.2)
        system("cls")
        state = DeadState(w,h)
        CurrentState = NextState(CurrentState,state)
        Render(CurrentState)
       
if __name__ == "__main__":
    print("Bienvenido, quieres simular El Juego de La Vida de Conway con valores al azar, o prefieres utilizar patrones preestablecidos.")
    while True:
        Decision = input("Escribe \"CONWAY\" si deseas simular la 1era opcion, o sino escribe \"PP\" para simular la 2da: ")
        if Decision.upper() == "CONWAY":
            h = int(input("Ingresa cuantas filas quiere que tenga: "))
            w = int(input("Ingresa cuantas columnas quiere que tenga: "))
            CurrentState = BoardState(w,h)
            break

        elif Decision.upper() == "PP":
            for i in listdir("WithTerminal\PatronesPreestablecidos"):
                print(str(i).replace(".txt",""))
            ChoosePP = input("Introduce el nombre del patron preestablecido que quieras simular de los que se encuentran anteriormente: ")
            CurrentState = FileReading(ChoosePP.capitalize())
            w = len(CurrentState[0])
            h = len(CurrentState)
            break
        else:
            print("Vuelve a intentarlo. Escribe tal cual esta escrita una de las 2 opciones que ofrecemos")

    main(CurrentState)
    
    