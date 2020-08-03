import pygame
import random
import math
#initialize pygame to use it
pygame.init()
#create window with pygame.display.set_mode((widht,heigth))
screen = pygame.display.set_mode((800,600))
#to change the caption of the window
pygame.display.set_caption("Space_Invaders")
#to change the icon of the window
icon =  pygame.image.load("alien.png")
pygame.display.set_icon(icon)
#background image
bg=pygame.image.load("sky.jpg")
#player(hero) image and co-ordinates
playerImg=pygame.image.load("spaceship.png")
playerX=370
playerY=480
#for the movement of player left and right
playerX_change=0
#player function to draw image on screen,call in loop
def player(playerX,playerY):
    #screen.blit(Image,(x,y cordinates))
    screen.blit(playerImg,(playerX,playerY))
# Enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 5
for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('C:\\Users\\deepapranav\\Downloads\\enemy.png'))
    enemyX.append(random.randint(0, 736))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(3)
    enemyY_change.append(40)
#enemy function to draw image on screen,call in loop
def enemy(X,Y,i):
    #screen.blit(Image,(x,y cordinates))
    screen.blit(enemyImg[i],(X,Y))
#bullet
#create bullet
# x same as player and y decreases from 480 to 0
# two states of bullet ready and fire
#ready-bullet doesnt appear on screen
#fire-bullet moves up
bullet= pygame.image.load('C:\\Users\\deepapranav\\Downloads\\bullet.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 25
bullet_state = "ready"
#same as player y
bullet_state="ready"
# function to fire the bullet, call when space bar is hit
def fire_bullet(x,y):
    global bullet_state
    bullet_state = "fire"
    #these addition to co-orinates make firing lookfrom centre n top nose of spaceship
    screen.blit(bullet,(x+16,y+10))
#collision of obejects
#use distance between 2 co-ordinates maths formula
def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemyX - bulletX, 2) + (math.pow(enemyY - bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False
#set score to 0
score_value = 0
#to display text on screen
font = pygame.font.Font('freesansbold.ttf', 32)
#co-ordiantes of where text message appear
textX = 10
testY = 10
#show on screen
def show_score(x, y):
    #text must be first rendered with value to be displayed,display or hide,color
    score = font.render("Score : " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))
# Game Over
over_font = pygame.font.Font('freesansbold.ttf',64)
#shows game over on screen when it is called
def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (200, 250))
    
#create a loop that runs till user quits the window
running = True
while running:
    #change background of screen using screen.fill((r,g,b))
    screen.fill((100,50,50))
    #making backgroud persist
    screen.blit(bg,(0,0))
    #check which event was chosen by the user
    for event in pygame.event.get():
        #check if user wants to quit by pressing cancel on top right(break while loop)
        if event.type == pygame.QUIT:
            running=False
            #to close the window
            pygame.quit()
        #key board event
        #check if any key is pressed
        if event.type == pygame.KEYDOWN:
            #check if it is left arrow key
            if event.key == pygame.K_LEFT:
                #we want to move the player to left so decreasex co-ordinate
                playerX_change=-4
            #check if it is right arrow key
            if event.key == pygame.K_RIGHT:
                 #we want to move the player to left so increase  x co-ordinate
                 playerX_change=4
            #check if space bar is pressed to fire
            if event.key == pygame.K_SPACE:
                if bullet_state=="ready":
                   # Get the current x cordinate of the spaceship 
                   bulletX=playerX
                   fire_bullet(bulletX,bulletY)
        #check if the key is released
        if event.type == pygame.KEYUP:
            #check if its either left or right arrow
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                #we have to stop the movement as the key is released
                playerX_change=0
    playerX+=playerX_change
    #to avoid the Player go beyond the screen on left
    if playerX < 0:
        playerX = 0
    # on right as size of image is 64pix (800-64=736)    
    elif playerX >= 736:
        playerX = 736    
    #enemy movement
    for i in range(num_of_enemies):
        # Game Over when any enemy reaches y=440
        if enemyY[i] > 440:
            for j in range(num_of_enemies):
                #all enemies disappear from screen
                enemyY[j] = 2000
            #displays game over    
            game_over_text()
            break
        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = 3
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736:
            enemyX_change[i] = -3
            enemyY[i] += enemyY_change[i]
        # Collision
        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            bulletY = 480
            bullet_state = "ready"
            score_value+=10
            enemyX[i] = random.randint(0, 736)
            enemyY[i] = random.randint(30, 150)

        enemy(enemyX[i], enemyY[i],i)
       
    #bullet movement
    #bullet disappers beyond the scene so only 1 bullet can be fired so get it back
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"

    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    player(playerX, playerY)
    #call the function to display score
    show_score(textX, testY)
    #update the change on window
    pygame.display.update()
    
    
