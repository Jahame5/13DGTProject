import pygame
pygame.init()
import random 

#create screen 
screen = pygame.display.set_mode((600,600))
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


#game loop 


class cars:
    def __init__(self, y_location, x_location ,colour,):
        self.y_location = y_location
        self.x_location = x_location
        self.colour = colour
        
        
    def draw(self):
        enemy_car = pygame.draw.rect(screen,darkgrey ,(self.x_location, self.y_location, 50, 100))
        enemy_car_image = pygame.image.load(self.colour).convert_alpha()
        enemy_resized_car = pygame.transform.smoothscale(enemy_car_image, [ 50,100])
        screen.blit(enemy_resized_car, enemy_car )


   
        
    def move(self):
        self.y_location +=25
        if self.y_location > 600:
          self.y_location = random.randint(-500,-50)

              
        
   
first_car = cars(-300, 450, "car_2.png")
second_car = cars(-150, 300, "car_3.png")
third_car = cars(-260, 100, "car_4.png")




car_x =290
car_y = 380


car_x_change= 0
car_y_change= 0



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
    pygame.draw.rect(screen, darkgrey,(70, 0, 470, 600, ))
    pygame.draw.rect( screen,yellow ,(200, 0, 20, 600))
    pygame.draw.rect( screen,yellow ,(400,0, 20, 600))
    first_car.draw()
    first_car.move()
    second_car.draw()
    second_car.move()
    third_car.draw()
    third_car.move()
    
    
    
    
    car_x += car_x_change
    car_y += car_y_change
    old_car= pygame.draw.rect(screen,darkgrey ,(car_x, car_y, 50, 100))
    car_image = pygame.image.load( "car_1.png"  ).convert_alpha()
    resized_car = pygame.transform.smoothscale(car_image, [ 50,100])
    screen.blit(resized_car, old_car )

   
    if car_x >= 1000 or car_x < 0 or car_y >= 900 or car_y < 0:
        quit_game = True

        
    


   
    clock.tick(13)
    pygame.display.update()








#screen update
draw_ground()
screen.fill(light_grey)
