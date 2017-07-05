#-*- coding: utf-8
import pygame,sys,random,string
#=============================初始化 BEGIN=============================#
pygame.init()
screen_width=960
mid_width=0.5*screen_width
screen_height=640
mid_height=0.5*screen_height
screen=pygame.display.set_mode((screen_width,screen_height),0,32)
bif = "tech.bmp" 
background=pygame.image.load(bif).convert()
sound1,sound2=pygame.mixer.Sound("01.wav"),pygame.mixer.Sound("02.wav")
soundaccel = pygame.mixer.Sound("45656_1082_1322.mp3")
winner=""
scorer=""
gamestate="home_page"
ball_r,ball2_r,ball3_r=16,16,16
bar_half_length=40
bar2_half_length=40
bar_width=8
barx=20
score1,score2=0,0
winscore=3
mode=1
pm = 8
timepm=0
set=5
sbl=1
sbr=1
sg=1
sc=3
opt=1
lan=1
sound=1
optball=1
ballsize = 3
ballnum = 1 # %2 == 1 : 一顆 ; %2 == 0 : 兩顆 #
ballspeed = 4
ball_basespeedx,ball_basespeedy=300,300
ball2_basespeedx,ball2_basespeedy=299,299
ball3_basespeedx,ball3_basespeedy=298,298
ball_speedx,ball_speedy = ball_basespeedx,ball_basespeedy
ball2_speedx,ball2_speedy = ball2_basespeedx,ball2_basespeedy
ball3_speedx,ball3_speedy = ball3_basespeedx,ball3_basespeedy
barlength=3
barspeed=2
barfreemove=0
bar_basespeed=400
bar2_basespeed=400
bar_speed,bar2_speed = bar_basespeed,bar2_basespeed
accelgra=350
accelballspeed=1.5
accelball = 0
accelball2 = 0
accelball3 = 0
lasermode,acceleration,invisibility,ran_reflect,gravity,curve_ball,wormhole = 0,0,0,0,0,0,0
ultitime = 90
timelimit = 1
comdiffi = 2
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
curvepm=0
blwh=0
grastatus = 0
grareversey1,grareversey2,grareversey3 = 0,0,0
grareversex1,grareversex2,grareversex3 = 0,0,0 
gra_ran=0
survivalscore = 0
catchscore = 0
laser = 0
lasertime = 0
laserouttime = 0
pmmodeon = 0
pmmodeonmax = 0
breakrecord = 0
grastatus = 0
acceldir = 1
#顏色(紅,綠,藍)#                                
#pic = 'bg.jpg'           
#image = pygame.image.load(pic).convert()                     加载图片，返回
#screen.blit(image,(0,0))                             显示图片位置为（0，0）  
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
ball,ball2,ball3 = 0,0,0
cb = 3
sur_1p_top5 = [0,0,0,0,0,0]
sur_2p_top5 = [0,0,0,0,0,0]
catch_1p_top5 = [0,0,0,0,0,0]
catch_2p_top5 = [0,0,0,0,0,0]
breakrecord,newhigh = 0,0
pointchange = 0
loadpercentage = 0
loadadd = 0
temptgamestate = ""
h = [40,40,40,40,40,40,40,40,40,40,40]
hr = [40,40,40,40,40,40]
hrc = [0,255,255,255,255,255]
#=============================初始化 END=============================#
#=============================結束pygame用的function BEGIN=============================#
def quit_game():
	pygame.display.quit()
	pygame.quit()
	sys.exit()
#=============================結束pygame用的function END=============================#
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
	sur_1p_top5[1] = string.atoi(a1)	
	a2 = f.readline()
	sur_1p_top5[2] = string.atoi(a2)
	a3 = f.readline()
	sur_1p_top5[3] = string.atoi(a3)
	a4 = f.readline()
	sur_1p_top5[4] = string.atoi(a4)
	a5 = f.readline()
	sur_1p_top5[5] = string.atoi(a5)
	f.close()	
def sur_2p_highscore():
	f = open( 'sur_2p_highscore.txt' , 'r+')
	a1 = f.readline()
	sur_2p_top5[1] = string.atoi(a1)	
	a2 = f.readline()
	sur_2p_top5[2] = string.atoi(a2)
	a3 = f.readline()
	sur_2p_top5[3] = string.atoi(a3)
	a4 = f.readline()
	sur_2p_top5[4] = string.atoi(a4)
	a5 = f.readline()
	sur_2p_top5[5] = string.atoi(a5)
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
		pygame.draw.line(screen, (255,255,255), (i,b-h), (i,b+h), 1)
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
		pygame.draw.line(screen, (255,255,255), (i,b-h), (i,b+h), 1)
		i += 1
def catch_1p_highscore():
	f = open( 'catch_1p_highscore.txt' , 'r+')
	a1 = f.readline()
	catch_1p_top5[1] = string.atoi(a1)	
	a2 = f.readline()
	catch_1p_top5[2] = string.atoi(a2)
	a3 = f.readline()
	catch_1p_top5[3] = string.atoi(a3)
	a4 = f.readline()
	catch_1p_top5[4] = string.atoi(a4)
	a5 = f.readline()
	catch_1p_top5[5] = string.atoi(a5)
	f.close()	
def catch_2p_highscore():
	f = open( 'catch_2p_highscore.txt' , 'r+')
	a1 = f.readline()
	catch_2p_top5[1] = string.atoi(a1)	
	a2 = f.readline()
	catch_2p_top5[2] = string.atoi(a2)
	a3 = f.readline()
	catch_2p_top5[3] = string.atoi(a3)
	a4 = f.readline()
	catch_2p_top5[4] = string.atoi(a4)
	a5 = f.readline()
	catch_2p_top5[5] = string.atoi(a5)
	f.close()	
	
	# 主程式
	
while True:	
	sur_1p_highscore()
	sur_2p_highscore()
	catch_1p_highscore()
	catch_2p_highscore()
#=================================================================================================#
	if gamestate == "home_page":
		#f = open( 'sur_1p_highscore.txt' , 'r+')
		#f.write("138\n78\n67\n54\n25\n")
		#f.close()	
		screen.blit(background,(0,0))
		#drawlefttri(100,200,50,50)
		#screen.blit(pygame.font.SysFont('Times New Roman', 30).render("%d"%(sur_1p_top5[5]), True, (255, 255, 255)), (80, 330))
		screen.blit(pygame.font.SysFont('Times New Roman', 120).render("Ping Pong Game", True, (171,171,171)), (80, 200))
		screen.blit(pygame.font.SysFont('Times New Roman', 40).render("Press any button but ESC to continue", True, (255, 255, 255)), (190, 370))
		screen.blit(pygame.font.SysFont('Times New Roman', 30).render("Press Space to move on to the next page.", True, (255, 255, 255)), (180, 440))
		screen.blit(pygame.font.SysFont('Times New Roman', 30).render("Press Backspace to go back to the previous page.", True, (255, 255, 255)), (180, 490))
		screen.blit(pygame.font.SysFont('Times New Roman', 30).render("Press ESC to quit the game.", True, (255, 255, 255)), (180, 540))
		screen.blit(pygame.font.SysFont('Times New Roman', 140).render("(", True, (255, 255, 255)), (120, 420))
		screen.blit(pygame.font.SysFont('Times New Roman', 140).render(")", True, (255, 255, 255)), (780, 420))
		for events in pygame.event.get():
			if events.type == pygame.KEYDOWN:	
				if events.key == pygame.K_ESCAPE:
					quit_game()
				else:
					gamestate = 11
		pygame.display.update()
#=================================================================================================#
	if gamestate == 11: #遊戲模式#
		screen.blit(background,(0,0))
		s1,s2,s3,s4,s5,s6,s7 = 40,40,40,40,40,40,30
		if mode != 7:
			screen.blit(exhibit_gm,(370,200))
		if mode == 1:
			s1 = 50
			modecircley =145
			screen.blit(pygame.font.SysFont('Times New Roman', 35).render("Player VS Computer", True, (255, 255, 255)), (525, 500))
		elif mode == 2:
			s2 = 50
			modecircley =215
			screen.blit(pygame.font.SysFont('Times New Roman', 35).render("Player VS Player", True, (255, 255, 255)), (525, 500))
		elif mode == 3:
			s3 = 50
			modecircley =285
			screen.blit(pygame.font.SysFont('Times New Roman', 35).render("Don't miss the ball.", True, (255, 255, 255)), (500, 455))
			screen.blit(pygame.font.SysFont('Times New Roman', 35).render("How long can you survive ?", True, (255, 255, 255)), (450, 500))
		elif mode == 4:
			s4 = 50
			modecircley =355
			screen.blit(pygame.font.SysFont('Times New Roman', 35).render("[Cooperation Mode]", True, (255, 255, 255)), (500, 500))
		elif mode == 5:
			s5 = 50
			modecircley =425
			screen.blit(pygame.font.SysFont('Times New Roman', 35).render("How many times can you catch", True, (255, 255, 255)), (420, 455))
			screen.blit(pygame.font.SysFont('Times New Roman', 35).render("a ball within 90 seconds ?", True, (255, 255, 255)), (450, 500))
		elif mode == 6:
			s6 =50
			modecircley =495
			screen.blit(pygame.font.SysFont('Times New Roman', 35).render("[Cooperation Mode]", True, (255, 255, 255)), (500, 500))
		elif mode == 7:
			s7 =40
			modecircley =595
		screen.blit(pygame.font.SysFont('Times New Roman', 80).render("Ping Pong Game", True, (171,171,171)), (30, 15))
		screen.blit(pygame.font.SysFont('Times New Roman', s1).render("Duel_1P", True, (255, 255, 255)), (80, 120))
		screen.blit(pygame.font.SysFont('Times New Roman', s2).render("Duel_2P", True, (255, 255, 255)), (80, 190))
		screen.blit(pygame.font.SysFont('Times New Roman', s3).render("Survival_1P", True, (255, 255, 255)), (80, 260))
		screen.blit(pygame.font.SysFont('Times New Roman', s4).render("Survival_2P", True, (255, 255, 255)), (80, 330))
		screen.blit(pygame.font.SysFont('Times New Roman', s5).render("CatchBall_1P", True, (255, 255, 255)), (80, 400))
		screen.blit(pygame.font.SysFont('Times New Roman', s6).render("CatchBall_2P", True, (255, 255, 255)), (80, 470))
		screen.blit(pygame.font.SysFont('Times New Roman', s7).render("Quit", True, (255, 255, 255)), (80, 570))
		pygame.draw.circle(screen, (255,255,255), (60,modecircley),6,0)
		#---------------------------Gamemode_Picture----------------------------#
		if mode == 1 or mode == 2:
			screen.blit(pygame.font.SysFont('Times New Roman', 20).render("90", True, (255, 255, 255)), (635, 210))
		if mode == 5 or mode == 6:
			screen.blit(pygame.font.SysFont('Times New Roman', 20).render("90", True, (255, 255, 255)), (635, 210))
		if mode != 7:
			screen.blit(pygame.font.SysFont('Times New Roman', 25).render("P1", True, (0, 0, 255)), (380, 220))
			pygame.draw.line(screen, (0,0,255), (385,330-20), (385,330+20), 4)			
		if mode == 1:
			screen.blit(pygame.font.SysFont('Times New Roman', 25).render("Com", True, (0, 255, 0)), (850, 320))
			pygame.draw.line(screen, (0,255,0), (888,410-20), (888,410+20), 4)
		if mode == 2:
			screen.blit(pygame.font.SysFont('Times New Roman', 25).render("P2", True, (255, 0, 0)), (870, 320))
			pygame.draw.line(screen, (255,0,0), (888,410-20), (888,410+20), 4)	
		if mode == 4 or mode == 6:
			screen.blit(pygame.font.SysFont('Times New Roman', 25).render("P2", True, (255, 0, 0)), (415, 320))
			pygame.draw.line(screen, (255,0,0), (430,410-20), (430,410+20), 4)	
		ballx,bally = 700,440
		if mode != 7:
			pygame.draw.circle(screen, (204,255,255), (int(ballx),int(bally)), 8,0)	
		if mode == 3 or mode == 4 or mode == 5 or mode == 6:
			screen.blit(pygame.font.SysFont('Times New Roman', 20).render("Score : 0", True, (255, 255, 255)), (800,210))
		if mode != 7:
			screen.blit(control_30_w,(373,270))
			screen.blit(control_30_s,(373,360))
		if mode == 2:
			screen.blit(control_30_up,(875,350))
			screen.blit(control_30_down,(875,440))
		if mode == 4 or mode == 6:
			screen.blit(control_30_up,(418,350))
			screen.blit(control_30_down,(418,440))
		#-----------------------------------------------------------------------#
		pygame.display.update()
		for events in pygame.event.get():
			if events.type == pygame.KEYDOWN:	
				if events.key == pygame.K_ESCAPE:
					quit_game()
				elif events.key == pygame.K_SPACE:
					if mode == 7:
						quit_game()
					if mode == 1 or mode == 2:
						bar2_speed = bar_speed
						ballx,bally=730,350
						ball_dirx,ball_diry=1,1	
						clockpm=pygame.time.Clock()
						lasermode,acceleration,invisibility,ran_reflect,gravity,curve_ball,wormhole = 0,0,0,0,0,0,0
						gamestate = "playmode"						
					if mode == 3 or mode == 4:
						lasermode,acceleration,invisibility,ran_reflect,gravity,curve_ball,wormhole = 0,0,0,0,0,0,0
						gamestate = "setting_survival"
					if mode == 5 or mode == 6:
						lasermode,acceleration,invisibility,ran_reflect,gravity,curve_ball,wormhole = 0,0,0,0,0,0,0
						gamestate = "setting_catch"
				elif events.key == pygame.K_BACKSPACE:
					gamestate = "home_page"
				elif events.key == pygame.K_TAB or events.key == pygame.K_s or events.key == pygame.K_DOWN:
					mode +=1
					if mode == 8:
						mode = 1
				elif events.key == pygame.K_w or events.key == pygame.K_UP :
					mode -=1
					if mode == 0:
						mode = 7
#=================================================================================================#
	if gamestate == "playmode":
		screen.blit(background,(0,0))
		survivalscore,catchscore = 0,0
		pm1,pm2,pm3,pm4,pm5,pm6,pm7,pm8  = 40,40,40,40,40,40,40,30
		if pm != 8:
			screen.blit(exhibit_bls,(550,200))
		if pm == 1:
			pm1 = 50
			pmcircley =145
			screen.blit(laser_50,(550,200))
			drawlefttri(405,150,20,15)
			drawrighttri(500,150,20,15)
			screen.blit(pygame.font.SysFont('Times New Roman', 20).render("You'll lose immediately if you're", True, (255, 255, 255)), (565, 420))
			screen.blit(pygame.font.SysFont('Times New Roman', 20).render("hit by a laser ray,", True, (255, 255, 255)), (565, 445))
			screen.blit(pygame.font.SysFont('Times New Roman', 20).render("or lose 5 points in CatchBall.", True, (255, 255, 255)), (565, 470))
		elif pm == 2:
			pm2 = 50
			pmcircley =205
			screen.blit(accel_50,(550,200))
			drawlefttri(405,210,20,15)
			drawrighttri(500,210,20,15)
			screen.blit(pygame.font.SysFont('Times New Roman', 20).render("The accelerator will increase the ball's", True, (255, 255, 255)), (565, 445))
			screen.blit(pygame.font.SysFont('Times New Roman', 20).render("speed by 1.5 until it hits a bar.", True, (255, 255, 255)), (565, 470))
		elif pm == 3:
			pm3 = 50
			pmcircley =265
			screen.blit(invis_50,(550,200))
			drawlefttri(405,270,20,15)
			drawrighttri(500,270,20,15)
			pygame.draw.line(screen, (200,200,200), (550+90,200), (550+90,500), 2)
			pygame.draw.line(screen, (200,200,200), (550+270,200), (550+270,500), 2)
			screen.blit(pygame.font.SysFont('Times New Roman', 20).render("Fortunately, the ball won't be invisible", True, (255, 255, 255)), (565, 445))
			screen.blit(pygame.font.SysFont('Times New Roman', 20).render("when it's accelerated.", True, (255, 255, 255)), (565, 470))
		elif pm == 4:
			pm4 = 50
			pmcircley =325
			screen.blit(bounce_50,(550,200))
			drawlefttri(405,330,20,15)
			drawrighttri(500,330,20,15)
			screen.blit(pygame.font.SysFont('Times New Roman', 20).render("The direction of the ball after it hits", True, (255, 255, 255)), (565, 445))
			screen.blit(pygame.font.SysFont('Times New Roman', 20).render("a surface is unpredictable", True, (255, 255, 255)), (565, 470))
		elif pm == 5:
			pm5 = 50
			pmcircley =385
			screen.blit(gra_50,(550,200))
			drawlefttri(405,390,20,15)
			drawrighttri(500,390,20,15)
			screen.blit(pygame.font.SysFont('Times New Roman', 20).render("The direction of the gravity field", True, (255, 255, 255)), (565, 445))
			screen.blit(pygame.font.SysFont('Times New Roman', 20).render("varies every 5 seconds.", True, (255, 255, 255)), (565, 470))
		elif pm == 6:
			pm6 = 50
			pmcircley =445
			screen.blit(vibrate_50,(550,200))
			drawlefttri(405,450,20,15)
			drawrighttri(500,450,20,15)
			screen.blit(pygame.font.SysFont('Times New Roman', 20).render("It will be difficult to predict", True, (255, 255, 255)), (565, 445))
			screen.blit(pygame.font.SysFont('Times New Roman', 20).render("where the ball is heading for.", True, (255, 255, 255)), (565, 470))
		elif pm == 7:
			pm7 = 50
			pmcircley =505
			screen.blit(wh_50,(550,200))
			drawlefttri(405,510,20,15)
			drawrighttri(500,510,20,15)
			screen.blit(pygame.font.SysFont('Times New Roman', 20).render("When a ball enters a wormhole, it'll", True, (255, 255, 255)), (565, 445))
			screen.blit(pygame.font.SysFont('Times New Roman', 20).render("come out from the other one.", True, (255, 255, 255)), (565, 470))
		elif pm == 8:
			pm8 = 40
			pmcircley =595
		pygame.draw.circle(screen, (255,255,255), (60,pmcircley),6,0)
		screen.blit(pygame.font.SysFont('Times New Roman', 80).render("Mode", True, (171,171,171)), (30,15))
		screen.blit(pygame.font.SysFont('Times New Roman', pm1).render("Laser", True, (255, 255, 255)), (80, 120))
		screen.blit(pygame.font.SysFont('Times New Roman', pm2).render("Acceleration", True, (255, 255, 255)), (80, 180))
		screen.blit(pygame.font.SysFont('Times New Roman', pm3).render("Invisibility", True, (255, 255, 255)), (80, 240))
		screen.blit(pygame.font.SysFont('Times New Roman', pm4).render("CrazyBounce", True, (255, 255, 255)), (80, 300))
		screen.blit(pygame.font.SysFont('Times New Roman', pm5).render("Gravity", True, (255, 255, 255)), (80, 360))
		screen.blit(pygame.font.SysFont('Times New Roman', pm6).render("Vibration", True, (255, 255, 255)), (80, 420))
		screen.blit(pygame.font.SysFont('Times New Roman', pm7).render("Wormhole", True, (255, 255, 255)), (80, 480))
		screen.blit(pygame.font.SysFont('Times New Roman', pm8).render("Continue", True, (255, 255, 255)), (80, 570))
		if (lasermode%2) == 1:
			screen.blit(pygame.font.SysFont('Times New Roman', pm1-5).render("On", True, (255, 255, 255)), (420, 125))	
		elif (lasermode%2) == 0:
			screen.blit(pygame.font.SysFont('Times New Roman', pm1-5).render("Off", True, (255, 255, 255)), (420, 125))
		if (acceleration%2) == 1:
			screen.blit(pygame.font.SysFont('Times New Roman', pm2-5).render("On", True, (255, 255, 255)), (420, 185))	
		elif (acceleration%2) == 0:
			screen.blit(pygame.font.SysFont('Times New Roman', pm2-5).render("Off", True, (255, 255, 255)), (420, 185))
		if (invisibility%2) == 1:
			screen.blit(pygame.font.SysFont('Times New Roman', pm3-5).render("On", True, (255, 255, 255)), (420, 245))	
		elif (invisibility%2) == 0:
			screen.blit(pygame.font.SysFont('Times New Roman', pm3-5).render("Off", True, (255, 255, 255)), (420, 245))
		if (ran_reflect%2) == 1:
			screen.blit(pygame.font.SysFont('Times New Roman', pm4-5).render("On", True, (255, 255, 255)), (420, 305))	
		elif (ran_reflect%2) == 0:
			screen.blit(pygame.font.SysFont('Times New Roman', pm4-5).render("Off", True, (255, 255, 255)), (420, 305))
		if (gravity%2) == 1:
			screen.blit(pygame.font.SysFont('Times New Roman', pm5-5).render("On", True, (255, 255, 255)), (420, 365))	
		elif (gravity%2) == 0:
			screen.blit(pygame.font.SysFont('Times New Roman', pm5-5).render("Off", True, (255, 255, 255)), (420, 365))
		if (curve_ball%2) == 1:
			screen.blit(pygame.font.SysFont('Times New Roman', pm6-5).render("On", True, (255, 255, 255)), (420, 425))	
		elif (curve_ball%2) == 0:
			screen.blit(pygame.font.SysFont('Times New Roman', pm6-5).render("Off", True, (255, 255, 255)), (420, 425))
		if (wormhole%2) == 1:
			screen.blit(pygame.font.SysFont('Times New Roman', pm7-5).render("On", True, (255, 255, 255)), (420, 485))	
		elif (wormhole%2) == 0:
			screen.blit(pygame.font.SysFont('Times New Roman', pm7-5).render("Off", True, (255, 255, 255)), (420, 485))
		for events in pygame.event.get():
			if events.type == pygame.KEYDOWN:	
				if events.key == pygame.K_ESCAPE:
					quit_game()
				if events.key == pygame.K_d or events.key == pygame.K_RIGHT:
					if pm == 1:
						lasermode += 1
					if pm == 2:
						acceleration += 1
					if pm == 3:
						invisibility += 1
					if pm == 4:
						ran_reflect += 1
					if pm == 5:
						gravity += 1
					if pm == 6:
						curve_ball += 1
					if pm == 7:
						wormhole += 1
				if events.key == pygame.K_a or events.key == pygame.K_LEFT:
					if pm == 1:
						lasermode -= 1
					if pm == 2:
						acceleration -= 1
					if pm == 3:
						invisibility -= 1
					if pm == 4:
						ran_reflect -= 1
					if pm == 5:
						gravity -= 1
					if pm == 6:
						curve_ball -= 1
					if pm == 7:
						wormhole -= 1
				if events.key == pygame.K_SPACE and pm == 8:
					gamestate = "setting_duel"
				if events.key == pygame.K_BACKSPACE:
					gamestate = 11
				if events.key == pygame.K_TAB or events.key == pygame.K_s or events.key == pygame.K_DOWN:
					ball_speedx,ball_speedy = 400,400
					pm+=1
					if pm == 9:
						pm = 1
				if events.key == pygame.K_w or events.key == pygame.K_UP :
					ball_speedx,ball_speedy = 400,400
					pm-=1
					if pm == 0:
						pm = 8
		#=============================計算時間 BEGIN=============================#
		millipm=clockpm.tick()
		secondspm=millipm/1000.0
		timepm += millipm
		#=============================計算時間 END=============================#
		#=============================計算球和棒子的新位置 BEGIN=============================#
		#------------------------------Gravity---------------------------#
		if pm == 5:
			screen.blit(control_down,(600,200))
			ball_speedx = 500
			if ball_diry >= 0:
				ball_speedy += 750*secondspm
			if ball_diry < 0:
				ball_speedy -= 750*secondspm
				if ball_speedy < 0:
					ball_speedy = -ball_speedy
					ball_diry = -ball_diry
		#----------------------------------------------------------------#
		ballx+=secondspm*ball_dirx*ball_speedx
		bally+=secondspm*ball_diry*ball_speedy
		#-----------------------------球撞到左邊的邊緣時BEGIN---------------------------#
		if bally > 515:
			bally = 485
		if ballx<565 and  ball_dirx < 0:
			accelball = 0
			if pm != 4:
				ball_dirx=-ball_dirx
			#------------------RANDOM_REFLECTION-----------------------------------#
			if pm == 4:
				rrx1 = 6*random.random()
				if rrx1 >= 0 and rrx1 < 1:
					ball_dirx,ball_diry=1.22,0.71
				elif rrx1 >= 1 and rrx1 < 2:
					ball_dirx,ball_diry=1,1						
				elif rrx1 >= 2 and rrx1 < 3:
					ball_dirx,ball_diry=1.13,0.85
				elif rrx1 >= 3 and rrx1 < 4:
					ball_dirx,ball_diry=1.13,-0.85
				elif rrx1 >= 4 and rrx1 < 5:
					ball_dirx,ball_diry=1,-1
				elif rrx1 >= 5 and rrx1 <= 6:
					ball_dirx,ball_diry=1.22,-0.71
		#-----------------------------球撞到左邊的邊緣時END-----------------------------#
		#-----------------------------球撞到右邊的邊緣時BEGIN---------------------------#
		elif ballx>885 and ball_dirx > 0:
			accelball = 0
			if pm != 4:
				ball_dirx=-ball_dirx
			#------------------RANDOM_REFLECTION-----------------------------------#
			if pm == 4:
				rrx1 = 6*random.random()
				if rrx1 >= 0 and rrx1 < 1:
					ball_dirx,ball_diry=-1.22,0.71
				elif rrx1 >= 1 and rrx1 < 2:
					ball_dirx,ball_diry=-1,1						
				elif rrx1 >= 2 and rrx1 < 3:
					ball_dirx,ball_diry=-1.13,0.85
				elif rrx1 >= 3 and rrx1 < 4:
					ball_dirx,ball_diry=-1.13,-0.85
				elif rrx1 >= 4 and rrx1 < 5:
					ball_dirx,ball_diry=-1,-1
				elif rrx1 >= 5 and rrx1 <= 6:
					ball_dirx,ball_diry=-1.22,-0.71
		#-----------------------------球撞到右邊的邊緣時END------------------------------#
		#-----------------------------球1撞到上方的邊緣時BEGIN---------------------------#
		if(bally<210) and ball_diry < 0 :
			accelball = 0
			if pm != 4:
				ball_diry=-ball_diry
			#------------------RANDOM_REFLECTION-----------------------------------#
			if pm == 4:
				rrx1 = 6*random.random()
				if rrx1 >= 0 and rrx1 < 1:
					ball_dirx,ball_diry=1.22,0.71
				elif rrx1 >= 1 and rrx1 < 2:
					ball_dirx,ball_diry=1,1						
				elif rrx1 >= 2 and rrx1 < 3:
					ball_dirx,ball_diry=1.13,0.85
				elif rrx1 >= 3 and rrx1 < 4:
					ball_dirx,ball_diry=-1.13,0.85
				elif rrx1 >= 4 and rrx1 < 5:
					ball_dirx,ball_diry=-1,1
				elif rrx1 >= 5 and rrx1 <= 6:
					ball_dirx,ball_diry=-1.22,0.71
			#------------------RANDOM_REFLECTION-----------------------------------#
		#-----------------------------球1撞到上方的邊緣時END-----------------------------#
		#-----------------------------球1撞到下方的邊緣時BEGIN---------------------------#
		if(bally>490)and (ball_diry > 0):
			accelball = 0
			if pm != 4:
				ball_diry=-ball_diry
			#------------------RANDOM_REFLECTION-----------------------------------#
			if pm == 4:
				rrx1 = 6*random.random()
				if rrx1 >= 0 and rrx1 < 1:
					ball_dirx,ball_diry=1.22,-0.71
				elif rrx1 >= 1 and rrx1 < 2:
					ball_dirx,ball_diry=1,-1						
				elif rrx1 >= 2 and rrx1 < 3:
					ball_dirx,ball_diry=1.13,-0.85
				elif rrx1 >= 3 and rrx1 < 4:
					ball_dirx,ball_diry=-1.13,-0.85
				elif rrx1 >= 4 and rrx1 < 5:
					ball_dirx,ball_diry=-1,-1
				elif rrx1 >= 5 and rrx1 <= 6:
					ball_dirx,ball_diry=-1.22,-0.71
			#------------------RANDOM_REFLECTION-----------------------------------#
		#-----------------------------球1撞到下方的邊緣時END-----------------------------#
		#===================================遊戲畫面BEGIN==================================#
		#---------------------------Normal----------------------------------#
		#-------------------------------------------------------------------#
		#---------------------------Acceleration----------------------------#
		if pm == 2:
			pygame.draw.line(screen, (255,255,0), (730,310), (730,390), 120)
			pygame.draw.line(screen, (0,255,0), (730+12-60,310+8), (730+36-60,310+40), 8)
			pygame.draw.line(screen, (0,255,0), (730+12-60,310+72), (730+36-60,310+40), 8)
			pygame.draw.line(screen, (0,255,0), (730+36-60,310+8), (730+60-60,310+40), 8)
			pygame.draw.line(screen, (0,255,0), (730+36-60,310+72), (730+60-60,310+40), 8)				
			pygame.draw.line(screen, (0,255,0), (730+60-60,310+8), (730+84-60,310+40), 8)
			pygame.draw.line(screen, (0,255,0), (730+60-60,310+72), (730+84-60,310+40), 8)
			pygame.draw.line(screen, (0,255,0), (730+84-60,310+8), (730+108-60,310+40), 8)
			pygame.draw.line(screen, (0,255,0), (730+84-60,310+72), (730+108-60,310+40), 8)
			if ballx <= 790  and ballx >= 670 and bally >= 310 and bally <= 390 and accelball == 0:
				ball_speedx,ball_speedy = 800,800
				accelball = 1
			if accelball == 0:
				ball_speedx,ball_speedy = 400,400
			if accelball == 1:
				pygame.draw.circle(screen, (204,0,204), (int(ballx),int(bally)), 10,0)
			if accelball == 0:
				pygame.draw.circle(screen, (204,255,255), (int(ballx),int(bally)), 10,0)
		#-------------------------------------------------------------------#
		#---------------------------Curve_ball------------------------------#
		if pm == 6:
			if (timepm)%100 <= 5 and curvepm == 0:
				ball_diry = -ball_diry
				curvepm = 1
			if (timepm)%100 >= 50 and (timepm)%100 <= 60:
				curvepm = 0
		#-------------------------------------------------------------------#
		#---------------------------Wormhole--------------------------------#
		if pm == 7:
			pygame.draw.circle(screen, (30,30,30), (640,350), 40,0)
			pygame.draw.circle(screen, (30,30,30), (820,350), 40,0)
			screen.blit(blackhole_56,(640-28,350-28))
			screen.blit(blackhole_56,(820-28,350-28))
			disblwh1 = (ballx-640)*(ballx-640) + (bally-350)*(bally-350)
			disblwh2 = (ballx-820)*(ballx-820) + (bally-350)*(bally-350)
			if disblwh2 > 1600 and disblwh1 > 1600:
				blwh = 0
			if disblwh1 <= 1600 and blwh == 0:
				ballx,bally = 820,350
				blwh = 1
			if disblwh2 <= 1600 and blwh == 0:
				ballx,bally = 640,350
				blwh = 1
		#-------------------------------------------------------------------#
		#---------------------------Invisibility-----------------------------#
		if ((pm != 3) or ( pm == 3 and  ((ballx < 640 or ballx > 820) or (ballx > 725 and ballx < 735) ))) and pm != 1 and pm != 8:
			if accelball == 0:
				pygame.draw.circle(screen, (204,255,255), (int(ballx),int(bally)), 10 ,0)	
		#-------------------------------------------------------------------#
		if pm == 1:
			if laser == 0:
				laserresttime = 0
				laserouttime = 0
				lasertime = timepm
				laser = 1
			if laser == 1:
				pygame.draw.line(screen, (255,0,0), (726,350), (726,351), 350)
				lasercountdown = 3-int((timepm - lasertime)/1000)
				screen.blit(pygame.font.SysFont('Times New Roman', 40).render("Laser in %d"%(lasercountdown), True, (255, 0, 0)), (650, 210))
				if (timepm - lasertime) >= 3000:
					laserouttime = timepm
					laser = 2
			if laser == 2:
				lasertime = 0
				pygame.draw.line(screen, (255,0,0), (726,330), (726,370), 350)
				if (timepm - laserouttime) >= 800:
					laserresttime = timepm
					laser = 3
			if laser == 3:
				screen.blit(pygame.font.SysFont('Times New Roman', 40).render("You lose", True, (255, 255, 255)), (660, 330))
				if timepm - laserresttime >= 2000:
					laser = 0
			if laser != 3:
				pygame.draw.line(screen, (0,0,255), (570,310), (570,390), bar_width)
			
		#-------------testing----------------#
		#screen.blit(pygame.font.SysFont('Times New Roman', 30).render("%d"%(lasermode), True, (255, 0, 0)), (300,100))	
		#screen.blit(pygame.font.SysFont('Times New Roman', 30).render("%d"%(ballx), True, (255, 0, 0)), (300,200))
		#===================================遊戲畫面END====================================#
		pygame.display.update()
