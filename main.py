import pygame
import random

pygame.init()

window = pygame.display.set_mode([1280, 720])
title = pygame.display.set_caption("BeeHoney")

bg = pygame.image.load("sprites/bg.png")

bee_x = 610
bee_y = 600
bee_direction = 8
bee_anim = 1
bee_image = pygame.image.load("sprites/bee_" + str(bee_anim) + ".png")

spider_x = 300
spider_y = 0
spider_direction = 16
spider_anim = 1
spider_image = pygame.image.load("sprites/spider_" + str(spider_anim) + ".png")

flower_x = 300
flower_y = 0
flower_local = random.randint(300, 900)
flower_direction = 20
flower_image = pygame.image.load("sprites/flower.png")

score = 0

def draw():
    pygame.font.init()

    font = pygame.font.get_default_font()
    font_size = pygame.font.SysFont(font, 100, True)
    score_text = "Score: {}".format(score)
    score_text_render = font_size.render(score_text, True, [255, 255, 255])

    window.blit(bg, (0, 0))
    window.blit(flower_image, (flower_x, flower_y))
    window.blit(bee_image, (bee_x, bee_y))
    window.blit(spider_image, (spider_x, spider_y))
    window.blit(score_text_render, (100, 30))


def colision():

    global score
    global flower_y
    global spider_y

    if spider_y > 480 and bee_x + 50 > spider_x > bee_x - 50:
        spider_y = -100
        score -= 10

    if flower_y > 600 and bee_x + 40 > flower_x > bee_x - 40:
        score += 1
        flower_y = -50


loop = True
clock = pygame.time.Clock()

while loop:
    clock.tick(15)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                bee_direction *= -1

    bee_x += bee_direction
    spider_y += spider_direction
    flower_y += flower_direction

    if spider_x < bee_x:
        spider_x += 2
    elif spider_x > bee_x:
        spider_x -= 2

    if spider_y > 750:
        spider_y = -50
        spider_x = bee_x

    if flower_y > 750:
        flower_y = -50
        flower_local = random.randint(300, 900)
        flower_x = flower_local

    if bee_x >= 910:
        bee_x = 910
    elif bee_x <= 300:
        bee_x = 300

    if bee_anim < 4:
        bee_anim += 1
        bee_image = pygame.image.load("sprites/bee_" + str(bee_anim) + ".png")
    elif bee_anim == 4:
        bee_anim = 1
        bee_image = pygame.image.load("sprites/bee_" + str(bee_anim) + ".png")

    if spider_anim < 4:
        spider_anim += 1
        spider_image = pygame.image.load("sprites/spider_" + str(spider_anim) + ".png")
    elif spider_anim == 4:
        spider_anim = 1
        spider_image = pygame.image.load("sprites/spider_" + str(spider_anim) + ".png")

    colision()
    draw()
    pygame.display.update()
