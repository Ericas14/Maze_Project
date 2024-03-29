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
    global levelCompl
    global nextLevel
    global level2img
    global begin
    global startpg
    global alienImage
    global lockImage
    global empty2Image
    global key2Image
    global planetsImage
    global endImage
    
    obtainedKey = False
    levelCompl = False
    nextLevel = False
    begin = False
    size(600,600)
    background(255, 255, 255)
    sprite = []
    emptyImage = loadImage("empty.jpg")
    smileyImage = loadImage("smiley.jpg")
    grassImage = loadImage("grass.jpg")
    keyImage = loadImage("key.jpg")
    lock2Image = loadImage("lock2.jpg")
    level2img = loadImage("glowmazelevel2.jpg")
    startpg = loadImage("startImage.jpg")
    alienImage = loadImage("alien.jpg")
    lockImage = loadImage("lock.png")
    empty2Image = loadImage("empty2.jpg")
    key2Image = loadImage("key.png")
    planetsImage = loadImage("planets.png")
    endImage = loadImage("glowmazeend.jpg")
    
    
    if begin == False:
        image(startpg, 0, 0, 600,600)
        
    if nextLevel == True:
        background(255,255,255)
        
    
    charc_r = 0
    charc_c = 2
    if nextLevel == False:
        sprites = [ emptyImage, smileyImage, grassImage, keyImage, lock2Image]
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
        [sprites[0],sprites[2],sprites[2],sprites[2],sprites[2],sprites[2],sprites[2],sprites[2],sprites[2],sprites[0], sprites[2],sprites[0],sprites[2],sprites[4],sprites[2], sprites[2],sprites[2],sprites[2],sprites[2],sprites[2] ],
        [sprites[2],sprites[2],sprites[2],sprites[2],sprites[2],sprites[2],sprites[2],sprites[2],sprites[2],sprites[0], sprites[0],sprites[0],sprites[2],sprites[0],sprites[2], sprites[2],sprites[2],sprites[2],sprites[2],sprites[2] ]
        ] #                                                                                                                                              key was here
    

