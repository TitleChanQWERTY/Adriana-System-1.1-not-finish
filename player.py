import pygame

isUp = False
isDown = False
isLeft = False
isRight = False

idPlayer = 0

idFinery = 0


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, filename, speed):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert_alpha()
        self.image = pygame.transform.scale(self.image.convert_alpha(), (16, 16))
        self.rect = self.image.get_rect(center=(x, y))
        self.idCh = idPlayer
        self.speed = speed

    def move(self):
        match self.idCh:
            case 0:
                if not isUp and not isDown and not isLeft and not isRight:
                    self.image = pygame.transform.scale(self.image.convert_alpha(), (16, 16))
                if isUp and self.rect.y > 160:
                    self.image = pygame.transform.scale(self.image.convert_alpha(), (16, 21))
                    self.rect.y -= self.speed
                if isDown and self.rect.y < 746:
                    self.image = pygame.transform.scale(self.image.convert_alpha(), (16, 21))
                    self.rect.y += self.speed
                if isLeft and self.rect.x > 255:
                    self.image = pygame.transform.scale(self.image.convert_alpha(), (21, 16))
                    self.rect.x -= self.speed
                if isRight and self.rect.x < 820:
                    self.image = pygame.transform.scale(self.image.convert_alpha(), (21, 16))
                    self.rect.x += self.speed
            case 1:
                if isUp and self.rect.y > 160:
                    self.rect.y = 170
                if isDown and self.rect.y < 742:
                    self.rect.y = 739
                if isRight and self.rect.x < 820:
                    self.rect.x += self.speed
                if isLeft and self.rect.x > 255:
                    self.rect.x -= self.speed


class PlayerMenu(pygame.sprite.Sprite):
    def __init__(self, x, y, speed):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('Sprite/Player/None.png').convert_alpha()
        self.image = pygame.transform.scale(self.image.convert_alpha(), (16, 16))
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = speed

    def move(self):
        if isUp and self.rect.y > 1:
            self.rect.y -= self.speed
        if isDown and self.rect.y < 890:
            self.rect.y += self.speed
        if isLeft and self.rect.x > 1:
            self.rect.x -= self.speed
        if isRight and self.rect.x < 1075:
            self.rect.x += self.speed
