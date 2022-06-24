import sys

sys.argv

if len(sys.argv) != 3:
    print("ERROR: provide a file name")
    exit()

f = open(sys.argv[1])
line1 = f.readline()
line2 = f.readline()
line3 = f.readline()
line4 = f.readline()
f.close()

contents = line1.strip() + line2.strip() + line3.strip() + line4.strip()

def generate_board():
    board = []
    for i in range(0,4):
        board.append([])
        for j in range(0,4):
            board[i].append(0)

    board[0][0] = contents[0].strip().lower()
    board[0][1] = contents[1].strip().lower()
    board[0][2] = contents[2].strip().lower()
    board[0][3] = contents[3].strip().lower()
    board[1][0] = contents[4].strip().lower()
    board[1][1] = contents[5].strip().lower()
    board[1][2] = contents[6].strip().lower()
    board[1][3] = contents[7].strip().lower()
    board[2][0] = contents[8].strip().lower()
    board[2][1] = contents[9].strip().lower()
    board[2][2] = contents[10].strip().lower()
    board[2][3] = contents[11].strip().lower()
    board[3][0] = contents[12].strip().lower()
    board[3][1] = contents[13].strip().lower()
    board[3][2] = contents[14].strip().lower()
    board[3][3] = contents[15].strip().lower()
    return board

class Tree_Node():
    def __init__(self, root = None):
        self.root = root
        self.children = {}
        self.leaf = False

class Tree(object):
    def __init__(self, root = None):
        self.root = root
        self.children = {}
        self.leaf = False

    def find(self, root):
        if root not in self.children:
            return None
        return self.children[root]

    def add(self, word):
        if len(word):
            root = word[0]
            word = word[1:]
            if root not in self.children:
                self.children[root] = Tree(root)
            return self.children[root].add(word)
        else:
            self.leaf = True
            return self

def find_words(board, tree, valid_words, row, col, path=None, current_root=None, word=None):
    root = board[row][col]
    if path is None or current_root is None or word is None:
        current_root = tree.find(root)
        path = [(row, col)]
        word = root
        #print(word)
    else:
        current_root = current_root.find(root)
        path.append((row, col))
        word = word + root
        #print(word)
    if current_root is None:
        return
    #else:
    if current_root.leaf:
        valid_words.add(word)
        #print("XXXXXXXX")
    for r in range(row-1, row+2):
        for c in range(col-1, col+2):
            if (r>= 0 and r<4 and c>=0 and c<4 and (r,c) not in path):
                    find_words(board, tree, valid_words, r, c, path[:], current_root, word[:])

dict = open(sys.argv[2], "r")

tree = Tree()
for line in dict:
    word = line.rstrip()
    tree.add(word)

valid_words = set()

board = generate_board()

for row in range(0,4):
    for col in range(0,4):
        find_words(board, tree, valid_words, row, col)

def custom_sort(str):
    return len(str), str.lower()

count_total = 0
count_for_len_3 = 0
count_for_len_4 = 0
count_for_len_5 = 0
count_for_len_6 = 0
count_for_len_7 = 0
count_for_len_8 = 0
count_for_len_9 = 0
count_for_len_10 = 0
count_for_len_11 = 0
count_for_len_12 = 0
count_for_len_13 = 0
count_for_len_14 = 0
count_for_len_15 = 0
count_for_len_16 = 0

for word in sorted(valid_words, key=custom_sort):
    if len(word) == 3:
        count_for_len_3 = count_for_len_3 +1
    if len(word) == 4:
        count_for_len_4 = count_for_len_4 +1
    if len(word) == 5:
        count_for_len_5 = count_for_len_5 +1
    if len(word) == 6:
        count_for_len_6 = count_for_len_6 +1
    if len(word) == 7:
        count_for_len_7 = count_for_len_7 +1
    if len(word) == 8:
        count_for_len_8 = count_for_len_8 +1
    if len(word) == 9:
        count_for_len_9 = count_for_len_9 +1
    if len(word) == 10:
        count_for_len_10 = count_for_len_10 +1
    if len(word) == 11:
        count_for_len_11 = count_for_len_11 +1
    if len(word) == 12:
        count_for_len_12 = count_for_len_12 +1
    if len(word) == 13:
        count_for_len_13 = count_for_len_13 +1
    if len(word) == 14:
        count_for_len_14 = count_for_len_14 +1
    if len(word) == 15:
        count_for_len_15 = count_for_len_15 +1
    if len(word) == 16:
        count_for_len_16 = count_for_len_16 +1

def print_board(board):
    for i in range(0,4):
        for j in range(0,4):
            print(board[i][j], end = " ")
        print()

print_board(board)
print("\n")

for word in sorted(valid_words, key=custom_sort):
    if len(word) > 2:
        count_total = count_total + 1
        print(word)


print("=====================================")
print("Total of " + str(count_for_len_3) + " words of length 3")
print("Total of " + str(count_for_len_4) + " words of length 4")
print("Total of " + str(count_for_len_5) + " words of length 5")
print("Total of " + str(count_for_len_6) + " words of length 6")
print("Total of " + str(count_for_len_7) + " words of length 7")
print("Total of " + str(count_for_len_8) + " words of length 8")
print("Total of " + str(count_for_len_9) + " words of length 9")
print("Total of " + str(count_for_len_10) + " words of length 10")
print("Total of " + str(count_for_len_11) + " words of length 11")
print("Total of " + str(count_for_len_12) + " words of length 12")
print("Total of " + str(count_for_len_13) + " words of length 13")
print("Total of " + str(count_for_len_14) + " words of length 14")
print("Total of " + str(count_for_len_15) + " words of length 15")
print("Total of " + str(count_for_len_16) + " words of length 16")
print("=====================================")
print("A total of " + str(count_total) + " words were found")
