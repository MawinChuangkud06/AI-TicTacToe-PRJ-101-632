#include<iostream>
#include<ios>
#include<cstdio>
#include<ctime>
#include<utility>
#include<string>
#include<cstring>
#include<vector>
#include<algorithm>
#include<cmath>
#define ll long long

// This Code Below is Unfixed One
/*#ifndef TICTACTOE_H
#define TICTACTOE_H
class TicTacToe
{
    public:
        char Player;
        char AI;
        char Turn;
        char PrevPlayed;
        char Diff;
        char Board[3][3];
        TicTacToe()
        {
            memcpy(this->Board, (char[3][3]){{'1', '2', '3'}, {'4', '5', '6'}, {'7', '8', '9'}}, sizeof(this->Board));
            std::srand(time(0));
        }

        void ChooseGameModeAndPlay()
        {
            std::cout<<"Choose GameMode\n1: Play Alone\n2: Play With AI\ninput Here : ";
            int n;
            again:
            std::cin>>n;
            switch (n)
            {
                case 1:
                    this->StartAloneGame();
                    break;
                case 2:
                    this->StartAIGame();
                    break;
                default:
                    std::cout<<"invaild Gamemode Choose Again"<<std::endl;
                    goto again;
                    break;
            }
        }

        void StartAIGame()
        {
            while (true)
            {
                this->PrintBoard();
                if (this->IsGameOver())
                {
                    std::cout<<"Game Over Winner : "<<this->PrevPlayed<<std::endl;
                    break;
                }
                if (this->IsTie())
                {
                    std::cout<<"Game Tie!"<<std::endl;
                    break;
                }
                this->AutoPlayRoundForAI();
            }
        }
        
        void StartAloneGame()
        {
            while (true)
            {
                this->PrintBoard();
                if (this->IsGameOver())
                {
                    std::cout<<"Game Over Winner : "<<this->PrevPlayed<<std::endl;
                    break;
                }
                if (this->IsTie())
                {
                    std::cout<<"Game Tie!"<<std::endl;
                    break;
                }
                this->AutoPlayRoundForPlayer();
            }
        }

    private:
        void PrintBoard()
        {
            for (int i = 0;i<13;i++)
            {
                std::cout<<'-';
            }
            std::cout<<std::endl;
            for (int i = 0;i<3;i++)
            {
                std::cout<<"| "<<this->Board[i][0]<<" | "<<this->Board[i][1]<<" | "<<this->Board[i][2]<<" |"<<std::endl;
            }
            for (int i = 0;i<13;i++)
            {
                std::cout<<'-';
            }
        }

        void ChooseTeam()
        {
            char n;
            again:
            std::cout<<"Choose You Team (O or X) : ";
            std::cin>>n;
            std::cout<<std::endl;
            n = std::toupper(n);
            if (n != 'O' && n != 'X') 
            {
                std::cout<<"invaild Team Try Again"<<std::endl;
                goto again;
            }

            this->Player = n;
            this->AI = (n == 'X') ? 'O' : 'X';
        }

        void StartTurn()
        {
            unsigned int n = std::rand() % 2;
            this->Turn = (n == 0) ? this->Player : this->AI;
        }

        void ChooseDiff()
        {
            char n;
            again:
            std::cout<<"Choose You AI Diff : ";
            std::cin>>n;
            std::cout<<std::endl;
            n = std::tolower(n);
            if (n != 'e' && n != 'm' && n != 'h')
            {
                std::cout<<"invaild Diff"<<std::endl;
                goto again;
            }
            this->Diff=n;
        }
        bool IsAbleToFill(unsigned int row, unsigned int col)
        {
            if (this->Board[row][col] >= '1' && this->Board[row][col] <= '9')
            {
                return true;
            } else {
                return false;
            }
        }

        bool IsGameOver()
        {
            for (int i = 0;i<3;i++)
            {
                if (this->Board[i][0] == this->Board[i][1] && this->Board[i][1] == this->Board[i][2])
                {
                    return true;
                } else if (this->Board[0][i] == this->Board[1][i] && this->Board[1][i] == this->Board[2][i])
                {
                    return true;
                }
            }
            if (this->Board[0][0] == this->Board[1][1] && this->Board[1][1] == this->Board[2][2])
            {
                return true;
            } else if (this->Board[0][2] == this->Board[1][1] && this->Board[1][1] == this->Board[2][0])
            {
                return true;
            }

            return false;
        }

        std::vector<std::pair<int, int>> GetAvaForEasyAI()
        {
            std::vector<std::pair<int, int>> vec;
            for (int i = 0;i<3;i++)
            {
                for (int j = 0;j<3;j++)
                {
                    if (IsAbleToFill(i, j))
                    {
                        vec.push_back(std::make_pair(i, j));
                    }
                }
            }
            return vec;
        }

        bool IsTie()
        {
            for (int i = 0;i<3;i++)
            {
                for (int j = 0;j<3;j++)
                {
                    if (this->IsAbleToFill(i, j))
                    {
                        return false;
                    }
                }
            }
            return true;
        }

        void PlayerFill(unsigned int row, unsigned int col)
        {
            // safety
            if (this->IsAbleToFill(row, col))
            {
                this->Board[row][col] = this->Player;
            }
        }

        void AIEasyFill()
        {
            std::vector<std::pair<int, int>> pii = this->GetAvaForEasyAI();
            std::pair<int, int> ava = pii[std::rand() % pii.size()];
            if (ava.first && ava.second)
            {
                this->Board[ava.first][ava.second] = this->AI;
            }
        }

        std::pair<int, int> FindAvaSpot(char symbol)
        {
            for (int i = 0;i<3;i++)
            {
                // Straight Line
                if (this->Board[i][0] == symbol && this->Board[i][1] == symbol && this->IsAbleToFill(i, 2))
                {
                    return std::make_pair(i, 2);
                } else if (this->Board[i][2] == symbol && this->Board[i][1] == symbol && this->IsAbleToFill(i, 0))
                {
                    return std::make_pair(i, 0);
                } else if (this->Board[i][2] == symbol && this->Board[i][0] == symbol && this->Board[i][1])
                {
                    return std::make_pair(i, 1);
                }
                // Vertical Line
                else if (this->Board[0][i] == symbol && this->Board[1][i] == symbol && this->IsAbleToFill(2, i))
                {
                    return std::make_pair(2, i);
                } else if (this->Board[2][i] == symbol && this->Board[1][i] == symbol == symbol && this->IsAbleToFill(0, i))
                {
                    return std::make_pair(0, i);
                } else if (this->Board[2][i] == symbol && this->Board[0][i] == symbol && this->Board[1][i])
                {
                    return std::make_pair(1, i);
                }
            }
            // Side 1
            if (this->Board[0][0] == symbol && this->Board[1][1] == symbol && this->IsAbleToFill(2, 2))
            {
                return std::make_pair(2, 2);
            } else if (this->Board[2][2] == symbol && this->Board[1][1] == symbol && this->IsAbleToFill(0, 0))
            {
                return std::make_pair(0, 0);
            } else if (this->Board[2][2] == symbol && this->Board[0][0] == symbol && this->IsAbleToFill(1, 1))
            {
                return std::make_pair(1, 1);
            } 
            // side 2
            else if (this->Board[0][2] == symbol && this->Board[1][1] == symbol && this->IsAbleToFill(2, 0))
            {
                return std::make_pair(2, 0);
            } else if (this->Board[2][0] == symbol && this->Board[1][1] == symbol && this->IsAbleToFill(0, 2))
            {
                return std::make_pair(0, 2);
            } else if (this->Board[0][2] == symbol && this->Board[2][0] == symbol && this->IsAbleToFill(1, 1))
            {
                return std::make_pair(1, 1);
            }
            return std::make_pair(0, 0);
        }

        long MiniMax(bool ismaxing, ll alpha, ll beta, unsigned long depth)
        {
            char winner = this->MiniMaxCheckWinner();
            if (winner == this->AI) return 1 - depth;
            if (winner == this->Player) return -1 + depth;
            if (IsTie()) return 0;
            if (ismaxing)
            {
                long maxscore = -1000000000;
                for (int i = 0;i<3;i++)
                {
                    for (int j = 0;j<3;j++)
                    {
                        if (this->IsAbleToFill(i, j))
                        {
                            char temp = this->Board[i][j];
                            this->Board[i][j] = this->AI;
                            long score = this->MiniMax(false, alpha, beta, depth+1);
                            if (maxscore < score) maxscore = score;
                            if (alpha < score) alpha = score;
                            this->Board[i][j] = temp;
                            if (beta <= alpha) break;
                        }
                    }
                }
                return maxscore;
            } else {
                long minscore = 100000000;
                for (int i = 0;i<3;i++)
                {
                    for (int j = 0;j<3;j++)
                    {
                        char temp = this->Board[i][j];
                        this->Board[i][j] = this->AI;
                        long score = this->MiniMax(true, alpha, beta, depth+1);
                        if (minscore > score) minscore = score;
                        if (beta > score) beta = score;
                        this->Board[i][j] = temp;
                        if (beta <= alpha) break;
                    }
                }
                return minscore;
            }
        }

        char MiniMaxCheckWinner()
        {
            for (int i = 0;i<3;i++)
            {
                if (this->Board[i][0] == this->Board[i][1] && this->Board[i][1] == this->Board[i][2])
                {
                    return this->Board[i][0];
                } else if (this->Board[0][i] == this->Board[1][i] && this->Board[1][i] == this->Board[2][i])
                {
                    return this->Board[0][i];
                }
            }
            if (this->Board[0][0] == this->Board[1][1] && this->Board[1][1] == this->Board[2][2])
            {
                return this->Board[0][0];
            } else if (this->Board[0][2] == this->Board[1][1] && this->Board[1][1] == this->Board[2][0])
            {
                return this->Board[0][2];
            }

            return ' ';
        }

        void AIFill()
        {
            switch (this->Diff)
            {
                case 'e':
                    this->AIEasyFill();
                    break;
                case 'm':
                {
                    std::pair<int, int> pii_AI = this->FindAvaSpot(this->AI);
                    if (this->IsAbleToFill(pii_AI.first, pii_AI.second))
                    {
                        this->Board[pii_AI.first][pii_AI.second] = this->AI;
                        return;
                    }

                    std::pair<int, int> pii_Player = this->FindAvaSpot(this->Player);
                    if (this->IsAbleToFill(pii_Player.first, pii_Player.second))
                    {
                        this->Board[pii_Player.first][pii_Player.second] = this->AI;
                        return;
                    }

                    // If no winning/blocking move, pick the first available spot.
                    for (int i = 0; i < 3; i++)
                    {
                        for (int j = 0; j < 3; j++)
                        {
                            if (this->IsAbleToFill(i, j))
                            {
                                this->Board[i][j] = this->AI;
                                return;
                            }
                        }
                    }
                    break;
                }
                case 'h':
                {
                    long bestscore = -10000000;  // Initialize minimax best score
                    std::pair<int, int> bestfill = std::make_pair(-1, -1);  // Initialize best move

                    for (int i = 0; i < 3; i++)
                    {
                        for (int j = 0; j < 3; j++)
                        {
                            if (this->IsAbleToFill(i, j))
                            {
                                char temp = this->Board[i][j];
                                this->Board[i][j] = this->AI;
                                long score = this->MiniMax(false, -10000000, 10000000, 0);
                                this->Board[i][j] = temp;

                                if (score > bestscore)
                                {
                                    bestscore = score;
                                    bestfill = std::make_pair(i, j);
                                }
                            }
                        }
                    }

                    // Ensure a move is placed if found
                    if (bestfill.first != -1 && bestfill.second != -1)
                    {
                        this->Board[bestfill.first][bestfill.second] = this->AI;
                    }
                    break;
                }
            }
        }

        // Game

        void SwitchPlayerTeam()
        {
            this->Player = (this->Player == 'O') ? 'X' : 'O';
        }

        void AutoPlayRoundForPlayer()
        {
            int plrCin;
            again:
            std::cin>>plrCin;
            if (plrCin < 1 || plrCin > 9)
            {
                std::cout<<"invaild input please try again"<<std::endl;
                goto again;
            }
            int row = std::floor((plrCin - 1) / 3);
            int col = (plrCin - 1) % 3;
            if (!this->IsAbleToFill(row, col))
            {
                std::cout<<"Board Already filled choose another spot"<<std::endl;
                goto again;
            }
            this->PlayerFill(row, col);
            this->PrevPlayed = this->Player;
            this->SwitchPlayerTeam();
        }

        void AutoPlayRoundForAI()
        {
            if (this->Turn == this->Player)
            {
                int plrCin;
                again:
                std::cin>>plrCin;
                if (plrCin < 1 || plrCin > 9)
                {
                    std::cout<<"invaild input please try again"<<std::endl;
                    goto again;
                }
                int row = std::floor((plrCin - 1) / 3);
                int col = (plrCin - 1) % 3;
                if (!this->IsAbleToFill(row, col))
                {
                    std::cout<<"Board already filled choose Another spot"<<std::endl;
                    goto again;
                }
                this->PlayerFill(row, col);
                this->PrevPlayed = this->Player;
                this->Turn = this->AI;

            } else {
                std::cout<<"AI Turn!..AI is Thinking and Choosing.."<<std::endl;
                this->AIFill();
                this->PrevPlayed = this->AI;
                this->Turn = this->Player;
            }
        }
};
#endif*/


