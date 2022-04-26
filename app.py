#pip install pygame
import sys
import pygame
import random
import time
from mainScreenButton import MainButton
from gamePauseScreenButton import GamePauseButton

#전역 변수 #안써도 무방하지만 나중에 전역변수가 무엇이였는지 알아보기 어려워진다.
Pause = False

#게임 종료
def quitgame():
    pygame.quit()
    sys.exit()

#퍼즈 화면 종료
def unpause():
    global Pause #전역변수는 사용하는 곳마다 작성해줘야한다. 물론 다 같은 의미로 적용된다.
    Pause = False

#게임 실패/성공시 스크린
def GameEndScreen(window_X, window_Y, Difficulty, player_life, enemy_life, remain_time):
    pygame.init()
    clock = pygame.time.Clock()
    #RGB 색깔
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    BLUE = (0, 0, 255)

    #게임 실패/성공 화면 디스플레이
    window = pygame.display.set_mode((window_X, window_Y))

    if enemy_life <= 0:
        TitleScript = pygame.font.SysFont('malgungothic', 72).render('You Won', True, RED)
    elif player_life <= 0:
        TitleScript = pygame.font.SysFont('malgungothic', 72).render('You Loose', True, RED)
    elif remain_time <= 0:
        TitleScript = pygame.font.SysFont('malgungothic', 72).render('Time Exceeded', True, RED)

    #게임 실패/성공 화면 글 요소
    RestartLevelScript = pygame.font.SysFont('malgungothic', 36).render('Restart Level', True, RED)
    ReturnToMenuScript = pygame.font.SysFont('malgungothic', 36).render('Return To Menu', True, RED)
    ExitGameScript = pygame.font.SysFont('malgungothic', 36).render('Exit Game', True, RED)
    #게임 실패/성공 화면 글 Hover 요소
    RestartLevelScriptAni = pygame.font.SysFont('malgungothic', 36).render('Restart Level', True, BLUE)
    ReturnToMenuScriptAni = pygame.font.SysFont('malgungothic', 36).render('Return To Menu', True, BLUE)
    ExitGameScriptAni = pygame.font.SysFont('malgungothic', 36).render('Exit Game', True, BLUE)

    #화면 송출
    while True:
        for event in pygame.event.get():
            #탈출키
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        #게임 실패/성공 화면 배경화면
        window.fill(BLACK)
        #게임 실패/성공 화면 배경화면에 글 띄우기
        #ui/ux를 성공하면 다른 py파일을 만드는게 맞지만 기능 구현에 초점을 맞춰서 퍼즈화면꺼를 빌려오겠다.
        TitleText = window.blit(TitleScript, (window_X/2 - TitleScript.get_width()/2, window_Y/6 - TitleScript.get_height()/2))
        RestartLevelButton = GamePauseButton(window, RestartLevelScript, window_X/2 - RestartLevelScript.get_width()/2, (window_Y/6)*3 - RestartLevelScript.get_height()/2, RestartLevelScript.get_width(), RestartLevelScript.get_height(),
                                 RestartLevelScriptAni, window_X, window_Y, Difficulty, action=game_screen)
        ReturnToMenuButton = GamePauseButton(window, ReturnToMenuScript, window_X/2 - ReturnToMenuScript.get_width()/2, (window_Y/6)*4 - ReturnToMenuScript.get_height()/2, ReturnToMenuScript.get_width(), ReturnToMenuScript.get_height(),
                                 ReturnToMenuScriptAni, window_X, window_Y, None, action=main_screen)
        ExitGameButton = GamePauseButton(window, ExitGameScript, window_X/2 - ExitGameScript.get_width()/2, (window_Y/6)*5 - ExitGameScript.get_height()/2, ExitGameScript.get_width(), ExitGameScript.get_height(),
                                 ExitGameScriptAni, window_X, window_Y, None, action=quitgame)
        pygame.display.update()
        clock.tick(15)

