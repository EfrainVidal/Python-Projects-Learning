import pygame
import random
from sys import exit # closes all code correctly
from random import randint, choice


class Player(pygame.sprite.Sprite): # create a player class for the sprite
    def __init__(self):
        super().__init__() # has to be here to intialize
        player_walk1 = pygame.image.load('UltimatePygameIntro-main/graphics/Player/player_walk_1.png').convert_alpha()
        player_walk2 = pygame.image.load('UltimatePygameIntro-main/graphics/Player/player_walk_2.png').convert_alpha()
        self.player_walk = [player_walk1, player_walk2]
        self.player_index = 0
        self.player_jump = pygame.image.load('UltimatePygameIntro-main/graphics/Player/jump.png').convert_alpha()

        self.image = self.player_walk[self.player_index]
        self.rect = self.image.get_rect(midbottom=(80, 300))
        self.gravity = 0

        self.jump_sound = pygame.mixer.Sound('UltimatePygameIntro-main/audio/jump.mp3')
        self.jump_sound.set_volume(0.01)

    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.rect.bottom >= 300:
            self.gravity = -20
            self.jump_sound.play()

    def apply_gravity(self):
        self.gravity += 1
        self.rect.y += self.gravity
        if self.rect.bottom >= 300:
            self.rect.bottom = 300

    def animation_state(self):
        if self.rect.bottom < 300:
            self.image = self.player_jump
        else:
            self.player_index += 0.1
            if self.player_index >= len(self.player_walk): self.player_index = 0
            self.image = self.player_walk[int(self.player_index)]

    def update(self):
        self.player_input()
        self.apply_gravity()
        self.animation_state()


class Obstacle(pygame.sprite.Sprite):
    def __init__(self, type):
        super().__init__()

        if type == 'fly':
            fly_1 = pygame.image.load('UltimatePygameIntro-main/graphics/fly/fly1.png').convert_alpha()
            fly_2 = pygame.image.load('UltimatePygameIntro-main/graphics/fly/fly2.png').convert_alpha()
            self.frames = [fly_1, fly_2]
            y_pos = 210
        else:
            snail_1 = pygame.image.load('UltimatePygameIntro-main/graphics/snail/snail1.png').convert_alpha()
            snail_2 = pygame.image.load('UltimatePygameIntro-main/graphics/snail/snail2.png').convert_alpha()
            self.frames = [snail_1, snail_2]
            y_pos = 300

        self.animation_index = 0
        self.image = self.frames[self.animation_index]  # always needed
        self.rect = self.image.get_rect(midbottom=(random.randint(900, 1100), y_pos))

    def animation_state(self):
        self.animation_index += 0.1
        if self.animation_index >= len(self.frames): self.animation_index = 0
        self.image = self.frames[int(self.animation_index)]

    def update(self):
        self.animation_state()
        self.rect.x -= 6
        self.destroy()

    def destroy(self):
        if self.rect.x <= -100:
            self.kill       # will destryo sprtie


def display_score():
    current_time = int(pygame.time.get_ticks() / 1000) - start_time    # time in milisecs - divide to set to secs
    score_surf = test_font.render(f'Score: {current_time}', False, (64, 64, 64))
    score_rect = score_surf.get_rect(center=(400, 50))
    screen.blit(score_surf, score_rect)
    return current_time


# def obstacle_movement(obstacle_list):
#     if obstacle_list:   # if list is not empty do this
#         for obstacle_rect in obstacle_list:
#             obstacle_rect.x -= 5     # move obstacles
#
#             if obstacle_rect.bottom == 300: screen.blit(snail_surf, obstacle_rect) # draw snail or fly based on bottom level
#             else: screen.blit(fly_surface, obstacle_rect)
#
#         obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x > -100] # check if enemy is too far to left
#
#         return obstacle_list
#     else: return []


# def collisions(player, obstacles):
    # if obstacles:
        # for obstacle_rect in obstacles:
            # if player.colliderect(obstacle_rect): return False
    # return True

