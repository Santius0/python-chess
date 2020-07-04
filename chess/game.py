import pygame
import os

from chess import rule_engine as engine

WIDTH = HEIGHT = 512
DIMENSIONS_H_W = 8
SQUARE_SIZE = HEIGHT // DIMENSIONS_H_W
MAX_FPS = 15


def get_images(path=r'../images'):
    path = os.path.abspath(path)
    _images = {}
    for img in os.listdir(path):
        _img = pygame.image.load(os.path.join(path, img))
        _img = pygame.transform.scale(_img, (SQUARE_SIZE, SQUARE_SIZE))
        _images[os.path.splitext(img)[0]] = _img
    return _images


"""
Responsible of all graphics within current gamestate
"""
def draw_game_state(screen, game_state, images):
    draw_board(screen)
    draw_pieces(screen, game_state.board, images)


"""
Draw squares on board using screen.
Note: top left square is always white
"""
def draw_board(screen):
    colours = [pygame.Color("white"), pygame.Color("grey")]
    for x in range(DIMENSIONS_H_W):
        for y in range(DIMENSIONS_H_W):
            colour = colours[((x+y) % 2)]
            pygame.draw.rect(screen, colour, pygame.Rect(x*SQUARE_SIZE, y*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))




"""
Draws pieces on the board using current game state
"""
def draw_pieces(screen, board, images):
    for x in range(DIMENSIONS_H_W):
        for y in range(DIMENSIONS_H_W):
            if board[x][y] != '-':
                screen.blit(images[board[x][y]], pygame.Rect(x * SQUARE_SIZE, y * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    screen.fill(pygame.Color("white"))
    game_state = engine.GameState()
    images = get_images()
    running = True
    squares_clicked = []
    while running:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False
            if e.type == pygame.MOUSEBUTTONDOWN:
                location = pygame.mouse.get_pos()
                square_clicked = (location[0] // SQUARE_SIZE, location[1] // SQUARE_SIZE)
                if len(squares_clicked) == 1:
                    if square_clicked == squares_clicked[0]:
                        squares_clicked = []
                    else:
                        squares_clicked.append(square_clicked)
                        game_state.move_piece(squares_clicked[0], squares_clicked[1])
                        squares_clicked = []
                elif len(squares_clicked) >= 2:
                    squares_clicked = []
                else:
                    squares_clicked.append(square_clicked)
        draw_game_state(screen, game_state, images)
        clock.tick(MAX_FPS)
        pygame.display.flip()


if __name__ == '__main__':
    main()