#=================================================================================================#
	if gamestate == "setting_duel":
		screen.blit(background,(0,0))
		set1,set2,set3,set4,set5 = 40,40,40,40,30
		if set == 1:
			set1 = 50
			settingcircley = 145
		elif set == 2:
			set2 = 50
			settingcircley = 205
		elif set == 3:
			set3 = 50
			settingcircley = 265
		elif set == 4:
			set4 = 50
			settingcircley = 325
			drawlefttri(340,330,20,15)
		elif set == 5:
			set5 = 40
			settingcircley = 575
		screen.blit(pygame.font.SysFont('Times New Roman', 80).render("Duel", True, (171,171,171)), (30, 15))
		screen.blit(pygame.font.SysFont('Times New Roman', set1).render("Ball", True, (255, 255, 255)), (80, 120))
		screen.blit(pygame.font.SysFont('Times New Roman', set2).render("Bar", True, (255, 255, 255)), (80, 180))
		screen.blit(pygame.font.SysFont('Times New Roman', set3).render("Others", True, (255, 255, 255)), (80, 240))
		if mode != 2:
			screen.blit(pygame.font.SysFont('Times New Roman', set4).render("Difficulty", True, (255, 255, 255)), (80, 300))
		screen.blit(pygame.font.SysFont('Times New Roman', set5).render("Start", True, (255, 255, 255)), (80, 550))
		pygame.draw.circle(screen, (255,255,255), (60,settingcircley),6,0)
		#----------------------------------------Difficulty--------------------------------------------#
		if mode == 1:
			if (comdiffi%4) == 1:
				screen.blit(pygame.font.SysFont('Times New Roman', set4-5).render("Advantage", True, (255, 255, 255)), (350, 305))
				if set == 4:
					drawrighttri(560,330,20,15)
				bar2_speed = 0.5*bar2_basespeed
			elif (comdiffi%4) == 2:
				screen.blit(pygame.font.SysFont('Times New Roman', set4-5).render("Fair_Game", True, (255, 255, 255)), (350, 305))
				if set == 4:
					drawrighttri(565,330,20,15)
				bar2_speed = bar2_basespeed
			elif (comdiffi%4) == 3:
				screen.blit(pygame.font.SysFont('Times New Roman', set4-5).render("Disadvantage", True, (255, 255, 255)), (350, 305))
				if set == 4:
					drawrighttri(620,330,20,15)
				bar2_speed = 2*bar2_basespeed
			elif (comdiffi%4) == 0:
				screen.blit(pygame.font.SysFont('Times New Roman', set4-5).render("Mission_Impossible", True, (255, 255, 255)), (350, 305))
				if set == 4:
					drawrighttri(730,330,20,15)
				bar2_speed=10000
		#----------------------------------------------------------------------------------------------#
		for events in pygame.event.get():
			if events.type == pygame.KEYDOWN:	
				if events.key == pygame.K_ESCAPE:
					quit_game()
				elif events.key == pygame.K_SPACE:
					if set == 5:
						scorer = ""
						winner = ""
						score1,score2 = 0,0
						timeout = 0
						loadseconds=0
						loadtime=0
						survivalscore,catchscore = 0,0
						loadpercentage = 0
						loadtimer = pygame.time.Clock()
						gamestate = "loading"
					elif set == 1:
						blspeedtimer=pygame.time.Clock()
						gamestate = "setting_ball"
					elif set == 2:
						brspeedtimer=pygame.time.Clock()
						ranbarexhibit = 5*random.random ()
						gamestate = "setting_bar"
					elif set == 3:
						gamestate = "setting_others"
				if events.key == pygame.K_d or events.key == pygame.K_RIGHT:	
					if set == 4:
						comdiffi += 1
				if events.key == pygame.K_a or events.key == pygame.K_LEFT:	
					if set == 4:
						comdiffi -= 1
				if events.key == pygame.K_BACKSPACE:
					if mode == 1 or mode == 2:
						ballx,bally=730,350
						ball_dirx,ball_diry=1,1
						ball_speedx,ball_speedy = 300,400
						lasermode,acceleration,invisibility,ran_reflect,gravity,curve_ball,wormhole = 0,0,0,0,0,0,0
						clockpm=pygame.time.Clock()
						gamestate = "playmode"
				elif events.key == pygame.K_TAB or events.key == pygame.K_s or events.key == pygame.K_DOWN:
					set += 1
					if set == 6:
						set = 1
					if mode == 2 and set == 4:
						set = 5
				elif events.key == pygame.K_w or events.key == pygame.K_UP :
					set -= 1
					if set == 0:
						set = 5
					if mode == 2 and set == 4:
						set = 3
		pygame.display.update()
#=================================================================================================#
	if gamestate == "loading" :
		screen.blit(background,(0,0))
		screen.blit(pygame.font.SysFont('Times New Roman', 100).render("Loading...", True, (255, 255, 255)), (285, 220))
		loadlength = int(760*loadpercentage/100)
		loadmilli=loadtimer.tick()
		loadseconds+=loadmilli
		#if loadseconds >= 1000:
		#	loadtime += 1
		#	loadseconds = 0
		if loadseconds%1000 <= 10 and loadadd == 0 and loadseconds >= 1000:
			loadaddran = random.random()
			loadpercentage += (loadaddran*15 + 10)
			loadadd = 1
		if loadseconds%1000 >= 480 and loadadd == 1:
			loadadd = 0
		if loadpercentage >= 150:
			screen.blit(pygame.font.SysFont('Times New Roman', 40).render("Please press space to continue", True, (255, 255, 255)), (250, 380))
		if loadpercentage <= 150:	
			pygame.draw.line(screen, (255,255,255), (480,450), (480,454), 760)
			pygame.draw.line(screen, (255,255,255), (480,530), (480,534), 760)
			pygame.draw.line(screen, (255,255,255), (100,450), (100,534), 4)
			pygame.draw.line(screen, (255,255,255), (860,450), (860,534), 4)
			if loadpercentage <= 100 and loadpercentage > 0:
				pygame.draw.line(screen, (0,255,0), (100 + 0.5*loadlength,454), (100 + 0.5*loadlength,530), loadlength)
			if loadpercentage <= 150 and loadpercentage >= 100:
				pygame.draw.line(screen, (0,255,0), (480,454), (480,530), 760)
			pygame.draw.line(screen, (255,255,255), (480,450), (480,534), 4)
			if loadpercentage <= 150 and loadpercentage >= 100:
				screen.blit(pygame.font.SysFont('Times New Roman', 45).render("100", True, (0,0,0)), (480-32, 465))			
			if loadpercentage <= 100 and loadpercentage > 0:	
				screen.blit(pygame.font.SysFont('Times New Roman', 45).render("%d"%(loadpercentage), True, (0,0,0)), (100 + 0.5*loadlength -20, 465))
		pygame.display.update()
		for events in pygame.event.get():
			if events.type == pygame.KEYDOWN:	
				if events.key == pygame.K_ESCAPE:
					quit_game()
				elif events.key == pygame.K_SPACE and loadpercentage >= 150:
					gameseconds=0
					gametimer=0
					laser=0
					survivalscore = 0
					gamestate = 0
#=================================================================================================#
	if gamestate == 0:    #準備階段#
		screen.blit(background,(0,0))
		if mode == 3:
			if survivalscore > sur_1p_top5[5] and newhigh == 0:
				if survivalscore > sur_1p_top5[1] and newhigh == 0:
					sur_1p_top5.insert(1,survivalscore)
					breakrecord = 1
					newhigh = 1
				if survivalscore <= sur_1p_top5[1] and survivalscore > sur_1p_top5[2] and newhigh == 0:
					sur_1p_top5.insert(2,survivalscore)
					newhigh = 2
				if survivalscore <= sur_1p_top5[2] and survivalscore > sur_1p_top5[3] and newhigh == 0:
					sur_1p_top5.insert(3,survivalscore)
					newhigh = 3
				if survivalscore <= sur_1p_top5[3] and survivalscore > sur_1p_top5[4] and newhigh == 0:
					sur_1p_top5.insert(4,survivalscore)
					newhigh = 4
				if survivalscore <= sur_1p_top5[4] and survivalscore > sur_1p_top5[5] and newhigh == 0:
					sur_1p_top5.insert(5,survivalscore)
					newhigh = 5
				sur_1p_top5[:-1]
				f = open( 'sur_1p_highscore.txt' , 'r+')
				f.write("%d\n%d\n%d\n%d\n%d\n"%(sur_1p_top5[1],sur_1p_top5[2],sur_1p_top5[3],sur_1p_top5[4],sur_1p_top5[5]))
				f.close()	
		if mode == 4:
			if survivalscore > sur_2p_top5[5] and newhigh == 0:
				if survivalscore > sur_2p_top5[1]:
					sur_2p_top5.insert(1,survivalscore)
					breakrecord = 1
					newhigh = 1
				if survivalscore <= sur_2p_top5[1] and survivalscore > sur_2p_top5[2] and newhigh == 0:
					sur_2p_top5.insert(2,survivalscore)
					newhigh = 2
				if survivalscore <= sur_2p_top5[2] and survivalscore > sur_2p_top5[3] and newhigh == 0:
					sur_2p_top5.insert(3,survivalscore)
					newhigh = 3
				if survivalscore <= sur_2p_top5[3] and survivalscore > sur_2p_top5[4] and newhigh == 0:
					sur_2p_top5.insert(4,survivalscore)
					newhigh = 4
				if survivalscore <= sur_2p_top5[4] and survivalscore > sur_2p_top5[5] and newhigh == 0:
					sur_2p_top5.insert(5,survivalscore)
					newhigh = 5
				sur_2p_top5[:-1]
				f = open( 'sur_2p_highscore.txt' , 'r+')
				f.write("%d\n%d\n%d\n%d\n%d\n"%(sur_2p_top5[1],sur_2p_top5[2],sur_2p_top5[3],sur_2p_top5[4],sur_2p_top5[5]))
				f.close()
		if mode == 5:
			if catchscore > catch_1p_top5[5] and newhigh == 0:
				if catchscore > catch_1p_top5[1]:
					catch_1p_top5.insert(1,catchscore)
					breakrecord = 1
					newhigh = 1
				if catchscore <= catch_1p_top5[1] and catchscore > catch_1p_top5[2] and newhigh == 0:
					catch_1p_top5.insert(2,catchscore)
					newhigh = 2
				if catchscore <= catch_1p_top5[2] and catchscore > catch_1p_top5[3] and newhigh == 0:
					catch_1p_top5.insert(3,catchscore)
					newhigh = 3
				if catchscore <= catch_1p_top5[3] and catchscore > catch_1p_top5[4] and newhigh == 0:
					catch_1p_top5.insert(4,catchscore)
					newhigh = 4
				if catchscore <= catch_1p_top5[4] and catchscore > catch_1p_top5[5] and newhigh == 0:
					catch_1p_top5.insert(5,catchscore)
					newhigh = 5
				catch_1p_top5[:-1]
				f = open( 'catch_1p_highscore.txt' , 'r+')
				f.write("%d\n%d\n%d\n%d\n%d\n"%(catch_1p_top5[1],catch_1p_top5[2],catch_1p_top5[3],catch_1p_top5[4],catch_1p_top5[5]))
				f.close()	
		if mode == 6:
			if catchscore > catch_2p_top5[5] and newhigh == 0:
				if catchscore > catch_2p_top5[1]:
					catch_2p_top5.insert(1,catchscore)
					breakrecord = 1
					newhigh = 1
				if catchscore <= catch_2p_top5[1] and catchscore > catch_2p_top5[2] and newhigh == 0:
					catch_2p_top5.insert(2,catchscore)
					newhigh = 2
				if catchscore <= catch_2p_top5[2] and catchscore > catch_2p_top5[3] and newhigh == 0:
					catch_2p_top5.insert(3,catchscore)
					newhigh = 3
				if catchscore <= catch_2p_top5[3] and catchscore > catch_2p_top5[4] and newhigh == 0:
					catch_2p_top5.insert(4,catchscore)
					newhigh = 4
				if catchscore <= catch_2p_top5[4] and catchscore > catch_2p_top5[5] and newhigh == 0:
					catch_2p_top5.insert(5,catchscore)
					newhigh = 5
				catch_2p_top5[:-1]
				f = open( 'catch_2p_highscore.txt' , 'r+')
				f.write("%d\n%d\n%d\n%d\n%d\n"%(catch_2p_top5[1],catch_2p_top5[2],catch_2p_top5[3],catch_2p_top5[4],catch_2p_top5[5]))
				f.close()	
		if newhigh != 0:
			screen.blit(pygame.font.SysFont('Times New Roman', 50).render("Congratulation !!", True, (255, 255, 255)), (320, 130))
			if breakrecord == 0:
				screen.blit(pygame.font.SysFont('Times New Roman', 50).render("New high score !", True, (255, 255, 255)), (310, 200))
			if breakrecord == 1:	
				screen.blit(pygame.font.SysFont('Times New Roman', 50).render("You break the record!", True, (255, 255, 255)), (300, 200))
			
		if mode == 3 or mode == 4:
			ball_speedx,ball_speedy = 400,400
			bar_half_length = 40
			bar_speed = bar_basespeed
			bar2_speed = bar2_basespeed
		if timeout == 1 and timelimit%2 == 1:
			if mode == 2:
				screen.blit(pygame.font.SysFont('Times New Roman', 40).render("Timeout.", True, (255, 255, 255)), (400, 200))
			if mode == 1:
				screen.blit(pygame.font.SysFont('Times New Roman', 40).render("Timeout.", True, (255, 255, 255)), (400, 200))
		if score1 == winscore:
		    winner = "P1"
		elif score2 == winscore: 
		    winner = "P2"
		#------------------------TODO 3 start------------------------#
		laser = 0
		screen.blit(pygame.font.SysFont('Times New Roman', 30).render("Please press space to continue", True, (255, 255, 255)), (300, 400))
		if score1 == 0 and score2 == 0 and timeout == 0 and survivalscore == 0 and catchscore == 0:
			screen.blit(pygame.font.SysFont('Times New Roman', 50).render("New Game", True, (255, 255, 255)), (370, 150))
		if winner != "": 
			if mode == 2:
				screen.blit(pygame.font.SysFont('Times New Roman', 30).render("The winner is %s"%(winner), True, (255, 255, 255)), (300, 250)) #(x,y)#
				scorer=""
			if mode == 1:
				if winner == "P1":
					screen.blit(pygame.font.SysFont('Times New Roman', 30).render("You win !!", True, (255, 255, 255)), (400, 250))
					scorer=""
				if winner == "P2":
					screen.blit(pygame.font.SysFont('Times New Roman', 30).render("You Lose !!", True, (255, 255, 255)), (400, 250))
					scorer=""
		if mode == 1:
			screen.blit(pygame.font.SysFont('Times New Roman', 40).render("P1 : %d   VS   Com : %d"%(score1,score2), True, (255, 255, 255)), (320, 300))
		if mode == 2:
			screen.blit(pygame.font.SysFont('Times New Roman', 40).render("P1 : %d   VS   P2 : %d"%(score1,score2), True, (255, 255, 255)), (320, 300))
		if scorer != "":
			if mode == 1:
				if scorer == "P1":
					screen.blit(pygame.font.SysFont('Times New Roman', 30).render("You score !!", True, (255, 255, 255)), (400, 250))
				if scorer == "P2":
					screen.blit(pygame.font.SysFont('Times New Roman', 30).render("Com scores !!", True, (255, 255, 255)), (400, 250))
			if mode == 2:
				if timeout == 1:
					screen.blit(pygame.font.SysFont('Times New Roman', 30).render("It's even.", True, (255, 255, 255)), (410, 250))
				if timeout == 0:
					screen.blit(pygame.font.SysFont('Times New Roman', 30).render("%s scores !!"%(scorer), True, (255, 255, 255)), (400, 250))
		if (mode == 3 or mode == 4) and survivalscore != 0 :
			screen.blit(pygame.font.SysFont('Times New Roman', 40).render("You have survived for %d seconds."%(gametimer), True, (255, 255, 255)), (230, 300))
		if (mode == 5 or mode == 6) and catchscore != 0 :
			screen.blit(pygame.font.SysFont('Times New Roman', 40).render("Your score : %d"%(catchscore), True, (255, 255, 255)), (370, 300))
		#------------------------TODO 3 end--------------------------#
		for events in pygame.event.get():
			if events.type == pygame.KEYDOWN:	
				if events.key == pygame.K_ESCAPE:
					quit_game()
				elif events.key == pygame.K_SPACE:
					if (acceleration%2) == 1:
						accelboxy=screen_height*39/64*random.random()+100
					if wormhole%2 == 1:
						why1=screen_height*44/64*random.random()+100
						why2=screen_height*44/64*random.random()+100
					if mode == 4 or mode == 3 or mode == 5 or mode == 6:
						timelimit = 0
						ballsize = 3
						ball_r = 16
						ball2_r = 16
						ball3_r = 16
						ballnum = 1
						ballspeed = 4
						ball_speedx,ball_speedy = 300,300
						if mode == 5 or mode == 6:
							ball_speedx,ball_speedy = 350,350
							ball2_speedx,ball2_speedy = 349,349
							ball3_speedx,ball3_speedy = 348,348
						barlength = 3
						bar_half_length = 60
						barspeed = 2
						bar_speed = 1.8*bar_basespeed
						bar2_speed = 1.8*bar2_basespeed
						barfreemove = 0
						pmmodeon = 0
						pmmodeonmax = 0
						lasermode,acceleration,invisibility,ran_reflect,gravity,curve_ball,wormhole = 0,0,0,0,0,0,0
					ballx,bally=screen_width/2,screen_height/2
					ball2x,ball2y=screen_width/2,screen_height/2
					ball3x,ball3y=screen_width/2,screen_height/2
					bar_x1,bar_x2=barx,screen_width-barx
					bar_y2,bar_y1=screen_height/2,screen_height/2
					if mode == 4 or mode == 6:
						bar_x2 = barx + barx + bar_width
					if mode != 1 and mode != 2:
						ballx,bally = 900,320
					bar_diry2,bar_diry1=0,0
					bar_dirx2,bar_dirx1=0,0
					ran1 = 12*random.random()
					ran2 = 12*random.random()
					ran3 = 12*random.random()
					if mode == 1 or mode == 2:
						if ran1 >= 0 and ran1 < 1:
							ball_dirx,ball_diry=1.22,0.71
						elif ran1 >= 1 and ran1 < 2:
							ball_dirx,ball_diry=1,1						
						elif ran1 >= 2 and ran1 < 3:
							ball_dirx,ball_diry=1.13,0.85
						elif ran1 >= 3 and ran1 < 4:
							ball_dirx,ball_diry=-1.13,0.85
						elif ran1 >= 4 and ran1 < 5:
							ball_dirx,ball_diry=-1,1
						elif ran1 >= 5 and ran1 < 6:
							ball_dirx,ball_diry=-1.22,0.71
						elif ran1 >= 6 and ran1 < 7:
							ball_dirx,ball_diry=-1.22,-0.71
						elif ran1 >= 7 and ran1 < 8:
							ball_dirx,ball_diry=-1,-1
						elif ran1 >= 8 and ran1 < 9:
							ball_dirx,ball_diry=-1.13,-0.85
						elif ran1 >= 9 and ran1 < 10:
							ball_dirx,ball_diry=1.13,-0.85
						elif ran1 >= 10 and ran1 < 11:
							ball_dirx,ball_diry=1,-1
						elif ran1 >= 11 and ran1 <= 12:
							ball_dirx,ball_diry=1.22,-0.71
						if ran2 >= 0 and ran2 < 1:
							ball2_dirx,ball2_diry=1.22,0.71
						elif ran2 >= 1 and ran2 < 2:
							ball2_dirx,ball2_diry=1,1						
						elif ran2 >= 2 and ran2 < 3:
							ball2_dirx,ball2_diry=1.13,0.85
						elif ran2 >= 3 and ran2 < 4:
							ball2_dirx,ball2_diry=-1.13,0.85
						elif ran2 >= 4 and ran2 < 5:
							ball2_dirx,ball2_diry=-1,1
						elif ran2 >= 5 and ran2 < 6:
							ball2_dirx,ball2_diry=-1.22,0.71
						elif ran2 >= 6 and ran2 < 7:
							ball2_dirx,ball2_diry=-1.22,-0.71
						elif ran2 >= 7 and ran2 < 8:
							ball2_dirx,ball2_diry=-1,-1
						elif ran2 >= 8 and ran2 < 9:
							ball2_dirx,ball2_diry=-1.13,-0.85
						elif ran2 >= 9 and ran2 < 10:
							ball2_dirx,ball2_diry=1.13,-0.85
						elif ran2 >= 10 and ran2 < 11:
							ball2_dirx,ball2_diry=1,-1
						elif ran2 >= 11 and ran2 <= 12:
							ball2_dirx,ball2_diry=1.22,-0.71
						if ball_dirx * ball2_dirx >0:
							ball2_dirx = -ball2_dirx
					else:
						ball_dirx,ball_diry = 1,1
						ball2_dirx,ball2_diry = 1,-1
						ball3_dirx,ball3_diry = 1,1
					ball_speedx0 = ball_speedx
					ball_speedy0 = ball_speedy
					ball2_speedx0 = ball2_speedx
					ball2_speedy0 = ball2_speedy
					ball3_speedx0 = ball3_speedx
					ball3_speedy0 = ball3_speedy
					ball = 1
					ball2 = 0
					ball3 = 0
					ball2first = 0
					ball3first = 0
					accelball =0
					accelball2 =0
					accelball3 = 0
					scorer = ""
					timeout=0
					gameseconds=0
					gametimer=0
					laser=0
					survivalscore = 0
					grastatus = 0
					countdownseconds = 0
					countdowntimer=pygame.time.Clock()
					catchballscore = 1
					catchball2score = 1
					catchball3score = 1
					balldeadtime = 0
					ball2deadtime = 0
					ball3deadtime = 0
					pointchange = 0
					laserminus1 = 0
					laserminus2 = 0
					catchscore = 0
					if newhigh != 0:
						temptgamestate = gamestate
						gamestate = "highscore"
					else:
						if winner != "":
							set = 5
							gamestate ="setting_duel"
						else:
							gamestate="countdown"
					breakrecord = 0
				elif events.key == pygame.K_BACKSPACE:
					if mode == 3 or mode == 4:
						gamestate = "setting_survival"
					elif mode == 5 or mode == 6:
						gamestate = "setting_catch"
					else:
						gamestate = "setting_duel"
		pygame.display.update()
