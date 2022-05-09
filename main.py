import sys
import pygame

from Button import Button

SCREEN_HEIGHT = 768
SCREEN_WIDTH = 1280
# Displaying all points and edges
pygame.init()
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
clock = pygame.time.Clock()


def get_font(size):  # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/font.ttf", size)


NOP_Info = get_font(16).render("No of Points:", True, "Black")
NOP_RECT = pygame.Rect(1050, 260, 140, 32)


def inc_screen():
    pygame.display.set_caption("Incremental Algorithm")

    no_of_points = ""
    active = False

    while True:
        mouse = pygame.mouse.get_pos()
        screen.fill((160, 160, 160))

        NOP_TEXT = get_font(16).render(no_of_points, True, "Black")
        pygame.draw.rect(screen, "Black", NOP_RECT, 2)
        screen.blit(NOP_Info, (NOP_RECT.x - 225, NOP_RECT.y + 5))
        screen.blit(NOP_TEXT, (NOP_RECT.x + 5, NOP_RECT.y + 5))
        NOP_RECT.w = max(100, NOP_TEXT.get_width() + 10)

        BACK = Button(image=None, pos=(1175, 700), text_input="BACK",
                      font=get_font(30), base_color="White", hovering_color="Green")
        BACK.changeColor(mouse)
        BACK.update(screen)

        MESH = Button(image=None, pos=(1000, 330), text_input="MESH",
                      font=get_font(30), base_color="White", hovering_color="Green")
        MESH.changeColor(mouse)
        MESH.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if BACK.checkForInput(mouse):
                    main_menu()
                if MESH.checkForInput(mouse):
                    no = int(no_of_points)
                    print(no)
                    # generate triangulation
                    pass

                if NOP_RECT.collidepoint(event.pos):
                    active = True
                else:
                    active = False
            if event.type == pygame.KEYDOWN and active:
                if event.key == pygame.K_BACKSPACE:
                    no_of_points = no_of_points[:-1]
                else:
                    no_of_points += event.unicode

        pygame.display.flip()
        clock.tick(90)


def dq_screen():
    pygame.display.set_caption("Divide & Conquer Algorithm")
    no_of_points = ""
    active = False

    while True:
        mouse = pygame.mouse.get_pos()
        screen.fill((160, 160, 160))

        NOP_TEXT = get_font(16).render(no_of_points, True, "Black")
        pygame.draw.rect(screen, "Black", NOP_RECT, 2)
        screen.blit(NOP_Info, (NOP_RECT.x - 225, NOP_RECT.y + 5))
        screen.blit(NOP_TEXT, (NOP_RECT.x + 5, NOP_RECT.y + 5))
        NOP_RECT.w = max(100, NOP_TEXT.get_width() + 10)

        BACK = Button(image=None, pos=(1175, 700), text_input="BACK",
                      font=get_font(30), base_color="White", hovering_color="Green")
        BACK.changeColor(mouse)
        BACK.update(screen)

        MESH = Button(image=None, pos=(1000, 330), text_input="MESH",
                      font=get_font(30), base_color="White", hovering_color="Green")
        MESH.changeColor(mouse)
        MESH.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if BACK.checkForInput(mouse):
                    main_menu()
                if MESH.checkForInput(mouse):
                    no = int(no_of_points)
                    print(no)
                    # generate triangulation
                    pass

                if NOP_RECT.collidepoint(event.pos):
                    active = True
                else:
                    active = False
            if event.type == pygame.KEYDOWN and active:
                if event.key == pygame.K_BACKSPACE:
                    no_of_points = no_of_points[:-1]
                else:
                    no_of_points += event.unicode

        pygame.display.flip()
        clock.tick(90)


def main_menu():
    pygame.display.set_caption("Delaunay Triangulation Main Menu")
    screen.fill((160, 160, 160))
    while True:
        mouse = pygame.mouse.get_pos()

        menu_text = get_font(100).render("Main Menu", True, "#CC00CC")
        menu_rect = menu_text.get_rect(center=(640, 100))
        screen.blit(menu_text, menu_rect)

        INC_BUTTON = Button(image=None, pos=(640, 350), text_input="Incremental Algorithm",
                            font=get_font(40), base_color="White", hovering_color="Green")
        DQ_BUTTON = Button(image=None, pos=(640, 500), text_input="Divide & Conquer Algorithm",
                           font=get_font(40), base_color="White", hovering_color="Green")

        for button in [INC_BUTTON, DQ_BUTTON]:
            button.changeColor(mouse)
            button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if INC_BUTTON.checkForInput(mouse):
                    inc_screen()
                if DQ_BUTTON.checkForInput(mouse):
                    dq_screen()

        pygame.display.update()


main_menu()
