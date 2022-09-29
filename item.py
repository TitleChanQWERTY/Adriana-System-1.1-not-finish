import pygame


class soulCoin(pygame.sprite.Sprite):
    def __init__(self, x, y, Frame, group):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('Sprite/item/soulCoin/sc_1.png').convert_alpha()
        self.image = pygame.transform.scale(self.image.convert_alpha(), (74, 74))
        self.rect = self.image.get_rect(center=(x, y))
        self.Frame = Frame
        self.add(group)

    def update(self):
        match self.Frame:
            case 25:
                self.image = pygame.image.load('Sprite/item/soulCoin/sc_1.png').convert_alpha()
                self.image = pygame.transform.scale(self.image, (64, 64))
                self.Frame = 0
            case 5:
                self.image = pygame.image.load('Sprite/item/soulCoin/sc_2.png').convert_alpha()
                self.image = pygame.transform.scale(self.image, (64, 64))
            case 10:
                self.image = pygame.image.load('Sprite/item/soulCoin/sc_3.png').convert_alpha()
                self.image = pygame.transform.scale(self.image, (64, 64))
            case 15:
                self.image = pygame.image.load('Sprite/item/soulCoin/sc_4.png').convert_alpha()
                self.image = pygame.transform.scale(self.image, (64, 64))
            case 20:
                self.image = pygame.image.load('Sprite/item/soulCoin/sc_5.png').convert_alpha()
                self.image = pygame.transform.scale(self.image, (64, 64))
        self.Frame += 1
        if self.rect.y < 800:
            self.rect.y += 7


