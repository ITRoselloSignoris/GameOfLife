"""
CELLULAR AUTOMATON FUNCTION PACKAGE
-----------------------------------
This file contains each Cellular Automaton function and variables.

"""
import numpy as np
import pygame

#Each variable contains a tuple with 3 elements
#Following the RGB composition, you assign a value to each element of the tuple.
#Each element could go from 0 to 255
CELLS_ALIVE = (255,255,255)
DYING_CELLS = (169,169,169)
COLOR_BG = (0,0,0)
COLOR_GRID = (50,50,50)
REFFRACTORY_CELL = (255,0,0)
FIRING_CELL = CELLS_ALIVE
ANT = (0,255,0)

NORTH = (0, -1) 
SOUTH = (0, 1)
EAST = (1, 0)
WEST = (-1, 0)
DIRECTIONS = [NORTH, EAST, SOUTH, WEST]

def ConwayGoL(screen, cell, size, progress = False): 
    """ Take a single step in Conway`s Game of Life and renders each cell state.
    
    Parameters
    ----------
    screen: The surface of the Pygame windowed screen
    cell: The current state of the game board
    size: The size of each cell, size * size
    progress: It indicates whether the simulation is paused or not. If False, the simulation is paused
    
    Returns
    -------
    It returns the updated state of the game board, following the rules and logic established in Conway`s Game of Life.
    """

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
    """ Take a single step in  Conway`s Game of Life and renders each cell state.
    
    Parameters
    ----------
    screen: The surface of the Pygame windowed screen
    cell: The current state of the game board
    size: The size of each cell, size * size
    progress: It indicates whether the simulation is paused or not. If False, the simulation is paused
    
    Returns
    -------
    It returns the updated state of the game board, following the rules and logic established in Day and Night.
    """
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
    """ Take a single step in Brian`s Brain and renders each cell state.
    
    Parameters
    ----------
    screen: The surface of the Pygame windowed screen
    cell: The current state of the game board
    size: The size of each cell, size * size
    progress: It indicates whether the simulation is paused or not. If False, the simulation is paused
    
    Returns
    -------
    It returns the updated state of the game board, following the rules and logic established in Brian`s Brain.
    """
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


#DOES NOT WORK ---FIX---
"""def Langton_Ant(screen, cell, size, direction, posx, posy, progress = False):
    updated_cells = np.zeros((cell.shape[0],cell.shape[1]))
    ant_cell = np.zeros((cell.shape[0],cell.shape[1]))
    for row,col in np.ndindex(cell.shape):
        color = COLOR_BG if cell[row,col] == 0 else (CELLS_ALIVE if cell[row,col] == 1 else ANT)
        print(row)
        print(col)
        if row == 1 and col == 1:
            ant_cell[row,col] = None
        if ant_cell[row,col] == None:
            print("FF")
            if cell[row,col] == 1:
                updated_cells[row,col] = 0
                direction = DIRECTIONS[direction+1]
                if progress:
                    color = DYING_CELLS
            else:
                updated_cells[row,col] = 1
                direction = DIRECTIONS[direction-1]
                if progress:
                    color = ANT
            updated_cells[posx + direction[0], posy + direction[1]] = None

        pygame.draw.rect(screen, color, (col * size, row * size, size - 1, size - 1))
    return  updated_cells
"""