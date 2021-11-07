def bfs(start, end, edges):
    result_list = []
    index = 0
    result_list.append(start)

    while(index<len(result_list)):
        item = result_list[index]
        for i in edges:
            if(i[0] == item):
                result_list.append(i[1])
                if(i[1] == end):
                    return result_list
            if(i[1] == item):
                result_list.append(i[0])
                if(i[0] == end):
                    return result_list
        index+=1
    
    return None

def dls(start, end, edges, max_depth):
    return

def iddfs(start, end, edges, max_depth):
    return

def ucs(start, end, edges):
    return

def UnInformedSearch(method_name, problem_file_name, maximum_depth_limit):
    edges = []

    with open(problem_file_name) as file:
        lines = file.read().splitlines()

    for item in lines[2:]:
        edges.append(item.split())

    if method_name == "BFS":
        return bfs(lines[0], lines[1], edges)
    elif method_name == "DLS":
        return dls(lines[0], lines[1], edges, maximum_depth_limit)
    elif method_name == "IDDFS":
        return iddfs(lines[0], lines[1], edges, maximum_depth_limit)
    elif method_name == "USC":
        return ucs(lines[0], lines[1], edges)

print(UnInformedSearch("BFS", 'test.txt', 3))