local tictactoe = {}
tictactoe.__index = tictactoe

function tictactoe.new()
    local self = setmetatable({}, tictactoe)
    self.Board = {
        {1, 2, 3},
        {4, 5, 6},
        {7, 8, 9}
    }
    self.Player = nil
    self.AI = nil
    self.Diff = nil
    self.PrevPlayed = nil
    self.Turn = nil
    return self
end

-- Lua Index of Table Start With 1
-- So I use 1 as First Index
function tictactoe:DrawBoard()
    print(string.rep("-", 14))
    for i = 1, 3 do
        print("|"..tostring(self.Board[i][1]).." | "..tostring(self.Board[i][2]).." | "..tostring(self.Board[i][3]).. " |")
    end
    print(string.rep("-", 14))
end
function tictactoe:ChooseTeam()
    ::again::
    io.write("Choose You Team (O or X ) : ")
    local n = string.upper(io.read())
    if n == "O" then
        self.Player = n
        self.AI = "X"
    elseif n == "X" then
        self.Player = n
        self.AI = "O"
    else
        print("Invaild Team")
        goto again
    end
end

function tictactoe:SelectDiff()
    ::again::
    io.write("Choose You AI Diff\ne: Easy\nm: Meduim\nh: Hard\nInput Here : ")
    local n = string.lower(io.read())
    if n == "e" then
        self.Diff = n
    elseif n == "m" then
        self.Diff = n
    elseif n == "h" then
        self.Diff = n
    else
        print("Invaild Input")
        goto again
    end
end

function tictactoe:StartTurn()
    local n = math.random(1, 2)
    if n == 1 then
        self.Turn = self.Player
    else
        self.Turn = self.AI
    end
end

function tictactoe:IsAbleToFill(row, col)
    return type(self.Board[row][col]) == "number"
end

function tictactoe:IsTie()
    for i = 1, 3 do
        for j = 1, 3 do
            if self:IsAbleToFill(i, j) then
                return false
            end
        end
    end
    return true
end

function tictactoe:IsGameOver()
    for i = 1, 3 do
        if self.Board[i][1] == self.Board[i][2] and self.Board[i][2] == self.Board[i][3] then
            return true
        elseif self.Board[1][i] == self.Board[2][i] and self.Board[2][i] == self.Board[3][i] then
            return true
        end
    end
    if self.Board[1][1] == self.Board[2][2] and self.Board[2][2] == self.Board[3][3] then
        return true
    elseif self.Board[1][3] == self.Board[2][2] and self.Board[2][2] == self.Board[3][1] then
        return true
    end
end

function tictactoe:PlayerFill(row, col)
    if self:IsAbleToFill(row, col) then
        self.Board[row][col] = self.Player
    else
        return
    end
end

