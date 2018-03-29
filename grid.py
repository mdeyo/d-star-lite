from graph import Node, Graph


class GridWorld(Graph):
    def __init__(self, x_dim, y_dim, connect8=True):
        self.x_dim = x_dim
        self.y_dim = y_dim
        # First make an element for each row (height of grid)
        self.cells = [0] * y_dim
        # Go through each element and replace with row (width of grid)
        for i in range(y_dim):
            self.cells[i] = [0] * x_dim
        # will this be an 8-connected graph or 4-connected?
        self.connect8 = connect8
        self.graph = {}

        self.generateGraphFromGrid()
        # self.printGrid()

    def __str__(self):
        msg = 'Graph:'
        for i in self.graph:
            msg += '\n  node: ' + i + ' g: ' + \
                str(self.graph[i].g) + ' rhs: ' + str(self.graph[i].rhs) + \
                ' neighbors: ' + str(self.graph[i].children)
        return msg

    def __repr__(self):
        return self.__str__()

    def printGrid(self):
        print('** GridWorld **')
        for row in self.cells:
            print(row)

    def printGValues(self):
        for j in range(self.y_dim):
            str_msg = ""
            for i in range(self.x_dim):
                node_id = 'x' + str(i) + 'y' + str(j)
                node = self.graph[node_id]
                if node.g == float('inf'):
                    str_msg += ' - '
                else:
                    str_msg += ' ' + str(node.g) + ' '
            print(str_msg)

    def generateGraphFromGrid(self):
        edge = 1
        for i in range(len(self.cells)):
            row = self.cells[i]
            for j in range(len(row)):
                # print('graph node ' + str(i) + ',' + str(j))
                node = Node('x' + str(i) + 'y' + str(j))
                if i > 0:  # not top row
                    node.parents['x' + str(i - 1) + 'y' + str(j)] = edge
                    node.children['x' + str(i - 1) + 'y' + str(j)] = edge
                if i + 1 < self.y_dim:  # not bottom row
                    node.parents['x' + str(i + 1) + 'y' + str(j)] = edge
                    node.children['x' + str(i + 1) + 'y' + str(j)] = edge
                if j > 0:  # not left col
                    node.parents['x' + str(i) + 'y' + str(j - 1)] = edge
                    node.children['x' + str(i) + 'y' + str(j - 1)] = edge
                if j + 1 < self.x_dim:  # not right col
                    node.parents['x' + str(i) + 'y' + str(j + 1)] = edge
                    node.children['x' + str(i) + 'y' + str(j + 1)] = edge
                self.graph['x' + str(i) + 'y' + str(j)] = node
