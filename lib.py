import numpy as np
import operator
import math
import lib.tempclass 


#BUBLSORT
def bubblsort(nlist):
    for passnum in range(len(nlist)-1,0,-1):
        for i in range(passnum):
            if nlist[i]>nlist[i+1]:
                temp = nlist[i]
                nlist[i] = nlist[i+1]
                nlist[i+1] = temp
    return nlist

#SHELLSORT
def shellsort(alist):
    sublistcount = len(alist)//2
    while sublistcount > 0:
        for start_position in range(sublistcount):
            gap_InsertionSort(alist, start_position, sublistcount)

        sublistcount = sublistcount // 2
    return alist

def gap_InsertionSort(nlist,start,gap):
    for i in range(start+gap,len(nlist),gap):

        current_value = nlist[i]
        position = i

        while position>=gap and nlist[position-gap]>current_value:
            nlist[position]=nlist[position-gap]
            position = position-gap

        nlist[position]=current_value

#QUICKSORT
def quicksort(array):
       if len(array) <= 1:
           return array
       else:
           q = array[len(array) // 2]
       l_nums = [n for n in array if n < q]
       e_nums = [q] * array.count(q)
       b_nums = [n for n in array if n > q]
       return quicksort(l_nums) + e_nums + quicksort(b_nums)

#MERGESORT
def mergesort(L, compare=operator.lt):
    if len(L) < 2:
        return L
    else:
        middle = int(len(L) / 2)
        left = mergesort(L[:middle], compare)
        right = mergesort(L[middle:], compare)
        return merge(left, right, compare)

def merge(left, right, compare):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if compare(left[i], right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result

#HEAPSORT
def heapify(arr, n, i):
    largest = i 
    l = 2 * i + 1   
    r = 2 * i + 2   
    if l < n and arr[i] < arr[l]:
        largest = l
    if r < n and arr[largest] < arr[r]:
        largest = r
    if largest != i:
        arr[i],arr[largest] = arr[largest],arr[i] 
        heapify(arr, n, largest)

def heapsort(arr):
    n = len(arr)
    for i in range(n, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i] 
        heapify(arr, i, 0)
    return arr


#RADIXSORT
def radixsort(nums):
    RADIX = 10
    placement = 1
    max_digit = max(nums)

    while placement < max_digit:
        buckets = [list() for _ in range( RADIX )]
        for i in nums:
            tmp = int((i / placement) % RADIX)
            buckets[tmp].append(i)
        a = 0
        for b in range( RADIX ):
            buck = buckets[b]
        for i in buck:
            nums[a] = i
            a += 1
        placement *= RADIX
    return nums


def Sradixsort(array):
    maxLen = -1
    for string in array: 
        strLen = len(string)
        if strLen > maxLen:
            maxLen = strLen
    oa = ord('A') - 1;
    oz = ord('z') - 1;
    n = oz - oa + 2; 
    buckets = [[] for i in range(0, n)] 
    for position in reversed(range(0, maxLen)):
        for string in array:
            index = 0 
            if position < len(string):
                index = ord(string[position]) - oa
            buckets[index].append(string) 
        del array[:]
        for bucket in buckets: 
            array.extend(bucket)
            del bucket[:]
    return array


def countSortDay(arr, n):
    output = [None] * n
    count = np.zeros(31, dtype=int)
    for i in range(0, n):
        count[arr[i].DD - 1] += 1
    for i in range(1, 31):
        count[i] += count[i - 1]
    for i in range(n - 1, -1, -1):
        output[count[arr[i].DD - 1] - 1] = arr[i]
        count[arr[i].DD - 1] -= 1
    for i in range(0, n):
        arr[i] = output[i]


def countSortMonth(arr, n):
    output = [None] * n
    count = np.zeros(12, dtype=int)
    for i in range(0, n):
        count[arr[i].MM - 1] += 1
    for i in range(1, 12):
        count[i] += count[i - 1]
    for i in range(n - 1, -1, -1):
        output[count[arr[i].MM - 1] - 1] = arr[i]
        count[arr[i].MM - 1] -= 1
    for i in range(0, n):
        arr[i] = output[i]


def countSortYear(arr, n):
    output = [None] * n
    count = np.zeros(1000, dtype=int)
    for i in range(0, n):
        count[arr[i].YYYY - 2000] += 1
    for i in range(1, 1000):
        count[i] += count[i - 1]
    for i in range(n - 1, -1, -1):
        output[count[arr[i].YYYY - 2000] - 1] = arr[i]
        count[arr[i].YYYY - 2000] -= 1
    for i in range(0, n):
        arr[i] = output[i]


def Dradixsort(arr):
    n = len(arr)
    countSortDay(arr, n)
    countSortMonth(arr, n)
    countSortYear(arr, n)
    return arr

#TIMSORT
minrun = 32

def InsSort(arr,start,end):    
    for i in range(start+1,end+1):
        elem = arr[i]
        j = i-1
        while j>=start and elem<arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = elem
    return arr

def merge(arr,start,mid,end):
    if mid==end:
        return arr
    first = arr[start:mid+1]
    last = arr[mid+1:end+1]
    len1 = mid-start+1
    len2 = end-mid
    ind1 = 0
    ind2 = 0
    ind  = start
     
    while ind1<len1 and ind2<len2:
        if first[ind1]<last[ind2]:
            arr[ind] = first[ind1]
            ind1 += 1
        else:
            arr[ind] = last[ind2]
            ind2 += 1
        ind += 1
     
    while ind1<len1:
        arr[ind] = first[ind1]
        ind1 += 1
        ind += 1
              
    while ind2<len2:
        arr[ind] = last[ind2]
        ind2 += 1
        ind += 1   
              
    return arr
            

def timsort(arr):
    n = len(arr)
    
    for start in range(0,n,minrun):
        end = min(start+minrun-1,n-1)
        arr = InsSort(arr,start,end)
        
    curr_size = minrun
    while curr_size<n:    
        for start in range(0,n,curr_size*2):
            mid = min(n-1,start+curr_size-1)
            end = min(n-1,mid+curr_size)
            arr = merge(arr,start,mid,end)
        curr_size *= 2
    return arr


#BUCKETSORT
def bucketsort(alist):
    largest = max(alist)
    length = len(alist)
    size = largest/length
 
    buckets = [[] for _ in range(length)]
    for i in range(length):
        j = int(alist[i]/size)
        if j != length:
            buckets[j].append(alist[i])
        else:
            buckets[length - 1].append(alist[i])
 
    for i in range(length):
        insertion_sort(buckets[i])
 
    result = []
    for i in range(length):
        result = result + buckets[i]
 
    return result
 
def insertion_sort(alist):
    for i in range(1, len(alist)):
        temp = alist[i]
        j = i - 1
        while (j >= 0 and temp < alist[j]):
            alist[j + 1] = alist[j]
            j = j - 1
        alist[j + 1] = temp

#COUNTING SORT
def countingsort(array1):
    
    m = max(array1) + 1
    count = [0] * m                
    
    for a in array1:
    # count occurences
        count[a] += 1             
    i = 0
    for a in range(m):            
        for c in range(count[a]):  
            array1[i] = a
            i += 1
    return array1
