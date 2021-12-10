def MinimaxGameTreeMin(tree, visited):
    for leaf in tree[2]:
        if(leaf[0] == tree[0]):
            return int(leaf[1])             #returns leaf value
    children = []
    for edge in tree[1]:
        if(edge[0] == tree[0]):
            visited.append(edge[1])
            value = MinimaxGameTreeMax([edge[1], tree[1], tree[2]], visited)
            if(type(value) != int):
                children.append(value[0])
            else:
                children.append(value)
    return min(children), children.index(min(children))         #returns min value and index of value in given children order

def MinimaxGameTreeMax(tree, visited):
    for leaf in tree[2]:
        if(leaf[0] == tree[0]):
            return int(leaf[1])
    children = []
    for edge in tree[1]:
        if(edge[0] == tree[0]):
            visited.append(edge[1])
            value = MinimaxGameTreeMin([edge[1], tree[1], tree[2]], visited)
            if(type(value) != int):
                children.append(value[0])
            else:
                children.append(value)
    return max(children), children.index(max(children))

def AlphaBetaGameTreeMin(tree, visited, parent_value):          #parent_value is parent's temporary maximum value
    for leaf in tree[2]:
        if(leaf[0] == tree[0]):
            return int(leaf[1])
    temp_value = parent_value
    children = []
    index = -1
    for edge in tree[1]:
        if(edge[0] == tree[0]):
            index+=1
            visited.append(edge[1])
            value = AlphaBetaGameTreeMax([edge[1], tree[1], tree[2]], visited, temp_value)
            if(parent_value != None and type(value) != int and value[0] < parent_value):
                return value[0], index
            elif(parent_value != None and type(value) == int and value < parent_value):
                return value, index
            if(type(value) != int):
                children.append(value[0])
            else:
                children.append(value)
            temp_value = min(children)
    return min(children), children.index(min(children))

def AlphaBetaGameTreeMax(tree, visited, parent_value):
    for leaf in tree[2]:
        if(leaf[0] == tree[0]):
            return int(leaf[1])
    temp_value = parent_value
    children = []
    index = -1
    for edge in tree[1]:
        if(edge[0] == tree[0]):
            index+=1
            visited.append(edge[1])
            value = AlphaBetaGameTreeMin([edge[1], tree[1], tree[2]], visited, temp_value)
            if(parent_value != None and type(value) != int and value[0] > parent_value):
                return value[0], index
            elif(parent_value != None and type(value) == int and value > parent_value):
                return value, index
            if(type(value) != int):
                children.append(value[0])
            else:
                children.append(value)
            temp_value = max(children)
    return max(children), children.index(max(children))

def possibleMoves(board):
    moves = []
    for i in range(3):
        for j in range(3):
            if(board[i][j] == ' '):
                moves.append((i,j))
    return moves

def isGameOver(depth, board):
    for i in range(3):
        if(board[i][0]=='X' and board[i][1]=='X' and board[i][2]=='X'):
            return 5-0.01*(depth-1)
        if(board[i][0]=='O' and board[i][1]=='O' and board[i][2]=='O'):
            return -5
    for j in range(3):
        if(board[0][j]=='X' and board[1][j]=='X' and board[2][j]=='X'):
            return 5-0.01*(depth-1)
        if(board[0][j]=='O' and board[1][j]=='O' and board[2][j]=='O'):
            return -5
    if(board[0][0]=='X' and board[1][1]=='X' and board[2][2]=='X'):
        return 5-0.01*(depth-1)
    if(board[0][0]=='O' and board[1][1]=='O' and board[2][2]=='O'):
        return -5
    if(board[2][0]=='X' and board[1][1]=='X' and board[0][2]=='X'):
        return 5-0.01*(depth-1)
    if(board[2][0]=='O' and board[1][1]=='O' and board[0][2]=='O'):
        return -5
    if(any(' ' in s for s in board)):
        return None
    return 0

def MinimaxTTTMin(depth, board, visited):
    moves = possibleMoves(board)
    children = []
    for i,j in moves:
        copyboard = [row[:] for row in board]
        copyboard[i][j]='O'
        visited.append(copyboard)
        score = isGameOver(depth, copyboard)
        if(score != None):
            children.append(score)
            continue
        value = MinimaxTTTMax(depth+1, copyboard, visited)[0]
        children.append(value)
    return min(children), children.index(min(children))

