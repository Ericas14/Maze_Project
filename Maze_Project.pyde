def setup():
    global sprites
    global maze
    global charc_c
    global charc_r
    global grassImage
    global smileyImage
    global emptyImage
    global keyImage
    global lock2Image
    global obtainedKey
    obtainedKey = False
    size(600,600)
    background(255, 255, 255)
    sprite = []
    emptyImage = loadImage("empty.jpg")
    smileyImage = loadImage("smiley.jpg")
    grassImage = loadImage("grass.jpg")
    keyImage = loadImage("key.jpg")
    lock2Image = loadImage("lock2.jpg")
    sprites = [ emptyImage, smileyImage, grassImage, keyImage, lock2Image]
    
    charc_r = 0
    charc_c = 2
    
    maze = [
    [sprites[2],sprites[2],sprites[1],sprites[2],sprites[2],sprites[2],sprites[2],sprites[2],sprites[2],sprites[2], sprites[2],sprites[2],sprites[2],sprites[2],sprites[2], sprites[2],sprites[2],sprites[2],sprites[2],sprites[2] ],
    [sprites[2],sprites[2],sprites[0],sprites[0],sprites[0],sprites[0],sprites[0],sprites[0],sprites[0],sprites[0], sprites[0],sprites[0],sprites[0],sprites[0],sprites[0], sprites[0],sprites[0],sprites[2],sprites[2],sprites[2] ],
    [sprites[2],sprites[2],sprites[0],sprites[2],sprites[2],sprites[2],sprites[2],sprites[2],sprites[2],sprites[2], sprites[2],sprites[0],sprites[2],sprites[0],sprites[2], sprites[2],sprites[0],sprites[2],sprites[2],sprites[2] ],
    [sprites[2],sprites[2],sprites[0],sprites[2],sprites[2],sprites[2],sprites[2],sprites[2],sprites[2],sprites[2], sprites[2],sprites[0],sprites[2],sprites[0],sprites[2], sprites[2],sprites[0],sprites[2],sprites[2],sprites[2] ],
    [sprites[2],sprites[2],sprites[0],sprites[2],sprites[2],sprites[2],sprites[2],sprites[0],sprites[0],sprites[0], sprites[2],sprites[0],sprites[2],sprites[0],sprites[2], sprites[2],sprites[0],sprites[0],sprites[0],sprites[0] ],
    [sprites[2],sprites[2],sprites[0],sprites[0],sprites[0],sprites[0],sprites[0],sprites[0],sprites[2],sprites[0], sprites[2],sprites[0],sprites[2],sprites[2],sprites[2], sprites[2],sprites[2],sprites[2],sprites[2],sprites[0] ],
    [sprites[2],sprites[2],sprites[0],sprites[2],sprites[2],sprites[2],sprites[2],sprites[0],sprites[2],sprites[0], sprites[2],sprites[0],sprites[0],sprites[0],sprites[0], sprites[0],sprites[2],sprites[2],sprites[2],sprites[0] ],
    [sprites[2],sprites[2],sprites[0],sprites[2],sprites[2],sprites[2],sprites[2],sprites[0],sprites[2],sprites[0], sprites[2],sprites[2],sprites[2],sprites[2],sprites[2], sprites[0],sprites[2],sprites[2],sprites[2],sprites[0] ],
    [sprites[0],sprites[0],sprites[0],sprites[2],sprites[2],sprites[2],sprites[2],sprites[0],sprites[2],sprites[0], sprites[0],sprites[0],sprites[0],sprites[0],sprites[0], sprites[0],sprites[2],sprites[2],sprites[2],sprites[0] ],
    [sprites[0],sprites[2],sprites[2],sprites[2],sprites[2],sprites[2],sprites[2],sprites[0],sprites[2],sprites[2], sprites[2],sprites[2],sprites[2],sprites[2],sprites[2], sprites[2],sprites[2],sprites[2],sprites[2],sprites[0] ],
    [sprites[0],sprites[2],sprites[2],sprites[2],sprites[2],sprites[2],sprites[2],sprites[0],sprites[2],sprites[2], sprites[0],sprites[2],sprites[2],sprites[2],sprites[2], sprites[2],sprites[2],sprites[2],sprites[2],sprites[0] ],
    [sprites[0],sprites[2],sprites[0],sprites[0],sprites[0],sprites[0],sprites[0],sprites[0],sprites[0],sprites[2], sprites[0],sprites[0],sprites[0],sprites[0],sprites[0], sprites[0],sprites[0],sprites[0],sprites[0],sprites[0] ],
    [sprites[2],sprites[2],sprites[0],sprites[2],sprites[2],sprites[2],sprites[2],sprites[2],sprites[2],sprites[2], sprites[0],sprites[2],sprites[2],sprites[2],sprites[2], sprites[2],sprites[0],sprites[2],sprites[2],sprites[2] ],
    [sprites[2],sprites[2],sprites[0],sprites[2],sprites[2],sprites[2],sprites[2],sprites[2],sprites[2],sprites[2], sprites[2],sprites[2],sprites[2],sprites[2],sprites[2], sprites[2],sprites[0],sprites[2],sprites[2],sprites[2] ],
    [sprites[0],sprites[0],sprites[0],sprites[2],sprites[0],sprites[0],sprites[0],sprites[0],sprites[0],sprites[0], sprites[2],sprites[0],sprites[0],sprites[0],sprites[2], sprites[0],sprites[0],sprites[2],sprites[2],sprites[2] ],
    [sprites[0],sprites[2],sprites[2],sprites[2],sprites[0],sprites[2],sprites[2],sprites[2],sprites[2],sprites[0], sprites[2],sprites[0],sprites[2],sprites[0],sprites[2], sprites[2],sprites[0],sprites[2],sprites[2],sprites[2] ],
    [sprites[0],sprites[0],sprites[0],sprites[0],sprites[0],sprites[2],sprites[2],sprites[2],sprites[2],sprites[0], sprites[2],sprites[0],sprites[2],sprites[0],sprites[2], sprites[2],sprites[0],sprites[0],sprites[0],sprites[3] ],
    [sprites[0],sprites[2],sprites[2],sprites[2],sprites[0],sprites[0],sprites[0],sprites[0],sprites[0],sprites[0], sprites[2],sprites[0],sprites[2],sprites[0],sprites[2], sprites[2],sprites[2],sprites[2],sprites[2],sprites[2] ],
    [sprites[0],sprites[2],sprites[2],sprites[2],sprites[2],sprites[2],sprites[2],sprites[2],sprites[2],sprites[0], sprites[2],sprites[0],sprites[2],sprites[0],sprites[2], sprites[2],sprites[2],sprites[2],sprites[2],sprites[2] ],
    [sprites[2],sprites[2],sprites[2],sprites[2],sprites[2],sprites[2],sprites[2],sprites[2],sprites[2],sprites[0], sprites[0],sprites[0],sprites[2],sprites[4],sprites[2], sprites[2],sprites[2],sprites[2],sprites[2],sprites[2] ]
        ]