#게임 일시정지(pause) 화면
def GamePauseScreen(window_X, window_Y, Difficulty):
    global Pause
    pygame.init()
    clock = pygame.time.Clock()
    #RGB 색깔
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    BLUE = (0, 0, 255)

    #퍼즈 화면 디스플레이
    window = pygame.display.set_mode((window_X, window_Y))

    #퍼즈 화면 글 요소
    TitleScript = pygame.font.SysFont('malgungothic', 72).render('Paused', True, RED)
    GoBackToGameScript = pygame.font.SysFont('malgungothic', 36).render('Go Back To Game', True, RED)
    RestartLevelScript = pygame.font.SysFont('malgungothic', 36).render('Restart Level', True, RED)
    ReturnToMenuScript = pygame.font.SysFont('malgungothic', 36).render('Return To Menu', True, RED)
    ExitGameScript = pygame.font.SysFont('malgungothic', 36).render('Exit Game', True, RED)
    #퍼즈 화면 글 Hover 요소
    GoBackToGameScriptAni = pygame.font.SysFont('malgungothic', 36).render('Go Back To Game', True, BLUE)
    RestartLevelScriptAni = pygame.font.SysFont('malgungothic', 36).render('Restart Level', True, BLUE)
    ReturnToMenuScriptAni = pygame.font.SysFont('malgungothic', 36).render('Return To Menu', True, BLUE)
    ExitGameScriptAni = pygame.font.SysFont('malgungothic', 36).render('Exit Game', True, BLUE)

    #메뉴 실행
    Pause = True
    #탈출키
    while Pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        #퍼즈 화면 배경화면
        window.fill(BLACK)
        #퍼즈 화면 배경화면에 글 띄우기
        TitleText = window.blit(TitleScript, (window_X/2 - TitleScript.get_width()/2, window_Y/6 - TitleScript.get_height()/2))
        GoBackToGameButton = GamePauseButton(window, GoBackToGameScript, window_X/2 - GoBackToGameScript.get_width()/2, (window_Y/6)*2 - GoBackToGameScript.get_height()/2, GoBackToGameScript.get_width(), GoBackToGameScript.get_height(),
                                 GoBackToGameScriptAni, window_X, window_Y, None, action=unpause)
        RestartLevelButton = GamePauseButton(window, RestartLevelScript, window_X/2 - RestartLevelScript.get_width()/2, (window_Y/6)*3 - RestartLevelScript.get_height()/2, RestartLevelScript.get_width(), RestartLevelScript.get_height(),
                                 RestartLevelScriptAni, window_X, window_Y, Difficulty, action=game_screen)
        ReturnToMenuButton = GamePauseButton(window, ReturnToMenuScript, window_X/2 - ReturnToMenuScript.get_width()/2, (window_Y/6)*4 - ReturnToMenuScript.get_height()/2, ReturnToMenuScript.get_width(), ReturnToMenuScript.get_height(),
                                 ReturnToMenuScriptAni, window_X, window_Y, None, action=main_screen)
        ExitGameButton = GamePauseButton(window, ExitGameScript, window_X/2 - ExitGameScript.get_width()/2, (window_Y/6)*5 - ExitGameScript.get_height()/2, ExitGameScript.get_width(), ExitGameScript.get_height(),
                                 ExitGameScriptAni, window_X, window_Y, None, action=quitgame)
        pygame.display.update()
        clock.tick(15)

#메뉴 화면
def main_screen(window_X, window_Y):
    pygame.init()
    clock = pygame.time.Clock()
    #RGB 색깔
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    BLUE = (0, 0, 255)

    # 게임 이름 설정
    pygame.display.set_caption('Robot Warfare')

    #난이도
    Easy = {"EnemyBulletSpeed": 100, "EnemyMotionSpeed": 300}
    Medium = {"EnemyBulletSpeed": 50, "EnemyMotionSpeed": 150}
    Hard = {"EnemyBulletSpeed": 25, "EnemyMotionSpeed": 75}

    #메뉴 화면 디스플레이
    window = pygame.display.set_mode((window_X, window_Y))

    #메뉴 화면 글 요소
    TitleScript = pygame.font.SysFont('malgungothic', 72).render('Robot Warfare', True, RED)
    EasyLevelScript = pygame.font.SysFont('malgungothic', 36).render('Easy', True, RED)
    MediumLevelScript = pygame.font.SysFont('malgungothic', 36).render('Medium', True, RED)
    HardLevelScript = pygame.font.SysFont('malgungothic', 36).render('Hard', True, RED)
    ExitScript = pygame.font.SysFont('malgungothic', 36).render('Exit', True, RED)
    #메뉴화면 글 Hover 요소
    EasyLevelScriptAni = pygame.font.SysFont('malgungothic', 36).render('Easy', True, BLUE)
    MediumLevelScriptAni = pygame.font.SysFont('malgungothic', 36).render('Medium', True, BLUE)
    HardLevelScriptAni = pygame.font.SysFont('malgungothic', 36).render('Hard', True, BLUE)
    ExitScriptAni = pygame.font.SysFont('malgungothic', 36).render('Exit', True, BLUE)

    #메뉴 실행
    menu = True
    #탈출키
    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        #메인 배경화면
        window.fill(BLACK)
        #메인 배경화면에 글 띄우기
        TitleText = window.blit(TitleScript, (window_X/2 - TitleScript.get_width()/2, window_Y/6 - TitleScript.get_height()/2))
        EasyLevelButton = MainButton(window, EasyLevelScript, window_X/2 - EasyLevelScript.get_width()/2, (window_Y/6)*2 - EasyLevelScript.get_height()/2, EasyLevelScript.get_width(), EasyLevelScript.get_height(),
                                 EasyLevelScriptAni, window_X, window_Y, Difficulty=Easy, action=game_screen)
        MediumLevelButton = MainButton(window, MediumLevelScript, window_X/2 - MediumLevelScript.get_width()/2, (window_Y/6)*3 - MediumLevelScript.get_height()/2, MediumLevelScript.get_width(), MediumLevelScript.get_height(),
                                 MediumLevelScriptAni, window_X, window_Y, Difficulty=Medium, action=game_screen)
        HardLevelButton = MainButton(window, HardLevelScript, window_X/2 - HardLevelScript.get_width()/2, (window_Y/6)*4 - HardLevelScript.get_height()/2, HardLevelScript.get_width(), HardLevelScript.get_height(),
                                 HardLevelScriptAni, window_X, window_Y, Difficulty=Hard, action=game_screen)
        ExitButton = MainButton(window, ExitScript, window_X/2 - ExitScript.get_width()/2, (window_Y/6)*5 - ExitScript.get_height()/2, ExitScript.get_width(), ExitScript.get_height(),
                                 ExitScriptAni, window_X, window_Y, None, action=quitgame)
        pygame.display.update()
        clock.tick(15)

