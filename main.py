import pygame
import threading

import bullet
import effect
import enemy
import enemyBulley
import item
import player
import op

from random import randint

pygame.init()
pygame.time.set_timer(pygame.USEREVENT, 1020)

RES = (1086, 907)
sc = pygame.display.set_mode((RES[0], RES[1]))

pygame.display.set_caption('Adriana.System 1.1:  Winter came with an uninvited guest')

# Player render
characterSprite = 'Sprite/Player/None.png'


# UI Frame
frameGame = pygame.image.load('Sprite/UI/Frame.png').convert_alpha()
frameGame = pygame.transform.scale(frameGame.convert_alpha(), (939, 939))
frameGameRect = frameGame.get_rect(center=(RES[0] // 2, RES[1] // 2))

# Font
font1 = pygame.font.Font('Font/3.ttf', 17)

font2 = pygame.font.Font('Font/1.ttf', 30)

font22 = pygame.font.Font('Font/1.ttf', 25)

fonFPS = pygame.font.Font('Font/4.ttf', 18)

timerSpawnBullet = 0


def createBullet(x, y, isDown, filename):
    global timerSpawnBullet
    match timerSpawnBullet:
        case 1:
            timerSpawnBullet = 0
            return bullet.Bullet(x, y, 20, isDown, playerBullet, filename)
    timerSpawnBullet += 1


timeSpawnRosa = 0
minTimeSpawnRosa = 85

def createBulletFour(x, y, idMove, filename):
    if idMove == 0:
        return enemyBulley.fourBullet(x, y, 8, 17, 0, filename, enemyBulletG)
    if idMove == 1:
        return enemyBulley.fourBullet(x, y, 8, 17, 1, filename, enemyBulletG)
    if idMove == 2:
        return enemyBulley.fourBullet(x, y, 8, 17, 2, filename, enemyBulletG)
    if idMove == 3:
        return enemyBulley.fourBullet(x, y, 8, 17, 3, filename, enemyBulletG)


timeSpawnBulletFour = 0

yPos = 0

select = None


def createBallRosa():
    global timeSpawnRosa, minTimeSpawnRosa, timeSpawnBulletFour, yPos, select
    if op.level >= 2:
        if countStalker < 2:
            match timeSpawnRosa:
                case 225:
                    xRand = randint(275, 795)
                    timeSpawnRosa -= minTimeSpawnRosa
                    select = randint(0, 1)
                    match select:
                        case 0:
                            yPos = 127
                        case 1:
                            yPos = 745
                    return enemy.ballRosa(xRand, yPos, select, ballRosa)
            timeSpawnRosa += 1
    else:
        match timeSpawnRosa:
            case 225:
                xRand = randint(275, 795)
                timeSpawnRosa -= minTimeSpawnRosa
                return enemy.ballRosa(xRand, 125, 0, ballRosa)
        timeSpawnRosa += 1
    for enemyB in ballRosa:
        match timeSpawnBulletFour:
            case 19:
                if op.level == 1:
                    timeSpawnBulletFour = 0
                    createBulletFour(enemyB.rect.x + 15, enemyB.rect.y + 30, 0, 'Sprite/Bullet/Enemy/1.png')
                    createBulletFour(enemyB.rect.x + 15, enemyB.rect.y - 15, 1, 'Sprite/Bullet/Enemy/1.png')
                    createBulletFour(enemyB.rect.x + 35, enemyB.rect.y + 20, 2, 'Sprite/Bullet/Enemy/1.png')
                    createBulletFour(enemyB.rect.x - 15, enemyB.rect.y + 20, 3, 'Sprite/Bullet/Enemy/1.png')
                if op.level >= 2:
                    match select:
                        case 0:
                            timeSpawnBulletFour = 0
                            createBulletFour(enemyB.rect.x + 15, enemyB.rect.y + 50, 0, 'Sprite/Bullet/Enemy/1.png')
                            createBulletFour(enemyB.rect.x + 15, enemyB.rect.y - 15, 1, 'Sprite/Bullet/Enemy/1.png')
                            createBulletFour(enemyB.rect.x + 35, enemyB.rect.y + 25, 2, 'Sprite/Bullet/Enemy/1.png')
                            createBulletFour(enemyB.rect.x - 15, enemyB.rect.y + 25, 3, 'Sprite/Bullet/Enemy/1.png')
                        case 1:
                            timeSpawnBulletFour = 0
                            createBulletFour(enemyB.rect.x + 15, enemyB.rect.y + 50, 0, 'Sprite/Bullet/Enemy/1.png')
                            createBulletFour(enemyB.rect.x + 35, enemyB.rect.y + 25, 2, 'Sprite/Bullet/Enemy/1.png')
                            createBulletFour(enemyB.rect.x - 15, enemyB.rect.y + 25, 3, 'Sprite/Bullet/Enemy/1.png')
        timeSpawnBulletFour += 1


timeCreateEyeFly = 0
timeCreateBulletEye = 0


def createSimpleBullet(x, y, Speed, Size, filename):
    return enemyBulley.simpleBullet(x, y, Size, Speed, filename, enemyBulletG)


FrameBack = 0


def createEyeFly():
    global timeCreateEyeFly, timeCreateBulletEye
    if op.level >= 2:
        if timeCreateEyeFly >= 365:
            XRand = randint(310, 775)
            timeCreateEyeFly = 125
            return enemy.eyeFly(XRand, 120, 0, eyeFlyG)
        else:
            timeCreateEyeFly += 1
        for eyeG in eyeFlyG:
            if timeCreateBulletEye > 40:
                timeCreateBulletEye = 0
                createSimpleBullet(eyeG.rect.x + 37, eyeG.rect.y + 45, 8, 28, 'Sprite/Bullet/Enemy/2.png')
            else:
                timeCreateBulletEye += 1


timeCreateFlare = 0
timeCreateBulletFlare = 0

timeOutShotFlare = 0


def createFlyFlare():
    global timeCreateFlare, timeCreateBulletFlare, timeOutShotFlare
    if op.level >= 3:
        if timeCreateFlare >= 200:
            XRand = randint(300, 795)
            timeCreateFlare = 1
            return enemy.FlyFlare(XRand, 120, 0, flareG)
        else:
            timeCreateFlare += 1
    for enemyB in flareG:
        if timeCreateBulletFlare >= 3:
            match timeOutShotFlare:
                case 25:
                    timeOutShotFlare = 0
                    timeCreateBulletFlare = 0
                case 5:
                    createBulletFour(enemyB.rect.x + 45, enemyB.rect.y + 50, 0, 'Sprite/Bullet/Enemy/1.png')
                case 10:
                    createBulletFour(enemyB.rect.x + 65, enemyB.rect.y + 25, 2, 'Sprite/Bullet/Enemy/1.png')
                case 15:
                    createBulletFour(enemyB.rect.x + 45, enemyB.rect.y - 15, 1, 'Sprite/Bullet/Enemy/1.png')
                case 20:
                    createBulletFour(enemyB.rect.x - 45, enemyB.rect.y + 25, 3, 'Sprite/Bullet/Enemy/1.png')
            timeOutShotFlare += 1
        else:
            timeCreateBulletFlare += 1


isStrike = False
HeartAnim = False

isDamagePlayer = False


def dieEnemyEffect(x, y):
    return effect.dieEnemy(x, y, 0, effectG)


def particalDie(x, y, idMove, speed):
    return effect.particalDie(x, y, 0, speed, idMove, particalG)


t3 = None

dieBallRosa = pygame.mixer.Sound('Audio/SFX/19.wav')
dieEye = pygame.mixer.Sound('Audio/SFX/13.wav')
dieFlare = pygame.mixer.Sound('Audio/SFX/8.wav')
dieStalker = pygame.mixer.Sound('Audio/SFX/4.wav')


def collision():
    global FrameBack, frameGame, frameGameRect, isStrike, HeartAnim, isDamagePlayer, countStalker, timeSet, t3
    for clockPlusC in clockPlusG:
        if p1.rect.collidepoint(clockPlusC.rect.center):
            timeSet += 5
            clockPlusC.kill()
            createUnFill('Sprite/UI/Fill/6.png', 840, 840)
    for coinC in coinG:
        if p1.rect.collidepoint(coinC.rect.center):
            op.SCORE += 1225
            if op.SCORE >= op.HISCORE:
                op.HISCORE = op.SCORE
            coinC.kill()
    for adrianC in adrianG:
        if p1.rect.collidepoint(adrianC.rect.center) or adrianC.rect.collidepoint(p1.rect.center):
            op.SCORE += 975
            if op.SCORE >= op.HISCORE:
                op.HISCORE = op.SCORE
            if op.player < 5:
                op.player += 1
            createUnFill('Sprite/UI/Fill/5.png', 840, 840)
            adrianC.kill()
    for cardC in cardG:
        if p1.rect.collidepoint(cardC.rect.center):
            if op.SCORE > 0:
                op.SCORE -= 129
            for enemyC in ballRosa:
                enemyC.kill()
            for enemyC in eyeFlyG:
                enemyC.kill()
            for enemyC in flareG:
                enemyC.kill()
            for enemyC in stalkerGirlG:
                enemyC.kill()
            createUnFill('Sprite/UI/Fill/2.png', 840, 840)
            op.countEnemy -= 3
            cardC.kill()
    for playerBulletC in playerBullet:
        for enemyC in ballRosa:
            if playerBulletC.rect.collidepoint(enemyC.rect.center) or \
                    enemyC.rect.collidepoint(playerBulletC.rect.center):
                dieEnemyEffect(enemyC.rect.x, enemyC.rect.y)
                op.countEnemy += 1
                createCoin(enemyC.rect.x, enemyC.rect.y, 0)
                op.SCORE += 492
                particalDie(enemyC.rect.x + 15, enemyC.rect.y + 50, 0, 9)
                particalDie(enemyC.rect.x + 15, enemyC.rect.y - 15, 1, 9)
                particalDie(enemyC.rect.x + 35, enemyC.rect.y + 25, 2, 9)
                particalDie(enemyC.rect.x - 15, enemyC.rect.y + 25, 3, 9)
                if op.SCORE >= op.HISCORE:
                    op.HISCORE = op.SCORE
                dieBallRosa.play()
                isStrike = True
                enemyC.kill()
    for playerBulletC in playerBullet:
        for enemyC in shotaG:
            if playerBulletC.rect.collidepoint(enemyC.rect.center):
                selectItem = randint(0, 15)
                if selectItem < 1 or selectItem > 2:
                    createCoin(enemyC.rect.x, enemyC.rect.y, 0)
                else:
                    createClock(enemyC.rect.x + 20, enemyC.rect.y - 5, 0)
                dieEnemyEffect(enemyC.rect.x, enemyC.rect.y)
                op.countEnemy += 1

                op.SCORE += 1492
                particalDie(enemyC.rect.x + 15, enemyC.rect.y + 50, 0, 9)
                particalDie(enemyC.rect.x + 15, enemyC.rect.y - 15, 1, 9)
                particalDie(enemyC.rect.x + 35, enemyC.rect.y + 25, 2, 9)
                particalDie(enemyC.rect.x - 15, enemyC.rect.y + 25, 3, 9)
                if op.SCORE >= op.HISCORE:
                    op.HISCORE = op.SCORE
                isStrike = True
                enemyC.kill()
    for playerBulletC in playerBullet:
        for enemyC in eyeFlyG:
            if playerBulletC.rect.collidepoint(enemyC.rect.center) or \
                    enemyC.rect.collidepoint(playerBulletC.rect.center):
                dieEnemyEffect(enemyC.rect.x, enemyC.rect.y)
                createCoin(enemyC.rect.x + 35, enemyC.rect.y - 15, 1)
                op.SCORE += 192
                if op.SCORE >= op.HISCORE:
                    op.HISCORE = op.SCORE
                op.countEnemy += 1
                particalDie(enemyC.rect.x + 15, enemyC.rect.y + 50, 0, 13)
                particalDie(enemyC.rect.x + 15, enemyC.rect.y - 15, 1, 13)
                particalDie(enemyC.rect.x + 35, enemyC.rect.y + 25, 2, 13)
                particalDie(enemyC.rect.x - 15, enemyC.rect.y + 25, 3, 13)
                dieEye.play()
                isStrike = True
                enemyC.kill()
    for playerBulletC in playerBullet:
        for enemyC in flareG:
            if playerBulletC.rect.collidepoint(enemyC.rect.center) or \
                    enemyC.rect.collidepoint(playerBulletC.rect.center):
                dieEnemyEffect(enemyC.rect.x, enemyC.rect.y)
                op.SCORE += 792
                if op.SCORE >= op.HISCORE:
                    op.HISCORE = op.SCORE
                createAnegelation(enemyC.rect.x + 25, enemyC.rect.y + 10)
                op.countEnemy += 1
                dieFlare.play()
                isStrike = True
                enemyC.kill()
    for playerBulletC in playerBullet:
        for enemyC in stalkerGirlG:
            if playerBulletC.rect.collidepoint(enemyC.rect.center):
                isStrike = True
                enemy.HealthStalker -= op.DamagePlayer
                if enemy.HealthStalker <= 0:
                    dieStalker.play()
                    countStalker -= 1
                    createAdrian(enemyC.rect.x + 45, enemyC.rect.y - 35)
                    dieEnemyEffect(enemyC.rect.x + 55, enemyC.rect.y + 55)
    for enemyBulletC in enemyBulletG:
        if enemyBulletC.rect.collidepoint(p1.rect.center) and isDamagePlayer:
            createUnFill('Sprite/UI/Fill/3.png', 840, 840)
            if op.SCORE > 0:
                op.SCORE -= 492
            HeartAnim = True
            op.player -= 1
            isDamagePlayer = False
            enemyBulletC.kill()
    for enemyBulletC in ballRosa:
        if p1.rect.collidepoint(enemyBulletC.rect.center) and isDamagePlayer:
            t3 = threading.Thread(target=createUnFill, args=('Sprite/UI/Fill/3.png', 840, 840)).start()
            if op.SCORE > 0:
                op.SCORE -= 992
            HeartAnim = True
            isDamagePlayer = False
            op.player -= 1
            enemyBulletC.kill()
    for enemyBulletC in virusG:
        if p1.rect.collidepoint(enemyBulletC.rect.center) and isDamagePlayer:
            createUnFill('Sprite/UI/Fill/3.png', 840, 840)
            if op.SCORE > 0:
                op.SCORE -= 26
            HeartAnim = True
            isDamagePlayer = False
            op.player -= 1
            enemyBulletC.kill()
    for enemyBulletC in eyeFlyG:
        if p1.rect.collidepoint(enemyBulletC.rect.center) and isDamagePlayer:
            createUnFill('Sprite/UI/Fill/4.png', 840, 840)
            if op.SCORE > 0:
                op.SCORE -= 392
            isDamagePlayer = False
            HeartAnim = True
            op.player -= 1
            enemyBulletC.kill()


clock = pygame.time.Clock()

timeSpawnBoss = 0
timeShotBoss = 0

playerBullet = pygame.sprite.Group()
enemyBulletG = pygame.sprite.Group()
ballRosa = pygame.sprite.Group()
flareG = pygame.sprite.Group()
eyeFlyG = pygame.sprite.Group()
alphaG = pygame.sprite.Group()
effectG = pygame.sprite.Group()
stalkerGirlG = pygame.sprite.Group()
particalG = pygame.sprite.Group()


def createUnFill(filename, sizeX, sizeY):
    return effect.UnfillBack(RES[0] // 2, RES[1] // 2, sizeX, sizeY, filename, alphaG)


current_scene = None


def switch_scene(scene):
    global current_scene
    current_scene = scene


HeartUI = pygame.image.load('Sprite/UI/Heart/fullHeart.png').convert_alpha()
HeartUI = pygame.transform.scale(HeartUI, (278, 94))
HeartRect = HeartUI.get_rect(center=(534, 95))

FrameHeart = 0

timeDamageOn = 0

countEnemyKill = 0


def createCoin(x, y, idCoin):
    match idCoin:
        case 0:
            return item.soulCoin(x, y, 0, coinG)
        case 1:
            return item.eyeCoin(x, y, 0, coinG)


timeSpawnStalker = 0

stalkerShotTime = 0

countStalker = 0


def createStalker():
    global timeSpawnStalker, stalkerShotTime, countStalker
    if op.level >= 2:
        if countStalker < 1:
            match timeSpawnStalker:
                case 305:
                    timeSpawnStalker = 0
                    countStalker += 1
                    randX = randint(300, 690)
                    return enemy.stalkerGirl(randX, 100, stalkerGirlG)
            timeSpawnStalker += 1
        for stalkerGirlC in stalkerGirlG:
            match stalkerShotTime:
                case 35:
                    stalkerShotTime = 0
                    createSimpleBullet(stalkerGirlC.rect.x + 56, stalkerGirlC.rect.y + 55, 7, 30,
                                       'Sprite/Bullet/Enemy/4.png')
            stalkerShotTime += 1


def createAnegelation(x, y):
    return item.cardAnegel(x, y, 0, cardG)


def createAdrian(x, y):
    return item.adrian(x, y, adrianG)


coinG = pygame.sprite.Group()
cardG = pygame.sprite.Group()
adrianG = pygame.sprite.Group()

p1 = player.Player(0, 0, 'Sprite/Player/None.png', 10)

shotaG = pygame.sprite.Group()

timeSpawnShota = 0

timeShotShota = 0


def createShota():
    global timeSpawnShota, timeShotShota
    if op.level >= 4:
        match timeSpawnShota:
            case 150:
                xPos = randint(295, 720)
                timeSpawnShota = 0
                return enemy.shota(xPos, 95, shotaG)
        timeSpawnShota += 1
        for sh in shotaG:
            match timeShotShota:
                case 19:
                    selectBullet = randint(0, 1)
                    timeShotShota = 0
                    match selectBullet:
                        case 0:
                            createSimpleBullet(sh.rect.x + 4, sh.rect.y + 45, 9, 25, 'Sprite/Bullet/Enemy/5.png')
                        case 1:
                            createSimpleBullet(sh.rect.x + 26, sh.rect.y + 45, 9, 25, 'Sprite/Bullet/Enemy/5.png')
            timeShotShota += 1


def dieScreen():
    global timeSet
    running = True
    FPS = 60

    dieFrame = pygame.image.load('Sprite/UI/dieFrame.png').convert_alpha()
    dieFrame = pygame.transform.scale(dieFrame, (RES[0], RES[1]))
    dieRect = dieFrame.get_rect(center=(RES[0] // 2, RES[1] // 2))

    # Fill
    FrameAlpha = 0
    alpha = 300
    isAlpha = True
    fillFrame = pygame.image.load('Sprite/UI/Fill/3.png').convert_alpha()
    fillFrame = pygame.transform.scale(fillFrame, (RES[0], RES[1]))
    fillFrame.set_alpha(alpha)
    fillRect = fillFrame.get_rect(center=(RES[0] // 2, RES[1] // 2))

    # Die
    FrameDie = 0
    isAnim = False
    isVisibleT = False
    dieText = pygame.image.load('Sprite/UI/Text/die/d_1.png').convert_alpha()
    dieText = pygame.transform.scale(dieText.convert_alpha(), (550, 550))
    dieTRect = dieText.get_rect(center=(550, 150))

    isKey = False

    while running:
        for e in pygame.event.get():
            match e.type:
                case pygame.QUIT:
                    running = False
                    switch_scene(None)
                case pygame.KEYDOWN:
                    match isKey:
                        case True:
                            player.isUp = False
                            player.isDown = False
                            player.isLeft = False
                            player.isRight = False
                            op.player = 5
                            op.level = int(1)
                            op.countEnemy = 0
                            for enemyC in ballRosa:
                                enemyC.kill()
                            for enemyC in eyeFlyG:
                                enemyC.kill()
                            for enemyC in flareG:
                                enemyC.kill()
                            for enemyC in stalkerGirlG:
                                enemyC.kill()
                            for eBulletC in enemyBulletG:
                                eBulletC.kill()
                            for shotaC in shotaG:
                                shotaC.kill()
                            for alphaC in alphaG:
                                alphaC.kill()
                            timeSet = 45
                            countStalker = 0
                            running = False
                            switch_scene(mainMenu)

        match isAlpha:
            case True:
                match FrameAlpha:
                    case 110:
                        alpha = 300
                        isAnim = True
                        isVisibleT = True
                        isAlpha = False
                        FrameAlpha = 0
                alpha -= 4
                fillFrame.set_alpha(alpha)
                FrameAlpha += 1
        match isAnim:
            case True:
                match FrameDie:
                    case 85:
                        isKey = True
                        isAnim = False
                    case 10:
                        dieText = pygame.image.load('Sprite/UI/Text/die/d_2.png').convert_alpha()
                        dieText = pygame.transform.scale(dieText.convert_alpha(), (550, 550))
                    case 20:
                        dieText = pygame.image.load('Sprite/UI/Text/die/d_3.png').convert_alpha()
                        dieText = pygame.transform.scale(dieText.convert_alpha(), (550, 550))
                    case 25:
                        dieText = pygame.image.load('Sprite/UI/Text/die/d_4.png').convert_alpha()
                        dieText = pygame.transform.scale(dieText.convert_alpha(), (550, 550))
                    case 40:
                        dieText = pygame.image.load('Sprite/UI/Text/die/d_5.png').convert_alpha()
                        dieText = pygame.transform.scale(dieText.convert_alpha(), (550, 550))
                    case 50:
                        dieText = pygame.image.load('Sprite/UI/Text/die/d_6.png').convert_alpha()
                        dieText = pygame.transform.scale(dieText.convert_alpha(), (550, 550))
                    case 55:
                        dieText = pygame.image.load('Sprite/UI/Text/die/d_7.png').convert_alpha()
                        dieText = pygame.transform.scale(dieText.convert_alpha(), (550, 550))
                    case 70:
                        dieText = pygame.image.load('Sprite/UI/Text/die/d_8.png').convert_alpha()
                        dieText = pygame.transform.scale(dieText.convert_alpha(), (550, 550))
                    case 80:
                        dieText = pygame.image.load('Sprite/UI/Text/die/d_9.png').convert_alpha()
                        dieText = pygame.transform.scale(dieText.convert_alpha(), (550, 550))
                FrameDie += 1

        sc.fill((0, 0, 0))
        sc.blit(dieFrame, dieRect)
        match isVisibleT:
            case True:
                sc.blit(dieText, dieTRect)
        match isAlpha:
            case True:
                sc.blit(fillFrame, fillRect)
        pygame.display.update()
        clock.tick(FPS)


def createClock(x, y, idCLock):
    match idCLock:
        case 0:
            item.clockPlus(x, y, 0, clockPlusG)


clockPlusG = pygame.sprite.Group()

timeSet = 45


def timeLost():
    running = True
    FPS = 60

    createUnFill('Sprite/UI/Fill/2.png', RES[0] * 2, RES[1] * 2)
    backFrame = pygame.image.load('Sprite/UI/timeFrame.png').convert_alpha()
    backFrame = pygame.transform.scale(backFrame, (RES[0], RES[1]))
    backRect = backFrame.get_rect(center=(RES[0] // 2, RES[1] // 2))

    while running:
        for e in pygame.event.get():
            match e.type:
                case pygame.QUIT:
                    running = False
                    switch_scene(None)
                case pygame.KEYDOWN:
                    countStalker = 0
                    running = False
                    switch_scene(mainMenu)
        sc.fill((0, 0, 0))
        sc.blit(backFrame, backRect)
        alphaG.draw(sc)
        pygame.display.update()
        clock.tick(FPS)
        alphaG.update()


t4 = None

virusG = pygame.sprite.Group()
timeSpawnVirus = 0
def createVirus():
    global timeSpawnVirus
    match timeSpawnVirus:
        case 120:
            Xrpos = randint(350, 710)
            Yrpos = randint(190, 340)
            timeSpawnVirus = 0
            return enemy.virus(Xrpos, Yrpos , 0, 0, 0, virusG)
    timeSpawnVirus += 1

def sceneScoreMode():
    global isStrike, FrameBack, frameGame, clock, HeartRect, HeartUI, FrameHeart, HeartAnim, isDamagePlayer, \
        timeDamageOn, countEnemyKill, p1, timeSet, t4

    op.level = 20

    match characterSprite:
        case 'Sprite/Player/Ioann.png':
            player.idPlayer = 0
            xPos = randint(280, 650)
            p1 = player.Player(xPos, 739, characterSprite, 12)
        case 'Sprite/Player/Valeria.png':
            player.idPlayer = 1
            p1 = player.Player(739, 739, characterSprite, 8)

    HIScoreText = font2.render('HISCORE: ' + str(op.HISCORE), False, (255, 255, 0))
    HIScoreRect = HIScoreText.get_rect(center=(534, 835))

    ScoreText = font22.render('SCORE: ' + str(op.SCORE), False, (255, 200, 0))
    ScoreRect = ScoreText.get_rect(center=(534, 868))

    FPSText = fonFPS.render(str(int(clock.get_fps())), False, (255, 255, 255))
    FPSRect = FPSText.get_rect(center=(270, 760))

    # Sprite Fill

    FillSprite = pygame.image.load('Sprite/UI/FillAnim/f_1.png').convert_alpha()
    FillSprite = pygame.transform.scale(FillSprite, (RES[0], RES[1]))
    FillRect = FillSprite.get_rect(center=(RES[0] // 2, RES[1] // 2))

    showAnim = pygame.image.load('Sprite/particl/show/s_1.png').convert_alpha()
    showAnim = pygame.transform.scale(showAnim.convert_alpha(), (639, 639))
    showRect = showAnim.get_rect(center=(RES[0] // 2, RES[1] // 2))

    IoannOutline = pygame.image.load('Sprite/UI/CharacterOutline/Ioann.png').convert_alpha()
    IoannOutline = pygame.transform.scale(IoannOutline, (610, 610))
    IoannOutline.set_alpha(100)
    IoannOutRect = IoannOutline.get_rect(center=(110, RES[1]//2+5))

    ValeriaOutline = pygame.image.load('Sprite/UI/CharacterOutline/Valeria.png').convert_alpha()
    ValeriaOutline = pygame.transform.scale(ValeriaOutline, (635, 635))
    ValeriaOutline.set_alpha(100)
    ValeriaOutRect = ValeriaOutline.get_rect(center=(945, RES[1]//2+5))

    FrameShow = 0

    FrameWings = 0

    running = True
    FPS = 60
    FrameDamage = 0
    createUnFill('Sprite/UI/Fill/4.png', 850, 850)
    while running:
        for e in pygame.event.get():
            match e.type:
                case pygame.QUIT:
                    running = False
                    switch_scene(None)
                case pygame.KEYDOWN:
                    if e.key == pygame.K_UP:
                        player.isUp = True
                    elif e.key == pygame.K_DOWN:
                        player.isDown = True
                    elif e.key == pygame.K_LEFT:
                        player.isLeft = True
                    elif e.key == pygame.K_RIGHT:
                        player.isRight = True
                case pygame.KEYUP:
                    if e.key == pygame.K_UP:
                        player.isUp = False
                    elif e.key == pygame.K_DOWN:
                        player.isDown = False
                    elif e.key == pygame.K_LEFT:
                        player.isLeft = False
                    elif e.key == pygame.K_RIGHT:
                        player.isRight = False
        sc.fill((7, 0, 11))
        match player.idFinery:
            case 1:
                finery = pygame.image.load("Sprite/Player/finery/Gentleman's hat.png").convert_alpha()
                finery = pygame.transform.scale(finery, (23, 23))
                fineryRect = finery.get_rect(center=(p1.rect.x + 7, p1.rect.y - 8))
                sc.blit(finery, fineryRect)
            case 2:
                finery = pygame.image.load("Sprite/Player/finery/Horn.png").convert_alpha()
                finery = pygame.transform.scale(finery, (30, 30))
                fineryRect = finery.get_rect(center=(p1.rect.x + 6, p1.rect.y - 5))
                sc.blit(finery, fineryRect)
            case 3:
                if FrameWings < 20:
                    finery = pygame.image.load("Sprite/Player/finery/Wings.png").convert_alpha()
                    finery = pygame.transform.scale(finery, (40, 40))
                    finery = pygame.transform.flip(finery, False, True)
                    fineryRect = finery.get_rect(center=(p1.rect.x + 8, p1.rect.y + 10))
                    sc.blit(finery, fineryRect)
                if FrameWings > 20:
                    finery = pygame.image.load("Sprite/Player/finery/Wings.png").convert_alpha()
                    finery = pygame.transform.scale(finery, (40, 40))
                    finery = pygame.transform.flip(finery, False, False)
                    fineryRect = finery.get_rect(center=(p1.rect.x + 8, p1.rect.y + 5))
                    sc.blit(finery, fineryRect)
                if FrameWings > 35:
                    FrameWings = 0
                FrameWings += 1

            case 4:
                finery = pygame.image.load("Sprite/Player/finery/Maid's bonnet.png").convert_alpha()
                finery = pygame.transform.scale(finery, (26, 26))
                fineryRect = finery.get_rect(center=(p1.rect.x + 8, p1.rect.y + 3))
                sc.blit(finery, fineryRect)
        match FrameShow:
            case 60:
                showAnim = pygame.image.load('Sprite/particl/show/s_1.png').convert_alpha()
                showAnim = pygame.transform.scale(showAnim, (600, 600))
                FrameShow = 0
            case 5:
                showAnim = pygame.image.load('Sprite/particl/show/s_2.png').convert_alpha()
                showAnim = pygame.transform.scale(showAnim, (600, 600))
            case 10:
                showAnim = pygame.image.load('Sprite/particl/show/s_3.png').convert_alpha()
                showAnim = pygame.transform.scale(showAnim, (600, 600))
            case 15:
                showAnim = pygame.image.load('Sprite/particl/show/s_4.png').convert_alpha()
                showAnim = pygame.transform.scale(showAnim, (600, 600))
            case 20:
                showAnim = pygame.image.load('Sprite/particl/show/s_5.png').convert_alpha()
                showAnim = pygame.transform.scale(showAnim, (600, 600))
            case 25:
                showAnim = pygame.image.load('Sprite/particl/show/s_6.png').convert_alpha()
                showAnim = pygame.transform.scale(showAnim, (600, 600))
            case 30:
                showAnim = pygame.image.load('Sprite/particl/show/s_7.png').convert_alpha()
                showAnim = pygame.transform.scale(showAnim, (600, 600))
            case 35:
                showAnim = pygame.image.load('Sprite/particl/show/s_8.png').convert_alpha()
                showAnim = pygame.transform.scale(showAnim, (600, 600))
            case 40:
                showAnim = pygame.image.load('Sprite/particl/show/s_9.png').convert_alpha()
                showAnim = pygame.transform.scale(showAnim, (600, 600))
            case 45:
                showAnim = pygame.image.load('Sprite/particl/show/s_10.png').convert_alpha()
                showAnim = pygame.transform.scale(showAnim, (600, 600))
            case 50:
                showAnim = pygame.image.load('Sprite/particl/show/s_11.png').convert_alpha()
                showAnim = pygame.transform.scale(showAnim, (600, 600))
            case 54:
                showAnim = pygame.image.load('Sprite/particl/show/s_12.png').convert_alpha()
                showAnim = pygame.transform.scale(showAnim, (600, 600))
        FrameShow += 0.5
        t4 = threading.Thread(target=collision()).start()

        keys = pygame.key.get_pressed()

        if keys[pygame.K_c]:
            match player.idPlayer:
                case 0:
                    createBullet(p1.rect.x + 9, p1.rect.y - 11, False, 'Sprite/Bullet/Player/B_1.png')
                case 1:
                    if p1.rect.y == 170:
                        createBullet(p1.rect.x + 9, p1.rect.y + 31, True, 'Sprite/Bullet/Player/3.png')
                    if p1.rect.y == 739:
                        bullet.isDown = False
                        createBullet(p1.rect.x + 9, p1.rect.y - 11, False, 'Sprite/Bullet/Player/2.png')

        match isDamagePlayer:
            case False:
                if timeDamageOn >= 50:
                    timeDamageOn = 0
                    p1.image.set_alpha(300)
                    isDamagePlayer = True
                else:
                    match FrameDamage:
                        case 20:
                            FrameDamage = 0
                            p1.image.set_alpha(300)
                        case 10:
                            p1.image.set_alpha(30)
                    FrameDamage += 1
                    timeDamageOn += 1

        match op.player:
            case 5:
                HeartUI = pygame.image.load('Sprite/UI/Heart/fullHeart.png').convert_alpha()
                HeartUI = pygame.transform.scale(HeartUI.convert_alpha(), (278, 74))
            case 4:
                HeartUI = pygame.image.load('Sprite/UI/Heart/CountHeart/4.png').convert_alpha()
                HeartUI = pygame.transform.scale(HeartUI.convert_alpha(), (278, 74))
            case 3:
                HeartUI = pygame.image.load('Sprite/UI/Heart/CountHeart/3.png').convert_alpha()
                HeartUI = pygame.transform.scale(HeartUI.convert_alpha(), (278, 74))
            case 2:
                HeartUI = pygame.image.load('Sprite/UI/Heart/CountHeart/2.png').convert_alpha()
                HeartUI = pygame.transform.scale(HeartUI.convert_alpha(), (278, 74))
            case 1:
                HeartUI = pygame.image.load('Sprite/UI/Heart/CountHeart/1.png').convert_alpha()
                HeartUI = pygame.transform.scale(HeartUI.convert_alpha(), (278, 74))
            case 0:
                running = False
                switch_scene(dieScreen)

        match isStrike:
            case True:
                match FrameBack:
                    case 30:
                        isStrike = False
                        FrameBack = 0
                    case 10:
                        frameGame = pygame.image.load('Sprite/UI/FrameStrike/Frame_1.png').convert_alpha()
                        frameGame = pygame.transform.scale(frameGame.convert_alpha(), (939, 939))
                    case 15:
                        frameGame = pygame.image.load('Sprite/UI/FrameStrike/Frame_2.png').convert_alpha()
                        frameGame = pygame.transform.scale(frameGame.convert_alpha(), (939, 939))
                    case 20:
                        frameGame = pygame.image.load('Sprite/UI/FrameStrike/Frame_3.png').convert_alpha()
                        frameGame = pygame.transform.scale(frameGame.convert_alpha(), (939, 939))
                    case 25:
                        frameGame = pygame.image.load('Sprite/UI/FrameStrike/Frame_4.png').convert_alpha()
                        frameGame = pygame.transform.scale(frameGame.convert_alpha(), (939, 939))
                FrameBack += 1
        createShota()
        createBallRosa()
        createStalker()
        createFlyFlare()
        createEyeFly()
        if HeartAnim:
            match FrameHeart:
                case 21:
                    FrameHeart = 0
                    HeartAnim = False
                case 0:
                    HeartUI = pygame.image.load('Sprite/UI/Heart/DamageHeartSprite/d_1.png').convert_alpha()
                    HeartUI = pygame.transform.scale(HeartUI.convert_alpha(), (278, 74))
                case 5:
                    HeartUI = pygame.image.load('Sprite/UI/Heart/DamageHeartSprite/d_2.png').convert_alpha()
                    HeartUI = pygame.transform.scale(HeartUI.convert_alpha(), (278, 74))
                case 10:
                    HeartUI = pygame.image.load('Sprite/UI/Heart/DamageHeartSprite/d_3.png').convert_alpha()
                    HeartUI = pygame.transform.scale(HeartUI.convert_alpha(), (278, 74))
                case 14:
                    HeartUI = pygame.image.load('Sprite/UI/Heart/DamageHeartSprite/d_4.png').convert_alpha()
                    HeartUI = pygame.transform.scale(HeartUI.convert_alpha(), (278, 74))
                case 19:
                    HeartUI = pygame.image.load('Sprite/UI/Heart/DamageHeartSprite/d_5.png').convert_alpha()
                    HeartUI = pygame.transform.scale(HeartUI.convert_alpha(), (278, 74))
            FrameHeart += 1
        clock.tick(FPS)
        sc.blit(showAnim, showRect)
        sc.blit(p1.image, p1.rect)
        particalG.draw(sc)
        ballRosa.draw(sc)
        shotaG.draw(sc)
        eyeFlyG.draw(sc)
        flareG.draw(sc)
        stalkerGirlG.draw(sc)
        playerBullet.draw(sc)
        enemyBulletG.draw(sc)
        adrianG.draw(sc)
        effectG.draw(sc)
        clockPlusG.draw(sc)
        cardG.draw(sc)
        coinG.draw(sc)
        alphaG.draw(sc)
        sc.blit(frameGame, frameGameRect)
        sc.blit(IoannOutline, IoannOutRect)
        sc.blit(ValeriaOutline, ValeriaOutRect)
        sc.blit(HeartUI, HeartRect)
        HIScoreText = font2.render('HISCORE: ' + str(op.HISCORE), False, (255, 255, 0))
        ScoreText = font22.render('SCORE: ' + str(op.SCORE), False, (255, 200, 0))
        FPSText = fonFPS.render(str(int(clock.get_fps())), False, (255, 255, 255))
        sc.blit(ScoreText, ScoreRect)
        sc.blit(HIScoreText, HIScoreRect)
        sc.blit(FPSText, FPSRect)
        sc.blit(FillSprite, FillRect)
        pygame.display.update()
        alphaG.update()
        p1.move()
        particalG.update()
        cardG.update()
        adrianG.update()
        coinG.update()
        shotaG.update()
        flareG.update()
        clockPlusG.update()
        stalkerGirlG.update()
        effectG.update()
        enemyBulletG.update()
        ballRosa.update()
        eyeFlyG.update()
        playerBullet.update()

def sceneGame():
    global isStrike, FrameBack, frameGame, clock, HeartRect, HeartUI, FrameHeart, HeartAnim, isDamagePlayer, \
        timeDamageOn, countEnemyKill, p1, timeSet, t4

    match characterSprite:
        case 'Sprite/Player/Ioann.png':
            player.idPlayer = 0
            xPos = randint(280, 650)
            p1 = player.Player(xPos, 739, characterSprite, 12)
        case 'Sprite/Player/Valeria.png':
            player.idPlayer = 1
            p1 = player.Player(739, 739, characterSprite, 8)
    match op.level:
        case 1:
            countEnemyKill = randint(5, 15)
        case 2:
            countEnemyKill = randint(20, 25)
        case 3:
            countEnemyKill = randint(35, 40)
        case 4:
            countEnemyKill = randint(45, 60)
        case 5:
            countEnemyKill = randint(5, 35)
        case 6:
            countEnemyKill = randint(65, 70)
        case 7:
            countEnemyKill = randint(75, 81)
        case 8:
            countEnemyKill = randint(85, 95)
        case 9:
            countEnemyKill = randint(80, 90)
        case 10:
            countEnemyKill = randint(10, 30)
    # Text
    countEnemyTXT = font1.render('Number of Enemies killed: ' + str(op.countEnemy) + '/' + str(countEnemyKill), False,
                                 (69, 3, 97))
    countEnemyRect = countEnemyTXT.get_rect(center=(545, 805))

    HIScoreText = font2.render('HISCORE: ' + str(op.HISCORE), False, (255, 255, 0))
    HIScoreRect = HIScoreText.get_rect(center=(534, 835))

    ScoreText = font22.render('SCORE: ' + str(op.SCORE), False, (255, 200, 0))
    ScoreRect = ScoreText.get_rect(center=(534, 868))

    fontTimer = pygame.font.Font('Font/4.ttf', 25)
    fontTimer2 = pygame.font.Font('Font/3.ttf', 25)
    TimeText = fontTimer.render(str(timeSet), False, (255, 255, 255))
    TimeTextRect = TimeText.get_rect(center=(550, 185))

    FPSText = fonFPS.render(str(int(clock.get_fps())), False, (255, 255, 255))
    FPSRect = FPSText.get_rect(center=(270, 760))

    # Sprite Complete
    completeImage = pygame.image.load('Sprite/UI/Text/Complete/c_1.png').convert_alpha()
    completeImage = pygame.transform.scale(completeImage, (555, 555))
    completeRect = completeImage.get_rect(center=(RES[0] // 2, RES[1] // 2))

    # Sprite Fill

    FillSprite = pygame.image.load('Sprite/UI/FillAnim/f_1.png').convert_alpha()
    FillSprite = pygame.transform.scale(FillSprite, (RES[0], RES[1]))
    FillRect = FillSprite.get_rect(center=(RES[0] // 2, RES[1] // 2))

    isComplete = False

    timeWait = 0
    timeWait2 = 0

    FrameComplete = 0

    FrameFill = 0

    fillComplete = False

    IoannOutline = pygame.image.load('Sprite/UI/CharacterOutline/Ioann.png').convert_alpha()
    IoannOutline = pygame.transform.scale(IoannOutline, (610, 610))
    IoannOutline.set_alpha(100)
    IoannOutRect = IoannOutline.get_rect(center=(110, RES[1]//2+5))

    ValeriaOutline = pygame.image.load('Sprite/UI/CharacterOutline/Valeria.png').convert_alpha()
    ValeriaOutline = pygame.transform.scale(ValeriaOutline, (635, 635))
    ValeriaOutline.set_alpha(100)
    ValeriaOutRect = ValeriaOutline.get_rect(center=(940, RES[1]//2+5))

    showAnim = pygame.image.load('Sprite/particl/show/s_1.png').convert_alpha()
    showAnim = pygame.transform.scale(showAnim.convert_alpha(), (639, 639))
    showRect = showAnim.get_rect(center=(RES[0] // 2, RES[1] // 2))
    FrameShow = 0

    FrameWings = 0

    FrameDamage = 0

    isBow = False

    running = True
    FPS = 60
    createUnFill('Sprite/UI/Fill/4.png', 850, 850)
    while running:
        for e in pygame.event.get():
            match e.type:
                case pygame.QUIT:
                    running = False
                    switch_scene(None)
                case pygame.KEYDOWN:
                    match e.key:
                        case pygame.K_UP:
                            player.isUp = True
                        case pygame.K_DOWN:
                            player.isDown = True
                        case pygame.K_LEFT:
                            player.isLeft = True
                        case pygame.K_RIGHT:
                            player.isRight = True
                case pygame.KEYUP:
                    match e.key:
                        case pygame.K_UP:
                            player.isUp = False
                        case pygame.K_DOWN:
                            player.isDown = False
                        case pygame.K_LEFT:
                            player.isLeft = False
                        case pygame.K_RIGHT:
                            player.isRight = False
                case pygame.USEREVENT:
                    if op.countEnemy < countEnemyKill:
                        timeSet -= 1
        sc.fill((7, 0, 11))
        match player.idFinery:
            case 1:
                finery = pygame.image.load("Sprite/Player/finery/Gentleman's hat.png").convert_alpha()
                finery = pygame.transform.scale(finery, (23, 23))
                fineryRect = finery.get_rect(center=(p1.rect.x + 7, p1.rect.y - 8))
                sc.blit(finery, fineryRect)
            case 2:
                finery = pygame.image.load("Sprite/Player/finery/Horn.png").convert_alpha()
                finery = pygame.transform.scale(finery, (30, 30))
                fineryRect = finery.get_rect(center=(p1.rect.x + 6, p1.rect.y - 5))
                sc.blit(finery, fineryRect)
            case 3:
                if FrameWings < 20:
                    finery = pygame.image.load("Sprite/Player/finery/Wings.png").convert_alpha()
                    finery = pygame.transform.scale(finery, (40, 40))
                    finery = pygame.transform.flip(finery, False, True)
                    fineryRect = finery.get_rect(center=(p1.rect.x + 8, p1.rect.y + 10))
                    sc.blit(finery, fineryRect)
                if FrameWings > 20:
                    finery = pygame.image.load("Sprite/Player/finery/Wings.png").convert_alpha()
                    finery = pygame.transform.scale(finery, (40, 40))
                    finery = pygame.transform.flip(finery, False, False)
                    fineryRect = finery.get_rect(center=(p1.rect.x + 8, p1.rect.y + 5))
                    sc.blit(finery, fineryRect)
                if FrameWings > 35:
                    FrameWings = 0
                FrameWings += 1
            case 4:
                finery = pygame.image.load("Sprite/Player/finery/Maid's bonnet.png").convert_alpha()
                finery = pygame.transform.scale(finery, (26, 26))
                fineryRect = finery.get_rect(center=(p1.rect.x + 8, p1.rect.y + 3))
                isBow = True
            case 5:
                finery = pygame.image.load("Sprite/Player/finery/clown wig.png").convert_alpha()
                finery = pygame.transform.scale(finery, (34, 34))
                fineryRect = finery.get_rect(center=(p1.rect.x + 8, p1.rect.y + 1))
                sc.blit(finery, fineryRect)
            case 6:
                finery = pygame.image.load("Sprite/Player/finery/Hakurei bow.png").convert_alpha()
                finery = pygame.transform.scale(finery, (36, 36))
                fineryRect = finery.get_rect(center=(p1.rect.x + 8, p1.rect.y + 2))
                isBow = True
            case 7:
                finery = pygame.image.load("Sprite/Player/finery/Realm glasses.png").convert_alpha()
                finery = pygame.transform.scale(finery, (27, 27))
                fineryRect = finery.get_rect(center=(p1.rect.x + 8, p1.rect.y + 5))
                isBow = True
            case 8:
                finery = pygame.image.load("Sprite/Player/finery/Sword.png").convert_alpha()
                finery = pygame.transform.scale(finery, (20, 20))
                fineryRect = finery.get_rect(center=(p1.rect.x + 8, p1.rect.y + 8))
                isBow = True
        match FrameShow:
            case 60:
                showAnim = pygame.image.load('Sprite/particl/show/s_1.png').convert_alpha()
                showAnim = pygame.transform.scale(showAnim, (600, 600))
                FrameShow = 0
            case 10:
                showAnim = pygame.image.load('Sprite/particl/show/s_3.png').convert_alpha()
                showAnim = pygame.transform.scale(showAnim, (600, 600))
            case 20:
                showAnim = pygame.image.load('Sprite/particl/show/s_5.png').convert_alpha()
                showAnim = pygame.transform.scale(showAnim, (600, 600))
            case 30:
                showAnim = pygame.image.load('Sprite/particl/show/s_7.png').convert_alpha()
                showAnim = pygame.transform.scale(showAnim, (600, 600))
            case 40:
                showAnim = pygame.image.load('Sprite/particl/show/s_9.png').convert_alpha()
                showAnim = pygame.transform.scale(showAnim, (600, 600))
            case 50:
                showAnim = pygame.image.load('Sprite/particl/show/s_11.png').convert_alpha()
                showAnim = pygame.transform.scale(showAnim, (600, 600))
        FrameShow += 0.5
        t4 = threading.Thread(target=collision()).start()
        match timeSet:
            case 0:
                running = False
                switch_scene(timeLost)
        keys = pygame.key.get_pressed()

        if keys[pygame.K_c]:
            match player.idPlayer:
                case 0:
                    createBullet(p1.rect.x + 9, p1.rect.y - 11, False, 'Sprite/Bullet/Player/B_1.png')
                case 1:
                    if p1.rect.y == 170:
                        createBullet(p1.rect.x + 9, p1.rect.y + 31, True, 'Sprite/Bullet/Player/3.png')
                    if p1.rect.y == 739:
                        bullet.isDown = False
                        createBullet(p1.rect.x + 9, p1.rect.y - 11, False, 'Sprite/Bullet/Player/2.png')

        match isDamagePlayer:
            case False:
                match timeDamageOn:
                    case 50:
                        p1.image.set_alpha(300)
                        timeDamageOn = 0
                        isDamagePlayer = True
                    case _:
                        match FrameDamage:
                            case 20:
                                FrameDamage = 0
                                p1.image.set_alpha(300)
                            case 10:
                                p1.image.set_alpha(30)
                        FrameDamage += 1
                        timeDamageOn += 1

        match op.player:
            case 5:
                HeartUI = pygame.image.load('Sprite/UI/Heart/fullHeart.png').convert_alpha()
                HeartUI = pygame.transform.scale(HeartUI.convert_alpha(), (278, 74))
            case 4:
                HeartUI = pygame.image.load('Sprite/UI/Heart/CountHeart/4.png').convert_alpha()
                HeartUI = pygame.transform.scale(HeartUI.convert_alpha(), (278, 74))
            case 3:
                HeartUI = pygame.image.load('Sprite/UI/Heart/CountHeart/3.png').convert_alpha()
                HeartUI = pygame.transform.scale(HeartUI.convert_alpha(), (278, 74))
            case 2:
                HeartUI = pygame.image.load('Sprite/UI/Heart/CountHeart/2.png').convert_alpha()
                HeartUI = pygame.transform.scale(HeartUI.convert_alpha(), (278, 74))
            case 1:
                HeartUI = pygame.image.load('Sprite/UI/Heart/CountHeart/1.png').convert_alpha()
                HeartUI = pygame.transform.scale(HeartUI.convert_alpha(), (278, 74))
            case 0:
                running = False
                switch_scene(dieScreen)

        match isStrike:
            case True:
                match FrameBack:
                    case 30:
                        isStrike = False
                        FrameBack = 0
                    case 10:
                        frameGame = pygame.image.load('Sprite/UI/FrameStrike/Frame_1.png').convert_alpha()
                        frameGame = pygame.transform.scale(frameGame.convert_alpha(), (939, 939))
                    case 15:
                        frameGame = pygame.image.load('Sprite/UI/FrameStrike/Frame_2.png').convert_alpha()
                        frameGame = pygame.transform.scale(frameGame.convert_alpha(), (939, 939))
                    case 20:
                        frameGame = pygame.image.load('Sprite/UI/FrameStrike/Frame_3.png').convert_alpha()
                        frameGame = pygame.transform.scale(frameGame.convert_alpha(), (939, 939))
                    case 25:
                        frameGame = pygame.image.load('Sprite/UI/FrameStrike/Frame_4.png').convert_alpha()
                        frameGame = pygame.transform.scale(frameGame.convert_alpha(), (939, 939))
                FrameBack += 1
        if op.countEnemy < countEnemyKill:
            createShota()
            createBallRosa()
            createStalker()
            createFlyFlare()
            createVirus()
            createEyeFly()
        if op.countEnemy >= countEnemyKill:
            if fillComplete:
                match FrameFill:
                    case 175:
                        timeWait2 = 0
                        timeWait = 0
                        FrameFill = 0
                        fillComplete = False
                        for enemyC in ballRosa:
                            enemyC.kill()
                        for enemyC in eyeFlyG:
                            enemyC.kill()
                        for enemyC in flareG:
                            enemyC.kill()
                        for enemyC in stalkerGirlG:
                            enemyC.kill()
                        for eBulletC in enemyBulletG:
                            eBulletC.kill()
                        for shotaC in shotaG:
                            shotaC.kill()
                        for alphaC in alphaG:
                            alphaC.kill()
                        switch_scene(nextLevel)
                        running = False
                    case 10:
                        FillSprite = pygame.image.load('Sprite/UI/FillAnim/f_2.png').convert_alpha()
                        FillSprite = pygame.transform.scale(FillSprite, (RES[0], RES[1]))
                    case 25:
                        FillSprite = pygame.image.load('Sprite/UI/FillAnim/f_3.png').convert_alpha()
                        FillSprite = pygame.transform.scale(FillSprite, (RES[0], RES[1]))
                    case 30:
                        FillSprite = pygame.image.load('Sprite/UI/FillAnim/f_4.png').convert_alpha()
                        FillSprite = pygame.transform.scale(FillSprite, (RES[0], RES[1]))
                    case 40:
                        FillSprite = pygame.image.load('Sprite/UI/FillAnim/f_5.png').convert_alpha()
                        FillSprite = pygame.transform.scale(FillSprite, (RES[0], RES[1]))
                    case 55:
                        FillSprite = pygame.image.load('Sprite/UI/FillAnim/f_6.png').convert_alpha()
                        FillSprite = pygame.transform.scale(FillSprite, (RES[0], RES[1]))
                    case 65:
                        FillSprite = pygame.image.load('Sprite/UI/FillAnim/f_7.png').convert_alpha()
                        FillSprite = pygame.transform.scale(FillSprite, (RES[0], RES[1]))
                FrameFill += 1

            if timeWait >= 125:
                isComplete = True
                match FrameComplete:
                    case 110:
                        if timeWait2 >= 2:
                            fillComplete = True
                        else:
                            timeWait2 += 1
                        FrameComplete = 0
                    case 10:
                        completeImage = pygame.image.load('Sprite/UI/Text/Complete/c_2.png').convert_alpha()
                        completeImage = pygame.transform.scale(completeImage, (555, 555))
                    case 15:
                        completeImage = pygame.image.load('Sprite/UI/Text/Complete/c_3.png').convert_alpha()
                        completeImage = pygame.transform.scale(completeImage, (555, 555))
                    case 25:
                        completeImage = pygame.image.load('Sprite/UI/Text/Complete/c_4.png').convert_alpha()
                        completeImage = pygame.transform.scale(completeImage, (555, 555))
                    case 40:
                        completeImage = pygame.image.load('Sprite/UI/Text/Complete/c_5.png').convert_alpha()
                        completeImage = pygame.transform.scale(completeImage, (555, 555))
                    case 50:
                        completeImage = pygame.image.load('Sprite/UI/Text/Complete/c_6.png').convert_alpha()
                        completeImage = pygame.transform.scale(completeImage, (555, 555))
                    case 60:
                        completeImage = pygame.image.load('Sprite/UI/Text/Complete/c_7.png').convert_alpha()
                        completeImage = pygame.transform.scale(completeImage, (555, 555))
                    case 70:
                        completeImage = pygame.image.load('Sprite/UI/Text/Complete/c_8.png').convert_alpha()
                        completeImage = pygame.transform.scale(completeImage, (555, 555))
                    case 80:
                        completeImage = pygame.image.load('Sprite/UI/Text/Complete/c_9.png').convert_alpha()
                        completeImage = pygame.transform.scale(completeImage, (555, 555))
                    case 90:
                        completeImage = pygame.image.load('Sprite/UI/Text/Complete/c_10.png').convert_alpha()
                        completeImage = pygame.transform.scale(completeImage, (555, 555))
                    case 100:
                        completeImage = pygame.image.load('Sprite/UI/Text/Complete/c_11.png').convert_alpha()
                        completeImage = pygame.transform.scale(completeImage, (555, 555))
                FrameComplete += 1
            else:
                timeWait += 1
        if HeartAnim:
            match FrameHeart:
                case 21:
                    FrameHeart = 0
                    HeartAnim = False
                case 0:
                    HeartUI = pygame.image.load('Sprite/UI/Heart/DamageHeartSprite/d_1.png').convert_alpha()
                    HeartUI = pygame.transform.scale(HeartUI.convert_alpha(), (278, 74))
                case 5:
                    HeartUI = pygame.image.load('Sprite/UI/Heart/DamageHeartSprite/d_2.png').convert_alpha()
                    HeartUI = pygame.transform.scale(HeartUI.convert_alpha(), (278, 74))
                case 10:
                    HeartUI = pygame.image.load('Sprite/UI/Heart/DamageHeartSprite/d_3.png').convert_alpha()
                    HeartUI = pygame.transform.scale(HeartUI.convert_alpha(), (278, 74))
                case 14:
                    HeartUI = pygame.image.load('Sprite/UI/Heart/DamageHeartSprite/d_4.png').convert_alpha()
                    HeartUI = pygame.transform.scale(HeartUI.convert_alpha(), (278, 74))
                case 19:
                    HeartUI = pygame.image.load('Sprite/UI/Heart/DamageHeartSprite/d_5.png').convert_alpha()
                    HeartUI = pygame.transform.scale(HeartUI.convert_alpha(), (278, 74))
            FrameHeart += 1
        clock.tick(FPS)
        sc.blit(showAnim, showRect)
        sc.blit(p1.image, p1.rect)
        match isBow:
            case True:
                sc.blit(finery, fineryRect)
        particalG.draw(sc)
        ballRosa.draw(sc)
        virusG.draw(sc)
        shotaG.draw(sc)
        eyeFlyG.draw(sc)
        flareG.draw(sc)
        stalkerGirlG.draw(sc)
        playerBullet.draw(sc)
        enemyBulletG.draw(sc)
        adrianG.draw(sc)
        effectG.draw(sc)
        clockPlusG.draw(sc)
        cardG.draw(sc)
        coinG.draw(sc)
        alphaG.draw(sc)
        sc.blit(frameGame, frameGameRect)
        sc.blit(IoannOutline, IoannOutRect)
        sc.blit(ValeriaOutline, ValeriaOutRect)
        match isComplete:
            case True:
                sc.blit(completeImage, completeRect)
        sc.blit(HeartUI, HeartRect)
        countEnemyTXT = font1.render('Number of Enemies killed: ' + str(op.countEnemy) + '/' + str(countEnemyKill),
                                     False,
                                     (64, 3, 97))
        HIScoreText = font2.render('HISCORE: ' + str(op.HISCORE), False, (255, 255, 0))
        ScoreText = font22.render('SCORE: ' + str(op.SCORE), False, (255, 200, 0))
        FPSText = fonFPS.render(str(int(clock.get_fps())), False, (255, 255, 255))
        if timeSet > 30:
            TimeText = fontTimer.render(str(timeSet), False, (0, 255, 0))
        else:
            TimeText = fontTimer2.render(str(timeSet), False, (255, 0, 0))
        sc.blit(countEnemyTXT, countEnemyRect)
        sc.blit(TimeText, TimeTextRect)
        sc.blit(ScoreText, ScoreRect)
        sc.blit(HIScoreText, HIScoreRect)
        sc.blit(FPSText, FPSRect)
        sc.blit(FillSprite, FillRect)
        pygame.display.update()
        alphaG.update()
        p1.move()
        particalG.update()
        virusG.update()
        cardG.update()
        adrianG.update()
        coinG.update()
        shotaG.update()
        flareG.update()
        clockPlusG.update()
        stalkerGirlG.update()
        effectG.update()
        enemyBulletG.update()
        ballRosa.update()
        eyeFlyG.update()
        playerBullet.update()


def cutscene():
    running = True
    FPS = 60

    selectScene = 0

    fontTXT = pygame.font.Font('Font/2.ttf', 28)
    TextTXT = fontTXT.render('', False, (255, 255, 255))
    TextRect = TextTXT.get_rect(center=(80, 805))

    backImage = pygame.image.load('Sprite/scene/1/1.png').convert_alpha()
    backImage = pygame.transform.scale(backImage, (650, 650))
    backImageRect = backImage.get_rect(center=(RES[0] // 2, RES[1] // 2))

    # UnFill
    alphaUn = 0
    FrameUnFill = 0
    unFillImage = pygame.image.load('Sprite/UI/Fill/1.png').convert_alpha()
    unFillImage = pygame.transform.scale(unFillImage, (RES[0], RES[1]))
    unFillImage.set_alpha(alphaUn)
    unFillRect = unFillImage.get_rect(center=(RES[0] // 2, RES[1] // 2))

    isVisibleScene = False

    isUnFill = False

    match op.level:
        case 4:
            while running:
                for e in pygame.event.get():
                    match e.type:
                        case pygame.QUIT:
                            running = False
                            switch_scene(None)
                        case pygame.KEYDOWN:
                            selectScene += 1
                match selectScene:
                    case 0:
                        TextTXT = fontTXT.render("Ioann: Well I don't know who could have done it", False, (0, 255, 0))
                    case 1:
                        TextTXT = fontTXT.render("Valeria: I don't know either", False, (255, 255, 255))
                    case 2:
                        isVisibleScene = True
                        TextTXT = fontTXT.render('...', False, (0, 0, 255))
                    case 3:
                        backImage = pygame.image.load('Sprite/scene/1/3.png').convert_alpha()
                        backImage = pygame.transform.smoothscale(backImage, (650, 650))
                        TextTXT = fontTXT.render('Valeria: Maybe it was QWERTY?', False, (255, 255, 255))
                    case 4:
                        backImage = pygame.image.load('Sprite/scene/1/2.png').convert_alpha()
                        backImage = pygame.transform.smoothscale(backImage, (650, 650))
                        TextTXT = fontTXT.render("Ioann: He couldn't do it, it's not very cruel, you understand for "
                                                 "him.", False, (0, 255, 0))
                    case 5:
                        backImage = pygame.image.load('Sprite/scene/1/1.png').convert_alpha()
                        backImage = pygame.transform.smoothscale(backImage, (650, 650))
                        TextTXT = fontTXT.render('...', False, (0, 0, 255))
                    case 6:
                        backImage = pygame.image.load('Sprite/scene/1/2.png').convert_alpha()
                        backImage = pygame.transform.smoothscale(backImage, (650, 650))
                        TextTXT = fontTXT.render('Ioann: Maybe it was Jan?', False, (0, 255, 0))
                    case 7:
                        backImage = pygame.image.load('Sprite/scene/1/3.png').convert_alpha()
                        backImage = pygame.transform.smoothscale(backImage, (650, 650))
                        TextTXT = fontTXT.render('Valeria: Yes maybe', False, (255, 255, 255))
                    case 8:
                        backImage = pygame.image.load('Sprite/scene/1/1.png').convert_alpha()
                        backImage = pygame.transform.smoothscale(backImage, (650, 650))
                        TextTXT = fontTXT.render('...', False, (0, 0, 255))
                    case 9:
                        isUnFill = True
                        selectScene = 10

                match isUnFill:
                    case True:
                        match FrameUnFill:
                            case 95:
                                switch_scene(sceneGame)
                                running = False
                        alphaUn += 3
                        unFillImage.set_alpha(alphaUn)
                        FrameUnFill += 1
                sc.fill((0, 0, 0))
                match isVisibleScene:
                    case True:
                        sc.blit(backImage, backImageRect)
                sc.blit(TextTXT, TextRect)
                sc.blit(unFillImage, unFillRect)
                pygame.display.update()
                clock.tick(FPS)
        case 7:
            while running:
                for e in pygame.event.get():
                    match e.type:
                        case pygame.QUIT:
                            running = False
                            switch_scene(None)
                        case pygame.KEYDOWN:
                            selectScene += 1
                match selectScene:
                    case 0:
                        TextTXT = fontTXT.render("Valeria: Jan can you for a minute", False, (255, 0, 0))
                    case 1:
                        TextTXT = fontTXT.render("Jan: What the fuck do you want", False, (255, 255, 255))
                    case 2:
                        TextTXT = fontTXT.render('Valeria: We have little fucking questions for you', False,
                                                 (255, 0, 0))
                    case 3:
                        isVisibleScene = True
                        backImage = pygame.image.load('Sprite/scene/2/1.png').convert_alpha()
                        backImage = pygame.transform.smoothscale(backImage, (750, 650))
                        TextTXT = fontTXT.render("Jan: So on and what questions do you have for me don't be afraid "
                                                 "what is my dick size ?", False, (255, 255, 255))
                    case 4:
                        backImage = pygame.image.load('Sprite/scene/2/2.png').convert_alpha()
                        backImage = pygame.transform.smoothscale(backImage, (850, 650))
                        TextTXT = fontTXT.render("Ioann: we are not interested in it", False, (0, 255, 0))
                    case 5:
                        backImage = pygame.image.load('Sprite/scene/2/2.png').convert_alpha()
                        backImage = pygame.transform.smoothscale(backImage, (850, 650))
                        TextTXT = fontTXT.render('Valeria: In addition, we know that you still have it small', False,
                                                 (255, 0, 0))
                    case 6:
                        backImage = pygame.image.load('Sprite/scene/2/1.png').convert_alpha()
                        backImage = pygame.transform.smoothscale(backImage, (750, 650))
                        TextTXT = fontTXT.render('Jan: Bitch', False, (255, 255, 255))
                    case 7:
                        backImage = pygame.image.load('Sprite/scene/2/2.png').convert_alpha()
                        backImage = pygame.transform.smoothscale(backImage, (850, 650))
                        TextTXT = fontTXT.render("Valeria: Say you've heard of the virus right?", False,
                                                 (255, 0, 0))
                    case 8:
                        backImage = pygame.image.load('Sprite/scene/2/1.png').convert_alpha()
                        backImage = pygame.transform.smoothscale(backImage, (750, 650))
                        TextTXT = fontTXT.render('Jan: Well, yes, and that I even know how it consists', False,
                                                 (255, 255, 255))
                    case 9:
                        backImage = pygame.image.load('Sprite/scene/2/2.png').convert_alpha()
                        backImage = pygame.transform.smoothscale(backImage, (850, 650))
                        TextTXT = fontTXT.render('Ioann: yea fag got caught', False,
                                                 (0, 255, 0))
                    case 9:
                        backImage = pygame.image.load('Sprite/scene/2/4.png').convert_alpha()
                        backImage = pygame.transform.smoothscale(backImage, (750, 650))
                        TextTXT = fontTXT.render('Jan: And why did I get caught', False,
                                                 (255, 255, 255))
                    case 10:
                        isVisibleScene = False
                        backImage = pygame.image.load('Sprite/scene/2/3.png').convert_alpha()
                        backImage = pygame.transform.smoothscale(backImage, (850, 650))
                        TextTXT = fontTXT.render('...', False,
                                                 (0, 0, 255))
                    case 11:
                        isVisibleScene = True
                        backImage = pygame.image.load('Sprite/scene/2/3.png').convert_alpha()
                        backImage = pygame.transform.smoothscale(backImage, (850, 650))
                        TextTXT = fontTXT.render('Valeria: We think that it was you who created or participated in '
                                                 'the creation of the virus', False,
                                                 (255, 0, 0))
                    case 12:
                        backImage = pygame.image.load('Sprite/scene/2/3.png').convert_alpha()
                        backImage = pygame.transform.smoothscale(backImage, (850, 650))
                        TextTXT = fontTXT.render('Valeria: After all, how do you know what it consists of', False,
                                                 (255, 0, 0))
                    case 13:
                        backImage = pygame.image.load('Sprite/scene/2/1.png').convert_alpha()
                        backImage = pygame.transform.smoothscale(backImage, (750, 650))
                        TextTXT = fontTXT.render('Jan: Oh fuck', False,
                                                 (255, 255, 255))
                    case 14:
                        backImage = pygame.image.load('Sprite/scene/2/4.png').convert_alpha()
                        backImage = pygame.transform.smoothscale(backImage, (750, 650))
                        TextTXT = fontTXT.render('Jan: You are fucked I fucking studied it because I work in a '
                                                 'laboratory, you are fuckers', False,
                                                 (255, 255, 255))

                    case 15:
                        backImage = pygame.image.load('Sprite/scene/2/2.png').convert_alpha()
                        backImage = pygame.transform.smoothscale(backImage, (850, 650))
                        TextTXT = fontTXT.render('Ioann, Valeria: Oh', False,
                                                 (255, 255, 0))
                    case 16:
                        backImage = pygame.image.load('Sprite/scene/2/2.png').convert_alpha()
                        backImage = pygame.transform.smoothscale(backImage, (850, 650))
                        TextTXT = fontTXT.render('Valeria: Forgive us, we somehow did not think', False,
                                                 (255, 0, 0))
                    case 17:
                        backImage = pygame.image.load('Sprite/scene/2/4.png').convert_alpha()
                        backImage = pygame.transform.smoothscale(backImage, (750, 650))
                        TextTXT = fontTXT.render('Jan: Fucking asphalters', False,
                                                 (255, 255, 255))
                    case 18:
                        isUnFill = True
                        selectScene = 19

                match isUnFill:
                    case True:
                        match FrameUnFill:
                            case 95:
                                switch_scene(sceneGame)
                                running = False
                        alphaUn += 3
                        unFillImage.set_alpha(alphaUn)
                        FrameUnFill += 1
                sc.fill((0, 0, 0))
                match isVisibleScene:
                    case True:
                        sc.blit(backImage, backImageRect)
                sc.blit(TextTXT, TextRect)
                sc.blit(unFillImage, unFillRect)
                pygame.display.update()
                clock.tick(FPS)
        case 10:
            while running:
                for e in pygame.event.get():
                    match e.type:
                        case pygame.QUIT:
                            running = False
                            switch_scene(None)
                        case pygame.KEYDOWN:
                            selectScene += 1
                match selectScene:
                    case 0:
                        TextTXT = fontTXT.render("Valeria: pour vodka", False, (155, 155, 155))
                    case 1:
                        TextTXT = fontTXT.render("Bartender: Will Be Done", False, (0, 0, 0))
                    case 2:
                        TextTXT = fontTXT.render('Ioann: Lera, you cant drink vodka ..', False,
                                                 (0, 255, 0))
                    case 3:
                        isVisibleScene = True
                        backImage = pygame.image.load('Sprite/scene/3/1.png').convert_alpha()
                        backImage = pygame.transform.scale(backImage, (650, 650))
                        TextTXT = fontTXT.render("Valeria: listen to me at all fuck now", False, (155, 155, 155))
                    case 4:
                        backImage = pygame.image.load('Sprite/scene/3/1.png').convert_alpha()
                        backImage = pygame.transform.scale(backImage, (650, 650))
                        TextTXT = fontTXT.render("Ioann: I understand everything but you can calm down", False, (0, 255, 0))
                    case 5:
                        backImage = pygame.image.load('Sprite/scene/3/1.png').convert_alpha()
                        backImage = pygame.transform.scale(backImage, (650, 650))
                        TextTXT = fontTXT.render('Valeria: I cant fucking find the scum that decided to kill people', False,
                                                 (155, 155, 155))
                    case 6:
                        backImage = pygame.image.load('Sprite/scene/3/1.png').convert_alpha()
                        backImage = pygame.transform.scale(backImage, (650, 650))
                        TextTXT = fontTXT.render('Valeria: Bitch!', False, (155, 155, 155))
                    case 7:
                        backImage = pygame.image.load('Sprite/scene/3/2.png').convert_alpha()
                        backImage = pygame.transform.scale(backImage, (650, 650))
                        TextTXT = fontTXT.render("Bartender: Look, it's not your fault and you shouldn't blame yourself.", False,
                                                 (0, 0, 0))
                    case 8:
                        backImage = pygame.image.load('Sprite/scene/3/2.png').convert_alpha()
                        backImage = pygame.transform.scale(backImage, (650, 650))
                        TextTXT = fontTXT.render("Ioann: Lera, that's just how it is.", False,
                                                 (0, 255, 0))
                    case 9:
                        backImage = pygame.image.load('Sprite/scene/3/2.png').convert_alpha()
                        backImage = pygame.transform.scale(backImage, (650, 650))
                        TextTXT = fontTXT.render('Valeria: Eh', False,
                                                 (0, 255, 0))
                    case 10:
                        backImage = pygame.image.load('Sprite/scene/3/3.png').convert_alpha()
                        backImage = pygame.transform.scale(backImage, (650, 650))
                        TextTXT = fontTXT.render('...', False,
                                                 (0, 0, 0))
                    case 11:
                        backImage = pygame.image.load('Sprite/scene/3/3.png').convert_alpha()
                        backImage = pygame.transform.scale(backImage, (650, 650))
                        TextTXT = fontTXT.render("Valeria: Maybe we'll still visit QWERTY", False,
                                                 (155, 155, 155))
                    case 12:
                        backImage = pygame.image.load('Sprite/scene/3/3.png').convert_alpha()
                        backImage = pygame.transform.scale(backImage, (650, 650))
                        TextTXT = fontTXT.render('Ioann: Mmmm', False,
                                                 (0, 255, 0))
                    case 13:
                        backImage = pygame.image.load('Sprite/scene/3/3.png').convert_alpha()
                        backImage = pygame.transform.scale(backImage, (650, 650))
                        TextTXT = fontTXT.render("Ioann: Okay, let's just keep you calm.", False,
                                                 (0, 255, 0))
                    case 14:
                        backImage = pygame.image.load('Sprite/scene/3/3.png').convert_alpha()
                        backImage = pygame.transform.scale(backImage, (650, 650))
                        TextTXT = fontTXT.render("Ioann: Anyway, I don't think it's him.", False,
                                                 (0, 255, 0))
                    case 15:
                        backImage = pygame.image.load('Sprite/scene/3/4.png').convert_alpha()
                        backImage = pygame.transform.scale(backImage, (650, 650))
                        TextTXT = fontTXT.render("Ioann: Let's drink quickly and let's go", False,
                                                 (0, 255, 0))

                    case 16:
                        backImage = pygame.image.load('Sprite/scene/3/4.png').convert_alpha()
                        backImage = pygame.transform.scale(backImage, (650, 650))
                        TextTXT = fontTXT.render("Valeria: yeah... ", False,
                                                     (155, 155, 155))
                    case 17:
                        backImage = pygame.image.load('Sprite/scene/3/4.png').convert_alpha()
                        backImage = pygame.transform.scale(backImage, (650, 650))
                        TextTXT = fontTXT.render("Valeria: let's see", False,
                                                 (155, 155, 155))
                    case 18:
                        backImage = pygame.image.load('Sprite/scene/3/4.png').convert_alpha()
                        backImage = pygame.transform.scale(backImage, (750, 750))
                        TextTXT = fontTXT.render('Bartender: Guys, I ask you to kill the one who decided to kill all people like this', False,
                                                 (0, 0, 0))
                    case 19:
                        isUnFill = True
                        selectScene = 20

                match isUnFill:
                    case True:
                        match FrameUnFill:
                            case 95:
                                switch_scene(sceneGame)
                                running = False
                        alphaUn += 3
                        unFillImage.set_alpha(alphaUn)
                        FrameUnFill += 1
                sc.fill((255, 255, 255))
                match isVisibleScene:
                    case True:
                        sc.blit(backImage, backImageRect)
                sc.blit(TextTXT, TextRect)
                sc.blit(unFillImage, unFillRect)
                pygame.display.update()
                clock.tick(FPS)
        case 14:
            while running:
                for e in pygame.event.get():
                    match e.type:
                        case pygame.QUIT:
                            running = False
                            switch_scene(None)
                        case pygame.KEYDOWN:
                            selectScene += 1
                match selectScene:
                    case 0:
                        TextTXT = fontTXT.render("Valeria: So where is his apartment?", False, (155, 155, 155))
                    case 1:
                        TextTXT = fontTXT.render("Ioann: Here's, the next one", False, (0, 0, 0))
                    case 2:
                        TextTXT = fontTXT.render('Valeria: yes', False,
                                                 (0, 255, 0))
                    case 3:
                        isVisibleScene = True
                        backImage = pygame.image.load('Sprite/scene/4/1.png').convert_alpha()
                        backImage = pygame.transform.scale(backImage, (650, 650))
                        TextTXT = fontTXT.render("Ioann: Come on, just you", False, (155, 155, 155))
                    case 4:
                        backImage = pygame.image.load('Sprite/scene/4/1.png').convert_alpha()
                        backImage = pygame.transform.scale(backImage, (650, 650))
                        TextTXT = fontTXT.render("Valeria: Why should I knock?", False, (0, 255, 0))
                    case 5:
                        backImage = pygame.image.load('Sprite/scene/4/1.png').convert_alpha()
                        backImage = pygame.transform.scale(backImage, (650, 650))
                        TextTXT = fontTXT.render('Ioann: Well, you are our master to knock', False,
                                                 (155, 155, 155))
                    case 6:
                        isVisibleScene = False
                        backImage = pygame.image.load('Sprite/scene/4/3.png').convert_alpha()
                        backImage = pygame.transform.scale(backImage, (650, 650))
                        TextTXT = fontTXT.render('...', False, (155, 155, 155))
                    case 7:
                        TextTXT = fontTXT.render("@#$%: Yes Yes! I'm already opening", False,
                                                 (0, 0, 0))
                    case 8:
                        TextTXT = fontTXT.render("@#$%: Fuck oh shit", False,
                                                 (0, 255, 0))
                    case 9:
                        TextTXT = fontTXT.render('Valeria: hello bitch milf', False,
                                                 (0, 255, 0))
                    case 10:
                        isVisibleScene = True
                        TextTXT = fontTXT.render('Ioann: Hello Adriana!', False,
                                                 (0, 0, 0))
                    case 11:
                        TextTXT = fontTXT.render("Adriana 0: Hello!", False,
                                                 (155, 155, 155))
                    case 12:
                        TextTXT = fontTXT.render('Ioann: Lera, dont you want to say hello?', False,
                                                 (0, 255, 0))
                    case 13:
                        backImage = pygame.image.load('Sprite/scene/4/2.png').convert_alpha()
                        backImage = pygame.transform.scale(backImage, (650, 650))
                        TextTXT = fontTXT.render("Valeria: I do not want", False,
                                                 (0, 255, 0))
                    case 14:
                        backImage = pygame.image.load('Sprite/scene/4/3.png').convert_alpha()
                        backImage = pygame.transform.scale(backImage, (650, 650))
                        TextTXT = fontTXT.render("Adriana 0: Listen, what have I done to you?", False,
                                                 (0, 255, 0))
                    case 15:
                        backImage = pygame.image.load('Sprite/scene/4/2.png').convert_alpha()
                        backImage = pygame.transform.scale(backImage, (650, 650))
                        TextTXT = fontTXT.render("Valeria: You know", False,
                                                 (0, 255, 0))

                    case 16:
                        backImage = pygame.image.load('Sprite/scene/4/3.png').convert_alpha()
                        backImage = pygame.transform.scale(backImage, (650, 650))
                        TextTXT = fontTXT.render("Ioann: Girls let's not", False,
                                                     (155, 155, 155))
                    case 17:
                        isVisibleScene = False
                        backImage = pygame.image.load('Sprite/scene/4/4.png').convert_alpha()
                        backImage = pygame.transform.smoothscale(backImage, (850, 650))
                        TextTXT = fontTXT.render("Adriana: Fuck you", False,
                                                 (155, 155, 155))
                    case 18:
                        isVisibleScene = True
                        TextTXT = fontTXT.render('Valeria: Bitch say where is your wimp', False,
                                                 (0, 0, 0))
                    case 19:
                        TextTXT = fontTXT.render('Adriana: He went to look for sister Ioann', False,
                                                 (0, 255, 0))
                    case 20:
                        TextTXT = fontTXT.render('Valeria: What for?', False,
                                                 (0, 255, 0))
                    case 30:
                        isUnFill = True
                        selectScene = 50

                match isUnFill:
                    case True:
                        match FrameUnFill:
                            case 95:
                                switch_scene(sceneGame)
                                running = False
                        alphaUn += 3
                        unFillImage.set_alpha(alphaUn)
                        FrameUnFill += 1
                sc.fill((255, 255, 255))
                match isVisibleScene:
                    case True:
                        sc.blit(backImage, backImageRect)
                sc.blit(TextTXT, TextRect)
                sc.blit(unFillImage, unFillRect)
                pygame.display.update()
                clock.tick(FPS)
def nextLevel():
    global timeSet
    Frame = 0

    continueImage = pygame.image.load('Sprite/UI/Text/Continue/c_1.png').convert_alpha()
    continueImage = pygame.transform.scale(continueImage, (555, 555))
    continueRect = continueImage.get_rect(center=(560, 1))

    timeSet = 60
    isVisibleText = False

    # Text
    FontKey = pygame.font.Font('Font/2.ttf', 55)
    alphaT = 20
    FrameAlpha = 0
    TextKey = FontKey.render('Press Any Key', False, (255, 255, 255))
    TextKey.set_alpha(alphaT)
    TextRect = TextKey.get_rect(center=(RES[0] // 2, 650))

    running = True
    FPS = 60

    isKey = False

    while running:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                switch_scene(None)
                running = False
            if e.type == pygame.KEYDOWN and isKey:
                op.countEnemy = 0
                match op.level:
                    case 1:
                        timeSet = 60
                        isKey = False
                        op.level = 2
                        switch_scene(sceneGame)
                        running = False
                    case 2:
                        if op.player < 5:
                            op.player += 2
                        timeSet = 65
                        isKey = False
                        switch_scene(sceneGame)
                        running = False
                        op.level = 3
                    case 3:
                        if op.player < 5:
                            op.player += 2
                        timeSet = 70
                        isKey = False
                        switch_scene(cutscene)
                        running = False
                        op.level = 4
                    case 4:
                        if op.player < 5:
                            op.player += 2
                        timeSet = 85
                        isKey = False
                        switch_scene(sceneGame)
                        running = False
                        op.level = 5
                    case 5:
                        if op.player < 5:
                            op.player += 2
                        timeSet = 85
                        isKey = False
                        switch_scene(sceneGame)
                        running = False
                        op.level = 6
                    case 6:
                        if op.player < 5:
                            op.player += 2
                        timeSet = 95
                        isKey = False
                        switch_scene(cutscene)
                        running = False
                        op.level = 7
                    case 7:
                        if op.player < 5:
                            op.player += 2
                        timeSet = 105
                        isKey = False
                        switch_scene(sceneGame)
                        running = False
                        op.level = 8
                    case 8:
                        if op.player < 5:
                            op.player += 2
                        timeSet = 105
                        isKey = False
                        switch_scene(sceneGame)
                        running = False
                        op.level = 9
                    case 9:
                        if op.player < 5:
                            op.player += 2
                        timeSet = 125
                        isKey = False
                        switch_scene(cutscene)
                        running = False
                        op.level = 10
                    case 10:
                        if op.player < 5:
                            op.player += 2
                        timeSet = 195
                        isKey = False
                        switch_scene(cutscene)
                        running = False
                        op.level = 11
                    case 11:
                        if op.player < 5:
                            op.player += 2
                        timeSet = 195
                        isKey = False
                        switch_scene(cutscene)
                        running = False
                        op.level = 12
                    case 12:
                        if op.player < 5:
                            op.player += 2
                        timeSet = 195
                        isKey = False
                        switch_scene(cutscene)
                        running = False
                        op.level = 13
                    case 13:
                        if op.player < 5:
                            op.player += 2
                        timeSet = 135
                        isKey = False
                        switch_scene(cutscene)
                        running = False
                        op.level = 14
        if Frame == 90:
            continueImage = pygame.image.load('Sprite/UI/Text/Continue/c_1.png').convert_alpha()
            continueImage = pygame.transform.scale(continueImage, (555, 555))
            Frame = 0

        if Frame == 10:
            continueImage = pygame.image.load('Sprite/UI/Text/Continue/c_2.png').convert_alpha()
            continueImage = pygame.transform.scale(continueImage, (555, 555))
        if Frame == 20:
            continueImage = pygame.image.load('Sprite/UI/Text/Continue/c_3.png').convert_alpha()
            continueImage = pygame.transform.scale(continueImage, (575, 575))
        if Frame == 30:
            continueImage = pygame.image.load('Sprite/UI/Text/Continue/c_4.png').convert_alpha()
            continueImage = pygame.transform.scale(continueImage, (595, 595))
        if Frame == 40:
            continueImage = pygame.image.load('Sprite/UI/Text/Continue/c_5.png').convert_alpha()
            continueImage = pygame.transform.scale(continueImage, (575, 575))
        if Frame == 50:
            continueImage = pygame.image.load('Sprite/UI/Text/Continue/c_6.png').convert_alpha()
            continueImage = pygame.transform.scale(continueImage, (555, 555))
        if Frame == 60:
            continueImage = pygame.image.load('Sprite/UI/Text/Continue/c_7.png').convert_alpha()
            continueImage = pygame.transform.scale(continueImage, (575, 575))
        if Frame == 70:
            continueImage = pygame.image.load('Sprite/UI/Text/Continue/c_8.png').convert_alpha()
            continueImage = pygame.transform.scale(continueImage, (595, 595))
        if Frame == 80:
            continueImage = pygame.image.load('Sprite/UI/Text/Continue/c_1.png').convert_alpha()
            continueImage = pygame.transform.scale(continueImage, (575, 575))
        Frame += 1

        if continueRect.y < 195:
            continueRect.y += 5
        else:
            isKey = True
            isVisibleText = True
        match FrameAlpha:
            case 65:
                alphaT = 20
                FrameAlpha = 0
        alphaT += 3
        TextKey.set_alpha(alphaT)
        FrameAlpha += 1

        sc.fill((0, 0, 0))
        clock.tick(FPS)
        sc.blit(continueImage, continueRect)
        match isVisibleText:
            case True:
                sc.blit(TextKey, TextRect)
        pygame.display.update()


t2 = None

touchButton = pygame.mixer.Sound('Audio/SFX/11.wav')


def mainMenu():
    global characterSprite
    WHITE = (255, 255, 255)
    YELLOW = (255, 255, 0)

    # Text
    StartGameTXT = font1.render('Start Game', False, WHITE)
    StartRECT = StartGameTXT.get_rect(center=(265, 435))
    ScoreTXT = font1.render('Score', False, WHITE)
    ScoreRECT = ScoreTXT.get_rect(center=(465, 525))
    ShopTXT = font1.render('Shop', False, WHITE)
    ShopRECT = ShopTXT.get_rect(center=(645, 325))

    # Frame
    Frame1 = pygame.image.load('Sprite/UI/Frame2.png').convert_alpha()
    Frame1 = pygame.transform.scale(Frame1, (188, 128))
    Frame1Rect = Frame1.get_rect(center=(263, 435))

    Frame2 = pygame.image.load('Sprite/UI/Frame2.png').convert_alpha()
    Frame2 = pygame.transform.scale(Frame2, (127, 128))
    Frame2Rect = Frame2.get_rect(center=(463, 525))

    Frame3 = pygame.image.load('Sprite/UI/Frame2.png').convert_alpha()
    Frame3 = pygame.transform.scale(Frame3, (118, 119))
    Frame3Rect = Frame3.get_rect(center=(643, 325))

    # KeySprite
    keyZ = pygame.image.load('Sprite/UI/Key/Z/Z_1.png').convert_alpha()
    keyZ = pygame.transform.scale(keyZ, (36, 36))
    keyZRect = keyZ.get_rect(center=(260, 385))

    FrameKey = 0
    pMenu = player.PlayerMenu(590, 690, 5)

    menuBack = pygame.image.load('Sprite/UI/menuBack.png').convert_alpha()
    menuBack = pygame.transform.scale(menuBack, (RES[0]+20, RES[1]+20))
    menuRect = menuBack.get_rect(center=(RES[0]//2, RES[1]//2))

    running = True
    FPS = 60
    createUnFill('Sprite/UI/Fill/1.png', 1500, 1300)
    while running:
        for e in pygame.event.get():
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_UP:
                    player.isUp = True
                elif e.key == pygame.K_DOWN:
                    player.isDown = True
                elif e.key == pygame.K_LEFT:
                    player.isLeft = True
                elif e.key == pygame.K_RIGHT:
                    player.isRight = True
                if e.key == pygame.K_z and Frame1Rect.collidepoint(pMenu.rect.center):
                    touchButton.play()
                    running = False
                    switch_scene(selectMode)
                if e.key == pygame.K_z and Frame2Rect.collidepoint(pMenu.rect.center):
                    touchButton.play()
                    running = False
                    switch_scene(scoreMenu)
                if e.key == pygame.K_z and Frame3Rect.collidepoint(pMenu.rect.center):
                    touchButton.play()
                    running = False
                    switch_scene(shop)
            if e.type == pygame.KEYUP:
                if e.key == pygame.K_UP:
                    player.isUp = False
                elif e.key == pygame.K_DOWN:
                    player.isDown = False
                elif e.key == pygame.K_LEFT:
                    player.isLeft = False
                elif e.key == pygame.K_RIGHT:
                    player.isRight = False
        if Frame1Rect.collidepoint(pMenu.rect.center):
            StartGameTXT = font1.render('Start Game', False, YELLOW)
            match FrameKey:
                case 86:
                    keyZ = pygame.image.load('Sprite/UI/Key/Z/Z_1.png').convert_alpha()
                    keyZ = pygame.transform.scale(keyZ, (36, 36))
                    keyZRect = keyZ.get_rect(center=(260, 385))
                    FrameKey = 0
                case 5:
                    keyZ = pygame.image.load('Sprite/UI/Key/Z/Z_2.png').convert_alpha()
                    keyZ = pygame.transform.scale(keyZ, (36, 36))
                    keyZRect = keyZ.get_rect(center=(260, 385))
                case 10:
                    keyZ = pygame.image.load('Sprite/UI/Key/Z/Z_3.png').convert_alpha()
                    keyZ = pygame.transform.scale(keyZ, (36, 36))
                    keyZRect = keyZ.get_rect(center=(260, 385))
                case 15:
                    keyZ = pygame.image.load('Sprite/UI/Key/Z/Z_4.png').convert_alpha()
                    keyZ = pygame.transform.scale(keyZ, (36, 36))
                    keyZRect = keyZ.get_rect(center=(260, 385))
                case 20:
                    keyZ = pygame.image.load('Sprite/UI/Key/Z/Z_5.png').convert_alpha()
                    keyZ = pygame.transform.scale(keyZ, (36, 36))
                    keyZRect = keyZ.get_rect(center=(260, 385))
                case 25:
                    keyZ = pygame.image.load('Sprite/UI/Key/Z/Z_6.png').convert_alpha()
                    keyZ = pygame.transform.scale(keyZ, (36, 36))
                    keyZRect = keyZ.get_rect(center=(260, 385))
                case 30:
                    keyZ = pygame.image.load('Sprite/UI/Key/Z/Z_7.png').convert_alpha()
                    keyZ = pygame.transform.scale(keyZ, (36, 36))
                    keyZRect = keyZ.get_rect(center=(260, 385))
                case 35:
                    keyZ = pygame.image.load('Sprite/UI/Key/Z/Z_8.png').convert_alpha()
                    keyZ = pygame.transform.scale(keyZ, (36, 36))
                    keyZRect = keyZ.get_rect(center=(260, 385))
                case 40:
                    keyZ = pygame.image.load('Sprite/UI/Key/Z/Z_9.png').convert_alpha()
                    keyZ = pygame.transform.scale(keyZ, (36, 36))
                    keyZRect = keyZ.get_rect(center=(260, 385))
                case 45:
                    keyZ = pygame.image.load('Sprite/UI/Key/Z/Z_10.png').convert_alpha()
                    keyZ = pygame.transform.scale(keyZ, (36, 36))
                    keyZRect = keyZ.get_rect(center=(260, 385))
                case 50:
                    keyZ = pygame.image.load('Sprite/UI/Key/Z/Z_11.png').convert_alpha()
                    keyZ = pygame.transform.scale(keyZ, (36, 36))
                    keyZRect = keyZ.get_rect(center=(260, 385))
                case 55:
                    keyZ = pygame.image.load('Sprite/UI/Key/Z/Z_12.png').convert_alpha()
                    keyZ = pygame.transform.scale(keyZ, (36, 36))
                    keyZRect = keyZ.get_rect(center=(260, 385))
                case 60:
                    keyZ = pygame.image.load('Sprite/UI/Key/Z/Z_13.png').convert_alpha()
                    keyZ = pygame.transform.scale(keyZ, (36, 36))
                    keyZRect = keyZ.get_rect(center=(260, 385))
                case 65:
                    keyZ = pygame.image.load('Sprite/UI/Key/Z/Z_14.png').convert_alpha()
                    keyZ = pygame.transform.scale(keyZ, (36, 36))
                    keyZRect = keyZ.get_rect(center=(260, 385))
                case 70:
                    keyZ = pygame.image.load('Sprite/UI/Key/Z/Z_15.png').convert_alpha()
                    keyZ = pygame.transform.scale(keyZ, (36, 36))
                    keyZRect = keyZ.get_rect(center=(260, 385))
                case 75:
                    keyZ = pygame.image.load('Sprite/UI/Key/Z/Z_16.png').convert_alpha()
                    keyZ = pygame.transform.scale(keyZ, (36, 36))
                    keyZRect = keyZ.get_rect(center=(260, 385))
                case 80:
                    keyZ = pygame.image.load('Sprite/UI/Key/Z/Z_17.png').convert_alpha()
                    keyZ = pygame.transform.scale(keyZ, (36, 36))
                    keyZRect = keyZ.get_rect(center=(260, 385))
                case 85:
                    keyZ = pygame.image.load('Sprite/UI/Key/Z/Z_6.png').convert_alpha()
                    keyZ = pygame.transform.scale(keyZ, (36, 36))
                    keyZRect = keyZ.get_rect(center=(260, 385))
            FrameKey += 1
        else:
            StartGameTXT = font1.render('Start Game', False, WHITE)
        if Frame2Rect.collidepoint(pMenu.rect.center):
            ScoreTXT = font1.render('Score', False, YELLOW)
            match FrameKey:
                case 86:
                    keyZ = pygame.image.load('Sprite/UI/Key/Z/Z_1.png').convert_alpha()
                    keyZ = pygame.transform.scale(keyZ, (36, 36))
                    keyZRect = keyZ.get_rect(center=(460, 470))
                    FrameKey = 0
                case 5:
                    keyZ = pygame.image.load('Sprite/UI/Key/Z/Z_2.png').convert_alpha()
                    keyZ = pygame.transform.scale(keyZ, (36, 36))
                    keyZRect = keyZ.get_rect(center=(460, 470))
                case 10:
                    keyZ = pygame.image.load('Sprite/UI/Key/Z/Z_3.png').convert_alpha()
                    keyZ = pygame.transform.scale(keyZ, (36, 36))
                    keyZRect = keyZ.get_rect(center=(460, 470))
                case 15:
                    keyZ = pygame.image.load('Sprite/UI/Key/Z/Z_4.png').convert_alpha()
                    keyZ = pygame.transform.scale(keyZ, (36, 36))
                    keyZRect = keyZ.get_rect(center=(460, 470))
                case 20:
                    keyZ = pygame.image.load('Sprite/UI/Key/Z/Z_5.png').convert_alpha()
                    keyZ = pygame.transform.scale(keyZ, (36, 36))
                    keyZRect = keyZ.get_rect(center=(460, 470))
                case 25:
                    keyZ = pygame.image.load('Sprite/UI/Key/Z/Z_6.png').convert_alpha()
                    keyZ = pygame.transform.scale(keyZ, (36, 36))
                    keyZRect = keyZ.get_rect(center=(460, 470))
                case 30:
                    keyZ = pygame.image.load('Sprite/UI/Key/Z/Z_7.png').convert_alpha()
                    keyZ = pygame.transform.scale(keyZ, (36, 36))
                    keyZRect = keyZ.get_rect(center=(460, 470))
                case 35:
                    keyZ = pygame.image.load('Sprite/UI/Key/Z/Z_8.png').convert_alpha()
                    keyZ = pygame.transform.scale(keyZ, (36, 36))
                    keyZRect = keyZ.get_rect(center=(460, 470))
                case 40:
                    keyZ = pygame.image.load('Sprite/UI/Key/Z/Z_9.png').convert_alpha()
                    keyZ = pygame.transform.scale(keyZ, (36, 36))
                    keyZRect = keyZ.get_rect(center=(460, 470))
                case 45:
                    keyZ = pygame.image.load('Sprite/UI/Key/Z/Z_10.png').convert_alpha()
                    keyZ = pygame.transform.scale(keyZ, (36, 36))
                    keyZRect = keyZ.get_rect(center=(460, 470))
                case 50:
                    keyZ = pygame.image.load('Sprite/UI/Key/Z/Z_11.png').convert_alpha()
                    keyZ = pygame.transform.scale(keyZ, (36, 36))
                    keyZRect = keyZ.get_rect(center=(460, 470))
                case 55:
                    keyZ = pygame.image.load('Sprite/UI/Key/Z/Z_12.png').convert_alpha()
                    keyZ = pygame.transform.scale(keyZ, (36, 36))
                    keyZRect = keyZ.get_rect(center=(460, 470))
                case 60:
                    keyZ = pygame.image.load('Sprite/UI/Key/Z/Z_13.png').convert_alpha()
                    keyZ = pygame.transform.scale(keyZ, (36, 36))
                    keyZRect = keyZ.get_rect(center=(460, 470))
                case 65:
                    keyZ = pygame.image.load('Sprite/UI/Key/Z/Z_14.png').convert_alpha()
                    keyZ = pygame.transform.scale(keyZ, (36, 36))
                    keyZRect = keyZ.get_rect(center=(460, 470))
                case 70:
                    keyZ = pygame.image.load('Sprite/UI/Key/Z/Z_15.png').convert_alpha()
                    keyZ = pygame.transform.scale(keyZ, (36, 36))
                    keyZRect = keyZ.get_rect(center=(460, 470))
                case 75:
                    keyZ = pygame.image.load('Sprite/UI/Key/Z/Z_16.png').convert_alpha()
                    keyZ = pygame.transform.scale(keyZ, (36, 36))
                    keyZRect = keyZ.get_rect(center=(460, 470))
                case 80:
                    keyZ = pygame.image.load('Sprite/UI/Key/Z/Z_17.png').convert_alpha()
                    keyZ = pygame.transform.scale(keyZ, (36, 36))
                    keyZRect = keyZ.get_rect(center=(460, 470))
                case 85:
                    keyZ = pygame.image.load('Sprite/UI/Key/Z/Z_6.png').convert_alpha()
                    keyZ = pygame.transform.scale(keyZ, (36, 36))
                    keyZRect = keyZ.get_rect(center=(460, 470))
            FrameKey += 1
        else:
            ScoreTXT = font1.render('Score', False, WHITE)
        if Frame3Rect.collidepoint(pMenu.rect.center):
            ShopTXT = font1.render('Shop', False, YELLOW)
            match FrameKey:
                case 86:
                    keyZ = pygame.image.load('Sprite/UI/Key/Z/Z_1.png').convert_alpha()
                    keyZ = pygame.transform.scale(keyZ, (36, 36))
                    keyZRect = keyZ.get_rect(center=(643, 275))
                    FrameKey = 0
                case 5:
                    keyZ = pygame.image.load('Sprite/UI/Key/Z/Z_2.png').convert_alpha()
                    keyZ = pygame.transform.scale(keyZ, (36, 36))
                    keyZRect = keyZ.get_rect(center=(643, 275))
                case 10:
                    keyZ = pygame.image.load('Sprite/UI/Key/Z/Z_3.png').convert_alpha()
                    keyZ = pygame.transform.scale(keyZ, (36, 36))
                    keyZRect = keyZ.get_rect(center=(643, 275))
                case 15:
                    keyZ = pygame.image.load('Sprite/UI/Key/Z/Z_4.png').convert_alpha()
                    keyZ = pygame.transform.scale(keyZ, (36, 36))
                    keyZRect = keyZ.get_rect(center=(643, 275))
                case 20:
                    keyZ = pygame.image.load('Sprite/UI/Key/Z/Z_5.png').convert_alpha()
                    keyZ = pygame.transform.scale(keyZ, (36, 36))
                    keyZRect = keyZ.get_rect(center=(643, 275))
                case 25:
                    keyZ = pygame.image.load('Sprite/UI/Key/Z/Z_6.png').convert_alpha()
                    keyZ = pygame.transform.scale(keyZ, (36, 36))
                    keyZRect = keyZ.get_rect(center=(643, 275))
                case 30:
                    keyZ = pygame.image.load('Sprite/UI/Key/Z/Z_7.png').convert_alpha()
                    keyZ = pygame.transform.scale(keyZ, (36, 36))
                    keyZRect = keyZ.get_rect(center=(643, 275))
                case 35:
                    keyZ = pygame.image.load('Sprite/UI/Key/Z/Z_8.png').convert_alpha()
                    keyZ = pygame.transform.scale(keyZ, (36, 36))
                    keyZRect = keyZ.get_rect(center=(643, 275))
                case 40:
                    keyZ = pygame.image.load('Sprite/UI/Key/Z/Z_9.png').convert_alpha()
                    keyZ = pygame.transform.scale(keyZ, (36, 36))
                    keyZRect = keyZ.get_rect(center=(643, 275))
                case 45:
                    keyZ = pygame.image.load('Sprite/UI/Key/Z/Z_10.png').convert_alpha()
                    keyZ = pygame.transform.scale(keyZ, (36, 36))
                    keyZRect = keyZ.get_rect(center=(643, 275))
                case 50:
                    keyZ = pygame.image.load('Sprite/UI/Key/Z/Z_11.png').convert_alpha()
                    keyZ = pygame.transform.scale(keyZ, (36, 36))
                    keyZRect = keyZ.get_rect(center=(643, 275))
                case 55:
                    keyZ = pygame.image.load('Sprite/UI/Key/Z/Z_12.png').convert_alpha()
                    keyZ = pygame.transform.scale(keyZ, (36, 36))
                    keyZRect = keyZ.get_rect(center=(643, 275))
                case 60:
                    keyZ = pygame.image.load('Sprite/UI/Key/Z/Z_13.png').convert_alpha()
                    keyZ = pygame.transform.scale(keyZ, (36, 36))
                    keyZRect = keyZ.get_rect(center=(643, 275))
                case 65:
                    keyZ = pygame.image.load('Sprite/UI/Key/Z/Z_14.png').convert_alpha()
                    keyZ = pygame.transform.scale(keyZ, (36, 36))
                    keyZRect = keyZ.get_rect(center=(643, 275))
                case 70:
                    keyZ = pygame.image.load('Sprite/UI/Key/Z/Z_15.png').convert_alpha()
                    keyZ = pygame.transform.scale(keyZ, (36, 36))
                    keyZRect = keyZ.get_rect(center=(643, 275))
                case 75:
                    keyZ = pygame.image.load('Sprite/UI/Key/Z/Z_16.png').convert_alpha()
                    keyZ = pygame.transform.scale(keyZ, (36, 36))
                    keyZRect = keyZ.get_rect(center=(643, 275))
                case 80:
                    keyZ = pygame.image.load('Sprite/UI/Key/Z/Z_17.png').convert_alpha()
                    keyZ = pygame.transform.scale(keyZ, (36, 36))
                    keyZRect = keyZ.get_rect(center=(643, 275))
                case 85:
                    keyZ = pygame.image.load('Sprite/UI/Key/Z/Z_6.png').convert_alpha()
                    keyZ = pygame.transform.scale(keyZ, (36, 36))
                    keyZRect = keyZ.get_rect(center=(643, 275))
            FrameKey += 1
        else:
            ShopTXT = font1.render('Shop', False, WHITE)

        sc.fill((33, 2, 43))
        sc.blit(menuBack, menuRect)
        sc.blit(StartGameTXT, StartRECT)
        sc.blit(ScoreTXT, ScoreRECT)
        sc.blit(ShopTXT, ShopRECT)
        sc.blit(Frame1, Frame1Rect)
        sc.blit(Frame2, Frame2Rect)
        sc.blit(Frame3, Frame3Rect)
        sc.blit(keyZ, keyZRect)
        sc.blit(pMenu.image, pMenu.rect)
        alphaG.draw(sc)
        pygame.display.update()
        clock.tick(FPS)
        pMenu.move()
        alphaG.update()


def selectMode():
    global isScore
    running = True
    FPS = 60

    pMove = player.PlayerMenu(500, 660, 8)

    # UnFill
    alphaUn = 250
    FrameUnFill = 0
    isUnFillUpdate = True
    unFillImage = pygame.image.load('Sprite/UI/Fill/2.png').convert_alpha()
    unFillImage = pygame.transform.scale(unFillImage, (RES[0], RES[1]))
    unFillImage.set_alpha(alphaUn)
    unFillRect = unFillImage.get_rect(center=(RES[0] // 2, RES[1] // 2))

    # Image
    storyMode = pygame.image.load('Sprite/UI/selectMode/story.png').convert_alpha()
    storyMode = pygame.transform.scale(storyMode, (269, 269))
    storyModeRect = storyMode.get_rect(center=(300, 350))

    scoreMode = pygame.image.load('Sprite/UI/selectMode/score.png').convert_alpha()
    scoreMode = pygame.transform.scale(scoreMode, (269, 269))
    scoreModeRect = scoreMode.get_rect(center=(810, 350))

    # Text
    FontT = pygame.font.Font('Font/2.ttf', 80)
    selectText = FontT.render('Select Mode', False, (255, 255, 255))
    selectTextRect = selectText.get_rect(center=(550, 110))

    Back = font1.render('Back', False, (255, 255, 255))
    backRect = Back.get_rect(center=(990, 870))

    Frame1 = pygame.image.load('Sprite/UI/Frame2.png').convert_alpha()
    Frame1 = pygame.transform.scale(Frame1, (147, 108))
    Frame1Rect = Frame1.get_rect(center=(985, 870))

    while running:
        for e in pygame.event.get():
            match e.type:
                case pygame.QUIT:
                    running = False
                    switch_scene(None)
                case pygame.KEYDOWN:
                    if e.key == pygame.K_UP:
                        player.isUp = True
                    elif e.key == pygame.K_DOWN:
                        player.isDown = True
                    elif e.key == pygame.K_LEFT:
                        player.isLeft = True
                    elif e.key == pygame.K_RIGHT:
                        player.isRight = True
                    if e.key == pygame.K_z and storyModeRect.collidepoint(pMove.rect.center):
                        touchButton.play()
                        running = False
                        isScore = False
                        switch_scene(selectCharacter)
                    if e.key == pygame.K_z and scoreModeRect.collidepoint(pMove.rect.center):
                        touchButton.play()
                        running = False
                        isScore = True
                        switch_scene(selectCharacter)
                    if e.key == pygame.K_z and Frame1Rect.collidepoint(pMove.rect.center):
                        running = False
                        switch_scene(mainMenu)
                case pygame.KEYUP:
                    if e.key == pygame.K_UP:
                        player.isUp = False
                    elif e.key == pygame.K_DOWN:
                        player.isDown = False
                    elif e.key == pygame.K_LEFT:
                        player.isLeft = False
                    elif e.key == pygame.K_RIGHT:
                        player.isRight = False
        if Frame1Rect.collidepoint(pMove.rect.center):
            Back = font1.render('Back', False, (255, 255, 0))
        else:
            Back = font1.render('Back', False, (255, 255, 255))
        match FrameUnFill:
            case 25:
                isUnFillUpdate = False
        match isUnFillUpdate:
            case True:
                alphaUn -= 14
                unFillImage.set_alpha(alphaUn)
                FrameUnFill += 1
        sc.fill((10, 2, 14))
        clock.tick(FPS)
        sc.blit(storyMode, storyModeRect)
        sc.blit(scoreMode, scoreModeRect)
        sc.blit(selectText, selectTextRect)
        sc.blit(Back, backRect)
        sc.blit(Frame1, Frame1Rect)
        sc.blit(pMove.image, pMove.rect)
        match isUnFillUpdate:
            case True:
                sc.blit(unFillImage, unFillRect)
        pygame.display.update()
        pMove.move()


isScore = False


def selectCharacter():
    global characterSprite, t2, isScore
    running = True
    FPS = 60

    pCharacter = player.PlayerMenu(550, 670, 6)

    # UnFill
    alphaUn = 250
    FrameUnFill = 0
    isUnFillUpdate = True
    unFillImage = pygame.image.load('Sprite/UI/Fill/2.png').convert_alpha()
    unFillImage = pygame.transform.scale(unFillImage.convert_alpha(), (RES[0], RES[1]))
    unFillImage.set_alpha(alphaUn)
    unFillRect = unFillImage.get_rect(center=(RES[0] // 2, RES[1] // 2))

    # Character Image
    IoannImage = pygame.image.load('Sprite/UI/selectCharacter/1.png').convert_alpha()
    IoannImage = pygame.transform.scale(IoannImage.convert_alpha(), (278, 278))
    IoannRect = IoannImage.get_rect(center=(300, 350))

    ValeriaImage = pygame.image.load('Sprite/UI/selectCharacter/2.png').convert_alpha()
    ValeriaImage = pygame.transform.scale(ValeriaImage.convert_alpha(), (278, 278))
    ValeriaRect = ValeriaImage.get_rect(center=(810, 350))

    # Text
    FontT = pygame.font.Font('Font/3.ttf', 40)
    selectText = FontT.render('Select Character', False, (255, 255, 255))
    selectTextRect = selectText.get_rect(center=(560, 110))

    FontC = pygame.font.Font('Font/2.ttf', 45)
    IoannTXT = FontC.render('Ioann', False, (0, 255, 5))
    IoannTXTrect = IoannTXT.get_rect(center=(300, 525))

    ValeriaTXT = FontC.render('Valeria', False, (255, 0, 5))
    ValeriaTXTrect = ValeriaTXT.get_rect(center=(810, 525))

    Back = font1.render('Back', False, (255, 255, 255))
    backRect = Back.get_rect(center=(990, 870))

    Frame1 = pygame.image.load('Sprite/UI/Frame2.png').convert_alpha()
    Frame1 = pygame.transform.scale(Frame1, (147, 108))
    Frame1Rect = Frame1.get_rect(center=(985, 870))

    while running:
        for e in pygame.event.get():
            match e.type:
                case pygame.QUIT:
                    running = False
                    switch_scene(None)
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_UP:
                    player.isUp = True
                elif e.key == pygame.K_DOWN:
                    player.isDown = True
                elif e.key == pygame.K_LEFT:
                    player.isLeft = True
                elif e.key == pygame.K_RIGHT:
                    player.isRight = True
                match isScore:
                    case False:
                        if e.key == pygame.K_z and IoannRect.collidepoint(pCharacter.rect.center):
                            touchButton.play()
                            op.SCORE = 0
                            op.HISCORE = 0
                            characterSprite = 'Sprite/Player/Ioann.png'
                            running = False
                            t2 = threading.Thread(target=switch_scene(sceneGame)).start()
                        if e.key == pygame.K_z and ValeriaRect.collidepoint(pCharacter.rect.center):
                            touchButton.play()
                            op.SCORE = 0
                            op.HISCORE = 0
                            characterSprite = 'Sprite/Player/Valeria.png'
                            running = False
                            t2 = threading.Thread(target=switch_scene(sceneGame)).start()
                    case True:
                        if e.key == pygame.K_z and IoannRect.collidepoint(pCharacter.rect.center):
                            op.SCORE = 0
                            op.HISCORE = 0
                            characterSprite = 'Sprite/Player/Ioann.png'
                            running = False
                            t2 = threading.Thread(target=switch_scene(sceneScoreMode)).start()
                        if e.key == pygame.K_z and ValeriaRect.collidepoint(pCharacter.rect.center):
                            op.SCORE = 0
                            op.HISCORE = 0
                            characterSprite = 'Sprite/Player/Valeria.png'
                            running = False
                            t2 = threading.Thread(target=switch_scene(sceneScoreMode)).start()
                if e.key == pygame.K_z and Frame1Rect.collidepoint(pCharacter.rect.center):
                    running = False
                    switch_scene(selectMode)

            if e.type == pygame.KEYUP:
                if e.type == pygame.KEYUP:
                    if e.key == pygame.K_UP:
                        player.isUp = False
                    elif e.key == pygame.K_DOWN:
                        player.isDown = False
                    elif e.key == pygame.K_LEFT:
                        player.isLeft = False
                    elif e.key == pygame.K_RIGHT:
                        player.isRight = False

        if Frame1Rect.collidepoint(pCharacter.rect.center):
            Back = font1.render('Back', False, (255, 255, 0))
        else:
            Back = font1.render('Back', False, (255, 255, 255))
        match FrameUnFill:
            case 25:
                isUnFillUpdate = False

        match isUnFillUpdate:
            case True:
                alphaUn -= 14
                unFillImage.set_alpha(alphaUn)
                FrameUnFill += 1

        sc.fill((10, 2, 16))
        sc.blit(IoannImage, IoannRect)
        sc.blit(ValeriaImage, ValeriaRect)
        sc.blit(IoannTXT, IoannTXTrect)
        sc.blit(ValeriaTXT, ValeriaTXTrect)
        sc.blit(selectText, selectTextRect)
        sc.blit(Back, backRect)
        sc.blit(Frame1, Frame1Rect)
        sc.blit(pCharacter.image, pCharacter.rect)
        match isUnFillUpdate:
            case True:
                sc.blit(unFillImage, unFillRect)
        pygame.display.update()
        clock.tick(FPS)
        pCharacter.move()


def loadingScreen():
    global font1, font2, font22, t1
    running = True
    FPS = 60

    # Image
    backscreen = pygame.image.load('Sprite/UI/loadingFrame.png').convert_alpha()
    backscreen = pygame.transform.scale(backscreen.convert_alpha(), (RES[0] - 6, RES[1] - 6))
    backRect = backscreen.get_rect(center=(RES[0] // 2, RES[1] // 2))

    loadingLogo = pygame.image.load('Sprite/UI/LogoLoading.png').convert_alpha()
    loadingLogo = pygame.transform.scale(loadingLogo.convert_alpha(), (366, 386))
    loadingRect = loadingLogo.get_rect(center=(200, 300))

    FrameAnim = 0
    loadingAnim = pygame.image.load('Sprite/UI/loadingAnim/la_1.png').convert_alpha()
    loadingAnim = pygame.transform.scale(loadingAnim.convert_alpha(), (415, 415))
    loadingAnimRect = loadingAnim.get_rect(center=(890, 820))

    # Text
    fontLoad = pygame.font.Font('Font/4.ttf', 35)
    loadingText = fontLoad.render('Reload Gun:', False, (255, 255, 255))
    loadingTextRect = loadingText.get_rect(center=(910, 825))

    fontTips = pygame.font.Font('Font/5.ttf', 25)
    selectT = randint(0, 4)
    tips = ''
    match selectT:
        case 0:
            tips = 'Welcome!'
        case 1:
            tips = 'We exist...'
        case 2:
            tips = 'I Love You'
        case 3:
            tips = 'Buy Clothes in Shop'
        case 4:
            tips = 'turn around)'
    tipsText = fontTips.render('Tips: '+str(tips), False, (255, 255, 255))
    tipsText.set_alpha(40)
    tipsRect = tipsText.get_rect(center=(400, 880))

    loadinPercent = 0

    while running:
        match FrameAnim:
            case 60:
                loadingAnim = pygame.image.load('Sprite/UI/loadingAnim/la_1.png').convert_alpha()
                loadingAnim = pygame.transform.scale(loadingAnim.convert_alpha(), (415, 415))
                FrameAnim = 0
            case 5:
                loadingAnim = pygame.image.load('Sprite/UI/loadingAnim/la_2.png').convert_alpha()
                loadingAnim = pygame.transform.scale(loadingAnim.convert_alpha(), (415, 415))
            case 10:
                loadingAnim = pygame.image.load('Sprite/UI/loadingAnim/la_3.png').convert_alpha()
                loadingAnim = pygame.transform.scale(loadingAnim.convert_alpha(), (415, 415))
            case 15:
                loadingAnim = pygame.image.load('Sprite/UI/loadingAnim/la_4.png').convert_alpha()
                loadingAnim = pygame.transform.scale(loadingAnim.convert_alpha(), (415, 415))
            case 20:
                loadingAnim = pygame.image.load('Sprite/UI/loadingAnim/la_5.png').convert_alpha()
                loadingAnim = pygame.transform.scale(loadingAnim.convert_alpha(), (415, 415))
            case 25:
                loadingAnim = pygame.image.load('Sprite/UI/loadingAnim/la_6.png').convert_alpha()
                loadingAnim = pygame.transform.scale(loadingAnim.convert_alpha(), (415, 415))
            case 30:
                loadingAnim = pygame.image.load('Sprite/UI/loadingAnim/la_7.png').convert_alpha()
                loadingAnim = pygame.transform.scale(loadingAnim.convert_alpha(), (415, 415))
            case 35:
                loadingAnim = pygame.image.load('Sprite/UI/loadingAnim/la_8.png').convert_alpha()
                loadingAnim = pygame.transform.scale(loadingAnim.convert_alpha(), (415, 415))
            case 40:
                loadingAnim = pygame.image.load('Sprite/UI/loadingAnim/la_9.png').convert_alpha()
                loadingAnim = pygame.transform.scale(loadingAnim.convert_alpha(), (415, 415))
            case 45:
                loadingAnim = pygame.image.load('Sprite/UI/loadingAnim/la_10.png').convert_alpha()
                loadingAnim = pygame.transform.scale(loadingAnim.convert_alpha(), (415, 415))
            case 50:
                loadingAnim = pygame.image.load('Sprite/UI/loadingAnim/la_11.png').convert_alpha()
                loadingAnim = pygame.transform.scale(loadingAnim.convert_alpha(), (415, 415))
            case 56:
                loadingAnim = pygame.image.load('Sprite/UI/loadingAnim/la_12.png').convert_alpha()
                loadingAnim = pygame.transform.scale(loadingAnim.convert_alpha(), (415, 415))
        FrameAnim += 1
        match loadinPercent:
            case 215:
                t1 = threading.Thread(target=switch_scene(TitleScreen)).start()
                running = False
        loadinPercent += 1
        sc.fill((0, 0, 0))
        sc.blit(backscreen, backRect)
        sc.blit(loadingLogo, loadingRect)
        sc.blit(loadingText, loadingTextRect)
        sc.blit(loadingAnim, loadingAnimRect)
        sc.blit(tipsText, tipsRect)
        pygame.display.update()
        clock.tick(FPS)


def TitleChanScreen():
    running = True
    FPS = 60

    fontTitle = pygame.font.Font('Font/5.ttf', 80)
    titleText = fontTitle.render('TitleChanQWERTY', False, (35, 6, 50))
    titleRect = titleText.get_rect(center=(RES[0] // 2, RES[1] // 2))

    Frame = 0

    TitleCh = pygame.image.load('Sprite/Player/TitleChanQWERTY.png').convert_alpha()
    TitleCh = pygame.transform.scale(TitleCh, (64, 64))
    TitleChRect = TitleCh.get_rect(center=(-730, 570))

    createUnFill('Sprite/UI/Fill/1.png', 1500, 1300)
    while running:
        for e in pygame.event.get():
            match e.type:
                case pygame.QUIT:
                    running = False
                    switch_scene(None)
        if Frame >= 255:
            running = False
            switch_scene(loadingScreen)
        TitleChRect.x += 19
        Frame += 1
        sc.fill((2, 0, 13))
        sc.blit(titleText, titleRect)
        sc.blit(TitleCh, TitleChRect)
        alphaG.draw(sc)
        pygame.display.update()
        clock.tick(FPS)
        alphaG.update()


def TitleScreen():
    global t1
    # Fill
    alpha = 350
    FrameAlpha = 0
    isAlpha = True
    fillImage = pygame.image.load('Sprite/UI/Fill/2.png').convert_alpha()
    fillImage.set_alpha(alpha)
    fillImage = pygame.transform.scale(fillImage.convert_alpha(), (RES[0], RES[1]))
    fillRect = fillImage.get_rect(center=(RES[0] // 2, RES[1] // 2))

    # Image
    backImage = pygame.image.load('Sprite/UI/titleImage/TitleImage.png').convert_alpha()
    backImage = pygame.transform.scale(backImage.convert_alpha(), (RES[0], RES[1] + 65))
    backRect = backImage.get_rect(center=(RES[0] // 2, RES[1] // 2 + 31))
    FrameTitle = 0

    Xpos = 1395
    logoImage = pygame.image.load('Sprite/UI/LogoTitle.png').convert_alpha()
    logoImage = pygame.transform.scale(logoImage.convert_alpha(), (366, 386))
    logoRect = logoImage.get_rect(center=(Xpos, 255))
    FrameLogo = 0
    isAnimLogo = False

    # Text
    FrameText = 0
    alphaT = 0
    font = pygame.font.Font('Font/1.ttf', 45)
    text = font.render('Press Any Key', False, (255, 255, 0))
    text.set_alpha(alphaT)
    textRect = text.get_rect(center=(255, 775))

    fontT = pygame.font.Font('Font/3.ttf', 15)
    textTitle = fontT.render('Powered By TitleChanQWERT *2022*', False, (51, 0, 78))
    textTitleRect = textTitle.get_rect(center=(840, 885))

    running = True
    FPS = 60

    scale = 696

    while running:
        for e in pygame.event.get():
            match e.type:
                case pygame.QUIT:
                    running = False
                    switch_scene(None)
                case pygame.KEYDOWN:
                    running = False
                    t1 = threading.Thread(target=switch_scene(mainMenu)).start()
        match FrameTitle:
            case 65:
                backImage = pygame.image.load('Sprite/UI/titleImage/TitleImage.png').convert_alpha()
                backImage = pygame.transform.scale(backImage.convert_alpha(), (RES[0], RES[1] + 65))
                FrameTitle = 0
            case 35:
                backImage = pygame.image.load('Sprite/UI/titleImage/TitleImage2.png').convert_alpha()
                backImage = pygame.transform.scale(backImage.convert_alpha(), (RES[0], RES[1] + 65))
        FrameTitle += 1
        match FrameText:
            case 60:
                alphaT = 0
                text.set_alpha(alphaT)
                FrameText = 0
            case 30:
                alphaT = 250
                text.set_alpha(alphaT)
        match isAlpha:
            case True:
                match FrameAlpha:
                    case 43:
                        isAlpha = False
                        isAnimLogo = True
                        alpha = 0
                        FrameAlpha = 0
                alpha -= 8
                fillImage.set_alpha(alpha)
                FrameAlpha += 1
        match isAnimLogo:
            case True:
                match FrameLogo:
                    case 95:
                        logoImage = pygame.image.load('Sprite/UI/LogoTitle.png').convert_alpha()
                        scale = 366
                        logoImage = pygame.transform.scale(logoImage.convert_alpha(), (366, 386))
                        isAnimLogo = False
                Xpos -= 4
                scale -= 5
                logoImage = pygame.transform.scale(logoImage.convert_alpha(), (scale, 386))
                logoRect = logoImage.get_rect(center=(Xpos, 255))
                FrameLogo += 1
        FrameText += 1
        sc.fill((0, 0, 0))
        sc.blit(backImage, backRect)
        sc.blit(logoImage, logoRect)
        sc.blit(textTitle, textTitleRect)
        sc.blit(text, textRect)
        match isAlpha:
            case True:
                sc.blit(fillImage, fillRect)
        pygame.display.update()
        clock.tick(FPS)


def scoreMenu():
    running = True
    FPS = 60

    pScore = player.PlayerMenu(550, 790, 7)

    # Fill
    alpha = 350
    FrameAlpha = 0
    isAlpha = True
    fillImage = pygame.image.load('Sprite/UI/Fill/2.png').convert_alpha()
    fillImage.set_alpha(alpha)
    fillImage = pygame.transform.scale(fillImage.convert_alpha(), (RES[0], RES[1]))
    fillRect = fillImage.get_rect(center=(RES[0] // 2, RES[1] // 2))

    # Text
    fontHI = pygame.font.Font('Font/2.ttf', 85)
    HISCORE = fontHI.render('HISCORE: ' + str(op.HISCORE), False, (255, 225, 0))
    HISCORErect = HISCORE.get_rect(center=(550, 350))

    fontSC = pygame.font.Font('Font/1.ttf', 65)
    SCORE = fontSC.render('HISCORE: ' + str(op.SCORE), False, (255, 185, 0))
    SCORErect = SCORE.get_rect(center=(550, 550))

    Back = font1.render('Back', False, (255, 255, 255))
    backRect = Back.get_rect(center=(990, 870))

    Frame1 = pygame.image.load('Sprite/UI/Frame2.png').convert_alpha()
    Frame1 = pygame.transform.scale(Frame1, (147, 108))
    Frame1Rect = Frame1.get_rect(center=(985, 870))

    fontYS = pygame.font.Font('Font/3.ttf', 70)
    YSCORE = fontYS.render('Your Score', False, (255, 255, 255))
    YSCORErect = YSCORE.get_rect(center=(550, 150))

    while running:
        for e in pygame.event.get():
            match e.type:
                case pygame.QUIT:
                    running = False
                    switch_scene(None)
                case pygame.KEYDOWN:
                    if e.key == pygame.K_UP:
                        player.isUp = True
                    elif e.key == pygame.K_DOWN:
                        player.isDown = True
                    elif e.key == pygame.K_LEFT:
                        player.isLeft = True
                    elif e.key == pygame.K_RIGHT:
                        player.isRight = True
                    if e.key == pygame.K_z and Frame1Rect.collidepoint(pScore.rect.center):
                        running = False
                        switch_scene(mainMenu)
                case pygame.KEYUP:
                    if e.key == pygame.K_UP:
                        player.isUp = False
                    elif e.key == pygame.K_DOWN:
                        player.isDown = False
                    elif e.key == pygame.K_LEFT:
                        player.isLeft = False
                    elif e.key == pygame.K_RIGHT:
                        player.isRight = False
        match isAlpha:
            case True:
                match FrameAlpha:
                    case 20:
                        isAlpha = False
                        alpha = 0
                        FrameAlpha = 0
                alpha -= 20
                fillImage.set_alpha(alpha)
                FrameAlpha += 1
        if Frame1Rect.collidepoint(pScore.rect.center):
            Back = font1.render('Back', False, (255, 255, 0))
        else:
            Back = font1.render('Back', False, (255, 255, 255))
        sc.fill((11, 2, 12))
        sc.blit(YSCORE, YSCORErect)
        sc.blit(HISCORE, HISCORErect)
        sc.blit(SCORE, SCORErect)
        sc.blit(Back, backRect)
        sc.blit(Frame1, Frame1Rect)
        sc.blit(pScore.image, pScore.rect)
        match isAlpha:
            case True:
                sc.blit(fillImage, fillRect)
        pygame.display.update()
        clock.tick(FPS)
        pScore.move()


def shop():
    running = True
    FPS = 60

    # Image
    shopBack = pygame.image.load('Sprite/UI/shop/1.png').convert_alpha()
    shopBack = pygame.transform.scale(shopBack, (RES[0], RES[1]))
    shopRect = shopBack.get_rect(center=(RES[0] // 2 - 1, RES[1] // 2 - 1))

    shopFrameImage = pygame.image.load('Sprite/UI/shop/Frame/f.png').convert_alpha()
    shopFrameImage = pygame.transform.scale(shopFrameImage, (1015, 1015))
    shopFRect = shopFrameImage.get_rect(center=(RES[0] // 2 - 155, RES[1] // 2 + 75))

    pShop = player.PlayerMenu(550, 820, 7)

    # Icon item
    genHat = pygame.image.load("Sprite/Player/finery/Gentleman's hat.png").convert_alpha()
    genHat = pygame.transform.scale(genHat, (36, 36))
    genHat.set_alpha(30)
    genRect = genHat.get_rect(center=(147, 455))

    horn = pygame.image.load("Sprite/Player/finery/Horn.png").convert_alpha()
    horn = pygame.transform.scale(horn, (42, 42))
    hornRect = horn.get_rect(center=(215, 455))

    wings = pygame.image.load("Sprite/Player/finery/Wings.png").convert_alpha()
    wings = pygame.transform.scale(wings, (45, 45))
    wingsRect = wings.get_rect(center=(298, 455))

    maid = pygame.image.load("Sprite/Player/finery/Maid's bonnet.png").convert_alpha()
    maid = pygame.transform.scale(maid, (42, 42))
    maidRect = maid.get_rect(center=(379, 455))

    clown = pygame.image.load("Sprite/Player/finery/clown wig.png").convert_alpha()
    clown = pygame.transform.scale(clown, (33, 33))
    clownRect = clown.get_rect(center=(440, 447))

    Hbow = pygame.image.load("Sprite/Player/finery/Hakurei bow.png").convert_alpha()
    Hbow = pygame.transform.scale(Hbow, (42, 42))
    HbowRect = Hbow.get_rect(center=(504, 451))

    RGlass = pygame.image.load("Sprite/Player/finery/Realm glasses.png").convert_alpha()
    RGlass = pygame.transform.scale(RGlass, (30, 30))
    RGRect = RGlass.get_rect(center=(569, 452))

    Sword = pygame.image.load("Sprite/Player/finery/Sword.png").convert_alpha()
    Sword = pygame.transform.scale(Sword, (31, 31))
    swordRect = Sword.get_rect(center=(625, 447))

    alpha = [50, 50, 50, 50, 50, 50, 50, 50]
    unAlpha = [300, 300, 300, 300, 300, 300, 300, 300]

    IoannIcon = pygame.image.load('Sprite/Player/Ioann.png').convert_alpha()
    IoannIcon = pygame.transform.scale(IoannIcon, (34, 34))
    IoannRect = IoannIcon.get_rect(center=(867, RES[1] // 2 + 25))

    # Text
    HISCOREText = font2.render("HISCORE: " + str(op.HISCORE), False, (255, 255, 0))
    HIRect = HISCOREText.get_rect(center=(450, 870))

    previewText = font22.render("Preview", False, (51, 188, 121))
    previewRect = previewText.get_rect(center=(871, RES[1] // 2 - 37))

    Back = font1.render('Back', False, (255, 255, 255))
    backRect = Back.get_rect(center=(990, 870))

    Frame1 = pygame.image.load('Sprite/UI/Frame2.png').convert_alpha()
    Frame1 = pygame.transform.scale(Frame1, (147, 108))
    Frame1Rect = Frame1.get_rect(center=(985, 870))

    FrameWings = 0

    createUnFill('Sprite/UI/Fill/1.png', 1500, 1300)
    while running:
        for e in pygame.event.get():
            match e.type:
                case pygame.QUIT:
                    running = False
                    switch_scene(None)
                case pygame.KEYDOWN:
                    if e.key == pygame.K_UP:
                        player.isUp = True
                    elif e.key == pygame.K_DOWN:
                        player.isDown = True
                    elif e.key == pygame.K_LEFT:
                        player.isLeft = True
                    elif e.key == pygame.K_RIGHT:
                        player.isRight = True
                    if genRect.collidepoint(pShop.rect.center):
                        if e.key == pygame.K_z and op.HISCORE >= 25000:
                            alpha[0] = 300
                            alpha[1] = 50
                            alpha[2] = 50
                            alpha[6] = 50
                            alpha[3] = 50
                            alpha[5] = 50
                            alpha[7] = 50
                            alpha[4] = 50
                            op.HISCORE -= 25000
                            player.idFinery = 1
                    if hornRect.collidepoint(pShop.rect.center):
                        if e.key == pygame.K_z and op.HISCORE >= 900:
                            alpha[1] = 300
                            alpha[0] = 50
                            alpha[6] = 50
                            alpha[2] = 50
                            alpha[3] = 50
                            alpha[5] = 50
                            alpha[4] = 50
                            alpha[7] = 50
                            op.HISCORE -= 900
                            player.idFinery = 2
                    if wingsRect.collidepoint(pShop.rect.center):
                        if e.key == pygame.K_z and op.HISCORE >= 32000:
                            alpha[2] = 300
                            alpha[1] = 50
                            alpha[3] = 50
                            alpha[6] = 50
                            alpha[0] = 50
                            alpha[4] = 50
                            alpha[7] = 50
                            alpha[5] = 50
                            op.HISCORE -= 32000
                            player.idFinery = 3
                    if maidRect.collidepoint(pShop.rect.center):
                        if e.key == pygame.K_z and op.HISCORE >= 1350:
                            alpha[3] = 300
                            alpha[1] = 50
                            alpha[2] = 50
                            alpha[0] = 50
                            alpha[4] = 50
                            alpha[7] = 50
                            alpha[5] = 50
                            alpha[6] = 50
                            op.HISCORE -= 1350
                            player.idFinery = 4
                    if clownRect.collidepoint(pShop.rect.center):
                        if e.key == pygame.K_z and op.HISCORE >= 2950:
                            alpha[6] = 50
                            alpha[3] = 50
                            alpha[1] = 50
                            alpha[2] = 50
                            alpha[0] = 50
                            alpha[4] = 300
                            alpha[7] = 50
                            alpha[5] = 50
                            op.HISCORE -= 2950
                            player.idFinery = 5
                    if HbowRect.collidepoint(pShop.rect.center):
                        if e.key == pygame.K_z and op.HISCORE >= 1950:
                            alpha[3] = 50
                            alpha[1] = 50
                            alpha[2] = 50
                            alpha[0] = 50
                            alpha[6] = 50
                            alpha[4] = 50
                            alpha[5] = 300
                            alpha[7] = 50
                            op.HISCORE -= 1950
                            player.idFinery = 6
                    if RGRect.collidepoint(pShop.rect.center):
                        if e.key == pygame.K_z and op.HISCORE >= 540:
                            alpha[3] = 50
                            alpha[1] = 50
                            alpha[2] = 50
                            alpha[0] = 50
                            alpha[6] = 300
                            alpha[4] = 50
                            alpha[7] = 50
                            alpha[5] = 50
                            op.HISCORE -= 540
                            player.idFinery = 7
                    if swordRect.collidepoint(pShop.rect.center):
                        if e.key == pygame.K_z and op.HISCORE >= 540:
                            alpha[3] = 50
                            alpha[1] = 50
                            alpha[2] = 50
                            alpha[0] = 50
                            alpha[6] = 50
                            alpha[4] = 50
                            alpha[7] = 300
                            alpha[5] = 50
                            op.HISCORE -= 540
                            player.idFinery = 8
                    if e.key == pygame.K_z and Frame1Rect.collidepoint(pShop.rect.center):
                        running = False
                        switch_scene(mainMenu)
                case pygame.KEYUP:
                    if e.key == pygame.K_UP:
                        player.isUp = False
                    elif e.key == pygame.K_DOWN:
                        player.isDown = False
                    elif e.key == pygame.K_LEFT:
                        player.isLeft = False
                    elif e.key == pygame.K_RIGHT:
                        player.isRight = False
        sc.fill((0, 0, 0))
        sc.blit(shopBack, shopRect)
        HISCOREText = font2.render("HISCORE: " + str(op.HISCORE), False, (255, 255, 0))
        if Frame1Rect.collidepoint(pShop.rect.center):
            Back = font1.render('Back', False, (255, 255, 0))
        else:
            Back = font1.render('Back', False, (255, 255, 255))
        if genRect.collidepoint(pShop.rect.center):
            priceText = font2.render("25000", False, (255, 255, 0))
            priceRect = priceText.get_rect(center=(RES[0] // 2 - 155, RES[1] // 2 - 100))
            genHat.set_alpha(unAlpha[0])
            sc.blit(priceText, priceRect)
        else:
            genHat.set_alpha(alpha[0])
        if hornRect.collidepoint(pShop.rect.center):
            priceText = font2.render("900", False, (255, 255, 0))
            priceRect = priceText.get_rect(center=(RES[0] // 2 - 155, RES[1] // 2 - 100))
            horn.set_alpha(unAlpha[1])
            sc.blit(priceText, priceRect)
        else:
            horn.set_alpha(alpha[1])
        if wingsRect.collidepoint(pShop.rect.center):
            priceText = font2.render("32000", False, (255, 255, 0))
            priceRect = priceText.get_rect(center=(RES[0] // 2 - 155, RES[1] // 2 - 100))
            wings.set_alpha(unAlpha[2])
            sc.blit(priceText, priceRect)
        else:
            wings.set_alpha(alpha[2])
        if maidRect.collidepoint(pShop.rect.center):
            priceText = font2.render("1350", False, (255, 255, 0))
            priceRect = priceText.get_rect(center=(RES[0] // 2 - 155, RES[1] // 2 - 100))
            maid.set_alpha(unAlpha[3])
            sc.blit(priceText, priceRect)
        else:
            maid.set_alpha(alpha[3])
        if clownRect.collidepoint(pShop.rect.center):
            priceText = font2.render("2950", False, (255, 255, 0))
            priceRect = priceText.get_rect(center=(RES[0] // 2 - 155, RES[1] // 2 - 100))
            clown.set_alpha(unAlpha[4])
            sc.blit(priceText, priceRect)
        else:
            clown.set_alpha(alpha[4])
        if HbowRect.collidepoint(pShop.rect.center):
            priceText = font2.render("1950", False, (255, 255, 0))
            priceRect = priceText.get_rect(center=(RES[0] // 2 - 155, RES[1] // 2 - 100))
            Hbow.set_alpha(unAlpha[5])
            sc.blit(priceText, priceRect)
        else:
            Hbow.set_alpha(alpha[5])
        if RGRect.collidepoint(pShop.rect.center):
            priceText = font2.render("540", False, (255, 255, 0))
            priceRect = priceText.get_rect(center=(RES[0] // 2 - 155, RES[1] // 2 - 100))
            RGlass.set_alpha(unAlpha[6])
            sc.blit(priceText, priceRect)
        else:
            RGlass.set_alpha(alpha[6])
        if swordRect.collidepoint(pShop.rect.center):
            priceText = font2.render("3500", False, (255, 255, 0))
            priceRect = priceText.get_rect(center=(RES[0] // 2 - 155, RES[1] // 2 - 100))
            Sword.set_alpha(unAlpha[7])
            sc.blit(priceText, priceRect)
        else:
            Sword.set_alpha(alpha[7])
        sc.blit(shopFrameImage, shopFRect)
        sc.blit(genHat, genRect)
        sc.blit(horn, hornRect)
        sc.blit(maid, maidRect)
        sc.blit(wings, wingsRect)
        sc.blit(clown, clownRect)
        sc.blit(RGlass, RGRect)
        sc.blit(Sword, swordRect)
        sc.blit(Hbow, HbowRect)
        sc.blit(Back, backRect)
        sc.blit(Frame1, Frame1Rect)
        sc.blit(HISCOREText, HIRect)
        sc.blit(IoannIcon, IoannRect)
        match player.idFinery:
            case 1:
                finery = pygame.image.load("Sprite/Player/finery/Gentleman's hat.png").convert_alpha()
                finery = pygame.transform.scale(finery, (46, 46))
                fineryRect = finery.get_rect(center=(IoannRect.x + 17, IoannRect.y - 11))
                sc.blit(finery, fineryRect)
            case 2:
                finery = pygame.image.load("Sprite/Player/finery/Horn.png").convert_alpha()
                finery = pygame.transform.scale(finery, (45, 45))
                fineryRect = finery.get_rect(center=(IoannRect.x + 14, IoannRect.y - 6))
                sc.blit(finery, fineryRect)
            case 3:
                if FrameWings < 20:
                    finery = pygame.image.load("Sprite/Player/finery/Wings.png").convert_alpha()
                    finery = pygame.transform.scale(finery, (66, 66))
                    finery = pygame.transform.flip(finery, False, True)
                    fineryRect = finery.get_rect(center=(IoannRect.x + 17, IoannRect.y + 16))
                    sc.blit(finery, fineryRect)
                    sc.blit(IoannIcon, IoannRect)
                if FrameWings > 20:
                    finery = pygame.image.load("Sprite/Player/finery/Wings.png").convert_alpha()
                    finery = pygame.transform.scale(finery, (66, 66))
                    finery = pygame.transform.flip(finery, False, False)
                    fineryRect = finery.get_rect(center=(IoannRect.x + 17, IoannRect.y + 12))
                    sc.blit(finery, fineryRect)
                    sc.blit(IoannIcon, IoannRect)
                if FrameWings > 35:
                    FrameWings = 0
                FrameWings += 1
            case 4:
                finery = pygame.image.load("Sprite/Player/finery/Maid's bonnet.png").convert_alpha()
                finery = pygame.transform.scale(finery, (49, 49))
                fineryRect = finery.get_rect(center=(IoannRect.x + 16, IoannRect.y + 5))
                sc.blit(finery, fineryRect)
            case 5:
                finery = pygame.image.load("Sprite/Player/finery/clown wig.png").convert_alpha()
                finery = pygame.transform.scale(finery, (65, 65))
                fineryRect = finery.get_rect(center=(IoannRect.x + 18, IoannRect.y - 5))
                sc.blit(finery, fineryRect)
                sc.blit(IoannIcon, IoannRect)
            case 6:
                finery = pygame.image.load("Sprite/Player/finery/Hakurei bow.png").convert_alpha()
                finery = pygame.transform.scale(finery, (55, 55))
                fineryRect = finery.get_rect(center=(IoannRect.x + 16, IoannRect.y + 2))
                sc.blit(finery, fineryRect)
            case 7:
                finery = pygame.image.load("Sprite/Player/finery/Realm glasses.png").convert_alpha()
                finery = pygame.transform.scale(finery, (48, 48))
                fineryRect = finery.get_rect(center=(IoannRect.x + 17, IoannRect.y + 12))
                sc.blit(finery, fineryRect)
            case 8:
                finery = pygame.image.load("Sprite/Player/finery/Sword.png").convert_alpha()
                finery = pygame.transform.scale(finery, (42, 42))
                fineryRect = finery.get_rect(center=(IoannRect.x + 17, IoannRect.y + 16))
                sc.blit(finery, fineryRect)
        sc.blit(previewText, previewRect)
        sc.blit(pShop.image, pShop.rect)
        alphaG.draw(sc)
        pygame.display.update()
        clock.tick(FPS)
        pShop.move()
        alphaG.update()


t1 = threading.Thread(target=switch_scene(TitleChanScreen)).start()
while current_scene is not None:
    current_scene()

pygame.quit()
