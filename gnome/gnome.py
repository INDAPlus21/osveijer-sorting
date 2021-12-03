import random
import time
import pygame

length = int(input("Length: "))

pygame.init()

size = width, height = 1000, 513

screen = pygame.display.set_mode(size)
gnome = pygame.image.load("gnome.png")
gnomeRect = gnome.get_rect()
gnomeRect.top = 450

def rand_array(len):
    out = []
    for i in range(len):
        out.append(random.randint(0,450))
    return out

def get_rects(arr):
    rects = []
    for i in range(len(arr)):
        rects.append(pygame.Rect(i*(1000/len(arr)),450-arr[i],1000/len(arr),arr[i]))
    return rects

def draw_rects(rects):
    screen.fill("black")
    for i in rects:
        pygame.draw.rect(screen, (255,255,255), i)
        pygame.display.flip()

def draw_flipped(i,j,rects):
    rect1 = rects[i]
    rect2 = rects[j]
    pygame.draw.rect(screen, (0,0,0), pygame.Rect(rect1.left,0,rect1.width,1000))
    pygame.draw.rect(screen, (255,255,255), rect1)
    pygame.draw.rect(screen, (255,255,255), rect2)
        

def draw_gnome(pos):
    global gnome,gnomeRect,length
    pygame.draw.rect(screen, (0,0,0), pygame.Rect(0,450,1000,63))
    gnomeRect.left = 1000*pos/length
    screen.blit(gnome, gnomeRect)
    pygame.display.flip()
    

def main_sort(arr):
    gnomePos = 0
    rects = get_rects(arr)
    draw_rects(rects)
    while gnomePos < len(arr):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                pygame.quit()
        if gnomePos == 0 or arr[gnomePos-1] <= arr[gnomePos]:
            gnomePos += 1
            draw_gnome(gnomePos)
        else:
            arr[gnomePos-1], arr[gnomePos] = arr[gnomePos], arr[gnomePos-1]
            rects = get_rects(arr)
            draw_flipped(gnomePos-1,gnomePos,rects)
            draw_gnome(gnomePos)
            gnomePos -= 1
        pygame.time.wait(10)
    q()

def q():
    pygame.time.wait(5000)
    pygame.display.quit()
    pygame.quit()

array = rand_array(length)
main_sort(array)