#=================================================================================================#
	if gamestate == 1: #Duel# #Survival#
		screen.blit(background,(0,0))
		screen.blit(top_margin,(0,0))
		for events in pygame.event.get():
			if events.type == pygame.QUIT:
				quit_game()
			#=============================鍵盤控制 BEGIN=============================#
			if events.type == pygame.KEYDOWN:
				if events.key == pygame.K_p:
					gamestate = "pause"
				if control%2 == 1:
					if events.key == pygame.K_w:
						bar_diry1=-1
					elif events.key == pygame.K_s:
						bar_diry1=1
					if mode == 2 or mode == 4:
						if events.key == pygame.K_UP:
							bar_diry2=-1
						elif events.key == pygame.K_DOWN:
							bar_diry2=1
					if barfreemove%2 == 1:
						if events.key == pygame.K_d:
							bar_dirx1=1
						elif events.key == pygame.K_a:
							bar_dirx1=-1
						if mode == 2:
							if events.key == pygame.K_RIGHT:
								bar_dirx2=1
							elif events.key == pygame.K_LEFT:
								bar_dirx2=-1
				if control%2 == 0:
					if events.key == pygame.K_UP:
						bar_diry1=-1
					elif events.key == pygame.K_DOWN:
						bar_diry1=1
					if mode == 2 or mode == 4:
						if events.key == pygame.K_w:
							bar_diry2=-1
						elif events.key == pygame.K_s:
							bar_diry2=1
					if barfreemove%2 == 1:
						if events.key == pygame.K_RIGHT:
							bar_dirx1=1
						elif events.key == pygame.K_LEFT:
							bar_dirx1=-1
						if mode == 2:
							if events.key == pygame.K_d:
								bar_dirx2=1
							elif events.key == pygame.K_a:
								bar_dirx2=-1
				if events.key == pygame.K_ESCAPE:
					quit_game()
				if events.key == pygame.K_BACKSPACE:
					if mode == 3 or mode == 4:
						gameseconds=0
						gametimer=0
						laser=0
						survivalscore = 0
						gamestate = "setting_survival"
					if mode == 1 or mode == 2:
						gamestate = "setting_duel"
			if events.type == pygame.KEYUP:
				if control%2 == 1:
					if events.key == pygame.K_w or events.key == pygame.K_s:
						bar_diry1=0
					if mode == 2 or mode == 4:
						if events.key == pygame.K_UP or events.key == pygame.K_DOWN:
							bar_diry2=0
					if barfreemove%2 == 1:
						if events.key == pygame.K_d or events.key == pygame.K_a:
							bar_dirx1=0
						if mode == 2 or mode == 4:
							if events.key == pygame.K_RIGHT or events.key == pygame.K_LEFT:
								bar_dirx2=0
				if control%2 == 0:
					if events.key == pygame.K_UP or events.key == pygame.K_DOWN:
						bar_diry1=0
					if mode == 2 or mode == 4:
						if events.key == pygame.K_w or events.key == pygame.K_s:
							bar_diry2=0						
					if barfreemove%2 == 1:		
						if events.key == pygame.K_RIGHT or events.key == pygame.K_LEFT:
							bar_dirx1=0
						if mode == 2 or mode == 4:
							if events.key == pygame.K_d or events.key == pygame.K_a:
								bar_dirx2=0
			#=============================鍵盤控制 END=============================#
		#=============================計算時間 BEGIN=============================#
		milli=clock.tick()
		seconds=milli/1000.0
		gamemilli=timer.tick()
		gameseconds+=gamemilli
		gametimer = int(gameseconds/1000)
		survivalscore = gametimer
		remaintime = ultitime - gametimer
		if remaintime == 0 and timelimit%2 == 1 and mode != 3 and mode != 4:
			timeout = 1
			if mode == 1:
				score1 += 1
				scorer = "P1"
			gamestate = 0
		#=============================計算時間 END=============================#
		#--------------------------Survival-----------------------------#
		if mode == 3 or mode == 4:
			ball_speedx += seconds*1
			ball_speedy += seconds*1
			if mode == 4:
				ball_speedx += seconds*1
				ball_speedy += seconds*1
			#ball_speedx0,ball_speedy0 = ball_speedx,ball_speedy
			pmmodeonmax = int((gameseconds - 15000)/30000) + 1
			if gameseconds%15000 >= 14980 :
				pmmodeon = 0
				lasermode,acceleration,invisibility,ran_reflect,gravity,curve_ball,wormhole = 0,0,0,0,0,0,0
			if pmmodeon < pmmodeonmax and gameseconds >= 15000 and gameseconds%15000 <= 1000:
				if gameseconds <= 60000:
					surmode_ran = 7*random.random()
				elif gameseconds > 60000:
					surmode_ran = 8*random.random()
				if surmode_ran >= 0 and surmode_ran < 1:
					lasermode = 1
				if surmode_ran >= 1 and surmode_ran < 2:
					acceleration = 1
					accelboxy=screen_height*39/64*random.random()+100
				if surmode_ran >= 2 and surmode_ran < 3:
					invisibility = 1
				if surmode_ran >= 3 and surmode_ran < 4:
					ran_reflect = 1
				if surmode_ran >= 4 and surmode_ran < 5:
					gravity = 1
				if surmode_ran >= 5 and surmode_ran < 6:
					curve_ball = 1
				if surmode_ran >= 6 and surmode_ran < 7:
					wormhole = 1
					why1=screen_height*44/64*random.random()+100
					why2=screen_height*44/64*random.random()+100
				pmmodeon += 1	
		#---------------------------------------------------------------#
		#=============================計算球和棒子的新位置 BEGIN=============================#
		#------------------------------Gravity---------------------------#
		if gravity%2 == 0:
			screen.blit(gra_50_dark,(505,5))
			screen.blit(control_down_dark,(555,5))
			if grastatus == 1:
				ball_speedx,ball_speedy = ball_speedx0,ball_speedy0
				ball2_speedx,ball2_speedy = ball2_speedx0,ball2_speedy0
				grastatus = 0
			else:
				grastatus = 0
			grastarttime = gameseconds
		if gravity%2 == 1:
			screen.blit(gra_50,(505,5))			
			if grastatus == 0:
				grastarttime = gameseconds
				ball_speedx0,ball_speedy0 = ball_speedx,ball_speedy
				ball2_speedx0,ball2_speedy0 = ball2_speedx,ball2_speedy
				grastatus = 1
			gracountdown = 5 - int((gameseconds - grastarttime)/1000)%5
			if grastatus == 1:	
				gra_ran = 6*random.random()
				grastatus = 2
			if gameseconds%5000 >= 4980:
				ball_speedx,ball_speedy = ball_speedx0,ball_speedy0
				ball2_speedx,ball2_speedy = ball2_speedx0,ball2_speedy0
				grastatus = 1
			if gra_ran >= 0 and gra_ran < 2:
				screen.blit(control_down,(555,5))
				if ball_diry>0:
					ball_speedy+=accelgra*seconds	
				elif ball_diry<0:
					ball_speedy-=accelgra*seconds
				if ballnum%2 == 0:
					if ball2_diry>0:
						ball2_speedy+=accelgra*seconds
					elif ball2_diry<0:
						ball2_speedy-=accelgra*seconds
			if gra_ran >= 2 and gra_ran < 4:
				screen.blit(control_up,(555,5))
				if ball_diry<0:
					ball_speedy+=accelgra*seconds	
				elif ball_diry>0:
					ball_speedy-=accelgra*seconds
				if ballnum%2 == 0:
					if ball2_diry<0:
						ball2_speedy+=accelgra*seconds
					elif ball2_diry>0:
						ball2_speedy-=accelgra*seconds
			if mode == 1 or mode == 2:
				if gra_ran >= 4 and gra_ran < 5:
					screen.blit(control_right,(555,5))
					if ball_dirx>0:
						ball_speedx+=accelgra*seconds	
					elif ball_dirx<0:
						ball_speedx-=accelgra*seconds
					if ballnum%2 == 0:
						if ball2_dirx>0:
							ball2_speedx+=accelgra*seconds
						elif ball2_dirx<0:
							ball2_speedx-=accelgra*seconds
				if gra_ran >= 5 and gra_ran <= 6:
					screen.blit(control_left,(550,5))
					if ball_dirx<0:
						ball_speedx+=accelgra*seconds	
					elif ball_dirx>0:
						ball_speedx-=accelgra*seconds
					if ballnum%2 == 0:
						if ball2_dirx<0:
							ball2_speedx+=accelgra*seconds
						elif ball2_dirx>0:
							ball2_speedx-=accelgra*seconds
			if mode == 3 or mode == 4:
				if gra_ran >= 4 and gra_ran <= 6:
					screen.blit(control_left,(550,5))
					if ball_dirx<0:
						ball_speedx+=accelgra*seconds	
					elif ball_dirx>0:
						ball_speedx-=accelgra*seconds
					if ballnum%2 == 0:
						if ball2_dirx<0:
							ball2_speedx+=accelgra*seconds
						elif ball2_dirx>0:
							ball2_speedx-=accelgra*seconds
			screen.blit(pygame.font.SysFont('Times New Roman', 40).render("%d"%(gracountdown), True, (250, 250, 250)), (517, 8))
			if ball_speedy < 0:
				grareversey1 = 1
			if grareversey1 == 1:
				ball_diry = -ball_diry
				ball_speedy = -ball_speedy
				grareversey1 = 0
			if ball2_speedy < 0:
				grareversey2 = 1
			if grareversey2 == 1:
				ball2_diry = -ball2_diry
				ball2_speedy = -ball2_speedy
				grareversey2 = 0
			if ball_speedx < 0:
				grareversex1 = 1
			if grareversex1 == 1:
				ball_dirx = -ball_dirx
				ball_speedx = -ball_speedx
				grareversex1 = 0
			if ball2_speedx < 0:
				grareversex2 = 1
			if grareversex2 == 1:
				ball2_dirx = -ball2_dirx
				ball2_speedx = -ball2_speedx
				grareversex2 = 0
		#----------------------------------------------------------------#
		ballx+=seconds*ball_dirx*ball_speedx
		bally+=seconds*ball_diry*ball_speedy
		if ballnum%2 == 0:
			ball2x+=seconds*ball2_dirx*ball2_speedx
			ball2y+=seconds*ball2_diry*ball2_speedy
		#-----------------------------球撞到左邊的邊緣時BEGIN---------------------------#
		if ballx<ball_r or (ball2x<ball_r and ballnum%2 == 0):
			ball_dirx=0
			ball2_dirx=0
			ball_speedx,ball_speedy = ball_speedx0,ball_speedy0
			ball2_speedx,ball2_speedy = ball2_speedx0,ball2_speedy0
			if (sound%2) == 1:
				sound2.play()
			if mode != 3 and mode != 4:
				score2+=1
				scorer = "P2"
			gamestate = 0
		#-----------------------------球撞到左邊的邊緣時END-----------------------------#
		#-----------------------------球撞到右邊的邊緣時BEGIN---------------------------#
		elif (ballx>screen_width-ball_r or (ball2x>screen_width-ball_r and ballnum%2 == 0)) and mode != 3 and mode != 4:
			ball_dirx=0
			ball2_dirx=0
			ball_speedx,ball_speedy = ball_speedx0,ball_speedy0
			ball2_speedx,ball2_speedy = ball2_speedx0,ball2_speedy0
			if (sound%2) == 1:
				sound2.play()
			score1+=1
			scorer = "P1"
			gamestate = 0
		if ran_reflect%2 == 1:
			screen.blit(bounce_50,(410,5))
		if ran_reflect%2 == 0:
			screen.blit(bounce_50_dark,(410,5))
		if (ballx>screen_width-ball_r) and (ball_dirx>0) and (mode == 3 or mode == 4):
			if ran_reflect%2 == 0:
				ball_dirx=-ball_dirx
			#------------------RANDOM_REFLECTION-----------------------------------#
			if ran_reflect%2 == 1:
				rrx1 = 6*random.random()
				if rrx1 >= 0 and rrx1 < 1:
					ball_dirx,ball_diry=-1.22,0.71
				elif rrx1 >= 1 and rrx1 < 2:
					ball_dirx,ball_diry=-1,1						
				elif rrx1 >= 2 and rrx1 < 3:
					ball_dirx,ball_diry=-1.13,0.85
				elif rrx1 >= 3 and rrx1 < 4:
					ball_dirx,ball_diry=-1.13,-0.85
				elif rrx1 >= 4 and rrx1 < 5:
					ball_dirx,ball_diry=-1,-1
				elif rrx1 >= 5 and rrx1 <= 6:
					ball_dirx,ball_diry=-1.22,-0.71
			#------------------RANDOM_REFLECTION-----------------------------------#
		#-----------------------------球撞到右邊的邊緣時END------------------------------#
		#-----------------------------球1撞到上方的邊緣時BEGIN---------------------------#
		if(bally<ball_r) and ball_diry < 0 :
			if ran_reflect%2 == 0:
				ball_diry=-ball_diry
			#------------------RANDOM_REFLECTION-----------------------------------#
			if ran_reflect%2 == 1:
				rrx1 = 6*random.random()
				if rrx1 >= 0 and rrx1 < 1:
					ball_dirx,ball_diry=1.22,0.71
				elif rrx1 >= 1 and rrx1 < 2:
					ball_dirx,ball_diry=1,1						
				elif rrx1 >= 2 and rrx1 < 3:
					ball_dirx,ball_diry=1.13,0.85
				elif rrx1 >= 3 and rrx1 < 4:
					ball_dirx,ball_diry=-1.13,0.85
				elif rrx1 >= 4 and rrx1 < 5:
					ball_dirx,ball_diry=-1,1
				elif rrx1 >= 5 and rrx1 <= 6:
					ball_dirx,ball_diry=-1.22,0.71
			#------------------RANDOM_REFLECTION-----------------------------------#
		#-----------------------------球1撞到上方的邊緣時END-----------------------------#
		#-----------------------------球1撞到下方的邊緣時BEGIN---------------------------#
		if(bally>=screen_height-ball_r)and (ball_diry > 0):
			if ran_reflect%2 == 0:
				ball_diry=-ball_diry
			#------------------RANDOM_REFLECTION-----------------------------------#
			if ran_reflect%2 == 1:
				rrx1 = 6*random.random()
				if rrx1 >= 0 and rrx1 < 1:
					ball_dirx,ball_diry=1.22,-0.71
				elif rrx1 >= 1 and rrx1 < 2:
					ball_dirx,ball_diry=1,-1						
				elif rrx1 >= 2 and rrx1 < 3:
					ball_dirx,ball_diry=1.13,-0.85
				elif rrx1 >= 3 and rrx1 < 4:
					ball_dirx,ball_diry=-1.13,-0.85
				elif rrx1 >= 4 and rrx1 < 5:
					ball_dirx,ball_diry=-1,-1
				elif rrx1 >= 5 and rrx1 <= 6:
					ball_dirx,ball_diry=-1.22,-0.71
			#------------------RANDOM_REFLECTION-----------------------------------#
		#-----------------------------球1撞到下方的邊緣時END-----------------------------#
		#-----------------------------球2撞到上方的邊緣時BEGIN---------------------------#
		if(ball2y<ball2_r)and ball2_diry < 0 :
			if ran_reflect%2 == 0:
				ball2_diry=-ball2_diry
			#------------------RANDOM_REFLECTION-----------------------------------#
			if ran_reflect%2 == 1:
				rrx2 = 6*random.random()
				if rrx2 >= 0 and rrx2 < 1:
					ball2_dirx,ball2_diry=1.22,0.71
				elif rrx2 >= 1 and rrx2 < 2:
					ball2_dirx,ball2_diry=1,1						
				elif rrx2 >= 2 and rrx2 < 3:
					ball2_dirx,ball2_diry=1.13,0.85
				elif rrx2 >= 3 and rrx2 < 4:
					ball2_dirx,ball2_diry=-1.13,0.85
				elif rrx2 >= 4 and rrx2 < 5:
					ball2_dirx,ball2_diry=-1,1
				elif rrx2 >= 5 and rrx2 <= 6:
					ball2_dirx,ball2_diry=-1.22,0.71
			#------------------RANDOM_REFLECTION-----------------------------------#
		#-----------------------------球2撞到上方的邊緣時END-----------------------------#
		#-----------------------------球2撞到下方的邊緣時BEGIN---------------------------#
		if(ball2y>=screen_height-ball2_r)and (ball2_diry > 0):
			if ran_reflect%2 == 0:
				ball2_diry=-ball2_diry
			#------------------RANDOM_REFLECTION-----------------------------------#
			if ran_reflect%2 == 1:
				rrx2 = 6*random.random()
				if rrx2 >= 0 and rrx2 < 1:
					ball2_dirx,ball2_diry=1.22,-0.71
				elif rrx2 >= 1 and rrx2 < 2:
					ball2_dirx,ball2_diry=1,-1						
				elif rrx2 >= 2 and rrx2 < 3:
					ball2_dirx,ball2_diry=1.13,-0.85
				elif rrx2 >= 3 and rrx2 < 4:
					ball2_dirx,ball2_diry=-1.13,-0.85
				elif rrx2 >= 4 and rrx2 < 5:
					ball2_dirx,ball2_diry=-1,-1
				elif rrx2 >= 5 and rrx2 <= 6:
					ball2_dirx,ball2_diry=-1.22,-0.71
			#------------------RANDOM_REFLECTION-----------------------------------#
		#-----------------------------球2撞到下方的邊緣時END-----------------------------#
		if((bar_diry1<0)and(bar_y1>bar_half_length))or((bar_diry1>0)and(bar_y1<screen_height-bar_half_length)):
			bar_y1+=seconds*bar_diry1*bar_speed
		if((bar_diry2<0)and(bar_y2>bar_half_length))or((bar_diry2>0)and(bar_y2<screen_height-bar_half_length)):
			bar_y2+=seconds*bar_diry2*bar2_speed
		if (barfreemove%2 == 1):
			if((bar_dirx1<0)and(bar_x1>barx))or((bar_dirx1>0)and(bar_x1<mid_width-barx)):
				bar_x1+=seconds*bar_dirx1*200
			if((bar_dirx2<0)and(bar_x2>mid_width+barx))or((bar_dirx2>0)and(bar_x2<screen_width-barx)):
				bar_x2+=seconds*bar_dirx2*200
		#-----------------------------球1撞到左方(右方)棒子時BEGIN-----------------------#
		if (ballx <= bar_x1+ball_r) and (ballx >= bar_x1-bar_width ) and (bally>=bar_y1-(bar_half_length+ball_r)) and (bally<=bar_y1+(bar_half_length+ball_r))and (ball_dirx<0):
			if accelball == 1:	
				accelball = 2
			if mode == 1 or mode == 2:
				ball_speedy+=(ball_diry*bar_diry1*bar_speed/10)
			#反彈時,球在y軸方向的速度會因棒子的移動而有所增減
			if ran_reflect%2 == 0:
				ball_dirx= -ball_dirx
			#------------------RANDOM_REFLECTION-----------------------------------#
			if ran_reflect%2 == 1:
				rrx1 = 6*random.random()
				if rrx1 >= 0 and rrx1 < 1:
					ball_dirx,ball_diry=1.22,-0.71
				elif rrx1 >= 1 and rrx1 < 2:
					ball_dirx,ball_diry=1,-1						
				elif rrx1 >= 2 and rrx1 < 3:
					ball_dirx,ball_diry=1.13,-0.85
				elif rrx1 >= 3 and rrx1 < 4:
					ball_dirx,ball_diry=1.13,0.85
				elif rrx1 >= 4 and rrx1 < 5:
					ball_dirx,ball_diry=1,1
				elif rrx1 >= 5 and rrx1 <= 6:
					ball_dirx,ball_diry=1.22,0.71
			#------------------RANDOM_REFLECTION-----------------------------------#
			if (sound%2) == 1:
				sound1.play()
		elif ((ballx >= bar_x2-ball_r) and (ballx <= bar_x2+bar_width) and (bally>=bar_y2-(bar_half_length+ball_r)) and (bally<=bar_y2+(bar_half_length+ball_r)) and (ball_dirx>0)) and (mode == 1 or mode == 2):
			if accelball == 1:	
				accelball = 2
			if mode == 1 or mode == 2:
				ball_speedy+=(ball_diry*bar_diry2*bar2_speed/10)
			#反彈時,球在y軸方向的速度會因棒子的移動而有所增減
			if ran_reflect%2 == 0:
				ball_dirx= -ball_dirx
			#------------------RANDOM_REFLECTION-----------------------------------#
			if ran_reflect%2 == 1:
				rrx1 = 6*random.random()
				if rrx1 >= 0 and rrx1 < 1:
					ball_dirx,ball_diry=-1.22,-0.71
				elif rrx1 >= 1 and rrx1 < 2:
					ball_dirx,ball_diry=-1,-1						
				elif rrx1 >= 2 and rrx1 < 3:
					ball_dirx,ball_diry=-1.13,-0.85
				elif rrx1 >= 3 and rrx1 < 4:
					ball_dirx,ball_diry=-1.13,0.85
				elif rrx1 >= 4 and rrx1 < 5:
					ball_dirx,ball_diry=-1,1
				elif rrx1 >= 5 and rrx1 <= 6:
					ball_dirx,ball_diry=-1.22,0.71
			#------------------RANDOM_REFLECTION-----------------------------------#
			if (sound%2) == 1:
				sound1.play()
		#--------------------------------Survival_2P----------------------------------------#
		elif ((ballx <= bar_x2+ball_r) and (ballx >= bar_x2-bar_width) and (bally>=bar_y2-(bar_half_length+ball_r)) and (bally<=bar_y2+(bar_half_length+ball_r)) and (ball_dirx<0)) and (mode == 4):
			if accelball == 1:	
				accelball = 2
			if ran_reflect%2 == 0:
				ball_dirx= -ball_dirx
			#------------------RANDOM_REFLECTION-----------------------------------#
			if ran_reflect%2 == 1:
				rrx1 = 6*random.random()
				if rrx1 >= 0 and rrx1 < 1:
					ball_dirx,ball_diry=1.22,-0.71
				elif rrx1 >= 1 and rrx1 < 2:
					ball_dirx,ball_diry=1,-1						
				elif rrx1 >= 2 and rrx1 < 3:
					ball_dirx,ball_diry=1.13,-0.85
				elif rrx1 >= 3 and rrx1 < 4:
					ball_dirx,ball_diry=1.13,0.85
				elif rrx1 >= 4 and rrx1 < 5:
					ball_dirx,ball_diry=1,1
				elif rrx1 >= 5 and rrx1 <= 6:
					ball_dirx,ball_diry=1.22,0.71
			#------------------RANDOM_REFLECTION-----------------------------------#
			if (sound%2) == 1:
				sound1.play()
		#-----------------------------球1撞到左方(右方)棒子時END-------------------------#
		#-----------------------------球2撞到左方(右方)棒子時BEGIN-----------------------#
		if (ball2x <= bar_x1+ball2_r) and (ball2x >= bar_x1-bar_width ) and (ball2y>=bar_y1-(bar_half_length+ball2_r)) and (ball2y<=bar_y1+(bar_half_length+ball2_r))and (ball2_dirx<0) and (mode == 1 or mode == 2) and ballnum%2 ==  0:
			if accelball2 == 1:	
				accelball2 = 2
			ball2_speedy+=(ball2_diry*bar_diry1*bar_speed/10)
			#反彈時,球在y軸方向的速度會因棒子的移動而有所增減
			if ran_reflect%2 == 0:
				ball2_dirx=-ball2_dirx
			#------------------RANDOM_REFLECTION-----------------------------------#
			if ran_reflect%2 == 1:
				rrx2 = 6*random.random()
				if rrx2 >= 0 and rrx2 < 1:
					ball2_dirx,ball2_diry=1.22,0.71
				elif rrx2 >= 1 and rrx2 < 2:
					ball2_dirx,ball2_diry=1,1						
				elif rrx2 >= 2 and rrx2 < 3:
					ball2_dirx,ball2_diry=1.13,0.85
				elif rrx2 >= 3 and rrx2 < 4:
					ball2_dirx,ball2_diry=1.13,-0.85
				elif rrx2 >= 4 and rrx2 < 5:
					ball2_dirx,ball2_diry=1,-1
				elif rrx2 >= 5 and rrx2 <= 6:
					ball2_dirx,ball2_diry=1.22,-0.71
			#------------------RANDOM_REFLECTION-----------------------------------#
			if (sound%2) == 1:
				sound1.play()
		elif ((ball2x >= bar_x2-ball2_r) and (ball2x <= bar_x2+bar_width) and (ball2y>=bar_y2-(bar_half_length+ball2_r)) and (ball2y<=bar_y2+(bar_half_length+ball2_r)) and (ball2_dirx>0) and (mode == 1 or mode == 2)and ballnum%2 ==  0):
			if accelball2 == 1:	
				accelball2 = 2
			ball2_speedy+=(ball2_diry*bar_diry2*bar_speed/10)
			#反彈時,球在y軸方向的速度會因棒子的移動而有所增減
			if ran_reflect%2 == 0:
				ball2_dirx=-ball2_dirx
			#------------------RANDOM_REFLECTION-----------------------------------#
			if ran_reflect%2 == 1:
				rrx2 = 6*random.random()
				if rrx2 >= 0 and rrx2 < 1:
					ball2_dirx,ball2_diry=-1.22,0.71
				elif rrx2 >= 1 and rrx2 < 2:
					ball2_dirx,ball2_diry=-1,1						
				elif rrx2 >= 2 and rrx2 < 3:
					ball2_dirx,ball2_diry=-1.13,0.85
				elif rrx2 >= 3 and rrx2 < 4:
					ball2_dirx,ball2_diry=-1.13,-0.85
				elif rrx2 >= 4 and rrx2 < 5:
					ball2_dirx,ball2_diry=-1,-1
				elif rrx2 >= 5 and rrx2 <= 6:
					ball2_dirx,ball2_diry=-1.22,-0.71
			#------------------RANDOM_REFLECTION-----------------------------------#
			if (sound%2) == 1:
				sound1.play()
		#-----------------------------球1撞到左方(右方)棒子時END-------------------------#
		#=============================計算球和棒子的新位置 END=============================#
		#-----------------------------One_Player_Computer--------------------------------#
		if mode == 1 and ballnum%2 == 0:
			if (ball_dirx > 0 and ball2_dirx > 0): 
				if ballx >= ball2x:
					if bar_y2 > bally:
						bar_diry2=-1
					if bar_y2 < bally:
						bar_diry2=1
				if ballx <= ball2x:
					if bar_y2 > ball2y:
						bar_diry2=-1
					if bar_y2 < ball2y:
						bar_diry2=1
			if (ball_dirx > 0 and ball2_dirx <= 0): 
				if bar_y2 > bally:
					bar_diry2=-1
				if bar_y2 < bally:
					bar_diry2=1
			if (ball_dirx <= 0 and ball2_dirx > 0):
				if bar_y2 > ball2y:
					bar_diry2=-1
				if bar_y2 < ball2y:
					bar_diry2=1
			if (ball_dirx <= 0 and ball2_dirx <= 0) or (invisibility%2 == 1 and ( ballx > 0.6*mid_width and ballx < 1.4*mid_width ) and accelball == 0 and ( ball2x > 0.6*mid_width or ball2x < 1.4*mid_width ) and accelball2 == 0):
				if bar_y2 > mid_height:
					bar_diry2=-1
				if bar_y2 < mid_height:
					bar_diry2=1
				if bar_y2 == mid_height:
					bar_diry2=0
		if mode == 1 and ballnum%2 == 1 :
			if ball_dirx > 0: 
				if bar_y2 > bally:
					bar_diry2=-1
				if bar_y2 < bally:
					bar_diry2=1
			if ball_dirx < 0 or ( invisibility%2 == 1 and ( ballx > 0.6*mid_width and ballx < 1.4*mid_width ) and accelball == 0):
				if bar_y2 > mid_height:
					bar_diry2=-1
				if bar_y2 < mid_height:
					bar_diry2=1
				if bar_y2 == mid_height:
					bar_diry2=0
		#-----------------------------One_Player_Computer--------------------------------#
		#===================================遊戲畫面BEGIN==================================#
		#---------------------------Laser------------------------------------#
		if lasermode%2 == 0:
			screen.blit(laser_50_dark,(245,5))
		if lasermode%2 == 1:
			screen.blit(laser_50,(245,5))
			if gametimer >= 2:
				if laser == 0:
					laserresttime = 0
					laserouttime = 0
					laser_ran = random.random()
					if laser_ran <= 0.5:
						laser_y = 200*random.random() + 80 #50-150   320  -490-590#
					if laser_ran > 0.5:
						laser_y = 200*fabs(random.random()-0.5) + 460
					lasertime = gameseconds
					laser = 1
				if laser == 1:
					pygame.draw.line(screen, (255,0,0), (480,laser_y), (480,laser_y+1), 960)
					lasercountdown = 3-int((gameseconds - lasertime)/1000)
					screen.blit(pygame.font.SysFont('Times New Roman', 40).render("%d"%(lasercountdown), True, (250, 250, 250)), (262, 8))
					if (gameseconds - lasertime) >= 3000:
						laserouttime = gameseconds
						laser = 2
				if laser == 2:
					lasertime = 0
					pygame.draw.line(screen, (255,0,0), (480,laser_y-20), (480,laser_y+20), 960)
					if (bar_y1 + bar_half_length >= laser_y - 20 and bar_y1 - bar_half_length <= laser_y - 20) or (bar_y1 - bar_half_length <= laser_y + 20 and bar_y1 + bar_half_length >= laser_y + 20):
						score2 += 1
						scorer = "P2"
						gamestate = 0
					if (bar_y2 + bar_half_length >= laser_y - 20 and bar_y2 - bar_half_length <= laser_y - 20) or (bar_y2 - bar_half_length <= laser_y + 20 and bar_y2 + bar_half_length >= laser_y + 20):
						if mode != 3:
							score1 += 1
							scorer = "P1"
							gamestate = 0
					if (gameseconds - laserouttime) >= 800:
						laserresttime = gameseconds
						laser = 3
				if laser == 3 and (gameseconds - laserresttime) >= 4000:
					laser = 0
		#-------------------------------------------------------------------#
		#---------------------------Acceleration----------------------------#
		if acceleration%2 == 0:
			accelball,accelball2 = 0,0
			screen.blit(accel_50_dark,(300,5))
		if acceleration%2 == 1:
			screen.blit(accel_50,(300,5))
			pygame.draw.line(screen, (255,255,0), (mid_width,accelboxy), (mid_width,accelboxy+100), 150)
			if acceldir == 1:
				pygame.draw.line(screen, (0,255,0), (mid_width+15-75,accelboxy+10), (mid_width+45-75,accelboxy+50), 10)
				pygame.draw.line(screen, (0,255,0), (mid_width+15-75,accelboxy+90), (mid_width+45-75,accelboxy+50), 10)
				pygame.draw.line(screen, (0,255,0), (mid_width+45-75,accelboxy+10), (mid_width+75-75,accelboxy+50), 10)
				pygame.draw.line(screen, (0,255,0), (mid_width+45-75,accelboxy+90), (mid_width+75-75,accelboxy+50), 10)
				pygame.draw.line(screen, (0,255,0), (mid_width+75-75,accelboxy+10), (mid_width+105-75,accelboxy+50), 10)
				pygame.draw.line(screen, (0,255,0), (mid_width+75-75,accelboxy+90), (mid_width+105-75,accelboxy+50), 10)
				pygame.draw.line(screen, (0,255,0), (mid_width+105-75,accelboxy+10), (mid_width+135-75,accelboxy+50), 10)
				pygame.draw.line(screen, (0,255,0), (mid_width+105-75,accelboxy+90), (mid_width+135-75,accelboxy+50), 10)
			if acceldir == -1:
				pygame.draw.line(screen, (0,255,0), (mid_width+45-75,accelboxy+10), (mid_width+15-75,accelboxy+50), 10)
				pygame.draw.line(screen, (0,255,0), (mid_width+45-75,accelboxy+90), (mid_width+15-75,accelboxy+50), 10)
				pygame.draw.line(screen, (0,255,0), (mid_width+75-75,accelboxy+10), (mid_width+45-75,accelboxy+50), 10)
				pygame.draw.line(screen, (0,255,0), (mid_width+75-75,accelboxy+90), (mid_width+45-75,accelboxy+50), 10)
				pygame.draw.line(screen, (0,255,0), (mid_width+105-75,accelboxy+10), (mid_width+75-75,accelboxy+50), 10)
				pygame.draw.line(screen, (0,255,0), (mid_width+105-75,accelboxy+90), (mid_width+75-75,accelboxy+50), 10)
				pygame.draw.line(screen, (0,255,0), (mid_width+135-75,accelboxy+10), (mid_width+105-75,accelboxy+50), 10)
				pygame.draw.line(screen, (0,255,0), (mid_width+135-75,accelboxy+90), (mid_width+105-75,accelboxy+50), 10)
			if ballx <= mid_width+75  and ballx >= mid_width-75 and bally>=accelboxy and bally<= accelboxy+100 and accelball == 0:
				ball_speedx0 = ball_speedx
				ball_speedy0 = ball_speedy
				ball_speedx,ball_speedy = ball_speedx*accelballspeed,ball_speedy*accelballspeed
				accelboxy=screen_height*39/64*random.random()+100
				if ball_dirx > 0:
					acceldir = 1
				if ball_dirx < 0:
					acceldir = -1
				accelball = 1
			if accelball == 2:
				ball_speedx,ball_speedy = ball_speedx0,ball_speedy0
				accelball = 0
			if ball2x <= mid_width+75  and ball2x >= mid_width-75 and ball2y>=accelboxy and ball2y<= accelboxy+100 and accelball2 == 0:
				ball2_speedx0 = ball2_speedx
				ball2_speedy0 = ball2_speedy
				ball2_speedx,ball2_speedy = ball2_speedx*accelballspeed,ball2_speedy*accelballspeed
				accelboxy=screen_height*39/64*random.random()+100
				if ball2_dirx > 0:
					acceldir = 1
				if ball2_dirx < 0:
					acceldir = -1
				accelball2 = 1
			if accelball2 == 2:
				ball2_speedx,ball2_speedy = ball2_speedx0,ball2_speedy0
				accelball2 = 0
			if (invisibility%2 == 0) or ( invisibility%2 == 1 and  ((ballx < 0.6*mid_width or ballx > 1.4*mid_width) or (ballx > 0.99*mid_width and ballx < 1.01*mid_width) or accelball == 1)):
				if accelball == 1:
					pygame.draw.circle(screen, (204,0,204), (int(ballx),int(bally)), ball_r,0)
				if accelball == 0:
					pygame.draw.circle(screen, (204,255,255), (int(ballx),int(bally)), ball_r,0)
			if (invisibility%2 == 0) or ( invisibility%2 == 1 and  ((ball2x < 0.6*mid_width or ball2x > 1.4*mid_width) or (ball2x > 0.99*mid_width and ball2x < 1.01*mid_width) or accelball2 == 1)):
				if accelball2 == 1 and ballnum%2 == 0:
					pygame.draw.circle(screen, (255,153,0), (int(ball2x),int(ball2y)), ball2_r,0)			
				if accelball2 == 0 and ballnum%2 == 0:
					pygame.draw.circle(screen, (255,153,153), (int(ball2x),int(ball2y)), ball2_r,0)
		#-------------------------------------------------------------------#
		#---------------------------Curve_Ball------------------------------#
		if curve_ball%2 == 0:
			screen.blit(vibrate_50_dark,(610,5))
		if curve_ball%2 == 1:
			screen.blit(vibrate_50,(610,5))
			if (gameseconds)%200 <= 5 and curve == 0:
				ball_diry = -ball_diry
				ball2_diry = -ball2_diry
				curve = 1
			if (gameseconds)%200 >= 50 and (gameseconds)%200 <= 60:
				curve = 0
		#-------------------------------------------------------------------#
		#---------------------------Wormhole--------------------------------#
		if wormhole%2 == 0:
			screen.blit(wh_50_dark,(665,5))
		if wormhole%2 == 1:
			screen.blit(wh_50,(665,5))
			pygame.draw.circle(screen, (30,30,30), (int(0.5*mid_width),int(why1)), 50,0)
			screen.blit(blackhole_70,(int(0.5*mid_width)-35,int(why1)-35))
			pygame.draw.circle(screen, (30,30,30), (int(1.5*mid_width),int(why2)), 50,0)
			screen.blit(blackhole_70,(int(1.5*mid_width)-35,int(why2)-35))
			disblwh1 = (ballx-int(0.5*mid_width))*(ballx-int(0.5*mid_width)) + (bally-int(why1))*(bally-int(why1))
			disblwh2 = (ballx-int(1.5*mid_width))*(ballx-int(1.5*mid_width)) + (bally-int(why2))*(bally-int(why2))
			disbl2wh1 = (ball2x-int(0.5*mid_width))*(ball2x-int(0.5*mid_width)) + (ball2y-int(why1))*(ball2y-int(why1))
			disbl2wh2 = (ball2x-int(1.5*mid_width))*(ball2x-int(1.5*mid_width)) + (ball2y-int(why2))*(ball2y-int(why2))
			if disblwh2 > 2500 and disblwh1 > 2500:
				blwh = 0
			if disblwh1 <= 2500 and blwh == 0:
				why2=screen_height*44/64*random.random()+100
				ballx,bally = int(1.5*mid_width),int(why2)
				blwh = 1
			if disblwh2 <= 2500 and blwh == 0:
				why1=screen_height*44/64*random.random()+100
				ballx,bally = int(0.5*mid_width),int(why1)
				blwh = 1
			if disbl2wh2 > 2500 and disbl2wh1 > 2500:
				bl2wh = 0
			if disbl2wh1 <= 2500 and bl2wh == 0:
				why2=screen_height*44/64*random.random()+100
				ball2x,ball2y = int(1.5*mid_width),int(why2)
				bl2wh = 1
			if disbl2wh2 <= 2500 and bl2wh == 0:
				why1=screen_height*44/64*random.random()+100
				ball2x,ball2y = int(0.5*mid_width),int(why1)
				bl2wh = 1
		#-------------------------------------------------------------------#
		#---------------------------Invisibility1---------------------------#
		if invisibility%2 == 0:
			screen.blit(invis_50_dark,(355,5))
		if invisibility%2 == 1:
			screen.blit(invis_50,(355,5))
			pygame.draw.line(screen, (200,200,200), (0.6*mid_width,60), (0.6*mid_width,640), 1)
			pygame.draw.line(screen, (200,200,200), (1.4*mid_width,60), (1.4*mid_width,640), 1)
		#-------------------------------------------------------------------#
		pygame.draw.line(screen, (171,171,171), (480,60), (480,61), 960)
		if timelimit%2 == 1 and mode != 4 and mode != 3:
			screen.blit(pygame.font.SysFont('Times New Roman', 20).render("%d"%(remaintime), True, (255, 255, 255)), (467, 10))
		if mode == 1 or mode == 2:
			screen.blit(pygame.font.SysFont('Times New Roman', 30).render("P1", True, (51, 153, 255)), (15, 10))
		if mode == 1:
			screen.blit(pygame.font.SysFont('Times New Roman', 30).render("Com", True, (102, 255, 51)), (880,10))	
		if mode == 2:
			screen.blit(pygame.font.SysFont('Times New Roman', 30).render("P2", True, (255, 102, 153)), (905,10))	
		pygame.draw.line(screen, (0,0,255), (bar_x1,bar_y1-bar_half_length), (bar_x1,bar_y1+bar_half_length), bar_width)
		if mode == 1:
			pygame.draw.line(screen, (0,255,0), (bar_x2,bar_y2-bar_half_length), (bar_x2,bar_y2+bar_half_length), bar_width)
		if mode == 2 or mode == 4: 
			pygame.draw.line(screen, (255,0,0), (bar_x2,bar_y2-bar_half_length), (bar_x2,bar_y2+bar_half_length), bar_width)	
		#---------------------------Invisibility2----------------------------#
		if (invisibility%2 == 0) or ( invisibility%2 == 1 and  ((ballx < 0.6*mid_width or ballx > 1.4*mid_width) or (ballx > 0.99*mid_width and ballx < 1.01*mid_width) )):
			if accelball == 0 :
				pygame.draw.circle(screen, (204,255,255), (int(ballx),int(bally)), ball_r,0)
		if (invisibility%2 == 0) or ( invisibility%2 == 1 and  ((ball2x < 0.6*mid_width or ball2x > 1.4*mid_width) or (ball2x > 0.99*mid_width and ball2x < 1.01*mid_width) )):
			if accelball2 == 0 and ballnum%2 == 0:
				pygame.draw.circle(screen, (255,153,153), (int(ball2x),int(ball2y)), ball2_r,0)			
		#-------------------------------------------------------------------#
		if mode == 3 or mode == 4:
			screen.blit(pygame.font.SysFont('Times New Roman', 35).render("Score : %d"%(gametimer), True, (255, 255, 255)), (750,10))
		#-------------testing----------------#	
		#screen.blit(pygame.font.SysFont('Times New Roman', 30).render("%d"%(pmmodeon), True, (255, 0, 0)), (300,200))	
		#screen.blit(pygame.font.SysFont('Times New Roman', 30).render("%d"%(pmmodeonmax), True, (255, 0, 0)), (300,300))	
		pygame.display.update()
		#===================================遊戲畫面END====================================#
