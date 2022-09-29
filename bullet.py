import pygame
import player


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, speed, isDown, group, filename):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert_alpha()
        self.image = pygame.transform.scale(self.image.convert_alpha(), (28, 28))
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = speed
        self.isDown = isDown
        self.add(group)

    def update(self):
        match player.idPlayer:
            case 0:
                if self.rect.y > 180:
                    self.rect.y -= self.speed
                else:
                    self.kill()
            case 1:
                if self.isDown:
                    if self.rect.y < 730:
                        self.rect.y += self.speed
                    else:
                        self.kill()
                if not self.isDown:
                    if self.rect.y > 175:
                        self.rect.y -= self.speed
                    else:
                        self.kill()