// Below is Fixed One By ChatGPT but i dont like :P
/*
#ifndef TICTACTOE_H
#define TICTACTOE_H
class TicTacToe
{
    public:
        char Player;
        char AI;
        char Turn;
        char PrevPlayed;
        char Diff;
        char Board[3][3];
        TicTacToe()
        {
            memcpy(this->Board, (char[3][3]){{'1', '2', '3'}, {'4', '5', '6'}, {'7', '8', '9'}}, sizeof(this->Board));
            std::srand(time(0));
        }

        void ChooseGameModeAndPlay()
        {
            std::cout<<"Choose GameMode\n1: Play Alone\n2: Play With AI\ninput Here : ";
            int n;
            again:
            std::cin>>n;
            switch (n)
            {
                case 1:
                    this->StartAloneGame();
                    break;
                case 2:
                    this->StartAIGame();
                    break;
                default:
                    std::cout<<"Invalid GameMode, Choose Again"<<std::endl;
                    goto again;
                    break;
            }
        }

        void StartAIGame()
        {
            while (true)
            {
                this->PrintBoard();
                if (this->IsGameOver())
                {
                    std::cout<<"Game Over Winner : "<<this->PrevPlayed<<std::endl;
                    break;
                }
                if (this->IsTie())
                {
                    std::cout<<"Game Tie!"<<std::endl;
                    break;
                }
                this->AIFill(); // Correct method call for AI move
            }
        }
        
        void StartAloneGame()
        {
            while (true)
            {
                this->PrintBoard();
                if (this->IsGameOver())
                {
                    std::cout<<"Game Over Winner : "<<this->PrevPlayed<<std::endl;
                    break;
                }
                if (this->IsTie())
                {
                    std::cout<<"Game Tie!"<<std::endl;
                    break;
                }
                this->PlayerFillTurn(); // Correct method for player move
            }
        }

    private:
        void PrintBoard()
        {
            for (int i = 0; i < 13; i++)
            {
                std::cout << '-';
            }
            std::cout << std::endl;
            for (int i = 0; i < 3; i++)
            {
                std::cout << "| " << this->Board[i][0] << " | " << this->Board[i][1] << " | " << this->Board[i][2] << " |" << std::endl;
            }
            for (int i = 0; i < 13; i++)
            {
                std::cout << '-';
            }
            std::cout << std::endl;
        }

        void ChooseTeam()
        {
            char n;
            again:
            std::cout << "Choose Your Team (O or X): ";
            std::cin >> n;
            n = std::toupper(n);
            if (n != 'O' && n != 'X') 
            {
                std::cout << "Invalid Team, Try Again" << std::endl;
                goto again;
            }

            this->Player = n;
            this->AI = (n == 'X') ? 'O' : 'X';
        }

        void ChooseDiff()
        {
            char n;
            again:
            std::cout << "Choose Your AI Difficulty (e for easy, m for medium, h for hard): ";
            std::cin >> n;
            n = std::tolower(n);
            if (n != 'e' && n != 'm' && n != 'h')
            {
                std::cout << "Invalid Difficulty" << std::endl;
                goto again;
            }
            this->Diff = n;
        }

        bool IsAbleToFill(unsigned int row, unsigned int col)
        {
            return this->Board[row][col] >= '1' && this->Board[row][col] <= '9';
        }

        bool IsGameOver()
        {
            // Check rows, columns, and diagonals for a winner
            for (int i = 0; i < 3; i++)
            {
                if (this->Board[i][0] == this->Board[i][1] && this->Board[i][1] == this->Board[i][2] && this->Board[i][0] != ' ')
                    return true;
                if (this->Board[0][i] == this->Board[1][i] && this->Board[1][i] == this->Board[2][i] && this->Board[0][i] != ' ')
                    return true;
            }
            if (this->Board[0][0] == this->Board[1][1] && this->Board[1][1] == this->Board[2][2] && this->Board[0][0] != ' ')
                return true;
            if (this->Board[0][2] == this->Board[1][1] && this->Board[1][1] == this->Board[2][0] && this->Board[0][2] != ' ')
                return true;

            return false;
        }

        bool IsTie()
        {
            for (int i = 0; i < 3; i++)
            {
                for (int j = 0; j < 3; j++)
                {
                    if (this->IsAbleToFill(i, j))
                        return false;
                }
            }
            return true;
        }

        void PlayerFill(unsigned int row, unsigned int col)
        {
            // safety
            if (this->IsAbleToFill(row, col))
            {
                this->Board[row][col] = this->Player;
                this->PrevPlayed = this->Player;
            }
        }

        void AIFill()
        {
            switch (this->Diff)
            {
                case 'e':
                    this->AIEasyFill();
                    break;
                case 'm':
                case 'h':
                    this->AIMediumOrHardFill();
                    break;
                default:
                    break;
            }
            this->PrevPlayed = this->AI;
        }

        void AIEasyFill()
        {
            std::vector<std::pair<int, int>> availableSpots = this->GetAvailableSpots();
            if (!availableSpots.empty())
            {
                std::pair<int, int> spot = availableSpots[std::rand() % availableSpots.size()];
                this->Board[spot.first][spot.second] = this->AI;
            }
        }

        void AIMediumOrHardFill()
        {
            // Implement more advanced AI strategies like minimax for medium and hard levels
            std::pair<int, int> bestMove = this->FindBestMove();
            this->Board[bestMove.first][bestMove.second] = this->AI;
        }

        std::vector<std::pair<int, int>> GetAvailableSpots()
        {
            std::vector<std::pair<int, int>> availableSpots;
            for (int i = 0; i < 3; i++)
            {
                for (int j = 0; j < 3; j++)
                {
                    if (IsAbleToFill(i, j))
                    {
                        availableSpots.push_back(std::make_pair(i, j));
                    }
                }
            }
            return availableSpots;
        }

        void PlayerFillTurn()
        {
            unsigned int row, col;
            std::cout << "Enter row and column to place your move (1-3 for each): ";
            std::cin >> row >> col;
            if (row >= 1 && row <= 3 && col >= 1 && col <= 3)
            {
                this->PlayerFill(row - 1, col - 1);
            }
            else
            {
                std::cout << "Invalid move. Try again." << std::endl;
                PlayerFillTurn();
            }
        }

        std::pair<int, int> FindBestMove()
        {
            std::vector<std::pair<int, int>> availableSpots = this->GetAvailableSpots();
            return availableSpots[std::rand() % availableSpots.size()];
        }
};
#endif
*/