def draw():
    global sprites  
    global maze  
    for row in range(len(maze)):
        for col in range(20):
            sprite = maze[row][col]
            image(sprite, col*30, row*30)
            
def keyPressed():
    global charc_c
    global charc_r
    global grassImage
    global smileyImage
    global emptyImage
    global obtainedKey
    global keyImage
    global lock2Image
    
    nextStep = maze[charc_r][charc_c]
    
    if key == CODED:
        if keyCode == RIGHT and charc_c != 19:
            print("right")
            nextStep = maze[charc_r][charc_c + 1]
            
            if nextStep != grassImage:
                maze[charc_r][charc_c + 1] = smileyImage
                maze[charc_r][charc_c] = emptyImage
                charc_c = charc_c + 1
                
            if nextStep == keyImage:
                obtainedKey = True
                            

        elif keyCode == LEFT and charc_c != 0:
            print("left")
            nextStep = maze[charc_r][charc_c - 1]
            
            if nextStep != grassImage:
                maze[charc_r][charc_c - 1] = smileyImage
                maze[charc_r][charc_c] = emptyImage
                charc_c = charc_c - 1

        elif keyCode == UP and charc_r != 0:
            print("up")
            nextStep = maze[charc_r - 1][charc_c]
            
            if nextStep != grassImage:
                maze[charc_r - 1][charc_c] = smileyImage
                maze[charc_r][charc_c] = emptyImage
                charc_r = charc_r - 1
                              

        elif keyCode == DOWN and charc_r != 19:
            print("down")
            nextStep = maze[charc_r + 1][charc_c]
            
            if obtainedKey == True and nextStep != grassImage:
                maze[charc_r + 1][charc_c] = smileyImage
                maze[charc_r][charc_c] = emptyImage
                charc_r = charc_r + 1
            elif nextStep != grassImage and nextStep != lock2Image:
                maze[charc_r + 1][charc_c] = smileyImage
                maze[charc_r][charc_c] = emptyImage
                charc_r = charc_r + 1
    print(charc_r , charc_c)
    print(obtainedKey)
