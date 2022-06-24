"""
CSCE 310
Summer 2021

A collection of recursive divide-and-conquer algorithms and functions.

- You must implement the largest(), addAll() and median() methods
- You may not use any library or built-in methods to implement these
- All implementations *must* be recursive/divide-and-conquer
- The defined methods must be used and should be considered "entry
  points" for your own recursive function that you should define

Author: TODO
"""
import copy
import math
import random

"""
Partitions the given array (arr) around a pivot element which is chosen
to be the last element in the array.  Partitioning means that all elements
less than the pivot will appear before the pivot and all elements greater
will appear after but there is no guarantee that the original order will
be preserved.

Once partitioned, the function
returns the index at which the pivot element ends up.

For example, with an input of arr = [8, 4, 1, 9, 3, 5], the pivot
would element would be 5 (the last element) and after partitioning, the
array may look like:
  [4, 1, 3, 5, 8, 9]
and the function will return 3 (the index where 5 ends up)
"""
def partition(arr):
    if len(arr) == 1:
      return 0
    i = -1
    n = len(arr)-1
    pivot = arr[n]

    for j in range(0 , n):
        if arr[j] <= pivot:
          i = i+1
          arr[i],arr[j] = arr[j],arr[i]
    arr[i+1],arr[n] = arr[n],arr[i+1]
    return ( i+1 )

"""
Searches the given array for the provided key, returns
true if the array contains the key.

This function has been done for you as an example.  This
function is the non-recursive "entry point"
"""
def contains( arr, key ):
  # start the search at index 0...
  return containsRecursive(arr, key, 0)
  # alternative:
  #return containsRecursiveDivide(arr, key)

"""
Recursive contains function
"""
def containsRecursive( arr, key, index ):
  if index > len(arr)-1:
    return False
  elif arr[index] == key:
    return True
  else:
    return containsRecursive(arr, key, index+1)

"""
Recursive (divide/conquer) contains function
"""
def containsRecursiveDivide( arr, key ):
  if(len(arr) == 0):
    return False
  elif len(arr) == 1:
    return arr[0] == key
  else:
    m = int(len(arr)/2)
    return containsRecursiveDivide(arr[0:m], key) or containsRecursiveDivide(arr[m:], key)

#res = [random.randrange(1, 90, 1) for i in range(10000)]
#res[376] = 91
def smallestRec(arr, index, val=None):
    if len(arr) == 0:
        return -1
    if index == 0:
        if val == None:
            val = arr[0]
    if index >= len(arr)-1:
        return val
    if len(arr) > 600:
        m = math.floor((len(arr))/2)
        arr2 = arr[0:m]
        arr3 = arr[m:]
        index2 = 0
        index3 = 0
        val2 = smallestRec(arr2, index2)
        val3 = smallestRec(arr3, index3)
        if val2 <= val3:
            val = val2
        else:
            val = val3
    else:
        if arr[index+1] <= val:
            val = arr[index+1]
        return smallestRec(arr, index+1, val)
    return val


"""
Finds and returns the maximum value in the given array
"""
def smallest( arr ):
    if len(arr) >= 0:
        index = 0
        val = smallestRec(arr, index)
    else:
        val = None
    return val


def largestRec(arr, index, val=None):
    if len(arr) == 0:
        return -1
    if index == 0:
        if val == None:
            val = arr[0]
    if index >= len(arr)-1:
        return val
    if len(arr) > 600:
        m = math.floor((len(arr))/2)
        arr2 = arr[0:m]
        arr3 = arr[m:]
        index2 = 0
        index3 = 0
        val2 = largestRec(arr2, index2)
        val3 = largestRec(arr3, index3)
        if val2 >= val3:
            val = val2
        else:
            val = val3
    else:
        if arr[index+1] >= val:
            val = arr[index+1]
        return largestRec(arr, index+1, val)
    return val


"""
Finds and returns the maximum value in the given array
"""
def largest( arr ):
    if len(arr) >= 0:
        index = 0
        val = largestRec(arr, index)
    else:
        val = None
    return val

