import random

import pygame

import op


class ballRosa(pygame.sprite.Sprite):
    def __init__(self, x, y, select, group):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('Sprite/Enemy/ballRosa.png').convert_alpha()
        self.image = pygame.transform.scale(self.image.convert_alpha(), (34, 34))
        self.rect = self.image.get_rect(center=(x, y))
        self.select = select
        self.add(group)

    def update(self):
        if op.level >= 2:
            match self.select:
                case 0:
                    if self.rect.y < 745:
                        self.rect.y += 10
                    else:
                        self.kill()
                case 1:
                    if self.rect.y > 125:
                        self.rect.y -= 10
                    else:
                        self.kill()
        else:
            if self.rect.y < 745:
                self.rect.y += 10
            else:
                self.kill()


class eyeFly(pygame.sprite.Sprite):
    def __init__(self, x, y, FrameEye, group):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('Sprite/Enemy/eyeFly/eyeFly_1.png').convert_alpha()
        self.image = pygame.transform.scale(self.image.convert_alpha(), (84, 84))
        self.rect = self.image.get_rect(center=(x, y))
        self.Frame = FrameEye
        self.add(group)

    def update(self):
        match self.Frame:
            case 30:
                self.image = pygame.image.load('Sprite/Enemy/eyeFly/eyeFly_1.png').convert_alpha()
                self.image = pygame.transform.scale(self.image.convert_alpha(), (84, 84))
                self.Frame = 0
            case 5:
                self.image = pygame.image.load('Sprite/Enemy/eyeFly/eyeFly_2.png').convert_alpha()
                self.image = pygame.transform.scale(self.image.convert_alpha(), (84, 84))
            case 15:
                self.image = pygame.image.load('Sprite/Enemy/eyeFly/eyeFly_3.png').convert_alpha()
                self.image = pygame.transform.scale(self.image.convert_alpha(), (84, 84))
            case 25:
                self.image = pygame.image.load('Sprite/Enemy/eyeFly/eyeFly_4.png').convert_alpha()
                self.image = pygame.transform.scale(self.image.convert_alpha(), (84, 84))

        self.Frame += 1
        if self.rect.y < 265:
            self.rect.y += 4


class FlyFlare(pygame.sprite.Sprite):
    def __init__(self, x, y, FrameEye, group):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('Sprite/Enemy/flyFlare/f_1.png').convert_alpha()
        self.image = pygame.transform.scale(self.image.convert_alpha(), (82, 82))
        self.rect = self.image.get_rect(center=(x, y))
        self.Frame = FrameEye
        self.add(group)

    def update(self):
        if self.Frame == 65:
            self.image = pygame.image.load('Sprite/Enemy/flyFlare/f_1.png').convert_alpha()
            self.image = pygame.transform.scale(self.image.convert_alpha(), (82, 82))
            self.Frame = 0
        if self.Frame == 5:
            self.image = pygame.image.load('Sprite/Enemy/flyFlare/f_2.png').convert_alpha()
            self.image = pygame.transform.scale(self.image.convert_alpha(), (82, 82))
        if self.Frame == 10:
            self.image = pygame.image.load('Sprite/Enemy/flyFlare/f_3.png').convert_alpha()
            self.image = pygame.transform.scale(self.image.convert_alpha(), (82, 82))
        if self.Frame == 20:
            self.image = pygame.image.load('Sprite/Enemy/flyFlare/f_4.png').convert_alpha()
            self.image = pygame.transform.scale(self.image.convert_alpha(), (82, 82))
        if self.Frame == 25:
            self.image = pygame.image.load('Sprite/Enemy/flyFlare/f_5.png').convert_alpha()
            self.image = pygame.transform.scale(self.image.convert_alpha(), (82, 82))
        if self.Frame == 30:
            self.image = pygame.image.load('Sprite/Enemy/flyFlare/f_6.png').convert_alpha()
            self.image = pygame.transform.scale(self.image.convert_alpha(), (82, 82))
        if self.Frame == 35:
            self.image = pygame.image.load('Sprite/Enemy/flyFlare/f_7.png').convert_alpha()
            self.image = pygame.transform.scale(self.image.convert_alpha(), (82, 82))
        if self.Frame == 40:
            self.image = pygame.image.load('Sprite/Enemy/flyFlare/f_8.png').convert_alpha()
            self.image = pygame.transform.scale(self.image.convert_alpha(), (82, 82))
        if self.Frame == 45:
            self.image = pygame.image.load('Sprite/Enemy/flyFlare/f_9.png').convert_alpha()
            self.image = pygame.transform.scale(self.image.convert_alpha(), (82, 82))
        if self.Frame == 50:
            self.image = pygame.image.load('Sprite/Enemy/flyFlare/f_10.png').convert_alpha()
            self.image = pygame.transform.scale(self.image.convert_alpha(), (82, 82))
        if self.Frame == 55:
            self.image = pygame.image.load('Sprite/Enemy/flyFlare/f_11.png').convert_alpha()
            self.image = pygame.transform.scale(self.image.convert_alpha(), (82, 82))
        if self.Frame == 60:
            self.image = pygame.image.load('Sprite/Enemy/flyFlare/f_12.png').convert_alpha()
            self.image = pygame.transform.scale(self.image.convert_alpha(), (82, 82))
        self.Frame += 1

        if self.rect.y < 295:
            self.rect.y += 2


