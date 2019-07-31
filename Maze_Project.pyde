def setup():
    global sprites
    global maze
    global charc_c
    global charc_r
    global wallImage
    global smileyImage
    global emptyImage
    size(600,600)
    sprite = []
    emptyImage = loadImage("empty.jpg")
    smileyImage = loadImage("smiley.jpg")
    wallImage = loadImage("wall.jpg")
    keyImage = loadImage("key.jpg")
    lockImage = loadImage("lock.jpg")
    sprites = [ emptyImage, smileyImage, wallImage, keyImage, lockImage]
    
    charc_r = 1
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
    [sprites[0],sprites[2],sprites[0],sprites[2],sprites[0],sprites[2],sprites[2],sprites[2],sprites[2],sprites[0], sprites[2],sprites[0],sprites[2],sprites[0],sprites[2], sprites[2],sprites[0],sprites[2],sprites[2],sprites[2] ],
    [sprites[0],sprites[0],sprites[0],sprites[0],sprites[0],sprites[2],sprites[2],sprites[2],sprites[2],sprites[0], sprites[2],sprites[0],sprites[2],sprites[0],sprites[2], sprites[2],sprites[0],sprites[0],sprites[0],sprites[3] ],
    [sprites[0],sprites[2],sprites[2],sprites[2],sprites[0],sprites[0],sprites[0],sprites[0],sprites[0],sprites[0], sprites[2],sprites[0],sprites[2],sprites[4],sprites[2], sprites[2],sprites[2],sprites[2],sprites[2],sprites[2] ],
    [sprites[0],sprites[2],sprites[2],sprites[2],sprites[2],sprites[2],sprites[2],sprites[2],sprites[2],sprites[0], sprites[2],sprites[0],sprites[2],sprites[0],sprites[2], sprites[2],sprites[2],sprites[2],sprites[2],sprites[2] ],
    [sprites[2],sprites[2],sprites[0],sprites[0],sprites[0],sprites[0],sprites[0],sprites[0],sprites[0],sprites[0], sprites[0],sprites[0],sprites[2],sprites[0],sprites[2], sprites[2],sprites[2],sprites[2],sprites[2],sprites[2] ]
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
    global wallImage
    global smileyImage
    global emptyImage
    
    nextStep = maze[charc_r][charc_c]
    
    if key == CODED:
        if keyCode == RIGHT:
            print("right")
            nextStep = maze[charc_r][charc_c + 1]
            
            if nextStep != wallImage:
                maze[charc_r][charc_c + 1] = smileyImage
                maze[charc_r][charc_c] = emptyImage
                charc_c = charc_c + 1
                
                

        elif keyCode == LEFT:
            print("left")

        elif keyCode == UP:
            print("up")

        elif keyCode == DOWN:
            print("down")
    print(charc_r , charc_c)
            
            
