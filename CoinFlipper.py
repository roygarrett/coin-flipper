class Queue:
    """Queue implementation as a list"""

    def __init__(self):
        """Create new queue"""
        self._items = []

    def is_empty(self):
        """Check if the queue is empty"""
        return not bool(self._items)

    def enqueue(self, item):
        """Add an item to the queue"""
        self._items.insert(0, item)

    def dequeue(self):
        """Remove an item from the queue"""
        return self._items.pop()

    def size(self):
        """Get the number of items in the queue"""
        return len(self._items)


class Vertex:
    def __init__(self, key, distance=0, predecessor=None, color='white'):
        self.id = key
        self.connectedTo = {}
        self.distance = distance
        self.predecessor = predecessor
        self.color = color

    def getDistance(self):
        return self.distance

    def setDistance(self, num):
        self.distance = num

    def getPred(self):
        return self.predecessor

    def setPred(self, p):
        self.predecessor = p

    def getColor(self):
        return self.color

    def setColor(self, c):
        self.color = c

    def addNeighbor(self, nbr, weight=0):
        self.connectedTo[nbr] = weight

    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])

    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self,nbr):
        return self.connectedTo[nbr]


class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self,key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self,n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def __contains__(self,n):
        return n in self.vertList

    def addEdge(self, f, t, weight=0):
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], weight)

    def getVertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())


def bfs(g, start):
  start.setDistance(0)
  start.setPred(None)
  vertQueue = Queue()
  vertQueue.enqueue(start)
  while (vertQueue.size() > 0):
    currentVert = vertQueue.dequeue()
    for nbr in currentVert.getConnections():
      if (nbr.getColor() == 'white'):
        nbr.setColor('gray')
        nbr.setDistance(currentVert.getDistance() + 1)
        nbr.setPred(currentVert)
        vertQueue.enqueue(nbr)
    currentVert.setColor('black')


def flip(num):
    if num == '0':
        return '1'
    if num == '1':
        return '0'


def coin_flip(num, node):
    l = list(node)
    if num == 1:
        l[-1] = flip(l[-1])
        l[-2] = flip(l[-2])
        l[-4] = flip(l[-4])
    if num == 2:
        l[-1] = flip(l[-1])
        l[-2] = flip(l[-2])
        l[-3] = flip(l[-3])
        l[-5] = flip(l[-5])
    if num == 3:
        l[-2] = flip(l[-2])
        l[-3] = flip(l[-3])
        l[-6] = flip(l[-6])
    if num == 4:
        l[-1] = flip(l[-1])
        l[-4] = flip(l[-4])
        l[-5] = flip(l[-5])
        l[-7] = flip(l[-7])
    if num == 5:
        l[-2] = flip(l[-2])
        l[-4] = flip(l[-4])
        l[-5] = flip(l[-5])
        l[-6] = flip(l[-6])
        l[-8] = flip(l[-8])
    if num == 6:
        l[-3] = flip(l[-3])
        l[-5] = flip(l[-5])
        l[-6] = flip(l[-6])
        l[-9] = flip(l[-9])
    if num == 7:
        l[-4] = flip(l[-4])
        l[-7] = flip(l[-7])
        l[-8] = flip(l[-8])
    if num == 8:
        l[-5] = flip(l[-5])
        l[-7] = flip(l[-7])
        l[-8] = flip(l[-8])
        l[-9] = flip(l[-9])
    if num == 9:
        l[-6] = flip(l[-6])
        l[-8] = flip(l[-8])
        l[-9] = flip(l[-9])
    new_node = ''
    for i in l:
        new_node += i
    return new_node


def display(node):
    stringy = ''
    l = list(node)
    l.reverse()
    stringy += '\n'
    for n in l[:3]:
        if n == '0':
            stringy += 'H'
        else:
            stringy += 'T'
    stringy += '\n'
    for n in l[3:6]:
        if n == '0':
            stringy += 'H'
        else:
            stringy += 'T'
    stringy += '\n'
    for n in l[6:]:
        if n == '0':
            stringy += 'H'
        else:
            stringy += 'T'
    stringy += '\n'
    print(stringy)


def get_node_num(b, node):
    return list(b.keys())[list(b.values()).index(node)]


def solve(y):
    x = y
    while x.getPred():
        display(x.getId())
        print('Computer Chooses Option ' + str(x.getWeight(x.getPred())) + ':')
        x = x.getPred()
    display(x.getId())


def connect(b, node):
    l = []
    for n in node.connectedTo:
        item = n.getId()
        l.append(get_node_num(b, item))
    return l


def main():
    # Creates nums and boards in dictionary - num: binary rep
    boards = {}
    stringy = ''
    for i in range(512):
        nums = list(bin(i))
        nums.pop(0)
        nums.pop(0)
        for n in nums:
            stringy += n
        biny = stringy.rjust(9, '0')
        boards[i] = biny
        stringy = ''
    node_num = 0
    current_node = boards[node_num]

    # creates graph of boards
    coin_graph = Graph()
    for a in boards.values():
        for b in boards.values():
            for c in range(1, 10):
                if coin_flip(c, a) == b:
                    coin_graph.addEdge(a, b, c)
    bfs(coin_graph, coin_graph.getVertex('111111111'))

    print('''\nWelcome to Flipper!  

You begin with nine coins, showing "heads", arranged in a 3x3 grid:

HHH    123
HHH    456  <= Coin Choice Options 1-9
HHH    789

Choose a coin to flip it over, along with those vertically and 
horizontally adjacent.

The object of the game is to end up with all coins showing "tails".

If you are stuck, choose Option 0 to show the solution.  :)''')

    display(current_node)
    print('''Option 0: Solve; Options 1-9: Choose Node
Node %d (%s)
Node %d connectedTo: %s\n''' % (node_num, current_node, node_num, connect(boards, coin_graph.getVertex(current_node))))

    # allows user to flip coins and flips them until the goal is reached or user asks for solve
    while current_node != '111111111':
        flip_choice = int(input('Choose Option 0-9: '))
        if flip_choice != 0:
            current_node = coin_flip(flip_choice, current_node)
            node_num = get_node_num(boards, current_node)

            display(current_node)
            print('''Option 0: Solve; Options 1-9: Choose Node
Node %d (%s)
Node %d connectedTo: %s\n''' % (node_num, current_node, node_num, connect(boards, coin_graph.getVertex(current_node))))

        else:
            solve(coin_graph.getVertex(current_node))
            break

    print('Success! :)')


main()

