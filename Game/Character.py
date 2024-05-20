import random
import pygame
import math

width = 1020
height = 650
window = pygame.display.set_mode((width, height))

class Bird(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.x = 50
        self.y = 425
        self.vel_x = 0
        self.vel_y = 0
        self.speed = 2
        self.images = [
            pygame.transform.scale(pygame.image.load("main_character.png"), (90, 90)).convert_alpha(),
            pygame.transform.scale(pygame.image.load("main_character2.png"), (90, 90)).convert_alpha(),
            pygame.transform.scale(pygame.image.load("main_character3.png"), (90, 90)).convert_alpha(),
            pygame.transform.scale(pygame.image.load("main_character4.png"), (90, 90)).convert_alpha(),
        ]
        self.current_image = 0
        self.image = self.images[self.current_image]
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)

    def move_up(self):
        if self.rect.top > 0:
            self.rect.y -= 5
            self.current_image = 3
            self.image = self.images[self.current_image]

    def move_down(self):
        if self.rect.bottom < height:
            self.rect.y += 5
            self.current_image = 2
            self.image = self.images[self.current_image]

    def move_left(self):
        if self.rect.left > 0:
            self.rect.x -= 10
            self.current_image = 1
            self.image = self.images[self.current_image]

    def move_right(self):
        if self.rect.right < width:
            self.rect.x += 10
            self.current_image = 0
            self.image = self.images[self.current_image]

class Predator(pygame.sprite.Sprite):
    def __init__(self, image_path, speed, bird):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(image_path), (85, 85)).convert_alpha()
        self.rect = self.image.get_rect()
        self.speed = speed
        self.bird = bird
        self.rect.x = random.randint(0, width-self.rect.width)
        self.rect.y = random.randint(0, height-self.rect.height)
        self.direction = random.choice([(1, 0), (-1, 0), (0, 1), (0, -1)])
        while pygame.sprite.collide_rect(self, bird):
                self.rect.x = random.randint(0, width-self.rect.width)
                self.rect.y = random.randint(0, height-self.rect.height)
    def update(self):
        dx = self.bird.rect.x - self.rect.x
        dy = self.bird.rect.y - self.rect.y
        distance = math.sqrt(dx ** 2 + dy ** 2)

        if distance != 0:
            dx /= distance
            dy /= distance

        self.rect.x += dx * self.speed
        self.rect.y += dy * self.speed

        if self.rect.left < 0 or self.rect.right > width:
            self.rect.x -= dx * self.speed
        if self.rect.top < 0 or self.rect.bottom > height:
            self.rect.y -= dy * self.speed

class Food(pygame.sprite.Sprite):
    def __init__(self, image_path, size, speed):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(image_path), size).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, width-self.rect.width)
        self.rect.y = random.randint(0, height-self.rect.width)
        self.speed = speed
        self.direction = random.choice([(1, 0), (-1, 0), (0, 1), (0, -1)])
    def update(self):
        self.rect.x += self.direction[0] * self.speed
        self.rect.y += self.direction[1] * self.speed
        if self.rect.left < 0 or self.rect.right > width:
            self.direction = (self.direction[0] * -1, self.direction[1])
        if self.rect.top < 0 or self.rect.bottom > height:
            self.direction = (self.direction[0], self.direction[1] * -1)