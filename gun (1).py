import math
from random import choice

import pygame
import random
import time
from random import randrange as rnd

FPS = 30

RED = 0xFF0000
BLUE = 0x0000FF
YELLOW = 0xFFC91F
GREEN = 0x00FF00
MAGENTA = 0xFF03B8
CYAN = 0x00FFCC
BLACK = (0, 0, 0)
WHITE = 0xFFFFFF
GREY = 0x7D7D7D
GAME_COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]
wheat=(245,222,179)
white = (255, 255, 255)
black = (0, 0, 0)
blue = (0,0,255)
red = (200, 0, 0)
light_red = (255, 0, 0)
yellow = (200, 200, 0)
light_yellow = (255, 255, 0)
green = (34, 177, 76)
light_green = (0, 255, 0)
brown = (160, 128, 96)
tankWidth = 40
tankHeight = 20
turretWidth = 5
wheelWidth = 5
ground_height = 35
 


WIDTH = 800
HEIGHT = 600


class Ball():
    def __init__(self, screen: pygame.Surface, x, y):
        """ Конструктор класса ball

        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.screen = screen
        self.x = x
        self.y = y
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.color = choice(GAME_COLORS)
        self.live = 30

    def move(self):
        """Переместить мяч по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """
        # FIXME
        if self.x > 800:
            self.vx = self.vx * (-0.7)
            self.x = 790
        if self.x < 0:
            self.vx = self.vx * (-0.7)
            self.x=10
        if self.y > 600:
             self.vy = self.vy * (-0.3)
             self.y = 590
        if self.y < 0:
            self.vy = self.vy * (-0.3)
            self.y=10
        self.x += self.vx
        self.y += self.vy
        self.vy += 1

    def draw(self):
        pygame.draw.circle(
            self.screen,
            self.color,
            (self.x, self.y),
            self.r
        )

    def hittest(self, obj):
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.

        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        # FIXME
        if (self.x-obj.x)**2+ (self.y-obj.y)**2<(self.r+obj.r)**2:
            return True
        else:
            return False


class Bull():
    def __init__(self, screen: pygame.Surface, x=780, y=450):
        self.screen = screen
        self.x = x
        self.y = y
        self.a = 4
        self.vx = 0
        self.vy = 0
        self.color = YELLOW

        self.live = 30

    def move(self):
        self.x += self.vx
        self.y += self.vy
        self.vy += 1

    def draw(self):
        pygame.draw.polygon(self.screen, self.color, [(self.x-self.a/2, self.y-self.a/2), (self.x+self.a/2, self.y-self.a/2), (self.x+self.a/2, self.y+self.a/2), (self.x-self.a/2, self.y+self.a/2)])

    def hittest(self, obj):
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.

        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        # FIXME
        if (self.x-obj.x)**2+ (self.y-obj.y)**2<(self.a+obj.r)**2:
            return True
        else:
            return False

class Bomb:
    def __init__(self, screen: pygame.Surface, x, y):
        self.screen = screen
        self.x = x
        self.y = y
        self.r = 5
        self.vx = 3
        self.vy = 3
        self.color = BLACK
        self.live = 30

    def move(self):
        """Переместить мяч по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """
        # FIXME
        if self.x > 800:
            self.vx = self.vx * (-0.7)
            self.x = 790
        if self.x < 0:
            self.vx = self.vx * (-0.7)
            self.x=10
        if self.y > 600:
             self.vy = self.vy * (-0.7)
             self.y = 590
        if self.y < 0:
            self.vy = self.vy * (-0.7)
            self.y=10
        self.x += self.vx
        self.y += self.vy
        self.vy += 1

    def draw(self):
        pygame.draw.circle(
            self.screen,
            self.color,
            (self.x, self.y),
            self.r
        )

    def hittest(self, obj):
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.

        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        # FIXME
        if (self.x-obj.x)**2+ (self.y-obj.y)**2<(self.r+obj.r)**2:
            return True
        else:
            return False

class Gun:
    def __init__(self, screen: pygame.Surface, x=20, y=450):
        self.screen = screen
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        self.x = x
        self.y = y
        self.r = 10
        self.a = 30
        self.b = 40
        self.vx = 10
        self.color1 = GREY
        self.color2 = GREY
        self.color3 = GREEN
        self.points = 0
        self.live = 1
        self.new_gun()
        self.win()

    def fire2_start(self, event):
        self.f2_on = 1

    def fire2_end(self, event):
        """Выстрел мячом.

        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        global balls, bullet
        bullet += 1
        new_ball = Ball(self.screen, self.x, self.y)
        new_ball.r += 5

        self.an = math.atan2((event.pos[1]-new_ball.y), (event.pos[0]-new_ball.x))
        new_ball.vx = self.f2_power * math.cos(self.an)
        new_ball.vy = self.f2_power * math.sin(self.an)
        balls.append(new_ball)
        self.f2_on = 0
        self.f2_power = 10

    def targetting(self, event):
        """Прицеливание. Зависит от положения мыши."""
        if event.pos[0] < self.x:
            if event.pos[1] < self.y:
                if event:
                    self.an = - (math.pi - math.atan((self.y - event.pos[1]) / (self.x - event.pos[0])))
                if self.f2_on:
                    self.color = GREEN
                else:
                    self.color = GREY
            if event.pos[1] >= self.y:
                if event:
                    self.an =  math.pi - math.atan((event.pos[1] - self.y) / (self.x - event.pos[0]))
                if self.f2_on:
                    self.color = GREEN
                else:
                    self.color = GREY
        if event.pos[0] > self.x:
            if event.pos[1] < self.y:
                if event:
                    self.an = - math.atan((self.y - event.pos[1]) / (event.pos[0]) - self.x)
                if self.f2_on:
                    self.color = GREEN
                else:
                    self.color = GREY
            if event.pos[1] >= self.y:
                if event:
                    self.an = math.atan((event.pos[1] - self.y) / (self.x - event.pos[0]))
                if self.f2_on:
                    self.color = GREEN
                else:
                    self.color = GREY
        if event.pos[0] == self.x:
            if event.pos[1] < self.y:
                if event:
                    self.an = - math.pi/2
                if self.f2_on:
                    self.color = GREEN
                else:
                    self.color = GREY
            if event.pos[1] >= self.y:
                if event:
                    self.an =  math.pi/2
                if self.f2_on:
                    self.color = GREEN
                else:
                    self.color = GREY
        #if event:
            #self.an = math.atan((event.pos[1]-450) / (event.pos[0]-20))
        if self.f2_on:
            self.color = RED
        else:
            self.color = GREY


    def draw(self):
        # FIXIT don't know how to do it
       pygame.draw.line(self.screen, self.color1, (self.x, self.y),(self.x + self.f2_power*math.cos(self.an), self.y +self.f2_power*math.sin(self.an)), width=5)
       pygame.draw.polygon(self.screen, self.color3, [(self.x-self.b/2, self.y-self.a/2), (self.x+self.b/2, self.y-self.a/2), (self.x+self.b/2, self.y+self.a/2), (self.x-self.b/2, self.y+self.a/2)])
       pygame.draw.circle(
            self.screen,
            self.color2,
            (self.x, self.y),
            self.r
        )


    def move(self):
        if self.x > 800  or self.x < 0:
            self.vx = self.vx * (-1)
        self.x += self.vx
    
    def win(self):
        print("The end. GREEN win")
        f1 = pygame.font.Font(None, 32)
        text1 = f1.render("The end. GREEN win", 1, GREEN)
        screen.blit(text1, (320, 240))

    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            self.color = RED
        else:
            self.color = GREY
    
    def hit(self, points=1):
        """Попадание шарика в цель."""
        self.points += points

    def new_gun(self):
        """ Инициализация новой цели. """
        self.live = 1
        self.x = 20
        self.y = 450
        self.a = 30
        self.b = 40
        self.r = 10
        color = self.color = GREY
        color2 = self.color2 = GREY
        color3 = self.color3= GREEN


