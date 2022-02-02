def getMax(arr):            #returns maximum element of an array
    value = arr[0][1]
    idx = arr[0][0]
    for item in arr[1:]:
        if(item[1] > value):
            value = item[1]
            idx = item[0]
    return idx, value

def calculate_viterbi(A, B, pi, O):
    N = len(A)
    M = len(B[0])
    T = len(O)
    
    result = []
    for i in range(N):
        arr = []
        for j in range(T):
            arr.append((None, 0.0))
        result.append(arr)
    
    for j in range(N):
        result[j][0] = (None, pi[j]*B[j][O[0]])
    
    for j in range(1,T):
        for i in range(N):
            values = []
            for k in range(N):
                values.append((k, result[k][j-1][1]*A[k][i]*B[i][O[j]]))
            result[i][j] = getMax(values)

    state_sequence = []
    idx, final_prob = getMax([row[-1] for row in result])
    state_sequence.insert(0, [row[-1] for row in result].index((idx, final_prob)))
    state_sequence.insert(0, idx)
    
    for m in range(T-2, 0, -1):
        idx = result[idx][m][0]
        state_sequence.insert(0, idx)

    return state_sequence


def viterbi(problem_file_name):
    with open (problem_file_name) as file:
        lines = file.read().splitlines()
        
    num_of_states = lines[1].count('|')+1
    
    pi_text = lines[3].split('|')
    pi=[]
    for item in pi_text:
        pi.append(float(item[item.find(':')+1:]))
    
    transition_text = lines[5].split('|')
    transitions_arr = []
    for item in transition_text:
        transitions_arr.append(float(item[item.find(':')+1:]))
        
    transition_probs = []
    for i in range(0, len(transitions_arr), num_of_states):
        transition_probs.append(transitions_arr[i:i+num_of_states])
    
    observations_text = lines[7].split('|')
    observations_arr = []
    for item in observations_text:
        observations_arr.append(float(item[item.find(':')+1:]))
        
    observation_probs = []
    for i in range(0, len(observations_arr), len(observations_arr)//num_of_states):
        observation_probs.append(observations_arr[i:i+(len(observations_arr)//num_of_states)])
    
    observation_queue_text = lines[9].split('|')
    observations = []
    for item in observation_queue_text:
        observations.append(int(item[item.find('s')+1:])-1)
        
    states, result = calculate_viterbi(transition_probs, observation_probs, pi, observations)
    
    output_states = []
    for i in range(len(states)):
        output_states.append('state'+str(states[i]+1))
    
    final_probabilty = getMax([row[-1] for row in result])
    
    state_dictionary = {}
    for i in range(num_of_states):
        state_dictionary.update({'state'+str(i+1): result[i]})
    
    return output_states, final_probabilty, state_dictionary

A = [[0.2, 0.8],[0.3, 0.7]]
B = [[0.75, 0.25], [0.4, 0.6]]
pi = [0.5, 0.5]
O = [0, 1, 1, 1, 0]

print(calculate_viterbi(A, B, pi, O))
