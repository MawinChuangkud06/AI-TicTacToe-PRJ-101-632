# PyGame (No Design) Coded By MawinCK and BlackBox AI

import pygame
from random import randint
from math import inf
from pyfiglet import figlet_format
from win32.win32gui import MessageBeep, MessageBox

def WindowPrompt(msg: str):
    MessageBeep(0)
    MessageBox(None, msg, "TicTacToe Prompt", 0)

class TicTacToe:
    def __init__(self):
        self.width = 800
        self.height = 600
        print(figlet_format("PyGame    Started..", width=100))
        print(figlet_format("TicTacToe", "isometric2", width=200))
        self.board = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
        self.ButtonBoard = [
            [pygame.Rect(i * 200 + (self.width - 600) // 2, j * 200 + (self.height - 600) // 2, 200, 200) for j in range(3)]
            for i in range(3)
        ]

        self.Screen = pygame.display.set_mode((self.width, self.height))

        self.PrevPlayed = None
        self.Player = None
        self.AI = None
        self.Turn = None
        self.running = False
        self.Diff = None

    def DrawBoard(self):
        self.Screen.fill((0, 0, 0))  # Clear the screen
        for i in range(3):
            for j in range(3):
                pygame.draw.rect(self.Screen, (255, 255, 255), self.ButtonBoard[i][j], 1)
                if type(self.board[i][j]) == str:
                    font = pygame.font.Font(None, 72)
                    text = font.render(self.board[i][j], True, (255, 255, 255))
                    text_rect = text.get_rect(center=(self.ButtonBoard[i][j].center))
                    self.Screen.blit(text, text_rect)

    def IsAbleToFill(self, row: int, col: int):
        return type(self.board[row][col]) == int

    def PlayerFill(self, row: int, col: int):
        if self.IsAbleToFill(row, col):
            self.board[row][col] = self.Player

    def IsTie(self):
        return all(type(self.board[i][j]) != int for i in range(3) for j in range(3))

    def IsGameOver(self) -> bool:
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2]:
                return True
            elif self.board[0][i] == self.board[1][i] == self.board[2][i]:
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2]:
            return True
        elif self.board[0][2] == self.board[1][1] == self.board[2][0]:
            return True
        return False

    def ChooseGameMode(self):
        RGB_BG = (0, 0, 0)
        self.Screen.fill(RGB_BG)

        pygame.font.init()
        font = pygame.font.Font(None, 36)
        title_text = font.render("Choose Your GameMode For TicTacToe:", True, (255, 255, 255))

        button_width = 200
        button_height = 50
        alone_button = pygame.Rect((self.width // 2 - button_width // 2, self.height // 2 - 25), (button_width, button_height))
        ai_button = pygame.Rect((self.width // 2 - button_width // 2, self.height // 2 + 30), (button_width, button_height))

        title_rect = title_text.get_rect(center=(self.width // 2, self.height // 2 - 100))
        self.Screen.blit(title_text, title_rect)
        pygame.draw.rect(self.Screen, (255, 255, 255), alone_button)
        pygame.draw.rect(self.Screen, (255, 255, 255), ai_button)

        alone_text = font.render("Play Alone", True, (0, 0, 0))
        ai_text = font.render("Play With AI", True, (0, 0, 0))
        self.Screen.blit(alone_text, alone_button.move(30, 10))
        self.Screen.blit(ai_text, ai_button.move(30, 10))

        pygame.display.flip()

        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    waiting = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if alone_button.collidepoint(event.pos):
                            print("Play Alone selected")
                            waiting = False
                            self.StartAloneGame()
                        elif ai_button.collidepoint(event.pos):
                            print("Play With AI selected")
                            waiting = False
                            self.StartAIGame()

    def ChooseDifficulty(self):
        RGB_BG = (0, 0, 0)
        self.Screen.fill(RGB_BG)

        pygame.font.init()
        font = pygame.font.Font(None, 36)
        title_text = font.render("Choose AI Difficulty:", True, (255, 255, 255))

        button_width = 200
        button_height = 50
        easy_button = pygame.Rect((self.width // 2 - button_width // 2, self.height // 2 - 25), (button_width, button_height))
        medium_button = pygame.Rect((self.width // 2 - button_width // 2, self.height // 2 + 30), (button_width, button_height))
        hard_button = pygame.Rect((self.width // 2 - button_width // 2, self.height // 2 + 85), (button_width, button_height))

        title_rect = title_text.get_rect(center=(self.width // 2, self.height // 2 - 100))
        self.Screen.blit(title_text, title_rect)
        pygame.draw.rect(self.Screen, (255, 255, 255), easy_button)
        pygame.draw.rect(self.Screen, (255, 255, 255), medium_button)
        pygame.draw.rect(self.Screen, (255, 255, 255), hard_button)

        easy_text = font.render("Easy", True, (0, 0, 0))
        medium_text = font.render("Medium", True, (0, 0, 0))
        hard_text = font.render("Hard", True, (0, 0, 0))
        self.Screen.blit(easy_text, easy_button.move(30, 10))
        self.Screen.blit(medium_text, medium_button.move(30, 10))
        self.Screen.blit(hard_text, hard_button.move(30, 10))

        pygame.display.flip()

        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    waiting = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if easy_button.collidepoint(event.pos):
                            self.Diff = 'e'
                            waiting = False
                        elif medium_button.collidepoint(event.pos):
                            self.Diff = 'm'
                            waiting = False
                        elif hard_button.collidepoint(event.pos):
                            self.Diff = 'h'
                            waiting = False

    def SwitchPlayerTeam(self):
        self.Player = 'O' if self.Player == 'X' else 'X'

    def StartAloneGame(self):
        self.running = True
        self.ChooseTeam()
        while self.running:
            self.DrawBoard()
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    for i in range(3):
                        for j in range(3):
                            if self.ButtonBoard[i][j].collidepoint(event.pos):
                                if self.IsAbleToFill(i, j):
                                    self.PlayerFill(i, j)
                                    self.PrevPlayed = self.Player
                                    if self.IsGameOver():
                                        self.running = False
                                        WindowPrompt(f"Game Over Winner: {self.PrevPlayed}")
                                    if self.IsTie():
                                        self.running = False
                                        WindowPrompt("Game Tie!")
                                    self.SwitchPlayerTeam()  # Switch to the next player
            pygame.display.flip()

    def ChooseTeam(self):
        RGB_BG = (0, 0, 0)
        self.Screen.fill(RGB_BG)
        font = pygame.font.Font(None, 36)
        title_text = font.render("Choose Your Team:", True, (255, 255, 255))

        button_width = 200
        button_height = 50
        o_button = pygame.Rect((self.width // 2 - button_width // 2, self.height // 2 - 25), (button_width, button_height))
        x_button = pygame.Rect((self.width // 2 - button_width // 2, self.height // 2 + 30), (button_width, button_height))

        title_rect = title_text.get_rect(center=(self.width // 2, self.height // 2 - 100))
        self.Screen.blit(title_text, title_rect)
        pygame.draw.rect(self.Screen, (255, 255, 255), o_button)
        pygame.draw.rect(self.Screen, (255, 255, 255), x_button)

        o_text = font.render("1: Play As O", True, (0, 0, 0))
        x_text = font.render("2: Play As X", True, (0, 0, 0))
        self.Screen.blit(o_text, o_button.move(30, 10))
        self.Screen.blit(x_text, x_button.move(30, 10))

        pygame.display.flip()

        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    waiting = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if o_button.collidepoint(event.pos):
                            self.Player = 'O'
                            self.AI = 'X'
                            waiting = False
                        elif x_button.collidepoint(event.pos):
                            self.Player = 'X'
                            self.AI = 'O'
                            waiting = False

        # Clear the screen after choosing the team
        self.Screen.fill((0, 0, 0))
        pygame.display.flip()

    def StartAIGame(self):
        self.running = True
        self.ChooseTeam()
        self.ChooseDifficulty()  # Choose AI difficulty
        self.StartTurn()
        while self.running:
            self.DrawBoard()
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    for i in range(3):
                        for j in range(3):
                            if self.ButtonBoard[i][j].collidepoint(event.pos) and self.Turn == self.Player:
                                if self.IsAbleToFill(i, j):
                                    self.PlayerFill(i, j)
                                    self.PrevPlayed = self.Player
                                    if self.IsGameOver():
                                        self.running = False
                                        WindowPrompt(f"Game Over Winner: {self.PrevPlayed}")
                                    elif self.IsTie():
                                        self.running = False
                                        WindowPrompt("Game Tie!")
                                    else:
                                        self.Turn = self.AI  # Switch to AI's turn
                elif event.type == pygame.QUIT:
                    pygame.quit()

            if self.Turn == self.AI:
                self.AIMove()
                self.PrevPlayed = self.AI
                if self.IsGameOver():
                    self.running = False
                    WindowPrompt(f"Game Over Winner: {self.AI}")
                elif self.IsTie():
                    self.running = False
                    WindowPrompt("Game Tie!")
                self.Turn = self.Player  # Switch back to player's turn

            pygame.display.flip()

    def StartTurn(self):
        n = randint(0, 1)
        self.Turn = self.Player if n == 0 else self.AI

    def MiniMaxCheckGameOver(self) -> str | None:
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2]:
                return self.board[i][0]
            elif self.board[0][i] == self.board[1][i] == self.board[2][i]:
                return self.board[0][i]
        if self.board[0][0] == self.board[1][1] == self.board[2][2]:
            return self.board[0][0]
        elif self.board[0][2] == self.board[1][1] == self.board[2][0]:
            return self.board[0][2]
        return None

    def MiniMax(self, ismaxing: bool, alpha: int, beta: int, depth: int) -> int:
        winner = self.MiniMaxCheckGameOver()
        if winner == self.AI:
            return 1 + depth
        if winner == self.Player:
            return -1 + depth
        if self.IsTie():
            return 0
        if ismaxing:
            maxValue = -inf
            for i in range(3):
                for j in range(3):
                    if self.IsAbleToFill(i, j):
                        self.board[i][j] = self.AI
                        value = self.MiniMax(False, alpha, beta, depth + 1)
                        self.board[i][j] = i * 3 + j + 1
                        maxValue = max(maxValue, value)
                        alpha = max(alpha, value)
                        if beta <= alpha:
                            break
            return maxValue
        else:
            minValue = inf
            for i in range(3):
                for j in range(3):
                    if self.IsAbleToFill(i, j):
                        self.board[i][j] = self.Player
                        value = self.MiniMax(True, alpha, beta, depth + 1)
                        self.board[i][j] = i * 3 + j + 1
                        minValue = min(minValue, value)
                        beta = min(beta, value)
                        if beta <= alpha:
                            break
            return minValue

    def FindAvaForEasyAI(self):
        ava = []
        for i in range(3):
            for j in range(3):
                if self.IsAbleToFill(i, j):
                    ava.append([i, j])
        return ava

    def EasyAIFill(self):
        ava = self.FindAvaForEasyAI()
        if ava:
            ava = ava[randint(0, len(ava) - 1)]
            self.board[ava[0]][ava[1]] = self.AI

    def FindAvaSpot(self, symbol: str):
        for i in range(3):
            if self.board[i][0] == symbol and self.board[i][1] == symbol and self.IsAbleToFill(i, 2):
                return [i, 2]
            elif self.board[i][2] == symbol and self.board[i][1] == symbol and self.IsAbleToFill(i, 0):
                return [i, 0]
            elif self.board[i][2] == symbol and self.board[i][0] == symbol and self.IsAbleToFill(i, 1):
                return [i, 1]
            elif self.board[0][i] == symbol and self.board[1][i] == symbol and self.IsAbleToFill(2, i):
                return [2, i]
            elif self.board[2][i] == symbol and self.board[1][i] == symbol and self.IsAbleToFill(0, i):
                return [0, i]
            elif self.board[2][i] == symbol and self.board[0][i] == symbol and self.IsAbleToFill(1, i):
                return [1, i]
        if self.board[0][0] == symbol and self.board[1][1] == symbol and self.IsAbleToFill(2, 2):
            return [2, 2]
        elif self.board[2][2] == symbol and self.board[1][1] == symbol and self.IsAbleToFill(0, 0):
            return [0, 0]
        elif self.board[2][2] == symbol and self.board[0][0] == symbol and self.IsAbleToFill(1, 1):
            return [1, 1]
        elif self.board[0][2] == symbol and self.board[1][1] == symbol and self.IsAbleToFill(2, 0):
            return [2, 0]
        elif self.board[2][0] == symbol and self.board[1][1] == symbol and self.IsAbleToFill(0, 2):
            return [0, 2]
        elif self.board[0][2] == symbol and self.board[2][0] == symbol and self.IsAbleToFill(1, 1):
            return [1, 1]
        return None

    def AIMove(self):
        if self.Diff == 'e':
            self.EasyAIFill()
        elif self.Diff == 'm':
            ava_AI = self.FindAvaSpot(self.AI)
            if ava_AI:
                self.board[ava_AI[0]][ava_AI[1]] = self.AI
                return
            ava_Player = self.FindAvaSpot(self.Player)
            if ava_Player:
                self.board[ava_Player[0]][ava_Player[1]] = self.AI
                return
            for i in range(3):
                for j in range(3):
                    if self.IsAbleToFill(i, j):
                        self.board[i][j] = self.AI
                        return
        elif self.Diff == 'h':
            bestfill = []
            bestscore = -inf
            for i in range(3):
                for j in range(3):
                    if self.IsAbleToFill(i, j):
                        self.board[i][j] = self.AI
                        score = self.MiniMax(False, -inf, inf, 0)
                        self.board[i][j] = i * 3 + j + 1
                        if bestscore < score:
                            bestscore = score
                            bestfill = [i, j]
            if bestfill:
                self.board[bestfill[0]][bestfill[1]] = self.AI

if __name__ == "__main__":
    pygame.init()
    T1 = TicTacToe()
    T1.ChooseGameMode()
    pygame.quit()