class Gun2(Gun):
    def __init__(self, screen: pygame.Surface, x=780, y=450):
        self.screen = screen
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        self.x = x
        self.y = y
        self.a = 30
        self.b = 40
        self.r = 10
        self.color = GREY
        self.color3= RED
        self.live = 1
        self.points = 0
        self.new_gun()
        self.win()



    def fire2_start(self, event):
        self.f2_on = 1

    def fire2_end(self, event):
        """Выстрел мячом.

        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        global bulls, bullet
        bullet += 1
        new_bull = Bull(self.screen)
        new_bull.a += 2

        self.an = math.atan2((event.pos[1]-new_bull.y), (event.pos[0]-new_bull.x))
        new_bull.vx = self.f2_power * math.cos(self.an)
        new_bull.vy = self.f2_power * math.sin(self.an)
        bulls.append(new_bull)
        self.f2_on = 0
        self.f2_power = 10

    def targetting(self, event):
        """Прицеливание. Зависит от положения мыши."""
        if event.pos[0] < 780:
            if event:
                self.an =  math.atan((event.pos[1] - 450) / (event.pos[0] - 780))
            if self.f2_on:
                self.color = GREEN
            else:
                self.color = GREY
        if event.pos[0] > 780:
            if event:
                self.an =  math.atan((event.pos[1]-450) / (780 - event.pos[0]))
            if self.f2_on:
                self.color = GREEN
            else:
                self.color = GREY
        if event.pos[0] == 780:
            if event:
                self.an = - math.pi /2
            if self.f2_on:
                self.color = GREEN
            else:
                self.color = GREY

    def hit(self, points=1):
        self.points += points





    def draw(self):
        # FIXIT don't know how to do it
        pygame.draw.line(self.screen, self.color, (self.x, self.y),(self.x + self.f2_power*math.cos(self.an), self.y +self.f2_power*math.sin(self.an)), width=5)
        pygame.draw.polygon(self.screen, self.color3, [(self.x-self.b/2, self.y-self.a/2), (self.x+self.b/2, self.y-self.a/2), (self.x+self.b/2, self.y+self.a/2), (self.x-self.b/2, self.y+self.a/2)])
        pygame.draw.circle(
            self.screen,
            self.color,
            (self.x, self.y),
            self.r)
        
    def win(self):
        print('The end. RED win')
        f1 = pygame.font.Font(None, 32)
        text2 = f1.render(f'The end. RED win', 1, RED)
        screen.blit(text2, (20, 10))



    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            self.color = GREEN
        else:
            self.color = GREY

    def new_gun(self):
        """ Инициализация новой цели. """
        self.live = 1
        self.x = 780
        self.y = 450
        self.a = 30
        self.b = 40
        self.r = 10
        color = self.color = GREY
        color3 = self.color3= choice(GAME_COLORS)



class Target():
#    self.points = 0
#    self.live = 1
    # FIXME: don't work!!! How to call this functions when object is created?
#    self.new_target()

    def __init__(self, screen: pygame.Surface,):
        """ Инициализация новой цели. """
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        self.points = 0
        self.screen = screen
        self.live = 1
        self.vx = rnd(1,10)
        self.vy = rnd(1,10)
        self.new_target()

    def new_target(self):
        """ Инициализация новой цели. """
        self.live = 1
        x = self.x = rnd(600, 780)
        y = self.y = rnd(300, 550)
        r = self.r = rnd(2, 50)
        r2 = self.r2 = r + 2 
        color = self.color = RED
        color = self.color2 = BLACK

    def move(self):
        if self.x > 800  or self.x < 0:
            self.vx = self.vx * (-0.7)
        if self.y > 600  or self.y < 0:
            self.vy = self.vy * (-0.7)
        self.x += self.vx
        self.y += self.vy


    def hit(self, points=1):
        """Попадание шарика в цель."""
        self.points += points

    def draw(self,screen):
        pygame.draw.circle(screen,
        self.color2,
        (self.x, self.y),
        self.r2
    )
        pygame.draw.circle(screen,
        self.color,
        (self.x, self.y),
        self.r
    )
    def fire2_start(self, event):
        self.f2_on = 1

    def fire2_end(self, event):
        """Выстрел мячом.

        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        global bombs, bullet
        bullet += 1
        new_bomb = Bomb(self.screen, self.x, self.y)

        self.an = math.atan2((event.pos[1]-new_bomb.y), (event.pos[0]-new_bomb.x))
        new_bomb.vx = self.f2_power * math.cos(self.an)
        new_bomb.vy = self.f2_power * math.sin(self.an)
        bombs.append(new_bomb)
        self.f2_on = 0
        self.f2_power = 10

    def targetting(self, event):
        if event:
            bombs = Bomb(screen, self.x, self.y)