def draw():
    global sprites  
    global maze 
    global levelCompl
    global nextLevel
    global level2img 
    global begin
    global startpg
    global charc_r
    global charc_c
    global alienImage
    global lockImage
    global empty2Image
    global key2Image
    global planetsImage
    global endImage

    
    if mousePressed:
          if mouseX in range (218,381) and mouseY in range (264,314):
            begin = True
    if begin == True: 
        background(255,255,255)      
        for row in range(len(maze)):
            for col in range(20):
                sprite = maze[row][col]
                image(sprite, col*30, row*30)
                
    
                
    if charc_r == 19 and charc_c == 13:
        levelCompl = True
        if nextLevel == False:
            image(level2img, 0,0,600,600)
            
    if keyPressed and key == "c" and levelCompl == True:
            nextLevel = True
            levelCompl = False
            charc_c = 1
            charc_r = 1
            obtainedKey = False
            sprites =[ empty2Image, alienImage, planetsImage, key2Image, lockImage]
            maze = [
    [sprites[2],sprites[2],sprites[2],sprites[2],sprites[2],sprites[2],sprites[2],sprites[2],sprites[2],sprites[2], sprites[2],sprites[2],sprites[2],sprites[2],sprites[2], sprites[2],sprites[2],sprites[2],sprites[2],sprites[2] ],
    [sprites[2],sprites[1],sprites[0],sprites[2],sprites[2],sprites[2],sprites[2],sprites[2],sprites[0],sprites[0], sprites[0],sprites[0],sprites[0],sprites[0],sprites[0], sprites[0],sprites[0],sprites[0],sprites[2],sprites[2] ],
    [sprites[2],sprites[2],sprites[0],sprites[2],sprites[2],sprites[2],sprites[2],sprites[2],sprites[0],sprites[2], sprites[0],sprites[0],sprites[2],sprites[2],sprites[2], sprites[0],sprites[2],sprites[0],sprites[2],sprites[2] ],
    [sprites[2],sprites[2],sprites[0],sprites[0],sprites[0],sprites[0],sprites[0],sprites[0],sprites[0],sprites[2], sprites[0],sprites[0],sprites[2],sprites[2],sprites[2], sprites[0],sprites[2],sprites[0],sprites[0],sprites[2] ],
    [sprites[2],sprites[2],sprites[2],sprites[2],sprites[2],sprites[2],sprites[2],sprites[2],sprites[2],sprites[2], sprites[0],sprites[0],sprites[2],sprites[2],sprites[0], sprites[0],sprites[2],sprites[2],sprites[0],sprites[2] ],
    [sprites[2],sprites[2],sprites[0],sprites[0],sprites[0],sprites[2],sprites[2],sprites[0],sprites[0],sprites[0], sprites[0],sprites[0],sprites[2],sprites[2],sprites[2], sprites[2],sprites[2],sprites[2],sprites[0],sprites[2] ],
    [sprites[2],sprites[2],sprites[0],sprites[2],sprites[0],sprites[2],sprites[2],sprites[0],sprites[2],sprites[0], sprites[2],sprites[0],sprites[2],sprites[2],sprites[2], sprites[2],sprites[2],sprites[2],sprites[0],sprites[2] ],
    [sprites[2],sprites[2],sprites[0],sprites[2],sprites[0],sprites[2],sprites[2],sprites[0],sprites[2],sprites[0], sprites[2],sprites[2],sprites[2],sprites[2],sprites[2], sprites[2],sprites[2],sprites[2],sprites[0],sprites[2] ],
    [sprites[2],sprites[2],sprites[0],sprites[2],sprites[0],sprites[2],sprites[2],sprites[0],sprites[2],sprites[0], sprites[2],sprites[0],sprites[2],sprites[2],sprites[2], sprites[2],sprites[2],sprites[2],sprites[0],sprites[2] ],
    [sprites[2],sprites[0],sprites[0],sprites[2],sprites[0],sprites[0],sprites[0],sprites[0],sprites[2],sprites[0], sprites[2],sprites[2],sprites[2],sprites[2],sprites[0], sprites[0],sprites[0],sprites[2],sprites[0],sprites[2] ],
    [sprites[2],sprites[0],sprites[2],sprites[2],sprites[0],sprites[2],sprites[2],sprites[2],sprites[2],sprites[2], sprites[2],sprites[2],sprites[2],sprites[2],sprites[0], sprites[0],sprites[0],sprites[0],sprites[0],sprites[2] ],
    [sprites[2],sprites[0],sprites[2],sprites[2],sprites[0],sprites[2],sprites[2],sprites[0],sprites[0],sprites[0], sprites[2],sprites[0],sprites[2],sprites[2],sprites[2], sprites[2],sprites[2],sprites[2],sprites[0],sprites[2] ],
    [sprites[2],sprites[0],sprites[2],sprites[2],sprites[2],sprites[2],sprites[2],sprites[0],sprites[2],sprites[0], sprites[2],sprites[2],sprites[2],sprites[2],sprites[2], sprites[2],sprites[2],sprites[2],sprites[0],sprites[2] ],
    [sprites[2],sprites[0],sprites[0],sprites[0],sprites[0],sprites[0],sprites[2],sprites[0],sprites[2],sprites[0], sprites[2],sprites[2],sprites[0],sprites[2],sprites[2], sprites[2],sprites[2],sprites[2],sprites[0],sprites[2] ],
    [sprites[2],sprites[0],sprites[2],sprites[0],sprites[2],sprites[0],sprites[2],sprites[0],sprites[2],sprites[0], sprites[2],sprites[0],sprites[0],sprites[2],sprites[2], sprites[2],sprites[2],sprites[2],sprites[0],sprites[2] ],
    [sprites[2],sprites[0],sprites[2],sprites[0],sprites[2],sprites[0],sprites[2],sprites[0],sprites[2],sprites[2], sprites[2],sprites[0],sprites[2],sprites[2],sprites[2], sprites[2],sprites[2],sprites[2],sprites[0],sprites[2] ],
    [sprites[2],sprites[0],sprites[2],sprites[0],sprites[2],sprites[0],sprites[0],sprites[0],sprites[2],sprites[2], sprites[2],sprites[0],sprites[2],sprites[2],sprites[2], sprites[3],sprites[2],sprites[2],sprites[0],sprites[2] ],
    [sprites[2],sprites[0],sprites[2],sprites[0],sprites[2],sprites[0],sprites[2],sprites[2],sprites[2],sprites[2], sprites[2],sprites[0],sprites[2],sprites[2],sprites[2], sprites[0],sprites[2],sprites[2],sprites[0],sprites[2] ],
    [sprites[2],sprites[0],sprites[2],sprites[0],sprites[2],sprites[0],sprites[0],sprites[0],sprites[0],sprites[0], sprites[0],sprites[0],sprites[0],sprites[0],sprites[0], sprites[0],sprites[2],sprites[2],sprites[4],sprites[2] ],
    [sprites[2],sprites[2],sprites[2],sprites[2],sprites[2],sprites[2],sprites[2],sprites[2],sprites[2],sprites[2], sprites[2],sprites[2],sprites[2],sprites[2],sprites[2], sprites[2],sprites[2],sprites[2],sprites[0],sprites[2] ]
        ]
            
    if charc_r == 19 and charc_c == 18:
        image(endImage, 0,0,600,600)
            
def keyPressed():
    global charc_c
    global charc_r
    global grassImage
    global smileyImage
    global emptyImage
    global obtainedKey
    global keyImage
    global lock2Image
    global nextLevel
    
    nextStep = maze[charc_r][charc_c]
    if nextLevel == False:
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
                    
    if nextLevel == True:
          if key == CODED:
            if keyCode == RIGHT and charc_c != 19:
                print("right")
                nextStep = maze[charc_r][charc_c + 1]
                
                if nextStep != planetsImage:
                    maze[charc_r][charc_c + 1] = alienImage
                    maze[charc_r][charc_c] = empty2Image
                    charc_c = charc_c + 1
                    
                if nextStep == keyImage:
                    obtainedKey = True
                                
    
            elif keyCode == LEFT and charc_c != 0:
                print("left")
                nextStep = maze[charc_r][charc_c - 1]
                
                if nextStep != planetsImage:
                    maze[charc_r][charc_c - 1] = alienImage
                    maze[charc_r][charc_c] = empty2Image
                    charc_c = charc_c - 1
    
            elif keyCode == UP and charc_r != 0:
                print("up")
                nextStep = maze[charc_r - 1][charc_c]
                
                if nextStep != planetsImage:
                    maze[charc_r - 1][charc_c] = alienImage
                    maze[charc_r][charc_c] = empty2Image
                    charc_r = charc_r - 1
                                
    
            elif keyCode == DOWN and charc_r != 19:
                print("down")
                nextStep = maze[charc_r + 1][charc_c]
                
                if obtainedKey == True and nextStep != planetsImage:
                    maze[charc_r + 1][charc_c] = alienImage
                    maze[charc_r][charc_c] = empty2Image
                    charc_r = charc_r + 1
                elif nextStep != planetsImage and nextStep != lockImage:
                    maze[charc_r + 1][charc_c] = alienImage
                    maze[charc_r][charc_c] = empty2Image
                    charc_r = charc_r + 1
    print(charc_r , charc_c)
    #print(obtainedKey)
    print(nextLevel)
