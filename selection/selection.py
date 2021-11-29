import random
import time
import pygame

pygame.init()

size = width, height = 1000, 450

screen = pygame.display.set_mode(size)

def rand_array(len):
    out = []
    for i in range(len):
        out.append(random.randint(0,20))
    return out

def get_rects(arr):
    rects = []
    for i in range(len(arr)):
        rects.append(pygame.Rect(i*50+10,450-arr[i]*25,40,arr[i]*25))
    return rects

def draw_rects(rects):
    screen.fill("black")
    for i in rects:
        pygame.draw.rect(screen, (255,255,255), i)
        pygame.display.flip()

def draw_highlights(i, l, rects):
    pygame.draw.rect(screen, (0,255,0), rects[i])
    pygame.display.flip()
    pygame.draw.rect(screen, (0,255,0), rects[l])
    pygame.display.flip()

def main_sort(arr):
    for i in range(len(arr)):
        minIndex = i
        j = i + 1
        rects = get_rects(arr)
        for l in range(j, len(arr)):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.display.quit()
                    pygame.quit()
            draw_rects(rects)
            draw_highlights(i, l, rects)
            if arr[l] < arr[minIndex]:
                minIndex = l
            pygame.time.wait(100)
        arr[i],arr[minIndex] = arr[minIndex],arr[i]
    q()

def q():
    pygame.time.wait(10000)
    pygame.display.quit()
    pygame.quit()

array = rand_array(20)
main_sort(array)



