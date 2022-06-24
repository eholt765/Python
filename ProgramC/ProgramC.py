import sys
import math
import copy


if len(sys.argv) != 2:
    print("ERROR: provide a file name")
    exit()


f = open(sys.argv[1])
mystring = f.readline()
f.close()

print(mystring)
#mystring = "BBABCBCAB"
n = len(mystring)

def gen_table(string):
    D = {}
    n = len(string)
    for i in range(0,n):
        for j in range(0,n):
            D[i,j] = 0

    for i in range(n):
        D[i,i] = 1


#    n = 9
#    print("")
#    for d in range(2, n+1):
#        print("____________")
#        for i in range(0, n-d+1):
#            j = d + i -1
#            print(str(d), "," ,str(i), "," ,str(j))
    for current_lenght in range(2, n+1):
#        print("-------------")
        #print(str(cl))
#        print("____________")
        for i in range(0, n - current_lenght + 1):
            j = i + current_lenght - 1
#            print(str(string[i]), ",  ", str(string[j]), str(i), ", ", str(j))
#            print("")
            if string[i] == string[j] and current_lenght == 2:
                D[i,j] = 2
            elif string[i] == string[j]:
                D[i,j] = D[i+1, j-1] + 2
            else:
                D[i, j] = max(D[i, j-1], D[i+1, j])


    return (D)




#for i in range(0,n):
#    print(seq[i])

def print_table(n, W, V, string):
    print("----------------------------------------------------------------------------")
    list_lets = []#W = W + 1
    res2 = "i\j  |"
    for j in range(0,W):
    #    print(j)

        letter = string[j]
        list_lets.append(letter)
        res2 = res2 + str(letter) + "("+str(j)+")"  + "|"

    print(res2)
    #print("----------------------------------------------------------------------------")
    for i in range(0,n):
        #print(string[i])
        letter2 = list_lets[i]
        res1 = str(letter2) + "("+str(i)+")"
        for j in range(0,W):
            #x = 5
            value = V[i,j]
            string = str(value)
            res1 = res1 + " | " + str(value)  + " "
            #if len(string) == 1:
            #    res1 = res1 + "  | " + str(value) + "    "
            #elif len(string) == 2:
            #    res1 = res1 + "  | " + str(value) + "   "
            #elif len(string) == 3:
            #    res1 = res1 + "  | " + str(value) + "  "
            #elif len(string) == 4:
            #    res1 = res1 + "  | " + str(value) + " "
            #else:
            #    res1 = res1 + "  | " + str(value) + ""
            #print(i, ", ", j, "   ", value)
        res1 = res1 + " |"
        print(res1)
        #print("----------------------------------------------------------------------------")

table = gen_table(mystring)
#table_vals = table[0]
#table_let = table[1]
#print_table(n, n, table, seq)
#print("")



#print_table(n, n, table, mystring)




#print(table)


def read_table(V,n,string):
    list_front = []
    list_rear = []
    i = 0
    start_point = V[i,n]
    while start_point != 0:# and i < len(seq):
        #i = i + 1
        lower_point = V[i+1,n]
        left_point = V[i,n-1]
        adj_point = V[i+1, n-1]
        if left_point == lower_point == adj_point: #and left_point != 0 and lower_point != 0:
#            print("Ture")
            if left_point != start_point:
                if i != n:
                    list_front.append(string[i])
                    list_rear.append(string[n])
#                    print("added", str(i))
#                    print("added", str(n))
                if i == n:
                    list_front.append(string[i])
#                    print("added", str(i))
                n = n-1
                i = i+1
                start_point = adj_point

            elif left_point == start_point:
                n = n-1
                i = i+1
#                print(str(i)," , ", str(n))
                start_point = adj_point
        elif adj_point == 0:
#            print("adj accent point is 0")
            if string[i+1] == string[n-1]:
                list_front.append(string[i+1])
                list_rear.append(string[n-1])
            else:
                list_front.append(string[i+1])
            start_point = 0
        elif lower_point == start_point-1 and left_point == start_point-2:
            list_front.append(string[i])
            list_rear.append(string[n])
#            print("added", str(i))
#            print("added", str(n))
            n = n-1
            i = i+1
            start_point = adj_point
        else:
            if left_point > lower_point:
                n = n-1
            elif left_point <= lower_point:
                i = i +1

    return (list_front, list_rear)

n = n-1
#print("N is : ", n)
lists = read_table(table, n, mystring)
front_list = lists[0]
rear_list = lists[1]
#print(front_list)
#print(rear_list)
longest_pal = ""
for i in range(0,len(front_list)):
    letter = front_list[i]
    longest_pal = longest_pal + letter

for i in range(len(rear_list)-1,-1,-1):
    letter = rear_list[i]
    longest_pal = longest_pal + letter

print("")
rev_longest_pal = longest_pal[::-1]
if longest_pal == rev_longest_pal:
    print("The longest palindrome is:", longest_pal, "which is of length,", table[0,n])
    if table[0,n] != len(longest_pal):
        print("ERROR: length from table is", str(table[0,n]), "but length of palindrome is", str(len(longest_pal)))

else:
    print("There was an error:", longest_pal, "is not a palindrome!!!")
