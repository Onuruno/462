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

def isPuzzleCompleted(puzzleArray):
    if (puzzleArray == [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '0']]):
        return True
    else:
        return False
    
def isMoveLegal(puzzleArray, move):
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

def makeMove(puzzleArray, move):
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

def fixPath(path):
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

def heuristicPuzzle(puzzleArray):
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

def minCost(queue):
    value=queue[0][2]
    index=0
    for i in range(len(queue)):
        if(queue[i][2]<value):
            value=queue[i][2]
            index=i
    return index
            
def ucsMaze(start, end, mazeArray):
    return mazeArray

def aStarMaze(star, end, mazeArray):
    return mazeArray
        
def ucsPuzzle(puzzleArray):
    queue = []
    queue.append(([puzzleArray], []))
    visited = []
    while(len(queue)>0):
        path = queue[0][0]
        moves = queue[0][1]
        selectedPuzzle = path[-1]
        queue.remove(queue[0])
        if(selectedPuzzle in visited):
            continue
        if(isPuzzleCompleted(selectedPuzzle)):
            return moves, fixPath(path), len(moves), len(moves)
        else:
            if(isMoveLegal(selectedPuzzle, 'L')):
                newPuzzle = copy2(selectedPuzzle)
                newPath = copy3(path)
                newMoves = moves.copy()
                
                makeMove(newPuzzle, 'L')
                
                newPath.append(newPuzzle)
                newMoves.append('LEFT')
                queue.append((newPath, newMoves))
                
            if(isMoveLegal(selectedPuzzle, 'U')):
                newPuzzle = copy2(selectedPuzzle)
                newPath = copy3(path)
                newMoves = moves.copy()
                
                makeMove(newPuzzle, 'U')
                
                newPath.append(newPuzzle)
                newMoves.append('UP')
                queue.append((newPath, newMoves))
                
            if(isMoveLegal(selectedPuzzle, 'R')):
                newPuzzle = copy2(selectedPuzzle)
                newPath = copy3(path)
                newMoves = moves.copy()
                
                makeMove(newPuzzle, 'R')
                
                newPath.append(newPuzzle)
                newMoves.append('RIGHT')
                queue.append((newPath, newMoves))
                
            if(isMoveLegal(selectedPuzzle, 'D')):
                newPuzzle = copy2(selectedPuzzle)
                newPath = copy3(path)
                newMoves = moves.copy()
                
                makeMove(newPuzzle, 'D')
                
                newPath.append(newPuzzle)
                newMoves.append('DOWN')
                queue.append((newPath, newMoves))
        visited.append(copy2(selectedPuzzle))    
    return None

def aStarPuzzle(puzzleArray):
    queue = []
    queue.append(([puzzleArray], [], heuristicPuzzle(puzzleArray)))
    visited = []
    while(len(queue)>0):
        index=minCost(queue)
        path = queue[index][0]
        moves = queue[index][1]
        selectedPuzzle = path[-1]
        queue.remove(queue[index])
        if(selectedPuzzle in visited):
            continue
        if(isPuzzleCompleted(selectedPuzzle)):
            return moves, fixPath(path), len(moves), len(moves)
        else:
            if(isMoveLegal(selectedPuzzle, 'L')):
                newPuzzle = copy2(selectedPuzzle)
                newPath = copy3(path)
                newMoves = moves.copy()
                
                makeMove(newPuzzle, 'L')
                
                newPath.append(newPuzzle)
                newMoves.append('LEFT')
                queue.append((newPath, newMoves, heuristicPuzzle(newPuzzle)+len(newMoves)))
                
            if(isMoveLegal(selectedPuzzle, 'U')):
                newPuzzle = copy2(selectedPuzzle)
                newPath = copy3(path)
                newMoves = moves.copy()
                
                makeMove(newPuzzle, 'U')
                
                newPath.append(newPuzzle)
                newMoves.append('UP')
                queue.append((newPath, newMoves, heuristicPuzzle(newPuzzle)+len(newMoves)))
                
            if(isMoveLegal(selectedPuzzle, 'R')):
                newPuzzle = copy2(selectedPuzzle)
                newPath = copy3(path)
                newMoves = moves.copy()
                
                makeMove(newPuzzle, 'R')
                
                newPath.append(newPuzzle)
                newMoves.append('RIGHT')
                queue.append((newPath, newMoves, heuristicPuzzle(newPuzzle)+len(newMoves)))
                
            if(isMoveLegal(selectedPuzzle, 'D')):
                newPuzzle = copy2(selectedPuzzle)
                newPath = copy3(path)
                newMoves = moves.copy()
                
                makeMove(newPuzzle, 'D')
                
                newPath.append(newPuzzle)
                newMoves.append('DOWN')
                queue.append((newPath, newMoves, heuristicPuzzle(newPuzzle)+len(newMoves)))
        visited.append(copy2(selectedPuzzle))    
    return None

def InformedSearch(method_name, problem_file_name):
    with open(problem_file_name) as file:
        lines = file.read().splitlines()
        
    if(problem_file_name[0] == 'm'):
        start = lines[0]
        end = lines[1]
        mazeArray = []
        for item in lines[2:]:
            mazeline = []
            for character in item:
                if(character == " "):
                    mazeline.append(0)
                elif(character == "#"):
                    mazeline.append(1)
            mazeArray.append(mazeline)
        
        if(method_name == "UCS"):
            return ucsMaze(start, end, mazeArray)
        elif(method_name == "AStar"):
            return aStarMaze(start, end, mazeArray)
                
    elif(problem_file_name[0] == 'e'):
        puzzleArray = []
        for item in lines[:3]:
            puzzleArray.append(item.split())
     
        if(method_name == "UCS"):
            return ucsPuzzle(puzzleArray)
        elif(method_name == "AStar"):
            return aStarPuzzle(puzzleArray)
