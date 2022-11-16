#source https://www.edureka.co/blog/snake-game-with-pygame/
#Task:
# Demonstrate your knowledge of Python by modifying a small simple game, “Hungry Snake”, where you need to demonstrate your knowledge of
# python syntax, use of 3 different data types, conditionals, loop, functions. Well commented and organised code will receive higher marks.
# Procedural or object-oriented approach to programming is appreciated. Modifications can include input from the  user, adding different levels
# with increasing difficulty, more snakes on screen, snakes with changing colours. Use your creativity!
#
# The code examples should be pushed to a private git repository.

import pygame
import random

pygame.init()

white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

dis_width = 600
dis_height = 400


dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game 00013277; 00013075 ')

# menu
start_img = pygame.image.load("Assets/start_btn.png").convert_alpha()
exit_img = pygame.image.load("Assets/exit_btn.png").convert_alpha()

# button class

class Button():
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self):
        action = False
        # get mouse position
        pos = pygame.mouse.get_pos()
        # check mousehover and clicked conditions
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        # draw button on screen
        dis.blit(self.image, (self.rect.x, self.rect.y))
        return  action

#create button instance
start_button = Button(100, 200, start_img, 0.5)
exit_button = Button(350, 200, exit_img, 0.5)

clock = pygame.time.Clock()

snake_block = 10
snake_speed = 15

snake_block2 = 10
snake_speed2 = 15

font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)


def Your_score(score):
    value = score_font.render("Your Score: " + str(score), True, white)
    dis.blit(value, [0, 0])
def User2_score(score):
    value = score_font.render("Your Score: " + str(score), True, white)
    dis.blit(value, [300, 0])

def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, yellow, [x[0], x[1], snake_block, snake_block])


def our_snake2 (snake_block2, snake_list2):
    for x in snake_list2:
        pygame.draw.rect(dis, green, [x[0], x[1], snake_block2, snake_block2])



def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])

run = True

while run:
    dis.fill((202, 228, 241))

    if start_button.draw():
        run = False
    if exit_button.draw():
        quit()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()

    def gameLoop():
        game_over = False
        game_close = False

        x1 = dis_width / 2
        y1 = dis_height / 2

        x2 = dis_width / 2
        y2 = dis_height / 2

        x1_change = 0
        y1_change = 0

        x2_change = 0
        y2_change = 0

        snake_List = []
        Length_of_snake = 1

        snake_List2 = []
        Length_of_snake2 = 1



        foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
        foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0



        while not game_over:

            while game_close == True:
                dis.fill(black)
                message("Game Over! Press C-Play Again or Q-Quit", red)
                Your_score(Length_of_snake - 1)
                User2_score(Length_of_snake2 - 1)
                pygame.display.update()

                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                            game_over = True
                            game_close = False
                        if event.key == pygame.K_c:
                            gameLoop()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        x1_change = -snake_block
                        y1_change = 0
                    elif event.key == pygame.K_RIGHT:
                        x1_change = snake_block
                        y1_change = 0
                    elif event.key == pygame.K_UP:
                        y1_change = -snake_block
                        x1_change = 0
                    elif event.key == pygame.K_DOWN:
                        y1_change = snake_block
                        x1_change = 0
            #         movement for 2 snack
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        x2_change = -snake_block2
                        y2_change = 0
                    elif event.key == pygame.K_d:
                        x2_change = snake_block2
                        y2_change = 0
                    elif event.key == pygame.K_w:
                        y2_change = -snake_block2
                        x2_change = 0
                    elif event.key == pygame.K_s:
                        y2_change = snake_block2
                        x2_change = 0

            if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0 and x2 >= dis_width or x2 < 0 or y2 >= dis_height or y2 < 0:
                game_close = True
            x1 += x1_change
            y1 += y1_change
            x2 += x2_change
            y2 += y2_change
            dis.fill(black)
            # comment
            pygame.draw.rect(dis, red, [foodx, foody, snake_block, snake_block])
            snake_Head = []
            snake_Head.append(x1)
            snake_Head.append(y1)
            snake_List.append(snake_Head)
            snake_Head2 = []
            snake_Head2.append(x2)
            snake_Head2.append(y2)
            snake_List2.append(snake_Head2)
            if len(snake_List) > Length_of_snake:
                del snake_List[0]
            if len(snake_List2) > Length_of_snake2:
                del snake_List2[0]

            for x in snake_List[:-1]:
                if x == snake_Head:
                    game_close = True

            our_snake(snake_block, snake_List)

            for x in snake_List2[:-1]:
                if x == snake_Head2:
                    game_close = True

            our_snake2(snake_block2, snake_List2)
            Your_score(Length_of_snake - 1)
            User2_score(Length_of_snake2 - 1)

            pygame.display.update()

            if x1 == foodx and y1 == foody:
                foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
                foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
                Length_of_snake += 1
            elif x2 == foodx and y2 == foody:
                foodx = round(random.randrange(0, dis_width - snake_block2) / 10.0) * 10.0
                foody = round(random.randrange(0, dis_height - snake_block2) / 10.0) * 10.0
                Length_of_snake2 += 1

            clock.tick(snake_speed2)

        pygame.quit()
        quit()

gameLoop()