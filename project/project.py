#13464312 Siwei Fan
import pygame
import sys
from pygame.locals import *
import audio_sound
from sound_recording import Recorder

#Initialize the timing function
time_counts=0
timeStr = "00:00:00"
is_start = False
TIME_COUNT = pygame.USEREVENT +1

#Initialize the software interface
image = pygame.image.load("back.png")
image_rect = image.get_rect()

start_image = pygame.image.load("start.png")
start_image_rect = image.get_rect()
start_image_rect.left = 329
start_image_rect.top = 375

end_image = pygame.image.load("end.png")

height = 450
width = 1058
SIZE = (width, height)

pygame.init()
screen = pygame.display.set_mode((SIZE))
pygame.display.set_caption("Project")

def init_view():
    global screen
    screen.fill((45,45,45))
    if is_start:
        screen.blit(end_image,start_image_rect)
    else:
        screen.blit(start_image,start_image_rect)
    screen.blit(image,image_rect)

Font = pygame.font.SysFont("Trebuchet MS", 25)
timeFont = Font.render("Time: "+str(timeStr), True,(255,255,255))
timeFontR=timeFont.get_rect()
timeFontR.center = (529,400)

#Get timer font
def getTime():
    global timeFontR,timeFont,screen
    init_view()
    timeFont = Font.render("Time: "+str(timeStr), True,(255,255,255))
    screen.blit(timeFont,timeFontR)
    pygame.display.flip()
    

getTime()

rec = Recorder()
rec1 = Recorder(isMic=False)

clock = pygame.time.Clock()

while True:
    clock.tick(60)
    for event in pygame.event.get():

        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == TIME_COUNT:
            time_counts += 1

#Determine the mouse click status
        if event.type == MOUSEBUTTONDOWN and 329<=event.pos[0]<= 329 + 50 and 375<=event.pos[1]<= 375 + 50:
            if is_start:
                rec.stop()
                pygame.time.wait(100)
                rec1.stop()
                is_start = False
                pygame.time.set_timer(TIME_COUNT,0)
            else:
                rec.start()
                pygame.time.wait(100)
                rec1.start()
                time_counts = 0
                is_start = True
                pygame.time.set_timer(TIME_COUNT,1000)

        m,s = divmod(time_counts,60)
        h,m = divmod(m,60)
        timeStr = "%02d:%02d:%02d"%(h,m,s)
        getTime()
       

#Keyboard trigger piano
        if event.type == KEYDOWN:
            if event.key == K_a:
                audio_sound.A_Sound.play()
            
            if event.key == K_d:
                audio_sound.D_Sound.play()
            
            if event.key == K_e:
                audio_sound.E_Sound.play()

            if event.key == K_f:
                audio_sound.F_Sound.play()

            if event.key == K_g:
                audio_sound.G_Sound.play()
            
            if event.key == K_h:
                audio_sound.H_Sound.play()
            
            if event.key == K_j:
                audio_sound.J_Sound.play()
            
            if event.key == K_k:
                audio_sound.K_Sound.play()
            
            if event.key == K_l:
                audio_sound.L_Sound.play()
            
            if event.key == K_o:
                audio_sound.O_Sound.play()
            
            if event.key == K_p:
                audio_sound.P_Sound.play()

            if event.key == K_s:
                audio_sound.S_Sound.play()
            
            if event.key == K_t:
                audio_sound.T_Sound.play()
            
            if event.key == K_u:
                audio_sound.U_Sound.play()
            
            if event.key == K_w:
                audio_sound.W_Sound.play()
            
            if event.key == K_y:
                audio_sound.Y_Sound.play()
            
            if event.key == K_SEMICOLON:
                audio_sound.semicolon_Sound.play()

            if event.key == 39:
                audio_sound.comma_Sound.play()