// Below is Fixed One
// This is so Painful
#ifndef TICTACTOE_H
#define TICTACTOE_H

class TicTacToe
{
public:
    char Player;
    char AI;
    char Turn;
    char PrevPlayed;
    char Diff;
    char Board[3][3];

    TicTacToe()
    {
        // Initialize the board with numbers
        memcpy(this->Board, (char[3][3]){{'1', '2', '3'}, {'4', '5', '6'}, {'7', '8', '9'}}, sizeof(this->Board));
        std::srand(time(0));
    }

    void ChooseGameModeAndPlay()
    {
        std::cout << "Choose GameMode\n1: Play Alone\n2: Play With AI\nInput Here: ";
        int n;
        again:
        std::cin >> n;
        switch (n)
        {
        case 1:
            this->StartAloneGame();
            break;
        case 2:
            this->StartAIGame();
            break;
        default:
            std::cout << "Invalid GameMode. Choose Again" << std::endl;
            goto again;
            break;
        }
    }

    void StartAIGame()
    {
        this->ChooseTeam();
        this->ChooseDiff();
        this->StartTurn();
        while (true)
        {
            this->PrintBoard();
            if (this->IsGameOver())
            {
                std::cout << "Game Over. Winner: " << this->PrevPlayed << std::endl;
                break;
            }
            if (this->IsTie())
            {
                std::cout << "Game Tie!" << std::endl;
                break;
            }
            this->AutoPlayRoundForAI();
        }
    }

