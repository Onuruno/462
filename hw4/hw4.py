import copy

def DoAction(environment, position, action, action_probabilities, reward, gamma):
    height = len(environment)
    width = len(environment[0])
    value = 0
    if(action == '<'):
        if((position[1] != 0) and (environment[position[0]][position[1]-1] != None)):
            value += action_probabilities[0]*(reward + gamma*environment[position[0]][position[1]-1])
        else:
            value += action_probabilities[0]*(reward + gamma*environment[position[0]][position[1]])
        if((position[0] != height-1) and (environment[position[0]+1][position[1]] != None)):
            value += action_probabilities[1]*(reward + gamma*environment[position[0]+1][position[1]])
        else:
            value += action_probabilities[1]*(reward + gamma*environment[position[0]][position[1]])
        if((position[0] != 0) and (environment[position[0]-1][position[1]] != None)):
            value += action_probabilities[2]*(reward + gamma*environment[position[0]-1][position[1]])
        else:
            value += action_probabilities[2]*(reward + gamma*environment[position[0]][position[1]])
    elif(action == '^'):
        if((position[0] != 0) and (environment[position[0]-1][position[1]] != None)):
            value += action_probabilities[0]*(reward + gamma*environment[position[0]-1][position[1]])
        else:
            value += action_probabilities[0]*(reward + gamma*environment[position[0]][position[1]])
        if((position[1] != 0) and (environment[position[0]][position[1]-1] != None)):
            value += action_probabilities[1]*(reward + gamma*environment[position[0]][position[1]-1])
        else:
            value += action_probabilities[1]*(reward + gamma*environment[position[0]][position[1]])
        if((position[1] != width-1) and (environment[position[0]][position[1]+1] != None)):
            value += action_probabilities[2]*(reward + gamma*environment[position[0]][position[1]+1])
        else:
            value += action_probabilities[2]*(reward + gamma*environment[position[0]][position[1]])
    elif(action == '>'):
        if((position[1] != width-1) and (environment[position[0]][position[1]+1] != None)):
            value += action_probabilities[0]*(reward + gamma*environment[position[0]][position[1]+1])
        else:
            value += action_probabilities[0]*(reward + gamma*environment[position[0]][position[1]])
        if((position[0] != 0) and (environment[position[0]-1][position[1]] != None)):
            value += action_probabilities[1]*(reward + gamma*environment[position[0]-1][position[1]])
        else:
            value += action_probabilities[1]*(reward + gamma*environment[position[0]][position[1]])
        if((position[0] != height-1) and (environment[position[0]+1][position[1]] != None)):
            value += action_probabilities[2]*(reward + gamma*environment[position[0]+1][position[1]])
        else:
            value += action_probabilities[2]*(reward + gamma*environment[position[0]][position[1]])
    elif(action == 'V'):
        if((position[0] != height-1) and (environment[position[0]+1][position[1]] != None)):
            value += action_probabilities[0]*(reward + gamma*environment[position[0]+1][position[1]])
        else:
            value += action_probabilities[0]*(reward + gamma*environment[position[0]][position[1]])
        if((position[1] != width-1) and (environment[position[0]][position[1]+1] != None)):
            value += action_probabilities[1]*(reward + gamma*environment[position[0]][position[1]+1])
        else:
            value += action_probabilities[1]*(reward + gamma*environment[position[0]][position[1]])
        if((position[1] != 0) and (environment[position[0]][position[1]-1] != None)):
            value += action_probabilities[2]*(reward + gamma*environment[position[0]][position[1]-1])
        else:
            value += action_probabilities[2]*(reward + gamma*environment[position[0]][position[1]])
    return value

def BestAction(environment, position, actions, action_probabilities, reward, gamma):
    height = len(environment)
    width = len(environment[0])
    values = []
    for action in actions:
        value = DoAction(environment, position, action, action_probabilities, reward, gamma)
        values.append(value)
    return max(values), actions[values.index(max(values))]

def CheckDifference(first, second, epsilon):
    for row1, row2 in zip(first,second):
        for value1, value2 in zip(row1, row2):
            if((value1 != None) and (abs(value1-value2) > epsilon)):
                return False
    return True

