"""
import pygame
pygame.init()

def main(): 
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Joystick Testing / XBOX360 Controller")

    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((255, 255, 255))

    joysticks = []
    clock = pygame.time.Clock()
    keepPlaying = True

    for i in range(0, pygame.joystick.get_count()):
        joysticks.append(pygame.joystick.Joystick(i))
        joysticks[-1].init()
        print("Detected joystick ", joysticks[-1].get_name(), " ")

    while keepPlaying:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                print("Keydown,", event.key)

            elif event.type == pygame.KEYUP:
                print("Keyup,", event.key)

            elif event.type == pygame.JOYAXISMOTION:
                print("Joystick '",joysticks[event.joy].get_name(),"' axis",event.axis,"motion.")


            elif event.type == pygame.JOYBUTTONDOWN:
                print("Joystick '",joysticks[event.joy].get_name(),"' button",event.button,"down.")

                if event.button == 0:
                    background.fill((255, 0, 0))

                elif event.button == 1:
                    background.fill((0, 0, 255))

            elif event.type == pygame.JOYBUTTONUP:
                print("Joystick '",joysticks[event.joy].get_name(),"' button",event.button,"up.")
                if event.button == 0:
                    background.fill((255, 255, 255))
                elif event.button == 1:
                    background.fill((255, 255, 255))

            elif event.type == pygame.JOYHATMOTION:
                print("Joystick '",joysticks[event.joy].get_name(),"' hat",event.hat," moved.")
                    
        screen.blit(background, (0, 0))
        pygame.display.flip()

main()
pygame.quit()
"""
"""
 l_X = joysticks[-1].get_axis(0)
            l_Y = joysticks[-1].get_axis(1)
            r_X = joysticks[-1].get_axis(3)
            r_Y = joysticks[-1].get_axis(4)
            t_L = joysticks[-1].get_axis(2)
            t_R = joysticks[-1].get_axis(5)

            if l_X:
                print(l_X)               
            elif l_Y:
                print(l_Y)                
            elif r_X:
                print(r_X)                
            elif r_Y:
                print(r_Y)                
            elif t_L:
                print(t_L)                
            elif t_R:
                print(t_R)                    
"""

import pygame 

pygame.init()

joysticks = []

clock = pygame.time.Clock()
keepPlaying = True

FPS = 60

for i in range(0,pygame.joystick.get_count()):
    joysticks.append(pygame.joystick.Joystick(i))
    joysticks[-1].init()
    print('Joystick detectado : ',joysticks[-1].get_name())

print('Nivel de bateria: ', joysticks[-1].get_power_level())

while keepPlaying:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.JOYBUTTONDOWN:
                if event.button == 0:
                    print('Boton A')
                elif event.button == 1:
                    print('Boton B')
                elif event.button == 2:
                    print('Boton X')
                elif event.button == 3:
                    print('Boton Y')
                elif event.button == 4:
                    print('Boton LB')
                elif event.button == 5:
                    print('Boton RB')
                elif event.button == 6:
                    print('Menu Izquierda')
                elif event.button == 7:
                    print('Menu Derecha')
                elif event.button == 8:
                    print('Boton L3')
                elif event.button == 9:
                    print('Boton R3')
                elif event.button == 10:
                    print('HOME')
    
        elif event.type == pygame.JOYHATMOTION:
            for i in range(joysticks[-1].get_numhats()):
                hat = joysticks[-1].get_hat(i)
                if hat == (1,0):
                    print('Derecha')
                elif hat == (0,1):
                    print('Arriba')
                elif hat == (-1,0):
                    print('Izquierda')
                elif hat == (0,-1):
                    print('Abajo')
                elif hat == (1,1):
                    print('Arriba & Derecha')
                elif hat == (-1,1):
                    print('Arriba & Izquierda')
                elif hat == (1,-1):
                    print('Abajo & Derecha')
                elif hat == (-1,-1):
                    print('Abajo & Izquierda') 

        elif event.type == pygame.JOYAXISMOTION:
            #axes = joysticks[-1].get_numaxes()
            #for k in range(axes):
            axis = joysticks[-1].get_axis(2)
            print('%1.2f'%axis)

