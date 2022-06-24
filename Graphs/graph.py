import sys
import math
import networkx as nx
import copy

if len(sys.argv) != 2:
    print("ERROR: provide a file name")
    exit()

g = nx.Graph()

lines = open(sys.argv[1], 'r').readlines()
n = int(lines[0].strip())
g.add_nodes_from(range(n), num = ' ', dt = ' ' , ft = ' ', color = ' ')
for line in lines[1:]:
    tokens = (line.split(" "))
    if len(tokens) == 3:
        node1 = int(tokens[0])
        node2 = int(tokens[1])
        g.add_edge(node1, node2, weight = float(tokens[2]))

g.to_undirected()


#print(g.edges)
#print(g.nodes)

def break_detection(V,E):
    sol = 0
    ng = nx.Graph()
    ng.add_nodes_from(V)
    ng.add_edges_from(E)
    ng.to_undirected()
    processes_list = []

    V = ng.nodes
    for p in V:
        ng.nodes[p]['color'] = 'white'
        ng.nodes[p]['num'] = p
    stack = []
    stack.append(V[0])

    nodes_in_edges = []
    for edge in E:
        e = edge
        (u,v,w) = e
        nodes_in_edges.append(u)
        nodes_in_edges.append(v)

    nodes_in_edges = set(nodes_in_edges)
    nodes_in_edges = list(nodes_in_edges)

    while len(stack) != 0:
        x = stack.pop()
        val = x['num']
        neighbors = list(ng.adj[val])

        k = 0
        while k != len(neighbors):
            y = neighbors[k]
            current_color = V[y]['color']
            if current_color == "white":
                stack.append(V[y])
                k = k+1
            else:
                k = k+1

        processes_list.append(val)
        x['color'] = 'black'
        temp_processes_list = set(processes_list)
        temp_processes_list = list(temp_processes_list)
        if len(temp_processes_list) != len(nodes_in_edges) and len(stack) == 0:
            t = 0
            while t < len(nodes_in_edges):
                a = nodes_in_edges[t]
                check_missing = temp_processes_list.count(a)
                if check_missing == 0:
                    t = len(nodes_in_edges)
                    stack.append(V[a])
                else:
                    t = t + 1

    processes_set = set(processes_list)
    #print(processes_set)
    #print(processes_list)
    if len(processes_list) != len(processes_set):
        sol = 1 #cycle was detected
    else:
        sol = -1 #cycle was NOTTTTT detected
    return sol



def DFS_traversal(g):
    V = g.nodes
    for p in V:
        g.nodes[p]['color'] = 'white'
        g.nodes[p]['num'] = p
        g.nodes[p]['dt'] = 1000000000
        g.nodes[p]['ft'] = 1000000000


    counter = 1
    stack = []
    V[0]['dt'] = counter
    V[0]['color'] = 'grey'
    stack.append(V[0])

    while len(stack) != 0:
        counter = counter + 1
        x = stack.pop()
        stack.append(x)
        val = x['num']
        neighbors = list(g.adj[val])
        #sorted(neighbors)
        neighbors = (sorted(neighbors))
        #print(neighbors)

        k = 0
        counter2 = 0
        while k != len(neighbors):
            y = neighbors[k]
            current_color = V[y]['color']
            if current_color == "white":
                V[y]['dt'] = counter
                V[y]['color'] = 'grey'
                stack.append(V[y])
                counter2 = len(neighbors) + 1
                k = len(neighbors)
            else:
                k = k+1

        for i in range(0, len(neighbors)):
            n = neighbors[i]
            color = V[n]['color']
            if color != 'white':
                counter2 = counter2 + 1

        if counter2 == len(neighbors):
            r = stack.pop()
            r['ft'] = counter
            r['color'] = 'black'

