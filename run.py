import pygame
import sys
import modules.settings as settings
import modules.data_base as data_base
pygame.init()

screen = pygame.display.set_mode((600, 600))
win = False

game = True
def blit_cell(cell, x, y):
    if data_base.list_cells[cell] == 1:
        cross = settings.Settings(x = x, y = y, name = "cross.png", width = 150, height= 150)
        cross.load_image()
        cross.blit_sprite(screen= screen)
    if data_base.list_cells[cell] == 2:
        zero = settings.Settings(x = x, y = y, name = "zero.png", width = 150, height = 150)
        zero.load_image()
        zero.blit_sprite(screen= screen)
def check_win(cell, cell1, cell2 , x1, x2, y1, y2):
    global win
    if data_base.list_cells[cell] == 1 and data_base.list_cells[cell1] == 1 and data_base.list_cells[cell2] == 1:
        pygame.draw.line(screen, "red", (x1, y1), (x2, y2), width= 5)
        win = True 
    if data_base.list_cells[cell] == 2 and data_base.list_cells[cell1] == 2 and data_base.list_cells[cell2] == 2:
        pygame.draw.line(screen, "red", (x1, y1), (x2, y2), width= 5)
        win = True 

    return win

def run_game():
    global win
    while game:
        background = settings.Settings(x = 0, y = 0, name = "background.png", width = 600, height = 600)
        background.load_image()
        background.blit_sprite(screen= screen)
        blit_cell(0, 50, 50)
        blit_cell(1, 225, 50)
        blit_cell(2, 395, 50)
        blit_cell(3, 50, 225)
        blit_cell(4, 225, 225)
        blit_cell(5, 395, 225)
        blit_cell(6, 50, 395)
        blit_cell(7, 225, 395)
        blit_cell(8, 395, 395)
        check_win(0, 1, 2, 125, 475, 125, 125)
        check_win(0, 3, 6, 125, 125, 125, 475)
        check_win(0, 4, 8, 125, 475, 125, 475)
        check_win(6, 7, 8, 125, 475, 475, 475)
        check_win(6, 4, 2, 125, 475, 475, 125)
        check_win(8, 5, 2, 475, 475, 475, 125)
        for event in pygame.event.get():
            

            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                print(f"{mouse_pos}")
                if win == False:
                    if 200 > mouse_pos[0] > 50 and 200 > mouse_pos[1] > 50 and data_base.list_choice[0] == 1 and data_base.list_cells[0] == 0:
                        data_base.list_cells[0] = 1
                        data_base.list_choice[0] = 2


                    if 200 > mouse_pos[0] > 50 and 200 > mouse_pos[1] > 50 and data_base.list_choice[0] == 2 and data_base.list_cells[0] == 0:  
                        data_base.list_cells[0] = 2
                        data_base.list_choice[0] = 1                      

                    if 375 > mouse_pos[0] > 225 and 200 > mouse_pos[1] > 50 and data_base.list_choice[0] == 1 and data_base.list_cells[1] == 0:
                        data_base.list_cells[1] = 1
                        data_base.list_choice[0] = 2

                    if 375 > mouse_pos[0] > 225 and 200 > mouse_pos[1] > 50 and data_base.list_choice[0] == 2 and data_base.list_cells[1] == 0:
                        data_base.list_cells[1] = 2
                        data_base.list_choice[0] = 1     
                    
                    if 550 > mouse_pos[0] > 395 and 200 > mouse_pos[1] > 50 :

                        if data_base.list_choice[0] == 1 and data_base.list_cells[2] == 0:
                            data_base.list_cells[2] = 1
                            data_base.list_choice[0] = 2

                        if data_base.list_choice[0] == 2 and data_base.list_cells[2] == 0:
                            data_base.list_cells[2] = 2
                            data_base.list_choice[0] = 1

                    if 200 > mouse_pos[0] > 50 and 375 > mouse_pos[1] > 225:

                        if data_base.list_choice[0] == 1 and data_base.list_cells[3] == 0:
                            data_base.list_cells[3] = 1
                            data_base.list_choice[0] = 2

                        if data_base.list_choice[0] == 2 and data_base.list_cells[3] == 0:
                            data_base.list_cells[3] = 2
                            data_base.list_choice[0] = 1

                    if 550 > mouse_pos[0] > 395 and 375 > mouse_pos[1] > 225:

                        if data_base.list_choice[0] == 1 and data_base.list_cells[5] == 0:
                            data_base.list_cells[5] = 1
                            data_base.list_choice[0] = 2


                        if data_base.list_choice[0] == 2 and data_base.list_cells[5] == 0:
                            data_base.list_cells[5] = 2
                            data_base.list_choice[0] = 1

                    if 375 > mouse_pos[0] > 225 and 375 > mouse_pos[1] > 225:

                        if data_base.list_choice[0] == 1 and data_base.list_cells[4] == 0:
                            data_base.list_cells[4] = 1
                            data_base.list_choice[0] = 2


                        if data_base.list_choice[0] == 2 and data_base.list_cells[4] == 0:
                            data_base.list_cells[4] = 2
                            data_base.list_choice[0] = 1

                    if 200 > mouse_pos[0] > 50 and 550 > mouse_pos[1] > 395:

                        if data_base.list_choice[0] == 1 and data_base.list_cells[6] == 0:
                            data_base.list_cells[6] = data_base.list_choice[0]
                            data_base.list_choice[0] = 2

                        if data_base.list_choice[0] == 2 and data_base.list_cells[6] == 0:
                            data_base.list_cells[6] = data_base.list_choice[0]
                            data_base.list_choice[0] = 1

                    if 375 > mouse_pos[0] > 225 and 550 > mouse_pos[1] > 395:

                        if data_base.list_choice[0] == 1 and data_base.list_cells[7] == 0:
                            data_base.list_cells[7] = data_base.list_choice[0]
                            data_base.list_choice[0] = 2

                        if data_base.list_choice[0] == 2 and data_base.list_cells[7] == 0:
                            data_base.list_cells[7] = data_base.list_choice[0]
                            data_base.list_choice[0] = 1

                    if 550 > mouse_pos[0] > 395 and 550 > mouse_pos[1] > 395:

                        if data_base.list_choice[0] == 1 and data_base.list_cells[8] == 0:
                            data_base.list_cells[8] = data_base.list_choice[0]
                            data_base.list_choice[0] = 2

                        if data_base.list_choice[0] == 2 and data_base.list_cells[8] == 0:
                            data_base.list_cells[8] = data_base.list_choice[0]
                            data_base.list_choice[0] = 1
        pygame.display.update()