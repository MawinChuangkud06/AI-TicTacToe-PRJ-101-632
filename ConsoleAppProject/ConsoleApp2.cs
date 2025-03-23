using System;
using System.Linq;
using System.Collections.Generic;
using System.Numerics;

public class TicTacToe
{
    private char[,] board;
    private char Player, AI, PrevPlayed, Turn, Diff;
    private Random rand;
    public TicTacToe()
    {
        board = new char[3, 3] {
            {'1', '2', '3'},
            { '4', '5', '6'},
            { '7', '8', '9'}
        };
        rand = new Random();
    }
    public void ChooseGameModeAndPlay()
    {
        int n;
        Console.Write("Choose the game mode\n1: Play Alone\n2: Play With AI : ");
        n = int.Parse(Console.ReadLine());
        Console.WriteLine();
        if (n == 1)
        {
            this.StartAloneGame();
        }
        else if (n == 2)
        {
            this.StartAIGame();
        }
        else
        {
            Console.WriteLine("Invalid Choice!");
        }
    }
    public void StartAIGame()
    {
        this.ChooseTeam();
        this.ChooseDiff();
        this.StartTurn();
        while (true)
        {
            this.PrintBoard();
            if (this.IsGameOver())
            {
                Console.WriteLine("Game Over Winner is : " + this.PrevPlayed);
            }
            if (this.IsTie())
            {
                Console.WriteLine("Game Over It's a Tie!");
            }
            this.AutoPlayRoundForAI();
        }

    }
    public void StartAloneGame()
    {
        this.ChooseTeam();
        while (true)
        {
            this.PrintBoard();
            if (this.IsGameOver())
            {
                Console.WriteLine("Game Over Winner is : " + this.PrevPlayed);
                break;
            }
            if (this.IsTie())
            {
                Console.WriteLine("Game Over It's a Tie!");
                break;
            }
            this.AutoPlayRoundForPlayer();
        }
    }
    // private
    private void PrintBoard()
    {
        Console.WriteLine(new string('-', 13));
        for (int i = 0; i < 3; i++)
        {
            Console.WriteLine($"| {board[i, 0]} | {board[i, 1]} | {board[i, 2]} |");
        }
        Console.WriteLine(new string('-', 13));
    }

    private void ChooseTeam()
    {
        char choice;
        Console.Write("Choose your team X or O : ");
        choice = char.ToUpper(Console.ReadKey().KeyChar);
        Console.WriteLine();
        while (choice != 'X' && choice != 'O')
        {
            Console.Write("\nInvalid choice, Choose your team X or O : ");
            choice = char.ToUpper(Console.ReadKey().KeyChar);
        }
        this.Player = choice;
        this.AI = (choice == 'X') ? 'O' : 'X';
    }

    private void ChooseDiff()
    {
        char choice;
        char[] diffs = { 'E', 'M', 'H' };
        Console.Write("Choose the difficulty E, M or H : ");
        choice = char.ToUpper(Console.ReadKey().KeyChar);
        Console.WriteLine();
        while (!diffs.Contains(choice))
        {
            Console.Write("\nInvalid choice, Choose the difficulty E, M or H : ");
            choice = char.ToUpper(Console.ReadKey().KeyChar);
        }
        this.Diff = choice;
    }

    private void StartTurn()
    {
        int n = rand.Next(0, 1);
        this.Turn = (n == 0) ? this.Player : this.AI;
    }

