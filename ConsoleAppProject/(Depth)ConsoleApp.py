#This Python Code Contain pyfiglet
#Also Install pyfiglet lib use pip install pyfiglet in terminal
#This Code Below Is The Code Without Depth if you Dont Like the Depth One You Can Run This Code Below
"""
from math import inf
from random import randint
from pyfiglet import figlet_format
class TicTacToe:
    def __init__(self):
        self.Board = [
            [1,2,3],
            [4,5,6],
            [7,8,9]
        ]
        self.Player = None
        self.AI = None
        self.Diff = None
        self.Turn = None
        self.PrevPlayed = None

    def DrawBoard(self):
        print("-"*13)
        for i in range(3):
           print(f"| {self.Board[i][0]} | {self.Board[i][1]} | {self.Board[i][2]} |")
        print("-"*13)
    
    def ChooseTeam(self):
        while True:
            n = input("Choose You Team (O or X) : ").upper()
            vaildteam = ["O", "X"]
            if n not in vaildteam:
                print("Invaild Team try Again")
                continue
            self.Player = n
            self.AI = "O" if self.Player == "X" else "X"
            break
    
    def ChooseDiff(self):
        while True:
            n = input("Choose You Diff For The AI\ne: Easy\nm: Meduim\nh: Hard\ninput Here : ").lower()
            vaildiff = ['e', 'm', 'h']
            if n not in vaildiff:
                print("Invaild Diff Try Again")
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
    
    def IsAbleToFill(self, row : int, col : int) -> bool:
        return type(self.Board[row][col]) == int
    
    def PlayerFill(self, row, col) -> bool:
        if not self.IsAbleToFill(row, col):
            return
        else:
            self.Board[row][col] = self.Player
    
    def MiniMaxCheckWinner(self):
        for i in range(3):
            if self.Board[i][0] == self.Board[i][1] and self.Board[i][1] == self.Board[i][2]:
                return self.Board[i][0]
            elif self.Board[0][i] == self.Board[1][i] and self.Board[1][i] == self.Board[2][i]:
                return self.Board[0][i]
        if self.Board[0][0] == self.Board[1][1] and self.Board[1][1] == self.Board[2][2]:
            return self.Board[0][0]
        elif self.Board[0][2] == self.Board[1][1] and self.Board[1][1] == self.Board[2][0]:
            return self.Board[0][2]
        return None
    
    def FindAvaSpot(self, symbol : str):
        for i in range(3):
            # Straight Line
            if self.Board[i][0] == symbol and self.Board[i][1] == symbol and self.IsAbleToFill(i, 2):
                return [i, 2]
            elif self.Board[i][2] == symbol and self.Board[i][1] == symbol and self.IsAbleToFill(i, 0):
                return [i, 0]
            elif self.Board[i][2] == symbol and self.Board[i][0] == symbol and self.IsAbleToFill(i, 1):
                return [i, 1]
            #Vertical Line
            elif self.Board[0][i] == symbol and self.Board[1][i] == symbol and self.IsAbleToFill(2, i):
                return [2, i]
            elif self.Board[2][i] == symbol and self.Board[1][i] == symbol and self.IsAbleToFill(0, i):
                return [0, i]
            elif self.Board[2][i] == symbol and self.Board[0][i] == symbol and self.IsAbleToFill(1, i):
                return [1, i]
        # More
        # Side 1
        if self.Board[0][0] == symbol and self.Board[1][1] == symbol and self.IsAbleToFill(2, 2):
            return [2, 2]
        elif self.Board[2][2] == symbol and self.Board[1][1] == symbol and self.IsAbleToFill(0, 0):
            return [0, 0]
        elif self.Board[2][2] == symbol and self.Board[0][0] == symbol and self.IsAbleToFill(1, 1):
            return [1, 1]
        # Side 2
        elif self.Board[0][2] == symbol and self.Board[1][1] == symbol and self.IsAbleToFill(2, 0):
            return [2, 0]
        elif self.Board[2][0] == symbol and self.Board[1][1] == symbol and self.IsAbleToFill(0, 2):
            return [0, 2]
        elif self.Board[0][2] == symbol and self.Board[2][0] == symbol and self.IsAbleToFill(1, 1):
            return [1, 1]
        return None
    
    def MiniMax(self, ismaxing, alpha : int , beta : int):
        if self.MiniMaxCheckWinner() == self.AI:
            return 1
        if self.MiniMaxCheckWinner() == self.Player:
            return -1
        if self.IsTie():
            return 0
        # The Algorithm
        if ismaxing:
            # When ismaxing is True
            # AI Do the AI TestCase
            maxscore = -inf
            for i in range(3):
                for j in range(3):
                    if self.IsAbleToFill(i, j):
                        temp = self.Board[i][j]
                        self.Board[i][j] = self.AI
                        score = self.MiniMax(False, alpha, beta)
                        maxscore = max(score, maxscore)
                        alpha = max(alpha, score)
                        self.Board[i][j] = temp
                        if beta <= alpha:
                            break
            return maxscore
        else:
            minscore = inf
            for i in range(3):
                for j in range(3):
                    if self.IsAbleToFill(i, j):
                        temp = self.Board[i][j]
                        self.Board[i][j] = self.Player
                        score = self.MiniMax(True, alpha, beta)
                        minscore = min(score, minscore)
                        beta = min(beta, score)
                        self.Board[i][j] = temp
                        if beta <= alpha:
                            break
            return minscore

    def AIEasyFill(self):
        ava = [[i, j] for i in range(3) for j in range(3) if self.IsAbleToFill(i, j)]
        avaspot = ava[randint(0, len(ava)-1)]
        self.Board[avaspot[0]][avaspot[1]] = self.AI
    
    def AIFill(self):
        match self.Diff:
            case 'e':
                self.AIEasyFill()
            case 'm':
                avaAI = self.FindAvaSpot(self.AI)
                if avaAI:
                    self.Board[avaAI[0]][avaAI[1]] = self.AI
                    return
                avaPlayer = self.FindAvaSpot(self.Player)
                if avaPlayer:
                    self.Board[avaPlayer[0]][avaPlayer[1]] = self.AI
                    return
                # This Code Below Run For The Start of The Game
                for i in range(3):
                    for j in range(3):
                        if self.IsAbleToFill(i, j):
                            self.Board[i][j] = self.AI
                            return
            case "h":
                bestfill = []
                bestscore = -inf
                for i in range(3):
                    for j in range(3):
                        if self.IsAbleToFill(i, j):
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
        if self.Turn == self.Player:
            while True:
                try:
                    plrcin = int(input(f"Player Turn! Currently Player is : {self.Player}\n Choose Board to Fill in From 1-9\n input Here : "))
                    if plrcin < 1 or plrcin > 9:
                        print("Invalid input, please choose a number between 1 and 9.")
                        continue
                    row, col = (plrcin - 1) // 3, (plrcin - 1) % 3
                    if not self.IsAbleToFill(row, col):
                        print("Board already filled, choose another spot.")
                        continue
                    self.PlayerFill(row, col)
                    break
                except ValueError:
                    print("Invalid input, please enter a number.")
            self.PrevPlayed = self.Player
            self.Turn = self.AI
        else:
            print("AI Turn!..AI Is Thinking And Choosing..")
            self.AIFill()
            self.PrevPlayed = self.AI
            self.Turn = self.Player

    def StartAIGame(self):
        self.ChooseTeam()
        self.ChooseDiff()
        while True:
            self.DrawBoard()
            if self.IsGameOver():
                print("Game Over! The Winner is {}".format(self.PrevPlayed))
                break
            if self.IsTie():
                print("Game Tie!")
                break
            self.AutoPlayRound()
                
# Test Result
if __name__ == "__main__": 
    print(figlet_format("TicTacToe..."))
    ttt1 = TicTacToe()
    ttt1.StartAIGame()
"""
#This Code Below is The Code With Depth Algorithm I dont use Node Since Is Doesnt matter Cus My Code Working Fine
from math import inf
from random import randint
from pyfiglet import figlet_format
class TicTacToe:
    def __init__(self):
        self.Board = [
            [1,2,3],
            [4,5,6],
            [7,8,9]
        ]
        self.Player = None
        self.AI = None
        self.Diff = None
        self.Turn = None
        self.PrevPlayed = None

    def DrawBoard(self):
        print("-"*13)
        for i in range(3):
           print(f"| {self.Board[i][0]} | {self.Board[i][1]} | {self.Board[i][2]} |")
        print("-"*13)
    
    def ChooseTeam(self):
        while True:
            n = input("Choose You Team (O or X) : ").upper()
            vaildteam = ["O", "X"]
            if n not in vaildteam:
                print("Invaild Team try Again")
                continue
            self.Player = n
            self.AI = "O" if self.Player == "X" else "X"
            break
    
    def ChooseDiff(self):
        while True:
            n = input("Choose You Diff For The AI\ne: Easy\nm: Meduim\nh: Hard\ninput Here : ").lower()
            vaildiff = ['e', 'm', 'h']
            if n not in vaildiff:
                print("Invaild Diff Try Again")
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
    
    def IsAbleToFill(self, row : int, col : int) -> bool:
        return type(self.Board[row][col]) == int
    
    def PlayerFill(self, row, col) -> bool:
        if not self.IsAbleToFill(row, col):
            return
        else:
            self.Board[row][col] = self.Player
    
    def MiniMaxCheckWinner(self):
        for i in range(3):
            if self.Board[i][0] == self.Board[i][1] and self.Board[i][1] == self.Board[i][2]:
                return self.Board[i][0]
            elif self.Board[0][i] == self.Board[1][i] and self.Board[1][i] == self.Board[2][i]:
                return self.Board[0][i]
        if self.Board[0][0] == self.Board[1][1] and self.Board[1][1] == self.Board[2][2]:
            return self.Board[0][0]
        elif self.Board[0][2] == self.Board[1][1] and self.Board[1][1] == self.Board[2][0]:
            return self.Board[0][2]
        return None
    
    def FindAvaSpot(self, symbol : str):
        for i in range(3):
            # Straight Line
            if self.Board[i][0] == symbol and self.Board[i][1] == symbol and self.IsAbleToFill(i, 2):
                return [i, 2]
            elif self.Board[i][2] == symbol and self.Board[i][1] == symbol and self.IsAbleToFill(i, 0):
                return [i, 0]
            elif self.Board[i][2] == symbol and self.Board[i][0] == symbol and self.IsAbleToFill(i, 1):
                return [i, 1]
            #Vertical Line
            elif self.Board[0][i] == symbol and self.Board[1][i] == symbol and self.IsAbleToFill(2, i):
                return [2, i]
            elif self.Board[2][i] == symbol and self.Board[1][i] == symbol and self.IsAbleToFill(0, i):
                return [0, i]
            elif self.Board[2][i] == symbol and self.Board[0][i] == symbol and self.IsAbleToFill(1, i):
                return [1, i]
        # More
        # Side 1
        if self.Board[0][0] == symbol and self.Board[1][1] == symbol and self.IsAbleToFill(2, 2):
            return [2, 2]
        elif self.Board[2][2] == symbol and self.Board[1][1] == symbol and self.IsAbleToFill(0, 0):
            return [0, 0]
        elif self.Board[2][2] == symbol and self.Board[0][0] == symbol and self.IsAbleToFill(1, 1):
            return [1, 1]
        # Side 2
        elif self.Board[0][2] == symbol and self.Board[1][1] == symbol and self.IsAbleToFill(2, 0):
            return [2, 0]
        elif self.Board[2][0] == symbol and self.Board[1][1] == symbol and self.IsAbleToFill(0, 2):
            return [0, 2]
        elif self.Board[0][2] == symbol and self.Board[2][0] == symbol and self.IsAbleToFill(1, 1):
            return [1, 1]
        return None
    
    def MiniMax(self, ismaxing, alpha : int , beta : int, depth : int):
        winner = self.MiniMaxCheckWinner()
        if winner == self.AI:
            return 1 - depth
        if winner == self.Player:
            return -1 + depth
        if self.IsTie():
            return 0
        # The Algorithm
        if ismaxing:
            # When ismaxing is True
            # AI Do the AI TestCase
            maxscore = -inf
            for i in range(3):
                for j in range(3):
                    if self.IsAbleToFill(i, j):
                        temp = self.Board[i][j]
                        self.Board[i][j] = self.AI
                        score = self.MiniMax(False, alpha, beta, depth+1)
                        maxscore = max(score, maxscore)
                        alpha = max(alpha, score)
                        self.Board[i][j] = temp
                        if beta <= alpha:
                            break
            return maxscore
        else:
            minscore = inf
            for i in range(3):
                for j in range(3):
                    if self.IsAbleToFill(i, j):
                        temp = self.Board[i][j]
                        self.Board[i][j] = self.Player
                        score = self.MiniMax(True, alpha, beta, depth + 1)
                        minscore = min(score, minscore)
                        beta = min(beta, score)
                        self.Board[i][j] = temp
                        if beta <= alpha:
                            break
            return minscore

    def AIEasyFill(self):
        ava = [[i, j] for i in range(3) for j in range(3) if self.IsAbleToFill(i, j)]
        avaspot = ava[randint(0, len(ava)-1)]
        self.Board[avaspot[0]][avaspot[1]] = self.AI
    
    def AIFill(self):
        match self.Diff:
            case 'e':
                self.AIEasyFill()
            case 'm':
                avaAI = self.FindAvaSpot(self.AI)
                if avaAI:
                    self.Board[avaAI[0]][avaAI[1]] = self.AI
                    return
                avaPlayer = self.FindAvaSpot(self.Player)
                if avaPlayer:
                    self.Board[avaPlayer[0]][avaPlayer[1]] = self.AI
                    return
                # This Code Below Run For The Start of The Game
                for i in range(3):
                    for j in range(3):
                        if self.IsAbleToFill(i, j):
                            self.Board[i][j] = self.AI
                            return
            case "h":
                bestfill = []
                bestscore = -inf
                for i in range(3):
                    for j in range(3):
                        if self.IsAbleToFill(i, j):
                            temp = self.Board[i][j]
                            self.Board[i][j] = self.AI
                            score = self.MiniMax(False, -inf, inf, 0)
                            if score > bestscore:
                                bestscore = score
                                bestfill = [i, j]
                            self.Board[i][j] = temp
                if bestfill:
                    self.Board[bestfill[0]][bestfill[1]] = self.AI

    def AutoPlayRound(self):
        if self.Turn == self.Player:
            while True:
                try:
                    plrcin = int(input(f"Player Turn! Currently Player is : {self.Player}\n Choose Board to Fill in From 1-9\n input Here : "))
                    if plrcin < 1 or plrcin > 9:
                        print("Invalid input, please choose a number between 1 and 9.")
                        continue
                    row, col = (plrcin - 1) // 3, (plrcin - 1) % 3
                    if not self.IsAbleToFill(row, col):
                        print("Board already filled, choose another spot.")
                        continue
                    self.PlayerFill(row, col)
                    break
                except ValueError:
                    print("Invalid input, please enter a number.")
            self.PrevPlayed = self.Player
            self.Turn = self.AI
        else:
            print("AI Turn!..AI Is Thinking And Choosing..")
            self.AIFill()
            self.PrevPlayed = self.AI
            self.Turn = self.Player

    def StartAIGame(self):
        self.ChooseTeam()
        self.ChooseDiff()
        while True:
            self.DrawBoard()
            if self.IsGameOver():
                print("Game Over! The Winner is {}".format(self.PrevPlayed))
                break
            if self.IsTie():
                print("Game Tie!")
                break
            self.AutoPlayRound()
                
# Test Result
if __name__ == "__main__": 
    print(figlet_format("TicTacToe..."))
    ttt1 = TicTacToe()
    ttt1.StartAIGame()
