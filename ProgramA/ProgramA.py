import sys
import math
import copy


if len(sys.argv) != 2:
    print("ERROR: provide a file name")
    exit()


class Node:
    def __init__(self, data, freq, number = None, left = None, right = None, parent = None):
        self.number = number
        self.data = data
        self.freq = freq
        self.left = left
        self.right = right
        self.parent = parent

    def get_number(self):
        return(self.number)
    def get_children(self):
        return((self.left, self.right))
    def get_parent(self):
        return(self.parent)
    def get_freq(self):
        return(self.freq)
    def get_data(self):
        return(self.data)

    def set_parent(self, node):
        self.parent = node
    def set_right(self, node):
        self.right = node
    def set_left(self, node):
        self.left = node
    def set_number(self, numb):
        self.number
    def set_data(self, data):
        self.data
    def set_freq(self, freq):
        self.freq

list_all_nodes = []
lines = open(sys.argv[1], 'r').readlines()
n = int(lines[0].strip())
#k = 1
for line in lines[1:]:
    tokens = (line.split(" "))
    if len(tokens) == 2:
        data = (tokens[0])
        freq = float(tokens[1])
        new_Node = Node(data,freq, 0,None, None, None)
#        k = k+1
        list_all_nodes.append(new_Node)

def custom_sort(node):
    return node.get_data()

sorted_nodes = sorted(list_all_nodes, key = custom_sort)

numbered_inorder_nodes = []
for i in range(0, len(sorted_nodes)):
    node = sorted_nodes[i]
    data = node.get_data()
    freq = node.get_freq()
    node_num = i+1
    new_Node = Node(data,freq, node_num,None, None, None)
    numbered_inorder_nodes.append(new_Node)

#for node in numbered_inorder_nodes:
#    print(node.get_data(), "   ", node.get_number())

rows = n + 1
columns = n +1
n = n + 1
def gen_table(n, c, list):

    C = {}
    R = {}
#    print("r is: ", r)
#    print("c is: ", c)
    #initalization
    for j in range(0,c):
        C[n,j] = 0
        R[n,j] = 0


    for i in range(0,n):
        for j in range(0,n):
            C[i,j] = 0
            R[i,j] = 0

    for i in range(1, n):
        C[i,i-1] = 0
        C[i,i] = list[i-1].get_freq()
        R[i,i] = i
    C[n+1, n] = 0

    for d in range(1, n-1):
#        print("____________")
        for i in range(1, n-d):
            j = d + i
            min = 1000000000        #1,000,000,000
            sum = 0
            for l in range(i, j+1):
#                print(i, ", ", j ,"--->", l)
                q = C[i, (l-1)] + C[(l+1), j]
                node = list[l-1]
                prob_or_node = node.get_freq()
                sum = sum + prob_or_node
                if q <= min:
                    min = q
                    R[i,j] = l
            total = min + sum
#            print(total)
            C[i,j] = min + sum

    return (R, C)


def print_table(r, c, D):
    r = r+1
    res2 = "i\j|  "
    for j in range(0,c):
        res2 = res2  + str(j) + "      |  "
    print(res2)
    print("----------------------------------------------------------------")
    for i in range(1, r):
        res1 = str(i)
        #print(i)
        for j in range(0,c):
            if i == r:
                value = 0
            else:
                value = D[i,j]
            value = round(value, 4)
            string = str(value)
            if len(string) == 1:
                res1 = (res1 + "  |  " + string + "    ")
            elif len(string) == 2:
                res1 = (res1 + "  |  " + string + "   ")
            elif len(string) == 3:
                res1 = (res1 + "  |  " + string + "  ")
            elif len(string) == 4:
                res1 = (res1 + "  |  " + string + " ")
            elif len(string) == 5:
                res1 = (res1 + "  |  " + string + "")
            else:
                res1 = (res1 + "  |  " + string + "")
        res1 = res1 + "  |"
        print(res1)
    #    print("----------------------------------------------------------------")


tables = gen_table(n, columns, numbered_inorder_nodes)
root_table = tables[0]
prob_table = tables[1]

print("THE ROOT TABLE IS: ")
print("----------------------------------------------------------------")
print_table(rows, columns, root_table)

print("")
print("")

print("THE PROBABILITY TABLE IS: ")
print("----------------------------------------------------------------")
print_table(rows, columns, prob_table)


n = n - 1


def build_tree(numbered_inorder_nodes, root_table, n):
    root_number = root_table[1,n]
    root = numbered_inorder_nodes[root_number-1]
    #root = ProsNode(None, None, None, None, None)
    stack = []
    final_nodes = []
    stack.append((root, 1, n))
    while len(stack) != 0:
        (u, i, j) = stack.pop()
        l = root_table[i, j]
        u = numbered_inorder_nodes[l-1]
        #data = match_node.get_data()
        #freq = match_node.get_freq()
        #u.set_data(data)
        #u.set_freq(freq)
        final_nodes.append(u)
        if(l < j):
            r_root = root_table[l+1,j]
            right_child = numbered_inorder_nodes[r_root-1]
            right_child.set_parent(u)
            u.set_right(right_child)
            stack.append((right_child, l+1, j))
        if(i < l):
            l_root = root_table[i,l-1]
            left_child = numbered_inorder_nodes[l_root-1]
            left_child.set_parent(u)
            u.set_left(left_child)
            stack.append((left_child, i, l-1))
            #V = Node(0, 0, None, None, None, u)
        #    u.set_left(V)
        #    stack.append(i, l-1)
    return final_nodes


final_list = build_tree(numbered_inorder_nodes, root_table, n)
#print(final_root.get_children())

def print_nodes(list):
    print("----------------------------------")
    for i in range(0,len(list)):
        print("NODE")
        node = list[i]
        prob = node.get_freq()
        key = node.get_data()
        parent = node.get_parent()
        if parent != None:
            parent_data = parent.get_data()
        else:
            parent_data = None
        children = node.get_children()
        R_child = children[1]
        L_child = children[0]
        if R_child != None:
            right = R_child.get_data()
        else:
            right = None
        if L_child != None:
            left = L_child.get_data()
        else:
            left = None
        print("     Key:         ", key)
        print("     Probability: ", prob*100, "%")
        print("     Parent:      ", parent_data)
        print("     Left Child:  ", left)
        print("     Right Child: ", right)
        print("----------------------------------")

print("")
print("")

print_nodes(final_list)
