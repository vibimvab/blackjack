import pygame
from random import choice
import math
import os

pygame.init()


def deal(card_deck, person_card):
    dealt_card = choice(card_deck)
    card_deck.remove(dealt_card)
    person_card.append(dealt_card % 52)


class Person:
    # 이미지 변수
    card_value = {
        1: pygame.image.load(os.path.join('card', 'spade_ace.png')),
        2: pygame.image.load(os.path.join('card', 'spade_two.png')),
        3: pygame.image.load(os.path.join('card', 'spade_three.png')),
        4: pygame.image.load(os.path.join('card', 'spade_four.png')),
        5: pygame.image.load(os.path.join('card', 'spade_five.png')),
        6: pygame.image.load(os.path.join('card', 'spade_six.png')),
        7: pygame.image.load(os.path.join('card', 'spade_seven.png')),
        8: pygame.image.load(os.path.join('card', 'spade_eight.png')),
        9: pygame.image.load(os.path.join('card', 'spade_nine.png')),
        10: pygame.image.load(os.path.join('card', 'spade_ten.png')),
        11: pygame.image.load(os.path.join('card', 'spade_jack.png')),
        12: pygame.image.load(os.path.join('card', 'spade_queen.png')),
        13: pygame.image.load(os.path.join('card', 'spade_king.png')),

        14: pygame.image.load(os.path.join('card', 'club_ace.png')),
        15: pygame.image.load(os.path.join('card', 'club_two.png')),
        16: pygame.image.load(os.path.join('card', 'club_three.png')),
        17: pygame.image.load(os.path.join('card', 'club_four.png')),
        18: pygame.image.load(os.path.join('card', 'club_five.png')),
        19: pygame.image.load(os.path.join('card', 'club_six.png')),
        20: pygame.image.load(os.path.join('card', 'club_seven.png')),
        21: pygame.image.load(os.path.join('card', 'club_eight.png')),
        22: pygame.image.load(os.path.join('card', 'club_nine.png')),
        23: pygame.image.load(os.path.join('card', 'club_ten.png')),
        24: pygame.image.load(os.path.join('card', 'club_jack.png')),
        25: pygame.image.load(os.path.join('card', 'club_queen.png')),
        26: pygame.image.load(os.path.join('card', 'club_king.png')),

        27: pygame.image.load(os.path.join('card', 'heart_ace.png')),
        28: pygame.image.load(os.path.join('card', 'heart_two.png')),
        29: pygame.image.load(os.path.join('card', 'heart_three.png')),
        30: pygame.image.load(os.path.join('card', 'heart_four.png')),
        31: pygame.image.load(os.path.join('card', 'heart_five.png')),
        32: pygame.image.load(os.path.join('card', 'heart_six.png')),
        33: pygame.image.load(os.path.join('card', 'heart_seven.png')),
        34: pygame.image.load(os.path.join('card', 'heart_eight.png')),
        35: pygame.image.load(os.path.join('card', 'heart_nine.png')),
        36: pygame.image.load(os.path.join('card', 'heart_ten.png')),
        37: pygame.image.load(os.path.join('card', 'heart_jack.png')),
        38: pygame.image.load(os.path.join('card', 'heart_queen.png')),
        39: pygame.image.load(os.path.join('card', 'heart_king.png')),

        40: pygame.image.load(os.path.join('card', 'diamond_ace.png')),
        41: pygame.image.load(os.path.join('card', 'diamond_two.png')),
        42: pygame.image.load(os.path.join('card', 'diamond_three.png')),
        43: pygame.image.load(os.path.join('card', 'diamond_four.png')),
        44: pygame.image.load(os.path.join('card', 'diamond_five.png')),
        45: pygame.image.load(os.path.join('card', 'diamond_six.png')),
        46: pygame.image.load(os.path.join('card', 'diamond_seven.png')),
        47: pygame.image.load(os.path.join('card', 'diamond_eight.png')),
        48: pygame.image.load(os.path.join('card', 'diamond_nine.png')),
        49: pygame.image.load(os.path.join('card', 'diamond_ten.png')),
        50: pygame.image.load(os.path.join('card', 'diamond_jack.png')),
        51: pygame.image.load(os.path.join('card', 'diamond_queen.png')),
        0: pygame.image.load(os.path.join('card', 'diamond_king.png'))
    }
    card_back = pygame.image.load(os.path.join('card', 'card_back.png'))
    player_cursor = pygame.image.load(os.path.join('card', 'player_cursor.png'))
    player_cursor.set_colorkey((255, 255, 255))

    # 글씨 폰트
    text = {}
    for font_size in range(10, 210, 10):
        text[font_size] = pygame.font.SysFont('Comic Sans MS', font_size)

    def __init__(self, screen, position):
        self.screen = screen
        self.card = []
        self.hand = 0
        self.position = position
        self.x_pos = position[0]
        self.y_pos = position[1]

    def draw_card(self):
        card_num = len(self.card)
        for i, card in enumerate(self.card):
            self.screen.blit(self.card_value[card], (134 / card_num * i - 105 + self.x_pos, self.y_pos))

    def deal(self, card_deck):
        deal(card_deck, self.card)

    @staticmethod
    def calculate_hand(cards):
        hand = 0
        ace_in_hand = False

        for card in cards:
            if 0 < card % 13 < 11:
                hand += card % 13
            else:
                hand += 10

        for card in cards:
            if card % 13 == 1:
                ace_in_hand = True

        if ace_in_hand and hand < 12:
            return hand + 10
        else:
            return hand


