#Individual Node object
class Node(object):
    def __init__(self, name , parent = None ):
        if(parent ==  None):
            self.name = "Root"
        else:
            self.name = name
        self.parent = parent
        self.children  = []

    def getChildren(self):
        return self.children
    
    def addChildren(self , child):
        self.children.append(child)


#Collection of all Nodes in the System
class Graph(object):
    def __init__(self):
        self.nodes = []
        
    def addNode(self, node):
        self.nodes.append(node)

    def getNode(self, nodeName):
        for node in self.nodes:
            if(node.name == nodeName):
                return node
            
        return "Not Found"
