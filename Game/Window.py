from pygame.locals import *
from Character import *
from pygame import Surface, K_LEFT, KEYUP, K_UP, K_RIGHT, K_DOWN, KEYDOWN, QUIT, MOUSEBUTTONDOWN
import  pygame
current_level = 1

#Create window error
def error_window(text):
    font = pygame.font.Font(None, 36)
    text_surf = font.render(text, True, (0, 0, 0))
    text_rect = text_surf.get_rect(center=(width//2, height//2-50))
    window.blit(text_surf, text_rect)
    button_text = font.render("Начать заново", True, (255, 255, 255))
    button_rect = button_text.get_rect(center=(width // 2, height // 2 + 50))
    pygame.draw.rect(window, (176, 196, 222), button_rect)
    window.blit(button_text, button_rect)
    pygame.display.flip()
    for event in pygame.event.get(QUIT):
        pygame.quit()
    for event in pygame.event.get(MOUSEBUTTONDOWN):
        if button_rect.collidepoint(event.pos):
            return False
        pygame.event.post(event)
    return True

#Create new_level
def next_play(text, current_level):

    font = pygame.font.Font(None, 56)
    text_surf = font.render(text, True, (0, 0, 0))
    text_rect = text_surf.get_rect(center=(width//2, height//2-50))
    window.blit(text_surf, text_rect)
    button_text = font.render("Следующий уровень", True, (255, 255, 255))
    button_rect = button_text.get_rect(center=(width // 2, height // 2))
    pygame.draw.rect(window, (176, 196, 222), button_rect)
    window.blit(button_text, button_rect)
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            return False
        for event in pygame.event.get(MOUSEBUTTONDOWN):
            if button_rect.collidepoint(event.pos):
                current_level += 1
                return False
        pygame.event.post(event)
    return True

'''def end_game(text):
    font = pygame.font.Font(None, 36)
    text_surf = font.render(text, True, (0, 0, 0))
    text_rect = text_surf.get_rect(center=(width//2, height//2-50))
    window.blit(text_surf, text_rect)
    button_text = font.render("Конец игры", True, (255, 255, 255))
    button_rect = button_text.get_rect(center=(width // 2, height // 2 + 50))
    pygame.draw.rect(window, (176, 196, 222), button_rect)
    window.blit(button_text, button_rect)
    pygame.display.flip()
    for event in pygame.event.get(QUIT):
        pygame.quit()
    for event in pygame.event.get(MOUSEBUTTONDOWN):
        if button_rect.collidepoint(event.pos):
            return False
        pygame.event.post(event)
    return True
'''








