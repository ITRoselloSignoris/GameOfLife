import random
import numpy as np
import time
import pygame

CELLS_ALIVE = (255,255,255)
DYING_CELLS = (169,169,169)
COLOR_BG = (0,0,0)
COLOR_GRID = (50,50,50)

def Update(screen, cell, size, progress = False):
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
                    color = DYING_CELLS

        pygame.draw.rect(screen, color, (col * size, row * size, size - 1, size - 1))
    
    return  updated_cells



def main():
    pygame.init()
    screen = pygame.display.set_mode((800,600))

    cell = np.zeros((60,80))
    screen.fill(COLOR_GRID)
    Update(screen, cell, 10)

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
                    Update(screen, cell, 10)
                    pygame.display.update()

                if event.key == pygame.K_RETURN:
                    n = 0
                    while True:
                        pos = ((random.randint(0,799)),(random.randint(0,599)))
                        cell[pos[1]//10,pos[0]//10] = 1
                        Update(screen, cell, 10)
                        pygame.display.update()
                        n += 1
                        if n == 1200:
                            break

                    

            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                cell[pos[1]//10,pos[0]//10] = 1
                Update(screen, cell, 10)
                pygame.display.update()

        screen.fill(COLOR_GRID)

        if running:
            cell = Update(screen,cell,10, progress = True)
            pygame.display.update()
        time.sleep(0.001)

if __name__ == "__main__":
    main()