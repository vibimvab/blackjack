import pygame
from sys import exit
from player import Player, Dealer
from button import blit_text_with_center, InflatableButton, ColorChangeButton, SettingsButton


def settings_screen():
    help_menu_button_pos = (WIDTH // 2, HEIGHT // 10 * 3)
    help_menu_button = InflatableButton(50, 'Help Menu', help_menu_button_pos)
    title_screen_button_pos = (WIDTH // 2, HEIGHT // 10 * 5)
    title_screen_button = InflatableButton(50, 'Title Screen', title_screen_button_pos)
    resume_button_pos = (WIDTH // 2, HEIGHT // 10 * 7)
    resume_button = InflatableButton(50, 'Resume', resume_button_pos)

    while True:
        for event in pygame.event.get():
            # 창 닫기
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                pygame.quit()
                exit()

            # 마우스 입력
            if event.type == pygame.MOUSEBUTTONDOWN:
                if help_menu_button.is_clicked():
                    help_menu_screen()
                elif title_screen_button.is_clicked():
                    return False
                elif resume_button.is_clicked():
                    return True

        screen.blit(background, (0, 0))
        help_menu_button.draw(screen)
        title_screen_button.draw(screen)
        resume_button.draw(screen)

        pygame.display.update()
        clock.tick(FPS)


def help_menu_screen() -> None:
    while True:
        for event in pygame.event.get():
            # 창 닫기
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                pygame.quit()
                exit()

            # 도움말 나가기
            if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0] \
                    or event.type == pygame.KEYDOWN and event.key == pygame.K_h \
                    or event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                return

        # 화면 출력
        screen.blit(background, (0, 0))
        screen.blit(text[50].render("New game: left click / space", False, 'Black'), (WIDTH // 5, HEIGHT // 10 + 50))
        screen.blit(text[50].render("Hit: left click / space", False, 'Black'), (WIDTH // 5, HEIGHT // 10 + 150))
        screen.blit(text[50].render("Stand: right click / S", False, 'Black'), (WIDTH // 5, HEIGHT // 10 + 250))
        screen.blit(text[50].render("Help: H", False, 'Black'), (WIDTH // 5, HEIGHT // 10 + 350))
        screen.blit(text[50].render("Split: P", False, 'Black'), (WIDTH // 5, HEIGHT // 10 + 450))
        screen.blit(text[50].render("Double Down: D", False, 'Black'), (WIDTH // 5, HEIGHT // 10 + 550))
        screen.blit(text[50].render("Quit: Q", False, 'Black'), (WIDTH // 5, HEIGHT // 10 + 650))

        pygame.display.update()
        clock.tick(FPS)


def title_screen() -> None:
    start_game_button_pos = (WIDTH // 2, HEIGHT // 40 * 19)
    start_game_button = InflatableButton(50, 'Start Game', start_game_button_pos)
    help_menu_button_pos = (WIDTH // 2, HEIGHT // 40 * 19 + 150)
    help_menu_button = InflatableButton(50, 'Help', help_menu_button_pos)
    quit_button_pos = (WIDTH // 2, HEIGHT // 40 * 19 + 300)
    quit_button = InflatableButton(50, 'Quit Game', quit_button_pos)

    while True:
        for event in pygame.event.get():
            # 창 닫기
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            # 마우스 입력
            if event.type == pygame.MOUSEBUTTONDOWN:
                # start game 버튼 클릭
                if start_game_button.is_clicked():
                    return
                elif help_menu_button.is_clicked():
                    help_menu_screen()
                elif quit_button.is_clicked():
                    pygame.quit()
                    exit()

            # 키보드 입력
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    exit()

                elif event.key == pygame.K_h:
                    help_menu_screen()

        # 화면 출력
        screen.blit(background, (0, 0))
        blit_text_with_center(screen, 100, "BLACKJACK", (WIDTH // 2, HEIGHT // 5))
        start_game_button.draw(screen)
        help_menu_button.draw(screen)
        quit_button.draw(screen)

        pygame.display.update()
        clock.tick(FPS)


def choose_player_num_screen() -> int:
    player_num = 3
    plus_player_num_button_pos = (WIDTH // 2 + 100, HEIGHT // 2)
    plus_player_num_button = ColorChangeButton(100, '+', plus_player_num_button_pos)
    minus_player_num_button_pos = (WIDTH // 2 - 100, HEIGHT // 2)
    minus_player_num_button = ColorChangeButton(100, '-', minus_player_num_button_pos)
    start_game_button_pos = (WIDTH // 2, HEIGHT // 4 * 3)
    start_game_button = InflatableButton(70, "Start Game", start_game_button_pos)

    while True:
        for event in pygame.event.get():
            # 창 닫기
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            # 키보드 입력
            if event.type == pygame.KEYDOWN:
                # 인원수 선택
                if event.key == pygame.K_1:
                    return 1
                elif event.key == pygame.K_2:
                    return 2
                elif event.key == pygame.K_3:
                    return 3
                elif event.key == pygame.K_4:
                    return 4
                elif event.key == pygame.K_5:
                    return 5
                elif event.key == pygame.K_6:
                    return 6
                elif event.key == pygame.K_7:
                    return 7

                # 도움말 창으로
                if event.key == pygame.K_h:
                    help_menu_screen()

                # 종료
                if event.key == pygame.K_q:
                    pygame.quit()
                    exit()

            # 마우스 입력
            if event.type == pygame.MOUSEBUTTONDOWN:
                if plus_player_num_button.is_clicked() and player_num < 7:
                    player_num += 1

                if minus_player_num_button.is_clicked() and player_num > 1:
                    player_num -= 1

                if start_game_button.is_clicked():
                    return player_num

        # 화면 출력
        screen.blit(background, (0, 0))
        blit_text_with_center(screen, 80, "Choose number of players", (WIDTH // 2, HEIGHT // 5))
        blit_text_with_center(screen, 150, str(player_num), (WIDTH // 2, HEIGHT // 2))
        plus_player_num_button.draw(screen)
        minus_player_num_button.draw(screen)
        start_game_button.draw(screen)

        pygame.display.update()
        clock.tick(FPS)


def game_screen(player_num):
    # 게임 변수
    game_stage = 0  # 0: 배팅, 1: hit/stand 2: 딜러 단계 및 정산
    player_list: [Player] = []
    for i in range(player_num):
        player_list.append(Player(screen, i, player_num))
    player_turn = 0
    card_deck = list(range(1, 52 * 4 + 1))
    dealer = Dealer(screen, (WIDTH // 2, HEIGHT // 6))
    settings_button = SettingsButton((70, 70), 45)

    while True:
        if game_stage == 0:
            for event in pygame.event.get():
                # 창 닫기
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

                # 키보드 입력
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_h:
                        help_menu_screen()

                    elif event.key == pygame.K_q:
                        pygame.quit()
                        exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if settings_button.is_clicked():
                        if not settings_screen():
                            return 1
                        break

                # 돌아가면서 배팅
                player_turn = player_list[player_turn].choose_bet_size(event, player_turn)
                if player_turn == player_num:  # 모든 플레이어가 베팅을 마치면
                    player_turn = 0
                    game_stage += 1

                    # 딜
                    for player in player_list:
                        player.initial_deal(card_deck)
                    dealer.initial_deal(card_deck)

            # 화면 출력
            screen.blit(background, (0, 0))
            settings_button.draw(screen, background_color)
            blit_text_with_center(screen, 50, "Choose your bet size", (WIDTH // 2, HEIGHT // 10))
            blit_text_with_center(screen, 30, "1: $500", (WIDTH // 2, HEIGHT // 10 + 70))
            blit_text_with_center(screen, 30, "2: $1000", (WIDTH // 2, HEIGHT // 10 + 140))
            blit_text_with_center(screen, 30, "3: $2000", (WIDTH // 2, HEIGHT // 10 + 210))

            for player in player_list:
                player.draw(game_stage, dealer.card)

            pygame.display.update()
            clock.tick(FPS)

        # hit/stand 단계
        elif game_stage == 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                    pygame.quit()
                    exit()

                # 키보드 입력
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_h:
                        help_menu_screen()

                # 마우스 입력
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if settings_button.is_clicked():
                        if not settings_screen():
                            return 1
                        break

                # 플레이어 액션
                player_turn = player_list[player_turn].hit_stand(event, player_turn, card_deck)
                if player_turn == player_num:  # 다음 단계로
                    player_turn = 0
                    game_stage += 1

                    for i in range(player_num):  # 모든 플레이어가 버스트 --> 딜 X
                        if player_list[i].hand < 22:
                            dealer.final_deal(card_deck)
                            break
                    for i in range(player_num):
                        player_list[i].bet_result(dealer.card)

            # 화면 출력
            screen.blit(background, (0, 0))
            settings_button.draw(screen, background_color)
            for player in player_list:
                player.draw(game_stage, dealer.card)
            dealer.draw(game_stage, player_list)

            pygame.display.update()
            clock.tick(FPS)

        # 정산 단계
        elif game_stage == 2:
            for event in pygame.event.get():
                if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                    pygame.quit()
                    exit()

                # 키보드 입력
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_h:
                        help_menu_screen()

                # 마우스 입력
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if settings_button.is_clicked():
                        if not settings_screen():
                            return 1
                        break

                # 게임 종료
                if pygame.mouse.get_pressed()[0] or event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    game_stage = 0
                    card_deck = [i + 1 for i in range(52 * 4)]
                    for i in range(player_num):
                        player_list[i].initialize()
                    dealer.initialize()

            # 화면 출력
            screen.blit(background, (0, 0))
            settings_button.draw(screen, background_color)
            for player in player_list:
                player.draw(game_stage, dealer.card)
            dealer.draw(game_stage, player_list)

            pygame.display.update()
            clock.tick(FPS)


def main():
    # 게임 변수
    run_screen = {
        1: title_screen,
        2: choose_player_num_screen,
        3: game_screen
    }
    game_screen_num = 1
    player_num = 0

    # 이벤트 루프
    while True:
        # title_screen
        if game_screen_num == 1:
            run_screen[1]()
            game_screen_num += 1

        # choose_player_num_screen
        elif game_screen_num == 2:
            player_num = run_screen[2]()
            game_screen_num += 1

        # game_screen
        elif game_screen_num == 3:
            game_screen_num = run_screen[3](player_num)


if __name__ == '__main__':
    pygame.init()

    # 화면 설정
    WIDTH = 1680
    HEIGHT = 1050
    screen_size = (WIDTH, HEIGHT - 55)
    screen = pygame.display.set_mode(screen_size)

    # 화면 타이틀 설정
    pygame.display.set_caption("BLACKJACK")

    # frame rate 설정
    FPS = 100
    clock = pygame.time.Clock()

    # 배경 화면 설정
    background = pygame.Surface(screen_size)
    background_color = 'gray74'
    background.fill(background_color)

    # 글씨 폰트 설정
    text = {}
    for font_size in range(10, 210, 10):
        text[font_size] = pygame.font.SysFont('Comic Sans MS', font_size)

    # 실행
    main()
