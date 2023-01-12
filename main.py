from tkinter import *
import math
import pygame


tk = Tk()
c = Canvas(tk, width=640, height=640, bg='white')
c.pack()

squ = c.create_rectangle(500, 100, 590, 190, fill='blue')
squf = c.create_rectangle(100, 620, 140, 640, fill='blue')
def rot_center(image, angle):
    orig_rect = image.get_rect()
    rot_image = pygame.transform.rotate(image, angle)
    rot_rect = orig_rect.copy()
    rot_rect.center = rot_image.get_rect().center
    rot_image = rot_image.subsurface(rot_rect).copy()
    return rot_image

def moveBall():
    squ2 = c.coords(squf)
    s = (590 - 100) ** 2 + (640 - 100) ** 2
    s2 = math.sqrt(s)
    coef = 10 / s2
    print(490 * coef, 540 * coef)
    c.move(squf, int(490 * coef), -int(540 * coef))
    c.after(50, moveBall)
c.after(50, moveBall)

mainloop()