#=================================================================================================#
	if gamestate == "setting_ball":
		screen.blit(background,(0,0))	
		bl1,bl2,bl3,bl4,bl5 = 40,40,40,30,30		
		if sbl == 1:
			bl1 = 50
			optballcircley =145
			screen.blit(exhibit_bls,(550,300))
			pygame.draw.circle(screen, (204,255,255), (730,450),ball_r,0)
			drawlefttri(340,150,20,15)
			drawrighttri(540,150,20,15)
		elif sbl == 2:
			bl2 = 50
			optballcircley =205
			screen.blit(exhibit_bls,(550,300))
			if (ballnum%2) == 1:
				pygame.draw.circle(screen, (204,255,255), (730,450),16,0)
			elif (ballnum%2) == 0:
				pygame.draw.circle(screen, (204,255,255), (680,450),16,0)
				pygame.draw.circle(screen, (255,153,153), (780,450),16,0)
			drawlefttri(340,210,20,15)
			drawrighttri(440,210,20,15)
		elif sbl == 3:
			bl3 = 50
			optballcircley =265
			screen.blit(exhibit_bls,(550,300))
			blspeedtime += blspeedtimer.tick()
			blspeedexhibitx = ball_speedx*blspeedtime/1000
			pygame.draw.circle(screen, (204,255,255), (int(blspeedexhibitx)%324 + 566,450),16,0)
			#screen.blit(pygame.font.SysFont('Times New Roman', 30).render("%d"%(blspeedtime), True, (255, 255, 255)), (80, 120))
			drawlefttri(340,270,20,15)
			if (ballspeed%7) != 1 and (ballspeed%7) != 0:
				drawrighttri(510,270,20,15)
		elif sbl == 4:
			bl4 = 40
			optballcircley =525	
		elif sbl == 5:
			bl5 = 40
			optballcircley =585
		screen.blit(pygame.font.SysFont('Times New Roman', 80).render("Setting_Ball", True, (171,171,171)), (30, 15))
		screen.blit(pygame.font.SysFont('Times New Roman', bl1).render("Size", True, (255, 255, 255)), (80, 120))
		screen.blit(pygame.font.SysFont('Times New Roman', bl2).render("Number", True, (255, 255, 255)), (80, 180))
		screen.blit(pygame.font.SysFont('Times New Roman', bl3).render("Speed", True, (255, 255, 255)), (80, 240))
		screen.blit(pygame.font.SysFont('Times New Roman', bl4).render("Reset", True, (255, 255, 255)), (80, 500))
		screen.blit(pygame.font.SysFont('Times New Roman', bl5).render("Confirm", True, (255, 255, 255)), (80, 560))
		pygame.draw.circle(screen, (255,255,255), (60,optballcircley),6,0)
		#-------------------------------------------球的大小------------------------------------------------------#
		if (ballsize%6) == 1:
			screen.blit(pygame.font.SysFont('Times New Roman', bl1-5).render("Tiny", True, (255, 255, 255)), (350, 125))
			ball_r,ball2_r = 1,1
		elif (ballsize%6) == 2:
			screen.blit(pygame.font.SysFont('Times New Roman', bl1-5).render("Small", True, (255, 255, 255)), (350, 125))
			ball_r,ball2_r = 8,8
		elif (ballsize%6) == 3:
			screen.blit(pygame.font.SysFont('Times New Roman', bl1-5).render("Medium", True, (255, 255, 255)), (350, 125))
			ball_r,ball2_r = 16,16
		elif (ballsize%6) == 4:
			screen.blit(pygame.font.SysFont('Times New Roman', bl1-5).render("Big", True, (255, 255, 255)), (350, 125))
			ball_r,ball2_r = 32,32
		elif (ballsize%6) == 5:
			screen.blit(pygame.font.SysFont('Times New Roman', bl1-5).render("Large", True, (255, 255, 255)), (350, 125))
			ball_r,ball2_r = 64,64
		elif (ballsize%6) == 0:
			screen.blit(pygame.font.SysFont('Times New Roman', bl1-5).render("Enormous", True, (255, 255, 255)), (350, 125))
			ball_r,ball2_r = 128,128
		#---------------------------------------------------------------------------------------------------------#
		#-------------------------------------------球的數量------------------------------------------------------#
		if (ballnum%2) == 1:
			screen.blit(pygame.font.SysFont('Times New Roman', bl2-5).render("One", True, (255, 255, 255)), (350, 185))
		elif (ballnum%2) == 0:
			screen.blit(pygame.font.SysFont('Times New Roman', bl2-5).render("Two", True, (255, 255, 255)), (350, 185))
		#---------------------------------------------------------------------------------------------------------#
		#-------------------------------------------球的速度------------------------------------------------------#
		if (ballspeed%7) == 1:
			screen.blit(pygame.font.SysFont('Times New Roman', bl3-5).render("It will take forever", True, (255, 255, 255)), (350, 245))
			ball_speedx,ball_speedy=0,0
			ball2_speedx,ball2_speedy=0,0
			if sbl == 3:
				drawrighttri(725,270,20,15)
		elif (ballspeed%7) == 2:
			screen.blit(pygame.font.SysFont('Times New Roman', bl3-5).render("Snail", True, (255, 255, 255)), (350, 245))
			ball_speedx,ball_speedy = 0.25*ball_basespeedx,0.25*ball_basespeedy
			ball2_speedx,ball2_speedy = 0.25*ball2_basespeedx,0.25*ball2_basespeedy
		elif (ballspeed%7) == 3:
			screen.blit(pygame.font.SysFont('Times New Roman', bl3-5).render("Slow", True, (255, 255, 255)), (350, 245))
			ball_speedx,ball_speedy = 0.5*ball_basespeedx,0.5*ball_basespeedy
			ball2_speedx,ball2_speedy = 0.5*ball2_basespeedx,0.5*ball2_basespeedy
		elif (ballspeed%7) == 4:
			screen.blit(pygame.font.SysFont('Times New Roman', bl3-5).render("Normal", True, (255, 255, 255)), (350, 245))
			ball_speedx,ball_speedy = ball_basespeedx,ball_basespeedy
			ball2_speedx,ball2_speedy = ball2_basespeedx,ball2_basespeedy
		elif (ballspeed%7) == 5:
			screen.blit(pygame.font.SysFont('Times New Roman', bl3-5).render("Fast", True, (255, 255, 255)), (350, 245))
			ball_speedx,ball_speedy = 2*ball_basespeedx,2*ball_basespeedy
			ball2_speedx,ball2_speedy = 2*ball2_basespeedx,2*ball2_basespeedy
		elif (ballspeed%7) == 6:
			screen.blit(pygame.font.SysFont('Times New Roman', bl3-5).render("Bullet", True, (255, 255, 255)), (350, 245))
			ball_speedx,ball_speedy=1200,1200
			ball2_speedx,ball2_speedy=1199,1199
		elif (ballspeed%7) == 0:
			screen.blit(pygame.font.SysFont('Times New Roman', bl3-5).render("What Happened !?", True, (255, 255, 255)), (350, 245))
			ball_speedx,ball_speedy=100000,100000
			ball2_speedx,ball2_speedy=99999,99999
			if sbl == 3:
				drawrighttri(700,270,20,15)
		#---------------------------------------------------------------------------------------------------------#
		pygame.display.update()
		for events in pygame.event.get():
			if events.type == pygame.KEYDOWN:	
				if events.key == pygame.K_ESCAPE:
					quit_game()
				elif events.key == pygame.K_SPACE:
					if sbl==4:
						ballsize = 3
						ballnum = 1
						ballspeed = 4
						sbl=5
					elif sbl==5:
						set=5
						gamestate = "setting_duel"
				elif events.key == pygame.K_d or events.key == pygame.K_RIGHT:
					if sbl==1:
						ballsize += 1
					elif sbl==2:
						ballnum += 1
					elif sbl==3:
						ballspeed += 1
				elif events.key == pygame.K_a or events.key == pygame.K_LEFT:
					if sbl==1:
						ballsize -= 1
					elif sbl==2:
						ballnum -= 1
					elif sbl==3:
						ballspeed -= 1
				elif events.key == pygame.K_BACKSPACE:
					gamestate = "setting_duel"
				elif events.key == pygame.K_TAB or events.key == pygame.K_s or events.key == pygame.K_DOWN:
					sbl +=1
					if sbl == 6:
						sbl = 1
				elif events.key == pygame.K_w or events.key == pygame.K_UP :
					sbl -=1
					if sbl == 0:
						sbl = 5