def game_screen(window_X, window_Y, Difficulty):
    #게임 실행 초기화
    pygame.init()

    #게임 화면 설정
    # window_X
    # window_Y
    window = pygame.display.set_mode((window_X, window_Y))

    # 게임 이름 설정
    pygame.display.set_caption('Robot Warfare')

    #시간 추척 기능 #참고로 1밀리세컨 기준 #1초 = 1천 밀리세컨
    clock = pygame.time.Clock()

    #rgb #배경화면으로 이용
    BLACK = (0,0,0)
    RED = (255, 0, 0)
    
    #플레이어
    #플레이어 캐릭터
    player_character = pygame.image.load("script/img/solider_init.png") #기본 설정
    player_bullet = pygame.image.load("script/img/rpg.png")
    player_character_stand = pygame.image.load("script/img/solider_init.png") #추후 누웠을때 다시 일어나게 하기 위해
    player_character_layDown = pygame.image.load("script/img/solider_laydown.png") #누워있는 사진

    #플레이어 위치
    player_posX = 0
    player_posY = window_Y/2
    player_dy = 0
    player_life = 10
    
    #플레이어 총알 위치
    player_bullet_list = []

    #적 위치
    #적 캐릭터
    enemy_character = pygame.image.load("script/img/hornet.png")
    enemy_bullet = pygame.image.load("script/img/plasma.png")

    #적 위치
    enemy_posX = window_X - enemy_character.get_width()
    enemy_posY = window_Y/2
    enemy_life = 10

    #적 총알 위치
    enemy_bullet_list = []

    #플레이어, 적이 죽어 게임 종료
    game_over = False

    #적 Events 설정
    #적 상하 움직임 시간 설정
    enemy_move_time = Difficulty["EnemyMotionSpeed"]
    enemy_move_event = pygame.USEREVENT + 1
    pygame.time.set_timer(enemy_move_event, enemy_move_time)
    #적 총알 시간 설정
    enemy_shoot_time = Difficulty['EnemyBulletSpeed']
    enemy_shoot_event = pygame.USEREVENT + 2
    pygame.time.set_timer(enemy_shoot_event, enemy_shoot_time)

    #시간
    start_ticks = pygame.time.get_ticks()
    total_time = 60

    #게임 화면 구동 단계
    while True:
        # remain_time -= 1
        #pygame.event
        for event in pygame.event.get():
            #프로그램 종료시
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            #키를 누를시
            if event.type == pygame.KEYDOWN:
                #캐릭터 위치 변화
                if event.key == pygame.K_UP:
                    player_character = player_character_layDown
                    player_dy -= player_character.get_height()
                if event.key == pygame.K_DOWN:
                    player_character = player_character_layDown
                    player_dy += player_character.get_height()
                #캐릭터 총알 위치
                if event.key == pygame.K_x:
                    if player_life > 0:
                        player_bullet_posX = player_posX + player_character.get_width()
                        player_bullet_posY = player_posY + player_character.get_height()/2
                        player_bullet_list.append([player_bullet_posX, player_bullet_posY])
                #pause(일시정지)
                if event.key == pygame.K_ESCAPE:
                    GamePauseScreen(window_X, window_Y, Difficulty)

            #키가 때졌을 때 #중요! 안하면 계속 움직인다
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    player_dy = 0
                    player_character = player_character_stand
                if event.key == pygame.K_DOWN:
                    player_dy = 0
                    player_character = player_character_stand
            # 적 캐릭터 최대 높이 최소 높이 조정
            if event.type == pygame.USEREVENT+1:
                if enemy_posY < 0:
                    enemy_posY = 0
                elif enemy_posY > window_Y - enemy_character.get_height():
                    enemy_posY = window_Y - enemy_character.get_height()
                #적 위치 조정
                enemy_dy = random.randint(-30, 30)
                enemy_posY += enemy_dy
            #적 총알 위치
            if event.type == pygame.USEREVENT+2:
                #체력이 있을때만 총알 출력
                if enemy_life > 0:
                    enemy_bullet_posX = window_X - enemy_character.get_width()
                    enemy_bullet_posY = enemy_posY + enemy_character.get_height() / 2
                    enemy_bullet_list.append([enemy_bullet_posX, enemy_bullet_posY])

        #플레이어 캐릭터 최대 높이 최소 높이 조정
        if player_posY < 0:
            player_posY = 0
        elif player_posY > window_Y - player_character.get_height():
            player_posY = window_Y - player_character.get_height()

        #플레이어 위치 조정(키)
        player_posY += player_dy

        #플레이어 총알 발사
        if len(player_bullet_list) != 0:
            #플레이어 총알을 순서대로 업데이트
            for bullet, bullet_posXY in enumerate(player_bullet_list):
                #플레이어 총알 x값을 총알 픽셀값만큼 증가
                bullet_posXY[0] += player_bullet.get_width()
                player_bullet_list[bullet][0] = bullet_posXY[0]
                #적에 맞을시 플레이어 총알 파괴
                if bullet_posXY[0] >= enemy_posX - enemy_character.get_width()/2:
                    if (enemy_posY - enemy_character.get_height()/2 <= bullet_posXY[1]) & (bullet_posXY[1] <= enemy_posY + enemy_character.get_height()/2):
                        player_bullet_list.remove(bullet_posXY)
                        enemy_life -= 1
                        if enemy_life == 0:
                            game_over = True
                #화면 나갈시 총알 파괴
                try:
                    if bullet_posXY[0] >= window_X:
                        player_bullet_list.remove(bullet_posXY)
                except:
                    pass

        # 적 총알 발사
        if len(enemy_bullet_list) != 0:
            # 적 총알을 순서대로 업데이트
            for bullet, bullet_posXY in enumerate(enemy_bullet_list):
                # 플레이어 총알 x값을 총알 픽셀값만큼 증가
                bullet_posXY[0] -= enemy_bullet.get_width()
                enemy_bullet_list[bullet][0] = bullet_posXY[0]
                # 적에 맞을시 플레이어 총알 파괴
                if bullet_posXY[0] <= 0 + player_character.get_width() / 2:
                    if (player_posY - player_character.get_height() / 2 <= bullet_posXY[1]) & (
                            bullet_posXY[1] <= player_posY + player_character.get_height() / 2):
                        enemy_bullet_list.remove(bullet_posXY)
                        player_life -= 1
                        if player_life == 0:
                            game_over = True
                # 화면 나갈시 총알 파괴
                try:
                    if bullet_posXY[0] <= 0:
                        enemy_bullet_list.remove(bullet_posXY)
                except:
                    pass

        #화면 출력 칸
        #배경 화면
        window.fill(BLACK)
        #플레이어 캐릭터 출력
        if player_life > 0:
            window.blit(player_character, (player_posX, player_posY))
        #적 캐릭터 출력
        if enemy_life > 0:
            window.blit(enemy_character, (enemy_posX, enemy_posY))
        #플레이어 총알 출력
        if len(player_bullet_list) != 0:
            for bullet_posX, bullet_posY in player_bullet_list:
                window.blit(player_bullet, (bullet_posX, bullet_posY))
        #플레이어 몫숨 출력
        my_life_txt = pygame.font.SysFont('malgungothic', 20).render(f'my life : {player_life}', True, RED)
        window.blit(my_life_txt, (30,10))
        # 적 총알 출력
        if len(enemy_bullet_list) != 0:
            for bullet_posX, bullet_posY in enemy_bullet_list:
                window.blit(player_bullet, (bullet_posX, bullet_posY))
        #적 몫숨 출력
        enemy_life_txt = pygame.font.SysFont('malgungothic', 20).render(f'enemy life : {enemy_life}', True, RED)
        window.blit(enemy_life_txt, (30,50))
        #남은 시간 출력
        remain_time = total_time - (pygame.time.get_ticks() - start_ticks) / 1000
        time_left_txt = pygame.font.SysFont('malgungothic', 20).render(f'remain time : {remain_time}', True, RED)
        window.blit(time_left_txt, (30, 90))
        #게임 종료 화면 출력
        if (game_over == True) or (remain_time <= 0):
            GameEndScreen(window_X, window_Y, Difficulty, player_life, enemy_life, remain_time)

        pygame.display.update()
        clock.tick(60)


if __name__ == '__main__':
    window_X = 800
    window_Y = 600
    main_screen(window_X, window_Y)