import sys
import copy

sys.argv

if len(sys.argv) != 2:
    print("ERROR: provide a file name")
    exit()

f = open(sys.argv[1])
n_and_L = f.readline().split()
weights = f.readline().split()
values = f.readline().split()
f.close()

n = int(n_and_L[0])
L = int(n_and_L[1])

class KnapSack:
    def __init__(self, max_weight):
        self.max_weight = max_weight
        self.items = []
        self.itemsIndex = []

    def get_current_value(self):
        current_value = 0
        for item in self.items:
            current_value += item.get_value()
        return current_value

    def get_max_weight(self):
        return self.max_weight

    def get_items(self):
        return self.items

    def get_current_weight(self):
        current_weight = 0
        for item in self.items:
            current_weight += item.get_weight()
        return current_weight

    def get_itemIndexes(self):
        return self.itemsIndex

    def add_item(self, item):
        self.items.append(item)

    def add_itemIndex(self, int):
        self.itemsIndex.append(int)

    def clear_itemsIndex(self):
        self.itemsIndex = []

    def remove_all_items(self):
        self.items = []

class Item:
    def __init__(self, number, weight, value):
        self.weight = int(weight)
        self.value = int(value)
        self.number = int(number)

    def get_weight(self):
        return self.weight

    def get_value(self):
        return self.value

    def get_number(self):
        return self.number

if len(weights) != len(values):
    print("ERROR: check data for weigths and values, lengths of given data do not match!")
if len(weights) == len(values):
    i = 0
    itemsList = []
    w = 0
    v = 0
    item = Item(0,w,v)
    itemsList.append(item)
    while i < len(weights):
        w = int(weights[i])
        v = int(values[i])
        item = Item((i+1),w,v)
        itemsList.append(item)
        i = i + 1

knapsack = KnapSack(L)
W = knapsack.get_max_weight()
n = len(itemsList)

def gen_table(n, W):
    V = {}
    W = W+1

    for i in range(0, n):
        for j in range(0, W):
            if i == 0 or j == 0:
                V[i,j] = 0
            else:
                item = itemsList[i]
                w_i = item.get_weight()
                v_i = item.get_value()

                if j - w_i >= 0:
                    #feasible
                    if V[((i-1), j)] > V[((i-1), (j-w_i))]:
                        V[(i,j)] = V[((i-1), j)]

                    if V[((i-1), j)] <= V[((i-1), (j-w_i))] + v_i:
                        V[(i,j)] = V[((i-1), (j-w_i))] + v_i

                else:
                    #not feasible
                    V[(i,j)] = V[((i-1), (j))]

    return V

def print_table(n, W, V):
    print("----------------------------------------------------------------------------")
    W = W + 1
    res2 = "i\j| "
    for j in range(0,W):
        res2 = res2 + str(j) + "      | "

    print(res2)
    #print("----------------------------------------------------------------------------")
    for i in range(0, n):
        res1 = str(i)
        for j in range(0,W):
            value = V[i,j]
            string = str(value)
            if len(string) == 1:
                res1 = res1 + "  | " + str(value) + "    "
            elif len(string) == 2:
                res1 = res1 + "  | " + str(value) + "   "
            elif len(string) == 3:
                res1 = res1 + "  | " + str(value) + "  "
            elif len(string) == 4:
                res1 = res1 + "  | " + str(value) + " "
            else:
                res1 = res1 + "  | " + str(value) + ""
            #print(i, ", ", j, "   ", value)
        res1 = res1 + "  |"
        print(res1)
    #    print("----------------------------------------------------------------------------")
        #print("_______________________________________")

V = gen_table(n,W)
print_table(n,W,V)

def decode_table(n,W,V):
    n = n-1
    final_items = []
    total_value = V[n,W]
    while n != 0:
        final_result = V[n,W]
        above_value = V[n-1,W]
        if above_value != final_result:
            the_item = itemsList[n]
            final_items.append(the_item)
            the_items_w = the_item.get_weight()
            W = W - the_items_w
            n = n-1
        if above_value == final_result:
            #the_item = itemsList[n]
            #final_items.append(the_item)
            #the_items_w = the_item.get_weight()
            #W = W = the_items_w
            n = n-1

    return (total_value , final_items)

results = decode_table(n,W,V)
print("")
print("RESULTS:")
print("-------------------------------------------------")
print("The optimal value of the KnapSack is: $", results[0])
print("")


final_items = results[1]
#str_of_final_items = ""
tot_weight = 0
for i in range (0,len(final_items)):
    item = final_items[i]
    weight = item.get_weight()
    tot_weight = tot_weight + weight
    value = item.get_value()
    number = item.get_number()
    print("Item: ", number,"   value: $", value, "     weight: ", weight, "lbs")

print("-------------------------------------------------")
print("Total weight:                 ", tot_weight)