def DFS_print(g):
    DFS_traversal(g)
    str = []
    DFS_sorted_nodes = (list(sorted(g.nodes(data = True), key = lambda x:x[1]['dt'])))
    for i in range(0, len(DFS_sorted_nodes)):
        a = DFS_sorted_nodes[i]
        node = (a[0])
        str.append(node)
    #ng =  nx.Graph()
    #ng.add_nodes_from(DFS_sorted_nodes)
    #ng.to_undirected()
    #str = (list(ng.nodes))
    #str = DFS_sorted_nodes
    print("DFS:" , str)
    print("_________________________________")
    print("")

print("_________________________________")
print("")
DFS_print(g)

def BFS_traversal(g):
    V = g.nodes
    for p in V:
        g.nodes[p]['color'] = 'white'
        g.nodes[p]['num'] = p
        g.nodes[p]['dt'] = 1000000000
        g.nodes[p]['ft'] = 1000000000

    counter = 1
    queue = []
    V[0]['dt'] = counter
    V[0]['color'] = 'grey'
    queue.append(V[0])

    while len(queue) != 0:
#        print(queue)
        #counter = counter + 1
        x = queue[0]
        queue.remove(x)
        val = x['num']
#        print("Values is:   " , val)
        neighbors = list(g.adj[val])
#        print("NONE SORTED NEIGHBORS",neighbors)
        neighbor_edges = []
        ng = nx.Graph()
        for i in range (0, len(neighbors)):
            node = neighbors[i]
            val2 = V[node]['num']
            w = g.edges[val,val2]['weight']
            ng.add_edge(val, val2, weight = w)

        weight_sorted_neighbors = []
        weight_sorted_neighbor_edges = (list(sorted(ng.edges(data = True), key = lambda x:x[2]['weight'])))
        #weight_sorted_neighbor_edges.reverse()
        for e in weight_sorted_neighbor_edges:
            (u,v,w) = e
            if u != val:
                weight_sorted_neighbors.append(u)
            if v != val:
                weight_sorted_neighbors.append(v)
        k = 0
    #    print("Current val: ", val)
    #    print(weight_sorted_neighbors)
        while k != len(weight_sorted_neighbors):

            y = weight_sorted_neighbors[k]
            current_color = V[y]['color']
            current_num = V[y]['num']
    #        print("neighbor val: ", current_num)
#            print(current_color)
            if current_color == "white":
                counter = counter + 1
                V[y]['dt'] = counter
                V[y]['color'] = 'grey'
                queue.append(V[y])
                k = k+1
            else:
                k = k+1

        x['ft'] = counter
        x['color'] = 'black'
        t = 0
        #V = sorted(V)
    #    if len(queue) == 0:
    #        print("THE QUEUE IS EMPTY")
        while t < (len(V)) and len(queue) == 0:
            n = V[t]
            dt = (n['dt'])
            if dt == 1000000000:
                counter = counter + 1
                V[t]['dt'] = counter
                queue.append(V[t])
                t = len(V)
            else:
                t = t+ 1


def BFS_print(g):
    BFS_traversal(g)
    str = []
    BFS_sorted_nodes = (list(sorted(g.nodes(data = True), key = lambda x:x[1]['dt'])))
    for i in range(0, len(BFS_sorted_nodes)):
        a = BFS_sorted_nodes[i]
        node = (a[0])
        str.append(node)

        #str = str , " " , node
    #ng =  nx.Graph()
    #ng.add_nodes_from(BFS_sorted_nodes)
    #ng.to_undirected()
    #str = (list(ng.nodes))
    #str = BFS_sorted_nodes
    print("BFS:" , str)
    print("_________________________________")
    print("")

BFS_print(g)