def PolicyIteration(environment, directions, goal_states, reward, action_probabilities, gamma, num_iteration):
    current_values = copy.deepcopy(environment)
    current_directions = copy.deepcopy(directions)
    
    actions = ['<', '^', '>', 'V']
    isPolicyStable = False
    
    while(not isPolicyStable):
        for iteration in range(int(num_iteration)):
            temp_values = copy.deepcopy(current_values)
            for i in range(len(environment)):
                for j in range(len(environment[0])):
                    if((i,j) not in goal_states and current_values[i][j] != None):
                        current_values[i][j] = DoAction(temp_values, (i,j), current_directions[i][j], action_probabilities, reward, gamma)
        isPolicyStable = True
        temp_directions = copy.deepcopy(current_directions)
        for i in range(len(environment)):
            for j in range(len(environment[0])):
                if((i,j) not in goal_states and current_values[i][j] != None):
                    bestAction = BestAction(current_values, (i,j), actions, action_probabilities, reward, gamma)[1]
                    current_directions[i][j] = bestAction
                    if(temp_directions[i][j] != bestAction):
                        isPolicyStable = False
    for i in range(len(current_values)):
        for j in range(len(current_values[0])):
            if(current_values[i][j] != None):
                current_values[i][j] = round(current_values[i][j], 2)
            else:
                current_values[i][j] = 0.0
    return current_values, current_directions

def ValueIteration(environment, directions, goal_states, reward, action_probabilities, gamma, epsilon):
    current_values = copy.deepcopy(environment)
    current_directions = copy.deepcopy(directions)

    while(True):
        temp_values = copy.deepcopy(current_values)
        temp_directions = copy.deepcopy(current_directions)
        for i in range(len(environment)):
            for j in range(len(environment[0])):
                if(((i,j) not in goal_states) and (environment[i][j] != None)):
                    actions = ['<', '^', '>', 'V']
                    value, action = BestAction(temp_values, (i,j), actions, action_probabilities, reward, gamma)
                    current_values[i][j] = value
                    current_directions[i][j] = action
        if(CheckDifference(current_values, temp_values, epsilon)):
            break
        
    for i in range(len(current_values)):
        for j in range(len(current_values[0])):
            if(current_values[i][j] != None):
                current_values[i][j] = round(current_values[i][j], 2)
            else:
                current_values[i][j] = 0.0
    return current_values, current_directions

def SolveMDP(method_name, problem_file_name):
    with open (problem_file_name) as file:
        lines = file.read().splitlines()
    row = int(lines[1][:lines[1].find(' ')])
    column = int(lines[1][lines[1].find(' ')+1:])
    
    obstacle_states = []
    obstacle_string = lines[3].split('|')
    for item in obstacle_string:
        x = int(item[1:item.find(',')])
        y = int(item[item.find(',')+1:-1])
        obstacle_states.append((x,y))
        
    goal_states = []
    goal_values = []
    goal_string = lines[5].split('|')
    for item in goal_string:
        x = int(item[1:item.find(',')])
        y = int(item[item.find(',')+1:item.find(')')])
        value = float(item[item.find(':')+1:])
        goal_states.append((x,y))
        goal_values.append(value)

    reward = float(lines[7])
    action_probabilities = [float(lines[9]), float(lines[10]), float(lines[11])]
    gamma = float(lines[13])
    epsilon = float(lines[15])
    num_iteration = float(lines[17])

    environment = []
    directions = []
    for i in range(row):
        arr = []
        arr2 = []
        for j in range(column):
            arr.append(0.)
            arr2.append('^')
        environment.append(arr)
        directions.append(arr2)
    for i in obstacle_states:
        environment[i[0]][i[1]] = None
    for i in range(len(goal_states)):
        environment[goal_states[i][0]][goal_states[i][1]] = goal_values[i]
        
    valueDictionary = {}
    actionDictionary = {}
    final_values, final_directions = None, None
    
    if(method_name == "ValueIteration"):
        final_values, final_directions = ValueIteration(environment, directions, goal_states, reward, action_probabilities, gamma, epsilon)                
    elif(method_name == "PolicyIteration"):
        final_values, final_directions = PolicyIteration(environment, directions, goal_states, reward, action_probabilities, gamma, num_iteration)
    
    for i in range(len(final_values)):
        for j in range(len(final_values[0])):
            valueDictionary[(i,j)] = final_values[i][j]
            if((i,j) not in obstacle_states and (i,j) not in goal_states):
                actionDictionary[(i,j)] = final_directions[i][j]
    return valueDictionary, actionDictionary