    void StartAloneGame()
    {
        this->ChooseTeam();
        while (true)
        {
            this->PrintBoard();
            if (this->IsGameOver())
            {
                std::cout << "Game Over. Winner: " << this->PrevPlayed << std::endl;
                break;
            }
            if (this->IsTie())
            {
                std::cout << "Game Tie!" << std::endl;
                break;
            }
            this->AutoPlayRoundForPlayer();
        }
    }

private:
    void PrintBoard()
    {
        for (int i = 0; i < 13; i++)
        {
            std::cout << '-';
        }
        std::cout << std::endl;
        for (int i = 0; i < 3; i++)
        {
            std::cout << "| " << this->Board[i][0] << " | " << this->Board[i][1] << " | " << this->Board[i][2] << " |" << std::endl;
        }
        for (int i = 0; i < 13; i++)
        {
            std::cout << '-';
        }
        std::cout << std::endl;
    }

    void ChooseTeam()
    {
        char n;
        again:
        std::cout << "Choose Your Team (O or X): ";
        std::cin >> n;
        std::cout << std::endl;
        n = std::toupper(n);
        if (n != 'O' && n != 'X') 
        {
            std::cout << "Invalid Team. Try Again" << std::endl;
            goto again;
        }

        this->Player = n;
        this->AI = (n == 'X') ? 'O' : 'X';
    }