#=================================================================================================#
	if gamestate == "setting_bar":
		screen.blit(background,(0,0))
		br1,br2,br3,br4,br5 = 40,40,40,30,30
		#screen.blit(exhibit_brs,(640,0))
		#screen.blit(pygame.font.SysFont('Times New Roman', br1).render("%d"%(brspeedtime), True, (255, 255, 255)), (80, 120))		
		if sbr == 1:
			br1 = 50
			setbarcircley =145
			screen.blit(exhibit_brs,(640,0))
			pygame.draw.line(screen, (0,0,255), (772,320-bar_half_length), (772,320+bar_half_length), bar_width)
			drawlefttri(370,150,20,15)
			if (barlength%5) != 0:
				drawrighttri(550,150,20,15)
		elif sbr == 2:
			br2 = 50
			setbarcircley =205
			screen.blit(exhibit_brs,(640,0))
			brspeedmilli = brspeedtimer.tick()
			brspeedtime += brspeedmilli
			brspeedexhibity += (bar_speed*brspeedmilli/1000)
			pygame.draw.line(screen, (0,0,255), (772,int(brspeedexhibity)%560+40-40), (772,int(brspeedexhibity)%560+40+40), bar_width)
			drawlefttri(370,210,20,15)
			drawrighttri(550,210,20,15)
		elif sbr == 3:
			br3 = 50
			setbarcircley =265
			screen.blit(exhibit_brs,(640,0))
			drawlefttri(370,270,20,15)
			drawrighttri(470,270,20,15)
			brspeedmilli = brspeedtimer.tick()
			brspeedtime += brspeedmilli
			brspeedexhibity += (200*brspeedmilli*bar_exhibitdiry/1000)
			brspeedexhibitx += (100*brspeedmilli*bar_exhibitdirx/1000)
			if barfreemove%2 == 0:
				if brspeedexhibity > 560:
					brspeedexhibitx,brspeedexhibity = 772,320
					bar_exhibitdiry = -1
				if brspeedexhibity < 80:
					brspeedexhibitx,brspeedexhibity = 772,320
					bar_exhibitdiry = 1
				pygame.draw.line(screen, (0,0,255), (772,int(brspeedexhibity)-40), (772,int(brspeedexhibity)+40), bar_width)
			#if barfreemove%2 == 0:
				#screen.blit(control_w,(640,0))
				#screen.blit(control_w,(640,0))
				#screen.blit(control_w,(640,0))
				#screen.blit(control_w,(640,0))
				#pygame.draw.line(screen, (0,0,255), (772,int(brspeedexhibity)%264+170+40-40), (772,int(brspeedexhibity)%264+170+40+40), bar_width)
			if barfreemove%2 == 1 :
				if brspeedexhibity > 520:
					brspeedexhibitx,brspeedexhibity = 772,320
					bar_exhibitdirx = 0
					bar_exhibitdiry = -1
				if brspeedexhibity < 120:
					brspeedexhibitx,brspeedexhibity = 772,320
					bar_exhibitdirx = -1
					bar_exhibitdiry = 0
				if brspeedexhibitx > 900:
					brspeedexhibitx,brspeedexhibity = 772,320
					bar_exhibitdirx = 0
					bar_exhibitdiry = 1
				if brspeedexhibitx < 650:
					brspeedexhibitx,brspeedexhibity = 772,320
					bar_exhibitdirx = 1
					bar_exhibitdiry = 0
				pygame.draw.line(screen, (0,0,255), (int(brspeedexhibitx),int(brspeedexhibity)-40), (int(brspeedexhibitx),int(brspeedexhibity)+40), bar_width)
			if bar_exhibitdiry == -1:
				screen.blit(control_w,(750,int(brspeedexhibity)-100))
			if bar_exhibitdiry == 1:
				screen.blit(control_s,(750,int(brspeedexhibity)+50))
			if bar_exhibitdirx == -1:
				screen.blit(control_a,(int(brspeedexhibitx)-65,295))
			if bar_exhibitdirx == 1:
				screen.blit(control_d,(int(brspeedexhibitx)+15,295))
		elif sbr == 4:
			br4 = 40
			setbarcircley =525	
		elif sbr == 5:
			br5 = 40
			setbarcircley =585
		screen.blit(pygame.font.SysFont('Times New Roman', 80).render("Setting_Bar", True, (171,171,171)), (30,15))
		screen.blit(pygame.font.SysFont('Times New Roman', br1).render("Length", True, (255, 255, 255)), (80, 120))
		screen.blit(pygame.font.SysFont('Times New Roman', br2).render("Speed", True, (255, 255, 255)), (80, 180))
		screen.blit(pygame.font.SysFont('Times New Roman', br3).render("Free_Move", True, (255, 255, 255)), (80, 240))
		screen.blit(pygame.font.SysFont('Times New Roman', br4).render("Reset", True, (255, 255, 255)), (80, 500))
		screen.blit(pygame.font.SysFont('Times New Roman', br5).render("Confirm", True, (255, 255, 255)), (80, 560))
		pygame.draw.circle(screen, (255,255,255), (60,setbarcircley),6,0)
		#-------------------------------------------BAR長度------------------------------------------------------#
		if (barlength%5) == 1:
			screen.blit(pygame.font.SysFont('Times New Roman', br1-5).render("Lucky ?", True, (255, 255, 255)), (380, 125))
			bar_half_length=2
		elif (barlength%5) == 2:
			screen.blit(pygame.font.SysFont('Times New Roman', br1-5).render("Short", True, (255, 255, 255)), (380, 125))
			bar_half_length=20
		elif (barlength%5) == 3:
			screen.blit(pygame.font.SysFont('Times New Roman', br1-5).render("Medium", True, (255, 255, 255)), (380, 125))
			bar_half_length=40
		elif (barlength%5) == 4:
			screen.blit(pygame.font.SysFont('Times New Roman', br1-5).render("Long", True, (255, 255, 255)), (380, 125))
			bar_half_length=80
		elif (barlength%5) == 0:
			screen.blit(pygame.font.SysFont('Times New Roman', br1-5).render("Like a boss", True, (255, 255, 255)), (380, 125))
			bar_half_length=320
			if sbr == 1:
				drawrighttri(605,150,20,15)
		#---------------------------------------------------------------------------------------------------------#
		#-------------------------------------------BAR速度------------------------------------------------------#
		if (barspeed%4) == 1:
			screen.blit(pygame.font.SysFont('Times New Roman', br2-5).render("Slow", True, (255, 255, 255)), (380, 185))
			bar_speed = 0.5*bar_basespeed
			if mode == 2:
				bar2_speed = 0.5*bar2_basespeed
		elif (barspeed%4) == 2:
			screen.blit(pygame.font.SysFont('Times New Roman', br2-5).render("Medium", True, (255, 255, 255)), (380, 185))
			bar_speed = bar_basespeed
			if mode == 2:
				bar2_speed = bar2_basespeed
		elif (barspeed%4) == 3:
			screen.blit(pygame.font.SysFont('Times New Roman', br2-5).render("Fast", True, (255, 255, 255)), (380, 185))
			bar_speed = 2*bar_basespeed
			if mode == 2:
				bar2_speed = 2*bar2_basespeed
		elif (barspeed%4) == 0:
			screen.blit(pygame.font.SysFont('Times New Roman', br2-5).render("Extreme", True, (255, 255, 255)), (380, 185))
			bar_speed=10000
			if mode == 2:
				bar2_speed=10000
		#---------------------------------------------------------------------------------------------------------#
		#-------------------------------------------BAR自由運動------------------------------------------------------#
		if (barfreemove%2) == 0:
			screen.blit(pygame.font.SysFont('Times New Roman', br3-5).render("Off", True, (255, 255, 255)), (380, 245))
		elif (barfreemove%2) == 1:
			screen.blit(pygame.font.SysFont('Times New Roman', br3-5).render("On", True, (255, 255, 255)), (380, 245))
		#---------------------------------------------------------------------------------------------------------#
		pygame.display.update()
		for events in pygame.event.get():
			if events.type == pygame.KEYDOWN:	
				if events.key == pygame.K_ESCAPE:
					quit_game()
				elif events.key == pygame.K_SPACE:
					if sbr==4:
						barlength = 3
						barspeed = 2
						barfreemove = 0
						sbr=5
					elif sbr==5:
						set=5
						gamestate = "setting_duel"
				elif events.key == pygame.K_d or events.key == pygame.K_RIGHT:
					if sbr==1:
						barlength +=1
					elif sbr==2:
						barspeed +=1
					elif sbr==3:
						barfreemove +=1
				elif events.key == pygame.K_a or events.key == pygame.K_LEFT:
					if sbr==1:
						barlength -=1
					elif sbr==2:
						barspeed -=1
					elif sbr==3:
						barfreemove -=1
				elif events.key == pygame.K_BACKSPACE:
					gamestate = "setting_duel"
				elif events.key == pygame.K_TAB or events.key == pygame.K_s or events.key == pygame.K_DOWN:
					sbr +=1
					if sbr == 6:
						sbr = 1
				elif events.key == pygame.K_w or events.key == pygame.K_UP :
					sbr -=1	
					if sbr == 0:
						sbr = 5
#=================================================================================================#
	if gamestate == "setting_others":
		screen.blit(background,(0,0))
		g1,g2,g3,g4,g5 = 40,40,40,30,30
		if sg == 1:
			g1 = 50
			setbarcircley =145
			drawlefttri(430,150,20,15)
			drawrighttri(510,150,20,15)
		elif sg == 2:
			g2 = 50
			setbarcircley =205
			drawlefttri(430,210,20,15)
			drawrighttri(530,210,20,15)
		elif sg == 3:
			g3 = 50
			setbarcircley =265
			drawlefttri(340,310,30,80)
			drawrighttri(545,310,30,80)
		elif sg == 4:
			g4 = 40
			setbarcircley =525
		elif sg == 5:
			g5 = 40
			setbarcircley =585
		screen.blit(pygame.font.SysFont('Times New Roman', 80).render("Setting_Others", True, (171,171,171)), (30,15))
		screen.blit(pygame.font.SysFont('Times New Roman', g1).render("Score_To_Win", True, (255, 255, 255)), (80, 120))
		screen.blit(pygame.font.SysFont('Times New Roman', g2).render("Time_Limit", True, (255, 255, 255)), (80, 180))
		screen.blit(pygame.font.SysFont('Times New Roman', g3).render("Control", True, (255, 255, 255)), (80, 240))
		screen.blit(pygame.font.SysFont('Times New Roman', g4).render("Reset", True, (255, 255, 255)), (80, 500))
		screen.blit(pygame.font.SysFont('Times New Roman', g5).render("Confirm", True, (255, 255, 255)), (80, 560))
		pygame.draw.circle(screen, (255,255,255), (60,setbarcircley),6,0)
		#-------------------------------------------Score-------------------------------------------------------#
		screen.blit(pygame.font.SysFont('Times New Roman', g1-5).render("%d"%(winscore), True, (255, 255, 255)), (450, 125))
		#-------------------------------------------------------------------------------------------------------#
		#-------------------------------------------Time--------------------------------------------------------#
		if ultitime >= 10:
			timelimit = 1
			screen.blit(pygame.font.SysFont('Times New Roman', g2-5).render("%d"%(ultitime), True, (255, 255, 255)), (440, 185))
		elif ultitime == 0:
			timelimit = 0
			screen.blit(pygame.font.SysFont('Times New Roman', g2-5).render("Off", True, (255, 255, 255)), (440, 185))
		#------------------------------------------------------------------------------------------------------#
		#-------------------------------------------Control----------------------------------------------------#
		if (control%2) == 1:
			screen.blit(pygame.font.SysFont('Times New Roman', 40).render("P1 : ", True, (255, 255, 255)), (350, 245))
			screen.blit(control_w,(425,240))
			screen.blit(control_s,(485,240))
			screen.blit(pygame.font.SysFont('Times New Roman', 40).render("P2 : ", True, (255, 255, 255)), (350, 325))
			screen.blit(control_up,(425,320))
			screen.blit(control_down,(485,320))
			if barfreemove%2 == 1:
				screen.blit(control_a,(545,240))
				screen.blit(control_d,(605,240))
				screen.blit(control_left,(545,320))
				screen.blit(control_right,(605,320))
		elif (control%2) == 0:
			screen.blit(pygame.font.SysFont('Times New Roman', 40).render("P1 : ", True, (255, 255, 255)), (350, 245))
			screen.blit(control_w,(425,320))
			screen.blit(control_s,(485,320))
			screen.blit(pygame.font.SysFont('Times New Roman', 40).render("P2 : ", True, (255, 255, 255)), (350, 325))
			screen.blit(control_up,(425,240))
			screen.blit(control_down,(485,240))
			if barfreemove%2 == 1:
				screen.blit(control_a,(545,320))
				screen.blit(control_d,(605,320))
				screen.blit(control_left,(545,240))
				screen.blit(control_right,(605,240))
		#------------------------------------------------------------------------------------------------------#
		pygame.display.update()
		for events in pygame.event.get():
			if events.type == pygame.KEYDOWN:	
				if events.key == pygame.K_ESCAPE:
					quit_game()
				elif events.key == pygame.K_SPACE:
					if sg==4:
						winscore = 3
						ultitime = 60
						control = 1
						sg=5
					elif sg==5:
						set=5
						gamestate = "setting_duel"
				elif events.key == pygame.K_BACKSPACE:
					gamestate = "setting_duel"
				elif events.key == pygame.K_TAB or events.key == pygame.K_s or events.key == pygame.K_DOWN:
					sg +=1
					if sg == 6:
						sg = 1
				elif events.key == pygame.K_w or events.key == pygame.K_UP :
					sg -=1	
					if sg == 0:
						sg = 5
				if sg == 1:
					if events.key == pygame.K_d or events.key == pygame.K_RIGHT:
						winscore +=1
					elif events.key == pygame.K_a or events.key == pygame.K_LEFT :
						if winscore > 1:
							winscore -=1	
				if sg == 2:
					if events.key == pygame.K_d or events.key == pygame.K_RIGHT:
						ultitime +=10
					elif events.key == pygame.K_a or events.key == pygame.K_LEFT :
						if ultitime >= 10:
							ultitime -=10	
				if sg == 3:
					if events.key == pygame.K_d or events.key == pygame.K_RIGHT:
						control +=1
					elif events.key == pygame.K_a or events.key == pygame.K_LEFT :
						control -=1		
#=================================================================================================#
	if gamestate == "setting_survival":
		screen.blit(background,(0,0))
		c1,c2,c3 = 40,40,30
		if sc == 1:
			c1 = 50
			setconcircley =145
			drawlefttri(340,185,30,80)
			drawrighttri(545,185,30,80)
		elif sc == 2:
			c2 = 50
			setconcircley =285
		elif sc == 3:
			c3 = 40
			setconcircley =585
		screen.blit(pygame.font.SysFont('Times New Roman', 80).render("Survival", True, (171,171,171)), (30,15))
		screen.blit(pygame.font.SysFont('Times New Roman', c1).render("Control", True, (255, 255, 255)), (80, 120))
		screen.blit(pygame.font.SysFont('Times New Roman', c2).render("Highscore_List", True, (255, 255, 255)), (80, 260))
		screen.blit(pygame.font.SysFont('Times New Roman', 40).render("1P_Highest_Score  :  %d"%(sur_1p_top5[1]), True, (171 ,171 ,171)), (80, 340))
		screen.blit(pygame.font.SysFont('Times New Roman', 40).render("2P_Highest_Score  :  %d"%(sur_2p_top5[1]), True, (171 ,171 ,171)), (80, 400))
		screen.blit(pygame.font.SysFont('Times New Roman', c3).render("Confirm", True, (255, 255, 255)), (80, 560))
		pygame.draw.circle(screen, (255,255,255), (60,setconcircley),6,0)
		#-------------------------------------------Control----------------------------------------------------#
		if (control%2) == 1:
			screen.blit(pygame.font.SysFont('Times New Roman', 40).render("P1 : ", True, (255, 255, 255)), (350, 125))
			screen.blit(control_w,(425,120))
			screen.blit(control_s,(485,120))
			screen.blit(pygame.font.SysFont('Times New Roman', 40).render("P2 : ", True, (255, 255, 255)), (350, 205))
			screen.blit(control_up,(425,200))
			screen.blit(control_down,(485,200))
		elif (control%2) == 0:
			screen.blit(pygame.font.SysFont('Times New Roman', 40).render("P1 : ", True, (255, 255, 255)), (350, 125))
			screen.blit(control_w,(425,200))
			screen.blit(control_s,(485,200))
			screen.blit(pygame.font.SysFont('Times New Roman', 40).render("P2 : ", True, (255, 255, 255)), (350, 205))
			screen.blit(control_up,(425,120))
			screen.blit(control_down,(485,120))
		#------------------------------------------------------------------------------------------------------#
		pygame.display.update()
		for events in pygame.event.get():
			if events.type == pygame.KEYDOWN:	
				if events.key == pygame.K_ESCAPE:
					quit_game()
				elif events.key == pygame.K_SPACE:
					if sc == 2:
						gamestate = "highscore"
					if sc == 3:
						scorer = ""
						winner = ""
						score1,score2 = 0,0
						timeout = 0
						loadseconds=0
						loadtime=0
						survivalscore,catchscore = 0,0
						loadpercentage = 0
						loadtimer = pygame.time.Clock()
						gamestate = "loading"
				elif events.key == pygame.K_BACKSPACE:
					gamestate = 11
				elif events.key == pygame.K_TAB or events.key == pygame.K_s or events.key == pygame.K_DOWN:
					sc +=1
					if sc == 4:
						sc = 1
				elif events.key == pygame.K_w or events.key == pygame.K_UP :
					sc -=1	
					if sc == 0:
						sc = 3
				if sc == 1:
					if events.key == pygame.K_d or events.key == pygame.K_RIGHT:
						control += 1
					elif events.key == pygame.K_a or events.key == pygame.K_LEFT:
						control -= 1
#=================================================================================================#
	if gamestate == "countdown":
		screen.blit(background,(0,0))
		screen.blit(top_margin,(0,0))
		countdownmilli = countdowntimer.tick()
		countdownseconds += countdownmilli
		countdown321 = 3 - int(countdownseconds/1000)
		if gravity%2 == 0:
			screen.blit(gra_50_dark,(505,5))
			screen.blit(control_down_dark,(555,5))
		if gravity%2 == 1:
			screen.blit(gra_50,(505,5))
			screen.blit(control_down,(555,5))
		if ran_reflect%2 == 1:
			screen.blit(bounce_50,(410,5))
		if ran_reflect%2 == 0:
			screen.blit(bounce_50_dark,(410,5))
		if lasermode%2 == 0:
			screen.blit(laser_50_dark,(245,5))
		if lasermode%2 == 1:
			screen.blit(laser_50,(245,5))
		#---------------------------Acceleration----------------------------#
		if acceleration%2 == 0:
			screen.blit(accel_50_dark,(300,5))
		if acceleration%2 == 1:
			screen.blit(accel_50,(300,5))
			accelboxy=screen_height*44/64*random.random()+80
			pygame.draw.line(screen, (255,255,0), (mid_width,200), (mid_width,200+100), 150)
			pygame.draw.line(screen, (0,255,0), (mid_width+15-75,200+10), (mid_width+45-75,200+50), 10)
			pygame.draw.line(screen, (0,255,0), (mid_width+15-75,200+90), (mid_width+45-75,200+50), 10)
			pygame.draw.line(screen, (0,255,0), (mid_width+45-75,200+10), (mid_width+75-75,200+50), 10)
			pygame.draw.line(screen, (0,255,0), (mid_width+45-75,200+90), (mid_width+75-75,200+50), 10)
			pygame.draw.line(screen, (0,255,0), (mid_width+75-75,200+10), (mid_width+105-75,200+50), 10)
			pygame.draw.line(screen, (0,255,0), (mid_width+75-75,200+90), (mid_width+105-75,200+50), 10)
			pygame.draw.line(screen, (0,255,0), (mid_width+105-75,200+10), (mid_width+135-75,200+50), 10)
			pygame.draw.line(screen, (0,255,0), (mid_width+105-75,200+90), (mid_width+135-75,200+50), 10)
		#-------------------------------------------------------------------#
		#---------------------------Curve_Ball------------------------------#
		if curve_ball%2 == 0:
			screen.blit(vibrate_50_dark,(610,5))
		if curve_ball%2 == 1:
			screen.blit(vibrate_50,(610,5))
		#-------------------------------------------------------------------#
		#---------------------------Wormhole--------------------------------#
		if wormhole%2 == 0:
			screen.blit(wh_50_dark,(665,5))
		if wormhole%2 == 1:
			screen.blit(wh_50,(665,5))
			pygame.draw.circle(screen, (30,30,30), (int(0.5*mid_width),200), 50,0)
			screen.blit(blackhole_70,(int(0.5*mid_width)-35,200-35))
			pygame.draw.circle(screen, (30,30,30), (int(1.5*mid_width),400), 50,0)
			screen.blit(blackhole_70,(int(1.5*mid_width)-35,400-35))
		#-------------------------------------------------------------------#
		#---------------------------Invisibility1---------------------------#
		if invisibility%2 == 0:
			screen.blit(invis_50_dark,(355,5))
		if invisibility%2 == 1:
			screen.blit(invis_50,(355,5))
			pygame.draw.line(screen, (200,200,200), (0.6*mid_width,60), (0.6*mid_width,640), 1)
			pygame.draw.line(screen, (200,200,200), (1.4*mid_width,60), (1.4*mid_width,640), 1)
		#-------------------------------------------------------------------#
		pygame.draw.line(screen, (171,171,171), (480,60), (480,61), 960)
		#pygame.draw.line(screen, (171,171,171), (480,0), (480,640), 1)
		remaintime = ultitime
		if mode == 1 or mode == 2:
			screen.blit(pygame.font.SysFont('Times New Roman', 20).render("%d"%(remaintime), True, (255, 255, 255)), (467, 10))
		if mode == 1 or mode == 2:
			screen.blit(pygame.font.SysFont('Times New Roman', 30).render("P1", True, (51, 153, 255)), (15, 10))
		if mode == 1:
			screen.blit(pygame.font.SysFont('Times New Roman', 30).render("Com", True, (102, 255, 51)), (880,10))	
		if mode == 2:
			screen.blit(pygame.font.SysFont('Times New Roman', 30).render("P2", True, (255, 102, 153)), (905,10))	
		pygame.draw.line(screen, (0,0,255), (bar_x1,bar_y1-bar_half_length), (bar_x1,bar_y1+bar_half_length), bar_width)
		if mode == 1:
			pygame.draw.line(screen, (0,255,0), (bar_x2,bar_y2-bar_half_length), (bar_x2,bar_y2+bar_half_length), bar_width)
		if mode == 2 or mode == 4 or mode == 6: 
			pygame.draw.line(screen, (255,0,0), (bar_x2,bar_y2-bar_half_length), (bar_x2,bar_y2+bar_half_length), bar_width)	
		screen.blit(pygame.font.SysFont('Times New Roman', 200).render("%d"%(countdown321), True, (255, 0, 0)), (435, 230))
		screen.blit(pygame.font.SysFont('Times New Roman', 30).render("You can press P to pause in the game.", True, (255, 255,255)), (250, 450))
		if mode == 3 or mode == 4 or mode == 5 or mode == 6:
			screen.blit(pygame.font.SysFont('Times New Roman', 35).render("Score : 0", True, (255, 255, 255)), (750,10))
		pygame.display.update()
		if countdown321 == 0:
			clock=pygame.time.Clock()
			timer=pygame.time.Clock()
			if mode == 5 or mode == 6:
				gamestate = 2
			else:
				gamestate = 1
		for events in pygame.event.get():
			if events.type == pygame.KEYDOWN:	
				if events.key == pygame.K_ESCAPE:
					quit_game()				
