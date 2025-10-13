import os
import pygame

AXE_X = 314
axe_y = 20
AXE_WID = 12
AXE_HGT = 20
LOG_X = 270
LOG_Y = 290
LOG_WID = 100
LOG_HGT = 140
VEL = 10
blade_x1 = 315
blade_y1 = 40
blade_x2 = 320
blade_y2 = 70
blade_x3 = 325
blade_y3 = 40
axe_blade = [(blade_x1, blade_y1), (blade_x2, blade_y2), (blade_x3, blade_y3)]
run = True
chop = False

os.environ['SDL_VIDEO_CENTERED'] = '1'

pygame.init()
window = pygame.display.set_mode(
            (640, 480)
        )
pygame.display.set_caption("Wood Chopper Game")
ico = file=os.path.join(
                os.path.dirname(
                    os.path.abspath(__file__)),
                            "images", "icon.png")
pygame.display.set_icon(
    pygame.image.load(ico)
)

clock = pygame.time.Clock()
while run:
    # pygame.time.delay(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break
    
    keys = pygame.key.get_pressed()

    if keys[pygame.K_ESCAPE]:
        run = False
        break
    if chop:
        if axe_y < LOG_Y - AXE_HGT:
            axe_y += VEL
    elif axe_y >= LOG_Y:
        print(chop)
        # chop = False
    elif keys[pygame.K_RETURN] and axe_y < LOG_Y:
        axe_y += VEL
        chop = True

    window.fill(
        "#000000"
    )
    pygame.draw.rect(
        window,
        "#7E2800",
        (LOG_X, LOG_Y, LOG_WID, LOG_HGT)
    )
    pygame.draw.rect(
        window,
        "#7E7E7E",
        (AXE_X, axe_y, AXE_WID, AXE_HGT)
    )
    pygame.draw.polygon(
        window,
        "#7E7E7E",
        axe_blade
    )
    pygame.display.update()

    clock.tick(60)

pygame.quit()
