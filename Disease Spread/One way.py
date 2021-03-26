import numpy as np
import pygame
pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode([500, 500])

def randompos(pos):
    x = np.random.normal()
    y = np.random.normal()
    return (pos[0] + x, pos[1] + y)

class simpBall:
    def __init__(self, pos):
        self.pos = pos
        self.col = (np.random.randint(0,256),
                    np.random.randint(0,256),
                    np.random.randint(0,256))
    def draw(self):
        pygame.draw.circle(screen, self.col, self.pos, 10, 0)

class velBall:
    def __init__(self,pos,vel):
        self.pos = pos
        self.vel = vel
        self.col = (np.random.randint(0,256),
                    np.random.randint(0,256),
                    np.random.randint(0,256))

        self.gamesize = (500,500)

    def update(self):

        x, y = self.pos
        dx, dy = self.vel
        newx = x + dx
        newy = y + dy

        if newx < 10: #left wall collision
            print('hit left wall')
        if newx > 490: #right wall collision
            print('hit right wall')
        if newy < 10: #top wall collision
            print('hit top wall')
        if newy > 490: #bottom wall collision
            print('hit bottom wall')

        self.pos = (newx, newy)
        
        
        pygame.draw.circle(screen, self.col, self.pos, 10, 0)

velBalls = [velBall((np.random.randint(100,401),np.random.randint(100,401)),
                    (10*np.random.normal(),10*np.random.normal()))
            for i in range(1)]
    
running = True
clock = pygame.time.Clock()
frame = 0
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with white
    screen.fill((255, 255, 255))

    for ball in velBalls:
        ball.update()
        print(ball.vel)

    
    pygame.display.flip()# Flip the display
    clock.tick(3)
    frame = frame + 1
    print('frame' , frame)


pygame.quit()
