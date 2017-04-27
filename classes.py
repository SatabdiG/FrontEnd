class Node(object):
    def __init__(self, content , left=None, right = None):
        self.content = content
        self.left = left
        self.right =  right

    def __str__(self):
        return str(self.content)