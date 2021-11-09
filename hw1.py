def bfs(start, end, edges):
    paths = [[start]]
    visited_nodes = [start]
    index = 0

    while(index<len(paths)):
        selectedPath = paths[index]
        selectedNode = selectedPath[-1]
        for item in edges:
            if(item[0] == selectedNode):
                visited_nodes.append(item[1])
                newPath = selectedPath.copy()
                newPath.append(item[1])
                if(item[1] == end):
                    return newPath, visited_nodes, len(newPath)-1
                paths.append(newPath)
            elif(item[1] == selectedNode):
                visited_nodes.append(item[0])
                newPath = selectedPath.copy()
                newPath.append(item[0])
                if(item[0] == end):
                    return newPath, visited_nodes, len(newPath)-1
                paths.append(newPath)
        index+=1
    return None

def dls(start, end, edges, max_depth, visitedNodes, path):
    selectedPath = path.copy()
    selectedPath.append(start)
    visitedNodes.append(start)
    if(max_depth == 0):
        if(start == end):
            path.append(end)
            return
        else:
            return
    
    selectedNode = start
    for item in edges:
        if(item[0] == selectedNode):
            dls(item[1], end, edges, max_depth-1, visitedNodes, selectedPath)
            if(visitedNodes[-1] == end):
                l = len(selectedPath) - len(path)
                path.extend(selectedPath[-l:])
                return
        elif(item[1] == selectedNode):
            dls(item[0], end, edges, max_depth-1, visitedNodes, selectedPath)
            if(visitedNodes[-1] == end):
                l = len(selectedPath) - len(path)
                path.extend(selectedPath[-l:])
                return
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
        visitedNodes = []
        path = []
        dls(lines[0], lines[1], edges, maximum_depth_limit, visitedNodes, path)
        if(visitedNodes[-1] == lines[1]):
            return path, visitedNodes, len(path)-1
        else:
            return None
    elif method_name == "IDDFS":
        return iddfs(lines[0], lines[1], edges, maximum_depth_limit)
    elif method_name == "USC":
        return ucs(lines[0], lines[1], edges)
