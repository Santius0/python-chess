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


def draw_game_state(screen, game_state, images):
    """
    Responsible of all graphics within current game state
    """
    draw_board(screen)
    draw_pieces(screen, game_state.board, images)


def draw_board(screen):
    """
    Draw squares on board using screen.
    Note: top left square is always white
    """
    colours = [pygame.Color("white"), pygame.Color("grey")]
    for x in range(DIMENSIONS_H_W):
        for y in range(DIMENSIONS_H_W):
            colour = colours[((x + y) % 2)]
            pygame.draw.rect(screen, colour, pygame.Rect(x * SQUARE_SIZE, y * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))


def draw_pieces(screen, board, images):
    """
    Draws pieces on the board using current game state
    """
    for x in range(DIMENSIONS_H_W):
        for y in range(DIMENSIONS_H_W):
            if board[x][y] != '-':
                screen.blit(images[board[x][y]],
                            pygame.Rect(x * SQUARE_SIZE, y * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))


def handle_click(location, game_state, clicks):
    square = (location[0] // SQUARE_SIZE, location[1] // SQUARE_SIZE)
    if len(clicks) == 1:
        if square == clicks[0]:
            clicks = []
        else:
            clicks.append(square)
            game_state.move_piece(clicks[0], clicks[1])
            clicks = []
    elif len(clicks) >= 2:
        clicks = []
    else:
        clicks.append(square)
    return game_state, clicks


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    screen.fill(pygame.Color("white"))
    game_state = engine.GameState()
    images = get_images()
    running = True
    clicks = []
    while running:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False
            if e.type == pygame.MOUSEBUTTONDOWN:
                game_state, clicks = handle_click(pygame.mouse.get_pos(), game_state, clicks)
        draw_game_state(screen, game_state, images)
        clock.tick(MAX_FPS)
        pygame.display.flip()


if __name__ == '__main__':
    main()
