import pygame

FrameFill = 0
UnFill = 230


class dieEnemy(pygame.sprite.Sprite):
    def __init__(self, x, y, FrameDie, group):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('Sprite/particl/die/enemy/e_1.png').convert_alpha()
        self.image = pygame.transform.scale(self.image.convert_alpha(), (64, 64))
        self.rect = self.image.get_rect(center=(x, y))
        self.FrameDie = FrameDie
        self.add(group)

    def update(self):
        match self.FrameDie:
            case 19:
                self.FrameDie = 0
                self.kill()
            case 0:
                self.image = pygame.image.load('Sprite/particl/die/enemy/e_2.png').convert_alpha()
                self.image = pygame.transform.scale(self.image.convert_alpha(), (64, 64))
            case 4:
                self.image = pygame.image.load('Sprite/particl/die/enemy/e_3.png').convert_alpha()
                self.image = pygame.transform.scale(self.image.convert_alpha(), (64, 64))
            case 9:
                self.image = pygame.image.load('Sprite/particl/die/enemy/e_4.png').convert_alpha()
                self.image = pygame.transform.scale(self.image.convert_alpha(), (64, 64))
            case 14:
                self.image = pygame.image.load('Sprite/particl/die/enemy/e_5.png').convert_alpha()
                self.image = pygame.transform.scale(self.image.convert_alpha(), (64, 64))
        self.FrameDie += 1


class UnfillBack(pygame.sprite.Sprite):
    def __init__(self, x, y, sizeX, SizeY, filename, group):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert_alpha()
        self.image.set_alpha(UnFill)
        self.image = pygame.transform.scale(self.image.convert_alpha(), (sizeX-180, SizeY-180))
        self.rect = self.image.get_rect(center=(x, y))
        self.add(group)

    def update(self):
        global UnFill, FrameFill
        match FrameFill:
            case 35:
                FrameFill = 0
                UnFill = 230
                self.kill()
        UnFill -= 7
        self.image.set_alpha(UnFill)
        FrameFill += 1


class particalDie(pygame.sprite.Sprite):
    def __init__(self, x, y, Frame, speed, idMove, group):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('Sprite/particl/diePartical/1/dp_1.png').convert_alpha()
        self.image = pygame.transform.scale(self.image.convert_alpha(), (39, 39))
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = speed
        self.Frame = Frame
        self.idMove = idMove
        self.add(group)

    def update(self):
        match self.idMove:
            case 0:
                if self.rect.y < 740:
                    self.rect.y += self.speed + 10
                else:
                    self.kill()
            case 1:
                if self.rect.y > 160:
                    self.rect.y -= self.speed
                else:
                    self.kill()
            case 2:
                if self.rect.x < 790:
                    self.rect.x += self.speed
                    self.rect.y += 5
                else:
                    self.kill()
            case 3:
                if self.rect.x > 245:
                    self.rect.x -= self.speed
                    self.rect.y += 5
                else:
                    self.kill()
        match self.Frame:
            case 14:
                self.image = pygame.image.load('Sprite/particl/diePartical/1/dp_1.png').convert_alpha()
                self.image = pygame.transform.scale(self.image.convert_alpha(), (39, 39))
                self.Frame = 0
            case 5:
                self.image = pygame.image.load('Sprite/particl/diePartical/1/dp_2.png').convert_alpha()
                self.image = pygame.transform.scale(self.image.convert_alpha(), (39, 39))
            case 10:
                self.image = pygame.image.load('Sprite/particl/diePartical/1/dp_3.png').convert_alpha()
                self.image = pygame.transform.scale(self.image.convert_alpha(), (39, 39))
        self.Frame += 1
