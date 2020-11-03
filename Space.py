import turtle
import os
import pygame

pygame.init()
keepPlaying = True

def main():

    joysticks = []
    clock = pygame.time.Clock()    
    FPS = 60

    for i in range(0,pygame.joystick.get_count()):
        joysticks.append(pygame.joystick.Joystick(i))
        joysticks[-1].init()
        print('Joystick detectado : ',joysticks[-1].get_name())
    
    
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
                    move_right()
                elif hat == (0,1):
                    print('Arriba')
                elif hat == (-1,0):
                    print('Izquierda')
                    move_left()
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
            axes = joysticks[-1].get_numaxes()
            for k in range(axes):
                axis = joysticks[-1].get_axis(k)
                #print(axis)

    #Set up the screen
    wn = turtle.Screen()
    wn.bgcolor("black")
    wn.title("Space Invaders")

    #Draw border
    border_pen = turtle.Turtle()
    border_pen.speed(0)
    border_pen.color("white")
    border_pen.penup()
    border_pen.setposition(-300,-300)
    border_pen.pensize(3)
    border_pen.pendown()

    for side in range(4):
        border_pen.fd(600)
        border_pen.lt(90)
    border_pen.hideturtle()

    #Create the player
    player = turtle.Turtle()
    player.setposition(0, -250)
    player.color("orange")
    player.shape("triangle")
    player.penup()
    player.speed(0)
    player.setheading(90)

    playerspeed = 15

    #Move L and R
    def move_left():
        x = player.xcor()
        x -= playerspeed
        if x < -280:
            x = -280
        player.setx(x)

    def move_right():
        x = player.xcor()
        x += playerspeed
        if x > 280:
            x = 280
        player.setx(x)

    
while keepPlaying:      
    main()
