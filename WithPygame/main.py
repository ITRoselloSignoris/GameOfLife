import random
import numpy as np
import time
import pygame

CELLS_ALIVE = (255,255,255)
DYING_CELLS = (169,169,169)
COLOR_BG = (0,0,0)
COLOR_GRID = (50,50,50)

REFFRACTORY_CELL = (255,0,0)
FIRING_CELL = CELLS_ALIVE

def ConwayGoL(screen, cell, size, progress = False):
    updated_cells = np.zeros((cell.shape[0],cell.shape[1]))

    for row,col in np.ndindex(cell.shape):
        alive = np.sum(cell[row-1:row+2,col-1:col+2]) - cell[row,col]
        color = COLOR_BG if cell[row,col] == 0 else CELLS_ALIVE

        if cell[row,col] == 1:
            if alive > 3 or alive < 2:
                if progress:
                    color = DYING_CELLS
            elif 2 <= alive <= 3:
                updated_cells[row,col] = 1
                if progress:
                    color = CELLS_ALIVE
        else:
            if alive == 3:
                updated_cells[row,col] = 1
                if progress:
                    color = CELLS_ALIVE

        pygame.draw.rect(screen, color, (col * size, row * size, size - 1, size - 1))
    
    return  updated_cells

def DayAndNight(screen, cell, size, progress = False):
    updated_cells = np.zeros((cell.shape[0],cell.shape[1]))

    for row,col in np.ndindex(cell.shape):
        alive = np.sum(cell[row-1:row+2,col-1:col+2]) - cell[row,col]
        color = COLOR_BG if cell[row,col] == 0 else CELLS_ALIVE

        if cell[row,col] == 1:
            if alive < 3 or (alive == 4 or alive == 5):
                if progress:
                    color = DYING_CELLS
            elif alive >= 6 or alive == 3:
                updated_cells[row,col] = 1
                if progress:
                    color = CELLS_ALIVE
        else:
            if alive >= 3 and alive != 5:
                updated_cells[row,col] = 1
                if progress:
                    color = CELLS_ALIVE

        pygame.draw.rect(screen, color, (col * size, row * size, size - 1, size - 1))
    
    return  updated_cells

def Brian_Brain(screen, cell, size, progress = False):
    updated_cells = np.zeros((cell.shape[0],cell.shape[1]))
    
    for row,col in np.ndindex(cell.shape):
        alive = np.nansum(cell[row-1:row+2,col-1:col+2]) - cell[row,col]
        color = COLOR_BG if cell[row,col] == 0 else (CELLS_ALIVE if cell[row,col] == 1 else REFFRACTORY_CELL)

        if cell[row,col] == 1:
            updated_cells[row,col] = None
            if progress:
                color = REFFRACTORY_CELL

        elif cell[row, col] == None:
            updated_cells[row,col] = 0
            if progress:
                color = DYING_CELLS

        else:
            if alive == 2:
                updated_cells[row,col] = 1
                if progress:
                    color = CELLS_ALIVE
                    
        pygame.draw.rect(screen, color, (col * size, row * size, size - 1, size - 1))
    return  updated_cells

def Choice(Decision, screen, cell, size, progress = False):
    if Decision.upper() == "DAN":
        return DayAndNight(screen, cell, size, progress)
    elif Decision.upper() == "CGL":
        return ConwayGoL(screen, cell, size, progress)
    elif Decision.upper() == "BB":
        return Brian_Brain(screen, cell, size, progress)

def main():
    print("Welcome, pick a one Cellular Automaton between these four to simulate. Write your desicion as indicates the parentheses of each.")
    Desicion = input("Conway`s Game Of Life (\"CGL\"), Day And Night (\"DAN\"), Brian`s Brain (\"BB\") o Langton`s Ant(\"LA\"): ") 
    RoundBB = 0
    pygame.init()
    screen = pygame.display.set_mode((800,600))
    
    cell = np.zeros((60,80))
    screen.fill(COLOR_GRID)
    Choice(Desicion, screen, cell, 10)

    pygame.display.flip()
    pygame.display.update()

    running = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE: 
                    running = not running
                    Choice(Desicion, screen, cell, 10)
                    pygame.display.update()

                if event.key == pygame.K_RETURN:
                    n = 0
                    while True:
                        pos = ((random.randint(0,799)),(random.randint(0,599)))
                        cell[pos[1]//10,pos[0]//10] = 1
                        Choice(Desicion, screen, cell, 10)
                        pygame.display.update()
                        n += 1
                        if n == 1200:
                            break

                    

            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                cell[pos[1]//10,pos[0]//10] = 1
                Choice(Desicion, screen, cell, 10)
                pygame.display.update()

            if pygame.mouse.get_pressed()[2] and Desicion.upper() == "BB":
                pos = pygame.mouse.get_pos()
                cell[pos[1]//10,pos[0]//10] = None
                Choice(Desicion, screen, cell, 10)
                pygame.display.update()

        screen.fill(COLOR_GRID)

        if running:
            cell = Choice(Desicion, screen, cell, 10, progress = True)
            pygame.display.update()
        time.sleep(0.001)

if __name__ == "__main__":
    main()