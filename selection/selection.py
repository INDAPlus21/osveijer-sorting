import random
import time
import pygame

length = int(input("Length: "))

pygame.init()

size = width, height = 1000, 450

screen = pygame.display.set_mode(size)

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

def draw_highlights(i, l, rects):
    pygame.draw.rect(screen, (0,255,0), rects[i])
    pygame.display.flip()
    pygame.draw.rect(screen, (0,255,0), rects[l])
    pygame.display.flip()

def erase_highlight(i, rects):
    pygame.draw.rect(screen, (255,255,255), rects[i])
    pygame.display.flip()

def draw_flipped(i,j,rects):
    rect1 = rects[i]
    rect2 = rects[j]
    pygame.draw.rect(screen, (0,0,0), pygame.Rect(rect1.left,0,rect1.width,1000))
    pygame.draw.rect(screen, (255,255,255), rect1)
    pygame.draw.rect(screen, (255,255,255), rect2)

def main_sort(arr):
    rects = get_rects(arr)
    draw_rects(rects)
    for i in range(len(arr)):
        minIndex = i
        j = i + 1
        for l in range(j, len(arr)):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.display.quit()
                    pygame.quit()
            draw_highlights(i, l, rects)
            if arr[l] < arr[minIndex]:
                minIndex = l
            pygame.time.wait(10)
            erase_highlight(l, rects)
        arr[i],arr[minIndex] = arr[minIndex],arr[i]
        rects = get_rects(arr)
        draw_flipped(i, minIndex,rects)
    q()

def q():
    pygame.time.wait(10000)
    pygame.display.quit()
    pygame.quit()

array = rand_array(length)
main_sort(array)