def MinimaxTTTMax(depth, board, visited):
    moves = possibleMoves(board)
    children = []
    for i,j in moves:
        copyboard = [row[:] for row in board]
        copyboard[i][j]='X'
        visited.append(copyboard)
        score = isGameOver(depth, copyboard)
        if(score != None):
            children.append(score)
            continue
        value = MinimaxTTTMin(depth+1, copyboard, visited)[0]
        children.append(value)
    return max(children), children.index(max(children))

def AlphaBetaTTTMin(depth, board, visited, parent_value):
    moves = possibleMoves(board)
    children = []
    temp_value = parent_value
    for i,j in moves:
        copyboard = [row[:] for row in board]
        copyboard[i][j]='O'
        visited.append(copyboard)
        score = isGameOver(depth, copyboard)
        if(score != None):
            if(parent_value != None and score <= parent_value):
                return score, len(children)
            children.append(score)
            temp_value = min(children)
            continue
        value = AlphaBetaTTTMax(depth+1, copyboard, visited, temp_value)[0]
        if(parent_value != None and value < parent_value):
            return value, len(children)
        children.append(value)
        temp_value = min(children)
    return min(children), children.index(min(children))

def AlphaBetaTTTMax(depth, board, visited, parent_value):
    moves = possibleMoves(board)
    children = []
    temp_value = parent_value
    for i,j in moves:
        copyboard = [row[:] for row in board]
        copyboard[i][j]='X'
        visited.append(copyboard)
        score = isGameOver(depth, copyboard)
        if(score != None):
            if(parent_value != None and score >= parent_value):
                return score, len(children)
            children.append(score)
            temp_value = max(children)
            continue
        value = AlphaBetaTTTMin(depth+1, copyboard, visited, temp_value)[0]
        if(parent_value != None and value > parent_value):
            return value, len(children)
        children.append(value)
        temp_value = max(children)
    return max(children), children.index(max(children))

def organizeList(lst):
    resultList = []
    for item in lst:
        string = ''
        for i in range(3):
            for j in range(3):
                string = string+(item[i][j])
        resultList.append(string)
    return resultList

def SolveGame(method_name, problem_file_name, player_type):
    with open(problem_file_name) as file:
            lines = file.read().splitlines()        
    if(problem_file_name[0] == 'g'):        #gametree case
        tree = [lines[0],[],[]]                       #tree[0] is root, tree[1] is list of edges in tree, tree[2] is list of leaf nodes
        visited = [lines[0]]                #list of expanded nodes added root first
        for item in lines[1:]:
            if(len(item.split()) == 1):
                index = item.split()[0].index(':')
                tree[2].append((item.split()[0][:index],item.split()[0][index+1:]))         #leaf list form -> [(leaf1, value1), ...]
            else:
                tree[1].append(item.split())                                    #edge list form -> [(parent, child, edge), ...]
        if(method_name == 'Minimax' and player_type == 'MAX'):
            result = MinimaxGameTreeMax(tree, visited)
        elif(method_name == 'Minimax' and player_type == 'MIN'):
            result = MinimaxGameTreeMin(tree, visited)
        elif(method_name == 'AlphaBeta' and player_type == 'MAX'):
            result = AlphaBetaGameTreeMax(tree, visited, None)              #root does not have a parent value
        elif(method_name == 'AlphaBeta' and player_type == 'MIN'):
            result = AlphaBetaGameTreeMin(tree, visited, None)
            
        return result[0], tree[1][result[1]][2], visited                #result contains the minimax value and index of the path in given order w.r.t. root
    
    elif(problem_file_name[0] == 't'):          #tictactoe case
        board = []                      #board is list of lists each contains a row
        for item in lines:
            line = []
            for character in item:
                line.append(character)
            board.append(line)
        visited = []
        if(method_name == 'Minimax'):
            result= MinimaxTTTMax(1, board, visited)
            score = result[0]
            position = (possibleMoves(board)[result[1]][1],possibleMoves(board)[result[1]][0])
            return score, position, organizeList(visited)
        elif(method_name == 'AlphaBeta'):
            result =  AlphaBetaTTTMax(1, board, visited, None)
            score = result [0]
            position = (possibleMoves(board)[result[1]][1],possibleMoves(board)[result[1]][0])
            return score, position, organizeList(visited)
        return board
    
#print(SolveGame('AlphaBeta', "tictactoe2.txt", 'MAX'))
