import copy
import random

def getAction(action, action_probabilities):
    if(action == '<'):
        actual_action = random.choices(['V', '<', '^'], weights=action_probabilities)[0]
    elif(action == '^'):
        actual_action = random.choices(['<', '^', '>'], weights=action_probabilities)[0]
    elif(action == '>'):
        actual_action = random.choices(['^', '>', 'V'], weights=action_probabilities)[0]
    else:
        actual_action = random.choices(['>', 'V', '<'], weights=action_probabilities)[0]
    return actual_action
    
def calculateUtilityTD(environment, current_state, next_state, lr, reward, gamma):
    current_value = environment[current_state[0]][current_state[1]]
    return current_value + lr*(reward + gamma*environment[next_state[0]][next_state[1]] - current_value)

def calculateUtilityQ(q_table, action, current_state, next_state, lr, reward, gamma):
    actions = ['<', '^', '>', 'V']
    current_value = q_table[current_state[0]][current_state[1]][actions.index(action)]
    return current_value + lr*(reward + gamma*max(q_table[next_state[0]][next_state[1]]) - current_value)

def getNextState(environment, position, action):
    height = len(environment)
    width = len(environment[0])
    if(action == '<'):
        if((position[1] != 0) and (environment[position[0]][position[1]-1] != None)):
            return (position[0],position[1]-1)
    elif(action == '^'):
        if((position[0] != 0) and (environment[position[0]-1][position[1]] != None)):
            return (position[0]-1, position[1])
    elif(action == '>'):
        if((position[1] != width-1) and (environment[position[0]][position[1]+1] != None)):
            return (position[0], position[1]+1)
    elif(action == 'V'):
        if((position[0] != height-1) and (environment[position[0]+1][position[1]] != None)):
            return (position[0]+1, position[1])
    return position

def chooseMaxTD(environment, position):
    values = []
    directions = []
    if((position[1] != 0) and (environment[position[0]][position[1]-1] != None)):
        values.append(environment[position[0]][position[1]-1])
    else:
        values.append(environment[position[0]][position[1]])
    directions.append('<')
    if((position[0] != 0) and (environment[position[0]-1][position[1]] != None)):
        values.append(environment[position[0]-1][position[1]])
    else:
        values.append(environment[position[0]][position[1]])
    directions.append('^')
    if((position[1] != len(environment[0])-1) and (environment[position[0]][position[1]+1] != None)):
        values.append(environment[position[0]][position[1]+1])
    else:
        values.append(environment[position[0]][position[1]])
    directions.append('>')
    if((position[0] != len(environment)-1) and (environment[position[0]+1][position[1]] != None)):
        values.append(environment[position[0]+1][position[1]])
    else:
        values.append(environment[position[0]][position[1]])
    directions.append('V')
    action = directions[values.index(max(values))]
    return action

def bestActions(environment, directions, goal_states):
    for i in range(len(environment)):
        for j in range(len(environment[0])):
            if((i,j) not in goal_states and environment[i][j] is not None):
                values = []
                arrows = []
                if((j != 0) and (environment[i][j-1] != None)):
                    values.append(environment[i][j-1])
                    arrows.append('<')
                if((i != 0) and (environment[i-1][j] != None)):
                    values.append(environment[i-1][j])
                    arrows.append('^')
                if((j != len(environment[0])-1) and (environment[i][j+1] != None)):
                    values.append(environment[i][j+1])
                    arrows.append('>')
                if((i != len(environment)-1) and (environment[i+1][j] != None)):
                    values.append(environment[i+1][j])
                    arrows.append('V')
                directions[i][j] =arrows[values.index(max(values))]                

def bestActionsQ(environment, directions, goal_states, action_probabilities):
    for i in range(len(environment)):
        for j in range(len(environment[0])):
            if((i,j) not in goal_states and environment[i][j] is not None):
                values = [0., 0., 0., 0.]
                arrows = ['<', '^', '>', 'V']
                if((j != 0) and (environment[i][j-1] != None)):
                    values[0] += action_probabilities[1]*environment[i][j-1]
                else:
                    values[0] += action_probabilities[1]*environment[i][j]
                if((i != len(environment)-1) and (environment[i+1][j] != None)):
                    values[0] += action_probabilities[0]*environment[i+1][j]
                else:
                    values[0] += action_probabilities[0]*environment[i][j]
                if((i != 0) and (environment[i-1][j] != None)):
                    values[0] += action_probabilities[2]*environment[i-1][j]
                else:
                    values[0] += action_probabilities[2]*environment[i][j]
                    
                if((i != 0) and (environment[i-1][j] != None)):
                    values[1] += action_probabilities[1]*environment[i-1][j]
                else:
                    values[1] += action_probabilities[1]*environment[i][j]
                if((j != 0) and (environment[i][j-1] != None)):
                    values[1] += action_probabilities[0]*environment[i][j-1]
                else:
                    values[1] += action_probabilities[0]*environment[i][j]
                if((j != len(environment[0])-1) and (environment[i][j+1] != None)):
                    values[1] += action_probabilities[2]*environment[i][j+1]
                else:
                    values[1] += action_probabilities[2]*environment[i][j]
                    
                if((j != len(environment[0])-1) and (environment[i][j+1] != None)):
                    values[2] += action_probabilities[1]*environment[i][j+1]
                else:
                    values[2] += action_probabilities[1]*environment[i][j]
                if((i != len(environment)-1) and (environment[i+1][j] != None)):
                    values[2] += action_probabilities[0]*environment[i+1][j]
                else:
                    values[2] += action_probabilities[0]*environment[i][j]
                if((i != 0) and (environment[i-1][j] != None)):
                    values[2] += action_probabilities[2]*environment[i-1][j]
                else:
                    values[2] += action_probabilities[2]*environment[i][j]
                    
                if((i != len(environment)-1) and (environment[i+1][j] != None)):
                    values[3] += action_probabilities[1]*environment[i+1][j]
                else:
                    values[3] += action_probabilities[1]*environment[i][j]
                if((j != 0) and (environment[i][j-1] != None)):
                    values[3] += action_probabilities[0]*environment[i][j-1]
                else:
                    values[3] += action_probabilities[0]*environment[i][j]
                if((j != len(environment[0])-1) and (environment[i][j+1] != None)):
                    values[3] += action_probabilities[2]*environment[i][j+1]
                else:
                    values[3] += action_probabilities[2]*environment[i][j]
                
                directions[i][j] =arrows[values.index(max(values))]
                
