import pygame
from pygame.locals import *
import random

pygame.init()
running = True

# Fonts
font = pygame.font.Font(None, 50)

# Variable for size of screen
size = width, height = (900, 800)

# Screen size
screen = pygame.display.set_mode((size))

# Name of game
pygame.display.set_caption("Highway Outlaws")

# font for menu title "Highway Outlaws"
menu_font = ('PublicPixel-z84yD.ttf')
cus_font = pygame.font.Font(menu_font, 55)

# music/sound for main menu
car_acc_sound = pygame.mixer.Sound('car-engine-starting-43705.mp3')
car_acc_played = False

# Rimsha did this 
class MainMenu:
    def __init__ (self, screen, font, width, height):
        self.screen = screen 
        self.font = font
        self.width = width 
        self.height = height 

    def run(self):
        # Accesses the global variable
        global car_acc_played
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    # Pressing spacebar to play the game 
                if event.type == KEYDOWN and event.key == K_SPACE:
                    return 
            self.screen.fill((0, 0, 0))
            # playing the ignition for the main menu
            # checking if the sound hasn't been played yet
            if not car_acc_played:
                car_acc_sound.play()
                car_acc_played = True
            # The title of the game and the positioning
            title_text = cus_font.render("Highway Outlaws", True, (255, 255, 255))
            screen.blit(title_text, (width // 2 - title_text.get_width() // 2, height // 2 - title_text.get_height() * 2))
            # Instructions for the player
            drive_text = self.font.render("Press SPACE to Drive", True, (255, 255, 255)) 
            self.screen.blit(drive_text, (self.width // 2 - drive_text.get_width() // 2, self.height // 2 - drive_text.get_height() // 2))
            # Updating the display 
            pygame.display.flip()

# 
if __name__ == "__main__":
    pygame.init()
    width, height = 900, 800
    screen = pygame.display.set_mode((width, height)) 
    font = pygame.font.Font(None, 50)

    main_menu = MainMenu(screen, font, width, height)
    main_menu.run() 
# rimsha did coding till here 

# Play background music
pygame.mixer.music.load('former-102685.mp3')
# this loops the music throughout the gameplay
pygame.mixer.music.play(-1)

# Define a list of background images
background_images = ["grass.jpg", "trees.jpg", "water.jpg"]
current_background_index = 0


# Load the current background image
background_image = pygame.image.load(background_images[current_background_index])
background_image = pygame.transform.scale(background_image, (size))


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

# Load the images for coin
coin_image = pygame.image.load("money_1.png")

#size of image of coin
coin_width, coin_height = 40, 40

# Resize the images
coin_image = pygame.transform.scale(coin_image, (coin_width, coin_height))

#sound when player collects coins
coin_sound = pygame.mixer.Sound("mixkit-game-treasure-coin-2038.wav")

# Set the initial location of the coins
coin_loc = pygame.Rect(random.randint(100, width - 100), -100, coin_width, coin_height)

#visiblity for coins
coin_visible = True
#timer for coins
coin_interval = 150
coin_timer = 0

# Function to reset the position of the coin and keep within the players reach
def reset_coin_position():
    min_x = int(width / 2 - road_width / 2 + roadmarking_width * 4)
    max_x = int(width / 2 + road_width / 2 - roadmarking_width * 4 - coin_width)
    coin_loc.x = random.randint(min_x, max_x)
    coin_loc.y = -100

#amount of money collected
total_cash = 0

# Function to display the level completion message
def display_level_completion(screen, font, amount):
    screen.fill((64, 64, 64))
    level_complete_text = font.render(f"Level 1 Completed: You've escaped with £{amount}", True, (204, 204, 0))
    screen.blit(level_complete_text, (width // 2 - level_complete_text.get_width() // 2, height // 2 - level_complete_text.get_height() // 2))
    pygame.display.update()

# Game over message
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
                reset_coin_position()
                # Reset the timers
                coin_timer = 0
                # Reset visibility
                coin_visible = True
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
        if car_loc.colliderect(coin_loc):
            coin_sound.play()
            total_cash += 5
            # Move the coin off the screen when collected
            reset_coin_position()

        # Checking if the player has collected £30
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
        background_image = pygame.transform.scale(background_image, (size))

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

        # Adjusted time interval for the coin to appear
        if coin_timer < 500 and not coin_visible:
            coin_timer += 1
            if coin_timer == 500:
                reset_coin_position()
                coin_visible = True

        # Update the position of the coin if it's visible
        if coin_visible:
            coin_loc.y += 1
            if coin_loc.y > height:
                coin_visible = False
                coin_timer = 0

        # Display the total amount of money collected
        total_cash_text = font.render(f"Total Cash: £{total_cash} / £100", True, (204, 0, 0))
        screen.blit(total_cash_text, (20, 20))

        # displays the coin image
        screen.blit(coin_image, (coin_loc.x, coin_loc.y))

        #displays the player car image
        screen.blit(car, car_loc)
        #displays the enemy car image
        screen.blit(en1_car, en1_car_loc)
    

    # Update the display
    pygame.display.update()

pygame.quit()

# Our have been working on replit for the majority of the time. There will be comments of who did what and where.
