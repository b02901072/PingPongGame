#-*- coding: utf-8
import pygame,sys,random,string,math
pygame.init()
screen_width,screen_height = 960,640
mid_width,mid_height = 0.5*screen_width,0.5*screen_height
screen = pygame.display.set_mode((screen_width,screen_height),0,32)
bif = "tech.jpg" 
background = pygame.image.load(bif).convert()
sound1,sound2 = pygame.mixer.Sound("01.wav"),pygame.mixer.Sound("02.wav")
winner,scorer = "",""
gamestate = "home_page"
ball_r = [0,16,16,16]
bar_half_length = [0,40,40]
bar_width = 8
bar_screen_space = 20
score1,score2 = 0,0
winscore = 3
gm_select = 1
dm_select = 1
timepm = 0
setduel_select = 1
setball_select = 1
setbar_select = 1
setoth_select = 1
setsc_select = 1
sound = 1
ball_x = [0,0,0,0]
ball_y = [0,0,0,0]
ball_sizelv = 3
ball_num = 1
ball_speedlv = 4
ball_basicspeedx = [0,300,299,298]
ball_basicspeedy = [0,300,299,298]
ball_setspeedx = [0,300,299,298]
ball_setspeedy = [0,300,299,298]
ball_speedx = [0,300,299,298]
ball_speedy = [0,300,299,298]
ball_acceltemptspeedx = [0,300,299,298]
ball_acceltemptspeedy = [0,300,299,298]
ball_gratemptspeedx = [0,300,299,298]
ball_gratemptspeedy = [0,300,299,298]
ball_basicspeed = [0,500,500,500]
ball_speed = [0,500,500,500]
ball_dirangle = [0,45,45,45]
bar_lengthlv = 3
bar_speedlv = 2
bar_freemove = 0
bar_basicspeed = [0,400,400]
bar_speed = [0,400,400]
bar_dirx = [0,0,0]
bar_diry = [0,0,0]
bar_x = [0,0,0]
bar_y = [0,0,0]
gra_accel = 350
ball_aceelratio = 1.5
ball_accelstatus = [0,0,0,0]
dm_style = [0,0,0,0,0,0,0,0]  # 雷射1、加速2、隱形3、亂彈4、重力5、震動6、蟲洞7 #
maxtime = 90
timelimit = 1
com_diffculty = 2
control = 1
timeout = 0
blspeedtime = 0
blspeedexhibitx = 0
brspeedtime = 0
brspeedexhibity =320
brspeedexhibitx = 0
bar_exhibitdirx = 0
bar_exhibitdiry = 1
curve = 0
curvepm = 0
dis_ballwh = [0,[0,0,0],[0,0,0],[0,0,0]]
wh_y = [0,0,0]
ballwh = [0,0,0,0]
ball_vis = [0,1,1,1]
gra_status = 0
gra_ran=0
laser_status = 0
laser_time = 0
laser_outtime = 0
dmmodeon = 0
dmmodeonmax = 0
breakrecord = 0
gra_status = 0
accel_dir = 1
cd_status = 1
pause_status = 0  
pic_o_p = pygame.image.load("one_player2.jpg").convert() 
exhibit_bls = pygame.image.load("small_tech.jpg").convert() 
exhibit_brs = pygame.image.load("long_tech.jpg").convert() 
exhibit_gm = pygame.image.load("gamemode.jpg").convert() 
control_w = pygame.image.load("50_50_tech_w.jpg").convert() 
control_s = pygame.image.load("50_50_tech_s.jpg").convert() 
control_a = pygame.image.load("50_50_tech_a.jpg").convert() 
control_d = pygame.image.load("50_50_tech_d.jpg").convert() 
control_up = pygame.image.load("50_50_tech_up.jpg").convert() 
control_down = pygame.image.load("50_50_tech_down.jpg").convert() 
control_left = pygame.image.load("50_50_tech_left.jpg").convert() 
control_right = pygame.image.load("50_50_tech_right.jpg").convert() 
control_30_w = pygame.image.load("30_tech_w.jpg").convert() 
control_30_s = pygame.image.load("30_tech_s.jpg").convert() 
control_30_up = pygame.image.load("30_tech_up.jpg").convert() 
control_30_down = pygame.image.load("30_tech_down.jpg").convert()
red_warning = pygame.image.load("red_warning.jpg").convert()
top_margin = pygame.image.load("960_60_tech.jpg").convert()
blackhole_70 = pygame.image.load("70_blackhole_light.jpg").convert()
blackhole_56 = pygame.image.load("56_blackhole_light.jpg").convert()
laser_50 = pygame.image.load("50_50_tech_laser.jpg").convert()
accel_50 = pygame.image.load("50_50_tech_accel.jpg").convert()
invis_50 = pygame.image.load("50_50_tech_invis.jpg").convert()
bounce_50 = pygame.image.load("50_50_tech_bounce.jpg").convert()
gra_50 = pygame.image.load("50_50_tech_gra.jpg").convert()
vibrate_50 = pygame.image.load("50_50_tech_vibrate.jpg").convert()
wh_50 = pygame.image.load("50_50_tech_wh.jpg").convert()
laser_50_dark = pygame.image.load("50_50_tech_laser_dark.jpg").convert()
accel_50_dark = pygame.image.load("50_50_tech_accel_dark.jpg").convert()
invis_50_dark = pygame.image.load("50_50_tech_invis_dark.jpg").convert()
bounce_50_dark = pygame.image.load("50_50_tech_bounce_dark.jpg").convert()
gra_50_dark = pygame.image.load("50_50_tech_gra_dark.jpg").convert()
vibrate_50_dark = pygame.image.load("50_50_tech_vibrate_dark.jpg").convert()
wh_50_dark = pygame.image.load("50_50_tech_wh_dark.jpg").convert()
control_down_dark = pygame.image.load("50_50_tech_down_dark.jpg").convert() 
ball_alive = [0,0,0,0]
ball_start = [0,0,0,0]
setcat_select = 3
record_top5 = [0,[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]
gamescore = [0,0,0,0,0,0,0]
breakrecord,newhigh = 0,0
scorechange = 0
load_percentage = 0
load_add = 0
temptgamestate = ""
h = [40,40,40,40,40,40,40,40,40,40,40]
hr = [40,40,40,40,40,40]
hrc = [0,255,255,255,255,255]
def quit_game():
	pygame.display.quit()
	pygame.quit()
	sys.exit()
def fabs(x):
	if x >= 0:
		return x
	if x < 0:
		return -x
def froot2(x):
	i = 0.5 * x
	while fabs( x - i*i ) >= 0.01:
		i = 0.5* ( i + x/i )
	root = int(i*100) / 100	
	return root
def sur_1p_highscore():
	f = open( 'sur_1p_highscore.txt' , 'r+')
	a1 = f.readline()
	record_top5[3][1] = string.atoi(a1)	
	a2 = f.readline()
	record_top5[3][2] = string.atoi(a2)
	a3 = f.readline()
	record_top5[3][3] = string.atoi(a3)
	a4 = f.readline()
	record_top5[3][4] = string.atoi(a4)
	a5 = f.readline()
	record_top5[3][5] = string.atoi(a5)
	f.close()	
def sur_2p_highscore():
	f = open( 'sur_2p_highscore.txt' , 'r+')
	a1 = f.readline()
	record_top5[4][1] = string.atoi(a1)	
	a2 = f.readline()
	record_top5[4][2] = string.atoi(a2)
	a3 = f.readline()
	record_top5[4][3] = string.atoi(a3)
	a4 = f.readline()
	record_top5[4][4] = string.atoi(a4)
	a5 = f.readline()
	record_top5[4][5] = string.atoi(a5)
	f.close()	
def drawlefttri(a,b,c,d):
	#			/	|	      
	#		/		| d
	#	/	  c		|
	#	------------- b
	#	\		i	|
	#		\		| d
	#			\	|
	#
	#				a
	i = a
	while i <= a and i >= a-c :
		h = int (d*(i-a+c)/c)
		pygame.draw.line(screen, (255,204,0), (i,b-h), (i,b+h), 1)
		i -= 1
def drawrighttri(a,b,c,d):
	#	|	\
	# d |		\
	#	|	  c		\
	#	------------- b
	#	|	i		/
	#	|		/
	#	|	/
	#
	#	a
	i = a
	while i >= a and i <= a+c :
		h = int (d*(a+c-i)/c)
		pygame.draw.line(screen, (255,204,0), (i,b-h), (i,b+h), 1)
		i += 1
def catch_1p_highscore():
	f = open( 'catch_1p_highscore.txt' , 'r+')
	a1 = f.readline()
	record_top5[5][1] = string.atoi(a1)	
	a2 = f.readline()
	record_top5[5][2] = string.atoi(a2)
	a3 = f.readline()
	record_top5[5][3] = string.atoi(a3)
	a4 = f.readline()
	record_top5[5][4] = string.atoi(a4)
	a5 = f.readline()
	record_top5[5][5] = string.atoi(a5)
	f.close()	
def catch_2p_highscore():
	f = open( 'catch_2p_highscore.txt' , 'r+')
	a1 = f.readline()
	record_top5[6][1] = string.atoi(a1)	
	a2 = f.readline()
	record_top5[6][2] = string.atoi(a2)
	a3 = f.readline()
	record_top5[6][3] = string.atoi(a3)
	a4 = f.readline()
	record_top5[6][4] = string.atoi(a4)
	a5 = f.readline()
	record_top5[6][5] = string.atoi(a5)
	f.close()	
def cos(x):
	a = math.radians(x)
	ans = math.cos(a)
	return ans
def sin(x):
	a = math.radians(x)
	ans = math.sin(a)
	return ans
def calculate_ball_speedxy():
	for i in [1,2,3]:
		ball_speedx[i] = ball_speed[i]*cos(ball_dirangle[i])
		ball_speedy[i] = ball_speed[i]*sin(ball_dirangle[i])
def calculate_ball_speed():
	for i in [1,2,3]:
		ball_speed[i] = math.hypot(ball_speedx[i],ball_speedy[i])
def calculate_ball_dirangle():
	for i in [1,2,3]:
		ball_dirangle[i] = math.degrees(math.atan2(ball_speedy[i],ball_speedx[i]))
def re_ball_dirangle():
	for i in [1,2,3]:
		ball_dirangle[i] = ball_dirangle[i]%360
def posi_nega(x):
	if x > 0:
		return 1
	elif x < 0: 
		return -1
	else:
		return 0	
while True:	
	sur_1p_highscore()
	sur_2p_highscore()
	catch_1p_highscore()
	catch_2p_highscore()
	if gamestate == "home_page":
		screen.blit(background,(0,0))
		screen.blit(pygame.font.SysFont('Times New Roman', 120).render("Ping Pong Game", True, (171,171,171)), (80, 200))
		screen.blit(pygame.font.SysFont('Times New Roman', 30).render("Ver_1.01", True, (204,204,204)), (750, 330))
		screen.blit(pygame.font.SysFont('Times New Roman', 40).render("Press any button but ESC to continue", True, (255, 255, 255)), (190, 370))
		screen.blit(pygame.font.SysFont('Times New Roman', 30).render("Press Space to move on to the next page.", True, (255, 255, 255)), (180, 440))
		screen.blit(pygame.font.SysFont('Times New Roman', 30).render("Press Backspace to go back to the previous page.", True, (255, 255, 255)), (180, 490))
		screen.blit(pygame.font.SysFont('Times New Roman', 30).render("Press ESC to quit the game.", True, (255, 255, 255)), (180, 540))
		for events in pygame.event.get():
			if events.type == pygame.KEYDOWN:	
				if events.key == pygame.K_ESCAPE:
					quit_game()
				else:
					gamestate = 'gamemode'
		pygame.display.update()
	if gamestate == 'gamemode': 
		screen.blit(background,(0,0))
		gm_fontsize = [0,40,40,40,40,40,40]
		screen.blit(exhibit_gm,(370,200))
		gm_fontsize[gm_select] = 50
		gm_circley = 75+70*gm_select
		if gm_select == 1:
			screen.blit(pygame.font.SysFont('Times New Roman', 35).render("Player VS Computer", True, (255, 255, 255)), (525, 500))
		elif gm_select == 2:
			screen.blit(pygame.font.SysFont('Times New Roman', 35).render("Player VS Player", True, (255, 255, 255)), (525, 500))
		elif gm_select == 3:
			screen.blit(pygame.font.SysFont('Times New Roman', 35).render("Don't miss the ball.", True, (255, 255, 255)), (500, 455))
			screen.blit(pygame.font.SysFont('Times New Roman', 35).render("How long can you survive ?", True, (255, 255, 255)), (450, 500))
		elif gm_select == 4:
			screen.blit(pygame.font.SysFont('Times New Roman', 35).render("[Cooperation Mode]", True, (255, 255, 255)), (500, 500))
		elif gm_select == 5:
			screen.blit(pygame.font.SysFont('Times New Roman', 35).render("Catch the balls as many times", True, (255, 255, 255)), (425, 455))
			screen.blit(pygame.font.SysFont('Times New Roman', 35).render("as possible within 90 seconds.", True, (255, 255, 255)), (450, 500))
		elif gm_select == 6:
			screen.blit(pygame.font.SysFont('Times New Roman', 35).render("[Cooperation Mode]", True, (255, 255, 255)), (500, 500))
		screen.blit(pygame.font.SysFont('Times New Roman', 80).render("Ping Pong Game", True, (171,171,171)), (30, 15))
		screen.blit(pygame.font.SysFont('Times New Roman', gm_fontsize[1]).render("Duel_1P", True, (255, 255, 255)), (80, 120))
		screen.blit(pygame.font.SysFont('Times New Roman', gm_fontsize[2]).render("Duel_2P", True, (255, 255, 255)), (80, 190))
		screen.blit(pygame.font.SysFont('Times New Roman', gm_fontsize[3]).render("Survival_1P", True, (255, 255, 255)), (80, 260))
		screen.blit(pygame.font.SysFont('Times New Roman', gm_fontsize[4]).render("Survival_2P", True, (255, 255, 255)), (80, 330))
		screen.blit(pygame.font.SysFont('Times New Roman', gm_fontsize[5]).render("CatchBall_1P", True, (255, 255, 255)), (80, 400))
		screen.blit(pygame.font.SysFont('Times New Roman', gm_fontsize[6]).render("CatchBall_2P", True, (255, 255, 255)), (80, 470))
		pygame.draw.circle(screen, (102,204,255), (60,gm_circley),6,0)
		#---------------------------Gamemode_Picture----------------------------#
		if gm_select == 1 or gm_select == 2 or gm_select == 5 or gm_select == 6:
			screen.blit(pygame.font.SysFont('Times New Roman', 20).render("90", True, (255, 255, 255)), (635, 210))
		screen.blit(pygame.font.SysFont('Times New Roman', 25).render("P1", True, (0, 0, 255)), (380, 220))
		pygame.draw.line(screen, (0,0,255), (385,330-20), (385,330+20), 4)			
		pygame.draw.circle(screen, (204,255,255), (700,440), 8,0)	
		screen.blit(control_30_w,(373,270))
		screen.blit(control_30_s,(373,360))
		if gm_select == 1:
			screen.blit(pygame.font.SysFont('Times New Roman', 25).render("Com", True, (0, 255, 0)), (850, 320))
			pygame.draw.line(screen, (0,255,0), (888,410-20), (888,410+20), 4)
		if gm_select == 2:
			screen.blit(pygame.font.SysFont('Times New Roman', 25).render("P2", True, (255, 0, 0)), (870, 320))
			pygame.draw.line(screen, (255,0,0), (888,410-20), (888,410+20), 4)	
			screen.blit(control_30_up,(875,350))
			screen.blit(control_30_down,(875,440))
		if gm_select == 4 or gm_select == 6:
			screen.blit(pygame.font.SysFont('Times New Roman', 25).render("P2", True, (255, 0, 0)), (415, 320))
			pygame.draw.line(screen, (255,0,0), (430,410-20), (430,410+20), 4)	
			screen.blit(control_30_up,(418,350))
			screen.blit(control_30_down,(418,440))
		if gm_select == 3 or gm_select == 4 or gm_select == 5 or gm_select == 6:
			screen.blit(pygame.font.SysFont('Times New Roman', 20).render("Score : 0", True, (255, 255, 255)), (800,210))
		pygame.display.update()
		for events in pygame.event.get():
			if events.type == pygame.KEYDOWN:	
				if events.key == pygame.K_ESCAPE:
					quit_game()
				elif events.key == pygame.K_SPACE:
					dm_style = [0,0,0,0,0,0,0,0]
					if gm_select == 1 or gm_select == 2:
						bar_speed[2] = bar_speed[1]
						ball_x[1],ball_y[1] = 730,350
						clockpm = pygame.time.Clock()
						gamestate = "duelmode"						
					if gm_select == 3 or gm_select == 4:
						gamestate = "setting_surcat"
					if gm_select == 5 or gm_select == 6:
						gamestate = "setting_surcat"
				elif events.key == pygame.K_BACKSPACE:
					gamestate = "home_page"
				elif events.key == pygame.K_TAB or events.key == pygame.K_s or events.key == pygame.K_DOWN:
					gm_select += 1
					if gm_select == 7:
						gm_select = 1
				elif events.key == pygame.K_w or events.key == pygame.K_UP :
					gm_select -= 1
					if gm_select == 0:
						gm_select = 6
	if gamestate == "duelmode":
		screen.blit(background,(0,0))
		gamescore[3],gamescore[5] = 0,0
		dm_fontsize = [0,40,40,40,40,40,40,40,30]
		dm_fontsize[dm_select] = dm_fontsize[dm_select] + 10
		if dm_select != 8:
			screen.blit(exhibit_bls,(550,200))
			dm_circley = 85+60*dm_select
			if dm_style[dm_select] == 1:
				drawlefttri(405,90+60*dm_select,20,15)
			if dm_style[dm_select] == 0:
				drawrighttri(500,90+60*dm_select,20,15)
		if dm_select == 1:
			screen.blit(laser_50,(550,200))
			screen.blit(pygame.font.SysFont('Times New Roman', 20).render("You'll lose immediately if you're", True, (255, 255, 255)), (565, 420))
			screen.blit(pygame.font.SysFont('Times New Roman', 20).render("hit by a laser ray,", True, (255, 255, 255)), (565, 445))
			screen.blit(pygame.font.SysFont('Times New Roman', 20).render("or lose 5 points in CatchBall.", True, (255, 255, 255)), (565, 470))
		elif dm_select == 2:
			screen.blit(accel_50,(550,200))
			screen.blit(pygame.font.SysFont('Times New Roman', 20).render("The accelerator will increase the ball's", True, (255, 255, 255)), (565, 445))
			screen.blit(pygame.font.SysFont('Times New Roman', 20).render("speed by 1.5 until it hits a bar.", True, (255, 255, 255)), (565, 470))
		elif dm_select == 3:
			screen.blit(invis_50,(550,200))
			pygame.draw.line(screen, (200,200,200), (550+90,200), (550+90,500), 2)
			pygame.draw.line(screen, (200,200,200), (550+270,200), (550+270,500), 2)
			screen.blit(pygame.font.SysFont('Times New Roman', 20).render("Fortunately, the ball won't be invisible", True, (255, 255, 255)), (565, 445))
			screen.blit(pygame.font.SysFont('Times New Roman', 20).render("when its speed is accelerated.", True, (255, 255, 255)), (565, 470))
		elif dm_select == 4:
			screen.blit(bounce_50,(550,200))
			screen.blit(pygame.font.SysFont('Times New Roman', 20).render("The direction of the ball after it hits", True, (255, 255, 255)), (565, 445))
			screen.blit(pygame.font.SysFont('Times New Roman', 20).render("a surface is unpredictable", True, (255, 255, 255)), (565, 470))
		elif dm_select == 5:
			screen.blit(gra_50,(550,200))
			screen.blit(pygame.font.SysFont('Times New Roman', 20).render("The direction of the gravity field", True, (255, 255, 255)), (565, 445))
			screen.blit(pygame.font.SysFont('Times New Roman', 20).render("varies every 5 seconds.", True, (255, 255, 255)), (565, 470))
		elif dm_select == 6:
			screen.blit(vibrate_50,(550,200))
			screen.blit(pygame.font.SysFont('Times New Roman', 20).render("It will be difficult to predict", True, (255, 255, 255)), (565, 445))
			screen.blit(pygame.font.SysFont('Times New Roman', 20).render("where the ball is heading for.", True, (255, 255, 255)), (565, 470))
		elif dm_select == 7:
			screen.blit(wh_50,(550,200))
			screen.blit(pygame.font.SysFont('Times New Roman', 20).render("When a ball enters a wormhole, it'll", True, (255, 255, 255)), (565, 445))
			screen.blit(pygame.font.SysFont('Times New Roman', 20).render("come out from the other one.", True, (255, 255, 255)), (565, 470))
		elif dm_select == 8:
			dm_circley =585
		pygame.draw.circle(screen, (102,204,255), (60,dm_circley),6,0)
		screen.blit(pygame.font.SysFont('Times New Roman', 80).render("Duel_Mode", True, (171,171,171)), (30,15))
		screen.blit(pygame.font.SysFont('Times New Roman', dm_fontsize[1]).render("Laser", True, (255, 255, 255)), (80, 120))
		screen.blit(pygame.font.SysFont('Times New Roman', dm_fontsize[2]).render("Acceleration", True, (255, 255, 255)), (80, 180))
		screen.blit(pygame.font.SysFont('Times New Roman', dm_fontsize[3]).render("Invisibility", True, (255, 255, 255)), (80, 240))
		screen.blit(pygame.font.SysFont('Times New Roman', dm_fontsize[4]).render("CrazyBounce", True, (255, 255, 255)), (80, 300))
		screen.blit(pygame.font.SysFont('Times New Roman', dm_fontsize[5]).render("Gravity", True, (255, 255, 255)), (80, 360))
		screen.blit(pygame.font.SysFont('Times New Roman', dm_fontsize[6]).render("Vibration", True, (255, 255, 255)), (80, 420))
		screen.blit(pygame.font.SysFont('Times New Roman', dm_fontsize[7]).render("Wormhole", True, (255, 255, 255)), (80, 480))
		screen.blit(pygame.font.SysFont('Times New Roman', dm_fontsize[8]).render("Continue", True, (255, 255, 255)), (80, 570))
		for i in [1,2,3,4,5,6,7]:
			if dm_style[i] == 1:
				screen.blit(pygame.font.SysFont('Times New Roman', dm_fontsize[i]-5).render("On", True, (255, 255, 255)), (420, 65+60*i))	
			elif dm_style[i] == 0:
				screen.blit(pygame.font.SysFont('Times New Roman', dm_fontsize[i]-5).render("Off", True, (255, 255, 255)), (420, 65+60*i))
		for events in pygame.event.get():
			if events.type == pygame.KEYDOWN:	
				if events.key == pygame.K_ESCAPE:
					quit_game()
				if (events.key == pygame.K_d or events.key == pygame.K_RIGHT) and dm_select != 8 and dm_style[dm_select] == 0:
					dm_style[dm_select] = 1
				if (events.key == pygame.K_a or events.key == pygame.K_LEFT) and dm_select != 8 and dm_style[dm_select] == 1:
					dm_style[dm_select] = 0
				if events.key == pygame.K_SPACE and dm_select == 8:
					ball_speedx[1],ball_speedy[1] = 300,300
					calculate_ball_speed()
					calculate_ball_dirangle()
					gamestate = "setting_duel"
				if events.key == pygame.K_BACKSPACE:
					gamestate = 'gamemode'
				if events.key == pygame.K_TAB or events.key == pygame.K_s or events.key == pygame.K_DOWN:
					ball_x[1],ball_y[1] = 730,350
					ball_speedx[1],ball_speedy[1] = 350,350
					calculate_ball_speed()
					calculate_ball_dirangle()
					dm_select += 1
					if dm_select == 9:
						dm_select = 1
					if dm_select == 5:
						ball_speedx[1],ball_speedy[1] = 400,400
				if events.key == pygame.K_w or events.key == pygame.K_UP :
					ball_x[1],ball_y[1] = 730,350
					ball_speedx[1],ball_speedy[1] = 350,350
					calculate_ball_speed()
					calculate_ball_dirangle()
					dm_select -= 1
					if dm_select == 0:
						dm_select = 8
					if dm_select == 5:
						ball_speedx[1],ball_speedy[1] = 400,400
		#=============================計算時間 BEGIN=============================#
		millipm = clockpm.tick()
		secondspm = millipm/1000.0
		timepm += millipm
		#=============================計算時間 END=============================#
		calculate_ball_speedxy()
		ball_x[1] += secondspm*ball_speedx[1]
		ball_y[1] += secondspm*ball_speedy[1]
		#-----------------------------左邊的邊緣BEGIN---------------------------#
		if ball_y[1] >= 500:
			ball_y[1] = 485
			ball_speedy[1] = -400
		if ball_x[1] < 565 and  ball_speedx[1] < 0:
			ball_accelstatus[1] = 0
			if dm_select != 4:
				ball_speedx[1] = -ball_speedx[1]
				calculate_ball_dirangle()
			if dm_select == 4:
				rrx1 = 2*random.random()
				if rrx1 < 1:
					ball_dirangle[1] = 30*random.random() + 30
				elif rrx1 >= 1 and rrx1 < 2:
					ball_dirangle[1] = 30*random.random() + 300	
				calculate_ball_speedxy()
		#-----------------------------右邊的邊緣BEGIN---------------------------#
		elif ball_x[1] > 885 and ball_speedx[1] > 0:
			ball_accelstatus[1] = 0
			if dm_select != 4:
				ball_speedx[1] = -ball_speedx[1]
				calculate_ball_dirangle()
			if dm_select == 4:
				rrx1 = 2*random.random()
				if rrx1 < 1:
					ball_dirangle[1] = 30*random.random() + 120
				elif rrx1 >= 1 and rrx1 < 2:
					ball_dirangle[1] = 30*random.random() + 210
				calculate_ball_speedxy()
		#-----------------------------上方的邊緣BEGIN---------------------------#
		if ball_y[1] < 210 and ball_speedy[1] < 0 :
			ball_accelstatus[1] = 0
			if dm_select != 4:
				ball_speedy[1] = -ball_speedy[1]
				calculate_ball_dirangle()
			if dm_select == 4:
				rrx1 = 2*random.random()
				if rrx1 < 1:
					ball_dirangle[1] = 30*random.random() + 30
				elif rrx1 >= 1 and rrx1 < 2:
					ball_dirangle[1] = 30*random.random() + 120
				calculate_ball_speedxy()
		#-----------------------------下方的邊緣BEGIN---------------------------#
		if ball_y[1] > 490 and ball_speedy[1] > 0:
			ball_accelstatus[1] = 0
			if dm_select != 4:
				ball_speedy[1] = -ball_speedy[1]
				calculate_ball_dirangle()
			if dm_select == 4:
				rrx1 = 2*random.random()
				if rrx1 < 1:
					ball_dirangle[1] = 30*random.random() + 210
				elif rrx1 >= 1 and rrx1 < 2:
					ball_dirangle[1] = 30*random.random() + 300
				calculate_ball_speedxy()
		#------------------------------Gravity---------------------------#
		if dm_select == 5:
			screen.blit(control_down,(600,200))
			ball_speedy[1] += 800*secondspm
			calculate_ball_speed()
			calculate_ball_dirangle()
		#---------------------------Acceleration----------------------------#
		if dm_select != 2:
			ball_accelstatus[1] = 0
		if dm_select == 2:
			pygame.draw.line(screen, (255,102,0), (730,310-5), (730,390+5), 130)
			pygame.draw.line(screen, (255,255,0), (730,310), (730,390), 120)
			for i in [1,2,3,4]:
				pygame.draw.line(screen, (0,255,0), (730+12*(2*i-1)-60,310+8), (730+12*(2*i+1)-60,310+40), 8)
				pygame.draw.line(screen, (0,255,0), (730+12*(2*i-1)-60,310+72), (730+12*(2*i+1)-60,310+40), 8)
			if ball_x[1] <= 790  and ball_x[1] >= 670 and ball_y[1] >= 310 and ball_y[1] <= 390 and ball_accelstatus[1] == 0:
				ball_speedx[1],ball_speedy[1] = 700,700
				calculate_ball_speed()
				ball_accelstatus[1] = 1
			if ball_accelstatus[1] == 0:
				ball_speedx[1],ball_speedy[1] = 400,400
				calculate_ball_speed()
		#---------------------------Vibration------------------------------#
		if dm_select == 6:
			if timepm%60 <= 5 and curvepm == 0:
				curve_ran = 5*random.random()
				if curve_ran < 4:
					ball_dirangle[1] = -ball_dirangle[1]
					re_ball_dirangle()
					calculate_ball_speedxy
				curvepm = 1
			if timepm%60 >= 50:
				curvepm = 0
		#---------------------------Wormhole--------------------------------#
		if dm_select == 7:
			pygame.draw.circle(screen, (255,255,255), (640,350), 42,0)
			pygame.draw.circle(screen, (255,255,255), (820,350), 42,0)
			pygame.draw.circle(screen, (30,30,30), (640,350), 40,0)
			pygame.draw.circle(screen, (30,30,30), (820,350), 40,0)
			screen.blit(blackhole_56,(640-28,350-28))
			screen.blit(blackhole_56,(820-28,350-28))
			dis_ballwh[1][1] = (ball_x[1]-640)*(ball_x[1]-640) + (ball_y[1]-350)*(ball_y[1]-350)
			dis_ballwh[1][2] = (ball_x[1]-820)*(ball_x[1]-820) + (ball_y[1]-350)*(ball_y[1]-350)
			if dis_ballwh[1][2] > 1600 and dis_ballwh[1][1] > 1600:
				ballwh[1] = 0
			if dis_ballwh[1][1] <= 1600 and ballwh[1] == 0:
				ball_x[1],ball_y[1] = 820,350
				ballwh[1] = 1
			if dis_ballwh[1][2] <= 1600 and ballwh[1] == 0:
				ball_x[1],ball_y[1] = 640,350
				ballwh[1] = 1
		#---------------------------Invisibility-----------------------------#
		if ((ball_x[1] >= 640 and ball_x[1] <= 725) or (ball_x[1] >= 735 and ball_x[1] <= 820)) and dm_select == 3:
			ball_vis[1] = 0
		else:
			ball_vis[1] = 1
		if ball_vis[1] == 1 and dm_select != 1 and dm_select != 8:
			if ball_accelstatus[1] == 1:
				pygame.draw.circle(screen, (204,0,204), (int(ball_x[1]),int(ball_y[1])), 10,0)
			if ball_accelstatus[1] == 0:
				pygame.draw.circle(screen, (204,255,255), (int(ball_x[1]),int(ball_y[1])), 10 ,0)	
		#-------------------------------------------------------------------#
		if dm_select == 1:
			if laser_status == 0:
				laser_resttime = 0
				laser_outtime = 0
				laser_time = timepm
				laser_status = 1
			if laser_status == 1:
				pygame.draw.line(screen, (255,0,0), (726,350), (726,351), 350)
				laser_countdown = 3 - int((timepm - laser_time)/1000)
				screen.blit(pygame.font.SysFont('Times New Roman', 40).render("Laser in %d"%(laser_countdown), True, (255, 0, 0)), (650, 210))
				if timepm - laser_time >= 3000:
					laser_outtime = timepm
					laser_status = 2
			if laser_status == 2:
				laser_time = 0
				pygame.draw.line(screen, (255,0,0), (726,330), (726,370), 350)
				if timepm - laser_outtime >= 800:
					laser_resttime = timepm
					laser_status = 3
			if laser_status == 3:
				screen.blit(pygame.font.SysFont('Times New Roman', 40).render("You lose", True, (255, 255, 255)), (660, 330))
				if timepm - laser_resttime >= 2000:
					laser_status = 0
			if laser_status != 3:
				pygame.draw.line(screen, (0,0,255), (570,310), (570,390), bar_width)
		pygame.display.update()
	if gamestate == "setting_duel":
		screen.blit(background,(0,0))
		setduel_fontsize = [0,40,40,40,40,30]
		setduel_fontsize[setduel_select] = setduel_fontsize[setduel_select]+10
		setduel_circley = 85+60*setduel_select
		if setduel_select == 4 and com_diffculty >= 2:
			drawlefttri(340,330,20,15)
		if setduel_select == 5:
			setduel_circley = 575
		screen.blit(pygame.font.SysFont('Times New Roman', 80).render("Duel", True, (171,171,171)), (30, 15))
		screen.blit(pygame.font.SysFont('Times New Roman', setduel_fontsize[1]).render("Ball", True, (255, 255, 255)), (80, 120))
		screen.blit(pygame.font.SysFont('Times New Roman', setduel_fontsize[2]).render("Bar", True, (255, 255, 255)), (80, 180))
		screen.blit(pygame.font.SysFont('Times New Roman', setduel_fontsize[3]).render("Others", True, (255, 255, 255)), (80, 240))
		screen.blit(pygame.font.SysFont('Times New Roman', setduel_fontsize[5]).render("Start", True, (255, 255, 255)), (80, 550))
		pygame.draw.circle(screen, (102,204,255), (60,setduel_circley),6,0)
		#----------------------------------------Difficulty--------------------------------------------#
		if gm_select == 1:
			screen.blit(pygame.font.SysFont('Times New Roman', setduel_fontsize[4]).render("Difficulty", True, (255, 255, 255)), (80, 300))
			if com_diffculty == 1:
				screen.blit(pygame.font.SysFont('Times New Roman', setduel_fontsize[4]-5).render("Advantage", True, (255, 255, 255)), (350, 305))
				if setduel_select == 4:
					drawrighttri(560,330,20,15)
				bar_speed[2] = 0.5*bar_basicspeed[2]
			elif com_diffculty == 2:
				screen.blit(pygame.font.SysFont('Times New Roman', setduel_fontsize[4]-5).render("Fair_Game", True, (255, 255, 255)), (350, 305))
				if setduel_select == 4:
					drawrighttri(565,330,20,15)
				bar_speed[2] = bar_basicspeed[2]
			elif com_diffculty == 3:
				screen.blit(pygame.font.SysFont('Times New Roman', setduel_fontsize[4]-5).render("Disadvantage", True, (255, 255, 255)), (350, 305))
				if setduel_select == 4:
					drawrighttri(620,330,20,15)
				bar_speed[2] = 2*bar_basicspeed[2]
			elif com_diffculty == 4:
				screen.blit(pygame.font.SysFont('Times New Roman', setduel_fontsize[4]-5).render("Mission_Impossible", True, (255, 255, 255)), (350, 305))
				bar_speed[2]=  10000
		for events in pygame.event.get():
			if events.type == pygame.KEYDOWN:	
				if events.key == pygame.K_ESCAPE:
					quit_game()
				elif events.key == pygame.K_SPACE:
					if setduel_select == 5:
						scorer,winner = "",""
						score1,score2 = 0,0
						timeout = 0
						load_seconds=0
						gamescore[3],gamescore[5] = 0,0
						load_percentage = 0
						loadtimer = pygame.time.Clock()
						gamestate = "loading"
					elif setduel_select == 1:
						blspeedtimer=pygame.time.Clock()
						gamestate = "setting_ball"
					elif setduel_select == 2:
						brspeedtimer=pygame.time.Clock()
						ranbarexhibit = 5*random.random ()
						gamestate = "setting_bar"
					elif setduel_select == 3:
						gamestate = "setting_others"
				if (events.key == pygame.K_d or events.key == pygame.K_RIGHT) and setduel_select == 4 and com_diffculty <= 3:	
					com_diffculty += 1
				if (events.key == pygame.K_a or events.key == pygame.K_LEFT) and setduel_select == 4 and com_diffculty >= 2:	
					com_diffculty -= 1
				if events.key == pygame.K_BACKSPACE:
					ball_x[1],ball_y[1] = 730,350
					ball_speedx[1],ball_speedy[1] = 400,400
					clockpm = pygame.time.Clock()
					gamestate = "duelmode"
				elif events.key == pygame.K_TAB or events.key == pygame.K_s or events.key == pygame.K_DOWN:
					setduel_select += 1
					if setduel_select == 6:
						setduel_select = 1
					if gm_select == 2 and setduel_select == 4:
						setduel_select = 5
				elif events.key == pygame.K_w or events.key == pygame.K_UP :
					setduel_select -= 1
					if setduel_select == 0:
						setduel_select = 5
					if gm_select == 2 and setduel_select == 4:
						setduel_select = 3
		pygame.display.update()
	if gamestate == "loading" :
		screen.blit(background,(0,0))
		load_barlength = int(760*load_percentage/100)
		loadmilli = loadtimer.tick()
		load_seconds += loadmilli
		if load_seconds%1000 <= 10 and load_add == 0 and load_seconds >= 1000:
			load_percentage += (random.random()*15 + 10)
			load_add = 1
		if load_seconds%1000 >= 900 and load_add == 1:
			load_add = 0
		if load_percentage >= 150:
			screen.blit(pygame.font.SysFont('Times New Roman', 100).render("Loading Complete", True, (255, 255, 255)), (120, 220))
			screen.blit(pygame.font.SysFont('Times New Roman', 40).render("Please press space to continue", True, (255, 255, 255)), (250, 380))
		if load_percentage <= 150:	
			if load_seconds%1500 <= 500:
				screen.blit(pygame.font.SysFont('Times New Roman', 100).render("Loading.", True, (255, 255, 255)), (285, 220))
			if load_seconds%1500 <= 1000 and load_seconds%1500 > 500:
				screen.blit(pygame.font.SysFont('Times New Roman', 100).render("Loading..", True, (255, 255, 255)), (285, 220))
			if load_seconds%1500 <= 1500 and load_seconds%1500 > 1000:
				screen.blit(pygame.font.SysFont('Times New Roman', 100).render("Loading...", True, (255, 255, 255)), (285, 220))
			pygame.draw.line(screen, (255,255,255), (480,450), (480,454), 760)
			pygame.draw.line(screen, (255,255,255), (480,530), (480,534), 760)
			pygame.draw.line(screen, (255,255,255), (100,450), (100,534), 4)
			pygame.draw.line(screen, (255,255,255), (860,450), (860,534), 4)
			if load_percentage <= 100 and load_percentage > 0:
				pygame.draw.line(screen, (0,255,0), (100 + 0.5*load_barlength,454), (100 + 0.5*load_barlength,530), load_barlength)
			if load_percentage >= 100:
				pygame.draw.line(screen, (0,255,0), (480,454), (480,530), 760)
			pygame.draw.line(screen, (255,255,255), (480,450), (480,534), 4)
			if load_percentage >= 100:
				screen.blit(pygame.font.SysFont('Times New Roman', 45).render("100", True, (0,0,0)), (480-32, 465))			
			if load_percentage <= 100 and load_percentage > 0:	
				screen.blit(pygame.font.SysFont('Times New Roman', 45).render("%d"%(load_percentage), True, (0,0,0)), (100 + 0.5*load_barlength -20, 465))
		pygame.display.update()
		for events in pygame.event.get():
			if events.type == pygame.KEYDOWN:	
				if events.key == pygame.K_ESCAPE:
					quit_game()
				elif (events.key == pygame.K_SPACE and load_percentage >= 150 ) or events.key == pygame.K_l:
					gameseconds = 0
					gametimer = 0
					laser_status = 0
					gamescore[3] = 0
					gamestate = 'preparation'
	if gamestate == 'preparation':
		screen.blit(background,(0,0))
		while gamescore[gm_select] > record_top5[gm_select][5] and newhigh == 0 and gm_select >= 3 and gm_select <= 6:
			if gamescore[gm_select] > record_top5[gm_select][1]:
				record_top5[gm_select].insert(1,gamescore[gm_select])
				breakrecord = 1
				newhigh = 1
				break
			if gamescore[gm_select] <= record_top5[gm_select][1] and gamescore[gm_select] > record_top5[gm_select][2]:
				record_top5[gm_select].insert(2,gamescore[gm_select])
				newhigh = 2
				break
			if gamescore[gm_select] <= record_top5[gm_select][2] and gamescore[gm_select] > record_top5[gm_select][3]:
				record_top5[gm_select].insert(3,gamescore[gm_select])
				newhigh = 3
				break
			if gamescore[gm_select] <= record_top5[gm_select][3] and gamescore[gm_select] > record_top5[gm_select][4]:
				record_top5[gm_select].insert(4,gamescore[gm_select])
				newhigh = 4
				break
			if gamescore[gm_select] <= record_top5[gm_select][4] and gamescore[gm_select] > record_top5[gm_select][5]:
				record_top5[gm_select].insert(5,gamescore[gm_select])
				newhigh = 5
		if newhigh != 0:
			record_top5[gm_select][:-1]
			if gm_select == 3:
				f = open( 'sur_1p_highscore.txt' , 'r+')
				f.write("%d\n%d\n%d\n%d\n%d\n"%(record_top5[3][1],record_top5[3][2],record_top5[3][3],record_top5[3][4],record_top5[3][5]))
				f.close()	
			if gm_select == 4:
				f = open( 'sur_2p_highscore.txt' , 'r+')
				f.write("%d\n%d\n%d\n%d\n%d\n"%(record_top5[4][1],record_top5[4][2],record_top5[4][3],record_top5[4][4],record_top5[4][5]))
				f.close()
			if gm_select == 5:
				f = open( 'catch_1p_highscore.txt' , 'r+')
				f.write("%d\n%d\n%d\n%d\n%d\n"%(record_top5[5][1],record_top5[5][2],record_top5[5][3],record_top5[5][4],record_top5[5][5]))
				f.close()	
			if gm_select == 6:
				f = open( 'catch_2p_highscore.txt' , 'r+')
				f.write("%d\n%d\n%d\n%d\n%d\n"%(record_top5[6][1],record_top5[6][2],record_top5[6][3],record_top5[6][4],record_top5[6][5]))
				f.close()	
			screen.blit(pygame.font.SysFont('Times New Roman', 50).render("Congratulation !!", True, (255, 255, 255)), (320, 130))
			if breakrecord == 0:
				screen.blit(pygame.font.SysFont('Times New Roman', 50).render("New high score !", True, (255, 255, 255)), (310, 200))
			if breakrecord == 1:	
				screen.blit(pygame.font.SysFont('Times New Roman', 50).render("You break the record!", True, (255, 255, 255)), (300, 200))
		if gm_select == 3 or gm_select == 4:
			ball_speedx[1],ball_speedy[1] = 400,400
			bar_half_length[1] = 40
			bar_speed[1] = bar_basicspeed[1]
			bar_speed[2] = bar_basicspeed[2]
		if timeout == 1 and timelimit%2 == 1:
			if gm_select == 2:
				screen.blit(pygame.font.SysFont('Times New Roman', 40).render("Timeout.", True, (255, 255, 255)), (400, 200))
			if gm_select == 1:
				screen.blit(pygame.font.SysFont('Times New Roman', 40).render("Timeout.", True, (255, 255, 255)), (400, 200))
		if score1 == winscore:
		    winner = "P1"
		elif score2 == winscore: 
		    winner = "P2"
		laser_status = 0
		screen.blit(pygame.font.SysFont('Times New Roman', 30).render("Please press space to continue", True, (255, 255, 255)), (300, 400))
		if score1 == 0 and score2 == 0 and timeout == 0 and gamescore[3] == 0 and gamescore[4] == 0 and gamescore[5] == 0 and gamescore[6] == 0:
			screen.blit(pygame.font.SysFont('Times New Roman', 50).render("New Game", True, (255, 255, 255)), (370, 150))
		if winner != "": 
			if gm_select == 2:
				screen.blit(pygame.font.SysFont('Times New Roman', 30).render("The winner is %gm_fontsize"%(winner), True, (255, 255, 255)), (300, 250)) #(x,y)#
				scorer=""
			if gm_select == 1:
				if winner == "P1":
					screen.blit(pygame.font.SysFont('Times New Roman', 30).render("You win !!", True, (255, 255, 255)), (400, 250))
					scorer=""
				if winner == "P2":
					screen.blit(pygame.font.SysFont('Times New Roman', 30).render("You Lose !!", True, (255, 255, 255)), (400, 250))
					scorer=""
		if gm_select == 1:
			screen.blit(pygame.font.SysFont('Times New Roman', 40).render("P1 : %d   VS   Com : %d"%(score1,score2), True, (255, 255, 255)), (320, 300))
		if gm_select == 2:
			screen.blit(pygame.font.SysFont('Times New Roman', 40).render("P1 : %d   VS   P2 : %d"%(score1,score2), True, (255, 255, 255)), (320, 300))
		if scorer != "":
			if gm_select == 1:
				if scorer == "P1":
					screen.blit(pygame.font.SysFont('Times New Roman', 30).render("You score !!", True, (255, 255, 255)), (400, 250))
				if scorer == "P2":
					screen.blit(pygame.font.SysFont('Times New Roman', 30).render("Com scores !!", True, (255, 255, 255)), (400, 250))
			if gm_select == 2:
				if timeout == 1:
					screen.blit(pygame.font.SysFont('Times New Roman', 30).render("It'gm_fontsize even.", True, (255, 255, 255)), (410, 250))
				if timeout == 0:
					screen.blit(pygame.font.SysFont('Times New Roman', 30).render("%gm_fontsize scores !!"%(scorer), True, (255, 255, 255)), (400, 250))
		if (gm_select == 3 or gm_select == 4) and gamescore[3] != 0 :
			screen.blit(pygame.font.SysFont('Times New Roman', 40).render("You have survived for %d seconds."%(gametimer), True, (255, 255, 255)), (230, 300))
		if (gm_select == 5 or gm_select == 6) and gamescore[5] != 0 :
			screen.blit(pygame.font.SysFont('Times New Roman', 40).render("Your score : %d"%(gamescore[5]), True, (255, 255, 255)), (370, 300))
		for events in pygame.event.get():
			if events.type == pygame.KEYDOWN:	
				if events.key == pygame.K_ESCAPE:
					quit_game()
				elif events.key == pygame.K_SPACE:
					if dm_style[2] == 1:
						accelboxy=screen_height*39/64*random.random()+100
					if dm_style[7] == 1:
						wh_y[1]=screen_height*44/64*random.random()+100
						wh_y[2]=screen_height*44/64*random.random()+100
					if gm_select == 3 or gm_select == 4 or gm_select == 5 or gm_select == 6:
						timelimit = 0
						ball_sizelv = 3
						ball_r = [0,16,16,16]
						ball_num = 1
						ball_speedlv = 4
						ball_setspeedx = [0,300,299,298]
						ball_setspeedy = [0,300,299,298]
						calculate_ball_speed()
						bar_lengthlv = 3
						bar_half_length[1] = 60
						bar_speedlv = 2
						bar_speed[1] = 1.8*bar_basicspeed[1]
						bar_speed[2] = 1.8*bar_basicspeed[2]
						bar_freemove = 0
						dmmodeon = 0
						dmmodeonmax = 0
						dm_style = [0,0,0,0,0,0,0,0]
						if gm_select == 5 or gm_select == 6:
							ball_speedx[1],ball_speedy[1] = 350,350
							ball_speedx[2],ball_speedy[2] = 349,349
							ball_speedx[3],ball_speedy[3] = 348,348
					for i in [1,2,3]:
						ball_x[i],ball_y[i]=screen_width/2,screen_height/2
						ball_speedx[i],ball_speedy[i] = ball_setspeedx[i],ball_setspeedy[i]
						calculate_ball_speed()
						calculate_ball_dirangle()
					bar_x[1],bar_x[2] = bar_screen_space,screen_width-bar_screen_space
					bar_y[2],bar_y[1] = screen_height/2,screen_height/2
					if gm_select == 4 or gm_select == 6:
						bar_x[2] = bar_screen_space + bar_screen_space + bar_width
					if gm_select != 1 and gm_select != 2:
						for i in [1,2,3]:
							ball_x[i],ball_y[i] = 900,320
					if gm_select == 1 or gm_select == 2:	
						for i in [1,2]:
							dir_ran = 4*random.random()
							if dir_ran < 4 and dir_ran >= 3 :
								ball_dirangle[i] = 30*random.random()+30
							if dir_ran < 3 and dir_ran >= 2:
								ball_dirangle[i] = 30*random.random()+30+90
							if dir_ran < 2 and dir_ran >= 1:
								ball_dirangle[i] = 30*random.random()+30+180
							if dir_ran < 1:
								ball_dirangle[i] = 30*random.random()+30+270
					ball_alive = [0,1,0,0]
					ball_start = [0,1,0,0]
					ball_accelstatus = [0,0,0,0]
					scorer = ""
					timeout=0
					gameseconds=0
					gametimer=0
					laser_status=0
					gamescore[3] = 0
					gra_status = 0
					countdownseconds = 0
					countdowntimer = pygame.time.Clock()
					ball_score = [0,1,1,1]
					ball_deadtime = [0,0,0,0]
					ball_cd = [0,0,0,0]
					scorechange = 0
					gamescore[5] = 0
					clock = pygame.time.Clock()
					timer = pygame.time.Clock()
					cd_status = 1
					pause_status = 0
					if newhigh != 0:
						temptgamestate = gamestate
						gamestate = "highscore"
					else:
						if winner != "":
							setduel_select = 5
							gamestate = "setting_duel"
						else:
							gamestate = 1
					breakrecord = 0
				elif events.key == pygame.K_BACKSPACE:
					if gm_select == 3 or gm_select == 4:
						gamestate = "setting_surcat"
					elif gm_select == 5 or gm_select == 6:
						gamestate = "setting_surcat"
					else:
						gamestate = "setting_duel"
		pygame.display.update()
	if gamestate == 1: 
		screen.blit(background,(0,0))
		screen.blit(top_margin,(0,0))
		for events in pygame.event.get():
			if events.type == pygame.QUIT:
				quit_game()
			if events.type == pygame.KEYDOWN:
				if events.key == pygame.K_p and cd_status == 0:
					pause_status = 1 - pause_status
				if control == 1:
					if events.key == pygame.K_w:
						bar_diry[1]= -1
					elif events.key == pygame.K_s:
						bar_diry[1]= 1
					if gm_select == 2 or gm_select == 4:
						if events.key == pygame.K_UP:
							bar_diry[2] = -1
						elif events.key == pygame.K_DOWN:
							bar_diry[2] = 1
					if bar_freemove == 1:
						if events.key == pygame.K_d:
							bar_dirx[1]= 1
						elif events.key == pygame.K_a:
							bar_dirx[1] = -1
						if gm_select == 2:
							if events.key == pygame.K_RIGHT:
								bar_dirx[2] = 1
							elif events.key == pygame.K_LEFT:
								bar_dirx[2] = -1
				if control == 2:
					if events.key == pygame.K_UP:
						bar_diry[1] = -1
					elif events.key == pygame.K_DOWN:
						bar_diry[1] = 1
					if gm_select == 2 or gm_select == 4:
						if events.key == pygame.K_w:
							bar_diry[2] = -1
						elif events.key == pygame.K_s:
							bar_diry[2] = 1
					if bar_freemove == 1:
						if events.key == pygame.K_RIGHT:
							bar_dirx[1] = 1
						elif events.key == pygame.K_LEFT:
							bar_dirx[1] = -1
						if gm_select == 2:
							if events.key == pygame.K_d:
								bar_dirx[2] = 1
							elif events.key == pygame.K_a:
								bar_dirx[2] = -1
				if events.key == pygame.K_ESCAPE:
					quit_game()
				if events.key == pygame.K_BACKSPACE:
					if gm_select == 3 or gm_select == 4 or gm_select == 5 or gm_select == 6:
						gameseconds = 0
						gametimer = 0
						laser_status = 0
						gamescore[3],gamescore[4],gamescore[5],gamescore[6] = 0,0,0,0
						gamestate = "setting_surcat"
					if gm_select == 1 or gm_select == 2:
						gamestate = "setting_duel"
			if events.type == pygame.KEYUP:
				if control == 1:
					if events.key == pygame.K_w or events.key == pygame.K_s:
						bar_diry[1] = 0
					if gm_select == 2 or gm_select == 4:
						if events.key == pygame.K_UP or events.key == pygame.K_DOWN:
							bar_diry[2] = 0
					if bar_freemove == 1:
						if events.key == pygame.K_d or events.key == pygame.K_a:
							bar_dirx[1] = 0
						if gm_select == 2 or gm_select == 4:
							if events.key == pygame.K_RIGHT or events.key == pygame.K_LEFT:
								bar_dirx[2] = 0
				if control == 2:
					if events.key == pygame.K_UP or events.key == pygame.K_DOWN:
						bar_diry[1] = 0
					if gm_select == 2 or gm_select == 4:
						if events.key == pygame.K_w or events.key == pygame.K_s:
							bar_diry[2] = 0						
					if bar_freemove == 1:		
						if events.key == pygame.K_RIGHT or events.key == pygame.K_LEFT:
							bar_dirx[1] = 0
						if gm_select == 2 or gm_select == 4:
							if events.key == pygame.K_d or events.key == pygame.K_a:
								bar_dirx[2] = 0
		#=============================計算時間 BEGIN=============================#
		countdownmilli = countdowntimer.tick()
		countdownseconds += countdownmilli
		countdown321 = 3 - int(countdownseconds/1000)
		if countdown321 == 0:
			cd_status = 0
		milli = clock.tick()
		seconds = milli/1000.0
		gamemilli = timer.tick()
		if cd_status == 1 or pause_status == 1:
			gamemilli = 0
			seconds = 0
		gameseconds += gamemilli
		gametimer = int(gameseconds/1000)
		remaintime = maxtime - gametimer
		if remaintime == 0 and (gm_select == 1 or gm_select == 2 or gm_select == 5 or gm_select == 6): 
			if timelimit == 1 and (gm_select == 1 or gm_select == 2):
				timeout = 1
				if gm_select == 1:
					score1 += 1
					scorer = "P1"
			gamestate = 'preparation'
		#=============================計算時間 END=============================#
		#--------------------------Survival-----------------------------#
		if gm_select == 3 or gm_select == 4 or gm_select == 5 or gm_select == 6:
			if gm_select == 3 or gm_select == 4:
				gamescore[gm_select] = gametimer
				ball_speedx[1] += seconds*(gm_select-2)
				ball_speedy[1] += seconds*(gm_select-2)
			if gm_select == 5 or gm_select == 6:
				for i in [1,2,3]:
					ball_speedx[i] += seconds*2
					ball_speedy[i] += seconds*2
				for i in [2,3]:
					if gameseconds < 15000*(i-1):
						ball_start[i] = 0
						ball_alive[i] = 0
						ball_speed[i] = 0
					elif gameseconds >= 15000*(i-1) and gameseconds < 15000*(i-1)+100:
						ball_start[i] = 1
						ball_alive[i] = 1
						ball_speed[i] = 500
						rrx1 = 2*random.random()
						if rrx1 < 1:
							ball_dirangle[i] = 30*random.random()+30
						if rrx1 < 2 and rrx1 >= 1:
							ball_dirangle[i] = 30*random.random()+300
						ball_speedx[i] = ball_speed[i]*cos(ball_dirangle[i])
						ball_speedy[i] = ball_speed[i]*sin(ball_dirangle[i])
			if dmmodeonmax <= 7:
				dmmodeonmax = int((gameseconds - 15000)/30000) + 1
			if gameseconds%15000 >= 14980 :
				dmmodeon = 0
				dm_style = [0,0,0,0,0,0,0,0]
			if dmmodeon < dmmodeonmax and gameseconds >= 15000:
				if gameseconds <= 60000:
					spmode_ran = int(7*random.random()) + 1
				elif gameseconds > 60000:
					spmode_ran = int(8*random.random()) + 1
				if spmode_ran <= 7:
					dm_style [spmode_ran] = 1
				if spmode_ran == 2:
					accelboxy = screen_height*39/64*random.random()+100
				if spmode_ran == 7:
					wh_y[1]=screen_height*44/64*random.random()+100
					wh_y[2]=screen_height*44/64*random.random()+100
				dmmodeon += 1
		#=============================球和棒子位置 BEGIN=============================#
		for i in [1,2,3]:
			calculate_ball_speedxy()
			ball_x[i] += seconds*ball_speedx[i]
			ball_y[i] += seconds*ball_speedy[i]
			if gm_select >= 1 and gm_select <= 4:
				if ball_num <= 1:
					ball_x[2] = 300
					ball_y[2] = 300
				if ball_num <= 2:
					ball_x[3] = 300
					ball_y[3] = 300
		#-----------------------------左邊的邊緣BEGIN---------------------------#
		for i in [1,2,3]:
			if ball_x[i] < ball_r[i]:
				if sound == 1:
					sound2.play()
				if gm_select == 1 or gm_select == 2:
					score2 += 1
					scorer = "P2"
				if gm_select == 1 or gm_select == 2 or gm_select == 3 or gm_select == 4:
					gamestate = 'preparation'
				if gm_select == 5 or gm_select == 6:
					if ball_alive[i] == 1:
						ball_accelstatus[i] = 0
						ball_deadtime[i] = gameseconds
						gamescore[gm_select] -= (ball_score[i] - int((ball_score[i]+1)/2))
						scorechange = -(ball_score[i] - int((ball_score[i]+1)/2))
						ball_score[i] = int((ball_score[i]+1)/2)
						ball_x[i],ball_y[i] = 900,320
						ball_speedx[i] = ball_speed[i]*cos(ball_dirangle[i])
						ball_speedy[i] = ball_speed[i]*sin(ball_dirangle[i])
						ball_alive[i] = 0
			if ball_alive[i] == 0 and ball_start[i] != 0 and (gm_select == 5 or gm_select == 6): 
				ball_speed[i] == 0
				ball_x[i],ball_y[i] = 900,320
				ball_cd[i] = ball_score[i] - int((gameseconds - ball_deadtime[i])/1000)
				if ball_cd[i] == 0:
					ball_speed[i] = 500
					rrx1 = 2*random.random()
					if rrx1 < 1:
						ball_dirangle[i] = 30*random.random()+30
					if rrx1 < 2 and rrx1 >= 1:
						ball_dirangle[i] = 30*random.random()+300
					ball_speedx[i] = ball_speed[i]*cos(ball_dirangle[i])
					ball_speedy[i] = ball_speed[i]*sin(ball_dirangle[i])
					ball_alive[i] = 1
		#-----------------------------右邊的邊緣BEGIN---------------------------#
		if (ball_x[1] > screen_width-ball_r[1] or ball_x[2] > screen_width-ball_r[2]) and (gm_select == 1 or gm_select == 2):
			ball_dirangle = [0,0,0,0]
			if sound == 1:
				sound2.play()
			if gm_select == 1 or gm_select == 2:
				score1 += 1
				scorer = "P1"
			gamestate = 'preparation'
		if dm_style[4] == 0:
			screen.blit(bounce_50_dark,(410,5))
		if dm_style[4] == 1:
			screen.blit(bounce_50,(410,5))
		for i in [1,2,3]:
			if ball_x[i] > screen_width-ball_r[i]-5 and ball_speedx[i] > 0 and (gm_select == 3 or gm_select == 4 or gm_select == 5 or gm_select == 6):
				if dm_style[4] == 0:
					ball_dirangle[i] = 180 - ball_dirangle[i]
				if dm_style[4] == 1:
					rrx1 = 2*random.random()
					if rrx1 < 1:
						ball_dirangle[i] = 30*random.random() + 120
					elif rrx1 >= 1 and rrx1 < 2:
						ball_dirangle[i] = 30*random.random() + 210
				ball_speedx[i] = ball_speed[i]*cos(ball_dirangle[i])
				ball_speedy[i] = ball_speed[i]*sin(ball_dirangle[i])
		#-----------------------------上方的邊緣BEGIN---------------------------#
		for i in [1,2,3]:
			if ball_y[i] < ball_r[i] and ball_speedy[i] < 0:
				if dm_style[4] == 0:
					ball_dirangle[i] = -ball_dirangle[i]
				if dm_style[4] == 1:
					rrx1 = 2*random.random()
					if rrx1 < 1:
						ball_dirangle[i] = 30*random.random()+30
					if rrx1 < 2 and rrx1 >= 1:
						ball_dirangle[i] = 30*random.random()+120
		#-----------------------------下方的邊緣BEGIN---------------------------#
			if ball_y[i] >= screen_height-ball_r[i] and ball_speedy[i] > 0:
				if dm_style[4] == 0:
					ball_dirangle[i] = -ball_dirangle[i]
				if dm_style[4] == 1:
					rrx1 = 2*random.random()
					if rrx1 < 1:
						ball_dirangle[i] = 30*random.random()+210
					if rrx1 < 2 and rrx1 >= 1:
						ball_dirangle[i] = 30*random.random()+300
		#-----------------------------撞到棒子時BEGIN-----------------------#
			if ball_x[i] <= bar_x[1]+ball_r[i] and ball_x[i] >= bar_x[1]-bar_width and ball_y[i] >= bar_y[1]-(bar_half_length[1]+ball_r[i]) and ball_y[i] <= bar_y[1]+(bar_half_length[1]+ball_r[i]) and ball_speedx[i] < 0:
				gamescore[gm_select] += ball_score[i]
				scorechange = ball_score[i]
				ball_score[i] += 1
				if ball_accelstatus[i] == 1:	
					ball_accelstatus[i] = 2
				if gm_select == 1 or gm_select == 2:
					ball_speedy[i] += bar_diry[1]*bar_speed[1]/10
					ball_speed[i] = math.hypot(ball_speedx[i],ball_speedy[i])
					ball_dirangle[i] = math.degrees(math.atan2(ball_speedy[i],ball_speedx[i]))
				if dm_style[4] == 0:
					ball_dirangle[i] = 180 - ball_dirangle[i]
				if dm_style[4] == 1:
					rrx1 = 2*random.random()
					if rrx1 < 1:
						ball_dirangle[i] = 30*random.random()+30
					if rrx1 < 2 and rrx1 >= 1:
						ball_dirangle[i] = 30*random.random()+300
				if sound == 1:
					sound1.play()
			elif ((ball_x[i] >= bar_x[2]-ball_r[i]) and (ball_x[i] <= bar_x[2]+bar_width) and (ball_y[i]>=bar_y[2]-(bar_half_length[1]+ball_r[i])) and (ball_y[i]<=bar_y[2]+(bar_half_length[1]+ball_r[i])) and ball_speedx[i] > 0) and (gm_select == 1 or gm_select == 2):
				if ball_accelstatus[i] == 1:	
					ball_accelstatus[i] = 2
				if gm_select == 1 or gm_select == 2:
					ball_speedy[i] += bar_diry[2]*bar_speed[2]/10
					calculate_ball_speed()
					calculate_ball_dirangle()
				if dm_style[4] == 0:
					ball_dirangle[i] = 180 - ball_dirangle[i]
				if dm_style[4] == 1:
					rrx1 = 2*random.random()
					if rrx1 < 1:
						ball_dirangle[i] = 30*random.random()+120
					if rrx1 < 2 and rrx1 >= 1:
						ball_dirangle[i] = 30*random.random()+210
				if sound == 1:
					sound1.play()
		#--------------------------------Survival_2P----------------------------------------#
			elif (ball_x[i] <= bar_x[2]+ball_r[i] and ball_x[i] >= bar_x[2]-bar_width and ball_y[i] >= bar_y[2]-(bar_half_length[1]+ball_r[i]) and ball_y[i] <= bar_y[2]+(bar_half_length[1]+ball_r[i]) and ball_speedx[i] < 0) and gm_select == 4:
				if ball_accelstatus[i] == 1:	
					ball_accelstatus[i] = 2
				if dm_style[4] == 0:
					ball_dirangle[i] = 180 - ball_dirangle[i]
				if dm_style[4] == 1:
					rrx1 = 2*random.random()
					if rrx1 < 1:
						ball_dirangle[i] = 30*random.random()+30
					if rrx1 < 2 and rrx1 >= 1:
						ball_dirangle[i] = 30*random.random()+300
				if sound == 1:
					sound1.play()
			re_ball_dirangle()			
			ball_speedx[i] = ball_speed[i]*cos(ball_dirangle[i])
			ball_speedy[i] = ball_speed[i]*sin(ball_dirangle[i])
		#-----------------------------撞到棒子時END-------------------------#
		#--------BAR移動---------#
		for j in [1,2]:	
			if (bar_diry[j] < 0 and bar_y[j] > bar_half_length[1]) or (bar_diry[j] > 0 and bar_y[j] < screen_height-bar_half_length[1]):
				bar_y[j] += seconds*bar_diry[j]*bar_speed[j]
			if bar_freemove == 1:
				if (bar_dirx[j] < 0 and bar_x[j] > bar_screen_space) or (bar_dirx[j] > 0 and bar_x[j] < mid_width-bar_screen_space):
					bar_x[j] += seconds*bar_dirx[j]*200
		#-----------------------------One_Player_Computer--------------------------------#
		if gm_select == 1:
			if ball_num == 2:
				if ball_speedx[1] > 0 and ball_speedx[2] > 0: 
					if ball_x[1] >= ball_x[2]:
						bar_diry[2] = -posi_nega(bar_y[2] - ball_y[1])
					if ball_x[1] <= ball_x[2]:
						bar_diry[2] = -posi_nega(bar_y[2] - ball_y[2])
				if ball_speedx[1] > 0 and ball_speedx[2] < 0: 
					bar_diry[2] = -posi_nega(bar_y[2] - ball_y[1])
				if ball_speedx[1] < 0 and ball_speedx[2] > 0:
					bar_diry[2] = -posi_nega(bar_y[2] - ball_y[2])
				if (ball_speedx[1] < 0 and ball_speedx[2] < 0) or (ball_vis[1] == 0 and ball_vis[2] == 0):
					bar_diry[2] = -posi_nega(bar_y[2]-mid_height)
			if ball_num == 1 :
				if ball_speedx[1] > 0: 
					bar_diry[2] = -posi_nega(bar_y[2] - ball_y[1])
				if (ball_dirangle[1] < 270 and ball_dirangle[1] > 90) or (dm_style[3] == 1 and ( ball_x[1] > 0.6*mid_width and ball_x[1] < 1.4*mid_width ) and ball_accelstatus[1] == 0):
					bar_diry[2] = -posi_nega(bar_y[2]-mid_height)
		#------------------------------Gravity---------------------------#
		calculate_ball_speedxy()
		if dm_style[5] == 0:
			screen.blit(gra_50_dark,(505,5))
			screen.blit(control_down_dark,(555,5))
			if gra_status != 0 :
				for i in [1,2]:
					ball_speedx[i],ball_speedy[i] = ball_gratemptspeedx[i],ball_gratemptspeedy[i]
			gra_status = 0
		if dm_style[5] == 1:
			screen.blit(gra_50,(505,5))	
			for i in [1,2,3]:
				if gra_status == 0:
					gra_starttime = gameseconds
					ball_gratemptspeedx[i],ball_gratemptspeedy[i] = ball_speedx[i],ball_speedy[i]
					gra_status = 1
				gra_countdown = 5 - int((gameseconds - gra_starttime)/1000)%5
				if gra_status == 1:	
					gra_ran = 6*random.random()
					gra_status = 2
				if gameseconds%5000 >= 4950:
					ball_speedx[i],ball_speedy[i] = ball_gratemptspeedx[i],ball_gratemptspeedy[i]
					gra_status = 1
				if gra_ran >= 0 and gra_ran < 2:
					screen.blit(control_down,(555,5))
					ball_speedy[i] += gra_accel*seconds	
				if gra_ran >= 2 and gra_ran < 4:
					screen.blit(control_up,(555,5))
					ball_speedy[i] += -gra_accel*seconds
				if gm_select == 1 or gm_select == 2:
					if gra_ran >= 4 and gra_ran < 5:
						screen.blit(control_right,(555,5))
						ball_speedx[i] += gra_accel*seconds
					if gra_ran >= 5 and gra_ran <= 6:
						screen.blit(control_left,(550,5))
						ball_speedx[i] += -gra_accel*seconds
				if gm_select == 3 or gm_select == 4:
					if gra_ran >= 4 and gra_ran <= 6:
						screen.blit(control_left,(550,5))
						ball_speedx[i] += -gra_accel*seconds
			screen.blit(pygame.font.SysFont('Times New Roman', 40).render("%d"%(gra_countdown), True, (250, 250, 250)), (517, 8))
			calculate_ball_speed()
			calculate_ball_dirangle()
			re_ball_dirangle()
		#---------------------------Laser------------------------------------#
		if dm_style[1] == 0:
			screen.blit(laser_50_dark,(245,5))
		if dm_style[1] == 1:
			screen.blit(laser_50,(245,5))
			if gametimer >= 2:
				if laser_status == 0:
					laser_resttime = 0
					laser_outtime = 0
					laser_ran = random.random()
					if laser_ran <= 0.5:
						laser_y = 200*random.random() + 80 #50-150   320  -490-590#
					if laser_ran > 0.5:
						laser_y = 200*fabs(random.random()-0.5) + 460
					laser_time = gameseconds
					laser_status = 1
				if laser_status == 1:
					pygame.draw.line(screen, (255,0,0), (480,laser_y), (480,laser_y+1), 960)
					laser_countdown = 3-int((gameseconds - laser_time)/1000)
					screen.blit(pygame.font.SysFont('Times New Roman', 40).render("%d"%(laser_countdown), True, (250, 250, 250)), (262, 8))
					if gameseconds - laser_time >= 3000:
						laser_outtime = gameseconds
						laser_status = 2
				if laser_status == 2:
					laser_time = 0
					pygame.draw.line(screen, (255,0,0), (480,laser_y-20), (480,laser_y+20), 960)
					if (bar_y[1] + bar_half_length[1] >= laser_y - 20 and bar_y[1] - bar_half_length[1] <= laser_y - 20) or (bar_y[1] - bar_half_length[1] <= laser_y + 20 and bar_y[1] + bar_half_length[1] >= laser_y + 20):	
						if gm_select == 5 or gm_select == 6:
							gamescore[gm_select] -= 5
							scorechange = -5
							laser_resttime = gameseconds
							laser_status = 3
						else:
							gamestate = 'preparation'
							if gm_select == 1 or gm_select == 2:
								score2 += 1
								scorer = "P2"	
					if (bar_y[2] + bar_half_length[1] >= laser_y - 20 and bar_y[2] - bar_half_length[1] <= laser_y - 20) or (bar_y[2] - bar_half_length[1] <= laser_y + 20 and bar_y[2] + bar_half_length[1] >= laser_y + 20):
						if gm_select == 6:
							gamescore[gm_select] -= 5
							scorechange = -5
							laser_resttime = gameseconds
							laser_status = 3
						elif gm_select != 3 and gm_select != 5 and gm_select != 6:
							gamestate = 'preparation'
							if gm_select == 1 or gm_select == 2:
								score1 += 1
								scorer = "P1"
					if gameseconds - laser_outtime >= 1000:
						laser_resttime = gameseconds
						laser_status = 3
				if laser_status == 3 and gameseconds - laser_resttime >= 4000:
					laser_status = 0
		#---------------------------Acceleration----------------------------#
		if dm_style[2] == 0:
			for i in [1,2,3]:
				if ball_accelstatus[i] == 1:
					ball_speedx[i],ball_speedy[i] = ball_acceltemptspeedx[i],ball_acceltemptspeedx[i]
			ball_accelstatus[1],ball_accelstatus[2] = 0,0
			screen.blit(accel_50_dark,(300,5))
		if dm_style[2] == 1:
			screen.blit(accel_50,(300,5))
			pygame.draw.line(screen, (255,102,0), (mid_width,accelboxy-5), (mid_width,accelboxy+105), 160)
			pygame.draw.line(screen, (255,255,0), (mid_width,accelboxy), (mid_width,accelboxy+100), 150)
			for i in [1,2,3,4]:
				if accel_dir == 1:
					pygame.draw.line(screen, (0,255,0), (mid_width+15*(2*i-1)-75,accelboxy+10), (mid_width+15*(2*i+1)-75,accelboxy+50), 10)
					pygame.draw.line(screen, (0,255,0), (mid_width+15*(2*i-1)-75,accelboxy+90), (mid_width+15*(2*i+1)-75,accelboxy+50), 10)
				if accel_dir == -1:
					pygame.draw.line(screen, (0,255,0), (mid_width+15*(2*i+1)-75,accelboxy+10), (mid_width+15*(2*i-1)-75,accelboxy+50), 10)
					pygame.draw.line(screen, (0,255,0), (mid_width+15*(2*i+1)-75,accelboxy+90), (mid_width+15*(2*i-1)-75,accelboxy+50), 10)
			for i in [1,2,3]:
				if ball_x[i] <= mid_width+80  and ball_x[i] >= mid_width-80 and ball_y[i]>=accelboxy-5 and ball_y[i]<= accelboxy+105 and ball_accelstatus[i] == 0:
					ball_acceltemptspeedx[i] = ball_speedx[i]
					ball_acceltemptspeedy[i] = ball_speedy[i]
					ball_speed[i] = ball_speed[i]*ball_aceelratio
					calculate_ball_speedxy()
					accelboxy = screen_height*39/64*random.random() + 100
					if (ball_dirangle[i] > 270 or ball_dirangle[i] < 90):
						accel_dir = 1
					if (ball_dirangle[i] < 270 and ball_dirangle[i] > 90):
						accel_dir = -1
					ball_accelstatus[i] = 1
				if ball_accelstatus[i] == 2:
					ball_speedx[i],ball_speedy[i] = ball_acceltemptspeedx[i],ball_acceltemptspeedy[i]
					calculate_ball_speed()
					ball_accelstatus[i] = 0
		#---------------------------Vibration------------------------------#
		if dm_style[6] == 0:
			screen.blit(vibrate_50_dark,(610,5))
		if dm_style[6] == 1:
			screen.blit(vibrate_50,(610,5))
			if (gameseconds)%200 <= 5 and curve == 0:
				for i in [1,2,3]:
					curve_ran = 5*random.random()
					if curve_ran < 3:
						ball_dirangle[i] = -ball_dirangle[i]
						re_ball_dirangle()
				calculate_ball_speedxy
				curve = 1
			if (gameseconds)%200 >= 50 and (gameseconds)%200 <= 100:
				curve = 0
		#---------------------------WormHole--------------------------------#
		if dm_style[7] == 0:
			screen.blit(wh_50_dark,(665,5))
		if dm_style[7] == 1:
			screen.blit(wh_50,(665,5))
			pygame.draw.circle(screen, (255,255,255), (int(0.5*mid_width),int(wh_y[1])), 52,0)
			pygame.draw.circle(screen, (255,255,255), (int(1.5*mid_width),int(wh_y[2])), 52,0)
			pygame.draw.circle(screen, (30,30,30), (int(0.5*mid_width),int(wh_y[1])), 50,0)
			screen.blit(blackhole_70,(int(0.5*mid_width)-35,int(wh_y[1])-35))
			pygame.draw.circle(screen, (30,30,30), (int(1.5*mid_width),int(wh_y[2])), 50,0)
			screen.blit(blackhole_70,(int(1.5*mid_width)-35,int(wh_y[2])-35))
			for i in [1,2,3]:
				for j in [1,2]:
					dis_ballwh[i][j] = (ball_x[i]-int((j-0.5)*mid_width))*(ball_x[i]-int((j-0.5)*mid_width)) + (ball_y[i]-int(wh_y[j]))*(ball_y[i]-int(wh_y[j]))
			for i in [1,2,3]:
				if dis_ballwh[i][2] > 2500 and dis_ballwh[i][1] > 2500:
					ballwh[i] = 0
				for j in [1,2]:
					if dis_ballwh[i][j] <= 2500 and ballwh[i] == 0:
						wh_y[3-j] = screen_height*44/64*random.random() + 120
						ball_x[i],ball_y[i] = int((2.5-j)*mid_width),int(wh_y[3-j])
						ballwh[i] = 1
		#---------------------------Invisibility1---------------------------#
		if dm_style[3] == 0:
			screen.blit(invis_50_dark,(355,5))
			for i in [1,2,3]:
				ball_vis[i] = 1
		if dm_style[3] == 1:
			screen.blit(invis_50,(355,5))
			pygame.draw.line(screen, (200,200,200), (0.6*mid_width,60), (0.6*mid_width,640), 1)
			pygame.draw.line(screen, (200,200,200), (1.4*mid_width,60), (1.4*mid_width,640), 1)
			for i in [1,2,3]:
				if (ball_x[i] >= 0.6*mid_width and ball_x[i] <= 0.99*mid_width) or (ball_x[i] >= 1.01*mid_width and ball_x[i] <= 1.4*mid_width) or ball_accelstatus[i] == 1:
					ball_vis[i] = 0
				else:
					ball_vis[i] = 1
		#-------------------------------------------------------------------#
		pygame.draw.line(screen, (171,171,171), (480,60), (480,61), 960)
		if gm_select == 1 or gm_select == 2:
			if timelimit == 1:
				screen.blit(pygame.font.SysFont('Times New Roman', 20).render("%d"%(remaintime), True, (255, 255, 255)), (467, 10))
			screen.blit(pygame.font.SysFont('Times New Roman', 30).render("P1", True, (51, 153, 255)), (15, 10))
			if gm_select == 1:
				screen.blit(pygame.font.SysFont('Times New Roman', 30).render("Com", True, (102, 255, 51)), (880,10))
				pygame.draw.line(screen, (0,255,0), (bar_x[2],bar_y[2]-bar_half_length[1]), (bar_x[2],bar_y[2]+bar_half_length[1]), bar_width)
			if gm_select == 2:
				screen.blit(pygame.font.SysFont('Times New Roman', 30).render("P2", True, (255, 102, 153)), (905,10))
				pygame.draw.line(screen, (255,0,0), (bar_x[2],bar_y[2]-bar_half_length[1]), (bar_x[2],bar_y[2]+bar_half_length[1]), bar_width)	
		pygame.draw.line(screen, (0,0,255), (bar_x[1],bar_y[1]-bar_half_length[1]), (bar_x[1],bar_y[1]+bar_half_length[1]), bar_width)
		if gm_select == 4 or gm_select == 6: 
			pygame.draw.line(screen, (255,0,0), (bar_x[2],bar_y[2]-bar_half_length[1]), (bar_x[2],bar_y[2]+bar_half_length[1]), bar_width)
		#----------------------Catchball----------------------------------#
		if gm_select == 5 or gm_select == 6:
			screen.blit(pygame.font.SysFont('Times New Roman', 20).render("%d"%(remaintime), True, (255, 255, 255)), (467, 10))
			if ball_alive[1] == 1:
				pygame.draw.circle(screen, (204,255,255), (50,30),20,0)
				if ball_score[1] < 10:
					screen.blit(pygame.font.SysFont('Times New Roman', 30).render("%d"%(ball_score[1]), True, (0, 0, 102)), (43, 13))
				if ball_score[1] >= 10:
					screen.blit(pygame.font.SysFont('Times New Roman', 30).render("%d"%(ball_score[1]), True, (0, 0, 102)), (35, 13))
			if ball_alive[1] == 0:
				screen.blit(pygame.font.SysFont('Times New Roman', 40).render("%d"%(ball_cd[1]), True, (204, 255, 255)), (38, 8))
			if ball_alive[2] == 1:
				pygame.draw.circle(screen, (255,153,153), (110,30), 20,0)	
				if ball_score[2] < 10:
					screen.blit(pygame.font.SysFont('Times New Roman', 30).render("%d"%(ball_score[2]), True, (102, 0, 0)), (103, 13))
				if ball_score[2] >= 10:
					screen.blit(pygame.font.SysFont('Times New Roman', 30).render("%d"%(ball_score[2]), True, (102, 0, 0)), (95, 13))
			if ball_alive[2] == 0 and gameseconds > 16000:
				screen.blit(pygame.font.SysFont('Times New Roman', 40).render("%d"%(ball_cd[2]), True, (255,153,153)), (98, 8))
			if ball_alive[3] == 1:
				pygame.draw.circle(screen, (102,255,102), (170,30), 20,0)	
				if ball_score[3] < 10:
					screen.blit(pygame.font.SysFont('Times New Roman', 30).render("%d"%(ball_score[3]), True, (0, 102, 0)), (163, 13))
				if ball_score[3] >= 10:
					screen.blit(pygame.font.SysFont('Times New Roman', 30).render("%d"%(ball_score[3]), True, (0, 102, 0)), (155, 13))
			if ball_alive[3] == 0 and gameseconds > 31000:
				screen.blit(pygame.font.SysFont('Times New Roman', 40).render("%d"%(ball_cd[3]), True, (102,255,102)), (158, 8))
			if scorechange > 0:
				screen.blit(pygame.font.SysFont('Times New Roman', 30).render("+%d"%(scorechange), True, (0, 255, 0)), (910,13))
			if scorechange < 0:
				screen.blit(pygame.font.SysFont('Times New Roman', 30).render("%d"%(scorechange), True, (255, 0, 0)), (910,13))
		#---------------------------Invisibility2----------------------------#
		if ball_vis[1] == 1 and ((gm_select >= 1 and gm_select <= 4) or ((gm_select ==5 or gm_select == 6) and ball_alive[1] == 1)):
			if ball_accelstatus[1] == 1:
				pygame.draw.circle(screen, (204,0,204), (int(ball_x[1]),int(ball_y[1])), ball_r[1],0)
			if ball_accelstatus[1] == 0:
				pygame.draw.circle(screen, (204,255,255), (int(ball_x[1]),int(ball_y[1])), ball_r[1],0)
		if ball_vis[2] == 1 and ((gm_select >= 1 and gm_select <= 4 and ball_num >= 2) or ((gm_select ==5 or gm_select == 6) and ball_alive[2] == 1)):
			if ball_accelstatus[2] == 1:
				pygame.draw.circle(screen, (255,153,0), (int(ball_x[2]),int(ball_y[2])), ball_r[2],0)			
			if ball_accelstatus[2] == 0:
				pygame.draw.circle(screen, (255,153,153), (int(ball_x[2]),int(ball_y[2])), ball_r[2],0)		
		if ball_vis[3] == 1 and ((gm_select >= 1 and gm_select <= 4 and ball_num >= 3) or ((gm_select ==5 or gm_select == 6) and ball_alive[3] == 1)):
			if ball_accelstatus[3] == 1:
				pygame.draw.circle(screen, (153,51,0), (int(ball_x[3]),int(ball_y[3])), ball_r[3],0)			
			if ball_accelstatus[3] == 0:
				pygame.draw.circle(screen, (102,255,102), (int(ball_x[3]),int(ball_y[3])), ball_r[3],0)			
		#-------------------------------------------------------------------#
		if gm_select == 3 or gm_select == 4 or gm_select == 5 or gm_select == 6:
			screen.blit(pygame.font.SysFont('Times New Roman', 35).render("Score : %d"%(gamescore[gm_select]), True, (255, 255, 255)), (750,10))
		if cd_status == 1:
			screen.blit(pygame.font.SysFont('Times New Roman', 200).render("%d"%(countdown321), True, (255, 0, 0)), (435, 230))
			screen.blit(pygame.font.SysFont('Times New Roman', 30).render("You can press P to pause in the game.", True, (255, 255,255)), (250, 450))
		if pause_status == 1:
			screen.blit(pygame.font.SysFont('Times New Roman', 200).render("PAUSE", True, (255, 0, 0)), (180, 230))
			screen.blit(pygame.font.SysFont('Times New Roman', 30).render("Press P to resume", True, (255, 255,255)), (350, 450))
		pygame.display.update()
	if gamestate == "setting_ball":
		screen.blit(background,(0,0))
		setball_fontsize = [0,40,40,40,30,30]
		setball_fontsize[setball_select] = setball_fontsize[setball_select]+10
		setball_circley = 85+60*setball_select
		if setball_select == 1:
			screen.blit(exhibit_bls,(550,300))
			pygame.draw.circle(screen, (204,255,255), (730,450),ball_r[1],0)
			if ball_sizelv >= 2:
				drawlefttri(340,150,20,15)
			if ball_sizelv <= 4:
				drawrighttri(540,150,20,15)
		elif setball_select == 2:
			screen.blit(exhibit_bls,(550,300))
			if ball_num == 1:
				pygame.draw.circle(screen, (204,255,255), (730,450),16,0)
				drawrighttri(440,210,20,15)
			elif ball_num == 2:
				pygame.draw.circle(screen, (204,255,255), (680,450),16,0)
				pygame.draw.circle(screen, (255,153,153), (780,450),16,0)
				drawlefttri(340,210,20,15)
		elif setball_select == 3:
			screen.blit(exhibit_bls,(550,300))
			blspeedtime += blspeedtimer.tick()
			blspeedexhibitx = ball_setspeedx[1]*blspeedtime/1000
			pygame.draw.circle(screen, (204,255,255), (int(blspeedexhibitx)%324 + 566,450),16,0)
			if ball_speedlv > 1:
				drawlefttri(340,270,20,15)
			if ball_speedlv != 1 and ball_speedlv != 7:
				drawrighttri(510,270,20,15)
		elif setball_select == 4:
			setball_circley = 525	
		elif setball_select == 5:
			setball_circley = 585
		screen.blit(pygame.font.SysFont('Times New Roman', 80).render("Setting_Ball", True, (171,171,171)), (30, 15))
		screen.blit(pygame.font.SysFont('Times New Roman', setball_fontsize[1]).render("Size", True, (255, 255, 255)), (80, 120))
		screen.blit(pygame.font.SysFont('Times New Roman', setball_fontsize[2]).render("Number", True, (255, 255, 255)), (80, 180))
		screen.blit(pygame.font.SysFont('Times New Roman', setball_fontsize[3]).render("Speed", True, (255, 255, 255)), (80, 240))
		screen.blit(pygame.font.SysFont('Times New Roman', setball_fontsize[4]).render("Reset", True, (255, 255, 255)), (80, 500))
		screen.blit(pygame.font.SysFont('Times New Roman', setball_fontsize[5]).render("Confirm", True, (255, 255, 255)), (80, 560))
		pygame.draw.circle(screen, (102,204,255), (60,setball_circley),6,0)
		#-------------------------------------------球的大小------------------------------------------------------#
		ball_r[1],ball_r[2] = 2**(ball_sizelv+1),2**(ball_sizelv+1)
		if ball_sizelv == 1:
			screen.blit(pygame.font.SysFont('Times New Roman', setball_fontsize[1]-5).render("Tiny", True, (255, 255, 255)), (350, 125))
			ball_r[1],ball_r[2] = 1,1
		elif ball_sizelv == 2:
			screen.blit(pygame.font.SysFont('Times New Roman', setball_fontsize[1]-5).render("Small", True, (255, 255, 255)), (350, 125))
		elif ball_sizelv == 3:
			screen.blit(pygame.font.SysFont('Times New Roman', setball_fontsize[1]-5).render("Medium", True, (255, 255, 255)), (350, 125))
		elif ball_sizelv == 4:
			screen.blit(pygame.font.SysFont('Times New Roman', setball_fontsize[1]-5).render("Big", True, (255, 255, 255)), (350, 125))
		elif ball_sizelv == 5:
			screen.blit(pygame.font.SysFont('Times New Roman', setball_fontsize[1]-5).render("Large", True, (255, 255, 255)), (350, 125))
		elif ball_sizelv == 6:
			screen.blit(pygame.font.SysFont('Times New Roman', setball_fontsize[1]-5).render("Enormous", True, (255, 255, 255)), (350, 125))
		#-------------------------------------------球的數量------------------------------------------------------#
		if ball_num == 1:
			screen.blit(pygame.font.SysFont('Times New Roman', setball_fontsize[2]-5).render("One", True, (255, 255, 255)), (350, 185))
		elif ball_num == 2:
			screen.blit(pygame.font.SysFont('Times New Roman', setball_fontsize[2]-5).render("Two", True, (255, 255, 255)), (350, 185))
		#-------------------------------------------球的速度------------------------------------------------------#
		ball_setspeedx[1],ball_setspeedy[1] = 0.25*(2**(ball_speedlv-1))*ball_basicspeedx[1],0.25*(2**(ball_speedlv-1))*ball_basicspeedy[1]
		ball_setspeedx[2],ball_setspeedy[2] = 0.25*(2**(ball_speedlv-1))*ball_basicspeedx[2],0.25*(2**(ball_speedlv-1))*ball_basicspeedy[2]
		if ball_speedlv == 1:
			screen.blit(pygame.font.SysFont('Times New Roman', setball_fontsize[3]-5).render("It take's forever", True, (255, 255, 255)), (350, 245))
			ball_setspeedx[1],ball_setspeedy[1]=0,0
			ball_setspeedx[2],ball_setspeedy[2]=0,0
			if setball_select == 3:
				drawrighttri(645,270,20,15)
		elif ball_speedlv == 2:
			screen.blit(pygame.font.SysFont('Times New Roman', setball_fontsize[3]-5).render("Snail", True, (255, 255, 255)), (350, 245))
		elif ball_speedlv == 3:
			screen.blit(pygame.font.SysFont('Times New Roman', setball_fontsize[3]-5).render("Slow", True, (255, 255, 255)), (350, 245))
		elif ball_speedlv == 4:
			screen.blit(pygame.font.SysFont('Times New Roman', setball_fontsize[3]-5).render("Normal", True, (255, 255, 255)), (350, 245))
		elif ball_speedlv == 5:
			screen.blit(pygame.font.SysFont('Times New Roman', setball_fontsize[3]-5).render("Fast", True, (255, 255, 255)), (350, 245))
		elif ball_speedlv == 6:
			screen.blit(pygame.font.SysFont('Times New Roman', setball_fontsize[3]-5).render("Bullet", True, (255, 255, 255)), (350, 245))
			ball_setspeedx[1],ball_setspeedy[1]=1200,1200
			ball_setspeedx[2],ball_setspeedy[2]=1199,1199
		elif ball_speedlv == 7:
			screen.blit(pygame.font.SysFont('Times New Roman', setball_fontsize[3]-5).render("What Happened !?", True, (255, 255, 255)), (350, 245))
			ball_setspeedx[1],ball_setspeedy[1]=100000,100000
			ball_setspeedx[2],ball_setspeedy[2]=99999,99999
		pygame.display.update()
		for events in pygame.event.get():
			if events.type == pygame.KEYDOWN:	
				if events.key == pygame.K_ESCAPE:
					quit_game()
				elif events.key == pygame.K_SPACE:
					if setball_select == 4:
						ball_sizelv,ball_num,ball_speedlv = 3,1,4
						setball_select=5
					elif setball_select == 5:
						setduel_select = 5
						gamestate = "setting_duel"
				elif events.key == pygame.K_d or events.key == pygame.K_RIGHT:
					if setball_select == 1 and ball_sizelv <= 4:
						ball_sizelv += 1
					elif setball_select == 2 and ball_num == 1:
						ball_num += 1
					elif setball_select == 3 and ball_speedlv <= 6:
						ball_speedlv += 1
				elif events.key == pygame.K_a or events.key == pygame.K_LEFT:
					if setball_select == 1 and ball_sizelv >= 2:
						ball_sizelv -= 1
					elif setball_select == 2 and ball_num == 2:
						ball_num -= 1
					elif setball_select == 3 and ball_speedlv >= 2:
						ball_speedlv -= 1
				elif events.key == pygame.K_BACKSPACE:
					gamestate = "setting_duel"
				elif events.key == pygame.K_TAB or events.key == pygame.K_s or events.key == pygame.K_DOWN:
					setball_select += 1
					if setball_select == 6:
						setball_select = 1
				elif events.key == pygame.K_w or events.key == pygame.K_UP :
					setball_select -= 1
					if setball_select == 0:
						setball_select = 5
	if gamestate == "setting_bar":
		screen.blit(background,(0,0))
		setbar_fontsize = [0,40,40,40,30,30]		
		setbar_fontsize[setbar_select] = setbar_fontsize[setbar_select]+10
		setbar_circley = 85+60*setbar_select
		if setbar_select == 1:
			screen.blit(exhibit_brs,(640,0))
			pygame.draw.line(screen, (0,0,255), (772,320-bar_half_length[1]), (772,320+bar_half_length[1]), bar_width)
			if bar_lengthlv >= 2:
				drawlefttri(370,150,20,15)
			if bar_lengthlv <= 4:
				drawrighttri(550,150,20,15)
		elif setbar_select == 2:
			screen.blit(exhibit_brs,(640,0))
			brspeedmilli = brspeedtimer.tick()
			brspeedtime += brspeedmilli
			brspeedexhibity += (bar_speed[1]*brspeedmilli/1000)
			pygame.draw.line(screen, (0,0,255), (772,int(brspeedexhibity)%560+40-40), (772,int(brspeedexhibity)%560+40+40), bar_width)
			if bar_speedlv >= 2:
				drawlefttri(370,210,20,15)
			if bar_speedlv <= 3:
				drawrighttri(550,210,20,15)
		elif setbar_select == 3:
			screen.blit(exhibit_brs,(640,0))
			if bar_freemove == 1:
				drawlefttri(370,270,20,15)
			if bar_freemove == 0:
				drawrighttri(470,270,20,15)
			brspeedmilli = brspeedtimer.tick()
			brspeedtime += brspeedmilli
			brspeedexhibity += (200*brspeedmilli*bar_exhibitdiry/1000)
			brspeedexhibitx += (100*brspeedmilli*bar_exhibitdirx/1000)
			if bar_freemove == 0:
				if brspeedexhibity > 560:
					brspeedexhibity = 320
					bar_exhibitdiry = -1
				if brspeedexhibity < 80:
					brspeedexhibity = 320
					bar_exhibitdiry = 1
				pygame.draw.line(screen, (0,0,255), (772,int(brspeedexhibity)-40), (772,int(brspeedexhibity)+40), bar_width)
			if bar_freemove == 1 :
				if bar_exhibitdirx == -1:
					screen.blit(control_a,(int(brspeedexhibitx)-65,295))
				if bar_exhibitdirx == 1:
					screen.blit(control_d,(int(brspeedexhibitx)+15,295))
				if brspeedexhibity > 520:
					brspeedexhibity = 320
					bar_exhibitdirx,bar_exhibitdiry = 0,-1
				if brspeedexhibity < 120:
					brspeedexhibity = 320
					bar_exhibitdirx,bar_exhibitdiry = -1,0
				if brspeedexhibitx > 900:
					brspeedexhibitx = 772
					bar_exhibitdirx,bar_exhibitdiry = 0,1
				if brspeedexhibitx < 650:
					brspeedexhibitx = 772
					bar_exhibitdirx,bar_exhibitdiry = 1,0
				pygame.draw.line(screen, (0,0,255), (int(brspeedexhibitx),int(brspeedexhibity)-40), (int(brspeedexhibitx),int(brspeedexhibity)+40), bar_width)
			if bar_exhibitdiry == -1:
				screen.blit(control_w,(750,int(brspeedexhibity)-100))
			if bar_exhibitdiry == 1:
				screen.blit(control_s,(750,int(brspeedexhibity)+50))
		elif setbar_select == 4:
			setbar_circley =525	
		elif setbar_select == 5:
			setbar_circley =585
		screen.blit(pygame.font.SysFont('Times New Roman', 80).render("Setting_Bar", True, (171,171,171)), (30,15))
		screen.blit(pygame.font.SysFont('Times New Roman', setbar_fontsize[1]).render("Length", True, (255, 255, 255)), (80, 120))
		screen.blit(pygame.font.SysFont('Times New Roman', setbar_fontsize[2]).render("Speed", True, (255, 255, 255)), (80, 180))
		screen.blit(pygame.font.SysFont('Times New Roman', setbar_fontsize[3]).render("Free_Move", True, (255, 255, 255)), (80, 240))
		screen.blit(pygame.font.SysFont('Times New Roman', setbar_fontsize[4]).render("Reset", True, (255, 255, 255)), (80, 500))
		screen.blit(pygame.font.SysFont('Times New Roman', setbar_fontsize[5]).render("Confirm", True, (255, 255, 255)), (80, 560))
		pygame.draw.circle(screen, (102,204,255), (60,setbar_circley),6,0)
		#-------------------------------------------BAR長度------------------------------------------------------#
		if bar_lengthlv == 1:
			screen.blit(pygame.font.SysFont('Times New Roman', setbar_fontsize[1]-5).render("Lucky ?", True, (255, 255, 255)), (380, 125))
			bar_half_length[1] = 2
		elif bar_lengthlv == 2:
			screen.blit(pygame.font.SysFont('Times New Roman', setbar_fontsize[1]-5).render("Short", True, (255, 255, 255)), (380, 125))
			bar_half_length[1] = 20
		elif bar_lengthlv == 3:
			screen.blit(pygame.font.SysFont('Times New Roman', setbar_fontsize[1]-5).render("Medium", True, (255, 255, 255)), (380, 125))
			bar_half_length[1] = 40
		elif bar_lengthlv == 4:
			screen.blit(pygame.font.SysFont('Times New Roman', setbar_fontsize[1]-5).render("Long", True, (255, 255, 255)), (380, 125))
			bar_half_length[1] = 80
		elif bar_lengthlv == 5:
			screen.blit(pygame.font.SysFont('Times New Roman', setbar_fontsize[1]-5).render("Like a boss", True, (255, 255, 255)), (380, 125))
			bar_half_length[1] = 320
		#-------------------------------------------BAR速度------------------------------------------------------#
		bar_speed[1] = 0.5*(2**bar_speedlv)*bar_basicspeed[1]
		if bar_speedlv == 1:
			screen.blit(pygame.font.SysFont('Times New Roman', setbar_fontsize[2]-5).render("Slow", True, (255, 255, 255)), (380, 185))
		elif bar_speedlv == 2:
			screen.blit(pygame.font.SysFont('Times New Roman', setbar_fontsize[2]-5).render("Medium", True, (255, 255, 255)), (380, 185))
		elif bar_speedlv == 3:
			screen.blit(pygame.font.SysFont('Times New Roman', setbar_fontsize[2]-5).render("Fast", True, (255, 255, 255)), (380, 185))
		elif bar_speedlv == 4:
			screen.blit(pygame.font.SysFont('Times New Roman', setbar_fontsize[2]-5).render("Extreme", True, (255, 255, 255)), (380, 185))
			bar_speed[1] = 10000
		if gm_select == 2:
			bar_speed[2] = bar_speed[1]
		#-------------------------------------------BAR自由運動------------------------------------------------------#
		if bar_freemove == 0:
			screen.blit(pygame.font.SysFont('Times New Roman', setbar_fontsize[3]-5).render("Off", True, (255, 255, 255)), (380, 245))
		elif bar_freemove == 1:
			screen.blit(pygame.font.SysFont('Times New Roman', setbar_fontsize[3]-5).render("On", True, (255, 255, 255)), (380, 245))
		pygame.display.update()
		for events in pygame.event.get():
			if events.type == pygame.KEYDOWN:	
				brspeedexhibitx,brspeedexhibity = 772,320
				if events.key == pygame.K_ESCAPE:
					quit_game()
				elif events.key == pygame.K_SPACE:
					if setbar_select == 4:
						bar_lengthlv,bar_speedlv,bar_freemove = 3,2,0
						setbar_select = 5
					elif setbar_select == 5:
						setduel_select = 5
						gamestate = "setting_duel"
				elif events.key == pygame.K_d or events.key == pygame.K_RIGHT:
					if setbar_select == 1 and bar_lengthlv <= 4:
						bar_lengthlv += 1
					elif setbar_select == 2 and bar_speedlv <= 3:
						bar_speedlv += 1
					elif setbar_select == 3 and bar_freemove == 0:
						bar_freemove += 1
				elif events.key == pygame.K_a or events.key == pygame.K_LEFT:
					if setbar_select == 1 and bar_lengthlv >= 2:
						bar_lengthlv -= 1
					elif setbar_select == 2 and bar_speedlv >= 2:
						bar_speedlv -= 1
					elif setbar_select == 3 and bar_freemove == 1:
						bar_freemove -= 1
				elif events.key == pygame.K_BACKSPACE:
					gamestate = "setting_duel"
				elif events.key == pygame.K_TAB or events.key == pygame.K_s or events.key == pygame.K_DOWN:
					setbar_select += 1
					if setbar_select == 6:
						setbar_select = 1
				elif events.key == pygame.K_w or events.key == pygame.K_UP :
					setbar_select -= 1	
					if setbar_select == 0:
						setbar_select = 5
	if gamestate == "setting_others":
		screen.blit(background,(0,0))
		setoth_fontsize = [0,40,40,40,30,30]
		setoth_fontsize[setoth_select] = setoth_fontsize[setoth_select]+10
		setoth_circley = 85+60*setoth_select
		if setoth_select == 1:
			if winscore >= 2:
				drawlefttri(430,150,20,15)
			drawrighttri(510,150,20,15)
		elif setoth_select == 2:
			if timelimit == 1:
				drawlefttri(430,210,20,15)
			drawrighttri(530,210,20,15)
		elif setoth_select == 3:
			if control == 2:
				drawlefttri(340,310,30,80)
			if control == 1:
				if bar_freemove == 0:
					drawrighttri(545,310,30,80)
				if bar_freemove == 1:
					drawrighttri(665,310,30,80)
		elif setoth_select == 4:
			setoth_circley =525
		elif setoth_select == 5:
			setoth_circley =585
		screen.blit(pygame.font.SysFont('Times New Roman', 80).render("Setting_Others", True, (171,171,171)), (30,15))
		screen.blit(pygame.font.SysFont('Times New Roman', setoth_fontsize[1]).render("Score_To_Win", True, (255, 255, 255)), (80, 120))
		screen.blit(pygame.font.SysFont('Times New Roman', setoth_fontsize[2]).render("Time_Limit", True, (255, 255, 255)), (80, 180))
		screen.blit(pygame.font.SysFont('Times New Roman', setoth_fontsize[3]).render("Control", True, (255, 255, 255)), (80, 240))
		screen.blit(pygame.font.SysFont('Times New Roman', setoth_fontsize[4]).render("Reset", True, (255, 255, 255)), (80, 500))
		screen.blit(pygame.font.SysFont('Times New Roman', setoth_fontsize[5]).render("Confirm", True, (255, 255, 255)), (80, 560))
		pygame.draw.circle(screen, (102,204,255), (60,setoth_circley),6,0)
		#-------------------------------------------Score-------------------------------------------------------#
		screen.blit(pygame.font.SysFont('Times New Roman', setoth_fontsize[1]-5).render("%d"%(winscore), True, (255, 255, 255)), (450, 125))
		#-------------------------------------------Time--------------------------------------------------------#
		if maxtime == 0:
			timelimit = 0
		else:
			timelimit = 1
		if timelimit == 1:
			screen.blit(pygame.font.SysFont('Times New Roman', setoth_fontsize[2]-5).render("%d"%(maxtime), True, (255, 255, 255)), (440, 185))
		if timelimit == 0:
			screen.blit(pygame.font.SysFont('Times New Roman', setoth_fontsize[2]-5).render("Off", True, (255, 255, 255)), (440, 185))
		#-------------------------------------------Control----------------------------------------------------#
		if control == 1:
			screen.blit(pygame.font.SysFont('Times New Roman', 40).render("P1 : ", True, (255, 255, 255)), (350, 245))
			screen.blit(control_w,(425,240))
			screen.blit(control_s,(485,240))
			screen.blit(pygame.font.SysFont('Times New Roman', 40).render("P2 : ", True, (255, 255, 255)), (350, 325))
			screen.blit(control_up,(425,320))
			screen.blit(control_down,(485,320))
			if bar_freemove == 1:
				screen.blit(control_a,(545,240))
				screen.blit(control_d,(605,240))
				screen.blit(control_left,(545,320))
				screen.blit(control_right,(605,320))
		elif control == 2:
			screen.blit(pygame.font.SysFont('Times New Roman', 40).render("P1 : ", True, (255, 255, 255)), (350, 245))
			screen.blit(control_w,(425,320))
			screen.blit(control_s,(485,320))
			screen.blit(pygame.font.SysFont('Times New Roman', 40).render("P2 : ", True, (255, 255, 255)), (350, 325))
			screen.blit(control_up,(425,240))
			screen.blit(control_down,(485,240))
			if bar_freemove == 1:
				screen.blit(control_a,(545,320))
				screen.blit(control_d,(605,320))
				screen.blit(control_left,(545,240))
				screen.blit(control_right,(605,240))
		pygame.display.update()
		for events in pygame.event.get():
			if events.type == pygame.KEYDOWN:	
				if events.key == pygame.K_ESCAPE:
					quit_game()
				elif events.key == pygame.K_SPACE:
					if setoth_select==4:
						winscore = 3
						maxtime = 60
						control = 1
						setoth_select=5
					elif setoth_select==5:
						setduel_select=5
						gamestate = "setting_duel"
				elif events.key == pygame.K_BACKSPACE:
					gamestate = "setting_duel"
				elif events.key == pygame.K_TAB or events.key == pygame.K_s or events.key == pygame.K_DOWN:
					setoth_select +=1
					if setoth_select == 6:
						setoth_select = 1
				elif events.key == pygame.K_w or events.key == pygame.K_UP :
					setoth_select -=1	
					if setoth_select == 0:
						setoth_select = 5
				if setoth_select == 1:
					if events.key == pygame.K_d or events.key == pygame.K_RIGHT:
						winscore += 1
					elif (events.key == pygame.K_a or events.key == pygame.K_LEFT) and winscore >= 2:
						winscore -= 1	
				if setoth_select == 2:
					if events.key == pygame.K_d or events.key == pygame.K_RIGHT:
						maxtime += 10
					elif (events.key == pygame.K_a or events.key == pygame.K_LEFT) and maxtime >= 10:
						maxtime -= 10
				if setoth_select == 3:
					if (events.key == pygame.K_d or events.key == pygame.K_RIGHT) and control == 1:
						control = 2
					elif (events.key == pygame.K_a or events.key == pygame.K_LEFT) and control == 2 :
						control = 1		
	if gamestate == "setting_surcat":
		screen.blit(background,(0,0))
		setsc_fontsize = [0,40,40,30]
		setsc_fontsize[setsc_select] = setsc_fontsize[setsc_select]+10
		if setsc_select == 1:
			setsc_circley = 145
			if control == 2:
				drawlefttri(340,185,30,80)
			if control == 1:
				drawrighttri(545,185,30,80)
		elif setsc_select == 2:
			setsc_circley = 285
		elif setsc_select == 3:
			setsc_circley = 585
		if gm_select == 3 or gm_select == 4:
			screen.blit(pygame.font.SysFont('Times New Roman', 80).render("Survival", True, (171,171,171)), (30,15))
			screen.blit(pygame.font.SysFont('Times New Roman', 40).render("1P_Highest_Score  :  %d"%(record_top5[3][1]), True, (171 ,171 ,171)), (80, 340))
			screen.blit(pygame.font.SysFont('Times New Roman', 40).render("2P_Highest_Score  :  %d"%(record_top5[4][1]), True, (171 ,171 ,171)), (80, 400))
		if gm_select == 5 or gm_select == 6:
			screen.blit(pygame.font.SysFont('Times New Roman', 80).render("CatchBall", True, (171,171,171)), (30,15))
			screen.blit(pygame.font.SysFont('Times New Roman', 40).render("1P_Highest_Score  :  %d"%(record_top5[5][1]), True, (171 ,171 ,171)), (80, 340))
			screen.blit(pygame.font.SysFont('Times New Roman', 40).render("2P_Highest_Score  :  %d"%(record_top5[6][1]), True, (171 ,171 ,171)), (80, 400))
		screen.blit(pygame.font.SysFont('Times New Roman', setsc_fontsize[1]).render("Control", True, (255, 255, 255)), (80, 120))
		screen.blit(pygame.font.SysFont('Times New Roman', setsc_fontsize[2]).render("Highscore_List", True, (255, 255, 255)), (80, 260))	
		screen.blit(pygame.font.SysFont('Times New Roman', setsc_fontsize[3]).render("Confirm", True, (255, 255, 255)), (80, 560))
		pygame.draw.circle(screen, (102,204,255), (60,setsc_circley),6,0)
		#-------------------------------------------Control----------------------------------------------------#
		if control == 1:
			screen.blit(pygame.font.SysFont('Times New Roman', 40).render("P1 : ", True, (255, 255, 255)), (350, 125))
			screen.blit(control_w,(425,120))
			screen.blit(control_s,(485,120))
			screen.blit(pygame.font.SysFont('Times New Roman', 40).render("P2 : ", True, (255, 255, 255)), (350, 205))
			screen.blit(control_up,(425,200))
			screen.blit(control_down,(485,200))
		elif control == 2:
			screen.blit(pygame.font.SysFont('Times New Roman', 40).render("P1 : ", True, (255, 255, 255)), (350, 125))
			screen.blit(control_w,(425,200))
			screen.blit(control_s,(485,200))
			screen.blit(pygame.font.SysFont('Times New Roman', 40).render("P2 : ", True, (255, 255, 255)), (350, 205))
			screen.blit(control_up,(425,120))
			screen.blit(control_down,(485,120))
		pygame.display.update()
		for events in pygame.event.get():
			if events.type == pygame.KEYDOWN:	
				if events.key == pygame.K_ESCAPE:
					quit_game()
				elif events.key == pygame.K_SPACE:
					if setsc_select == 2:
						gamestate = "highscore"
					if setsc_select == 3:
						scorer,winner = "",""
						score1,score2 = 0,0
						timeout = 0
						load_seconds=0
						gamescore[3],gamescore[4],gamescore[5],gamescore[6] = 0,0,0,0
						load_percentage = 0
						loadtimer = pygame.time.Clock()
						gamestate = "loading"
				elif events.key == pygame.K_BACKSPACE:
					gamestate = 'gamemode'
				elif events.key == pygame.K_TAB or events.key == pygame.K_s or events.key == pygame.K_DOWN:
					setsc_select += 1
					if setsc_select == 4:
						setsc_select = 1
				elif events.key == pygame.K_w or events.key == pygame.K_UP :
					setsc_select -=1	
					if setsc_select == 0:
						setsc_select = 3
				if setsc_select == 1:
					if (events.key == pygame.K_d or events.key == pygame.K_RIGHT) and control == 1:
						control = 2
					elif (events.key == pygame.K_a or events.key == pygame.K_LEFT) and control == 2:
						control = 1	
	if gamestate == "highscore":
		screen.blit(background,(0,0))
		screen.blit(pygame.font.SysFont('Times New Roman', 80).render("High Score List", True, (171,171,171)), (30,15))
		pygame.draw.line(screen, (221,221,221), (520,115), (520,600), 4)
		pygame.draw.line(screen, (221,221,221), (50,210), (900,210), 4)
		pygame.draw.line(screen, (221,221,221), (140,115), (140,600), 4)
		if newhigh != 0:
			hr[newhigh] = 50
			hrc[newhigh] = 0
		screen.blit(pygame.font.SysFont('Times New Roman', hr[1]).render("1st", True, (255,255,hrc[1])), (60,240))
		screen.blit(pygame.font.SysFont('Times New Roman', hr[2]).render("2nd", True, (255,255,hrc[2])), (60,310))
		screen.blit(pygame.font.SysFont('Times New Roman', hr[3]).render("3rd", True, (255,255,hrc[3])), (60,380))
		screen.blit(pygame.font.SysFont('Times New Roman', hr[4]).render("4th", True, (255,255,hrc[4])), (60,450))
		screen.blit(pygame.font.SysFont('Times New Roman', hr[5]).render("5th", True, (255,255,hrc[5])), (60,520))
		if gm_select == 3 or gm_select == 4:
			screen.blit(pygame.font.SysFont('Times New Roman', 50).render("Survival 1P", True, (255,255,255)), (200,140))
			screen.blit(pygame.font.SysFont('Times New Roman', 50).render("Survival 2P", True, (255,255,255)), (590,140))
			for i in [1,2,3,4,5]:
				screen.blit(pygame.font.SysFont('Times New Roman', h[i]).render("%d"%(record_top5[3][i]), True, (255,255,255)), (290,170+70*i))
				screen.blit(pygame.font.SysFont('Times New Roman', h[i+5]).render("%d"%(record_top5[4][i]), True, (255,255,255)), (680,170+70*i))
			if gm_select == 3 and newhigh != 0:
				h[newhigh] = 50
				screen.blit(pygame.font.SysFont('Times New Roman', 50).render("%d"%(record_top5[3][newhigh]), True, (255,255,0)), (290,170+70*newhigh))
			if gm_select == 4 and newhigh != 0:
				h[newhigh+5] = 50
				screen.blit(pygame.font.SysFont('Times New Roman', 50).render("%d"%(record_top5[4][newhigh]), True, (255,255,0)), (680,170+70*newhigh))
		if gm_select == 5 or gm_select == 6:
			screen.blit(pygame.font.SysFont('Times New Roman', 50).render("CatchBall 1P", True, (255,255,255)), (185,140))
			screen.blit(pygame.font.SysFont('Times New Roman', 50).render("CatchBall 2P", True, (255,255,255)), (580,140))
			for i in [1,2,3,4,5]:
				screen.blit(pygame.font.SysFont('Times New Roman', h[i]).render("%d"%(record_top5[5][i]), True, (255,255,255)), (290,170+70*i))
				screen.blit(pygame.font.SysFont('Times New Roman', h[i+5]).render("%d"%(record_top5[6][i]), True, (255,255,255)), (680,170+70*i))
			if gm_select == 5 and newhigh != 0:
				h[newhigh] = 50
				screen.blit(pygame.font.SysFont('Times New Roman', 50).render("%d"%(record_top5[5][newhigh]), True, (255,255,0)), (290,170+70*newhigh))
			if gm_select == 6 and newhigh != 0:
				h[newhigh+5] = 50
				screen.blit(pygame.font.SysFont('Times New Roman', 50).render("%d"%(record_top5[6][newhigh]), True, (255,255,0)), (680,170+70*newhigh))
		pygame.display.update()
		for events in pygame.event.get():
			if events.type == pygame.KEYDOWN:	
				if events.key == pygame.K_ESCAPE:
					quit_game()
				elif events.key == pygame.K_SPACE or events.key == pygame.K_BACKSPACE:
					h = [0,40,40,40,40,40,40,40,40,40,40]
					hr = [0,40,40,40,40,40]
					hrc = [0,255,255,255,255,255]
					newhigh = 0
					if temptgamestate == 0:
						gamestate = 'preparation'
						temptgamestate = ""
					else:
						if gm_select == 3 or gm_select == 4:
							gamestate = "setting_surcat"
						if gm_select == 5 or gm_select == 6:					
							gamestate = "setting_surcat"