-- Might Confunse You on This One
-- Function For AI (MiniMax Algorithm/AI Algorithm)
function tictactoe:EasyAIFill()
    local ava = {}
    for i = 1, 3 do
        for j = 1, 3 do
            if self:IsAbleToFill(i, j) then
                table.insert(ava, {i, j})
            end
        end
    end
    if ava then
        local avaSpot = ava[math.random(1, #ava)]
        self.Board[avaSpot[1]][avaSpot[2]] = self.AI
    end
end

function tictactoe:FindAvaSpot(symbol)
    for i= 1,  3 do
        if self.Board[i][1] == symbol and self.Board[i][2] == symbol and self:IsAbleToFill(i, 3) then
            return {i, 3}
        elseif self.Board[i][3] == symbol and self.Board[i][2] == symbol and self:IsAbleToFill(i, 1) then
            return {i, 1}
        elseif self.Board[1][i] == symbol and self.Board[2][i] == symbol and self:IsAbleToFill(3, i) then
            return {3, i}
        elseif self.Board[3][i] == symbol and self.Board[2][i] == symbol and self:IsAbleToFill(1, i) then
            return {1, i}
        elseif self.Board[3][i] == symbol and self.Board[1][i] == symbol and self:IsAbleToFill(2, i) then
            return {2, i}
        elseif self.Board[i][3] == symbol and self.Board[i][1] == symbol and self:IsAbleToFill(i, 2) then
            return {i, 2}
        end
    end
    -- Ava Spot 2 For AI Meduim
    if self.Board[1][1] == symbol and self.Board[2][2] == symbol and self:IsAbleToFill(3, 3) then return {3, 3} end
    if self.Board[3][3] == symbol and self.Board[2][2] == symbol and self:IsAbleToFill(1, 1) then return {1, 1} end
    if self.Board[1][3] == symbol and self.Board[2][2] == symbol and self:IsAbleToFill(3, 1) then return {3, 1} end
    if self.Board[3][1] == symbol and self.Board[2][2] == symbol and self:IsAbleToFill(1, 3) then return {1, 3} end
    return nil
end
-- Now This One Gonna Be The Main Algorithm for The Minimax AI which is a Hard Mode AI
-- This One For Checking Winner With MiniMax Or Maybe you can use The IsGameOver() Func Which i Made this Optional
-- Well is Just Waste of Line You Can Just Replace This With IsGameOver And Make the IsGameOver Reutrn char instead of Bool
function tictactoe:MiniMaxCheckWinner()
    for i = 1, 3 do
        if self.Board[i][1] == self.Board[i][2] and self.Board[i][2] == self.Board[i][3] then
            return self.Board[i][1]
        elseif self.Board[1][i] == self.Board[2][i] and self.Board[2][i] == self.Board[3][i] then
            return self.Board[1][i]
        end
    end
    if self.Board[1][1] == self.Board[2][2] and self.Board[2][2] == self.Board[3][3] then
        return self.Board[1][1]
    elseif self.Board[1][3] == self.Board[2][2] and self.Board[2][2] == self.Board[3][1] then
        return self.Board[1][3]
    end
    return nil
end
-- Now All We Need is Just This Function For The Hard AI Algorithm
function tictactoe:MiniMax(ismaxing, alpha, beta, depth)
    local winner = self:MiniMaxCheckWinner()
    if winner == self.AI then return 1 - depth end
    if winner == self.Player then return -1 + depth end
    if self:IsTie() then return 0 end
    if ismaxing then
        -- This One For The AI Case
        -- Such That AI Going Check All Possible Way to Win The Player With This Algorithm
        local maxscore = -math.huge
        for i = 1, 3 do
            for j = 1, 3 do
                if self:IsAbleToFill(i, j) then
                    local temp = self.Board[i][j] 
                    self.Board[i][j] = self.AI
                    local score = self:MiniMax(false, alpha, beta, depth + 1)
                    maxscore = math.max(score, maxscore)
                    self.Board[i][j] = temp
                    alpha = math.max(alpha, score)
                    if beta <= alpha then
                        break
                    end

                end
            end
        end
        return maxscore
    else
        -- This One For The Player Case
        -- Such That AI Going To Play The Player To Find That How Will AI Win or Block Player Spot When Player is Filling(Might not Accruate)
        local minscore = math.huge
        for i = 1, 3 do
            for j = 1, 3 do
                if self:IsAbleToFill(i, j) then
                    local temp = self.Board[i][j]
                    self.Board[i][j] = self.Player
                    local score = self:MiniMax(true, alpha, beta, depth + 1)
                    minscore = math.min(score, minscore)
                    self.Board[i][j] = temp
                    beta = math.min(beta, score) 
                    if beta <= alpha then break end

                end
            end
        end
        return minscore
    end
end

function tictactoe:AIFill()
    if self.Diff == "e" then
        self:EasyAIFill()
    elseif self.Diff == "m" then
        local WinSpot = self:FindAvaSpot(self.AI)
        if WinSpot then
            self.Board[WinSpot[1]][WinSpot[2]] = self.AI
            return
        end
        local BlockSpot = self:FindAvaSpot(self.Player) 
        if BlockSpot then
            self.Board[BlockSpot[1]][BlockSpot[2]] = self.AI
            return
        end
        -- This Code Run When There No WinSpot or BlockSpot
        for i = 1, 3 do
            for j = 1, 3 do
                if self:IsAbleToFill(i, j) then
                    self.Board[i][j] = self.AI
                    return
                end
            end
        end
    elseif self.Diff == "h" then
        -- This One Use The Algorithm For Winning So Feel Free To View The Soucre of the Algorithm
        local bestscore = -math.huge
        local bestfill = nil
        for i = 1, 3 do
            for j = 1, 3 do
                if self:IsAbleToFill(i, j) then
                    local temp = self.Board[i][j] 
                    self.Board[i][j] = self.AI
                    local score = self:MiniMax(false, -math.huge, math.huge, 0)
                    if score > bestscore then
                        bestscore = score
                        bestfill = {i, j}
                    end
                    self.Board[i][j] = temp
                end
            end
        end
        if bestfill then
            self.Board[bestfill[1]][bestfill[2]] = self.AI
        end
    end
end

-- Function For Main Game Code
function tictactoe:AutoPlayRound()
    if self.Turn == self.Player then
        -- Player's turn
        local validInput = false
        while not validInput do
            io.write(string.format("Player Turn! Currently Player Is %s\nChoose To Fill From 1-9\ninput Here : ", self.Player))
            local plrCin = tonumber(io.read())
            if plrCin and plrCin >= 1 and plrCin <= 9 then
                local row = math.ceil(plrCin / 3)
                local col = (plrCin - 1) % 3 + 1
                if self:IsAbleToFill(row, col) then
                    self:PlayerFill(row, col)
                    validInput = true
                else
                    print("Board Already Filled. Choose Another.")
                end
            else
                print("Invalid input. Please enter a number between 1 and 9.")
            end
        end
        self.PrevPlayed = self.Player
        self.Turn = self.AI
    else
        -- AI's turn
        print("AI Turn!.. AI is Thinking.. and Choosing")
        self:AIFill()
        self.PrevPlayed = self.AI
        self.Turn = self.Player
    end
end

-- Fit In All Function Together into Simple Code
function tictactoe:StartAIGame()
    self:ChooseTeam()
    self:SelectDiff()
    self:StartTurn()
    while true do
        --os.execute("clear")
        self:DrawBoard()
        if self:IsGameOver() then print("Game Over Winner : " .. self.PrevPlayed) break end
        if self:IsTie() then print("Game Tie!") break end
        self:AutoPlayRound()
    end
end

-- Test Result
local ttt1 = tictactoe.new()
ttt1:StartAIGame()