#=================================================================================================#					
	if gamestate == "pause":
		screen.blit(background,(0,0))
		screen.blit(top_margin,(0,0))
		if gravity%2 == 0:
			screen.blit(gra_50_dark,(505,5))
			screen.blit(control_down_dark,(555,5))
		if gravity%2 == 1:
			screen.blit(gra_50,(505,5))
			if gra_ran >= 0 and gra_ran < 2:
				screen.blit(control_down,(555,5))
			if gra_ran >= 2 and gra_ran < 4:
				screen.blit(control_up,(555,5))
			if mode != 5 and mode != 6:
				if gra_ran >= 4 and gra_ran < 5:
					screen.blit(control_right,(555,5))
				if gra_ran >= 5 and gra_ran <= 6:
					screen.blit(control_left,(550,5))
			if mode == 5 or mode == 6:
				if gra_ran >= 4 and gra_ran <= 6:
					screen.blit(control_left,(550,5))
			screen.blit(pygame.font.SysFont('Times New Roman', 40).render("%d"%(gracountdown), True, (250, 250, 250)), (517, 8))
		if ran_reflect%2 == 1:
			screen.blit(bounce_50,(410,5))
		if ran_reflect%2 == 0:
			screen.blit(bounce_50_dark,(410,5))
		if lasermode%2 == 0:
			screen.blit(laser_50_dark,(245,5))
		if lasermode%2 == 1:
			screen.blit(laser_50,(245,5))
			if gametimer >= 2:
				if laser == 1:
					pygame.draw.line(screen, (255,0,0), (480,laser_y), (480,laser_y+1), 960)
					screen.blit(pygame.font.SysFont('Times New Roman', 40).render("%d"%(lasercountdown), True, (250, 250, 250)), (262, 8))
				if laser == 2:
					pygame.draw.line(screen, (255,0,0), (480,laser_y-20), (480,laser_y+20), 960)
		#---------------------------Acceleration----------------------------#
		if acceleration%2 == 0:
			screen.blit(accel_50_dark,(300,5))
		if acceleration%2 == 1:
			screen.blit(accel_50,(300,5))
			pygame.draw.line(screen, (255,255,0), (mid_width,accelboxy), (mid_width,accelboxy+100), 150)
			if acceldir == 1:
				pygame.draw.line(screen, (0,255,0), (mid_width+15-75,accelboxy+10), (mid_width+45-75,accelboxy+50), 10)
				pygame.draw.line(screen, (0,255,0), (mid_width+15-75,accelboxy+90), (mid_width+45-75,accelboxy+50), 10)
				pygame.draw.line(screen, (0,255,0), (mid_width+45-75,accelboxy+10), (mid_width+75-75,accelboxy+50), 10)
				pygame.draw.line(screen, (0,255,0), (mid_width+45-75,accelboxy+90), (mid_width+75-75,accelboxy+50), 10)
				pygame.draw.line(screen, (0,255,0), (mid_width+75-75,accelboxy+10), (mid_width+105-75,accelboxy+50), 10)
				pygame.draw.line(screen, (0,255,0), (mid_width+75-75,accelboxy+90), (mid_width+105-75,accelboxy+50), 10)
				pygame.draw.line(screen, (0,255,0), (mid_width+105-75,accelboxy+10), (mid_width+135-75,accelboxy+50), 10)
				pygame.draw.line(screen, (0,255,0), (mid_width+105-75,accelboxy+90), (mid_width+135-75,accelboxy+50), 10)
			if acceldir == -1:
				pygame.draw.line(screen, (0,255,0), (mid_width+45-75,accelboxy+10), (mid_width+15-75,accelboxy+50), 10)
				pygame.draw.line(screen, (0,255,0), (mid_width+45-75,accelboxy+90), (mid_width+15-75,accelboxy+50), 10)
				pygame.draw.line(screen, (0,255,0), (mid_width+75-75,accelboxy+10), (mid_width+45-75,accelboxy+50), 10)
				pygame.draw.line(screen, (0,255,0), (mid_width+75-75,accelboxy+90), (mid_width+45-75,accelboxy+50), 10)
				pygame.draw.line(screen, (0,255,0), (mid_width+105-75,accelboxy+10), (mid_width+75-75,accelboxy+50), 10)
				pygame.draw.line(screen, (0,255,0), (mid_width+105-75,accelboxy+90), (mid_width+75-75,accelboxy+50), 10)
				pygame.draw.line(screen, (0,255,0), (mid_width+135-75,accelboxy+10), (mid_width+105-75,accelboxy+50), 10)
				pygame.draw.line(screen, (0,255,0), (mid_width+135-75,accelboxy+90), (mid_width+105-75,accelboxy+50), 10)
			if (invisibility%2 == 0) or ( invisibility%2 == 1 and  ((ballx < 0.6*mid_width or ballx > 1.4*mid_width) or (ballx > 0.99*mid_width and ballx < 1.01*mid_width) )) or (accelball == 1):
				if accelball == 1 and ball == 1:
					pygame.draw.circle(screen, (255,153,0), (int(ballx),int(bally)), ball_r,0)
				if accelball == 0 and ball == 1:
					pygame.draw.circle(screen, (204,255,255), (int(ballx),int(bally)), ball_r,0)
			if (invisibility%2 == 0) or ( invisibility%2 == 1 and  ((ball2x < 0.6*mid_width or ball2x > 1.4*mid_width) or (ball2x > 0.99*mid_width and ball2x < 1.01*mid_width) )) or (accelball2 == 1):
				if mode != 5 and mode != 6:
					if accelball2 == 1 and ballnum%2 == 0:
						pygame.draw.circle(screen, (204,0,204), (int(ball2x),int(ball2y)), ball2_r,0)			
					if accelball2 == 0 and ballnum%2 == 0:
						pygame.draw.circle(screen, (255,153,153), (int(ball2x),int(ball2y)), ball2_r,0)
				if mode == 5 or mode == 6:
					if accelball2 == 1 and ball2 == 1:
						pygame.draw.circle(screen, (255,153,0), (int(ball2x),int(ball2y)), ball2_r,0)			
					if accelball2 == 0 and ball2 == 1:
						pygame.draw.circle(screen, (255,153,153), (int(ball2x),int(ball2y)), ball2_r,0)
			if (invisibility%2 == 0) or ( invisibility%2 == 1 and  ((ball3x < 0.6*mid_width or ball3x > 1.4*mid_width) or (ball3x > 0.99*mid_width and ball3x < 1.01*mid_width) )) or (accelball3 == 1):
				if mode == 5 or mode == 6:
					if accelball3 == 1 and ball3 == 1:
						pygame.draw.circle(screen, (153,51,0), (int(ball3x),int(ball3y)), ball3_r,0)			
					if accelball3 == 0 and ball3 == 1:
						pygame.draw.circle(screen, (255,153,153), (int(ball3x),int(ball3y)), ball3_r,0)
		#-------------------------------------------------------------------#
		#---------------------------Curve_Ball------------------------------#
		if curve_ball%2 == 0:
			screen.blit(vibrate_50_dark,(610,5))
		if curve_ball%2 == 1:
			screen.blit(vibrate_50,(610,5))
		#-------------------------------------------------------------------#
		#---------------------------Wormhole--------------------------------#
		if wormhole%2 == 0:
			screen.blit(wh_50_dark,(665,5))
		if wormhole%2 == 1:
			screen.blit(wh_50,(665,5))
			pygame.draw.circle(screen, (30,30,30), (int(0.5*mid_width),int(why1)), 50,0)
			screen.blit(blackhole_70,(int(0.5*mid_width)-35,int(why1)-35))
			pygame.draw.circle(screen, (30,30,30), (int(1.5*mid_width),int(why2)), 50,0)
			screen.blit(blackhole_70,(int(1.5*mid_width)-35,int(why2)-35))
		#-------------------------------------------------------------------#
		#---------------------------Invisibility1---------------------------#
		if invisibility%2 == 0:
			screen.blit(invis_50_dark,(355,5))
		if invisibility%2 == 1:
			screen.blit(invis_50,(355,5))
			pygame.draw.line(screen, (200,200,200), (0.6*mid_width,60), (0.6*mid_width,640), 1)
			pygame.draw.line(screen, (200,200,200), (1.4*mid_width,60), (1.4*mid_width,640), 1)
		#-------------------------------------------------------------------#
		if (invisibility%2 == 0) or ( invisibility%2 == 1 and  ((ballx < 0.6*mid_width or ballx > 1.4*mid_width) or (ballx > 0.99*mid_width and ballx < 1.01*mid_width) )):
			if accelball == 0 and ball == 1:
				pygame.draw.circle(screen, (204,255,255), (int(ballx),int(bally)), ball_r,0)
		if (invisibility%2 == 0) or ( invisibility%2 == 1 and  ((ball2x < 0.6*mid_width or ball2x > 1.4*mid_width) or (ball2x > 0.99*mid_width and ball2x < 1.01*mid_width) )):
			if mode != 5 and mode != 6:
				if accelball2 == 0 and ballnum%2 == 0:
					pygame.draw.circle(screen, (255,153,153), (int(ball2x),int(ball2y)), ball2_r,0)
			if mode == 5 or mode == 6:
				if accelball2 == 0 and ball2 == 1:
					pygame.draw.circle(screen, (255,153,153), (int(ball2x),int(ball2y)), ball2_r,0)
		if (invisibility%2 == 0) or ( invisibility%2 == 1 and  ((ball3x < 0.6*mid_width or ball3x > 1.4*mid_width) or (ball3x > 0.99*mid_width and ball3x < 1.01*mid_width) )):
			if mode == 5 or mode == 6:
				if accelball3 == 0 and ball3 == 1:
					pygame.draw.circle(screen, (255,153,153), (int(ball3x),int(ball3y)), ball3_r,0)							
		pygame.draw.line(screen, (171,171,171), (480,60), (480,61), 960)
		if mode == 1 or mode == 2 or mode == 5 or mode == 6:
			screen.blit(pygame.font.SysFont('Times New Roman', 20).render("%d"%(remaintime), True, (255, 255, 255)), (467, 10))
		if mode == 1 or mode == 2:
			screen.blit(pygame.font.SysFont('Times New Roman', 30).render("P1", True, (51, 153, 255)), (15, 10))
		if mode == 1:
			screen.blit(pygame.font.SysFont('Times New Roman', 30).render("Com", True, (102, 255, 51)), (880,10))	
		if mode == 2:
			screen.blit(pygame.font.SysFont('Times New Roman', 30).render("P2", True, (255, 102, 153)), (905,10))	
		pygame.draw.line(screen, (0,0,255), (bar_x1,bar_y1-bar_half_length), (bar_x1,bar_y1+bar_half_length), bar_width)
		if mode == 1:
			pygame.draw.line(screen, (0,255,0), (bar_x2,bar_y2-bar_half_length), (bar_x2,bar_y2+bar_half_length), bar_width)
		if mode == 2 or mode == 4 or mode == 6: 
			pygame.draw.line(screen, (255,0,0), (bar_x2,bar_y2-bar_half_length), (bar_x2,bar_y2+bar_half_length), bar_width)
		if mode == 3 or mode == 4:
			screen.blit(pygame.font.SysFont('Times New Roman', 35).render("Score : %d"%(survivalscore), True, (255, 255, 255)), (750,10))
		if mode == 5 or mode == 6:
			screen.blit(pygame.font.SysFont('Times New Roman', 35).render("Score : %d"%(catchscore), True, (255, 255, 255)), (750,10))
			if ball == 1:
				pygame.draw.circle(screen, (204,255,255), (50,30),20,0)
				if catchballscore < 10:
					screen.blit(pygame.font.SysFont('Times New Roman', 30).render("%d"%(catchballscore), True, (0, 0, 102)), (43, 13))
				if catchballscore >= 10:
					screen.blit(pygame.font.SysFont('Times New Roman', 30).render("%d"%(catchballscore), True, (0, 0, 102)), (38, 13))
			if ball == 0:
				screen.blit(pygame.font.SysFont('Times New Roman', 40).render("%d"%(ballcountdown), True, (204, 255, 255)), (38, 8))
			if ball2 == 1:
				pygame.draw.circle(screen, (255,153,153), (110,30), 20,0)	
				if catchball2score < 10:
					screen.blit(pygame.font.SysFont('Times New Roman', 30).render("%d"%(catchball2score), True, (102, 0, 0)), (103, 13))
				if catchball2score >= 10:
					screen.blit(pygame.font.SysFont('Times New Roman', 30).render("%d"%(catchball2score), True, (102, 0, 0)), (98, 13))
			if ball2 == 0 and gameseconds > 15000:
				screen.blit(pygame.font.SysFont('Times New Roman', 40).render("%d"%(ball2countdown), True, (255,153,153)), (98, 8))
			if ball3 == 1:
				pygame.draw.circle(screen, (102,255,102), (170,30), 20,0)	
				if catchball3score < 10:
					screen.blit(pygame.font.SysFont('Times New Roman', 30).render("%d"%(catchball3score), True, (0, 102, 0)), (163, 13))
				if catchball2score >= 10:
					screen.blit(pygame.font.SysFont('Times New Roman', 30).render("%d"%(catchball3score), True, (0, 102, 0)), (158, 13))
			if ball3 == 0 and gameseconds > 30000:
				screen.blit(pygame.font.SysFont('Times New Roman', 40).render("%d"%(ball3countdown), True, (102,255,102)), (158, 8))
			if pointchange > 0:
				screen.blit(pygame.font.SysFont('Times New Roman', 30).render("+%d"%(pointchange), True, (0, 255, 0)), (910,13))
			if pointchange < 0:
				screen.blit(pygame.font.SysFont('Times New Roman', 30).render("%d"%(pointchange), True, (255, 0, 0)), (910,13))
		screen.blit(pygame.font.SysFont('Times New Roman', 200).render("PAUSE", True, (255, 0, 0)), (180, 230))
		screen.blit(pygame.font.SysFont('Times New Roman', 30).render("Press P to resume", True, (255, 255,255)), (350, 450))
		for events in pygame.event.get():
			if events.type == pygame.KEYDOWN:	
				if events.key == pygame.K_p:
					milli=clock.tick()
					gamemilli=timer.tick()
					if mode != 5 and mode != 6:
						gamestate = 1
					if mode == 5 or mode == 6:
						gamestate = 2
		pygame.display.update()
