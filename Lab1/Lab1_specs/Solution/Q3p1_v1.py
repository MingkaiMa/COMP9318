class Tree(object):
    def __init__(self, name='ROOT', children=None):
        self.name = name
        self.children = []
        if children is not None:
            for child in children:
                self.add_child(child)
    def __repr__(self):
        return self.name
    def add_child(self, node):
        assert isinstance(node, Tree)
        self.children.append(node)



def make_tree(tokens):

    stack1 = []
    stack2 = []
    
    for i in range(len(tokens)):
        if(tokens[i] == '['):
            stack2.append(i)
            continue

        if(i < len(tokens) - 1 and tokens[i] != '[' and tokens[i] != ']' and tokens[i + 1] != '[' and tokens[i + 1] != ']'):
            stack1.append(Tree(tokens[i]))
            continue

        if(i < len(tokens) - 1 and tokens[i] != '[' and tokens[i] != ']' and tokens[i + 1] == ']'):
            stack1.append(Tree(tokens[i]))
            continue

        if(i < len(tokens) - 1 and tokens[i] != '[' and tokens[i] != ']' and tokens[i + 1] == '['):
            stack1.append(i)
            continue

        if(tokens[i] == ']'):
            nextNodeIndex = stack2.pop() - 1
            toPushNode = Tree(tokens[nextNodeIndex])
            children = []
            while(stack1[-1] != nextNodeIndex):
                children = [stack1.pop()] + children

            stack1.pop()
            toPushNode.children = children
            stack1.append(toPushNode)


    tree = stack1.pop()
    return tree


def print_tree(root, indent=0):
    print(' ' * indent, root)
    if len(root.children) > 0:
        for child in root.children:
            print_tree(child, indent+4)
                
            
def max_depth(root):

    
    if len(root.children) == 0:
        return 1

    L = []

    for child in root.children:
        L.append(1 + max_depth(child))

    return max(L)
        
        
    


    
tokens = ['1', '[', '2', '[', '3', '4', '5', ']', '6', '[', '7', '8', '[', '9', ']', '10', '[', '11', '12', ']', ']', '13', ']']
#tokens = ['1', '[', '2', '3', '[',  '8',']', ']']
tree = make_tree(tokens)
print_tree(tree)