class Player(Person):
    def __init__(self, screen, player, total_player):
        deg = math.pi * 3 / 4 - (math.pi / (total_player * 4)) - (math.pi / (total_player * 4)) * player * 2
        # FIXME: use WIDTH and HEIGHT for x_pos and y_pos
        super().__init__(screen, (840 + 1120 * math.cos(deg) // 1, -370 + 1120 * math.sin(deg) // 1))
        self.money = 10000
        self.bet_size = 0

    def draw(self, game_stage, dealer_cards):
        self.screen.blit(self.text[30].render(f"Money: {self.money}", False, 'Black'),
                         (self.x_pos - 100, self.y_pos + 100))
        self.screen.blit(self.text[30].render(f"Bet: {self.bet_size}", False, 'Black'),
                         (self.x_pos - 100, self.y_pos + 150))

        # 파산
        if self.money < 0:
            self.screen.blit(self.text[50].render('Bankrupted', False, 'Black'), (self.x_pos - 105, 35 + self.y_pos))

        else:
            if game_stage >= 1:
                # 카드
                self.draw_card()
                # 핸드 밸류
                self.screen.blit(self.text[40].render(f"{self.hand}", False, 'Black'),
                                 (-105 + self.x_pos, -55 + self.y_pos))

                # 버스트
                if self.hand > 21:
                    self.screen.blit(self.text[40].render("BUSTED!", False, 'Black'),
                                     (-45 + self.x_pos, -55 + self.y_pos))
                    return

            # 배팅 결과
            if game_stage >= 2:
                dealer_hand = self.calculate_hand(dealer_cards)
                if self.hand == 21 and len(self.card) == 2:  # 플레이어 블랙잭
                    if dealer_hand == 21 and len(dealer_cards) == 2:  # 딜러도 블랙잭 --> 무승부
                        self.screen.blit(self.text[40].render("DRAW!", False, 'Black'),
                                         (-45 + self.x_pos, -55 + self.y_pos))
                    else:
                        self.screen.blit(self.text[40].render("BLACKJACK!!!", False, 'Black'),
                                         (-45 + self.x_pos, -55 + self.y_pos))
                elif dealer_hand == 21 and len(dealer_cards) == 2:  # 플레이어 블랙잭 아님, 딜러 블랙잭
                    self.screen.blit(self.text[40].render("Lose", False, 'Black'),
                                     (-45 + self.x_pos, -55 + self.y_pos))
                else:  # 플레이어, 딜러가 블랙잭 아님
                    if dealer_hand == self.hand:
                        self.screen.blit(self.text[40].render("DRAW!", False, 'Black'),
                                         (-45 + self.x_pos, -55 + self.y_pos))
                    elif dealer_hand > 21 or dealer_hand < self.hand < 22:
                        self.screen.blit(self.text[40].render("WIN!", False, 'Black'),
                                         (-45 + self.x_pos, -55 + self.y_pos))
                    else:
                        self.screen.blit(self.text[40].render("Lose", False, 'Black'),
                                         (-45 + self.x_pos, -55 + self.y_pos))

    def hit(self, card_deck):
        self.deal(card_deck)
        self.hand = self.calculate_hand(self.card)

    def double_down(self, card_deck):
        self.money -= self.bet_size
        self.bet_size *= 2
        self.deal(card_deck)
        self.hand = self.calculate_hand(self.card)

    def choose_bet_size(self, event, player_turn):
        if self.money >= 0:
            if event.type == pygame.KEYDOWN \
                    and (event.key == pygame.K_1 or event.key == pygame.K_2 or event.key == pygame.K_3):
                if event.key == pygame.K_1:
                    self.bet_size = 500
                elif event.key == pygame.K_2:
                    self.bet_size = 1000
                elif event.key == pygame.K_3:
                    self.bet_size = 2000
                self.money -= self.bet_size

                return player_turn + 1
            else:
                return player_turn  # 인풋이 없을 때도 끊임 없이 리턴을 내지 않으면 event loop 안에서 player_turn == None 이 돼버림
        else:
            return player_turn + 1

    def initial_deal(self, card_deck):
        if self.money >= 0:
            self.deal(card_deck)
            self.deal(card_deck)
            self.hand = self.calculate_hand(self.card)

    def hit_stand(self, event, player_turn, card_deck):
        if self.money >= 0:
            if self.hand >= 21:
                return player_turn + 1

            else:
                # hit
                if pygame.mouse.get_pressed()[0] or event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    self.hit(card_deck)
                    return player_turn

                # stand
                elif pygame.mouse.get_pressed()[2] or event.type == pygame.KEYDOWN and event.key == pygame.K_s:
                    return player_turn + 1

                # double down
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_d and len(self.card) == 2:
                    self.double_down(card_deck)
                    return player_turn + 1

                else:
                    return player_turn
        else:
            return player_turn + 1

    def bet_result(self, dealer_card):
        if self.money >= 0:
            dealer_hand = self.calculate_hand(dealer_card)

            if self.hand < 22:
                if self.hand == 21 and len(self.card) == 2:  # 플레이어 블랙잭
                    if dealer_hand == 21 and len(dealer_card) == 2:  # 딜러도 블랙잭 --> 무승부
                        self.money += self.bet_size
                    else:
                        self.money += self.bet_size // 2 * 5
                elif not (dealer_hand == 21 and len(dealer_card) == 2):  # 딜러가 블랙잭이 아니라면
                    if dealer_hand == self.hand:
                        self.money += self.bet_size
                    elif dealer_hand > 21 or dealer_hand < self.hand < 22:
                        self.money += self.bet_size * 2

    def initialize(self):
        self.card = []
        self.bet_size = 0
        self.hand = 0

    # def set_xy_pos(self, player, total_player):  # 플레이어 중간 추가 기능 위함
    #     deg = math.pi * 3 / 4 - (math.pi / (total_player * 4)) - (math.pi / (total_player * 4)) * player * 2
    #     self.x_pos = 840 + 1120 * math.cos(deg)
    #     self.y_pos = -370 + 1120 * math.sin(deg)


class Dealer(Person):
    def __init__(self, screen, position):
        super().__init__(screen, position)

    def initial_deal(self, card_deck):
        self.deal(card_deck)
        self.deal(card_deck)

    def final_deal(self, card_deck):
        while True:
            if self.calculate_hand(self.card) > 16:
                self.hand = self.calculate_hand(self.card)
                return

            self.deal(card_deck)

    def initialize(self):
        self.card = []
        self.hand = 0

    def draw(self, game_stage, player_list):
        if game_stage >= 1:
            # 딜러 카드
            self.draw_card()
            if game_stage == 1:
                self.screen.blit(self.card_back, (134 / len(self.card) - 105 + self.x_pos, self.y_pos))

            if game_stage >= 2:
                if len(self.card) == 2:  # 일단 카드 뒷면 그려 놓고 버스트 아닌 사람이 있으면 다시 그림
                    self.screen.blit(self.card_back, (134 / len(self.card) - 105 + self.x_pos, self.y_pos))

                    for player in player_list:
                        if player.hand < 22:
                            self.screen.blit(self.card_value[self.card[1]],
                                             (134 - 105 + self.x_pos, self.y_pos))
                            self.screen.blit(self.text[40].render(f"{self.hand}", False, 'Black'),
                                             (-105 + self.x_pos, -55 + self.y_pos))
                            break