def TD0(environment, directions, goal_states, goal_values, start_state, reward, action_probabilities, lr, gamma, epsilon, episode_count):
    current_values = copy.deepcopy(environment)
    
    for episode in range(episode_count):
        current_state = start_state
        while(current_state not in goal_states):
            if(random.random() <= epsilon):
                actions = ["<", "^", ">", "V"]
                selected_action = actions[random.randint(0, 3)]
            else:
                selected_action = chooseMaxTD(current_values, current_state)
            actual_action = getAction(selected_action, action_probabilities)
            next_state = getNextState(current_values, current_state, actual_action)
            
            if(next_state in goal_states):
                utility_score = calculateUtilityTD(current_values, current_state, next_state, lr, reward+goal_values[goal_states.index(next_state)], gamma)
                current_values[current_state[0]][current_state[1]] = utility_score
                break
            else:
                utility_score = calculateUtilityTD(current_values, current_state, next_state, lr, reward, gamma)
                current_values[current_state[0]][current_state[1]] = utility_score
                current_state = next_state
    for i in range(len(goal_states)):
        current_values[goal_states[i][0]][goal_states[i][1]] = goal_values[i]
    bestActions(current_values, directions, goal_states)
    return current_values, directions

def Q_Learning(environment, directions, goal_states, goal_values, start_state, reward, action_probabilities, lr, gamma, epsilon, episode_count):
    current_values = copy.deepcopy(environment)
    q_table = []
    for i in range(len(environment)):
        arr = []
        for j in range(len(environment[0])):
            if(environment[i][j] is not None):
                arr.append([0., 0., 0., 0.])
            else:
                arr.append(None)
        q_table.append(arr)
    actions = ["<", "^", ">", "V"]
        
    for episode in range(episode_count):
        current_state = start_state
        while(current_state not in goal_states):
            if(random.random() <= epsilon):
                selected_action = actions[random.randint(0, 3)]
            else:
                arr = q_table[current_state[0]][current_state[1]]
                selected_action = actions[arr.index(max(arr))]
            actual_action = getAction(selected_action, action_probabilities)
            next_state = getNextState(environment, current_state, actual_action)
            
            if(next_state in goal_states):
                utility_score = calculateUtilityQ(q_table, selected_action, current_state, next_state, lr, reward+goal_values[goal_states.index(next_state)], gamma)
                q_table[current_state[0]][current_state[1]][actions.index(selected_action)] = utility_score
                break
            else:
                utility_score = calculateUtilityQ(q_table, selected_action, current_state, next_state, lr, reward, gamma)
                q_table[current_state[0]][current_state[1]][actions.index(selected_action)] = utility_score
                current_state = next_state
    for i in range(len(environment)):
        for j in range(len(environment[0])):
            if(current_values[i][j] is not None):
                current_values[i][j] = max(q_table[i][j])
    for i in range(len(goal_states)):
        current_values[goal_states[i][0]][goal_states[i][1]] = goal_values[i]
    bestActionsQ(current_values, directions, goal_states, action_probabilities)
    return current_values, directions

def SolveMDP(method_name, problem_file_name, random_seed):
    random.seed(random_seed)
    
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

    start_state = (int(lines[7][1:lines[7].find(',')]), int(lines[7][lines[7].find(',')+1:-1]))

    reward = float(lines[9])
    action_probabilities = [float(lines[12]), float(lines[11]), float(lines[13])]
    learning_rate = float(lines[15])
    gamma = float(lines[17])
    epsilon = float(lines[19])
    episode_count = int(lines[21])

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
        
    valueDictionary = {}
    actionDictionary = {}
    final_values, final_directions = None, None
    
    if(method_name == "TD(0)"):
        final_values, final_directions = TD0(environment, directions, goal_states, goal_values, start_state, reward, action_probabilities, learning_rate, gamma, epsilon, episode_count)    
    else:
        final_values, final_directions = Q_Learning(environment, directions, goal_states, goal_values, start_state, reward, action_probabilities, learning_rate, gamma, epsilon, episode_count)
        
    for i in range(len(final_values)):
        for j in range(len(final_values[0])):
            if(final_values[i][j] != None):
                final_values[i][j] = round(final_values[i][j], 2)
            else:
                final_values[i][j] = 0.0

    for i in range(len(final_values)):
        for j in range(len(final_values[0])):
            if((i,j) not in obstacle_states):
                valueDictionary[(i,j)] = final_values[i][j]
            if((i,j) not in obstacle_states and (i,j) not in goal_states):
                actionDictionary[(i,j)] = final_directions[i][j]
    return valueDictionary, actionDictionary


#print(SolveMDP('Q-learning', 'mdp3.txt', 462))
