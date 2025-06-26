import pygame
import random
import time 

#create screen
pygame.init()
screen = pygame.display.set_mode((490,600))
game_icon=pygame.image.load("game_icon.png")
pygame.display.set_icon(game_icon)
pygame.display.set_caption("2D Car game ")


#colours
white = (225, 255, 255)
black = (0 ,0, 0)
red = (255, 0,  0)
light_grey = (211, 211, 211)
darkgrey = ( 105, 105, 105)
yellow= (255, 255, 0)


#tick speed 
clock = pygame.time.Clock()



#font
font=pygame.font.Font("freesansbold.ttf", 20)
exit_font=pygame.font.Font("freesansbold.ttf",20)
score_font=pygame.font.SysFont("arialblack",30)

def message(msg,txt_colour, bkgd_colour, x_pos, y_pos):
   txt=font.render(msg, True, txt_colour, bkgd_colour)
   text_box=txt.get_rect(center=(x_pos,y_pos))
   screen.blit(txt, text_box)



def load_high_score():
    try:
        hi_score_file= open("HI_score.txt", 'r')
    except:
        hi_score_file = open("HI_score.txt", 'w')
        hi_score_file.write("0")
    hi_score_file = open("HI_score.txt", 'r')
    value= hi_score_file.read()
    hi_score_file.close()
    return value
   


#game loop
class cars:
    def __init__(self, y_location, x_location ,colour,):
        self.y_location = y_location
        self.x_location = x_location
        self.colour = colour
        self.speed= random.randint (10,20)
        
    def draw(self):
        enemy_car = pygame.draw.rect(screen,darkgrey ,(self.x_location, self.y_location, 50, 100))
        enemy_car_image = pygame.image.load(self.colour).convert_alpha()
        enemy_resized_car = pygame.transform.smoothscale(enemy_car_image, [ 50,100])
        screen.blit(enemy_resized_car, enemy_car )

  
   
        
    def move(self):
        self.y_location +=15
        if self.y_location > 600:
           self.speed = random.randint (10,20)
           self.y_location = random.randint(-500,-50)
          



    

   
first_car = cars(-400, 350, "car_2.png")
second_car = cars(-150, 230, "car_3.png")
third_car = cars(-280, 110, "car_4.png")



car_x =225
car_y = 380
car_x_change= 0
car_y_change= 0
score =0

high_score = load_high_score()
    
   
running = True
while running:
    for event in pygame.event.get():
       if event.type == pygame.quit:
           quit_game == True
       if event.type ==pygame.KEYDOWN:
           if event.key == pygame.K_LEFT:
               car_x_change = -20
               car_y_change = 0
           elif event.key == pygame.K_RIGHT:
               car_x_change = 20
               car_y_change = 0
               
         



            
               
    #background 
    screen.fill(light_grey)
    pygame.draw.rect(screen, darkgrey,(80, 0, 340,600))
    pygame.draw.rect( screen,yellow ,(180, 0, 20, 600))
    pygame.draw.rect( screen,yellow ,(310,0, 20, 600))
    first_car.draw()
    first_car.move()
    second_car.draw()
    second_car.move()
    third_car.draw()
    third_car.move()





 # traffic collisions
    
    old_car_rect = pygame.Rect(car_x, car_y, 50,85)


    for car in [first_car , second_car, third_car]:
        enemy_car_rect= pygame.Rect (car.x_location, car.y_location, 68,83)
        if old_car_rect.colliderect(enemy_car_rect):
           print("game over")
           game_over = True
           running = False
           
    
    if car_x < 90:
       car_x =90
    if car_x >470:
       car_x =470



      
    
    car_x += car_x_change
    car_y += car_y_change
    old_car= pygame.draw.rect(screen,darkgrey ,(car_x, car_y, 50, 100))
    car_image = pygame.image.load( "car_1.png"  ).convert_alpha()
    resized_car = pygame.transform.smoothscale(car_image, [ 50,100])
    screen.blit(resized_car, old_car )

   
    if car_x >= 1000 or car_x < 0 or car_y >= 900 or car_y < 0:
        quit_game = True


        
    
        
     
    score_msg="score:"+ str(score)
    highscore_msg = "high score:" + str(high_score)
    message (str(score_msg), white, black, 50,50)
    message (str(highscore_msg), white, black, 60,80)



    
    clock.tick(10)
    pygame.display.update()

    






    if (int(score))> (int(high_score)):
        message("NEW HIGH SCORE" , black, 500, 360)
        pygame.display.update()
        hi_score_file= open("HI_score.txt", 'w')
        hi_score_file.write( str (score))
        hi_score_file.close()


    
  



#screen update
screen.fill(light_grey)



