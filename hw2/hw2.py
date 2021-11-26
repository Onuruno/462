def copy2(a):
    b=[]
    for i in range(len(a)):
        b.append(a[i].copy())
    return b

def copy3(a):
    b=[]
    for i in range(len(a)):
        c=copy2(a[i])
        b.append(c.copy())
    return b

def isPuzzleCompleted(puzzleArray):     #Checks whether a puzzle is completed
    if (puzzleArray == [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '0']]):
        return True
    else:
        return False
    
def isPuzzleMoveLegal(puzzleArray, move):   #Checks whether a move is legal in a puzzle
    if(move == 'L'):
        for item in puzzleArray:
            if(item[0] == '0'):
                return False
        return True
    elif(move == 'U'):
        for item in puzzleArray[0]:
            if(item == '0'):
                return False
        return True
    elif(move == 'R'):
        for item in puzzleArray:
            if(item[2] == '0'):
                return False
        return True
    elif(move == 'D'):
        for item in puzzleArray[2]:
            if(item == '0'):
                return False
        return True
    
def isMazeMoveLegal(position, move, mazeArray):     #Checks whether a move is legal in a maze
    if(move == 'L'):
        if(position[0] > 0 and mazeArray[position[1]][position[0]-1] == 0):
            return True
    elif(move == 'U'):
        if(position[1] > 0 and mazeArray[position[1]-1][position[0]] == 0):
            return True
    elif(move == 'R'):
        if(position[0] < len(mazeArray[0])-1 and mazeArray[position[1]][position[0]+1] == 0):
            return True
    elif(move == 'D'):
        if(position[1] < len(mazeArray)-1 and mazeArray[position[1]+1][position[0]] == 0):
            return True
    return False

def makePuzzleMove(puzzleArray, move):      #changes the given puzzle w.r.t. a move
    for i in range(3):
        for j in range(3):
            if(puzzleArray[i][j] == '0'):
                row=i
                column=j            
    if(move == 'L'):
        puzzleArray[row][column] = puzzleArray[row][column-1]
        puzzleArray[row][column-1] = '0'
        return puzzleArray
    elif(move == 'U'):
        puzzleArray[row][column] = puzzleArray[row-1][column]
        puzzleArray[row-1][column] = '0'
        return puzzleArray
    elif(move == 'R'):
        puzzleArray[row][column] = puzzleArray[row][column+1]
        puzzleArray[row][column+1] = '0'
        return puzzleArray
    elif(move == 'D'):
        puzzleArray[row][column] = puzzleArray[row+1][column]
        puzzleArray[row+1][column] = '0'
        return puzzleArray

def fixPath(path):      #turns puzzle positions into valid form   [['6', '1', '2'], ['4', '0', '3'], ['7', '8', '5']] -> '6124 3785'
    result=[]
    for item in path:
        new_str=''
        for i in item:
            for j in i:
                new_str+=j
        a= list(new_str)
        a[a.index('0')]=' '
        new_str=''.join(a)
        result.append(new_str)
    return result

def heuristicPuzzle(puzzleArray):       #Computes a heuristic value for a puzzle with Manhattan distance
    value=0
    for i in range(3):
        for j in range(3):
            if(puzzleArray[i][j] == '1'):
                value+=(i+j)
            elif(puzzleArray[i][j] == '2'):
                value+=(i+abs(j-1))
            elif(puzzleArray[i][j] == '3'):
                value+=(i+abs(j-2))
            elif(puzzleArray[i][j] == '4'):
                value+=(abs(i-1)+j)
            elif(puzzleArray[i][j] == '5'):
                value+=(abs(i-1)+abs(j-1))
            elif(puzzleArray[i][j] == '6'):
                value+=(abs(i-1)+abs(j-2))
            elif(puzzleArray[i][j] == '7'):
                value+=(abs(i-2)+j)
            elif(puzzleArray[i][j] == '8'):
                value+=(abs(i-2)+abs(j-1))
    return value

def heuristicMaze(position, end):       #Computes a heuristic value for a maze with Manhattan distance
    return abs(end[1]-position[1])+abs(end[0]-position[0])

def minCostPuzzle(queue):       #returns index of minimum cost path in the queue
    value=queue[0][2]
    index=0
    for i in range(len(queue)):
        if(queue[i][2]<value):
            value=queue[i][2]
            index=i
    return index

def minCostMaze(queue):     #returns index of minimum cost path in the queue
    value=queue[0][1]
    index=0
    for i in range(len(queue)):
        if(queue[i][1]<value):
            value=queue[i][1]
            index=i
    return index
            
