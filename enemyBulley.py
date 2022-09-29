import pygame


class fourBullet(pygame.sprite.Sprite):
    def __init__(self, x, y, speed, size, idMove, filename, group):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert_alpha()
        self.image = pygame.transform.scale(self.image.convert_alpha(), (size, size))
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = speed
        self.idMove = idMove
        self.add(group)

    def update(self):
        match self.idMove:
            case 0:
                if self.rect.y < 755:
                    self.rect.y += self.speed + 10
                else:
                    self.kill()
            case 1:
                if self.rect.y > 165:
                    self.rect.y -= self.speed
                else:
                    self.kill()
            case 2:
                if self.rect.x < 795:
                    self.rect.x += self.speed
                    self.rect.y += 8
                else:
                    self.kill()
            case 3:
                if self.rect.x > 245:
                    self.rect.x -= self.speed
                    self.rect.y += 8
                else:
                    self.kill()


class simpleBullet(pygame.sprite.Sprite):
    def __init__(self, x, y, Size, Speed, filename, group):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert_alpha()
        self.image = pygame.transform.scale(self.image.convert_alpha(), (Size, Size))
        self.rect = self.image.get_rect(center=(x, y))
        self.Speed = Speed
        self.add(group)

    def update(self):
        if self.rect.y < 785:
            self.rect.y += self.Speed
        else:
            self.kill()
