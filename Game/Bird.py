'''
Птичий полет: игрок управляет птицей,
летящей через различные среды, избегая хищников 
и собирая пищу.
'''

from Window import *
pygame.init()
pygame.init()
img = pygame.image.load("icon.png")
pygame.display.set_icon(img)
pygame.display.set_caption("Bird game")

bg_image_list = [pygame.transform.scale((pygame.image.load('bg1.jpg')), (width, height)).convert(),
                 pygame.transform.scale((pygame.image.load('bg1.jpg')), (width, height)).convert(),
                 pygame.transform.scale((pygame.image.load('bg.png')), (width, height)).convert(),
                 pygame.transform.scale((pygame.image.load('bg2.jpg')), (width, height)).convert(),
                 pygame.transform.scale((pygame.image.load('bg3.png')), (width, height)).convert(),
                 pygame.transform.scale((pygame.image.load('bg4.png')), (width, height)).convert()]
pred1_speed_list = [1, 2, 3, 4, 5]
pred2_speed_list = [2, 3, 4, 4, 5]
food_list = [3, 5, 8, 12, 15]

def start_game():
    #Create window
    global current_level
    clock = pygame.time.Clock()
    window = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Bird game")
    bg_image = pygame.image.load('bg1.jpg').convert()

    #Create sprites
    sprites = pygame.sprite.Group()
    predators = pygame.sprite.Group()
    foods = pygame.sprite.Group()

    bird = Bird()
    sprites.add(bird)

    cat = Predator("din.png", current_level, bird)
    eagle = Predator("eagle.png", current_level, bird)
    predators.add(cat, eagle)
    sprites.add(cat, eagle)

    for _ in range(food_list[current_level - 1]):
        food = Food("strawberry.png", (50, 50), 3)
        food2 = Food("berry.png", (40, 40), 2)
        food3 = Food("nuts.png", (30, 30), 4)
        sprites.add(food, food2, food3)
        foods.add(food, food2, food3)

    run = True
    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            bird.move_left()
        if keys[pygame.K_RIGHT]:
            bird.move_right()
        if keys[pygame.K_UP]:
            bird.move_up()
        if keys[pygame.K_DOWN]:
            bird.move_down()

        bird_predator = pygame.sprite.spritecollide(bird, predators, False)
        for predator in bird_predator:
            if error_window("Вы проиграли! Начать игру заново?"):
                sprites.empty()
                predators.empty()
                foods.empty()
                bird = Bird()
                sprites.add(bird)
                cat = Predator("din.png", 2, bird)
                eagle = Predator("eagle.png", 2, bird)
                predators.add(cat, eagle)
                sprites.add(cat, eagle)
                for _ in range(5):
                    food = Food("strawberry.png", (50, 50), 3)
                    food2 = Food("berry.png", (40, 40), 2)
                    food3 = Food("nuts.png", (30, 30), 4)
                    sprites.add(food, food2, food3)
                    foods.add(food, food2, food3)

        food_collisions = pygame.sprite.spritecollide(bird, foods, True)

        if not foods:
            if next_play("Вы выиграли! Начать следующий уровень?", current_level):
                current_level += 1
                if current_level < len(bg_image_list):
                    bg_image = bg_image_list[current_level]
                if current_level < len(bg_image_list):
                    bg_image = bg_image_list[current_level]
                if current_level - 1 < len(pred1_speed_list):
                    cat.speed = pred1_speed_list[current_level - 1]
                if current_level - 1 < len(pred2_speed_list):
                    eagle.speed = pred2_speed_list[current_level - 1]
                if current_level - 1 < len(food_list):
                    food_count = food_list[current_level - 1]
                foods.empty()
                sprites.empty()
                predators.empty()
                foods.empty()
                bird = Bird()
                sprites.add(bird)
                predators.add(cat, eagle)
                sprites.add(cat, eagle)
                cat.bird = bird
                eagle.bird = bird
                for _ in range(food_count):
                    food = Food("strawberry.png", (50, 50), 3)
                    food2 = Food("berry.png", (40, 40), 2)
                    food3 = Food("nuts.png", (30, 30), 4)
                    sprites.add(food, food2, food3)
                    foods.add(food, food2, food3)
                if current_level >= len(bg_image_list):
                    start_window()

        foods.update()
        predators.update()

        window.blit(bg_image, (0, 0))
        sprites.draw(window)
        pygame.display.flip()

def start_window():
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 56)
    window = pygame.display.set_mode((width, height))
    image = pygame.transform.scale((pygame.image.load("icon.png")), (500, 500)).convert_alpha()
    button_text = font.render("Начать игру", True, (255, 255, 255))
    button_rect = button_text.get_rect(center=(width // 2 + 200, height // 2))
    run = True
    while run:
        clock.tick(120)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect.collidepoint(event.pos):
                    run = False
                    start_game()
            window.fill((176, 196, 222))
            window.blit(image, (80, 80))
            window.blit(button_text, button_rect)
            pygame.display.flip()

start_window()

pygame.quit()




