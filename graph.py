class Node:
    def __init__(self, id):
        self.id = id
        # dictionary of parent node ID's
        # key = id of parent
        # value = (edge cost,)
        self.parents = {}
        # dictionary of children node ID's
        # key = id of child
        # value = (edge cost,)
        self.children = {}
        # g approximation
        self.g = float('inf')
        # rhs value
        self.rhs = float('inf')

    def __str__(self):
        return 'Node: ' + self.id + ' g: ' + str(self.g) + ' rhs: ' + str(self.rhs)

    def __repr__(self):
        return self.__str__()

    def update_parents(self, parents):
        self.parents = parents


class Graph:
    def __init__(self):
        self.graph = {}

    def __str__(self):
        msg = 'Graph:'
        for i in self.graph:
            msg += '\n  node: ' + i + ' g: ' + \
                str(self.graph[i].g) + ' rhs: ' + str(self.graph[i].rhs)
        return msg

    def __repr__(self):
        return self.__str__()

    def setStart(self, id):
        if(self.graph[id]):
            self.start = id
        else:
            raise ValueError('start id not in graph')

    def setGoal(self, id):
        if(self.graph[id]):
            self.goal = id
        else:
            raise ValueError('goal id not in graph')


def addNodeToGraph(graph, id, neighbors, edge=1):
    node = Node(id)
    for i in neighbors:
        # print(i)
        node.parents[i] = edge
        node.children[i] = edge
    graph[id] = node
    return graph


def makeGraph():
    graph = {}

    # 8-connected graph (w diagonals)
    # Impossible to find path - 2 obstacles in middle
    # graph = addNodeToGraph(graph, 'x1y1', ['x1y2', 'x2y1', 'x2y2'])
    # graph = addNodeToGraph(
    #     graph, 'x2y1', ['x1y1', 'x1y2', 'x3y1', 'x2y2', 'x3y2'], float('inf'))
    # graph = addNodeToGraph(graph, 'x1y2', ['x1y1', 'x2y1', 'x2y2'])
    # graph = addNodeToGraph(
    #     graph, 'x2y2', ['x1y1', 'x1y2', 'x3y1', 'x2y1', 'x3y2'], float('inf'))
    # graph = addNodeToGraph(graph, 'x3y1', ['x3y2', 'x2y1', 'x2y2'])
    # graph = addNodeToGraph(graph, 'x3y2', ['x3y1', 'x2y1', 'x2y2'])

    # 8-connected graph (w diagonals)
    # Impossible to find path - 2 obstacles in middle
    # graph = addNodeToGraph(graph, 'x1y1', ['x1y2', 'x2y1', 'x2y2'])
    # graph = addNodeToGraph(
    #     graph, 'x2y1', ['x1y1', 'x1y2', 'x3y1', 'x2y2', 'x3y2'], float('inf'))
    # graph = addNodeToGraph(graph, 'x1y2', ['x1y1', 'x2y1', 'x2y2'])
    # graph = addNodeToGraph(
    #     graph, 'x2y2', ['x1y1', 'x1y2', 'x3y1', 'x2y1', 'x3y2'])
    # graph = addNodeToGraph(graph, 'x3y1', ['x3y2', 'x2y1', 'x2y2'])
    # graph = addNodeToGraph(graph, 'x3y2', ['x3y1', 'x2y1', 'x2y2'])

    # 4-connected graph (w/out diagonals)
    graph = addNodeToGraph(graph, 'x1y1', ['x1y2', 'x2y1'])
    graph = addNodeToGraph(graph, 'x2y1', ['x1y1', 'x3y1', 'x2y2'])
    graph = addNodeToGraph(graph, 'x1y2', ['x1y1', 'x2y2'])
    graph = addNodeToGraph(graph, 'x2y2', ['x1y2', 'x2y1', 'x3y2'])
    graph = addNodeToGraph(graph, 'x3y1', ['x3y2', 'x2y1'])
    graph = addNodeToGraph(graph, 'x3y2', ['x3y1', 'x2y2'])

    g = GridWorld(X_DIM, Y_DIM)
    # g.graph = graph
    # print(g)
    return g