def collision_sprite():
    if pygame.sprite.spritecollide(player.sprite, obstacle_group, False):
        obstacle_group.empty()
        return False
    else: return True


# def player_animation():
    # global player_surf, player_index

    # if player_rect.bottom < 300:
        # Jump
        # player_surf = player_jump
    # else:
        # walk
        # player_index += 0.1 # change walk surface slower to look better
        # if player_index >= len(player_walk) : player_index = 0 # restart back to 0 in list
        # player_surf = player_walk[int(player_index)]
    # play walking animation if player on floor
    # display jump surface when player not on floor


pygame.init()       # necessary to start
screen = pygame.display.set_mode((800, 400))    # create playsurface
pygame.display.set_caption('Runner')    # set title of window
clock = pygame.time.Clock()     # controls frame rate
test_font = pygame.font.Font('UltimatePygameIntro-main/font/Pixeltype.ttf', 50)      # creates a font in pygame (font type, size)
game_active = False
start_time = 0  # var for time
score = 0
bg_music = pygame.mixer.Sound('UltimatePygameIntro-main/audio/music.wav')
bg_music.set_volume(0.02)
bg_music.play(loops=-1)     # loop sounds forever


# Groups
player = pygame.sprite.GroupSingle()   # create instance of class
player.add(Player())

obstacle_group = pygame.sprite.Group()

sky_surface = pygame.image.load('UltimatePygameIntro-main/graphics/Sky.png').convert()
ground_surface = pygame.image.load('UltimatePygameIntro-main/graphics/ground.png').convert() # convert makes the game faster

# score_surface = test_font.render('My Game', False, (64,64,64))
# score_rect = score_surface.get_rect(center=(400, 25))   # centers the words

# Snail
# snail_frame_1 = pygame.image.load('UltimatePygameIntro-main/graphics/snail/snail1.png').convert_alpha() # removes weird block around snail
# snail_frame_2 = pygame.image.load('UltimatePygameIntro-main/graphics/snail/snail2.png').convert_alpha() # removes weird block around snail
# snail_frames = [snail_frame_1, snail_frame_2]
# snail_frame_index = 0
# snail_surf = snail_frames[snail_frame_index]

# Fly
# fly_frame_1 = pygame.image.load('UltimatePygameIntro-main/graphics/fly/fly1.png').convert_alpha()
# fly_frame_2 = pygame.image.load('UltimatePygameIntro-main/graphics/fly/fly2.png').convert_alpha()
# fly_frames = [fly_frame_1, fly_frame_2]
# fly_frame_index = 0
# fly_surface = fly_frames[fly_frame_index]

obstacle_rect_list = []

# player_walk1 = pygame.image.load('UltimatePygameIntro-main/graphics/Player/player_walk_1.png').convert_alpha()
# player_walk2 = pygame.image.load('UltimatePygameIntro-main/graphics/Player/player_walk_2.png').convert_alpha()
# player_walk = [player_walk1, player_walk2]
# player_index = 0
# player_jump = pygame.image.load('UltimatePygameIntro-main/graphics/Player/jump.png').convert_alpha()

# player_surf = player_walk[player_index]
# player_rect = player_surf.get_rect(bottomright=(80, 300))    # create a rectangle around the surface image, choose point
# player_gravity = 0  # creates a var for gravity

# Intro Screen
player_stand = pygame.image.load('UltimatePygameIntro-main/graphics/Player/player_stand.png').convert_alpha()
player_stand = pygame.transform.rotozoom(player_stand, 0, 2)     # scale the played to make bigger overriding the var
player_stand_rect = player_stand.get_rect(center=(400, 200))

game_name = test_font.render('Pixel Runner', False, (111, 196, 169))
game_name_rect = game_name.get_rect(center=(400, 80))

game_message = test_font.render('Press Space to Run', False, (111, 196, 169))
game_message_rect = game_message.get_rect(center=(400, 340))

# Timer
obstacle_timer = pygame.USEREVENT + 1   # add +1 to all timer events added
pygame.time.set_timer(obstacle_timer, 1500)     # when to trigger event