    private bool IsAbleToFill(int row, int col)
    {
        return board[row, col] != 'X' && board[row, col] != 'O';
    }
    private bool IsTie()
    {
        for (int i = 0; i < 3; i++)
        {
            for (int j = 0; j < 3; j++)
            {
                if (this.IsAbleToFill(i, j)) return false;
            }
        }
        return true;
    }
    private bool IsGameOver()
    {
        for (int i = 0; i < 3; i++)
        {
            // Check Horizontal
            if (board[i, 0] == board[i, 1] && board[i, 1] == board[i, 2]) return true;
            // Check Vertical
            if (board[0, i] == board[1, i] && board[1, i] == board[2, i]) return true;
        }
        // Check Side Way
        if (board[0, 0] == board[1, 1] && board[1, 1] == board[2, 2]) return true;
        if (board[0, 2] == board[1, 1] && board[1, 1] == board[2, 0]) return true;
        return false;
    }
    private void PlayerFill(int row, int col)
    {
        if (this.IsAbleToFill(row, col))
        {
            board[row, col] = this.Player;
        }
    }
    private List<int> FindAvaSpot(char symbol)
    {
        for (int i = 0; i < 3; i++)
        {
            if (board[i, 0] == symbol && board[i, 1] == symbol && this.IsAbleToFill(i, 2))
            {
                return new List<int> { i, 2 };
            }
            if (board[i, 1] == symbol && board[i, 2] == symbol && this.IsAbleToFill(i, 0))
            {
                return new List<int> { i, 0 };
            }
            if (board[i, 0] == symbol && board[i, 2] == symbol && this.IsAbleToFill(i, 1))
            {
                return new List<int> { i, 1 };
            }
            if (board[0, i] == symbol && board[1, i] == symbol && this.IsAbleToFill(2, i))
            {
                return new List<int> { 2, i };
            }
            if (board[1, i] == symbol && board[2, i] == symbol && this.IsAbleToFill(0, i))
            {
                return new List<int> { 0, i };
            }
            if (board[0, i] == symbol && board[2, i] == symbol && this.IsAbleToFill(1, i))
            {
                return new List<int> { 1, i };
            }
        }
        if (board[0, 0] == symbol && board[1, 1] == symbol && this.IsAbleToFill(2, 2))
        {
            return new List<int> { 2, 2 };
        }
        if (board[1, 1] == symbol && board[2, 2] == symbol && this.IsAbleToFill(0, 0))
        {
            return new List<int> { 0, 0 };
        }
        if (board[0, 0] == symbol && board[2, 2] == symbol && this.IsAbleToFill(1, 1))
        {
            return new List<int> { 1, 1 };
        }
        if (board[0, 2] == symbol && board[1, 1] == symbol && this.IsAbleToFill(2, 0))
        {
            return new List<int> { 2, 0 };
        }
        if (board[1, 1] == symbol && board[2, 0] == symbol && this.IsAbleToFill(0, 2))
        {
            return new List<int> { 0, 2 };
        }
        if (board[0, 2] == symbol && board[2, 0] == symbol && this.IsAbleToFill(1, 1))
        {
            return new List<int> { 1, 1 };
        }
        return new List<int> { -1, -1 };
    }

    private List<List<int>> GetAvaSpotForEasyAI()
    {
        List<List<int>> li = new List<List<int>>();
        for (int i = 0; i < 3; i++)
        {
            for (int j = 0; j < 3; j++)
            {
                if (this.IsAbleToFill(i, j))
                {
                    li.Add(new List<int> { i, j });
                }
            }
        }
        return li;
    }
    private void AIEasyFill()
    {
        List<List<int>> li = this.GetAvaSpotForEasyAI();
        int n = rand.Next(0, li.Count);
        board[li[n][0], li[n][1]] = this.AI;
    }