def cycle_detection(V,E):
    sol = 0
    ng = nx.Graph()
    ng.add_nodes_from(V)
    ng.add_edges_from(E)
    ng.to_undirected()
    processes_list = []

    V = ng.nodes
    for p in V:
        ng.nodes[p]['color'] = 'white'
        ng.nodes[p]['num'] = p
    stack = []
    stack.append(V[0])

    nodes_in_edges = []
    for edge in E:
        e = edge
        (u,v,w) = e
        nodes_in_edges.append(u)
        nodes_in_edges.append(v)

    nodes_in_edges = set(nodes_in_edges)
    nodes_in_edges = list(nodes_in_edges)

    while len(stack) != 0:
        x = stack.pop()
        val = x['num']
        neighbors = list(ng.adj[val])

        k = 0
        while k != len(neighbors):
            y = neighbors[k]
            current_color = V[y]['color']
            if current_color == "white":
                stack.append(V[y])
                k = k+1
            else:
                k = k+1

        processes_list.append(val)
        x['color'] = 'black'
        temp_processes_list = set(processes_list)
        temp_processes_list = list(temp_processes_list)
        if len(temp_processes_list) != len(nodes_in_edges) and len(stack) == 0:
            t = 0
            while t < len(nodes_in_edges):
                a = nodes_in_edges[t]
                check_missing = temp_processes_list.count(a)
                if check_missing == 0:
                    t = len(nodes_in_edges)
                    stack.append(V[a])
                else:
                    t = t + 1

    processes_set = set(processes_list)
    #print(processes_set)
    #print(processes_list)
    if len(processes_list) != len(processes_set):
        sol = 1 #cycle was detected
    else:
        sol = -1 #cycle was NOTTTTT detected
    return sol

def MST(g):
    weight_sorted_edges = (list(sorted(g.edges(data = True), key = lambda x:x[2]['weight'])))
    #print(weight_sorted_edges)
    MST_edges = []
    k = 0
    n = g.number_of_nodes()
    while len(MST_edges) < (n-1) and k < len(weight_sorted_edges):
        V = list(g.nodes)
        MST_edges_temp = copy.deepcopy(MST_edges)
        Et = (weight_sorted_edges[k])
        point1 = Et[0]
        point2 = Et[1]
        MST_edges_temp.append((Et))
        #print(MST_edges_temp)
        #print(cycle_detection(V, MST_edges_temp))
        check_val = cycle_detection(V, MST_edges_temp)
        if check_val == -1:
            MST_edges = MST_edges_temp
            k = k + 1
        if check_val == 1:
            MST_edges_temp.remove(Et)
            MST_edges = MST_edges_temp
            k = k +1

    return (V,MST_edges)

def MST_print(MST_edgesA):
    MST_edges = (sorted(MST_edgesA))
    l = len(MST_edges)
    tot_weight = 0
    print("MST:")
    print("")
    for i in range(0, l):
        point1 = MST_edges[i][0]
        point2 = MST_edges[i][1]
        weight = MST_edges[i][2].get('weight')
        tot_weight = tot_weight + weight
        print("(",point1,",",point2,")  Edge Weight: ", weight )
    tot_weight = round(tot_weight, 3)
    print("")
    print("Total Weight: ", tot_weight)
    print("")

MST = MST(g)
MST_edges = ((MST[1]))

MST_print(MST_edges)



def check_for_node(weight_sorted_neighbors, p2):
    index = -1
    for i in range(0,len(weight_sorted_neighbors)):
        t = weight_sorted_neighbors[i]
        if t == p2:
            index = i
            return index
        else:
            index = -1
    return index



