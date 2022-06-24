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
L = float(n_and_L[1])

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
    def __init__(self, weight, value):
        self.weight = float(weight)
        self.value = float(value)

    def get_weight(self):
        return self.weight

    def get_value(self):
        return self.value

if len(weights) != len(values):
    print("ERROR: check data for weigths and values, lengths of given data do not match!")
if len(weights) == len(values):
    i = 0
    itemsList = []
    while i < len(weights):
        w = float(weights[i])
        v = float(values[i])
        item = Item(w,v)
        itemsList.append(item)
        i = i + 1

BestKS = KnapSack(L)

def KnapSacRec(set, subset, j):
    n = len(set)
    if j == n:
        return
    for k in range(j+1, n):
        ks = KnapSack(L)
        TempBestSol = copy.deepcopy(subset)
        subset.append(set[k])
        for i in range(0, len(subset)):
            ks.add_item(itemsList[subset[i]])

        if ks.get_current_weight() <= L:
            KnapSacRec(set, subset, k)
            TempBestSol = copy.deepcopy(subset)

            if ks.get_current_value() > BestKS.get_current_value():
                BestKS.remove_all_items()
                BestKS.clear_itemsIndex()
                TempBestSolB = copy.deepcopy(TempBestSol)
                for t in range(0, len(TempBestSolB)):
                    BestKS.add_item(itemsList[TempBestSolB[t]])
                    BestKS.add_itemIndex(TempBestSolB[t])
                BestSolSet = copy.deepcopy(TempBestSolB)
        subset.pop()
    return BestKS
set = list(range(n))
subset = []
index = -1
KnapSacRec(set, subset, index)
print("For best solution choose items at indexs " + str(BestKS.get_itemIndexes()) + " for a total value of $" + str(BestKS.get_current_value()) + " and a total weight of " + str(BestKS.get_current_weight()) + "lbs")
