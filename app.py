#pip install pygame
import sys
import pygame
import random

def game():
    #게임 실행 초기화
    pygame.init()

    #게임 화면 설정
    window_X = 800
    window_Y = 600
    window = pygame.display.set_mode((window_X, window_Y))

    # 게임 이름 설정
    pygame.display.set_caption('Robot Warfare')

    #프레임 설정시간
    clock = pygame.time.Clock()

    #rgb #배경화면으로 이용
    BLACK = (0,0,0)
    RED = (255, 0, 0)
    
    #플레이어
    #플레이어 캐릭터
    player_character = pygame.image.load("script/img/solider_init.png")
    player_bullet = pygame.image.load("script/img/rpg.png")

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
    enemy_move_time = 100
    enemy_move_event = pygame.USEREVENT + 1
    pygame.time.set_timer(enemy_move_event, enemy_move_time)
    #적 총알 시간 설정
    enemy_shoot_time = 300
    enemy_shoot_event = pygame.USEREVENT + 2
    pygame.time.set_timer(enemy_shoot_event, enemy_shoot_time)


    while True:
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
                    player_dy -= player_character.get_height()
                if event.key == pygame.K_DOWN:
                    player_dy += player_character.get_height()
                #캐릭터 총알 위치
                if event.key == pygame.K_x:
                    player_bullet_posX = player_posX + player_character.get_width()
                    player_bullet_posY = player_posY + player_character.get_height()/2
                    player_bullet_list.append([player_bullet_posX, player_bullet_posY])
            #키가 때졌을 때 #중요! 안하면 계속 움직인다
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    player_dy = 0
                if event.key == pygame.K_DOWN:
                    player_dy = 0

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
        # print(player_bullet_list)
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
        #게임 오버 멘트 출력
        if game_over == True:
            if enemy_life <= 0:
                game_over_txt = pygame.font.SysFont('malgungothic', 72).render('You Won', True, RED)
                window.blit(game_over_txt, game_over_txt.get_rect(centerx=window_X / 2, centery=window_Y / 2))
            elif player_life <= 0:
                game_over_txt = pygame.font.SysFont('malgungothic', 72).render('You Loose', True, RED)
                window.blit(game_over_txt, game_over_txt.get_rect(centerx=window_X / 2, centery=window_Y / 2))

        pygame.display.update()
        clock.tick(60)


if __name__ == '__main__':
    game()