def SP(g, p1, p2):
    V = g.nodes
    for p in V:
        g.nodes[p]['color'] = 'white'
        g.nodes[p]['num'] = p
        g.nodes[p]['dt'] = 1000000000     #1,000,000,000
        g.nodes[p]['ft'] = -10000000
    visited = []
    unvisited = list(V)

    queue = []

    V[p1]['dt'] = 0
    num = V[p1]['num']
    V[p1]['ft'] = num
    #queue.append(V[2])
    for p in V:
        queue.append(V[p])

    #print(queue)
    while len(queue) != 0:
        temp_worst_dist = 100000000
        for i in range(0, len(queue)):
            a = queue[i]
            nodeA = (a['num'])
            distA = a['dt']
            colorA = a['color']
            if distA <= temp_worst_dist and colorA == 'white':
                nextNode = nodeA
                temp_worst_dist = distA
        #print("this is the next node: ", nextNode)

        #x = queue[nextNode]
        x = (V[nextNode])
        x['color'] = 'grey'
        val = (x['num'])
        #print("next value is", val)
        #val = x['num']
        #print(queue)
        if queue.count(V[val]) == 0:
            queue = []
        else:
            queue.remove(V[val])
            #print(val)
            copy_value = copy.deepcopy(val)
            #path.append(val)
            neighbors = list(g.adj[val])
            neighbor_edges = []
            ng = nx.Graph()
            for i in range (0, len(neighbors)):
                node = neighbors[i]
                val2 = V[node]['num']
                w = g.edges[val,val2]['weight']
                ng.add_edge(val, val2, weight = w)

            weight_sorted_neighbors = []
            weight_sorted_neighbor_edges = (list(sorted(ng.edges(data = True), key = lambda x:x[2]['weight'])))
            for e in weight_sorted_neighbor_edges:
                (u,v,w) = e
                if u != val:
                    weight_sorted_neighbors.append(u)
                if v != val:
                    weight_sorted_neighbors.append(v)

    #    print(weight_sorted_neighbors)
            for i in range(0,len(weight_sorted_neighbors)):
                index = weight_sorted_neighbors[i]
                y = V[index]
            # get the weight of the edge and x
                weight = x['dt']
                weight_edge = g.edges[val,index]['weight']
    #        print(weight_edge)
                new_weight = weight + weight_edge
                old_weight = y['dt']
                if new_weight <= old_weight:
                    y['dt'] = new_weight
                    y['ft'] = val


def all_combos(g):
    V = list(g.nodes)
    combos = []
    for i in range(0,len(V)-1):
        for j in range(i+1,len(V)):
            a = V[i]
            b = V[j]
            if a != b:
                combos.append([a,b])
    return combos


def SP_path_decoder(g, p1, p2):
    SP(g, p1, p2)
    V = g.nodes
    for p in V:
        g.nodes[p]['color'] = 'white'
    sorted_nodes = (list(sorted(g.nodes(data = True), key = lambda x:x[1]['dt'])))
    stack = []
    nodes = []

    beginning_node = sorted_nodes[0]
    start_node = beginning_node[1]
    dist_start = start_node['dt']
    prev_start = start_node['ft']
    start_value = start_node['num']

    last_node = V[p2]
    dist_last = last_node['dt']
    prev_last = last_node['ft']
    last_value = last_node['num']

    break_loop_val = start_value
    break_value = 1

    if dist_last == 1000000000 or dist_start == 1000000000:
        finalPath = []
        return finalPath

    stack.append(last_node)

    while break_value == 1:
        x = stack.pop()
        dist_curr = x['dt']
        prev_curr = x['ft']
        curr_value = x['num']
        stack.append(x)

        next_node = V[prev_curr]
        break_key = next_node['num']

        stack.append(next_node)

        if break_loop_val == break_key:
            break_value = -1

    finalPath = []
    for i in range(0,len(stack)):
        node = stack[i]
        val = node['num']
        finalPath.append(val)
    finalPath.reverse()
    return finalPath

def gen_all_shortest_path(g):
    combos = all_combos(g)
    E = g.edges
    V = g.nodes
    for i in range (0, len(combos)):
        a = combos[i]
        p1 = int(a[0])
        p2 = int(a[1])
        path = (SP_path_decoder(g, p1, p2))
        print_shortest_path(g, p1, p2, path)

def print_shortest_path(g, p1, p2, path):
    print(p1, "--->>>", p2)
    tot_weight = 0
    if len(path) == 0:
        print("NO PATH EXISTS BETWEEN THE POINTS")
        #print("path weight: ", tot_weight )
        #print("_________________________________")
        #print("")

    for i in range(0,len(path)-1):
        point1 = path[i]
        point2 = path[i+1]
        weight = g.edges[point1,point2].get('weight')
        tot_weight = tot_weight + weight
        print("(",point1,",",point2,")  Edge Weight: ", weight, "--->>>" )
    tot_weight = round(tot_weight, 3)
    print("path weight: ", tot_weight )
    print("_________________________________")
    #print("")

print("Shortest Paths:")
print("_________________________________")

gen_all_shortest_path(g)
