import pygame
import math

pygame.init()
screen = pygame.display.set_mode((1280, 720))
old_mouse = pygame.mouse.get_pos()
total_distance = 0
special_mode = False
start_time = 0

running = True
center = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

hex_color = "#F0EAD6"
eggshell = (int(hex_color[1:3], 16), int(hex_color[3:5], 16), int(hex_color[5:7], 16))

arc_width = 60
arc_height = 60
rect = (center.x - arc_width / 2, center.y + 50, arc_width, arc_height)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    new_mouse = pygame.mouse.get_pos()
    distance = math.sqrt((new_mouse[0] - old_mouse[0])**2 + (new_mouse[1] - old_mouse[1])**2)
    total_distance += distance

    mouse_x, mouse_y = pygame.mouse.get_pos()
    lefteye = center.x - 70 + (mouse_x - center.x) * 0.08
    righteye = center.x + 70 + (mouse_x - center.x) * 0.08
    vert = center.y - 10 + (mouse_y - center.y) * 0.1
    mouth_rect = (center.x - 30 + (mouse_x - center.x) * 0.08, center.y + 20 + (mouse_y - center.y) * 0.1, 60, 60)

    if total_distance >= 10000 and not special_mode:
        special_mode = True
        start_time = pygame.time.get_ticks()
        total_distance = 0

    if special_mode:
        screen.fill(eggshell)
        pygame.draw.circle(screen, (157, 185, 44), (int(center.x), int(center.y)), 200)
        pygame.draw.circle(screen, "black", (int(lefteye), int(vert)), 20)
        pygame.draw.circle(screen, "black", (int(righteye), int(vert)), 20)
        pygame.draw.arc(screen, "black", mouth_rect, math.radians(0), math.radians(180), 15)

        current_time = pygame.time.get_ticks()
        elapsed = current_time - start_time
        if elapsed >= 5000:
            special_mode = False
    else:
        screen.fill(eggshell)
        pygame.draw.circle(screen, "purple", (int(center.x), int(center.y)), 200)
        pygame.draw.circle(screen, "black", (int(lefteye), int(vert)), 20)
        pygame.draw.circle(screen, "black", (int(righteye), int(vert)), 20)
        pygame.draw.arc(screen, "black", mouth_rect, math.radians(180), math.radians(360), 15)

    old_mouse = new_mouse
    pygame.display.flip()

pygame.quit()
