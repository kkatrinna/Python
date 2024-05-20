from Character import *

food1_group = pygame.sprite.Group()
food2_group = pygame.sprite.Group()
food3_group = pygame.sprite.Group()
food_time = 0

current_time = pygame.time.get_ticks()
if current_time - food_time > 100:
    if len(food1_group) <= 5:
        food1 = Food()
        food1_rect = food1.rect
        if not pygame.sprite.spritecollide(food1, food1_group, False):
            food1_group.add(food1)
    if len(food2_group) <= 5:
        food2 = Food2()
        food2_rect = food2.rect
        if not pygame.sprite.spritecollide(food2, food2_group, False):
            food2_group.add(food2)
    if len(food3_group) <= 5:
        food3 = Food3()
        food3_rect = food3.rect
        food_time = current_time
        if not pygame.sprite.spritecollide(food3, food3_group, False):
            food3_group.add(food3)

    food1_group.update()
    food2_group.update()
    food3_group.update()

    food1_group.draw(window)
    food2_group.draw(window)
    food3_group.draw(window)