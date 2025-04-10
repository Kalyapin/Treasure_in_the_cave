from pygame import *


class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (50, 50))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

    def colliding_with(self, other_sprite):
        return sprite.collide_rect(self, other_sprite)


class Player(GameSprite):
    def update(self):

        key_pressed = key.get_pressed()

        if key_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if key_pressed[K_s] and self.rect.y < 430:
            self.rect.y += self.speed
        if key_pressed[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed
        if key_pressed[K_d] and self.rect.x < 630:
            self.rect.x += self.speed


class EnemyH(GameSprite):
    def __init__(self, player_image, player_x, player_y, player_speed, distance):
        super().__init__(player_image, player_x, player_y, player_speed)
        self.direction = True
        self.x1 = player_x
        self.x2 = player_x + distance

    def update(self):

        if self.direction == True:
            self.rect.x += self.speed
            if self.rect.x > self.x2:
                self.direction = False
        else:
            self.rect.x -= self.speed
            if self.rect.x < self.x1:
                self.direction = True


class EnemyV(GameSprite):
    def __init__(self, player_image, player_x, player_y, player_speed, distance):
        super().__init__(player_image, player_x, player_y, player_speed)
        self.direction = True
        self.y1 = player_y
        self.y2 = player_y + distance

    def update(self):
        if self.direction == True:
            self.rect.y += self.speed
            if self.rect.y > self.y2:
                self.direction = False

        else:
            self.rect.y -= self.speed
            if self.rect.y < self.y1:
                self.direction = True


class WallV(sprite.Sprite):
    def __init__(self, player_x, player_y):
        super().__init__()
        self.image = transform.scale(image.load("images/wallV.png"), (50, 150))
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class WallH(sprite.Sprite):
    def __init__(self, player_x, player_y):
        super().__init__()
        self.image = transform.scale(image.load("images/wall_h.png"), (150, 50))
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class WallBlock(sprite.Sprite):
    def __init__(self, player_x, player_y):
        super().__init__()
        self.image = transform.scale(image.load("images/bricksx64.png"), (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class MessageSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (200, 300))
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


window = display.set_mode((700, 500))
display.set_caption("Treasure in the cave")
background = transform.scale(image.load("images/background.jpg"), (700, 500))

levels = []

active_level = 0

player = Player("images/JK_P_Sword__Idle_008.png", 0, 0, 0)
main_treasure = GameSprite("images/treasures.png", 0, 0, 0)
walls = []
zombies = []
fake_treasures = []
traps = []
game_starts_screen = MessageSprite("images/Game_starts.png", 250, 100)
win_screen = MessageSprite("images/Win.png", 250, 100)
death_screen = MessageSprite("images/Death.png", 250, 100)
next_lvl_screen = MessageSprite("images/Next_level.png", 250, 100)


def level_1():
    global player, main_treasure, walls, zombies, fake_treasures, traps

    player = Player("images/JK_P_Sword__Idle_008.png", 600, 450, 5)
    main_treasure = GameSprite("images/treasures.png", 550, 450, 0)

    walls = [WallV(450, 250), WallV(450, 400), WallV(450, 400), WallV(150, 50),
             WallV(150, 0), WallH(400, 200),
             WallV(610, 90),
             WallH(270, 200), WallH(240, 330), WallH(300, 450), WallH(150, 450),
             WallH(0, 450), WallH(90, 330),
             WallH(200, 40), WallH(350, 40),
             WallH(0, 330), WallH(60, 200), WallH(500, 40), WallBlock(350, 150)]

    zombies = [EnemyH("images/__Zombie01_Idle_005.png", 500, 300, 2, 100),
               EnemyV("images/__Zombie01_Idle_005.png", 550, 200, 2, 200)]

    fake_treasures = [GameSprite("images/fake_treasure.png", 50, 50, 0)]

    traps = [GameSprite("images/vinhaTile.png", 0, 200, 0)]

def level_2():
    global player, main_treasure, walls, zombies, fake_treasures, traps
    player = Player("images/JK_P_Sword__Idle_008.png", 10, 50, 3)
    zombies = [EnemyH("images/__Zombie01_Idle_005.png", 100, 250, 2, 50)]
    main_treasure = GameSprite("images/treasures.png", 550, 450, 0)

    walls = [WallH(70, 370), WallH(220, 370), WallH(370, 370), WallBlock(470, 435),
             WallV(470, 220), WallH(70, 250)]

    zombies = [EnemyH("images/__Zombie01_Idle_005.png", 520, 300, 2, 90),
               EnemyV("images/__Zombie01_Idle_005.png", 550, 200, 2, 200)]

    fake_treasures = [GameSprite("images/fake_treasure.png", 400, 430, 0)]

    traps = [GameSprite("images/vinhaTile.png", 460, 165, 0)]


levels.append(level_1)
levels.append(level_2)

state = 4
# 0 - playing
# 1 - death
# 2 - next level
# 3 - finish
# 4 - start
# 5 - switching levels
clock = time.Clock()
fps = 60

state_timer = 0

game = True
while game:
    window.blit(background, (0, 0))

    if state == 0:
        for wall in walls:
            if player.colliding_with(wall):
                state = 1
        for trap in traps:
            if player.colliding_with(trap):
                state = 1
        for zombie in zombies:
            if player.colliding_with(zombie):
                state = 1
        if player.colliding_with(main_treasure):
            state = 2
        player.update()
        player.reset()
        main_treasure.reset()
        for trap in traps:
            trap.reset()
        for fake_treasure in fake_treasures:
            fake_treasure.reset()

        for wall in walls:
            wall.reset()
        for zombie in zombies:
            zombie.update()
            zombie.reset()

    elif state == 1:
        death_screen.reset()
        if state_timer == 120:
            state = 0
            levels[active_level]()
            state_timer = 0

        state_timer += 1

    elif state == 2:
        next_lvl_screen.reset()
        if state_timer == 120:
            active_level += 1
            levels[active_level]()
            state = 0

        state_timer += 1


    elif state == 3:
        if state_timer == 120:
            if active_level > len(levels):
                active_level = 0
            else:
                state = 5
        state_timer += 1

    elif state == 4:
        game_starts_screen.reset()
        if state_timer == 120:
            levels[active_level]()
            state = 0
            state_timer = 0

        state_timer += 1

    elif state == 5:
        if state_timer == 180:
            levels[active_level]()
            state_timer = 0

        state_timer += 1


    for e in event.get():
        if e.type == QUIT:
            game = False

    clock.tick(fps)
    display.update()
