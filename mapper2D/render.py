import pygame
import mapper2D

### ---
 
window_width, window_height = 1920, 1080
tileSize = 10
terrainContrast =4
smoothing = 8
waterOcurance = 2
### ---

screen = pygame.display.set_mode((window_width, window_height))
tiles = mapper2D.make2dMapArray(window_width, window_height, tileSize, mapper2D.makeHeightMap(window_width//tileSize, (window_height//tileSize)//2, terrainContrast, smoothing))

def render(tiles):
    for x in range(len(tiles)):
        for y in range(len(tiles[0])):
            if tiles[x][y][2] == "ground":  # If blocktype is True
                pygame.draw.rect(screen, (0, 200, 0), pygame.Rect(tiles[x][y][0], tiles[x][y][1], tileSize, tileSize))
            elif tiles[x][y][2] == "air":
                pygame.draw.rect(screen, (102, 255, 255), pygame.Rect(tiles[x][y][0], tiles[x][y][1], tileSize, tileSize))
            elif tiles[x][y][2] == "fluid":
                pygame.draw.rect(screen, (100, 100, 255), pygame.Rect(tiles[x][y][0], tiles[x][y][1], tileSize, tileSize))

def refresh():
    screen.fill((0, 0, 0)) 
    render(tiles)
    pygame.display.flip()

clock = pygame.time.Clock()
running = True
mapper2D.fluidMaker(tiles, waterOcurance)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Update fluid simulation
    mapper2D.fluidUpdater(tiles)

    refresh()
    clock.tick(120)  # Adjust as needed
