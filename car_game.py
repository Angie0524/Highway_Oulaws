# Main menu function
import pygame
from pygame.locals import *
import random

pygame.init()
running = True

# Name of game
pygame.display.set_caption("Highway Outlaws")

# font for menu title "Highway Outlaws"
menu_font = ('PublicPixel-z84yD.ttf')
cus_font = pygame.font.Font(menu_font, 55)

class MainMenu:
    def __init__ (self, screen, font, width, height):
        self.screen = screen 
        self.font = font
        self.width = width 
        self.height = height 

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    # Pressing spacebar to play the game 
                if event.type == KEYDOWN and event.key == K_SPACE:
                    return 
            self.screen.fill((0, 0, 0))
            # The title of the game and the positioning
            title_text = cus_font.render("Highway Outlaws", True, (255, 255, 255))
            screen.blit(title_text, (width // 2 - title_text.get_width() // 2, height // 2 - title_text.get_height() * 2))
            drive_text = self.font.render("Press SPACE to Drive", True, (255, 255, 255)) 
            self.screen.blit(title_text, (self.width // 2 - title_text.get_width() // 2, self.height // 2 - title_text.get_height() // 2))
            # Updating the display 
            pygame.display.flip()
# Example usage 
if __name__ == "__main__":
    pygame.init()
    width, height = 900, 800
    screen = pygame.display.set_mode((width, height)) 
    font = pygame.font.Font(None, 50)

    main_menu = MainMenu(screen, font, width, height)
    main_menu.run() 
        

# Play background music
pygame.mixer.music.load('former-102685.mp3')
# this loops the music throughout the gameplay
pygame.mixer.music.play(-1)

# Define a list of background images
background_images = ["grass.jpg", "trees.jpg", "water.jpg"]
current_background_index = 0


# Load the current background image
background_image = pygame.image.load(background_images[current_background_index])
background_image = pygame.transform.scale(background_image, (width, height))


# Define initial background position
background_y = 0


# Default speeds
def_scrolling_speed = 0.35
def_player_speed = 2.5
def_en_car_speed = 1


# Size of road and roadmarkings
road_width = int(width/1.8)
roadmarking_width = int(width/80)
r_lane = width/2 + road_width/4
l_lane = width/2 - road_width/4


# Load the car image
car = pygame.image.load("player_car.png")
# Define the desired dimensions for the car
new_width, new_height = 90, 160
# Resize the car image
car = pygame.transform.scale(car, (new_width, new_height))
# Display and location of the car on the screen
car_loc = car.get_rect()
car_loc = pygame.Rect(width/2 - road_width/4 - 40, height*0.85 - 80, 80, 160)


# Load the opposing car image
en1_car = pygame.image.load("enemy_car1.png")
# Define the desired dimensions for the opposing car
new_width, new_height = 90, 160
# Resize the opposing car image
en1_car = pygame.transform.scale(en1_car, (new_width, new_height))
# Display and location of the opposing car on the screen
en1_car_loc = en1_car.get_rect()
en1_car_loc = pygame.Rect(l_lane - 40, height*0.25 - 80, 80, 160)

#oskar edited this coin part
class Coin:
    def __init__(self, image_path, width, height, sound_path):
        self.image = pygame.image.load(image_path)
        self.width = width
        self.height = height
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.sound = pygame.mixer.Sound(sound_path)
        self.visible = True
        self.interval = 150
        self.timer = 0
        self.location = pygame.Rect(random.randint(100, width - 100), -100, self.width, self.height)
        
    def reset_position(self, road_width, roadmarking_width, width, height):
        min_x = int(width / 2 - road_width / 2 + roadmarking_width * 4)
        max_x = int(width / 2 + road_width / 2 - roadmarking_width * 4 - self.width)
        self.location.x = random.randint(min_x, max_x)
        self.location.y = -100

    def play_sound(self):
        self.sound.play()

    def move(self):
        if self.timer < 500 and not self.visible:
            self.timer += 1
            if self.timer == 500:
                self.reset_position(road_width, roadmarking_width, width, height)
                self.visible = True

        if self.visible:
            self.location.y += 1
            if self.location.y > height:
                self.visible = False
                self.timer = 0

    def draw(self, screen):
        screen.blit(self.image, (self.location.x, self.location.y))

#amount of money collected
total_cash = 0

# Function to display the level completion message
def display_level_completion(screen, font, amount):
    screen.fill((64, 64, 64))
    level_complete_text = font.render(f"Level 1 Completed: You've escaped with £{amount}", True, (204, 204, 0))
    screen.blit(level_complete_text, (width // 2 - level_complete_text.get_width() // 2, height // 2 - level_complete_text.get_height() // 2))
    pygame.display.update()

# Game over message (Amara)
game_over_text = font.render("You Got Caught!", True, (255, 0, 0))
running = True
game_over = False

#game over image
game_over_image = pygame.image.load("police_car.gif")
game_over_image = pygame.transform.scale(game_over_image, (width, height))

# Game over sound
game_over_sound = pygame.mixer.Sound('police-siren-21498.mp3')
game_over_police = pygame.mixer.Sound('police-quotwe-have-you-surroundedquot-pa-system-168595.mp3')

#game loop
while running:

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

        if event.type == KEYDOWN:
            # Restart the game if the game is over and the user presses the 'R' key
            if game_over and event.key == pygame.K_r:
                game_over = False
                pygame.mixer.music.play(-1)
                game_over_sound.stop()
                game_over_police.stop()
                # Reset the player car location
                car_loc = pygame.Rect(width / 2 - road_width / 4 - new_width / 2, height * 0.85 - new_height / 2, new_width, new_height)
                # Reset the enemy car location
                en1_car_loc.center = (l_lane - new_width / 2, -200)
                # Reset the total amount of cash
                total_cash = 0
                # Reset the positions of coins and money
                coin.reset_position(road_width, roadmarking_width, width, height)
                # Reset the timers
                coin.timer = 0
                # Reset visibility
                coin.visible = True
            # Quit the game if the user presses the 'Q' key
            if event.key == pygame.K_q:
                running = False

    if running:
        #moving the player car into the left lane or right lane by used arrow key or WASD
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            if car_loc.centerx > l_lane:
                #how fast the player should shift into the left lane
                car_loc.centerx -= def_player_speed

        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            if car_loc.centerx < r_lane:
                #how fast the player should shift into the right lane
                car_loc.centerx += def_player_speed


    #animate the oncoming vehicle
    en1_car_loc[1] += 1
    en1_car_loc.y += def_en_car_speed
    if en1_car_loc[1] > height:
        if random.randint(0,1) == 0:
            #shift the enemy into the right lane
            en1_car_loc.center = r_lane, -200
        else:
            #shift the enemy car into the left lane
            en1_car_loc.center = l_lane, -200 

    # Check for collision between enemy and player car
    if running and not game_over:
        if car_loc.colliderect(en1_car_loc):
            game_over = True

        # Check for collision and collect money
        if car_loc.colliderect(en1_car_loc):
            game_over = True

        # Check for collision with coins and play sound for coin collecting
           if car_loc.colliderect(coin.location) and coin.visible:
               coin.play_sound()
               total_cash += 5
               #move the coin off the screen when collected
               coin.reset_position(road_width, roadmarking_width, width, height)

        # Checking if the player has collected £100
        if total_cash >= 100:
            display_level_completion(screen, font, total_cash)
            pygame.time.delay(3000)
            pygame.mixer.music.stop()
            running = False

    # How fast the bachground should scroll
    background_y += def_scrolling_speed

    if background_y >= background_image.get_height():
        # Resets the background position
        background_y = 0
        # Chooses a random backgrouqnd image
        current_background_index = random.randint(0, len(background_images) - 1)
        background_image = pygame.image.load(background_images[current_background_index])
        background_image = pygame.transform.scale(background_image, (width, height))

    # Draw the two background images
    screen.blit(background_image, (0, background_y))
    screen.blit(background_image, (0, background_y - background_image.get_height()))

    # Road shape, colour, and coordinates
    pygame.draw.rect(
        screen,
        (50, 50, 50),
        (width / 2 - road_width / 2, 0, road_width, height))

    # Yellow road marking in the middle
    pygame.draw.rect(
        screen,
        (255, 240, 60),
        (width / 2 - roadmarking_width / 2, 0, roadmarking_width, height))

    # White road markings on the left
    pygame.draw.rect(
        screen,
        (255, 255, 255),
        (width / 2 - road_width / 2 + roadmarking_width * 2, 0, roadmarking_width, height))

    # White road markings on the right
    pygame.draw.rect(
        screen,
        (255, 255, 255),
        (width / 2 + road_width / 2 - roadmarking_width * 3, 0, roadmarking_width, height))
    
    if game_over:
        #Playing police siren sound
        game_over_sound.play()
        game_over_police.play(0)
        screen.blit(game_over_image, (0, 0))
        screen.blit(game_over_text, (width // 2 - game_over_text.get_width() // 2, height // 2 - game_over_text.get_height() // 2))
        game_over_instructions = font.render("Press 'R' to restart or 'Q' to quit", True, (255, 255, 255))
        screen.blit(game_over_instructions, (width // 2 - game_over_instructions.get_width() // 2, height // 2 + game_over_text.get_height()))
        pygame.mixer.music.stop()

    #oskar edited this part
    if not game_over:
        
        #display the coin
        if coin.visible:
            coin.move()
            coin.draw(screen)

        # Display the total amount of money collected
        total_cash_text = font.render(f"Total Cash: £{total_cash} / £100", True, (204, 0, 0))
        screen.blit(total_cash_text, (20, 20))

        # displays the coin image
        coin.draw(screen)

        #displays the player car image
        screen.blit(car, car_loc)
        #displays the enemy car image
        screen.blit(en1_car, en1_car_loc)
    

    # Update the display
    pygame.display.update()

pygame.quit()

# My team and I have been working on replit for the majority of the time. There will be comments of who did what and where.