    void StartTurn()
    {
        unsigned int n = std::rand() % 2;
        this->Turn = (n == 0) ? this->Player : this->AI;
    }

    void ChooseDiff()
    {
        char n;
        again:
        std::cout << "Choose Your AI Difficulty (e for easy, m for medium, h for hard): ";
        std::cin >> n;
        std::cout << std::endl;
        n = std::tolower(n);
        if (n != 'e' && n != 'm' && n != 'h')
        {
            std::cout << "Invalid Difficulty. Try Again" << std::endl;
            goto again;
        }
        this->Diff = n;
    }

    bool IsAbleToFill(unsigned int row, unsigned int col)
    {
        if (this->Board[row][col] >= '1' && this->Board[row][col] <= '9')
        {
            return true;
        }
        return false;
    }

    bool IsGameOver()
    {
        for (int i = 0; i < 3; i++)
        {
            if (this->Board[i][0] == this->Board[i][1] && this->Board[i][1] == this->Board[i][2])
            {
                return true;
            }
            else if (this->Board[0][i] == this->Board[1][i] && this->Board[1][i] == this->Board[2][i])
            {
                return true;
            }
        }
        if (this->Board[0][0] == this->Board[1][1] && this->Board[1][1] == this->Board[2][2])
        {
            return true;
        }
        else if (this->Board[0][2] == this->Board[1][1] && this->Board[1][1] == this->Board[2][0])
        {
            return true;
        }

        return false;
    }

