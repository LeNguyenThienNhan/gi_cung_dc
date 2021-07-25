#...:))
import pygame, sys
import random
pygame.init()
pygame.font.init()

screen = pygame.display.set_mode((900, 500))

gamepos_x1 = 442.52
gamepos_x2 = 442.52

gamepos_y1 = random.randint(1,500)
gamepos_y2 = random.randint(1,500)


RED = (0,0,0)
left_colur = [255, 255, 255]
right_colour = [0, 102, 204]

score_1 = 0
score_2 = 0
scoretest_1 = 0
scoretest_2 = 0

pos1_x = 0
pos1_y = 200

pos2_x = 885
pos2_y = 200

#colour

run = True
#Toạ độ x,y
small_posx1 = 0
small_posy1 = 0

small_posx2 = 465
small_posy2 = 0

center_posx = 440
center_posy = 0

#font chữ

def font_score(score_1, score_2):
	font_score1 = pygame.font.Font('freesansbold.ttf', 20)
	fontsuf_score1 = font_score1.render('Score: %s' %score_1, True, RED)
	fontrect_score1 = fontsuf_score1.get_rect()
	fontrect_score1.center = (380,30)
	screen.blit(fontsuf_score1, fontrect_score1)

	font_score2 = pygame.font.Font('freesansbold.ttf', 20)
	fontsuf_score2 = font_score2.render('Score: %s' %score_2, True, RED)
	fontrect_score2 = fontsuf_score2.get_rect()
	fontrect_score2.center = (520,30)
	screen.blit(fontsuf_score2, fontrect_score2)

#game_play
def game_play(gamepos_x1, gamepos_x2):
	pygame.draw.rect(screen, (0, 0, 0), (gamepos_x1, gamepos_y1, 30,30))
	pygame.draw.rect(screen, (0, 0, 0), (gamepos_x2, gamepos_y2, 30,30))

#Chương trình
while run:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

#vẽ nền

	pygame.draw.rect(screen, (255 ,102, 102), (small_posx1, small_posy1, 450, 500))
	pygame.draw.rect(screen, (102, 178, 255), (small_posx2, small_posy2, 450, 500))
	pygame.draw.rect(screen, (0, 0, 0), (center_posx, center_posy, 30, 500))

#score

	font_score(score_1, score_2)

#di chuyển
	key = pygame.key.get_pressed() 
	if key[pygame.K_UP] and pos2_y - 1.5 >=0:
			pos2_y = pos2_y - 1.5
	if key[pygame.K_w] and pos1_y - 1.5 >=0:
			pos1_y = pos1_y - 1.5
	if key[pygame.K_DOWN] and pos2_y + 1.5 <= 430:
			pos2_y = pos2_y + 1.5
	if key[pygame.K_s] and pos1_y + 1.5 <= 430:
			pos1_y = pos1_y + 1.5

#luật
	if (gamepos_x1 == pos1_x) and (gamepos_y1 == pos1_y):
		score_1 = score_1 + 5
	if (gamepos_x2 == pos2_x) and (gamepos_y2 == pos2_y):
		score_2 = score_2 + 5
#ve
	pygame.draw.rect(screen, (102, 178, 255), (pos1_x, pos1_y, 15,70))
	pygame.draw.rect(screen, (255, 102, 102), (pos2_x, pos2_y, 15,70))

#tạo vật
	if score_1 != scoretest_1:
		gamepos_y1 = random.randint(1,430)
	if score_2 != scoretest_2:
		gamepos_y2 = random.randint(1,430)	

	game_play(gamepos_x1, gamepos_x2)
#bien
	gamepos_x1 = gamepos_x1 + 1
	gamepos_x2 = gamepos_x2 - 1 

	scoretest_1 = score_1
	scoretest_2 = score_2

	pygame.display.update()
	pygame.display.flip()

	
	

	


