import pygame
from math import pi, cos, sin
import datetime
from pygame import gfxdraw

WIDTH,HEIGHT = 1920,1080
center = (WIDTH/2, HEIGHT/2)
clock_radius = 400

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Cringest clock')
clock = pygame.time.Clock()

FPS=60
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
YELLOW = (196,166,0)
CLOCK = (33,35,57)

def numbers(number,size,position):
  font = pygame.font.SysFont('Arial',size, True, False)
  text = font.render(number, True, BLACK)
  text_rect = text.get_rect(center = position)
  screen.blit(text, text_rect)

def polar_to_cartesian(r, theta):
  x = r * sin(pi * theta / 180)
  y = r * cos(pi * theta / 180)
  return x + WIDTH / 2, -(y - HEIGHT/2)

def write_text(text,size, position, font_file, text_rotate_degrees=0, align = 'center'):
    font = pygame.font.Font(font_file, size)
    text_surface = font.render(text, True, CLOCK)
    if text_rotate_degrees != 0:
      text_surface = pygame.transform.rotate(text_surface, text_rotate_degrees)
    
    text_rect = text_surface.get_rect()

    if align == 'right':
      text_rect.topright = position
    elif align == 'left':
      text_rect.topleft = position
    else:
      text_rect.center = position
    screen.blit(text_surface, text_rect)


def main():
  run = True
  while run:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        run = False


    



    current_time = datetime.datetime.now()
    second = current_time.second
    minute = current_time.minute
    hour = current_time.hour


    screen.fill(WHITE)
    pygame.draw.circle(screen, BLACK, center, clock_radius-10, 10)
    pygame.draw.circle(screen, BLACK, center, clock_radius-28, 4)
    pygame.draw.circle(screen, BLACK, center, 12)

    #draw dividing lines
    rb = 15
    thetas = [23*rb, 1*rb, 6*rb, 11*rb, 14*rb+6, 20*rb]
    for theta in thetas:
      pygame.draw.line(screen, CLOCK, polar_to_cartesian(clock_radius - 30, theta), 
                        polar_to_cartesian(clock_radius - 335, theta), 2)

    write_text(u"Relax", 40, (WIDTH / 2 + 6, HEIGHT / 2 - 250), "Regular.ttf")
    write_text(u"Study", 40, (WIDTH / 2 + 200, HEIGHT / 2 - 60), "Regular.ttf", 8, 'right')
    write_text(u"Gaming", 40, (WIDTH / 2 + 230, HEIGHT / 2 + 60), "Regular.ttf", 360-23, 'right')
    write_text(u"Dinner", 40, (WIDTH / 2 + 33, HEIGHT / 2 + 155), "Regular.ttf", 360-3, 'right')
    write_text(u"Watching movie", 40, (WIDTH / 2 - 140, HEIGHT / 2 - 44), "Regular.ttf", 360-65, 'right')
    write_text(u"Reading", 40, (WIDTH / 2 - 110, HEIGHT / 2 - 260), "Regular.ttf", 55, 'right')
    

    for number in range(1,13):
      numbers(str(number), 50, polar_to_cartesian(clock_radius-80, number*30))
    
    for num in range(0,361,6):
        if num % 5!=0:
            pygame.draw.line(screen, BLACK, polar_to_cartesian(clock_radius-15, num), 
                                polar_to_cartesian(clock_radius-28, num), 2)

        else:
            pygame.draw.line(screen, BLACK, polar_to_cartesian(clock_radius-15, num), 
                            polar_to_cartesian(clock_radius-30, num), 6)
    
    #second
    r = 340 #long
    theta = second * (360/60)
    pygame.draw.line(screen, RED, center, polar_to_cartesian(r,theta), 4)

    #minute
    m = 280
    theta = (minute + second /60) *(360/60)
    pygame.draw.line(screen, BLACK, center, polar_to_cartesian(m,theta), 10)

    #hour
    h = 250
    theta = (hour+minute/60 + second/360) * (360 / 12)
    pygame.draw.line(screen, BLACK, center, polar_to_cartesian(h,theta), 18)



    #play button
    gfxdraw.filled_circle(screen, int(center[0]), int(center[1]), clock_radius - 350, YELLOW)
    pygame.draw.circle(screen, CLOCK, center, clock_radius -351-1,2)
    write_text("PLAY", 46, (WIDTH/2, HEIGHT/2 + 3), 'Regular.ttf')
    
    pygame.display.update()
    clock.tick(FPS)

  pygame.quit()

if __name__ == '__main__':
  main()