def ucsMaze(start, end, mazeArray):
    queue = []
    queue.append([start])       #a list containing the paths
    visited = []            #a list containing the processed positions in the maze
    while(len(queue)>0):
        path = queue[0]
        selectedPosition = path[-1]
        queue.remove(queue[0])
        if(selectedPosition in visited):
            continue
        visited.append(selectedPosition)
        if(selectedPosition == end):
            return path, visited, len(path)-1, len(path)-1, len(visited)
        else:
            if(isMazeMoveLegal(selectedPosition, 'L', mazeArray)):
                newPath = path.copy()
                newPath.append((selectedPosition[0]-1,selectedPosition[1]))
                queue.append(newPath)
                
            if(isMazeMoveLegal(selectedPosition, 'U', mazeArray)):
                newPath = path.copy()
                newPath.append((selectedPosition[0],selectedPosition[1]-1))
                queue.append(newPath)
                
            if(isMazeMoveLegal(selectedPosition, 'R', mazeArray)):
                newPath = path.copy()
                newPath.append((selectedPosition[0]+1,selectedPosition[1]))
                queue.append(newPath)
                
            if(isMazeMoveLegal(selectedPosition, 'D', mazeArray)):
                newPath = path.copy()
                newPath.append((selectedPosition[0],selectedPosition[1]+1))
                queue.append(newPath)
    return None

def aStarMaze(start, end, mazeArray):
    queue = []          #a list containing the paths and the manhattan discance value of the paths' current positions
    queue.append(([start], heuristicMaze(start, end)))
    visited = []
    while(len(queue)>0):
        index = minCostMaze(queue)
        path = queue[index][0]
        cost = queue[index][1]
        selectedPosition = path[-1]
        queue.remove(queue[index])
        if(selectedPosition in visited):
            continue
        visited.append(selectedPosition)
        if(selectedPosition == end):
            return path, visited, len(path)-1, len(path)-1, len(visited)
        else:
            if(isMazeMoveLegal(selectedPosition, 'L', mazeArray)):
                newPosition = (selectedPosition[0]-1,selectedPosition[1])
                newPath = path.copy()
                newPath.append(newPosition)
                queue.append((newPath, cost+1+heuristicMaze(newPosition, end)))
                
            if(isMazeMoveLegal(selectedPosition, 'U', mazeArray)):
                newPosition = (selectedPosition[0],selectedPosition[1]-1)
                newPath = path.copy()
                newPath.append(newPosition)
                queue.append((newPath, cost+1+heuristicMaze(newPosition, end)))
                
            if(isMazeMoveLegal(selectedPosition, 'R', mazeArray)):
                newPosition = (selectedPosition[0]+1,selectedPosition[1])
                newPath = path.copy()
                newPath.append(newPosition)
                queue.append((newPath, cost+1+heuristicMaze(newPosition, end)))
                
            if(isMazeMoveLegal(selectedPosition, 'D', mazeArray)):
                newPosition = (selectedPosition[0],selectedPosition[1]+1)
                newPath = path.copy()
                newPath.append(newPosition)
                queue.append((newPath, cost+1+heuristicMaze(newPosition, end)))
    return None
        
def ucsPuzzle(puzzleArray):
    queue = []          #a list containing the paths and moves
    queue.append(([puzzleArray], []))
    visited = []        #list of positions processed
    while(len(queue)>0):
        path = queue[0][0]
        moves = queue[0][1]
        selectedPuzzle = path[-1]
        queue.remove(queue[0])
        if(selectedPuzzle in visited):
            continue
        visited.append(copy2(selectedPuzzle)) 
        if(isPuzzleCompleted(selectedPuzzle)):
            return moves, fixPath(visited), len(moves), len(moves)
        else:
            if(isPuzzleMoveLegal(selectedPuzzle, 'L')):
                newPuzzle = copy2(selectedPuzzle)
                newPath = copy3(path)
                newMoves = moves.copy()
                
                makePuzzleMove(newPuzzle, 'L')
                
                newPath.append(newPuzzle)
                newMoves.append('LEFT')
                queue.append((newPath, newMoves))
                
            if(isPuzzleMoveLegal(selectedPuzzle, 'U')):
                newPuzzle = copy2(selectedPuzzle)
                newPath = copy3(path)
                newMoves = moves.copy()
                
                makePuzzleMove(newPuzzle, 'U')
                
                newPath.append(newPuzzle)
                newMoves.append('UP')
                queue.append((newPath, newMoves))
                
            if(isPuzzleMoveLegal(selectedPuzzle, 'R')):
                newPuzzle = copy2(selectedPuzzle)
                newPath = copy3(path)
                newMoves = moves.copy()
                
                makePuzzleMove(newPuzzle, 'R')
                
                newPath.append(newPuzzle)
                newMoves.append('RIGHT')
                queue.append((newPath, newMoves))
                
            if(isPuzzleMoveLegal(selectedPuzzle, 'D')):
                newPuzzle = copy2(selectedPuzzle)
                newPath = copy3(path)
                newMoves = moves.copy()
                
                makePuzzleMove(newPuzzle, 'D')
                
                newPath.append(newPuzzle)
                newMoves.append('DOWN')
                queue.append((newPath, newMoves))   
    return None

