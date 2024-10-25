import pygame
import math
import pyautogui
import ctypes

pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((250, 250))

hwnd = pygame.display.get_wm_info()["window"]
def set_window_always_on_top():
    ctypes.windll.user32.SetWindowPos(hwnd, -1, 0, 0, 0, 0, 0x0001 | 0x0002)

running = True

center = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

hex_color = "#F0EAD6"
eggshell = (int(hex_color[1:3], 16), int(hex_color[3:5], 16), int(hex_color[5:7], 16))

arc_width = 30  
arc_height = 30 
face_radius = 100  
eye_offset_x = 35 
eye_radius = 10  
mouth_offset_x = 15  
mouth_offset_y = 10  
mouth_width = 30 
mouth_height = 30 

def get_window_position():
    user32 = ctypes.windll.user32
    hwnd = pygame.display.get_wm_info()["window"]
    rect = ctypes.wintypes.RECT()
    user32.GetWindowRect(hwnd, ctypes.byref(rect))
    return rect.left, rect.top

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    set_window_always_on_top()

    win_x, win_y = get_window_position()

    mouse_x, mouse_y = pyautogui.position()

    relative_mouse_x = mouse_x - win_x
    relative_mouse_y = mouse_y - win_y

    lefteye = center.x - eye_offset_x + (relative_mouse_x - center.x) * 0.02
    righteye = center.x + eye_offset_x + (relative_mouse_x - center.x) * 0.02
    vert = center.y - 5 + (relative_mouse_y - center.y) * 0.025  

    mouth_rect = (
        center.x - mouth_offset_x + (relative_mouse_x - center.x) * 0.02,
        center.y + mouth_offset_y + (relative_mouse_y - center.y) * 0.025,
        mouth_width, mouth_height
    )

    screen.fill(eggshell)

    pygame.draw.circle(screen, "purple", (int(center.x), int(center.y)), face_radius)
    pygame.draw.circle(screen, "black", (int(lefteye), int(vert)), eye_radius)
    pygame.draw.circle(screen, "black", (int(righteye), int(vert)), eye_radius)
    pygame.draw.arc(screen, "black", mouth_rect, math.radians(180), math.radians(360), 7)  

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
