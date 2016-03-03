import pygame, sys
import functions
import globalvars
from pygame.locals import *
from functions import *


def main():

    print "Hello"
    
    pygame.init()
    globalvars.screen
    globalvars.background
    pygame.display.set_caption('Army Project')



    "Main loop"
    while True:
        globalvars.screen.blit(globalvars.background, (0,0))
        globalvars.screen.blit(globalvars.redhome, (75,50))
        
        pygame.display.update()
        pygame.event.wait()
        
if __name__ == '__main__':
    main()
    
                        




                        






    
