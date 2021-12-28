def SolveMDP(method_name, problem_file_name):
    with open (problem_file_name) as file:
        lines = file.read().splitlines()
    row = lines[1][:lines[1].find(' ')]
    column = lines[1][lines[1].find(' ')+1:]
    
    obstacle_states = []
    obstacle_string = lines[3].split('|')
    for item in obstacle_string:
        x = int(item[1:item.find(',')])
        y = int(item[item.find(',')+1:-1])
        obstacle_states.append((x,y))
        
    goal_states = []
    goal_string = lines[5].split('|')
    for item in goal_string:
        x = int(item[1:item.find(',')])
        y = int(item[item.find(',')+1:item.find(')')])
        value = float(item[item.find(':')+1:])
        goal_states.append([(x,y), value])

    reward = float(lines[7])
    action_probabilities = [float(lines[9]), float(lines[10]), float(lines[11])]
    gamma = float(lines[13])
    epsilon = float(lines[15])
    num_iteration = float(lines[17])

    if(method_name == "ValueIteration"):
        pass
    elif(method_name == "PolicyIteration"):
        pass