    private char MiniMaxCheckWinner()
    {
        for (int i = 0; i < 3; i++)
        {
            // Check Horizontal
            if (board[i, 0] == board[i, 1] && board[i, 1] == board[i, 2]) return board[i, 0];
            // Check Vertical
            if (board[0, i] == board[1, i] && board[1, i] == board[2, i]) return board[0, i];
        }
        // Check Side Way
        if (board[0, 0] == board[1, 1] && board[1, 1] == board[2, 2]) return board[0, 0];
        if (board[0, 2] == board[1, 1] && board[1, 1] == board[2, 0]) return board[0, 2];
        return ' ';
    }
    private int MiniMax(bool ismaxing, long alpha, long beta, ulong depth)
    {
        if (this.MiniMaxCheckWinner() == this.AI)
        {
            return 1 - (int)depth;
        }
        if (this.MiniMaxCheckWinner() == this.Player)
        {
            return -1 + (int)depth;
        }
        if (this.IsTie())
        {
            return 0 + (int)depth;
        }
        if (ismaxing)
        {
            int bestScore = -1000;
            for (int i = 0; i < 3; i++)
            {
                for (int j = 0; j < 3; j++)
                {
                    if (this.IsAbleToFill(i, j))
                    {
                        board[i, j] = this.AI;
                        int score = this.MiniMax(false, alpha, beta, depth + 1);
                        board[i, j] = (char)(i * 3 + j + 1 + '0');
                        bestScore = Math.Max(score, bestScore);
                        alpha = Math.Max(alpha, bestScore);
                        if (beta <= alpha)
                        {
                            break;
                        }
                    }
                }
            }
            return bestScore;
        }
        else
        {
            int bestScore = 1000;
            for (int i = 0; i < 3; i++)
            {
                for (int j = 0; j < 3; j++)
                {
                    if (this.IsAbleToFill(i, j))
                    {
                        board[i, j] = this.Player;
                        int score = this.MiniMax(true, alpha, beta, depth + 1);
                        board[i, j] = (char)(i * 3 + j + 1 + '0');
                        bestScore = Math.Min(score, bestScore);
                        beta = Math.Min(beta, bestScore);
                        if (beta <= alpha)
                        {
                            break;
                        }
                    }
                }
            }
            return bestScore;
        }
    }
    private void AIFill()
    {
        switch (this.Diff)
        {
            case 'E':
                this.AIEasyFill();
                break;
            case 'M':
                List<int> avaAI = this.FindAvaSpot(this.AI);
                if (avaAI[0] != -1 && avaAI[1] != -1)
                {
                    board[avaAI[0], avaAI[1]] = this.AI;
                    return;
                }
                List<int> avaPlayer = this.FindAvaSpot(this.Player);
                if (avaPlayer[0] != -1 && avaPlayer[1] != -1)
                {
                    board[avaPlayer[0], avaPlayer[1]] = this.AI;
                    return;
                }
                for (int i = 0; i < 3; i++)
                {
                    for (int j = 0; j < 3; j++)
                    {
                        if (this.IsAbleToFill(i, j))
                        {
                            this.board[i, j] = this.AI;
                            return;
                        }
                    }
                }
                break;
            case 'H':
                int bestScore = -1000;
                List<int> bestMove = new List<int> { -1, -1 };
                for (int i = 0; i < 3; i++)
                {
                    for (int j = 0; j < 3; j++)
                    {
                        if (this.IsAbleToFill(i, j))
                        {
                            board[i, j] = this.AI;
                            int score = this.MiniMax(false, -1000, 1000, 0);
                            board[i, j] = (char)(i * 3 + j + 1 + '0');
                            if (score > bestScore)
                            {
                                bestScore = score;
                                bestMove = new List<int> { i, j };
                            }
                        }
                    }
                }
                board[bestMove[0], bestMove[1]] = this.AI;
                break;
        }
    }
    private void SwitchPlayerTeam()
    {
        this.Player = (this.Player == 'X') ? 'O' : 'X';
    }
    private void AutoPlayRoundForPlayer()
    {
        int plrCin;
        Console.WriteLine("Player Turn, Current Player is : " + this.Player);
        Console.Write("Enter the number of the spot : ");
        plrCin = int.Parse(Console.ReadLine());
        Console.WriteLine();
        while (plrCin < 1 || plrCin > 9 || !this.IsAbleToFill((plrCin - 1) / 3, (plrCin - 1) % 3))
        {
            Console.Write("Invalid spot, Enter the number of the spot : ");
            plrCin = int.Parse(Console.ReadLine());
        }
        this.PlayerFill((plrCin - 1) / 3, (plrCin - 1) % 3);
        this.PrevPlayed = this.Player;
        this.SwitchPlayerTeam();
    }
    private void AutoPlayRoundForAI()
    {
        if (this.Turn == this.Player)
        {
            int n;
            Console.WriteLine("Player Turn, Current Player is : " + this.Player);
            Console.Write("Enter the number of the spot : ");
            n = int.Parse(Console.ReadLine());
            Console.WriteLine();
            while (n < 1 || n > 9 || !this.IsAbleToFill((n - 1) / 3, (n - 1) % 3))
            {
                Console.Write("Invalid spot, Enter the number of the spot : ");
                n = int.Parse(Console.ReadLine());
            }
            this.PlayerFill((n - 1) / 3, (n - 1) % 3);
            this.PrevPlayed = this.Player;
            this.Turn = this.AI;
        }
        else
        {
            Console.WriteLine("AI Turn! AI is Thinking and Choosing..");
            this.AIFill();
            this.PrevPlayed = this.AI;
            this.Turn = this.Player;
        }
    }

}
public class Program
{
    public static void Main()
    {
        TicTacToe T1 = new TicTacToe();
        T1.ChooseGameModeAndPlay();
    }
}