def aStarPuzzle(puzzleArray):
    queue = []          #a list containing the paths, moves and the manhattan distance heuristic value for the moment
    queue.append(([puzzleArray], [], heuristicPuzzle(puzzleArray)))
    visited = []        #list of positions processed
    while(len(queue)>0):
        index = minCostPuzzle(queue)
        path = queue[index][0]
        moves = queue[index][1]
        selectedPuzzle = path[-1]
        queue.remove(queue[index])
        if(selectedPuzzle in visited):
            continue
        visited.append(copy2(selectedPuzzle))
        if(isPuzzleCompleted(selectedPuzzle)):
            return moves, fixPath(visited), len(moves), len(moves)
        else:
            if(isPuzzleMoveLegal(selectedPuzzle, 'L')):
                newPuzzle = copy2(selectedPuzzle)
                newPath = copy3(path)
                newMoves = moves.copy()
                
                makePuzzleMove(newPuzzle, 'L')
                
                newPath.append(newPuzzle)
                newMoves.append('LEFT')
                queue.append((newPath, newMoves, heuristicPuzzle(newPuzzle)+len(newMoves)))
                
            if(isPuzzleMoveLegal(selectedPuzzle, 'U')):
                newPuzzle = copy2(selectedPuzzle)
                newPath = copy3(path)
                newMoves = moves.copy()
                
                makePuzzleMove(newPuzzle, 'U')
                
                newPath.append(newPuzzle)
                newMoves.append('UP')
                queue.append((newPath, newMoves, heuristicPuzzle(newPuzzle)+len(newMoves)))
                
            if(isPuzzleMoveLegal(selectedPuzzle, 'R')):
                newPuzzle = copy2(selectedPuzzle)
                newPath = copy3(path)
                newMoves = moves.copy()
                
                makePuzzleMove(newPuzzle, 'R')
                
                newPath.append(newPuzzle)
                newMoves.append('RIGHT')
                queue.append((newPath, newMoves, heuristicPuzzle(newPuzzle)+len(newMoves)))
                
            if(isPuzzleMoveLegal(selectedPuzzle, 'D')):
                newPuzzle = copy2(selectedPuzzle)
                newPath = copy3(path)
                newMoves = moves.copy()
                
                makePuzzleMove(newPuzzle, 'D')
                
                newPath.append(newPuzzle)
                newMoves.append('DOWN')
                queue.append((newPath, newMoves, heuristicPuzzle(newPuzzle)+len(newMoves)))    
    return None

def InformedSearch(method_name, problem_file_name):
    with open(problem_file_name) as file:
        lines = file.read().splitlines()
        
    if(problem_file_name[0] == 'm'):
        start = (int(lines[0][1:lines[0].index(',')]), int(lines[0][lines[0].index(',')+1:-1]))         #x,y positions of the start tuple
        end = (int(lines[1][1:lines[1].index(',')]), int(lines[1][lines[1].index(',')+1:-1]))           #x,y positions of the end tuple
        mazeArray = []
        for item in lines[2:]:
            mazeline = []           #list containing lists, each one is representation of lines of maze
            for character in item:
                if(character == " "):           #adds 0 for the empty space
                    mazeline.append(0)
                elif(character == "#"):         #adds 1 for the walls
                    mazeline.append(1)
            mazeArray.append(mazeline)
        
        if(method_name == "UCS"):
            return ucsMaze(start, end, mazeArray)
        elif(method_name == "AStar"):
            return aStarMaze(start, end, mazeArray)
                
    elif(problem_file_name[0] == 'e'):
        puzzleArray = []
        for item in lines[:3]:      #gets start position of the puzzle
            puzzleArray.append(item.split())
     
        if(method_name == "UCS"):
            return ucsPuzzle(puzzleArray)
        elif(method_name == "AStar"):
            return aStarPuzzle(puzzleArray)  