#=================================================================================================#
	if gamestate == 2: #CatchBall#
		screen.blit(background,(0,0))
		screen.blit(top_margin,(0,0))
		for events in pygame.event.get():
			if events.type == pygame.QUIT:
				quit_game()
			#=============================鍵盤控制 BEGIN=============================#
			if events.type == pygame.KEYDOWN:
				if events.key == pygame.K_p:
					gamestate = "pause"
				if control%2 == 1:
					if events.key == pygame.K_w:
						bar_diry1=-1
					elif events.key == pygame.K_s:
						bar_diry1=1
					if mode == 5 or mode == 6:
						if events.key == pygame.K_UP:
							bar_diry2=-1
						elif events.key == pygame.K_DOWN:
							bar_diry2=1
				if control%2 == 0:
					if events.key == pygame.K_UP:
						bar_diry1=-1
					elif events.key == pygame.K_DOWN:
						bar_diry1=1
					if mode == 5 or mode == 6:
						if events.key == pygame.K_w:
							bar_diry2=-1
						elif events.key == pygame.K_s:
							bar_diry2=1
				if events.key == pygame.K_ESCAPE:
					quit_game()
				if events.key == pygame.K_BACKSPACE:
					if mode == 5 or mode == 6:
						gameseconds=0
						gametimer=0
						laser=0
						survivalscore = 0
						gamestate = "setting_catch"
			if events.type == pygame.KEYUP:
				if control%2 == 1:
					if events.key == pygame.K_w or events.key == pygame.K_s:
						bar_diry1=0
					if mode == 6:
						if events.key == pygame.K_UP or events.key == pygame.K_DOWN:
							bar_diry2=0
				if control%2 == 0:
					if events.key == pygame.K_UP or events.key == pygame.K_DOWN:
						bar_diry1=0
					if mode == 6:
						if events.key == pygame.K_w or events.key == pygame.K_s:
							bar_diry2=0						
			#=============================鍵盤控制 END=============================#
		#=============================計算時間 BEGIN=============================#
		milli=clock.tick()
		seconds=milli/1000.0
		gamemilli=timer.tick()
		gameseconds+=gamemilli
		gametimer = int(gameseconds/1000)
		remaintime = ultitime - gametimer
		if remaintime == 0 :
			timeout = 1
			gamestate = 0
		#=============================計算時間 END=============================#
		#--------------------------Unknown-----------------------------#
		if mode == 5 or mode == 6:
			if ball == 1:
				ball_speedx += 2*seconds
				ball_speedy += 2*seconds
			if ball2 == 1:
				ball2_speedx += 2*seconds
				ball2_speedy += 2*seconds
			if ball3 == 1:
				ball3_speedx += 2*seconds
				ball3_speedy += 2*seconds
			if gameseconds > 15000 and ball2first == 0:
				ball2 = 1
				ball2first = 1
			if gameseconds >30000 and ball3first == 0:
				ball3 = 1
				ball3first = 1
			if gameseconds <= 15000:
				pmmodeonmax = 1
			if gameseconds > 15000 and gameseconds <= 45000:
				pmmodeonmax = 2
			if gameseconds > 45000 and gameseconds <= 90000:
				pmmodeonmax = 3
			if gameseconds > 90000:
				pmmodeonmax = 4
			if gameseconds%15000 >= 14980 :
				pmmodeon = 0
				lasermode,acceleration,invisibility,ran_reflect,gravity,curve_ball,wormhole = 0,0,0,0,0,0,0
			if gameseconds%15000 >= 12000:
				screen.blit(red_warning,(350,580))
			if pmmodeon < pmmodeonmax and gameseconds%15000 <= 2000:
				catchmode_ran = 12*random.random()
				if catchmode_ran >= 0 and catchmode_ran < 2:
					lasermode = 1
				if catchmode_ran >= 2 and catchmode_ran < 4:
					acceleration = 1
					accelboxy=screen_height*39/64*random.random()+100
				if catchmode_ran >= 4 and catchmode_ran < 6:
					invisibility = 1
				if catchmode_ran >= 6 and catchmode_ran < 7:
					ran_reflect = 1
				if catchmode_ran >= 7 and catchmode_ran < 9:
					gravity = 1
				if catchmode_ran >= 9 and catchmode_ran < 10:
					curve_ball = 1
				if catchmode_ran >= 10 and catchmode_ran < 12:
					wormhole = 1
					why1=screen_height*44/64*random.random()+100
					why2=screen_height*44/64*random.random()+100
				pmmodeon += 1	
		#---------------------------------------------------------------#
		#=============================計算球和棒子的新位置 BEGIN=============================#
		#------------------------------Gravity---------------------------#
		if gravity%2 == 0:
			screen.blit(gra_50_dark,(505,5))
			screen.blit(control_down_dark,(555,5))
			if grastatus == 1:
				grastatus = 0
				ball_speedx,ball_speedy = ball_speedx0,ball_speedy0
				ball2_speedx,ball2_speedy = ball2_speedx0,ball2_speedy0
				ball3_speedx,ball3_speedy = ball3_speedx0,ball3_speedy0
			else:
				grastatus = 0
			grastarttime = gameseconds
		if gravity%2 == 1:
			screen.blit(gra_50,(505,5))			
			if grastatus == 0:
				grastarttime = gameseconds
				ball_speedx0,ball_speedy0 = ball_speedx,ball_speedy
				ball2_speedx0,ball2_speedy0 = ball2_speedx,ball2_speedy
				ball3_speedx0,ball3_speedy0 = ball3_speedx,ball3_speedy
				grastatus = 1
			gracountdown = 5 - int((gameseconds - grastarttime)/1000)%5
			if grastatus == 1:	
				gra_ran = 6*random.random()
				grastatus = 2
			if gameseconds%5000 >= 4980:
				ball_speedx,ball_speedy = ball_speedx0,ball_speedy0
				ball2_speedx,ball2_speedy = ball2_speedx0,ball2_speedy0
				ball3_speedx,ball3_speedy = ball3_speedx0,ball3_speedy0
				grastatus = 1
			if gra_ran >= 0 and gra_ran < 2:
				screen.blit(control_down,(555,5))
				if ball == 1:
					if ball_diry>0:
						ball_speedy+=accelgra*seconds	
					elif ball_diry<0:
						ball_speedy-=accelgra*seconds
				if ball2 == 1:
					if ball2_diry>0:
						ball2_speedy+=accelgra*seconds
					elif ball2_diry<0:
						ball2_speedy-=accelgra*seconds
				if ball3 == 1:
					if ball3_diry>0:
						ball3_speedy+=accelgra*seconds
					elif ball2_diry<0:
						ball3_speedy-=accelgra*seconds
			if gra_ran >= 2 and gra_ran < 4:
				screen.blit(control_up,(555,5))
				if ball == 1:
					if ball_diry<0:
						ball_speedy+=accelgra*seconds	
					elif ball_diry>0:
						ball_speedy-=accelgra*seconds
				if ball2 == 1:
					if ball2_diry<0:
						ball2_speedy+=accelgra*seconds
					elif ball2_diry>0:
						ball2_speedy-=accelgra*seconds
				if ball3 == 1:
					if ball3_diry<0:
						ball3_speedy+=accelgra*seconds
					elif ball3_diry>0:
						ball3_speedy-=accelgra*seconds
			if gra_ran >= 4 and gra_ran <= 6:
				screen.blit(control_left,(550,5))
				if ball == 1:
					if ball_dirx<0:
						ball_speedx+=accelgra*seconds	
					elif ball_dirx>0:
						ball_speedx-=accelgra*seconds
				if ball2 == 1:
					if ball2_dirx<0:
						ball2_speedx+=accelgra*seconds
					elif ball2_dirx>0:
						ball2_speedx-=accelgra*seconds
				if ball3 == 1:
					if ball3_dirx<0:
						ball3_speedx+=accelgra*seconds
					elif ball3_dirx>0:
						ball3_speedx-=accelgra*seconds
			screen.blit(pygame.font.SysFont('Times New Roman', 40).render("%d"%(gracountdown), True, (250, 250, 250)), (517, 8))
			if ball_speedy < 0:
				grareversey1 = 1
			if grareversey1 == 1:
				ball_diry = -ball_diry
				ball_speedy = -ball_speedy
				grareversey1 = 0
			if ball2_speedy < 0:
				grareversey2 = 1
			if grareversey2 == 1:
				ball2_diry = -ball2_diry
				ball2_speedy = -ball2_speedy
				grareversey2 = 0
			if ball3_speedy < 0:
				grareversey3 = 1
			if grareversey3 == 1:
				ball3_diry = -ball3_diry
				ball3_speedy = -ball3_speedy
				grareversey2 = 0
			if ball_speedx < 0:
				grareversex1 = 1
			if grareversex1 == 1:
				ball_dirx = -ball_dirx
				ball_speedx = -ball_speedx
				grareversex1 = 0
			if ball2_speedx < 0:
				grareversex2 = 1
			if grareversex2 == 1:
				ball2_dirx = -ball2_dirx
				ball2_speedx = -ball2_speedx
				grareversex2 = 0
			if ball3_speedx < 0:
				grareversex3 = 1
			if grareversex3 == 1:
				ball3_dirx = -ball3_dirx
				ball3_speedx = -ball3_speedx
				grareversex3 = 0
		#----------------------------------------------------------------#
		if ball == 1:
			ballx+=seconds*ball_dirx*ball_speedx
			bally+=seconds*ball_diry*ball_speedy
		if ball2 == 1:
			ball2x+=seconds*ball2_dirx*ball2_speedx
			ball2y+=seconds*ball2_diry*ball2_speedy
		if ball3 == 1:
			ball3x+=seconds*ball3_dirx*ball3_speedx
			ball3y+=seconds*ball3_diry*ball3_speedy
		#-----------------------------球撞到左邊的邊緣時BEGIN---------------------------#
		if ballx<ball_r and ball == 1:
			if (sound%2) == 1:
				sound2.play()
			catchscore -= 2
			pointchange = -2
			if catchballscore > 2:
				catchballscore -= 2
			if catchballscore <= 2:
				catchballscore = 1
			ball_speedx,ball_speedy = 350,350
			ballx,bally = 900,320
			ball = 0
		if ball == 1:
			balldeadtime = gameseconds
		if ball == 0:
			accelball = 0
			ball_speedx,ball_speedy = 350,350
			ballx,bally = 900,320
			if (gameseconds - balldeadtime) >= catchballscore*1000:
				ball = 1
		if ball2x<ball2_r and ball2 == 1:
			if (sound%2) == 1:
				sound2.play()
			catchscore -= 2
			pointchange = -2
			if catchball2score > 2:
				catchball2score -= 2
			if catchball2score <= 2:
				catchball2score = 1
			ball2_speedx,ball2_speedy = 349,349
			ball2x,ball2y = 900,320
			ball2 = 0
		if ball2 == 1:
			ball2deadtime = gameseconds
		if ball2 == 0:
			accelball2 = 0
			ball2_speedx,ball2_speedy = 349,349
			ball2x,ball2y = 900,320
			if (gameseconds - ball2deadtime) >= catchball2score*1000 and gameseconds > 15000:
				ball2 = 1
		if ball3x<ball3_r and ball3 == 1:
			if (sound%2) == 1:
				sound2.play()
			catchscore -= 2
			pointchange = -2
			if catchball3score > 2:
				catchball3score -= 2
			if catchball3score <= 2:
				catchball3score = 1
			ball3_speedx,ball3_speedy = 348,348
			ball3x,ball3y = 900,320
			ball3 = 0
		if ball3 == 1:
			ball3deadtime = gameseconds
		if ball3 == 0:
			accelball3 = 0
			ball3_speedx,ball3_speedy = 348,348
			ball3x,ball3y = 900,320
			if (gameseconds - ball3deadtime) >= catchball3score*1000 and gameseconds > 30000:
				ball3 = 1
		ballcountdown = catchballscore-int((gameseconds - balldeadtime)/1000)
		ball2countdown = catchball2score-int((gameseconds - ball2deadtime)/1000)
		ball3countdown = catchball3score-int((gameseconds - ball3deadtime)/1000)
		#-----------------------------球撞到左邊的邊緣時END-----------------------------#
		if ran_reflect%2 == 1:
			screen.blit(bounce_50,(410,5))
		if ran_reflect%2 == 0:
			screen.blit(bounce_50_dark,(410,5))
		#-----------------------------球撞到右邊的邊緣時BEGIN---------------------------#
		if (ballx>screen_width-ball_r) and (ball_dirx>0):
			if ran_reflect%2 == 0:
				ball_dirx=-ball_dirx
			#------------------RANDOM_REFLECTION-----------------------------------#
			if ran_reflect%2 == 1:
				rrx1 = 6*random.random()
				if rrx1 >= 0 and rrx1 < 1:
					ball_dirx,ball_diry=-1.22,0.71
				elif rrx1 >= 1 and rrx1 < 2:
					ball_dirx,ball_diry=-1,1						
				elif rrx1 >= 2 and rrx1 < 3:
					ball_dirx,ball_diry=-1.13,0.85
				elif rrx1 >= 3 and rrx1 < 4:
					ball_dirx,ball_diry=-1.13,-0.85
				elif rrx1 >= 4 and rrx1 < 5:
					ball_dirx,ball_diry=-1,-1
				elif rrx1 >= 5 and rrx1 <= 6:
					ball_dirx,ball_diry=-1.22,-0.71
			#------------------RANDOM_REFLECTION-----------------------------------#
		if (ball2x>screen_width-ball2_r) and (ball2_dirx>0):
			if ran_reflect%2 == 0:
				ball2_dirx=-ball2_dirx
			#------------------RANDOM_REFLECTION-----------------------------------#
			if ran_reflect%2 == 1:
				rrx1 = 6*random.random()
				if rrx1 >= 0 and rrx1 < 1:
					ball2_dirx,ball2_diry=-1.22,0.71
				elif rrx1 >= 1 and rrx1 < 2:
					ball2_dirx,ball2_diry=-1,1						
				elif rrx1 >= 2 and rrx1 < 3:
					ball2_dirx,ball2_diry=-1.13,0.85
				elif rrx1 >= 3 and rrx1 < 4:
					ball2_dirx,ball2_diry=-1.13,-0.85
				elif rrx1 >= 4 and rrx1 < 5:
					ball2_dirx,ball2_diry=-1,-1
				elif rrx1 >= 5 and rrx1 <= 6:
					ball2_dirx,ball2_diry=-1.22,-0.71
			#------------------RANDOM_REFLECTION-----------------------------------#
		if (ball3x>screen_width-ball3_r) and (ball3_dirx>0):
			if ran_reflect%2 == 0:
				ball3_dirx=-ball3_dirx
			#------------------RANDOM_REFLECTION-----------------------------------#
			if ran_reflect%2 == 1:
				rrx1 = 6*random.random()
				if rrx1 >= 0 and rrx1 < 1:
					ball3_dirx,ball3_diry=-1.22,0.71
				elif rrx1 >= 1 and rrx1 < 2:
					ball3_dirx,ball3_diry=-1,1						
				elif rrx1 >= 2 and rrx1 < 3:
					ball3_dirx,ball3_diry=-1.13,0.85
				elif rrx1 >= 3 and rrx1 < 4:
					ball3_dirx,ball3_diry=-1.13,-0.85
				elif rrx1 >= 4 and rrx1 < 5:
					ball3_dirx,ball3_diry=-1,-1
				elif rrx1 >= 5 and rrx1 <= 6:
					ball3_dirx,ball3_diry=-1.22,-0.71
			#------------------RANDOM_REFLECTION-----------------------------------#
		#-----------------------------球撞到右邊的邊緣時END------------------------------#
		#-----------------------------球1撞到上方的邊緣時BEGIN---------------------------#
		if(bally<ball_r) and ball_diry < 0 :
			if ran_reflect%2 == 0:
				ball_diry=-ball_diry
			#------------------RANDOM_REFLECTION-----------------------------------#
			if ran_reflect%2 == 1:
				rrx1 = 6*random.random()
				if rrx1 >= 0 and rrx1 < 1:
					ball_dirx,ball_diry=1.22,0.71
				elif rrx1 >= 1 and rrx1 < 2:
					ball_dirx,ball_diry=1,1						
				elif rrx1 >= 2 and rrx1 < 3:
					ball_dirx,ball_diry=1.13,0.85
				elif rrx1 >= 3 and rrx1 < 4:
					ball_dirx,ball_diry=-1.13,0.85
				elif rrx1 >= 4 and rrx1 < 5:
					ball_dirx,ball_diry=-1,1
				elif rrx1 >= 5 and rrx1 <= 6:
					ball_dirx,ball_diry=-1.22,0.71
			#------------------RANDOM_REFLECTION-----------------------------------#
		#-----------------------------球1撞到上方的邊緣時END-----------------------------#
		#-----------------------------球1撞到下方的邊緣時BEGIN---------------------------#
		if(bally>=screen_height-ball_r)and (ball_diry > 0):
			if ran_reflect%2 == 0:
				ball_diry=-ball_diry
			#------------------RANDOM_REFLECTION-----------------------------------#
			if ran_reflect%2 == 1:
				rrx1 = 6*random.random()
				if rrx1 >= 0 and rrx1 < 1:
					ball_dirx,ball_diry=1.22,-0.71
				elif rrx1 >= 1 and rrx1 < 2:
					ball_dirx,ball_diry=1,-1						
				elif rrx1 >= 2 and rrx1 < 3:
					ball_dirx,ball_diry=1.13,-0.85
				elif rrx1 >= 3 and rrx1 < 4:
					ball_dirx,ball_diry=-1.13,-0.85
				elif rrx1 >= 4 and rrx1 < 5:
					ball_dirx,ball_diry=-1,-1
				elif rrx1 >= 5 and rrx1 <= 6:
					ball_dirx,ball_diry=-1.22,-0.71
			#------------------RANDOM_REFLECTION-----------------------------------#
		#-----------------------------球1撞到下方的邊緣時END-----------------------------#
		#-----------------------------球2撞到上方的邊緣時BEGIN---------------------------#
		if(ball2y<ball2_r)and ball2_diry < 0 :
			if ran_reflect%2 == 0:
				ball2_diry=-ball2_diry
			#------------------RANDOM_REFLECTION-----------------------------------#
			if ran_reflect%2 == 1:
				rrx2 = 6*random.random()
				if rrx2 >= 0 and rrx2 < 1:
					ball2_dirx,ball2_diry=1.22,0.71
				elif rrx2 >= 1 and rrx2 < 2:
					ball2_dirx,ball2_diry=1,1						
				elif rrx2 >= 2 and rrx2 < 3:
					ball2_dirx,ball2_diry=1.13,0.85
				elif rrx2 >= 3 and rrx2 < 4:
					ball2_dirx,ball2_diry=-1.13,0.85
				elif rrx2 >= 4 and rrx2 < 5:
					ball2_dirx,ball2_diry=-1,1
				elif rrx2 >= 5 and rrx2 <= 6:
					ball2_dirx,ball2_diry=-1.22,0.71
			#------------------RANDOM_REFLECTION-----------------------------------#
		#-----------------------------球2撞到上方的邊緣時END-----------------------------#
		#-----------------------------球2撞到下方的邊緣時BEGIN---------------------------#
		if(ball2y>=screen_height-ball2_r)and (ball2_diry > 0):
			if ran_reflect%2 == 0:
				ball2_diry=-ball2_diry
			#------------------RANDOM_REFLECTION-----------------------------------#
			if ran_reflect%2 == 1:
				rrx2 = 6*random.random()
				if rrx2 >= 0 and rrx2 < 1:
					ball2_dirx,ball2_diry=1.22,-0.71
				elif rrx2 >= 1 and rrx2 < 2:
					ball2_dirx,ball2_diry=1,-1						
				elif rrx2 >= 2 and rrx2 < 3:
					ball2_dirx,ball2_diry=1.13,-0.85
				elif rrx2 >= 3 and rrx2 < 4:
					ball2_dirx,ball2_diry=-1.13,-0.85
				elif rrx2 >= 4 and rrx2 < 5:
					ball2_dirx,ball2_diry=-1,-1
				elif rrx2 >= 5 and rrx2 <= 6:
					ball2_dirx,ball2_diry=-1.22,-0.71
			#------------------RANDOM_REFLECTION-----------------------------------#
		#-----------------------------球2撞到下方的邊緣時END-----------------------------#
		#-----------------------------球3撞到上方的邊緣時BEGIN---------------------------#
		if(ball3y<ball3_r)and ball3_diry < 0 :
			if ran_reflect%2 == 0:
				ball3_diry=-ball3_diry
			#------------------RANDOM_REFLECTION-----------------------------------#
			if ran_reflect%2 == 1:
				rrx2 = 6*random.random()
				if rrx2 >= 0 and rrx2 < 1:
					ball3_dirx,ball3_diry=1.22,0.71
				elif rrx2 >= 1 and rrx2 < 2:
					ball3_dirx,ball3_diry=1,1						
				elif rrx2 >= 2 and rrx2 < 3:
					ball3_dirx,ball3_diry=1.13,0.85
				elif rrx2 >= 3 and rrx2 < 4:
					ball3_dirx,ball3_diry=-1.13,0.85
				elif rrx2 >= 4 and rrx2 < 5:
					ball3_dirx,ball3_diry=-1,1
				elif rrx2 >= 5 and rrx2 <= 6:
					ball3_dirx,ball3_diry=-1.22,0.71
			#------------------RANDOM_REFLECTION-----------------------------------#
		#-----------------------------球2撞到上方的邊緣時END-----------------------------#
		#-----------------------------球3撞到下方的邊緣時BEGIN---------------------------#
		if(ball3y>=screen_height-ball3_r)and (ball3_diry > 0):
			if ran_reflect%2 == 0:
				ball3_diry=-ball3_diry
			#------------------RANDOM_REFLECTION-----------------------------------#
			if ran_reflect%2 == 1:
				rrx2 = 6*random.random()
				if rrx2 >= 0 and rrx2 < 1:
					ball3_dirx,ball3_diry=1.22,-0.71
				elif rrx2 >= 1 and rrx2 < 2:
					ball3_dirx,ball3_diry=1,-1						
				elif rrx2 >= 2 and rrx2 < 3:
					ball3_dirx,ball3_diry=1.13,-0.85
				elif rrx2 >= 3 and rrx2 < 4:
					ball3_dirx,ball3_diry=-1.13,-0.85
				elif rrx2 >= 4 and rrx2 < 5:
					ball3_dirx,ball3_diry=-1,-1
				elif rrx2 >= 5 and rrx2 <= 6:
					ball3_dirx,ball3_diry=-1.22,-0.71
			#------------------RANDOM_REFLECTION-----------------------------------#
		#-----------------------------球2撞到下方的邊緣時END-----------------------------#
		if((bar_diry1<0)and(bar_y1>bar_half_length))or((bar_diry1>0)and(bar_y1<screen_height-bar_half_length)):
			bar_y1+=seconds*bar_diry1*bar_speed
		if((bar_diry2<0)and(bar_y2>bar_half_length))or((bar_diry2>0)and(bar_y2<screen_height-bar_half_length)):
			bar_y2+=seconds*bar_diry2*bar2_speed
		#-----------------------------球1撞到左方(右方)棒子時BEGIN-----------------------#
		if (ballx <= bar_x1+ball_r) and (ballx >= bar_x1-bar_width ) and (bally>=bar_y1-(bar_half_length+ball_r)) and (bally<=bar_y1+(bar_half_length+ball_r))and (ball_dirx<0) and ball == 1:
			catchscore += catchballscore
			pointchange = catchballscore
			catchballscore += 1
			if accelball == 1:	
				accelball = 2
			if ran_reflect%2 == 0:
				ball_dirx= -ball_dirx
			#------------------RANDOM_REFLECTION-----------------------------------#
			if ran_reflect%2 == 1:
				rrx1 = 6*random.random()
				if rrx1 >= 0 and rrx1 < 1:
					ball_dirx,ball_diry=1.22,-0.71
				elif rrx1 >= 1 and rrx1 < 2:
					ball_dirx,ball_diry=1,-1						
				elif rrx1 >= 2 and rrx1 < 3:
					ball_dirx,ball_diry=1.13,-0.85
				elif rrx1 >= 3 and rrx1 < 4:
					ball_dirx,ball_diry=1.13,0.85
				elif rrx1 >= 4 and rrx1 < 5:
					ball_dirx,ball_diry=1,1
				elif rrx1 >= 5 and rrx1 <= 6:
					ball_dirx,ball_diry=1.22,0.71
			#------------------RANDOM_REFLECTION-----------------------------------#
			if (sound%2) == 1:
				sound1.play()
		#--------------------------------Survival_2P----------------------------------------#
		if ((ballx <= bar_x2+ball_r) and (ballx >= bar_x2-bar_width) and (bally>=bar_y2-(bar_half_length+ball_r)) and (bally<=bar_y2+(bar_half_length+ball_r)) and (ball_dirx<0)) and (mode == 6) and ball == 1:
			catchscore += catchballscore
			pointchange = catchballscore
			catchballscore += 1
			if accelball == 1:	
				accelball = 2
			if ran_reflect%2 == 0:
				ball_dirx= -ball_dirx
			#------------------RANDOM_REFLECTION-----------------------------------#
			if ran_reflect%2 == 1:
				rrx1 = 6*random.random()
				if rrx1 >= 0 and rrx1 < 1:
					ball_dirx,ball_diry=1.22,-0.71
				elif rrx1 >= 1 and rrx1 < 2:
					ball_dirx,ball_diry=1,-1						
				elif rrx1 >= 2 and rrx1 < 3:
					ball_dirx,ball_diry=1.13,-0.85
				elif rrx1 >= 3 and rrx1 < 4:
					ball_dirx,ball_diry=1.13,0.85
				elif rrx1 >= 4 and rrx1 < 5:
					ball_dirx,ball_diry=1,1
				elif rrx1 >= 5 and rrx1 <= 6:
					ball_dirx,ball_diry=1.22,0.71
			#------------------RANDOM_REFLECTION-----------------------------------#
			if (sound%2) == 1:
				sound1.play()
		#-----------------------------球1撞到左方(右方)棒子時END-------------------------#
		#-----------------------------球2撞到左方(右方)棒子時BEGIN-----------------------#
		if (ball2x <= bar_x1+ball2_r) and (ball2x >= bar_x1-bar_width ) and (ball2y>=bar_y1-(bar_half_length+ball2_r)) and (ball2y<=bar_y1+(bar_half_length+ball2_r))and (ball2_dirx<0) and ball2 == 1:
			catchscore += catchball2score
			pointchange = catchball2score
			catchball2score += 1
			if accelball2 == 1:	
				accelball2 = 2
			if ran_reflect%2 == 0:
				ball2_dirx=-ball2_dirx
			#------------------RANDOM_REFLECTION-----------------------------------#
			if ran_reflect%2 == 1:
				rrx2 = 6*random.random()
				if rrx2 >= 0 and rrx2 < 1:
					ball2_dirx,ball2_diry=1.22,0.71
				elif rrx2 >= 1 and rrx2 < 2:
					ball2_dirx,ball2_diry=1,1						
				elif rrx2 >= 2 and rrx2 < 3:
					ball2_dirx,ball2_diry=1.13,0.85
				elif rrx2 >= 3 and rrx2 < 4:
					ball2_dirx,ball2_diry=1.13,-0.85
				elif rrx2 >= 4 and rrx2 < 5:
					ball2_dirx,ball2_diry=1,-1
				elif rrx2 >= 5 and rrx2 <= 6:
					ball2_dirx,ball2_diry=1.22,-0.71
			#------------------RANDOM_REFLECTION-----------------------------------#
			if (sound%2) == 1:
				sound1.play()
		if ((ball2x <= bar_x2+ball2_r) and (ball2x >= bar_x2-bar_width) and (ball2y>=bar_y2-(bar_half_length+ball2_r)) and (ball2y<=bar_y2+(bar_half_length+ball2_r)) and (ball2_dirx<0) and ball2 == 1) and mode == 6:
			catchscore += catchball2score
			pointchange = catchball2score
			catchball2score += 1
			if accelball2 == 1:	
				accelball2 = 2
			if ran_reflect%2 == 0:
				ball2_dirx=-ball2_dirx
			#------------------RANDOM_REFLECTION-----------------------------------#
			if ran_reflect%2 == 1:
				rrx2 = 6*random.random()
				if rrx2 >= 0 and rrx2 < 1:
					ball2_dirx,ball2_diry=1.22,0.71
				elif rrx2 >= 1 and rrx2 < 2:
					ball2_dirx,ball2_diry=1,1						
				elif rrx2 >= 2 and rrx2 < 3:
					ball2_dirx,ball2_diry=1.13,0.85
				elif rrx2 >= 3 and rrx2 < 4:
					ball2_dirx,ball2_diry=1.13,-0.85
				elif rrx2 >= 4 and rrx2 < 5:
					ball2_dirx,ball2_diry=1,-1
				elif rrx2 >= 5 and rrx2 <= 6:
					ball2_dirx,ball2_diry=1.22,-0.71
			#------------------RANDOM_REFLECTION-----------------------------------#
			if (sound%2) == 1:
				sound1.play()
		#-----------------------------球2撞到左方(右方)棒子時END-------------------------#
		#-----------------------------球3撞到左方(右方)棒子時BEGIN-----------------------#
		if (ball3x <= bar_x1+ball3_r) and (ball3x >= bar_x1-bar_width ) and (ball3y>=bar_y1-(bar_half_length+ball3_r)) and (ball3y<=bar_y1+(bar_half_length+ball3_r))and (ball3_dirx<0) and ball3 == 1:
			catchscore += catchball3score
			pointchange = catchball3score
			catchball3score += 1
			if accelball3 == 1:	
				accelball3 = 2
			if ran_reflect%2 == 0:
				ball3_dirx=-ball3_dirx
			#------------------RANDOM_REFLECTION-----------------------------------#
			if ran_reflect%2 == 1:
				rrx2 = 6*random.random()
				if rrx2 >= 0 and rrx2 < 1:
					ball3_dirx,ball3_diry=1.22,0.71
				elif rrx2 >= 1 and rrx2 < 2:
					ball3_dirx,ball3_diry=1,1						
				elif rrx2 >= 2 and rrx2 < 3:
					ball3_dirx,ball3_diry=1.13,0.85
				elif rrx2 >= 3 and rrx2 < 4:
					ball3_dirx,ball3_diry=1.13,-0.85
				elif rrx2 >= 4 and rrx2 < 5:
					ball3_dirx,ball3_diry=1,-1
				elif rrx2 >= 5 and rrx2 <= 6:
					ball3_dirx,ball3_diry=1.22,-0.71
			#------------------RANDOM_REFLECTION-----------------------------------#
			if (sound%2) == 1:
				sound1.play()
		if ((ball3x <= bar_x2+ball3_r) and (ball3x >= bar_x2-bar_width) and (ball3y>=bar_y2-(bar_half_length+ball3_r)) and (ball3y<=bar_y2+(bar_half_length+ball3_r)) and (ball3_dirx<0) and ball3 == 1) and mode == 6:
			catchscore += catchball3score
			pointchange = catchball3score
			catchball3score += 1
			if accelball3 == 1:	
				accelball3 = 2
			if ran_reflect%2 == 0:
				ball3_dirx=-ball3_dirx
			#------------------RANDOM_REFLECTION-----------------------------------#
			if ran_reflect%2 == 1:
				rrx2 = 6*random.random()
				if rrx2 >= 0 and rrx2 < 1:
					ball3_dirx,ball3_diry=1.22,0.71
				elif rrx2 >= 1 and rrx2 < 2:
					ball3_dirx,ball3_diry=1,1						
				elif rrx2 >= 2 and rrx2 < 3:
					ball3_dirx,ball3_diry=1.13,0.85
				elif rrx2 >= 3 and rrx2 < 4:
					ball3_dirx,ball3_diry=1.13,-0.85
				elif rrx2 >= 4 and rrx2 < 5:
					ball3_dirx,ball3_diry=1,-1
				elif rrx2 >= 5 and rrx2 <= 6:
					ball3_dirx,ball3_diry=1.22,-0.71
			#------------------RANDOM_REFLECTION-----------------------------------#
			if (sound%2) == 1:
				sound1.play()
		#-----------------------------球2撞到左方(右方)棒子時END-------------------------#
		#=============================計算球和棒子的新位置 END=============================#
		#===================================遊戲畫面BEGIN==================================#
		#---------------------------Laser------------------------------------#
		if lasermode%2 == 0:
			screen.blit(laser_50_dark,(245,5))
		if lasermode%2 == 1:
			screen.blit(laser_50,(245,5))
			if gametimer >= 2:
				if laser == 0:
					laserresttime = 0
					laserouttime = 0
					laser_ran = random.random()
					if laser_ran <= 0.5:
						laser_y = 200*random.random() + 80 #50-150   320  -490-590#
					if laser_ran > 0.5:
						laser_y = 200*fabs(random.random()-0.5) + 460
					lasertime = gameseconds
					laser = 1
				if laser == 1:
					pygame.draw.line(screen, (255,0,0), (480,laser_y), (480,laser_y+1), 960)
					lasercountdown = 3-int((gameseconds - lasertime)/1000)
					screen.blit(pygame.font.SysFont('Times New Roman', 40).render("%d"%(lasercountdown), True, (250, 250, 250)), (262, 8))
					if (gameseconds - lasertime) >= 3000:
						laserouttime = gameseconds
						laser = 2
				if laser == 2:
					lasertime = 0
					pygame.draw.line(screen, (255,0,0), (480,laser_y-20), (480,laser_y+20), 960)
					if (bar_y1 + 40 >= laser_y - 20 and bar_y1 - 40 <= laser_y - 20) or (bar_y1 - 40 <= laser_y + 20 and bar_y1 + 40 >= laser_y + 20):
						if laserminus1 == 0:
							catchscore -= 5
							pointchange = -5
							laserminus1 = 1
					if ((bar_y2 + 40 >= laser_y - 20 and bar_y2 - 40 <= laser_y - 20) or (bar_y2 - 40 <= laser_y + 20 and bar_y2 + 40 >= laser_y + 20)) and mode == 6:
						if laserminus2 == 0:
							catchscore -= 5
							pointchange = -5
							laserminus2 = 1
					if (gameseconds - laserouttime) >= 800:
						laserresttime = gameseconds
						laser = 3
				if laser == 3 and (gameseconds - laserresttime) >= 4000:
					laserminus1,laserminus2 = 0,0
					laser = 0
		#-------------------------------------------------------------------#
		#---------------------------Acceleration----------------------------#
		if acceleration%2 == 0:
			accelball,accelball2,accelball3 = 0,0,0
			screen.blit(accel_50_dark,(300,5))
		if acceleration%2 == 1:
			screen.blit(accel_50,(300,5))
			pygame.draw.line(screen, (255,255,0), (mid_width,accelboxy), (mid_width,accelboxy+100), 150)
			if acceldir == 1:
				pygame.draw.line(screen, (0,255,0), (mid_width+15-75,accelboxy+10), (mid_width+45-75,accelboxy+50), 10)
				pygame.draw.line(screen, (0,255,0), (mid_width+15-75,accelboxy+90), (mid_width+45-75,accelboxy+50), 10)
				pygame.draw.line(screen, (0,255,0), (mid_width+45-75,accelboxy+10), (mid_width+75-75,accelboxy+50), 10)
				pygame.draw.line(screen, (0,255,0), (mid_width+45-75,accelboxy+90), (mid_width+75-75,accelboxy+50), 10)
				pygame.draw.line(screen, (0,255,0), (mid_width+75-75,accelboxy+10), (mid_width+105-75,accelboxy+50), 10)
				pygame.draw.line(screen, (0,255,0), (mid_width+75-75,accelboxy+90), (mid_width+105-75,accelboxy+50), 10)
				pygame.draw.line(screen, (0,255,0), (mid_width+105-75,accelboxy+10), (mid_width+135-75,accelboxy+50), 10)
				pygame.draw.line(screen, (0,255,0), (mid_width+105-75,accelboxy+90), (mid_width+135-75,accelboxy+50), 10)
			if acceldir == -1:
				pygame.draw.line(screen, (0,255,0), (mid_width+45-75,accelboxy+10), (mid_width+15-75,accelboxy+50), 10)
				pygame.draw.line(screen, (0,255,0), (mid_width+45-75,accelboxy+90), (mid_width+15-75,accelboxy+50), 10)
				pygame.draw.line(screen, (0,255,0), (mid_width+75-75,accelboxy+10), (mid_width+45-75,accelboxy+50), 10)
				pygame.draw.line(screen, (0,255,0), (mid_width+75-75,accelboxy+90), (mid_width+45-75,accelboxy+50), 10)
				pygame.draw.line(screen, (0,255,0), (mid_width+105-75,accelboxy+10), (mid_width+75-75,accelboxy+50), 10)
				pygame.draw.line(screen, (0,255,0), (mid_width+105-75,accelboxy+90), (mid_width+75-75,accelboxy+50), 10)
				pygame.draw.line(screen, (0,255,0), (mid_width+135-75,accelboxy+10), (mid_width+105-75,accelboxy+50), 10)
				pygame.draw.line(screen, (0,255,0), (mid_width+135-75,accelboxy+90), (mid_width+105-75,accelboxy+50), 10)
			if ballx <= mid_width+75  and ballx >= mid_width-75 and bally>=accelboxy and bally<= accelboxy+100 and accelball == 0:
				ball_speedx0 = ball_speedx
				ball_speedy0 = ball_speedy
				ball_speedx,ball_speedy = ball_speedx*accelballspeed,ball_speedy*accelballspeed
				accelboxy=screen_height*39/64*random.random()+100
				if ball_dirx > 0:
					acceldir = 1
				if ball_dirx < 0:
					acceldir = -1
				accelball = 1
			if accelball == 2:
				ball_speedx,ball_speedy = ball_speedx0,ball_speedy0
				accelball = 0
			if ball2x <= mid_width+75  and ball2x >= mid_width-75 and ball2y>=accelboxy and ball2y<= accelboxy+100 and accelball2 == 0:
				ball2_speedx0 = ball2_speedx
				ball2_speedy0 = ball2_speedy
				ball2_speedx,ball2_speedy = ball2_speedx*accelballspeed,ball2_speedy*accelballspeed
				accelboxy=screen_height*39/64*random.random()+100
				if ball2_dirx > 0:
					acceldir = 1
				if ball2_dirx < 0:
					acceldir = -1
				accelball2 = 1
			if accelball2 == 2:
				ball2_speedx,ball2_speedy = ball2_speedx0,ball2_speedy0
				accelball2 = 0
			if ball3x <= mid_width+75  and ball3x >= mid_width-75 and ball3y>=accelboxy and ball3y<= accelboxy+100 and accelball3 == 0:
				ball3_speedx0 = ball3_speedx
				ball3_speedy0 = ball3_speedy
				ball3_speedx,ball3_speedy = ball3_speedx*accelballspeed,ball3_speedy*accelballspeed
				accelboxy=screen_height*39/64*random.random()+100
				if ball3_dirx > 0:
					acceldir = 1
				if ball3_dirx < 0:
					acceldir = -1
				accelball3 = 1
			if accelball3 == 2:
				ball3_speedx,ball3_speedy = ball3_speedx0,ball3_speedy0
				accelball3 = 0
			if (invisibility%2 == 0) or ( invisibility%2 == 1 and  ((ballx < 0.6*mid_width or ballx > 1.4*mid_width) or (ballx > 0.99*mid_width and ballx < 1.01*mid_width) or accelball == 1)):
				if accelball == 1 and ball == 1:
					pygame.draw.circle(screen, (204,0,204), (int(ballx),int(bally)), ball_r,0)
				if accelball == 0 and ball == 1:
					pygame.draw.circle(screen, (204,255,255), (int(ballx),int(bally)), ball_r,0)
			if (invisibility%2 == 0) or ( invisibility%2 == 1 and  ((ball2x < 0.6*mid_width or ball2x > 1.4*mid_width) or (ball2x > 0.99*mid_width and ball2x < 1.01*mid_width) or accelball2 == 1)):
				if accelball2 == 1 and ball2 == 1:
					pygame.draw.circle(screen, (255,153,0), (int(ball2x),int(ball2y)), ball2_r,0)			
				if accelball2 == 0 and ball2 == 1:
					pygame.draw.circle(screen, (255,153,153), (int(ball2x),int(ball2y)), ball2_r,0)
			if (invisibility%2 == 0) or ( invisibility%2 == 1 and ((ball3x < 0.6*mid_width or ball3x > 1.4*mid_width) or (ball3x > 0.99*mid_width and ball3x < 1.01*mid_width) or accelball3 == 1)):
				if accelball3 == 1 and ball3 == 1:
					pygame.draw.circle(screen, (153,51,0), (int(ball3x),int(ball3y)), ball3_r,0)			
				if accelball3 == 0 and ball3 == 1:
					pygame.draw.circle(screen, (103,255,102), (int(ball3x),int(ball3y)), ball3_r,0)
		#-------------------------------------------------------------------#
		#---------------------------Curve_Ball------------------------------#
		if curve_ball%2 == 0:
			screen.blit(vibrate_50_dark,(610,5))
		if curve_ball%2 == 1:
			screen.blit(vibrate_50,(610,5))
			if (gameseconds)%200 <= 5 and curve == 0:
				ball_diry = -ball_diry
				ball2_diry = -ball2_diry
				ball3_diry = -ball3_diry
				curve = 1
			if (gameseconds)%200 >= 50 and (gameseconds)%200 <= 60:
				curve = 0
		#-------------------------------------------------------------------#
		#---------------------------Wormhole--------------------------------#
		if wormhole%2 == 0:
			screen.blit(wh_50_dark,(665,5))
		if wormhole%2 == 1:
			screen.blit(wh_50,(665,5))
			pygame.draw.circle(screen, (30,30,30), (int(0.5*mid_width),int(why1)), 50,0)
			screen.blit(blackhole_70,(int(0.5*mid_width)-35,int(why1)-35))
			pygame.draw.circle(screen, (30,30,30), (int(1.5*mid_width),int(why2)), 50,0)
			screen.blit(blackhole_70,(int(1.5*mid_width)-35,int(why2)-35))
			disblwh1 = (ballx-int(0.5*mid_width))*(ballx-int(0.5*mid_width)) + (bally-int(why1))*(bally-int(why1))
			disblwh2 = (ballx-int(1.5*mid_width))*(ballx-int(1.5*mid_width)) + (bally-int(why2))*(bally-int(why2))
			disbl2wh1 = (ball2x-int(0.5*mid_width))*(ball2x-int(0.5*mid_width)) + (ball2y-int(why1))*(ball2y-int(why1))
			disbl2wh2 = (ball2x-int(1.5*mid_width))*(ball2x-int(1.5*mid_width)) + (ball2y-int(why2))*(ball2y-int(why2))
			disbl3wh1 = (ball3x-int(0.5*mid_width))*(ball3x-int(0.5*mid_width)) + (ball3y-int(why1))*(ball3y-int(why1))
			disbl3wh2 = (ball3x-int(1.5*mid_width))*(ball3x-int(1.5*mid_width)) + (ball3y-int(why2))*(ball3y-int(why2))
			if disblwh2 > 2500 and disblwh1 > 2500:
				blwh = 0
			if disblwh1 <= 2500 and blwh == 0:
				why2=screen_height*44/64*random.random()+100
				ballx,bally = int(1.5*mid_width),int(why2)
				blwh = 1
			if disblwh2 <= 2500 and blwh == 0:
				why1=screen_height*44/64*random.random()+100
				ballx,bally = int(0.5*mid_width),int(why1)
				blwh = 1
			if disbl2wh2 > 2500 and disbl2wh1 > 2500:
				bl2wh = 0
			if disbl2wh1 <= 2500 and bl2wh == 0:
				why2=screen_height*44/64*random.random()+100
				ball2x,ball2y = int(1.5*mid_width),int(why2)
				bl2wh = 1
			if disbl2wh2 <= 2500 and bl2wh == 0:
				why1=screen_height*44/64*random.random()+100
				ball2x,ball2y = int(0.5*mid_width),int(why1)
				bl2wh = 1
			if disbl3wh2 > 2500 and disbl3wh1 > 2500:
				bl3wh = 0
			if disbl3wh1 <= 2500 and bl3wh == 0:
				why2=screen_height*44/64*random.random()+100
				ball3x,ball3y = int(1.5*mid_width),int(why2)
				bl3wh = 1
			if disbl3wh2 <= 2500 and bl3wh == 0:
				why1=screen_height*44/64*random.random()+100
				ball3x,ball3y = int(0.5*mid_width),int(why1)
				bl3wh = 1
		#-------------------------------------------------------------------#
		#---------------------------Invisibility1---------------------------#
		if invisibility%2 == 0:
			screen.blit(invis_50_dark,(355,5))
		if invisibility%2 == 1:
			screen.blit(invis_50,(355,5))
			pygame.draw.line(screen, (200,200,200), (0.6*mid_width,60), (0.6*mid_width,640), 1)
			pygame.draw.line(screen, (200,200,200), (1.4*mid_width,60), (1.4*mid_width,640), 1)
		#-------------------------------------------------------------------#
		pygame.draw.line(screen, (171,171,171), (480,60), (480,61), 960)
		screen.blit(pygame.font.SysFont('Times New Roman', 20).render("%d"%(remaintime), True, (255, 255, 255)), (467, 10))
		pygame.draw.line(screen, (0,0,255), (bar_x1,bar_y1-bar_half_length), (bar_x1,bar_y1+bar_half_length), bar_width)
		if mode == 6: 
			pygame.draw.line(screen, (255,0,0), (bar_x2,bar_y2-bar_half_length), (bar_x2,bar_y2+bar_half_length), bar_width)	
		screen.blit(pygame.font.SysFont('Times New Roman', 35).render("Score : %d"%(catchscore), True, (255, 255, 255)), (750,10))
		if ball == 1:
			pygame.draw.circle(screen, (204,255,255), (50,30),20,0)
			if catchballscore < 10:
				screen.blit(pygame.font.SysFont('Times New Roman', 30).render("%d"%(catchballscore), True, (0, 0, 102)), (43, 13))
			if catchballscore >= 10:
				screen.blit(pygame.font.SysFont('Times New Roman', 30).render("%d"%(catchballscore), True, (0, 0, 102)), (35, 13))
		if ball == 0:
			screen.blit(pygame.font.SysFont('Times New Roman', 40).render("%d"%(ballcountdown), True, (204, 255, 255)), (38, 8))
		if ball2 == 1:
			pygame.draw.circle(screen, (255,153,153), (110,30), 20,0)	
			if catchball2score < 10:
				screen.blit(pygame.font.SysFont('Times New Roman', 30).render("%d"%(catchball2score), True, (102, 0, 0)), (103, 13))
			if catchball2score >= 10:
				screen.blit(pygame.font.SysFont('Times New Roman', 30).render("%d"%(catchball2score), True, (102, 0, 0)), (95, 13))
		if ball2 == 0 and gameseconds > 15000:
			screen.blit(pygame.font.SysFont('Times New Roman', 40).render("%d"%(ball2countdown), True, (255,153,153)), (98, 8))
		if ball3 == 1:
			pygame.draw.circle(screen, (102,255,102), (170,30), 20,0)	
			if catchball3score < 10:
				screen.blit(pygame.font.SysFont('Times New Roman', 30).render("%d"%(catchball3score), True, (0, 102, 0)), (163, 13))
			if catchball3score >= 10:
				screen.blit(pygame.font.SysFont('Times New Roman', 30).render("%d"%(catchball3score), True, (0, 102, 0)), (155, 13))
		if ball3 == 0 and gameseconds > 30000:
			screen.blit(pygame.font.SysFont('Times New Roman', 40).render("%d"%(ball3countdown), True, (102,255,102)), (158, 8))
		if pointchange > 0:
			screen.blit(pygame.font.SysFont('Times New Roman', 30).render("+%d"%(pointchange), True, (0, 255, 0)), (910,13))
		if pointchange < 0:
			screen.blit(pygame.font.SysFont('Times New Roman', 30).render("%d"%(pointchange), True, (255, 0, 0)), (910,13))
		#---------------------------Invisibility2----------------------------#
		if (invisibility%2 == 0) or ( invisibility%2 == 1 and  ((ballx < 0.6*mid_width or ballx > 1.4*mid_width) or (ballx > 0.99*mid_width and ballx < 1.01*mid_width) )):
			if accelball == 0 and ball == 1:
				pygame.draw.circle(screen, (204,255,255), (int(ballx),int(bally)), ball_r,0)
		if (invisibility%2 == 0) or ( invisibility%2 == 1 and  ((ball2x < 0.6*mid_width or ball2x > 1.4*mid_width) or (ball2x > 0.99*mid_width and ball2x < 1.01*mid_width) )):
			if accelball2 == 0 and ball2 == 1:
				pygame.draw.circle(screen, (255,153,153), (int(ball2x),int(ball2y)), ball2_r,0)	
		if (invisibility%2 == 0) or ( invisibility%2 == 1 and  ((ball3x < 0.6*mid_width or ball3x > 1.4*mid_width) or (ball3x > 0.99*mid_width and ball3x < 1.01*mid_width) )):
			if accelball3 == 0 and ball3 == 1:
				pygame.draw.circle(screen, (102,255,102), (int(ball3x),int(ball3y)), ball3_r,0)	
		#-------------------------------------------------------------------#
		#-------------testing----------------#	
		#screen.blit(pygame.font.SysFont('Times New Roman', 30).render("%d"%(ball3x), True, (255, 0, 0)), (300,200))	
		#screen.blit(pygame.font.SysFont('Times New Roman', 30).render("%d"%(accelball3), True, (255, 0, 0)), (300,300))	
		pygame.display.update()
		#===================================遊戲畫面END====================================#
