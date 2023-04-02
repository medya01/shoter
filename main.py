from pygame import *
from random import randint
from pygame import rect
font.init()

window = display.set_mode((700, 500))

background = transform.scale(image.load('galaxy.jpg'), (700, 500))

mixer.init()
mixer.music.load('space.ogg')
mixer.music.play(-1)


class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, player_widht, player_height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (player_widht, player_height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.width = player_widht
        self.height = player_height

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def update(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_RIGHT] and self.rect.x < 630:
            self.rect.x += self.speed
        if key_pressed[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
    def fire(self):
        bullet = Bullet('bullet.png', self.rect.centerx - 7 , self.rect.top, -5, 15, 20 )
        bullets.add(bullet)




lost = 0
ster = 0

class Enemy(GameSprite):
    def update(self):
        global lost
        self.rect.y += self.speed
        if self.rect.y > 500:
            self.rect.y = 0
            self.rect.x = randint(0, 800)
            lost = lost + 1

class Bullet(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y <= 0:
            self.kill()



monster = Enemy('ufo.png', randint(0 , 500), 0, randint(4, 6), 90 ,55)
monster2 = Enemy('ufo.png', randint(0 , 500), 0, randint(4, 6), 90 ,55)
monster3 = Enemy('ufo.png', randint(0 , 500), 0, randint(4, 6), 90 ,55)
monster4 = Enemy('ufo.png', randint(0 , 500), 0, randint(4, 6), 90 ,55)
monster5 = Enemy('ufo.png', randint(0 , 500), 0, randint(4, 6), 90 ,55)

monsters = sprite.Group()
monsters.add(monster)
monsters.add(monster2)
monsters.add(monster3)
monsters.add(monster4)
monsters.add(monster5)

font = font.Font(None, 50)
win = font.render('You win!', True, (0,255,0))
lose = font.render('You lose!', True, (0,255,0))

bullets = sprite.Group()

rocket = Player('rocket.png', 90, 400, 15, 50, 80)

clock = time.Clock()
finish = False
game = True
while game:



    if finish != True:
        window.blit(background, (0, 0))
        rocket.update()
        rocket.reset()
        monsters.update()
        monsters.draw(window)
        bullets.update()
        bullets.draw(window)

        if sprite.spritecollide(rocket, monsters, False):
            finish = True
            window.blit(lose, (200,200))


        spisok_monstrov = sprite.groupcollide(monsters, bullets, True, True)
        for m in spisok_monstrov:
            ster += 1
            monster = Enemy('ufo.png', randint(0, 500), 0, randint(4, 6), 90, 55)
            monsters.add(monster)

        shetchik = font.render('Пропущено ' + str(lost), 1, (255, 255, 255))
        shetchik2 = font.render('Счёт ' + str(ster), 1, (255, 255, 255))
        window.blit(shetchik, (0, 0))
        window.blit(shetchik2, (0, 35))

        if lost >= 5:
            finish = True
            window.blit(lose, (200,200))

        if ster >= 15:
            finish = True
            window.blit(win, (200,200))



    for e in event.get():
        if e.type == QUIT:
            game = False
        if e.type == KEYDOWN:
            if e.key == K_SPACE:
                rocket.fire()

    display.update()
    clock.tick(60)