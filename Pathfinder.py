pythag = lambda a, b: (a**2 + b**2)**0.5

def reconstruct(cameFrom, current):
    path = []
    while current in cameFrom:
        path.insert(0, current)
        current = cameFrom[current]
    return path
    

def aStar(map, start, end, blocked=[], allowDiagonals=False):
    h = lambda node: pythag(node[0] - end[0], node[1] - end[1])
    d = lambda node1, node2: pythag(node1[0] - node2[0], node1[1] - node2[1])
            
    def getCurrent():
        lowest = False
        for i in openSet:
            if lowest == False or fScore[i] < fScore[lowest]:
                lowest = i
        return lowest
    
    def neighbors(node):
        changes = []
        leftEnd = node[0] != 0
        rightEnd = node[0] != len(grid)-1
        topEnd = node[1] != 0
        bottomEnd = node[1] != len(grid[0])-1
        
        if leftEnd:
            changes.append((-1, 0))
        if rightEnd:
            changes.append((1, 0))
        if topEnd:
            changes.append((0, -1))
        if bottomEnd:
            changes.append((0, 1))
            
        if allowDiagonals:
            if leftEnd and topEnd:
                changes.append((-1, -1))
            if leftEnd and bottomEnd:
                changes.append((-1, 1))
            if rightEnd and topEnd:
                changes.append((1, -1))
            if rightEnd and bottomEnd:
                changes.append((1, 1))
                
        for i in range(len(changes)):
            changes[i] = (node[0] + changes[i][0], node[1] + changes[i][1])
        remove = []
        for i in changes:
            if map[i[0]][i[1]] in blocked:
                remove.append(i)
                
        for i in remove:
            changes.remove(i)
            
        return changes
    
    grid = []
    for i in range(len(map)):
        grid.append([])
        for j in range(len(map[0])):
            grid[-1].append((i,j))
            
    high = len(grid[0])*len(grid[1])*2
    
    openSet = {start}
    cameFrom = {}
    gScore = {}
    fScore = {}
    for i in grid:
        for j in i:
            gScore[j] = high
            fScore[j] = high
    gScore[start] = 0
    fScore[start] = h(start)
    
    
    while len(openSet) > 0:
        current = getCurrent()
        if current == end:
            return reconstruct(cameFrom, current) # End here
        
        openSet.remove(current)
        for i in neighbors(current):
            
            tentativeGScore = gScore[current] + d(current, i)
            if tentativeGScore < gScore[i]: #Found best path to i
                cameFrom[i] = current
                gScore[i] = tentativeGScore
                fScore[i] = gScore[i] + h(i)
            
                if i not in openSet:
                    openSet.add(i)
                
    return False