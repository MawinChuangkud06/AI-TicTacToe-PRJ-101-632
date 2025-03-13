#Must Install The Lib Below:
# 1 -> pip install pyfiglet
# Lib
from random import randint
from math import inf
from pyfiglet import figlet_format
from os import system
class tictactoe:
    def __init__(self):
        self.Board = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
        self.Player = None
        self.AI = None
        self.PrevPlayed = None
        self.Turn = None
        self.Diff = None
    def DrawBoard(self):
        print("-"*14)
        for i in range(3):
            print(f"| {self.Board[i][0]} | {self.Board[i][1]} | {self.Board[i][2]} | ")
        print("-"*14)
    def ChooseTeam(self):
        while True:
            n = input("Choose You Team (O or X) : ").upper()
            vaildTeam = ["O", "X"]
            if n not in vaildTeam:
                print("Invaild Team")
                continue
            self.Player = n
            self.AI = "O" if n == "X" else "X"
            break
    def SelectDiff(self):
        while True:
            n = input("Select You Diff for AI\ne: Easy\nm: Meduim\nh: Hard\ninput Here : ").lower()
            vaildDiff = ["e", "m", "h"]
            if n not in vaildDiff:
                print("Invaild Diff")
                continue
            self.Diff = n
            break
    def StartTurn(self):
        n = randint(1, 2)
        self.Turn = self.Player if n == 1 else self.AI
    def IsTie(self) -> bool:
        return all([type(self.Board[i][j]) != int for i in range(3) for j in range(3)])
    def IsGameOver(self) -> bool:
        for i in range(3):
            if self.Board[i][0] == self.Board[i][1] and self.Board[i][1] == self.Board[i][2]:
                return True
            elif self.Board[0][i] == self.Board[1][i] and self.Board[1][i] == self.Board[2][i]:
                return True
        if self.Board[0][0] == self.Board[1][1] and self.Board[1][1] == self.Board[2][2]:
            return True
        elif self.Board[0][2] == self.Board[1][1] and self.Board[1][1] == self.Board[2][0]:
            return True
        return False
    def IsAbleFill(self, row : int, col : int) -> bool:
        return type(self.Board[row][col]) == int
    def PlayerFill(self, row : int, col : int):
        if self.IsAbleFill(row, col):
            self.Board[row][col] = self.Player
        else:
            return
    # AI Algorithm/ Hard Mode/ Meduim Mode/ Easy Mode
    def EasyAIFill(self):
        ava = [[i, j] for i in range(3) for j in range(3) if self.IsAbleFill(i, j)]
        avaSpot = ava[randint(0, len(ava)-1)]
        self.Board[avaSpot[0]][avaSpot[1]] = self.AI
    def FindAvaSpot(self, symbol : str):
        for i in range(3):
            if self.Board[i][0] == symbol and self.Board[i][1] == symbol and self.IsAbleFill(i, 2):
                return [i, 2]
            elif self.Board[i][2] == symbol and self.Board[i][1] == symbol and self.IsAbleFill(i, 0):
                return [i, 0]
            elif self.Board[0][i] == symbol and self.Board[1][i] == symbol and self.IsAbleFill(2, i):
                return [2, i]
            elif self.Board[2][i] == symbol and self.Board[1][i] == symbol and self.IsAbleFill(0, i):
                return [0, i]
            elif self.Board[i][0] == symbol and self.Board[i][2] == symbol and self.IsAbleFill(i, 1):
                return [i, 1]
            elif self.Board[0][i] == symbol and self.Board[2][i] == symbol and self.IsAbleFill(1, i):
                return [1, i]
        if self.Board[0][0] == symbol and self.Board[1][1] == symbol and self.IsAbleFill(2, 2):
            return [0, 0]
        elif self.Board[2][2] == symbol and self.Board[1][1] == symbol and self.Board[0][0]:
            return [2, 2]
        elif self.Board[0][2] == symbol and self.Board[1][1] == symbol and self.IsAbleFill(2, 0):
            return [2, 0]
        elif self.Board[2][0] == symbol and self.Board[1][1] == symbol and self.IsAbleFill(0, 2):
            return [0, 2]
        return []
    def MiniMaxCheckWinner(self) -> str:
        for i in range(3):
            if self.Board[i][0] == self.Board[i][1] and self.Board[i][1] == self.Board[i][2]:
                return self.Board[i][0]
            elif self.Board[0][i] == self.Board[1][i] and self.Board[1][i] == self.Board[2][i]:
                return self.Board[0][i]
        if self.Board[0][0] == self.Board[1][1] and self.Board[2][2]:
            return self.Board[0][0]
        elif self.Board[0][2] == self.Board[1][1] and self.Board[2][0]:
            return self.Board[0][2]
        return None
    # The Algorithm of MiniMax (Might Slow)
    def MiniMax(self, ismaxing : bool, alpha : int, beta : int) -> int:
        if self.MiniMaxCheckWinner() == self.AI:
            return 1
        if self.MiniMaxCheckWinner() == self.Player:
            return -1
        if self.IsTie():
            return 0
        if ismaxing:
            maxscore = -inf
            for i in range(3):
                for j in range(3):
                    if self.IsAbleFill:
                        temp = self.Board[i][j]
                        self.Board[i][j] = self.AI
                        score = self.MiniMax(False, alpha, beta)
                        maxscore = max(score, maxscore)
                        self.Board[i][j] = temp
                        alpha = max(alpha, score)
                        if beta <= alpha:
                            break
            return maxscore
        else:
            minscore = inf
            for i in range(3):
                for j in range(3):
                    if self.IsAbleFill(i, j):
                        temp = self.Board[i][j]
                        self.Board[i][j] = self.Player
                        score = self.MiniMax(True, alpha, beta)
                        minscore = min(score, minscore)
                        self.Board[i][j] = temp
                        beta = min(beta, score)
                        if beta <= alpha:
                            break
            return minscore
    def AIFill(self):
        match self.Diff:
            case "e":
                self.EasyAIFill()
            case "m":
                WinSpot = self.FindAvaSpot(self.AI)
                if WinSpot:
                    self.Board[WinSpot[0]][WinSpot[1]] = self.AI
                    return
                BlockSpot = self.FindAvaSpot(self.Player)
                if BlockSpot:
                    self.Board[BlockSpot[0]][BlockSpot[1]] = self.AI
                    return
                for i in range(3):
                    for j in range(3):
                        if self.IsAbleFill(i, j):
                            self.Board[i][j] = self.AI
                            return
            case "h":
                bestscore = -inf
                bestfill = None
                for i in range(3):
                    for j in range(3):
                        if self.IsAbleFill(i, j):
                            temp = self.Board[i][j]
                            self.Board[i][j] = self.AI
                            score = self.MiniMax(False, -inf, inf)
                            if score > bestscore:
                                bestscore = score
                                bestfill = [i, j]
                            self.Board[i][j] = temp
                if bestfill:
                    self.Board[bestfill[0]][bestfill[1]] = self.AI
    def AutoPlayRound(self):
        match self.Turn:
            case self.Player:
                while True:
                    row, col = None, None
                    plrcin = int(input(f"Player Turn! Currently Player is : {self.Player}\n Choose Board to Fill in From 1-9\n input Here : "))
                    if plrcin > 9 or plrcin < 1 or not plrcin:
                        print("invaild input")
                        continue
                    if plrcin <= 3:
                        row, col = 0, plrcin - 1
                        if not self.IsAbleFill(row, col):
                            print("Board Already Filled Choose Another To Fill")
                            continue
                        self.PlayerFill(row, col)
                        break
                    elif plrcin <= 6:
                        row, col = 1, plrcin - 4
                        if not self.IsAbleFill(row, col):
                            print("Board Already Filled Choose Another To Fill")
                            continue
                        self.PlayerFill(row, col)
                        break
                    elif plrcin <= 9:
                        row, col = 2, plrcin - 7
                        if not self.IsAbleFill(row, col):
                            print("Board Already Filled Choose Another To Fill")
                            continue
                        self.PlayerFill(row, col)
                        break
                self.PrevPlayed = self.Player
                self.Turn = self.AI
            case self.AI:
                print("AI Turn!..AI Is Thinking And Choosing..")
                self.AIFill()
                self.PrevPlayed = self.AI
                self.Turn = self.Player
    def StartGame(self):
        self.ChooseTeam()
        self.SelectDiff()
        self.StartTurn()
        while True:
            self.DrawBoard()
            if self.IsGameOver():
                print(f"Game Over Winner : {self.PrevPlayed}")
                break
            if self.IsTie():
                print("Game Tie!")
                break
            self.AutoPlayRound()
#Test Result
if __name__ == "__main__":
    print(figlet_format("TicTacToe..."))
    ttt1 = tictactoe()
    ttt1.StartGame()