    bool IsTie()
    {
        for (int i = 0; i < 3; i++)
        {
            for (int j = 0; j < 3; j++)
            {
                if (this->IsAbleToFill(i, j))
                {
                    return false;
                }
            }
        }
        return true;
    }

    void PlayerFill(unsigned int row, unsigned int col)
    {
        // Safety check to prevent invalid move
        if (this->IsAbleToFill(row, col))
        {
            this->Board[row][col] = this->Player;
        }
    }

    void AIEasyFill()
    {
        std::vector<std::pair<int, int>> available = this->GetAvaForEasyAI();
        std::pair<int, int> spot = available[std::rand() % available.size()];
        if (spot.first != -1 && spot.second != -1)
        {
            this->Board[spot.first][spot.second] = this->AI;
        }
    }

    std::vector<std::pair<int, int>> GetAvaForEasyAI()
    {
        std::vector<std::pair<int, int>> available;
        for (int i = 0; i < 3; i++)
        {
            for (int j = 0; j < 3; j++)
            {
                if (IsAbleToFill(i, j))
                {
                    available.push_back(std::make_pair(i, j));
                }
            }
        }
        return available;
    }

    void SwitchPlayerTeam()
    {
        this->Player = (this->Player == 'O') ? 'X' : 'O';
    }