# snail_animation_timer = pygame.USEREVENT + 2
# pygame.time.set_timer(snail_animation_timer, 400)
#
# fly_animation_timer = pygame.USEREVENT + 3
# pygame.time.set_timer(fly_animation_timer, 200)

while True:
    for event in pygame.event.get():    # gets player input(event)
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if game_active:
            # mouse
            # if event.type == pygame.MOUSEBUTTONDOWN and player_rect.bottom >= 300:    # jump if mouse clicked on player
            #     if player_rect.collidepoint(event.pos):
            #         player_gravity = -20

            # Keyboard
            # if event.type == pygame.KEYDOWN:    # check for keys pressed
            #     if event.key == pygame.K_SPACE and player_rect.bottom >= 300:     # what to do if space is pressed
            #         player_gravity = -20

            if event.type == obstacle_timer:
                obstacle_group.add(Obstacle(choice(['fly', 'snail', 'snail', 'snail'])))
                # if randint(0,2):     # random true or false
                #    obstacle_rect_list.append(snail_surf.get_rect(bottomright=(randint(900, 1100), 300))) # random space
                # else:
                #    obstacle_rect_list.append(fly_surface.get_rect(bottomright=(randint(900, 1100), 210))) # random space

            # if event.type == snail_animation_timer:
            #     if snail_frame_index == 0: snail_frame_index = 1
            #     else: snail_frame_index = 0
            #     snail_surf = snail_frames[snail_frame_index]
            #
            # if event.type == fly_animation_timer:
            #     if fly_frame_index == 0: fly_frame_index = 1
            #     else: fly_frame_index = 0
            #     fly_surf = fly_frames[fly_frame_index]

        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:    # start game is not playing
                game_active = True
                # snail_rect.left = 800
                start_time = int(pygame.time.get_ticks() / 1000)


    # Game Screen
    if game_active:
        # Screen Surface
        screen.blit(sky_surface, (0, 0))     # puts surface on screen
        screen.blit(ground_surface, (0, 300))
        # pygame.draw.rect(screen, '#c0e8ec', score_rect)  # draw using rectangle
        # pygame.draw.rect(screen, '#c0e8ec', score_rect, 10)  # draw using rectangle
        # screen.blit(score_surface, score_rect)
        score = display_score()

        # Snail
        #snail_rect.x -= 4   # move the snail to the left
        #if snail_rect.right <= 0: snail_rect.left = 800       # respawn on the
        #screen.blit(snail_surf, snail_rect)  # place the snail on the screen

        # Player
        # player_gravity += 1
        # player_rect.y += player_gravity     # moves player down
        # if player_rect.bottom >= 300: player_rect.bottom = 300   # don't let player pass ground
        # player_animation()
        # screen.blit(player_surf, player_rect)
        player.draw(screen) # draw sprites
        player.update() # update sprites

        obstacle_group.draw(screen)
        obstacle_group.update()

        # Obstacle Movement
        # obstacle_rect_list = obstacle_movement(obstacle_rect_list)  # override the new list

        # Collision
        game_active = collision_sprite()
        # game_active = collisions(player_rect, obstacle_rect_list)
        # if snail_rect.colliderect(player_rect):  # ends game if player collides with snail
        # game_active = False

    # Game Over Screen
    else:
        screen.fill((94, 129, 162))
        screen.blit(player_stand, player_stand_rect)
        obstacle_rect_list.clear()
        # player_rect.midbottom = (80, 300)
        player_gravity = 0

        score_message = test_font.render(f'Your Score: {score}', False, (111, 196, 169))
        score_message_rect = score_message.get_rect(center=(400, 330))
        screen.blit(game_name, game_name_rect)

        if score == 0: screen.blit(game_message, game_message_rect)     # display score instead of press space
        else: screen.blit(score_message, score_message_rect)


    # draw all elements
    # update everything
    pygame.display.update()
    clock.tick(60)      # how many frames per sec max