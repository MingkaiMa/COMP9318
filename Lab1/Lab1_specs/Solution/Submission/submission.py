## import modules here 

################# Question 0 #################

def add(a, b): # do not change the heading of the function
    return a + b


################# Question 1 #################

def nsqrt(x): # do not change the heading of the function
    n = x
    if n < 0:
        return None

    if n == 0 or n == 1:
        return n

    if n == 2 or n == 3:
        return 1

    left = 1
    right = n // 2

    result = None
    while (left <= right):
        middle = (left + right) // 2

        sqMiddle = middle * middle

        if sqMiddle == n:
            return middle

        if sqMiddle < n:
            result = middle

            left = middle + 1

        else:
            right = middle - 1

    return result



################# Question 2 #################


# x_0: initial guess
# EPSILON: stop when abs(x - x_new) < EPSILON
# MAX_ITER: maximum number of iterations

## NOTE: you must use the default values of the above parameters, do not change them

def find_root(f, fprime, x_0=1.0, EPSILON = 1E-7, MAX_ITER = 1000): # do not change the heading of the function
    for i in range(MAX_ITER):
        ff = f(x_0)
        fp = fprime(x_0)

        x_new = x_0 - ff / fp

        if(abs(x_new - x_0) < EPSILON):
            return x_new

        x_0 = x_new


    return x_new


################# Question 3 #################

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

def make_tree(tokens): # do not change the heading of the function

    stack1 = []
    stack2 = []

    if (len(tokens) == 1):
        return Tree(tokens[0])

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

def max_depth(root): # do not change the heading of the function
    if len(root.children) == 0:
        return 1

    L = []

    for child in root.children:
        L.append(1 + max_depth(child))

    return max(L)
