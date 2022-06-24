import sys
import math

import heapq

if len(sys.argv) != 2:
    print("ERROR: provide a file name")
    exit()

f = open(sys.argv[1])
lines = f.readlines()
test_str = ''
for i in range(0, len(lines)):
    char = lines[i]
    test_str = test_str + char

all_freq = {}
for i in test_str:
    if i in all_freq:
        all_freq[i] += 1
    else:
        all_freq[i] = 1

#print(all_freq)



class Node:
    def __init__(self ,data, left, right):
        self.left = left
        self.right = right
        self.data = data
        self.freq = freq
    def children(self):
        return((self.left, self.right))
    def __gt__(self, other):
        return self.freq > other.freq
    def __lt__(self, other):
        return self.freq < other.freq
    def __eq__(self, other):
        if(other == None):
            return False
        if(not isinstance(other, Node)):
            return False
        return self.freq == other.freq

keysList = []
for key in all_freq.keys():
    keysList.append(key)

for i in keysList:
    if i in all_freq:
        all_freq[i] = (all_freq[i]/len(test_str))*100
        all_freq[i] = round(all_freq[i], 4)
        #print(all_freq[i])

#print(all_freq)

h = []
for i in range(0, len(keysList)):
    symbol = keysList[i]
    freq = all_freq[symbol]
    #freq = freq/(len(test_str))
    #print(freq)
    Tx = Node(symbol, None, None)
    Tx.data = freq
    heapq.heappush(h, (freq, Tx, symbol))

while len(h) > 1:
    Tl = heapq.heappop(h)
    #print(Tl)
    #print(Tl[1].children())
    Tr = heapq.heappop(h)
    #print(Tr)
    #print(Tr[1].children())
    wtTl = Tl[0]
    wtTr = Tr[0]
    wtTp = wtTl + wtTr
    Tp = Node(None, Tl, Tr)
    #Tp.left(Tl)
    #Tp.right(Tr)
    #if(wtTl > wtTr):
    #    Tp = Node(None, Tl, Tr)
    #else:
    #    Tp = Node(None, Tr, Tl)
    heapq.heappush(h, (wtTp, Tp))
node = heapq.heappop(h)

def recTree(node, path = "", code = {}):
    children = node[1].children()
    #print("CCCCCCCCC")
    #print(node)
    #print("CCCCCCCC")
    LC = children[0]
    #print("AAAAAAAA")
    #print(LC)
    #print("AAAAAAAA")
    RC = children[1]
    #print("BBBBBBB")
    #print(RC)
    #print("BBBBBBB")
    #print(path)
    if len(LC) == 2 and len(RC) == 2:
        tempPath = path
        path = path + "0"
    #    print(path)
        recTree(LC, path, code)
        path = tempPath
        path = path + "1"
    #    print(path)
        recTree(RC, path, code)
    if len(LC) == 3 and len(RC) == 3:
        tempPath = path
        path = path + "0"
    #    print(path)
        letter = LC[2]
    #    print(letter)
        code[letter] = path
        path = tempPath
        path = path + "1"
    #    print(path)
        letter = RC[2]
        code[letter] = path
    if len(LC) == 3 and len(RC) == 2:
        tempPath = path
        path = path + "0"
    #    print(path)
        letter = LC[2]
    #    print(letter)
        code[letter] = path
        path = tempPath
        path = path + "1"
    #    print(path)
        recTree(RC, path, code)
    if len(LC) == 2 and len(RC) == 3:
        tempPath = path
        path = path + "1"
    #    print(path)
        letter = RC[2]
    #    print(letter)
        code[letter] = path
        path = tempPath
        path = path + "0"
    #    print(path)
        recTree(LC, path, code)
    return code

code = recTree(node)

avgCodeLen = 0
#print(keysList)
keysList2 = []

def custom_sort(str):
    return len(str), str.lower()

for k in sorted(keysList, key=custom_sort):
    keysList2.append(k)
#keysList2 = keysList.sort()
#print(keysList2)
keysList = keysList2
for i in range(0,len(keysList)):
    print(str(keysList[i]) + "  " + str(code[keysList[i]])  + "  " + str(all_freq[keysList[i]]) + "%")
    codeLen = len(code[keysList[i]])
    freqCode = ((all_freq[keysList[i]]))
    avgCodeLen = avgCodeLen + (codeLen * freqCode)

avgCodeLen = avgCodeLen/100
bitsOfOriginalFile = len(test_str) * 8
bitsOfNewFile = len(test_str) * avgCodeLen
bitsOfNewFile = round(bitsOfNewFile)
compRatio = (bitsOfNewFile/bitsOfOriginalFile)*100

print("Average codeword length: " + str(avgCodeLen) + " bits")
print("Original size (bits): " + str(bitsOfOriginalFile))
print("Encoding size (bits): " + str(bitsOfNewFile))
print("Compression ratio: " + str(compRatio) + "%")
print("Compression ratio calulated by Encoding size/Original size)*100")