HealthStalker = 40


class stalkerGirl(pygame.sprite.Sprite):
    def __init__(self, x, y, group):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('Sprite/Enemy/stalkerGirl/sg_1.png').convert_alpha()
        self.image = pygame.transform.scale(self.image.convert_alpha(), (120, 120))
        self.rect = self.image.get_rect(center=(x, y))
        self.Frame = 0
        self.add(group)

    def update(self):
        global HealthStalker
        if HealthStalker <= 0:
            op.SCORE += 992
            HealthStalker = 35
            op.countEnemy += 1
            if op.SCORE >= op.HISCORE:
                op.HISCORE = op.SCORE
            self.kill()
        match self.Frame:
            case 21:
                self.image = pygame.image.load('Sprite/Enemy/stalkerGirl/sg_1.png').convert_alpha()
                self.image = pygame.transform.scale(self.image.convert_alpha(), (120, 120))
                self.Frame = 0
            case 12:
                self.image = pygame.image.load('Sprite/Enemy/stalkerGirl/sg_2.png').convert_alpha()
                self.image = pygame.transform.scale(self.image.convert_alpha(), (120, 120))
            case 18:
                self.image = pygame.image.load('Sprite/Enemy/stalkerGirl/sg_3.png').convert_alpha()
                self.image = pygame.transform.scale(self.image.convert_alpha(), (120, 120))
        self.Frame += 1
        if self.rect.y < 139:
            self.rect.y += 2


class shota(pygame.sprite.Sprite):
    def __init__(self, x, y, group):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('Sprite/Enemy/shota/shota.png').convert_alpha()
        self.image = pygame.transform.scale(self.image.convert_alpha(), (44, 51))
        self.rect = self.image.get_rect(center=(x, y))
        self.random = random.randint(0, 3)
        self.ySelect = random.randint(200, 475)
        self.Frame = 0
        self.add(group)

    def update(self):
        match self.random:
            case 0:
                if self.rect.y <= 755:
                    self.rect.y += 4
                else:
                    self.kill()
            case 1:
                if self.rect.y < self.ySelect:
                    self.rect.y += 4
                else:
                    if self.rect.x < 815:
                        self.image = pygame.image.load('Sprite/Enemy/shota/shota_right.png').convert_alpha()
                        self.image = pygame.transform.scale(self.image.convert_alpha(), (44, 51))
                        self.rect.x += 3
                    else:
                        self.kill()
            case 2:
                if self.rect.y < self.ySelect:
                    self.rect.y += 4
                else:
                    if self.rect.x > 215:
                        self.image = pygame.image.load('Sprite/Enemy/shota/shota_right.png').convert_alpha()
                        self.image = pygame.transform.scale(self.image.convert_alpha(), (44, 51))
                        self.image = pygame.transform.flip(self.image, True, False)
                        self.rect.x -= 3
                    else:
                        self.kill()
            case 3:
                if self.rect.y < self.ySelect:
                    self.rect.y += 4
                else:
                    match self.Frame:
                        case 35:
                            self.image = pygame.image.load('Sprite/Enemy/shota/shota.png').convert_alpha()
                            self.image = pygame.transform.scale(self.image.convert_alpha(), (44, 51))
                            self.Frame = 0
                        case 15:
                            self.image = pygame.image.load('Sprite/Enemy/shota/shota_down.png').convert_alpha()
                            self.image = pygame.transform.scale(self.image.convert_alpha(), (44, 51))
                    self.Frame += 1

class virus(pygame.sprite.Sprite):
    def __init__(self, x, y, alpha, scale, Frame, group):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('Sprite/Enemy/virus.png').convert_alpha()
        self.image.set_alpha(10)
        self.rect = self.image.get_rect(center=(x, y))
        self.Frame = Frame
        self.Scale = scale
        self.Alp = alpha
        self.add(group)

    def update(self):
        if self.Frame <= 40:
            self.Scale += 1
            self.image = pygame.image.load('Sprite/Enemy/virus.png').convert_alpha()
            self.rect.x += 1
            self.rect.x -= 1
            self.image = pygame.transform.scale(self.image, (self.Scale, self.Scale))
            self.Alp += 5
            self.image.set_alpha(self.Alp)
            self.Frame += 1
        else:
            if self.rect.y < 755:
                self.image = pygame.image.load('Sprite/Enemy/virus2.png').convert_alpha()
                self.image = pygame.transform.scale(self.image, (self.Scale, self.Scale+15))
                self.image.set_alpha(155)
                self.rect.y += 8
            else:
                self.kill()