class eyeCoin(pygame.sprite.Sprite):
    def __init__(self, x, y, Frame, group):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('Sprite/item/eyeCoin/ec_1.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (45, 45))
        self.rect = self.image.get_rect(center=(x, y))
        self.Frame = Frame
        self.add(group)

    def update(self):
        match self.Frame:
            case 25:
                self.image = pygame.image.load('Sprite/item/eyeCoin/ec_1.png').convert_alpha()
                self.image = pygame.transform.scale(self.image, (45, 45))
                self.Frame = 0
            case 5:
                self.image = pygame.image.load('Sprite/item/eyeCoin/ec_2.png').convert_alpha()
                self.image = pygame.transform.scale(self.image, (45, 45))
            case 10:
                self.image = pygame.image.load('Sprite/item/eyeCoin/ec_3.png').convert_alpha()
                self.image = pygame.transform.scale(self.image, (45, 45))
            case 15:
                self.image = pygame.image.load('Sprite/item/eyeCoin/ec_4.png').convert_alpha()
                self.image = pygame.transform.scale(self.image, (45, 45))
            case 20:
                self.image = pygame.image.load('Sprite/item/eyeCoin/ec_5.png').convert_alpha()
                self.image = pygame.transform.scale(self.image, (45, 45))
        self.Frame += 1
        if self.rect.y < 800:
            self.rect.y += 6


class cardAnegel(pygame.sprite.Sprite):
    def __init__(self, x, y, Frame, group):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('Sprite/item/anegelesion card/AC_1.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (75, 75))
        self.rect = self.image.get_rect(center=(x, y))
        self.Frame = Frame
        self.add(group)

    def update(self):
        match self.Frame:
            case 55:
                self.image = pygame.image.load('Sprite/item/anegelesion card/AC_1.png').convert_alpha()
                self.image = pygame.transform.scale(self.image, (72, 72))
                self.Frame = 0
            case 10:
                self.image = pygame.image.load('Sprite/item/anegelesion card/AC_2.png').convert_alpha()
                self.image = pygame.transform.scale(self.image, (72, 72))
            case 20:
                self.image = pygame.image.load('Sprite/item/anegelesion card/AC_3.png').convert_alpha()
                self.image = pygame.transform.scale(self.image, (72, 72))
            case 30:
                self.image = pygame.image.load('Sprite/item/anegelesion card/AC_4.png').convert_alpha()
                self.image = pygame.transform.scale(self.image, (72, 72))
            case 40:
                self.image = pygame.image.load('Sprite/item/anegelesion card/AC_5.png').convert_alpha()
                self.image = pygame.transform.scale(self.image, (72, 72))
            case 50:
                self.image = pygame.image.load('Sprite/item/anegelesion card/AC_6.png').convert_alpha()
                self.image = pygame.transform.scale(self.image, (72, 72))
        self.Frame += 1
        if self.rect.y < 745:
            self.rect.y += 3
        else:
            self.kill()


class adrian(pygame.sprite.Sprite):
    def __init__(self, x, y, group):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('Sprite/item/adrian/a_1.png').convert_alpha()
        self.image = pygame.transform.scale(self.image.convert_alpha(), (52, 52))
        self.rect = self.image.get_rect(center=(x, y))
        self.Frame = 0
        self.add(group)

    def update(self):
        match self.Frame:
            case 75:
                self.image = pygame.image.load('Sprite/item/adrian/a_1.png').convert_alpha()
                self.image = pygame.transform.scale(self.image.convert_alpha(), (52, 52))
                self.Frame = 0
            case 10:
                self.image = pygame.image.load('Sprite/item/adrian/a_2.png').convert_alpha()
                self.image = pygame.transform.scale(self.image.convert_alpha(), (52, 52))
            case 20:
                self.image = pygame.image.load('Sprite/item/adrian/a_3.png').convert_alpha()
                self.image = pygame.transform.scale(self.image.convert_alpha(), (52, 52))
            case 30:
                self.image = pygame.image.load('Sprite/item/adrian/a_4.png').convert_alpha()
                self.image = pygame.transform.scale(self.image.convert_alpha(), (52, 52))
            case 40:
                self.image = pygame.image.load('Sprite/item/adrian/a_5.png').convert_alpha()
                self.image = pygame.transform.scale(self.image.convert_alpha(), (52, 52))
            case 50:
                self.image = pygame.image.load('Sprite/item/adrian/a_6.png').convert_alpha()
                self.image = pygame.transform.scale(self.image.convert_alpha(), (52, 52))
            case 60:
                self.image = pygame.image.load('Sprite/item/adrian/a_7.png').convert_alpha()
                self.image = pygame.transform.scale(self.image.convert_alpha(), (52, 52))
            case 70:
                self.image = pygame.image.load('Sprite/item/adrian/a_8.png').convert_alpha()
                self.image = pygame.transform.scale(self.image.convert_alpha(), (52, 52))
        self.Frame += 1
        if self.rect.y <= 785:
            self.rect.y += 5
        else:
            self.kill()


class clockPlus(pygame.sprite.Sprite):
    def __init__(self, x, y, Frame, group):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('Sprite/item/clockPlus/cp_1.png').convert_alpha()
        self.image = pygame.transform.scale(self.image.convert_alpha(), (37, 37))
        self.Frame = Frame
        self.rect = self.image.get_rect(center=(x, y))
        self.add(group)

    def update(self):
        match self.Frame:
            case 50:
                self.image = pygame.image.load('Sprite/item/clockPlus/cp_1.png').convert_alpha()
                self.image = pygame.transform.scale(self.image.convert_alpha(), (37, 37))
                self.Frame = 0
            case 5:
                self.image = pygame.image.load('Sprite/item/clockPlus/cp_2.png').convert_alpha()
                self.image = pygame.transform.scale(self.image.convert_alpha(), (37, 37))
            case 10:
                self.image = pygame.image.load('Sprite/item/clockPlus/cp_3.png').convert_alpha()
                self.image = pygame.transform.scale(self.image.convert_alpha(), (37, 37))
            case 15:
                self.image = pygame.image.load('Sprite/item/clockPlus/cp_4.png').convert_alpha()
                self.image = pygame.transform.scale(self.image.convert_alpha(), (37, 37))
            case 20:
                self.image = pygame.image.load('Sprite/item/clockPlus/cp_5.png').convert_alpha()
                self.image = pygame.transform.scale(self.image.convert_alpha(), (37, 37))
            case 25:
                self.image = pygame.image.load('Sprite/item/clockPlus/cp_6.png').convert_alpha()
                self.image = pygame.transform.scale(self.image.convert_alpha(), (37, 37))
            case 30:
                self.image = pygame.image.load('Sprite/item/clockPlus/cp_7.png').convert_alpha()
                self.image = pygame.transform.scale(self.image.convert_alpha(), (37, 37))
            case 35:
                self.image = pygame.image.load('Sprite/item/clockPlus/cp_8.png').convert_alpha()
                self.image = pygame.transform.scale(self.image.convert_alpha(), (37, 37))
            case 40:
                self.image = pygame.image.load('Sprite/item/clockPlus/cp_9.png').convert_alpha()
                self.image = pygame.transform.scale(self.image.convert_alpha(), (37, 37))
            case 45:
                self.image = pygame.image.load('Sprite/item/clockPlus/cp_10.png').convert_alpha()
                self.image = pygame.transform.scale(self.image.convert_alpha(), (37, 37))
        self.Frame += 1
        if self.rect.y < 765:
            self.rect.y += 5
        else:
            self.kill()
