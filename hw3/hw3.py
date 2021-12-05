def MinimaxGameTreeMin(tree, visited):
    for leaf in tree[2]:
        if(leaf[0] == tree[0]):
            return int(leaf[1])
    children = []
    for edge in tree[1]:
        if(edge[0] == tree[0]):
            visited.append(edge[1])
            value = MinimaxGameTreeMax([edge[1], tree[1], tree[2]], visited)
            if(type(value) != int):
                children.append(value[0])
            else:
                children.append(value)
    return min(children), children.index(min(children))

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

def AlphaBetaGameTreeMin(tree, visited):
    return

def AlphaBetaGameTreeMax(tree, visited):
    return

def SolveGame(method_name, problem_file_name, player_type):
    with open(problem_file_name) as file:
            lines = file.read().splitlines()        
    if(problem_file_name[0] == 'g'):        #gametree case
        tree = []                       #tree[0] is root, tree[1] is list of edges in tree, tree[2] is list of leaf nodes
        tree.append(lines[0]) 
        tree.append([])
        tree.append([])
        visited = []
        visited.append(lines[0])
        for item in lines[1:]:
            if(len(item.split()) == 1):
                index = item.split()[0].index(':')
                tree[2].append((item.split()[0][:index],item.split()[0][index+1:]))
            else:
                tree[1].append(item.split())
        if(method_name == 'Minimax' and player_type == 'MAX'):
            result = MinimaxGameTreeMax(tree, visited)
        elif(method_name == 'Minimax' and player_type == 'MIN'):
            result = MinimaxGameTreeMin(tree, visited)
        elif(method_name == 'AlphaBeta' and player_type == 'MAX'):
            result = AlphaBetaGameTreeMax(tree, visited)
        elif(method_name == 'AlphaBeta' and player_type == 'MIN'):
            result = AlphaBetaGameTreeMin(tree, visited)
            
        return result[0], tree[1][result[1]][2], visited
    
    elif(problem_file_name[0] == 't'):          #tictactoe case
        board = []                      #board is list of lists each contains a row
        for item in lines:
            line = []
            for character in item[:-1]:
                line.append(character)
            board.append(line)
        return board
    
print(SolveGame('Minimax', "gametree1.txt", 'MIN'))