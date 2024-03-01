from FunctionPackage import Functions
import time
import random

def Choice(Decision, screen, cell, size,  progress = False, Posx = 1, Posy = 1, Direction = 0):
    while True:
        if Decision.upper() == "DAN":
            return Functions.DayAndNight(screen, cell, size, progress)
        elif Decision.upper() == "CGL":
            return Functions.ConwayGoL(screen, cell, size, progress)
        elif Decision.upper() == "BB":
            return Functions.Brian_Brain(screen, cell, size, progress)
        elif Decision.upper() == "LA":
            return Functions.Langton_Ant(screen, cell, size, Direction, Posx, Posy, progress)

def main():
    print("Welcome, pick a one Cellular Automaton between these four to simulate. Write your desicion as indicates the parentheses of each.")
    while True:
        Desicion = input("Conway`s Game Of Life (\"CGL\"), Day And Night (\"DAN\"), Brian`s Brain (\"BB\") o Langton`s Ant(\"LA\"): ")
        if Desicion.upper() != "DAN" and Desicion.upper() != "CGL" and Desicion.upper() != "LA" and Desicion.upper() != "BB":
            print("La opcion que acabas de introducir no corresponde a ninguna de las opciones disponibles.\nVuelve a intentarlo")
        else:
            break
    Functions.pygame.init()
    screen = Functions.pygame.display.set_mode((800,600))
    
    cell = Functions.np.zeros((60,80))
    screen.fill(Functions.COLOR_GRID)
    Choice(Desicion, screen, cell, 10)

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
                    Choice(Desicion, screen, cell, 10)
                    Functions.pygame.display.update()

                if event.key == Functions.pygame.K_RETURN:
                    n = 0
                    while True:
                        pos = ((random.randint(0,799)),(random.randint(0,599)))
                        cell[pos[1]//10,pos[0]//10] = 1
                        Choice(Desicion, screen, cell, 10)
                        Functions.pygame.display.update()
                        n += 1
                        if n == 1200:
                            break

            if Functions.pygame.mouse.get_pressed()[0]:
                pos = Functions.pygame.mouse.get_pos()
                cell[pos[1]//10,pos[0]//10] = 1
                Choice(Desicion, screen, cell, 10)
                Functions.pygame.display.update()

            if Functions.pygame.mouse.get_pressed()[2] and Desicion.upper() == "BB":
                pos = Functions.pygame.mouse.get_pos()
                cell[pos[1]//10,pos[0]//10] = None
                Choice(Desicion, screen, cell, 10)
                Functions.pygame.display.update()

        screen.fill(Functions.COLOR_GRID)

        if running:
            cell = Choice(Desicion, screen, cell, 10, progress = True)
            Functions.pygame.display.update()
        time.sleep(0.001)

if __name__ == "__main__":
    main()