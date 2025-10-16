import os
import pygame

# Constants
AXE_START_POS = 20
AXE_END_POS = 280
AXE_X = 314
AXE_WID = 12
AXE_HGT = 20
BLADE_START_POS_X1 = 315
BLADE_START_POS_X2 = 320
BLADE_START_POS_X3 = 325
BLADE_END_POS = 260
BLOCK_LEFT_WID = 15
BLOCK_LEFT_HGT = 70
BLOCK_RIGHT_WID = 15
BLOCK_RIGHT_HGT = 70
LOG_X = 270
LOG_Y = 310
LOG_WID = 100
LOG_HGT = 140
VEL = 20

# Variables
axe_y = AXE_START_POS
blade_y1 = 40
blade_y2 = 70
blade_y3 = 40
block_left_x = 305
block_left_y = 240
block_right_x = 320
block_right_y = 240
axe_blade = [
    (BLADE_START_POS_X1, blade_y1),
    (BLADE_START_POS_X2, blade_y2),
    (BLADE_START_POS_X3, blade_y3)
]
run = True
chopped = False

# Position window in center of display
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

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break
    
    keys = pygame.key.get_pressed()

    if keys[pygame.K_ESCAPE]:
        run = False
        break
    if axe_y == 20:
        block_left_x = 305
        block_left_y = 240
        block_right_x = 320
        block_right_y = 240
        chopped = False
    if keys[pygame.K_RETURN]:
        axe_y = AXE_END_POS
        axe_blade = [
            (BLADE_START_POS_X1, blade_y1 + BLADE_END_POS),
            (BLADE_START_POS_X2, blade_y2 + BLADE_END_POS),
            (BLADE_START_POS_X3, blade_y3 + BLADE_END_POS)
        ]
        chopped = True
    if axe_y > 20:
        axe_y -= VEL
        for i in range(len(axe_blade)):
            axe_blade[i] = (axe_blade[i][0], axe_blade[i][1] - VEL)
        block_left_x -= VEL
        block_left_y -= VEL
        block_right_x += VEL
        block_right_y -= VEL
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
        "#A34303",
        (block_left_x, block_left_y, BLOCK_LEFT_WID, BLOCK_LEFT_HGT)
    )
    pygame.draw.rect(
        window,
        "#A34303",
        (block_right_x, block_right_y, BLOCK_RIGHT_WID, BLOCK_RIGHT_HGT)
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
