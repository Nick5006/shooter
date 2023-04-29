from pygame import *
from random import randint
game = True
pointenemylost = 0
pointenemydead = 0
font.init()
font1 = font.Font(None, 20)
font2 = font.Font(None, 100)
schetchick1 = font1.render(str(pointenemydead), True, (255, 255, 255))
win = font2.render('You Win', True, (0, 255, 0))
lose = font2.render('You Lose', True, (255, 0, 0))
bulletshoot = True
rocketShoot = False
clock = time.Clock()

class GameSprite(sprite.Sprite):
    def __init__(self, speed, pl_image, x, y, width, height):
        super().__init__()
        self.speed = speed
        self.image = transform.scale(image.load(pl_image), (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = width

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Bullet(GameSprite):
    def update(self):
        self.rect.y -= self.speed

        if self.rect.y <= 0:
            self.kill()

class Rocket(GameSprite):
    def update(self):
        self.rect.y -= self.speed
        sprite_list2 = sprite.groupcollide(rockets, monsters, True, False)
        xz = self.rect.centerx
        yz = self.rect.top
        for ei in sprite_list2:
            boom = Boom(0, 'Взрыв2.png', xz, yz, 200, 200)
            booms.add(boom)

            mb = sprite.groupcollide(booms, monsters, True, True)
            for ert in mb:
                boom.kill()

        if self.rect.y <= 0:
            self.kill()
class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y >= 500:
            self.rect.y = 0
            self.rect.x = randint(0 + self.width, 700 - self.width)
            self.speed = randint(1, 4)
            global pointenemylost
            pointenemylost += 1
class Boom(GameSprite):
    def update(self):
        mb = sprite.groupcollide(booms, monsters, True, True)
        for ert in mb:
            self.kill()

class Player(GameSprite):
    global bulletshoot
    global rocketShoot

    def update(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_a] and self.rect.x >= 0:
            self.rect.x -= self.speed
        if key_pressed[K_d] and self.rect.x <= 700 - self.width:
            self.rect.x += self.speed
        if key_pressed[K_LEFT] and self.rect.x >= 0:
            self.rect.x -= self.speed
        if key_pressed[K_RIGHT] and self.rect.x <= 700 - self.width:
            self.rect.x += self.speed
        if key_pressed[K_LSHIFT]:
            self.speed = 20
        if not key_pressed[K_LSHIFT]:
            self.speed = 4

    def fire(self):
        global player_centerx
        global player_top
        if bulletshoot:
            bullet = Bullet(20, 'bullet.png', player_centerx, player_top, 10, 20)
            bullets.add(bullet)
            fire.play()
        elif rocketShoot:
            rocket = Rocket(20, 'рокета.png', player_centerx, player_top, 10, 20)
            rockets.add(rocket)



mixer.init()
window = display.set_mode((700, 500))
fire = mixer.Sound('fire.ogg')

bg = transform.scale(image.load('galaxy.jpg'), (700, 500))
mixer.music.load('space.ogg')
mixer.music.play(-1)
rockets = sprite.Group()
booms = sprite.Group()

player = Player(4, 'rocket.png', 350, 400, 65, 80)
monster1 = Enemy(randint(1, 4), 'ufo.png', randint(80, 620), 0, 80, 65)
monster2 = Enemy(randint(1, 4), 'ufo.png', randint(80, 620), 0, 80, 65)
monster3 = Enemy(randint(1, 4), 'ufo.png', randint(80, 620), 0, 80, 65)
monster4 = Enemy(randint(1, 4), 'ufo.png', randint(80, 620), 0, 80, 65)
monster5 = Enemy(randint(1, 4), 'ufo.png', randint(80, 620), 0, 80, 65)
monster6 = Enemy(randint(1, 4), 'ufo.png', randint(80, 620), 0, 80, 65)
monster7 = Enemy(randint(1, 4), 'ufo.png', randint(80, 620), 0, 80, 65)
monster8 = Enemy(randint(1, 4), 'ufo.png', randint(80, 620), 0, 80, 65)
monster9 = Enemy(randint(1, 4), 'ufo.png', randint(80, 620), 0, 80, 65)
monster10 = Enemy(randint(1, 4), 'ufo.png', randint(80, 620), 0, 80, 65)
monsters = sprite.Group()
bullets = sprite.Group()
monsters.add(monster1)
monsters.add(monster2)
monsters.add(monster3)
monsters.add(monster4)
monsters.add(monster5)
monsters.add(monster6)
monsters.add(monster7)
monsters.add(monster8)
monsters.add(monster9)
monsters.add(monster10)

while True:
    if game:
        window.blit(bg, (0, 0))
        player_centerx = player.rect.centerx
        player_top = player.rect.top
        player.reset()
        player.update()
        monsters.draw(window)
        monsters.update()
        bullets.draw(window)
        bullets.update()
        rockets.draw(window)
        rockets.update()
        sprites_list = sprite.groupcollide(monsters, bullets, True, True)
        booms.draw(window)
        booms.update()
        for e in sprites_list:
            pointenemydead += 1
        schetchick = font1.render('Пропущено: ' + str(pointenemylost), True, (255, 255, 255))
        schetchick1 = font1.render('Убито:' + str(pointenemydead), True, (255, 255, 255))
        window.blit(schetchick, (20, 20))
        window.blit(schetchick1, (20, 36))

    for e in event.get():

        if e.type == QUIT:
            exit()
        if e.type == KEYDOWN:
            if e.key == K_SPACE:
                player.fire()
            if e.key == K_1:
                rocketShoot = False
                bulletshoot = True
            if e.key == K_2:
                bulletshoot = False
                rocketShoot = True
        if e.type == KEYUP:
            if e.key == K_SPACE:
                pass
            if e.key == K_1:
                pass
            if e.key == K_2:
                pass
    if pointenemydead == 10:
        game = False
        window.blit(win, (250, 250))
    elif pointenemylost >= 10:
        game = False
        window.blit(lose, (250, 250))
    clock.tick(60)
    display.update()
# 250y 500x