    void AutoPlayRoundForAI()
    {
        if (this->Turn == this->Player)
        {
            unsigned int plrCin, row, col;
            again:
            std::cout<<"Current Player : "<<this->Player<<std::endl;
            std::cout<<"Please Choose Board to Fill in The Blank from 1-9 : "<<std::endl;
            std::cin>>plrCin;
            if (plrCin < 1 || plrCin > 9)
            {
                std::cout<<"invaild input TryAgain"<<std::endl;
                goto again;
            }
            row = (plrCin - 1) / 3;
            col = (plrCin - 1) % 3;
            if (!this->IsAbleToFill(row, col))
            {
                std::cout<<"Board Already Filled Choose Another Spot"<<std::endl;
                goto again;
            }
            this->PlayerFill(row, col);\
            this->PrevPlayed = this->Player;
            this->Turn = this->AI;
        } else {
            std::cout<<"AI Turn!..AI is Thinking and Choosing"<<std::endl;
            this->AIFill();
            this->PrevPlayed = this->AI;
            this->Turn = this->Player;
        }
    }

    void AutoPlayRoundForPlayer()
    {
        unsigned int plrCin, row, col;
        again:
        std::cout<<"Current Player "<<this->Player<<std::endl;
        std::cout << "Enter your move between 1 and 9: ";
        std::cin>>plrCin;
        if (plrCin < 1 || plrCin > 9)
        {
            std::cout<<"invaild input try again"<<std::endl;
            goto again;
        }
        row = (plrCin - 1) / 3;
        col = (plrCin - 1) % 3;
        if (!this->IsAbleToFill(row, col))
        {
            std::cout<<"Board Already Filled Choose Another Spot"<<std::endl;
            goto again;
        }
        this->PlayerFill(row, col);\
        this->PrevPlayed = this->Player;
        this->SwitchPlayerTeam();
    }

    void AIFill()
    {
        switch (this->Diff)
        {
            case 'e': // Easy
                this->AIEasyFill();
                break;
            case 'm': // Medium
                {
                    std::pair<int, int> pii_AI = this->FindAvaSpot(this->AI);
                    if (this->IsAbleToFill(pii_AI.first, pii_AI.second))
                    {
                        this->Board[pii_AI.first][pii_AI.second] = this->AI;
                        return;
                    }
                    std::pair<int, int> pii_Player = this->FindAvaSpot(this->Player);
                    if (this->IsAbleToFill(pii_Player.first, pii_Player.second))
                    {
                        this->Board[pii_Player.first][pii_Player.second] = this->AI;
                        return;
                    }
                }
                break;
            case 'h': // Hard (e.g., using Minimax algorithm)
                {
                    long bestScore = -1000000;
                    std::pair<int, int> bestMove = std::make_pair(-1, -1); // maybe put -1, -1
                    for (int i = 0; i < 3; i++)
                    {
                        for (int j = 0; j < 3; j++)
                        {
                            if (this->IsAbleToFill(i, j))
                            {
                                this->Board[i][j] = this->AI;
                                long score = this->MiniMax(true, -1000000, 1000000, 0);
                                this->Board[i][j] = (char)(i * 3 + j + '1');
                                if (score > bestScore)
                                {
                                    bestScore = score;
                                    bestMove = std::make_pair(i, j);
                                }
                            }
                        }
                    }
                    if (bestMove.first != -1 && bestMove.second != -1)
                    {
                        this->Board[bestMove.first][bestMove.second] = this->AI;
                    }
                }
                break;
            default:
                std::cout << "Invalid difficulty level!" << std::endl;
                break;
        }
    }

