import pygame
import sys
import random
import math

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
BALL_RADIUS = 20
NUM_BALLS = 10
GRAVITY = 0.5
FRICTION = -0.8
BALL_COLOR = (255, 0, 0)
BACKGROUND_COLOR = (0, 0, 0)

# Set up display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Multiple Bouncing Balls Simulation")

class Ball:
    def __init__(self, x, y, dx, dy):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy

    def move(self):
        self.dy += GRAVITY
        self.x += self.dx
        self.y += self.dy

        # Bounce off walls
        if self.x - BALL_RADIUS < 0 or self.x + BALL_RADIUS > WIDTH:
            self.dx *= FRICTION
            self.x = max(BALL_RADIUS, min(WIDTH - BALL_RADIUS, self.x))

        if self.y - BALL_RADIUS < 0 or self.y + BALL_RADIUS > HEIGHT:
            self.dy *= FRICTION
            self.y = max(BALL_RADIUS, min(HEIGHT - BALL_RADIUS, self.y))

    def draw(self, surface):
        pygame.draw.circle(surface, BALL_COLOR, (int(self.x), int(self.y)), BALL_RADIUS)

def check_collision(ball1, ball2):
    dx = ball1.x - ball2.x
    dy = ball1.y - ball2.y
    distance = math.sqrt(dx**2 + dy**2)

    if distance < 2 * BALL_RADIUS:
        # Reflect velocities
        angle = math.atan2(dy, dx)
        speed1 = math.sqrt(ball1.dx**2 + ball1.dy**2)
        speed2 = math.sqrt(ball2.dx**2 + ball2.dy**2)
        ball1.dx = speed2 * math.cos(angle)
        ball1.dy = speed2 * math.sin(angle)
        ball2.dx = speed1 * math.cos(angle + math.pi)
        ball2.dy = speed1 * math.sin(angle + math.pi)

def main():
    balls = []
    for _ in range(NUM_BALLS):
        x = random.randint(BALL_RADIUS, WIDTH - BALL_RADIUS)
        y = random.randint(BALL_RADIUS, HEIGHT - BALL_RADIUS)
        dx = random.uniform(-2, 2)
        dy = random.uniform(-2, 2)
        balls.append(Ball(x, y, dx, dy))

    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(BACKGROUND_COLOR)

        for i in range(NUM_BALLS):
            balls[i].move()
            balls[i].draw(screen)
            for j in range(i + 1, NUM_BALLS):
                check_collision(balls[i], balls[j])

        pygame.display.flip()
        clock.tick(60)

if __name__ == '__main__':
    main()
