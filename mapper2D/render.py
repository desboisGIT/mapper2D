import pygame
import mapper2D

window_width, window_height = 1920, 1080
screen = pygame.display.set_mode((window_width, window_height))
tileSize = 10
tiles = mapper2D.make2dMapArray(window_width, window_height,tileSize,mapper2D.makeHeightMap(192,108//2,2,8))

def render(tiles):
    for x in range(len(tiles)):
        for y in range(len(tiles[0])):
            if tiles[x][y][2]:  # If blocktype is True
                pygame.draw.rect(screen, (0, 200, 0), pygame.Rect(tiles[x][y][0], tiles[x][y][1], tileSize, tileSize))
            else:
                pygame.draw.rect(screen, (102, 255, 255), pygame.Rect(tiles[x][y][0], tiles[x][y][1], tileSize, tileSize))




running = True
while running:
    screen.fill((0, 0, 0)) 
    render(tiles)
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
