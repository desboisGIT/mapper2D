import random

def generateMap(width, groundMid, contrast):
    heightList = []
    ht = groundMid
    for i in range(width):
        ht += random.randint(-contrast, contrast)
        heightList.append(ht)
    return heightList

def smooth(heightMap):
    smoothedMap = heightMap.copy()
    for i in range(1, len(heightMap) - 1):
        smoothedMap[i] = (heightMap[i-1] + heightMap[i] + heightMap[i+1]) // 3
    return smoothedMap

def mapper2D(width, groundMid, contrast, smoothingLevels):
    heightMap = generateMap(width, groundMid, contrast)
    for i in range(smoothingLevels):
        heightMap = smooth(heightMap)
    return heightMap