def addRec(arr, index, total):
    if len(arr) == 1:
        total = total + arr[0]
    if index > len(arr)-1:
        return total
    if len(arr) >= 1000:
        m = math.floor((len(arr))/2)
        arr2 = arr[0:m]
        arr3 = arr[m:]
        index2 = 0
        index3 = 0
        total2 = addRec(arr2, index2, total)
        total3 = addRec(arr3, index3, total)
        total = total2 + total3 + total
        return total
    if index <= len(arr)-2:
        total = arr[index] + arr[index+1] + total
        return addRec(arr, index+2, total)
    if index <= len(arr)-1:
        total = arr[index] + total
        return addRec(arr, index+1, total)
    return total

"""
Computes the sum of all elements in the given array.
"""
def addAll( arr ):
    if len(arr) >= 0:
        index = 0
        totalInit = 0
        Total = addRec(arr, index, totalInit)
    else:
        Total = None
      ## TODO: implement calling your own recursive function
      ## this method is just the entry point to the recursion
    return Total

"""
Computes the median element of the given array, but
does *not* modify the given array.
"""
def medRec(arr, kthElementL, kthElementR):
    if len(arr) == 1:
        midpoint = arr[0]
        return midpoint
    random.shuffle(arr)
    value = partition(arr)
    arr2 = arr[0:value]
    arr3 = arr[value:]
    if kthElementR==0 and (len(arr2) != len(set(arr2)) or len(arr3) != len(set(arr3))):
        m = math.floor((len(arr)/2))
        arr2 = arr[0:m]
        arr3 = arr[m:]
        kthElementR = 1
    if (len(arr2) > len(arr3)):
        kthElementR = kthElementR - len(arr3)
        if kthElementR>=0:
            random.shuffle(arr2)
            return medRec(arr2, kthElementL, kthElementR)
        else:
            kthElementR = len(arr3) + kthElementR
            random.shuffle(arr3)
            return medRec(arr3, kthElementL, kthElementR)
    if (len(arr3) > len(arr2)):
        kthElementL = kthElementL - len(arr2)
        if kthElementL>=0:
            random.shuffle(arr3)
            return medRec(arr3, kthElementL, kthElementR)
        else:
            kthElementL = len(arr2) + kthElementL
            random.shuffle(arr2)
            return medRec(arr2, kthElementL, kthElementR)
    if (len(arr2) == len(arr3)) and len(arr2) != 1:
        kthElementR = kthElementR - len(arr3)
        if kthElementR>=0:
            random.shuffle(arr2)
            return medRec(arr2, kthElementL, kthElementR)
        else:
            kthElementR = len(arr3) + kthElementR
            random.shuffle(arr3)
            return medRec(arr3, kthElementL, kthElementR)
    if len(arr2) == 1 and len(arr3) == 1:
        point2 = arr2[0]
        point3 = arr3[0]
        if point2 >= point3:
            midpoint = point2
            return midpoint
        else:
            midpoint = point3
            return midpoint
    return midpoint

def median( arr ):
    b = copy.deepcopy(arr)
    if len(arr) >= 0:
        m = math.floor((len(arr))/2)
        kthElementL = m
        kthElementR = kthElementL
        #midpoint = -1000000
        median = medRec(arr, kthElementL, kthElementR)
        return median
        #print("The median value is " + str(value))
        #print("The median of the given array is " + str(medpoint))
    else:
        median = None
        return median
    #    medpoint = 0
    return median


arr = [51, 55, 22, 79, 47, 99, 47, 90, 32, 67, 73, 82, 37]
#arr = [50, 43, 70, 78, 14, 61, 32, 70, 11, 24, 80, 5, 99]
#arr = [67, 43, 71, 45, 36, 81, 77, 83, 37, 18, 76, 87, 82, 37, 74]
print(median(arr))
import statistics
print(statistics.median(arr))
