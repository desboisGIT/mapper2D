import random

def generateLevels(width, groundMid, contrast,maxHeightFactor, minHeightFactor):
    heightList = []
    ht = groundMid
    for i in range(width):
        ht += random.randint(-contrast, contrast)
        if ht >groundMid*maxHeightFactor:
            ht -= contrast
        if ht <groundMid//minHeightFactor:
            ht += contrast
        heightList.append(ht)
    return heightList

def smooth(heightMap):
    smoothedMap = heightMap.copy()
    for i in range(1, len(heightMap) - 1):
        smoothedMap[i] = (heightMap[i-1] + heightMap[i] + heightMap[i+1]) // 3
    return smoothedMap

def makeHeightMap(width, groundMid, contrast, smoothingLevels,maxHeightFactor=1.5, minHeightFactor=1.5): #width and groundmid are in tiles
    heightMap = generateLevels(width, groundMid, contrast, maxHeightFactor, minHeightFactor)
    for i in range(smoothingLevels):
        heightMap = smooth(heightMap)
    return heightMap

def make2dMapArray(window_width, window_height, tileSize, heightMap):
    nb = window_height // tileSize
    tilesMap =[]
    for x in range(window_width // tileSize):
        tilesMap.append([])
        for y in range(window_height // tileSize):
            if y > nb - heightMap[x]:
                blocktype = "ground"  # ground for solid blocks
            else:
                blocktype = "air"  # air for air blocks
            tilesMap[x].append([x * tileSize, y * tileSize, blocktype])  # structure: xCord, yCord, blockType
    return tilesMap


def calculateVolume(tileList,x,y, deepth=300):
    pass

def calculateFluidLevel(heightMap):
    sum = 0
    for data in heightMap:
        sum += data
    return sum//len(heightMap)

def fluidMaker(Map, occurrence):
    fluidList = []
    for x in range(len(Map)):
        for y in range(len(Map[0])):
            test = random.randint(0, occurrence * 10)
            if Map[x][y][2] == "air" and test == 1:
                fluidList.append([x, y])
                Map[x][y][2] = "fluid"

def fluidUpdater(Map):
    for x in range(len(Map)):
        for y in range(len(Map[0])):
            if Map[x][y][2] == "fluid":
                # Check if there's an empty space below
                if y < len(Map[0]) - 1 and Map[x][y + 1][2] == "air":
                    # Fluid falls down
                    Map[x][y][2] = "air"
                    Map[x][y + 1][2] = "fluid"
                else:
                    # If there's no empty space below, try moving horizontally
                    direction = random.choice([-1, 1])  # Randomly choose left or right
                    if x + direction >= 0 and x + direction < len(Map):
                        # Check if there's air in the chosen direction
                        if Map[x + direction][y][2] == "air":
                            # Move fluid to the chosen direction
                            Map[x][y][2] = "air"
                            Map[x + direction][y][2] = "fluid"