class Target2():
#    self.points = 0
#    self.live = 1
    # FIXME: don't work!!! How to call this functions when object is created?
#    self.new_target()

    def __init__(self):
        """ Инициализация новой цели. """
        self.points = 0
        self.live = 1
        self.vx = rnd(1,10)
        self.vy = rnd(1,10)
        self.new_target2()


    def new_target2(self):
        """ Инициализация новой цели. """
        self.live = 1
        x = self.x = 400
        y = self.y = 300
        r = self.r = rnd(2, 50)
        r2 = self.r2 = r + 2 
        color = self.color = GREEN
        color = self.color2 = BLACK



    def move(self):
        self.x += self.vx
        self.y += self.vy
        if self.x > 800  or self.x < 0:
            self.x = 400
        if self.y > 600  or self.y < 0:
            self.y = 300

    def hit(self, points=1):
        """Попадание шарика в цель."""
        self.points += points

    def draw(self,screen):
        pygame.draw.circle(screen,
        self.color2,
        (self.x, self.y),
        self.r2
    )
        pygame.draw.circle(screen,
        self.color,
        (self.x, self.y),
        self.r
    )



pygame.init()

 
screen = pygame.display.set_mode((WIDTH, HEIGHT))
bullet = 0
bulls = []
balls = []
bombs = []
start_time1 = -6
start_time2 = -6
clock = pygame.time.Clock()
gun = Gun(screen)
gun2 = Gun2(screen)
target = Target(screen)
target2 = Target2()
finished = False

