import pygame
import time

#메인 화면 버튼
class MainButton:
    def __init__(self, window, txt, x, y, width, height, txtChangeColor, actionScreenX, actionScreenY, Difficulty, action=None):
        mouse=pygame.mouse.get_pos()
        click=pygame.mouse.get_pressed()
        #마우스가 글 안에 들어왔을때
        if x+width > mouse[0] > x and y + height > mouse[1] > y:
            #색깔 변화해주고
            window.blit(txtChangeColor, (x, y))
            #action(연결된 함수)이 있고 클릭을 한다면
            if click[0] and action != None:
                if Difficulty == None:
                    time.sleep(1)
                    action()
                else:
                    time.sleep(1)
                    action(actionScreenX, actionScreenY, Difficulty)


        else:
            window.blit(txt, (x,y))