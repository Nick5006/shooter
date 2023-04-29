from pygame import *
from random import randint

window = display.set_mode((500, 500))

window.fill((200, 255, 255))
clock = time.Clock()
font.init()


class Area:
    def __init__(self, color, x=0, y=0, width=100, height=50):
        self.fill_color = color
        self.rect = Rect(x, y, width, height)

    def fill(self):
        draw.rect(window, self.fill_color, self.rect)


class Label(Area):
    def set_text(self, text, fsize=25, text_color=(0, 0, 0)):
        self.text = text
        self.image = font.Font(None, fsize).render(text, True, text_color)

    def draw(self, shift_x=0, shift_y=0):
        draw.rect(window, self.fill_color, self.rect)
        window.blit(self.image, (self.rect.x + shift_x, self.rect.y + shift_y))


w1 = Area((255, 0, 0), 50, 100, 60, 100)
w2 = Area((255, 0, 0), 175, 100, 60, 100)
w3 = Area((255, 0, 0), 300, 100, 60, 100)
w4 = Area((255, 0, 0), 425, 100, 60, 100)

spisoc = []
x = 50
for i in range(4):
    card = Label((255, 0, 0), x, 100, 50, 100)
    card.set_text('Click')
    spisoc.append(card)
    x+=120

while True:
    for i in range(0, 4):
        spisoc[i].draw(5,15)
    '''w1.fill()
    w2.fill()
    w3.fill()
    w4.fill()'''
    display.update()
    clock.tick(40)
    for e in event.get():
        if e.type == QUIT:
            exit()
