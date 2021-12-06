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

def SolveGame(method_name, problem_file_name, player_type):
    with open(problem_file_name) as file:
            lines = file.read().splitlines()        
    if(problem_file_name[0] == 'g'):        #gametree case
        tree = []                       #tree[0] is root, tree[1] is list of edges in tree, tree[2] is list of leaf nodes
        tree.append(lines[0]) 
        tree.append([])
        tree.append([])
        visited = []                #list of expanded nodes
        visited.append(lines[0])    #add root to expanded
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
            for character in item[:-1]:
                line.append(character)
            board.append(line)
        return board
    
#print(SolveGame('AlphaBeta', "gametree1.txt", 'MAX'))
