import os
import pygame

X = 270
Y = 290
running = True

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
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break
        # elif event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_ESCAPE:
        #         running = False
        #         break
        #     elif event.key == pygame.K_RIGHT:
        #         X += 10
        #     elif event.key == pygame.K_LEFT:
        #         X -= 10
        #     elif event.key == pygame.K_DOWN:
        #         Y += 10
        #     elif event.key == pygame.K_UP:
        #         Y -= 10

    window.fill(
        "#000000"
    )
    pygame.draw.rect(
        window,
        "#7E2800",
        (X, Y, 100, 140)
    )
    pygame.display.update()    

    clock.tick(60)

pygame.quit()