    long MiniMax(bool isMaximizingPlayer, long alpha, long beta, unsigned long depth)
    {
        char winner = this->MiniMaxCheckWinner();
        if (winner == this->AI) return 10 - depth;
        if (winner == this->Player) return depth - 10;
        if (this->IsTie()) return 0;

        if (isMaximizingPlayer)
        {
            long maxEval = -1000000;
            for (int i = 0; i < 3; i++)
            {
                for (int j = 0; j < 3; j++)
                {
                    if (this->IsAbleToFill(i, j))
                    {
                        this->Board[i][j] = this->AI;
                        long eval = this->MiniMax(false, alpha, beta, depth + 1);
                        this->Board[i][j] = (char)(i * 3 + j + '1');
                        maxEval = std::max(maxEval, eval);
                        alpha = std::max(alpha, eval);
                        if (beta <= alpha) break;
                    }
                }
            }
            return maxEval;
        }
        else
        {
            long minEval = 1000000;
            for (int i = 0; i < 3; i++)
            {
                for (int j = 0; j < 3; j++)
                {
                    if (this->IsAbleToFill(i, j))
                    {
                        this->Board[i][j] = this->Player;
                        long eval = this->MiniMax(true, alpha, beta, depth + 1);
                        this->Board[i][j] = (char)(i * 3 + j + '1');
                        minEval = std::min(minEval, eval);
                        beta = std::min(beta, eval);
                        if (beta <= alpha) break;
                    }
                }
            }
            return minEval;
        }
    }

    char MiniMaxCheckWinner()
    {
        // Check rows
        for (int i = 0; i < 3; i++)
        {
            if (this->Board[i][0] == this->Board[i][1] && this->Board[i][1] == this->Board[i][2])
            {
                return this->Board[i][0];
            }
        }

        // Check columns
        for (int j = 0; j < 3; j++)
        {
            if (this->Board[0][j] == this->Board[1][j] && this->Board[1][j] == this->Board[2][j])
            {
                return this->Board[0][j];
            }
        }

        // Check diagonals
        if (this->Board[0][0] == this->Board[1][1] && this->Board[1][1] == this->Board[2][2])
        {
            return this->Board[0][0];
        }
        if (this->Board[0][2] == this->Board[1][1] && this->Board[1][1] == this->Board[2][0])
        {
            return this->Board[0][2];
        }

        return ' ';  // No winner
    }

    std::pair<int, int> FindAvaSpot(char symbol)
    {
        for (int i = 0;i<3;i++)
        {
            // Straight Line
            if (this->Board[i][0] == symbol && this->Board[i][1] == symbol && this->IsAbleToFill(i, 2))
            {
                return std::make_pair(i, 2);
            } else if (this->Board[i][2] == symbol && this->Board[i][1] == symbol && this->IsAbleToFill(i, 0))
            {
                return std::make_pair(i, 0);
            } else if (this->Board[i][2] == symbol && this->Board[i][0] == symbol && this->Board[i][1])
            {
                return std::make_pair(i, 1);
            }
                // Vertical Line
            else if (this->Board[0][i] == symbol && this->Board[1][i] == symbol && this->IsAbleToFill(2, i))
            {
                return std::make_pair(2, i);
            } else if (this->Board[2][i] == symbol && this->Board[1][i] == symbol == symbol && this->IsAbleToFill(0, i))
            {
                 return std::make_pair(0, i);
            } else if (this->Board[2][i] == symbol && this->Board[0][i] == symbol && this->Board[1][i])
            {
                return std::make_pair(1, i);
            }
        }
            // Side 1
            if (this->Board[0][0] == symbol && this->Board[1][1] == symbol && this->IsAbleToFill(2, 2))
            {
                return std::make_pair(2, 2);
            } else if (this->Board[2][2] == symbol && this->Board[1][1] == symbol && this->IsAbleToFill(0, 0))
            {
                return std::make_pair(0, 0);
            } else if (this->Board[2][2] == symbol && this->Board[0][0] == symbol && this->IsAbleToFill(1, 1))
            {
                return std::make_pair(1, 1);
            } 
            // side 2
            else if (this->Board[0][2] == symbol && this->Board[1][1] == symbol && this->IsAbleToFill(2, 0))
            {
                return std::make_pair(2, 0);
            } else if (this->Board[2][0] == symbol && this->Board[1][1] == symbol && this->IsAbleToFill(0, 2))
            {
                return std::make_pair(0, 2);
            } else if (this->Board[0][2] == symbol && this->Board[2][0] == symbol && this->IsAbleToFill(1, 1))
            {
                return std::make_pair(1, 1);
            }
            return std::make_pair(0, 0);
        }
};

#endif


int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    TicTacToe T1;
    T1.ChooseGameModeAndPlay();

    return 0;
}
