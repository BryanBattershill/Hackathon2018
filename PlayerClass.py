import time

class PlayerClass:

    #VARS
    lives
    buffer
    def __init__(self):
        #CONSTRUCTER
        lives = 3
        buffer = 0

    def damage():
        lives = lives - 1
        dead()
        if buffer !=0:
            buffer = time.time() - buffer
        else:
            buffer = time.time()
        if buffer > 2:
            buffer = 0;
        
    def dead():
        return lives==0

    
