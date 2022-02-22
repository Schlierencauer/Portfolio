import pygame, sys
pygame.init()

def main():
    clock = pygame.time.Clock()

    pygame.display.set_caption('Gierka No.1')
    icon = pygame.image.load('sandwich.jpg')
    pygame.display.set_icon(icon)

    #pygame.mixer.music.load(r'C:\Users\Slezi\Desktop\Git\Pygame\COMBAT02.MP3')
    #pygame.mixer.music.play(-1)

    size = width, height = (800, 600)
    screen = pygame.display.set_mode(size)

    speed = [10, 100]
    acc = [0, 9.81]

    image = pygame.image.load(r'po nocce.jpg')
    image = pygame.transform.scale(image, size)

    surface_center = (
        (width-image.get_width())/2,
        (height-image.get_height())/2
    )

    screen.blit(image, surface_center)
    ball = pygame.image.load('atom.png')
    ball = pygame.transform.scale(ball, (ball.get_width()//2,
                                         ball.get_height()//2))
    screen.blit(ball, (width/2, height/2))
    ballrect = ball.get_rect(center = (width/2 ,height/2))
    pygame.display.flip()

    while True:
        clock.tick(60)
        print(clock.get_fps())
        pygame.time.delay(50)

        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
                sys.exit()

        speed[1] = speed[1] + acc[1]*1

        ballrect = ballrect.move(speed)
        if ballrect.left < 0 or ballrect.right > width:
            speed[0] = -speed[0]
        if ballrect.top < 0 or ballrect.bottom > height:
            speed[1] = -speed[1]

        screen.blit(image, surface_center)
        screen.blit(ball, ballrect)
        pygame.display.flip()
if __name__ == '__main__':
    main()
    pygame.quit()
    sys.exit()