while not finished:
    screen.fill(WHITE)
    gun.draw()
    gun.move()
    gun2.draw()
    target.draw(screen)
    target2.draw(screen)
    target.move()
    target2.move() 
    if time.time() - start_time1 < 5:
        gun.win()
    elif time.time() - start_time1 == 5:
        gun2.live = 1

    if time.time() - start_time2 < 5:
        gun2.win()
    elif time.time() - start_time2 == 5:
        gun.live = 1

    
            
    for b in balls:
        b.draw()
    pygame.display.update()
    for k in bulls:
        k.draw()
    pygame.display.update()
    for t in bombs:
        t.draw()
    pygame.display.update()


    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            gun.fire2_start(event)
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
            gun2.fire2_start(event)
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            gun.fire2_end(event)
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 3:
            gun2.fire2_end(event)
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 2:
            target.fire2_start(event)
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 2:
            target.fire2_end(event)
        elif event.type == pygame.MOUSEMOTION:
            gun.targetting(event)
            gun2.targetting(event)
            target.targetting(event)

    
    for b in balls:
        b.move()
        if b.hittest(target) and target.live:
            target.live = 0
            target.hit()
            target.new_target()
        if b.hittest(target2) and target2.live:
            target2.live = 0
            target2.hit()
            target2.new_target2()
        if b.hittest(gun2) and gun2.live:
            gun2.live = 0
            gun2.hit()
            gun2.new_gun()
            start_time1 = time.time()

                    

    
    #pygame.display.flip()

    for k in bulls:
        k.move()
        if k.hittest(target) and target.live:
            target.live = 0
            target.hit()
            target.new_target()
        if k.hittest(target2) and target2.live:
            target2.live = 0
            target2.hit()
            target2.new_target2()
        if k.hittest(gun) and gun.live:
            gun.live = 0
            gun.hit()
            gun.new_gun()
            start_time2 = time.time()
            
            
    
    for t in bombs:
        t.move()
        if t.hittest(gun) and gun.live:
            gun.live = 0
            gun.hit()
            gun.new_gun()
        if t.hittest(gun2) and gun2.live:
            gun2.live = 0
            gun2.hit()
            gun2.new_gun()


    gun.power_up()
    gun2.power_up()

pygame.quit()
