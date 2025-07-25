import pygame
import random
import time 


#create screen
pygame.init()
screen = pygame.display.set_mode((520,600))
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

def message(msg,txt_colour,  x_pos, y_pos):
   txt=font.render(msg, True, txt_colour, )
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
        global score
        self.y_location +=10
        if self.y_location > 600:
           self.speed = random.randint (10,20)
           self.y_location = random.randint(-500,-50)
           score += 1
          



    

   
first_car = cars(-600, 410, "car_2.png")
second_car = cars(-1000,290 , "car_3.png")
third_car = cars(-200, 170, "car_4.png")
fourth_car = cars(-450, 60, "car_5.png")



car_x =225
car_y = 380
car_x_change= 0
car_y_change= 0
score = 0

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
    pygame.draw.rect(screen, darkgrey,(40, 0, 435,600))
    pygame.draw.rect( screen,yellow ,(250, 0, 20, 600))
    pygame.draw.rect( screen,yellow ,(367,0, 20, 600))
    pygame.draw.rect( screen,yellow ,(130,0, 20, 600))
    first_car.draw()
    first_car.move()
    second_car.draw()
    second_car.move()
    third_car.draw()
    third_car.move()
    fourth_car.draw()
    fourth_car.move()
   
     
          
# walls 

    if car_x < 60:
       car_x =60
    if car_x >400:
       car_x =400

       

    
    car_x += car_x_change
    car_y += car_y_change
    old_car= pygame.draw.rect(screen,darkgrey ,(car_x, car_y, 50, 100))
    car_image = pygame.image.load( "car_1.png"  ).convert_alpha()
    resized_car = pygame.transform.smoothscale(car_image, [ 50,100])
    screen.blit(resized_car, old_car )

   
    if car_x >= 1000 or car_x < 0 or car_y >= 900 or car_y < 0:
        quit_game = True

        





# traffic collision
 
    old_car_rect = pygame.Rect(car_x, car_y, 50,85)
   

    for car in [first_car, second_car, third_car, fourth_car]:
        enemy_car_rect= pygame.Rect (car.x_location, car.y_location, 68 ,83)
        if old_car_rect.colliderect(enemy_car_rect):
           if car.y_location > 600:
              score += 1
              screen.fill(white)

              pygame.display.update()

            

           
           game_over = message("GAME OVER!" , black , 260 , 270)
           game_over = True
           running = False


           if (int(score))> (int(high_score)):
               pygame.display.update()
               game_over = message("NEW HIGH SCORE" , black , 260 , 300)
               game_over=True 


               
             
        
    
    hi_score_file= open("HI_score.txt", 'w')
    hi_score_file.write( str (score))
    hi_score_file.close()

           
        
     
    score_msg="score:"+ str(score)
    highscore_msg = "high score:" + str(high_score)
    message (str(score_msg), black,  50,50)
    message (str(highscore_msg), black,  80,80)


  






     
                                                            


       
    clock.tick(13)
    pygame.display.update()


          


        
 
                
    
        



#screen update
screen.fill(light_grey)



