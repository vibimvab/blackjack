import pygame
import math
import os
from hand import Hand

pygame.init()


class Person:
    # 이미지 변수
    player_cursor = pygame.image.load(os.path.join('card', 'player_cursor.png'))
    player_cursor.set_colorkey((255, 255, 255))

    # 글씨 폰트
    text = {}
    for font_size in range(10, 210, 10):
        text[font_size] = pygame.font.SysFont('Comic Sans MS', font_size)

    def __init__(self, screen, position):
        self.screen = screen
        self.hand: list[Hand] = []
        self.position = position
        self.x_pos = position[0]
        self.y_pos = position[1]


class Player(Person):
    def __init__(self, screen, player, total_player):
        deg = math.pi * 3 / 4 - (math.pi / (total_player * 4)) - (math.pi / (total_player * 4)) * player * 2
        # FIXME: use WIDTH and HEIGHT for x_pos and y_pos
        super().__init__(screen, (840 + 1120 * math.cos(deg) // 1, -370 + 1120 * math.sin(deg) // 1))
        self.player_num = player
        self.money = 10000
        self.bet_size = 0
        self.hand_turn = 0
        self.bankrupted = False

    def draw(self, game_stage, dealer_cards, player_turn):
        self.screen.blit(self.text[30].render(f"Money: {self.money}", False, 'Black'),
                         (self.x_pos - 100, self.y_pos + 150))

        # 파산
        if self.is_bankrupted():
            self.screen.blit(self.text[50].render('Bankrupted', False, 'Black'), (self.x_pos - 105, 35 + self.y_pos))

        else:
            if game_stage == 0:
                if player_turn == self.player_num:
                    self.screen.blit(self.player_cursor, (self.x_pos - 130, self.y_pos + 140))
                # bet size
                self.screen.blit(self.text[30].render(f"Bet: {self.bet_size}", False, 'Black'),
                                 (self.x_pos - 100, self.y_pos + 100))
            if game_stage >= 1:
                # 핸드 별로 bet size 따로 출력
                for hand_num, hand in enumerate(self.hand):
                    hand_turn = self.player_num == player_turn and self.hand_turn == hand_num
                    hand.draw(game_stage, dealer_cards, hand_turn)

    def choose_bet_size(self, event, player_turn):
        if not self.is_bankrupted():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    if self.money >= 500:
                        self.bet_size = 500
                        self.money -= self.bet_size
                        return player_turn + 1
                    else:
                        self.bet_size = self.money
                        self.money -= self.bet_size
                        return player_turn + 1
                elif event.key == pygame.K_2 and self.money >= 1000:
                    self.bet_size = 1000
                    self.money -= self.bet_size
                    return player_turn + 1
                elif event.key == pygame.K_3 and self.money >= 2000:
                    self.bet_size = 2000
                    self.money -= self.bet_size
                    return player_turn + 1
                else:
                    return player_turn
            else:
                return player_turn  # 인풋이 없을 때도 끊임 없이 리턴을 내지 않으면 event loop 안에서 player_turn == None 이 돼버림
        else:
            return player_turn + 1

    def initial_deal(self, card_deck):
        if self.money >= 0:
            self.hand.append(Hand(self.screen, 0, self.position, self.bet_size, card_deck))

    def turn_end(self, player_turn):
        if self.hand_turn >= len(self.hand):
            self.hand_turn = 0
            return player_turn + 1
        else:
            return player_turn

    def hit_stand(self, event, player_turn, card_deck):
        if not self.is_bankrupted():
            if self.hand[self.hand_turn].value >= 21:
                self.hand_turn += 1
                return self.turn_end(player_turn)

            else:
                # hit
                if pygame.mouse.get_pressed()[0] or event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    self.hand[self.hand_turn].deal(card_deck)
                    return self.turn_end(player_turn)

                # stand
                elif pygame.mouse.get_pressed()[2] or event.type == pygame.KEYDOWN and event.key == pygame.K_s:
                    self.hand_turn += 1
                    return self.turn_end(player_turn)

                # double down
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_d \
                        and len(self.hand[self.hand_turn].card) == 2 \
                        and self.money >= self.bet_size:
                    self.money = self.hand[self.hand_turn].double_down(self.money, card_deck)
                    self.hand_turn += 1
                    return self.turn_end(player_turn)

                # split
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_v \
                        and self.hand[self.hand_turn].can_be_split()\
                        and self.money >= self.bet_size:
                    self.hand.append(Hand(self.screen, self.hand[self.hand_turn].split + 1, self.position,
                                          self.bet_size, card_deck, num=len(self.hand),
                                          split_card=self.hand[self.hand_turn].card.pop(1)))
                    self.hand[self.hand_turn].deal(card_deck)
                    self.money -= self.bet_size
                    return self.turn_end(player_turn)

                else:
                    return self.turn_end(player_turn)
        else:
            return player_turn + 1

    def bet_result(self, dealer_card):
        for hand in self.hand:
            self.money += hand.bet_result(dealer_card)

    def is_bankrupted(self):
        return self.bankrupted

    def initialize(self):
        self.hand = []
        self.bet_size = 0
        self.hand_turn = 0

        if self.money <= 0:
            self.bankrupted = True

    # def set_xy_pos(self, player, total_player):  # 플레이어 중간 추가 기능 위함
    #     deg = math.pi * 3 / 4 - (math.pi / (total_player * 4)) - (math.pi / (total_player * 4)) * player * 2
    #     self.x_pos = 840 + 1120 * math.cos(deg)
    #     self.y_pos = -370 + 1120 * math.sin(deg)


class Dealer(Person):
    card_back = pygame.image.load(os.path.join('card', 'card_back.png'))

    def __init__(self, screen, position, card_deck):
        super().__init__(screen, position)
        self.hand = [Hand(self.screen, -1, self.position, -1, card_deck)]

    def initial_deal(self, card_deck):
        self.hand = [Hand(self.screen, -1, self.position, -1, card_deck)]

    def final_deal(self, card_deck):
        while True:
            if self.hand[0].value > 16:
                return self.hand[0].value

            self.hand[0].deal(card_deck)

    def initialize(self):
        self.hand[0].card = []
        self.hand[0].value = 0

    def draw(self, game_stage, player_list):
        if game_stage >= 1:
            # 딜러 카드
            self.hand[0].draw_card()
            if game_stage == 1:
                self.screen.blit(self.card_back, (134 / len(self.hand[0].card) - 105 + self.x_pos, self.y_pos))

            if game_stage >= 2:
                if len(self.hand[0].card) == 2:  # 일단 카드 뒷면 그려 놓고 버스트 아닌 사람이 있으면 다시 그림
                    self.screen.blit(self.card_back, (134 / len(self.hand[0].card) - 105 + self.x_pos, self.y_pos))

                    for player in player_list:
                        for hand in player.hand:
                            if hand.value < 22:
                                self.screen.blit(Hand.card_value[self.hand[0].card[1]],
                                                 (134 / len(self.hand[0].card) - 105 + self.x_pos, self.y_pos))
                                self.screen.blit(self.text[40].render(f"{self.hand[0].value}", False, 'Black'),
                                                 (-105 + self.x_pos, -55 + self.y_pos))
                                return
                else:
                    self.screen.blit(self.text[40].render(f"{self.hand[0].value}", False, 'Black'),
                                     (-105 + self.x_pos, -55 + self.y_pos))
