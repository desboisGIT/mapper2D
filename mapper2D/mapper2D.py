import random

def generateLevels(width, groundMid, contrast,maxHeightFactor, minHeightFactor):
    heightList = []
    ht = groundMid
    for i in range(width):
        ht += random.randint(-contrast, contrast)
        if ht >groundMid+maxHeightFactor:
            ht -= contrast
        if ht <groundMid-minHeightFactor:
            ht += contrast
        heightList.append(ht)
    return heightList

def smooth(heightMap):
    smoothedMap = heightMap.copy()
    for i in range(1, len(heightMap) - 1):
        smoothedMap[i] = (heightMap[i-1] + heightMap[i] + heightMap[i+1]) // 3
    return smoothedMap

def makeHeightMap(width, groundMid, contrast, smoothingLevels,maxHeightFactor=10, minHeightFactor=1.5): #width and groundmid are in tiles
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
                blocktype = True  # True for solid blocks
            else:
                blocktype = False  # False for air blocks
            tilesMap[x].append([x * tileSize, y * tileSize, blocktype])  # structure: xCord, yCord, blockType
    return tilesMap


def calculateVolume(tileList,x,y, deepth=300):
    pass

def calculateFluidLevel(heightMap):
    sum = 0
    for data in heightMap:
        sum += data
    return sum//len(heightMap)

def fluidMaker(heightMap, ocurance):
    fluidLevel = calculateFluidLevel(heightMap)
