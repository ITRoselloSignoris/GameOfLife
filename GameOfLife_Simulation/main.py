""" 
THE GAME OF LIFE SIMULATION ON THE TERMINAL
-------------------------------------------
This program displays a Game Of Life simulation on the terminal.
The user can choose between, a board state where he chooses the amount of rows and columns, and each cell has a randomized int value between 0 and 1, or
a board state loaded with a pre established pattern from a .txt file.
"""
import random
import time 
from os import system, listdir

PATRONES = listdir("GameOfLife_Simulation\PatronesPreestablecidos")

def BoardState(width,height):
    """ Construct a matrix with random state in each cell.
    
    Parameters
    ----------
    width: The amount of columns of the matrix
    height: The amount of rows of the matrix

    Returns
    -------
    A matrix of dimensions width x height where each cell has a randomized integer value between 1 or 0, both being included, eith equal probability.
    """
    ls = []
    for j in range(0,height):
        ls1 = []
        for k in range(0,width):
            ls1.append(random.randint(0,1))
        ls.append(ls1)
    return ls

def DeadState(width,height):
    """ It creates a matrix with dead states in each cell.
    
    Parameters
    ----------
    width: The amount of columns of the matrix 
    height: The amount of rows of the matrix
    
    Returns
    -------
    A matrix of dimensions width x height where each cell has a dead state (0).
    """
    return [[0 for i in range(width)]for j in range(height)]

def FileReading(Choice):
    """ Loads a Board State from the given filepath. 
    
    Parameters
    ----------
    Choice: The file name of the pre established pattern
    
    Returns
    -------
    A board state loaded from the given filepath.
    """
    with open(f"GameOfLife_Simulation\PatronesPreestablecidos\{Choice}.txt", "r") as File:
        lines = [l.rstrip() for l in File.readlines()]

    height = len(lines)
    width = len(lines[0])
    board = DeadState(width, height)

    for x, line in enumerate(lines):
        for y, char in enumerate(line):
            board[x][y] = int(char)

    return board

def Render(Matriz):
    """ It displays the Board State given by printing it to the terminal.
    
    Parameters
    ----------
    Matriz: A Board state
    
    Returns
    -------
    It returns nothing - It is a display function.
    """
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
    """ If needed, it changes each cell value from the NewState board, following the rules and logic established by the Game Of Life.
    
    Parameters
    ----------
    InitialState: The Current Board state
    NewState: The New Board state
    
    Returns
    -------
    The new state of the board.
    """
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
    """ It runs the Game of Life forever, starting from the initial state. 
    
    Parameters
    ----------
    CurrentState: The Current Board state
    
    Returns
    -------
    It returns nothing -- To stop it, it needs to be forcibly exited.
    """
    Render(CurrentState)

    while True:
        time.sleep(0.2)
        system("cls")
        state = DeadState(w,h)
        CurrentState = NextState(CurrentState,state)
        Render(CurrentState)
         
if __name__ == "__main__":
    """It asks the user to choose between a randomly board state, or a board state with a pre established pattern.
    """

    print("Bienvenido, quieres simular El Juego de La Vida de Conway con valores al azar, o prefieres utilizar patrones preestablecidos.")
    while True:
        Decision = input("Escribe \"CONWAY\" si deseas simular la 1era opcion, o sino escribe \"PP\" para simular la 2da: ")
        if Decision.upper() == "CONWAY":
            h = int(input("Ingresa cuantas filas quiere que tenga: "))
            w = int(input("Ingresa cuantas columnas quiere que tenga: "))
            Initial_State = BoardState(w,h)
            break

        elif Decision.upper() == "PP":
            for i in PATRONES:
                print(str(i).replace(".txt",""))
            while True:
                ChoosePP = input("Introduce el nombre del patron preestablecido que quieras simular de los que se encuentran arriba: ")
                try:
                    PATRONES.index(f"{ChoosePP.capitalize()}" + ".txt")
                except ValueError:
                    print("Ese nombre no coincide con ninguno de los patrones preestablecidos. Vuelve a intentarlo")
                else:
                    break
                
            Initial_State = FileReading(ChoosePP.capitalize())
            w = len(Initial_State[0])
            h = len(Initial_State)
            break
        else:
            print("Vuelve a intentarlo. Escribe tal cual esta escrita una de las 2 opciones que ofrecemos")

    main(Initial_State)
    
    