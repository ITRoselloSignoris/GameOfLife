import random
import time 
from os import system

#Creacion de la matriz y asignacion de valores
def BoardState(width,height):
    ls = []
    for j in range(0,height):
        ls1 = []
        for k in range(0,width):
            ls1.append(random.randint(0,1))
        ls.append(ls1)
    return ls

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
                    continue
                for y1 in range((y-1),(y+2)):
                    if y1 < 0 or y1 >= len(InitialState) or (x1 == x and y1 == y):
                        continue
                    ContadorVivos += InitialState[y1][x1]

            #Se muere por despoblacion
            if ContadorVivos <= 1 and InitialState[y][x] == 1:
                NewState[y][x] = 0

            #Se muere por sobrepoblacion
            if ContadorVivos > 3 and InitialState[y][x] == 1:
                NewState[y][x] = 0

            #Cobra vida por la reproduccion
            if ContadorVivos == 3 and InitialState[y][x] == 0:
                NewState[y][x] = 1
        
    return NewState



def main():
    print("Bienvenido al Juego de la Vida de Conway")
    h = int(input("Ingresa cuantas filas quiere que tenga: "))
    w = int(input("Ingresa cuantas columnas quiere que tenga: "))
    CurrentState = BoardState(w,h)
    Render(CurrentState)
    NewState = CurrentState
    while True:
        system("cls")
        Render(NextState(CurrentState,NewState))
        CurrentState = NewState
        time.sleep(0.001)
        
if __name__ == "__main__":
    main()
    
    