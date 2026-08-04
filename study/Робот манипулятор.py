import pygame
import numpy as np

# Параметры окна
WINDOW_WIDTH, WINDOW_HEIGHT = 800, 600

# Цвета
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Длина сегментов манипулятора
ARM_LENGTH1 = 150
ARM_LENGTH2 = 100

pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Robot Arm Simulation")

clock = pygame.time.Clock()


def forward_kinematics(theta1, theta2):
    x1 = ARM_LENGTH1 * np.cos(theta1)
    y1 = ARM_LENGTH1 * np.sin(theta1)
    x2 = x1 + ARM_LENGTH2 * np.cos(theta1 + theta2)
    y2 = y1 + ARM_LENGTH2 * np.sin(theta1 + theta2)
    return (x1, y1), (x2, y2)


def main():
    running = True
    theta1 = np.pi / 4
    theta2 = np.pi / 4

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            theta1 -= 0.01
        if keys[pygame.K_RIGHT]:
            theta1 += 0.01
        if keys[pygame.K_UP]:
            theta2 += 0.01
        if keys[pygame.K_DOWN]:
            theta2 -= 0.01

        screen.fill(WHITE)

        (x1, y1), (x2, y2) = forward_kinematics(theta1, theta2)

        base_x = WINDOW_WIDTH // 2
        base_y = WINDOW_HEIGHT // 2

        pygame.draw.line(screen, BLACK, (base_x, base_y), (base_x + x1, base_y - y1), 5)
        pygame.draw.line(screen, RED, (base_x + x1, base_y - y1), (base_x + x2, base_y - y2), 5)
        pygame.draw.circle(screen, BLACK, (base_x + int(x1), base_y - int(y1)), 10)
        pygame.draw.circle(screen, RED, (base_x + int(x2), base_y - int(y2)), 10)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()
