"""
CELLULAR AUTOMATON SIMULATION WITH PYGAME AND NUMPY
---------------------------------------------------
This program uses Pygame and Numpy modules (Which are imported from the FunctionPackage), to simulate different Cellular Automatons. 
The user can choose up to 3 different Cellular Automatons. 
Also, they can pause the simulation when they press the Spacebar or change a cell state when they press Left CLick on it.
"""
from FunctionPackage import Functions
import time
import random

def Choice(Decision, screen, cell, size,  progress = False):
    """ It calls the function of the Cellular Automaton chosen by the user, and returns its value.
    
    Parameters
    ----------
    Decision: The chosen Cellular Automaton code
    screen: The surface of the Pygame windowed screen
    cell: The current state of the game board
    size: The size of each cell, size * size
    progress: It indicates whether the simulation is paused or not. If False, the simulation is paused
    
    Returns
    -------
    It returns the next state of the game board, according to rules and logic of the Cellular Automaton chosen
    """
    while True:
        if Decision.upper() == "DAN":
            return Functions.DayAndNight(screen, cell, size, progress)
        elif Decision.upper() == "CGL":
            return Functions.ConwayGoL(screen, cell, size, progress)
        elif Decision.upper() == "BB":
            return Functions.Brian_Brain(screen, cell, size, progress)
        elif Decision.upper() == "LA":
            return Functions.Langton_Ant(screen, cell, size, progress)

def main():
    """ It configures the surface of the simulation windowed screen, the pygame events such as the possibiliy of 
    modifying the functionality of the simulation when different keys are being pressed and last but not least, it 
    runs the Cellular Automaton forever.
    
    Parameters
    ----------
    This function does not have parameters
    
    Returns
    -------
    This function never returns - To stop it, the program must be forcibly exited.
    """

    print("Welcome, pick a one Cellular Automaton between these four to simulate. Write your desicion as indicates the parentheses of each.")
    while True:
        Decision = input("Conway`s Game Of Life (\"CGL\"), Day And Night (\"DAN\"), Brian`s Brain (\"BB\") o Langton`s Ant(\"LA\"): ")
        if Decision.upper() != "DAN" and Decision.upper() != "CGL" and Decision.upper() != "LA" and Decision.upper() != "BB":
            print("La opcion que acabas de introducir no corresponde a ninguna de las opciones disponibles.\nVuelve a intentarlo")
        else:
            break
    Functions.pygame.init()
    screen = Functions.pygame.display.set_mode((800,600))
    
    cell = Functions.np.zeros((60,80))
    screen.fill(Functions.COLOR_GRID)
    Choice(Decision, screen, cell, 10)

    Functions.pygame.display.flip()
    Functions.pygame.display.update()

    running = False

    while True:
        for event in Functions.pygame.event.get():
            if event.type == Functions.pygame.QUIT:
                Functions.pygame.quit()
                return
            
            elif event.type == Functions.pygame.KEYDOWN:
                if event.key == Functions.pygame.K_SPACE: 
                    running = not running
                    Choice(Decision, screen, cell, 10)
                    Functions.pygame.display.update()

                if event.key == Functions.pygame.K_RETURN:
                    n = 0
                    while True:
                        pos = ((random.randint(0,799)),(random.randint(0,599)))
                        cell[pos[1]//10,pos[0]//10] = 1
                        Choice(Decision, screen, cell, 10)
                        Functions.pygame.display.update()
                        n += 1
                        if n == 1200:
                            break

            if Functions.pygame.mouse.get_pressed()[0]:
                pos = Functions.pygame.mouse.get_pos()
                cell[pos[1]//10,pos[0]//10] = 1
                Choice(Decision, screen, cell, 10)
                Functions.pygame.display.update()

            if Functions.pygame.mouse.get_pressed()[2] and Decision.upper() == "BB":
                pos = Functions.pygame.mouse.get_pos()
                cell[pos[1]//10,pos[0]//10] = None
                Choice(Decision, screen, cell, 10)
                Functions.pygame.display.update()

        screen.fill(Functions.COLOR_GRID)

        if running:
            cell = Choice(Decision, screen, cell, 10, progress = True)
            Functions.pygame.display.update()
        time.sleep(0.001)

if __name__ == "__main__":
    main()