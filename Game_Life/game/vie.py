from numpy.core.arrayprint import printoptions
import pygame 
import numpy as np


class grid():
    def __init__(self, screen):
        self.screen = screen
        self.column = 10
        self.row = 10 
        self.rows_height = self.screen.get_height()/self.row
        self.rows_witdh = self.screen.get_height()/self.column
        

    def draw(self):

        for i in range(1,self.row):
            # draw grid
            pygame.draw.line(self.screen ,(0,0,0), (0,self.rows_height*i), (self.screen.get_height(),self.rows_height*i), 1)
        for i in range(1,self.column):
            # draw grid
            pygame.draw.line(self.screen ,(0,0,0), (self.rows_witdh*i,0), (self.rows_witdh*i, self.screen.get_width()), 1)

    def fill_rect(self, col=0, row=0): 
        reX = self.rows_witdh*(col-1)
        reY = self.rows_height*(row-1)
        #print(col)
        #print(row)
        rectangle = pygame.Rect(reX,reY, self.screen.get_width()/self.column,self.screen.get_height()/self.row)
        self.screen.fill((0,0,0), rectangle) 
    
    def fill_grid(self, finit):
        for x in range(self.column):
            for y in range(self.row):
                if finit[y][x]:
                    self.fill_rect(x+1,y+1)



class jeu():
    def __init__(self, gridy):
        self.column = gridy.column
        self.row = gridy.row

    def the_game(self, finit):
        sinit = finit
        for x in range(self.column):
            for y in range(self.row):
                alive_neib = 0
                tets = 0
                val = finit[y][x]
                if x==5 and y = =5:
                    tets += 1
                    print(tets)
                try:
                    if finit[y-1][x-1]:
                        alive_neib += 1
                        if x==5 and y ==5:
                            print(alive_neib)
                            print(" A is alive ")
                        
                except:
                    pass
                try:
                    if finit[y-1][x]:
                        alive_neib += 1
                        if x==5 and y ==5:
                            print(alive_neib)
                            print(" B is alive ")
                        
                except:
                    pass
                try:
                    if finit[y-1][x+1]:
                        alive_neib += 1
                        if x==5 and y ==5:
                            print(alive_neib)
                            print(" C is alive ")
                        
                except:
                    pass
                try:
                    if finit[y][x-1]:
                        alive_neib += 1
                        if x==5 and y ==5:
                            print(alive_neib)
                            print(" D is alive" )
                       
                except:
                    pass
                try:
                    if finit[y][x+1]:
                        alive_neib += 1
                        if x==5 and y ==5:
                            print(alive_neib)
                            print(" F is alive")
                       
                except:
                    pass
                try:
                    if finit[y+1][x-1]:
                        alive_neib += 1
                        if x==5 and y ==5:
                            print(alive_neib)
                            print(" G is alive")
                        
                except:
                    pass
                try:
                    if finit[y+1][x]:
                        alive_neib += 1
                        if x==5 and y ==5:
                            print(alive_neib)
                            print(" H is alive")
                        
                except:
                    pass
                try:
                    if finit[y+1][x+1]:
                        alive_neib += 1
                        if x==5 and y ==5:
                            print(alive_neib)
                            print(" I is alive")
                        
                except:
                    pass

                pygame.time.wait(10)

                if val: #val
                    # print(" %d %d is OK " %(y,x))
                    if finit[5][5]:
                        print(alive_neib)
                    if alive_neib == 3 or alive_neib == 2:
                        print("gd2")
                        # sinit[y][x] = True
                        # Any live cell with two or three live neighbours survives.
                        
                    else:
                        sinit[y][x] = False
                        # All other live cells die in the next generation.

                else:
                    # print(" %d %d is dead " %(y,x))
                    if  alive_neib == 3:
                        sinit[y][x] = True
                        print(" %d %d is reborn" %(y,x))
                        #Any dead cell with three live neighbours becomes a live cell.

                        
                    
        return sinit
                




         

def foo(finit):
    print(np.where(finit == 0, 1, finit))
    pygame.init()

    # Set up the drawing window
    screen = pygame.display.set_mode([500, 500])
    

    gridy= grid(screen)
    algo = jeu(gridy)

    # Run until the user asks to quit
    running = True
    while running:
    # for i in range(1):
        screen.fill((255, 255, 255))

        # Did the user click the window close button?
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        gridy.draw()
        
        gridy.fill_grid(finit)


        pygame.display.flip()   

        finit =  algo.the_game(finit)
        pygame.time.wait(10)
        print(np.where(finit == 0, 1, finit))



    # Done! Time to quit.
    pygame.quit()