#=================================================================================================#	
	if gamestate == "setting_catch":
		screen.blit(background,(0,0))
		cb1,cb2,cb3 = 40,40,30
		if cb == 1:
			cb1 = 50
			cbcircley =145
			drawlefttri(340,185,30,80)
			drawrighttri(545,185,30,80)
		elif cb == 2:
			cb2 = 50
			cbcircley =285
		elif cb == 3:
			cb3 = 40
			cbcircley =585
		screen.blit(pygame.font.SysFont('Times New Roman', 80).render("CatchBall", True, (171,171,171)), (30,15))
		screen.blit(pygame.font.SysFont('Times New Roman', cb1).render("Control", True, (255, 255, 255)), (80, 120))
		screen.blit(pygame.font.SysFont('Times New Roman', cb2).render("Highscore_List", True, (255, 255, 255)), (80, 260))
		screen.blit(pygame.font.SysFont('Times New Roman', 40).render("1P_Highest_Score  :  %d"%(catch_1p_top5[1]), True, (171 ,171 ,171)), (80, 340))
		screen.blit(pygame.font.SysFont('Times New Roman', 40).render("2P_Highest_Score  :  %d"%(catch_2p_top5[1]), True, (171 ,171 ,171)), (80, 400))
		screen.blit(pygame.font.SysFont('Times New Roman', cb3).render("Confirm", True, (255, 255, 255)), (80, 560))
		pygame.draw.circle(screen, (255,255,255), (60,cbcircley),6,0)
		#-------------------------------------------Control----------------------------------------------------#
		if (control%2) == 1:
			screen.blit(pygame.font.SysFont('Times New Roman', 40).render("P1 : ", True, (255, 255, 255)), (350, 125))
			screen.blit(control_w,(425,120))
			screen.blit(control_s,(485,120))
			screen.blit(pygame.font.SysFont('Times New Roman', 40).render("P2 : ", True, (255, 255, 255)), (350, 205))
			screen.blit(control_up,(425,200))
			screen.blit(control_down,(485,200))
		elif (control%2) == 0:
			screen.blit(pygame.font.SysFont('Times New Roman', 40).render("P1 : ", True, (255, 255, 255)), (350, 125))
			screen.blit(control_w,(425,200))
			screen.blit(control_s,(485,200))
			screen.blit(pygame.font.SysFont('Times New Roman', 40).render("P2 : ", True, (255, 255, 255)), (350, 205))
			screen.blit(control_up,(425,120))
			screen.blit(control_down,(485,120))
		#------------------------------------------------------------------------------------------------------#
		pygame.display.update()
		for events in pygame.event.get():
			if events.type == pygame.KEYDOWN:	
				if events.key == pygame.K_ESCAPE:
					quit_game()
				elif events.key == pygame.K_SPACE:
					if cb == 3:
						survivalscore,catchscore = 0,0
						scorer = ""
						winner = ""
						score1,score2 = 0,0
						timeout = 0
						loadseconds=0
						loadtime=0
						loadpercentage = 0
						loadtimer = pygame.time.Clock()
						gamestate = "loading"
					if cb == 2:
						gamestate = "highscore"
				elif events.key == pygame.K_BACKSPACE:
					gamestate = 11
				elif events.key == pygame.K_TAB or events.key == pygame.K_s or events.key == pygame.K_DOWN:
					cb +=1
					if cb == 4:
						cb = 1
				elif events.key == pygame.K_w or events.key == pygame.K_UP :
					cb -=1	
					if cb == 0:
						cb = 3
				if cb == 1:
					if events.key == pygame.K_d or events.key == pygame.K_RIGHT:
						control += 1
					elif events.key == pygame.K_a or events.key == pygame.K_LEFT:
						control -= 1
#=================================================================================================#	
	if gamestate == "highscore":
		screen.blit(background,(0,0))
		screen.blit(pygame.font.SysFont('Times New Roman', 80).render("High Score List", True, (171,171,171)), (30,15))
		if mode == 3 or mode == 4:
			screen.blit(pygame.font.SysFont('Times New Roman', 50).render("Survival 1P", True, (255,255,255)), (200,140))
			screen.blit(pygame.font.SysFont('Times New Roman', 50).render("Survival 2P", True, (255,255,255)), (590,140))
		if mode == 5 or mode == 6:
			screen.blit(pygame.font.SysFont('Times New Roman', 50).render("CatchBall 1P", True, (255,255,255)), (185,140))
			screen.blit(pygame.font.SysFont('Times New Roman', 50).render("CatchBall 2P", True, (255,255,255)), (580,140))
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
		if mode == 3 or mode == 4:
			screen.blit(pygame.font.SysFont('Times New Roman', h[1]).render("%d"%(sur_1p_top5[1]), True, (255,255,255)), (290,240))
			screen.blit(pygame.font.SysFont('Times New Roman', h[2]).render("%d"%(sur_1p_top5[2]), True, (255,255,255)), (290,310))
			screen.blit(pygame.font.SysFont('Times New Roman', h[3]).render("%d"%(sur_1p_top5[3]), True, (255,255,255)), (290,380))
			screen.blit(pygame.font.SysFont('Times New Roman', h[4]).render("%d"%(sur_1p_top5[4]), True, (255,255,255)), (290,450))
			screen.blit(pygame.font.SysFont('Times New Roman', h[5]).render("%d"%(sur_1p_top5[5]), True, (255,255,255)), (290,520))
			screen.blit(pygame.font.SysFont('Times New Roman', h[6]).render("%d"%(sur_2p_top5[1]), True, (255,255,255)), (680,240))
			screen.blit(pygame.font.SysFont('Times New Roman', h[7]).render("%d"%(sur_2p_top5[2]), True, (255,255,255)), (680,310))
			screen.blit(pygame.font.SysFont('Times New Roman', h[8]).render("%d"%(sur_2p_top5[3]), True, (255,255,255)), (680,380))
			screen.blit(pygame.font.SysFont('Times New Roman', h[9]).render("%d"%(sur_2p_top5[4]), True, (255,255,255)), (680,450))
			screen.blit(pygame.font.SysFont('Times New Roman', h[10]).render("%d"%(sur_2p_top5[5]), True, (255,255,255)), (680,520))
			if mode == 3 and newhigh != 0:
				h[newhigh] = 50
				screen.blit(pygame.font.SysFont('Times New Roman', 50).render("%d"%(sur_1p_top5[newhigh]), True, (255,255,0)), (290,170+70*newhigh))
			if mode == 4 and newhigh != 0:
				h[newhigh+5] = 50
				screen.blit(pygame.font.SysFont('Times New Roman', 50).render("%d"%(sur_2p_top5[newhigh]), True, (255,255,0)), (680,170+70*newhigh))
		if mode == 5 or mode == 6:
			screen.blit(pygame.font.SysFont('Times New Roman', h[1]).render("%d"%(catch_1p_top5[1]), True, (255,255,255)), (290,240))
			screen.blit(pygame.font.SysFont('Times New Roman', h[2]).render("%d"%(catch_1p_top5[2]), True, (255,255,255)), (290,310))
			screen.blit(pygame.font.SysFont('Times New Roman', h[3]).render("%d"%(catch_1p_top5[3]), True, (255,255,255)), (290,380))
			screen.blit(pygame.font.SysFont('Times New Roman', h[4]).render("%d"%(catch_1p_top5[4]), True, (255,255,255)), (290,450))
			screen.blit(pygame.font.SysFont('Times New Roman', h[5]).render("%d"%(catch_1p_top5[5]), True, (255,255,255)), (290,520))
			screen.blit(pygame.font.SysFont('Times New Roman', h[6]).render("%d"%(catch_2p_top5[1]), True, (255,255,255)), (680,240))
			screen.blit(pygame.font.SysFont('Times New Roman', h[7]).render("%d"%(catch_2p_top5[2]), True, (255,255,255)), (680,310))
			screen.blit(pygame.font.SysFont('Times New Roman', h[8]).render("%d"%(catch_2p_top5[3]), True, (255,255,255)), (680,380))
			screen.blit(pygame.font.SysFont('Times New Roman', h[9]).render("%d"%(catch_2p_top5[4]), True, (255,255,255)), (680,450))
			screen.blit(pygame.font.SysFont('Times New Roman', h[10]).render("%d"%(catch_2p_top5[5]), True, (255,255,255)), (680,520))
			if mode == 5 and newhigh != 0:
				h[newhigh] = 50
				screen.blit(pygame.font.SysFont('Times New Roman', 50).render("%d"%(catch_1p_top5[newhigh]), True, (255,255,0)), (290,170+70*newhigh))
			if mode == 6 and newhigh != 0:
				h[newhigh+5] = 50
				screen.blit(pygame.font.SysFont('Times New Roman', 50).render("%d"%(catch_2p_top5[newhigh]), True, (255,255,0)), (680,170+70*newhigh))
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
						gamestate = 0
						temptgamestate = ""
					else:
						if mode == 3 or mode == 4:
							gamestate = "setting_survival"
						if mode == 5 or mode == 6:					
							gamestate = "setting_catch"

		