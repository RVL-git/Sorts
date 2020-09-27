#import lib.lib as func
#import lib.tempclass as cs
#import winsound
#import numpy as np
#from random import choice
#import random
#from string import ascii_letters

#import time
#from datetime import date, timedelta

#import matplotlib.pyplot as plt

##seed == 1: случайный 
##seed == 2: частично упорядоченный
##seed == 3: состоящий из одинаковых элементов



#def partially(data, size):
#    blocksize = size // 4
#    data [:blocksize] = sorted(data [: blocksize])
#    data [blocksize * 3:] = sorted(data [blocksize * 3:])
#    return data

#def genSTR (size, seed):
#    temp =[]
#    if (seed == 3):
#        temp = []
#        for i in range(size//2):
#            temp.append('b')
#        for i in range(size//2, size):
#            temp.append('a')
#        return temp
#    for j in range(size):
#        temp.append(''.join(choice(ascii_letters) for i in range(np.random.randint(1,10))))    
#    temp = partially(temp, size) if seed == 2 else temp
#    return temp

#def genINT(size, short, seed):
#    temp = []
#    if (seed == 3):
#        max = 1 if short else 10000
#        for i in range(size):
#            temp.append(10*max)
#        temp[:size // 2] *=2
#        return temp
#    max = 100 if short else 100000
#    temp = [random.randint(1, max) for i in range(size)]
#    temp = partially(temp, size) if seed == 2 else temp
#    return temp

#def genDATE(size, seed):
#    temp =[]
#    d1 = cs.Date(2000, 1, 1)  
#    d2 = cs.Date(2020, 11, 31)  
#    if (seed == 3):
#        temp = []
#        for i in range(size // 2):
#            temp.append(d2)
#        for i in range(size//2, size):
#            temp.append(d1)
#        return temp

#    #d1 = date(2000, 1, 1)  
#    #d2 = date(2020, 12, 31)
#    for i in range(size):
#        #cur = d2 - timedelta(days = i)
#        temp.append(cs.Date(random.randint(2000, 2021),random.randint(1, 12),random.randint(1, 31)))

#    random.shuffle(temp)
#    temp = partially(temp, size) if seed == 2 else temp
#    return temp

#def testSorts(i, dtype):
#    dictTemp =  {
#                '100': 0,
#                '1000': 0,
#                '10000' : 0,
#                '100000' : 0,
#                '1000000' : 0
#                #'10000000' : 0,
#                #'100000000' : 0
#                }
#    for size in [100, 1000, 10000, 100000, 1000000]:

#        if(dtype == 0):
#            Array = genSTR(size, 1)
#        if(dtype == 1):
#            Array = genDATE(size, 1)
#        if(dtype == 2):
#            Array = genINT(size, True, 1)
#        if(dtype == 3):
#            Array = genINT(size, False, 1)

#        if i == 0:
#            iter_start = time.perf_counter()
#            func.bubblsort(Array)
#            now = time.perf_counter()
#            dictTemp[str(size)] = now - iter_start
#        if i == 1:
#            iter_start = time.perf_counter()
#            func.shellsort(Array)
#            now = time.perf_counter()
#            dictTemp[str(size)] = now - iter_start
#        if i == 2:
#            iter_start = time.perf_counter()
#            func.quicksort(Array)
#            now = time.perf_counter()
#            dictTemp[str(size)] = now - iter_start
#        if i == 3:
#            iter_start = time.perf_counter()
#            func.mergesort(Array)
#            now = time.perf_counter()
#            dictTemp[str(size)] = now - iter_start
#        if i == 5:
#            if(dtype == 0):
#                iter_start = time.perf_counter()
#                func.Sradixsort(Array)
#                now = time.perf_counter()
#                dictTemp[str(size)] = now - iter_start
#            elif(dtype == 1):
#                iter_start = time.perf_counter()
#                func.Dradixsort(Array)
#                now = time.perf_counter()
#                dictTemp[str(size)] = now - iter_start
#            else:
#                iter_start = time.perf_counter()
#                func.radixsort(Array)
#                now = time.perf_counter()
#                dictTemp[str(size)] = now - iter_start
#        if i == 4:
#            iter_start = time.perf_counter()
#            func.heapsort(Array)
#            now = time.perf_counter()
#            dictTemp[str(size)] = now - iter_start
#        if i == 6:
#            iter_start = time.perf_counter()
#            sorted(Array)
#            now = time.perf_counter()
#            dictTemp[str(size)] = now - iter_start
#        print(size, dtype)
#        print(dictTemp[str(size)])
#    return dictTemp
            
#def testArray(Array, sTYPE, dTYPE):
#    #print(Array)
#    dictTemp =  {
#                #'bubblesort': 0,
#                #'shellsort': 0,
#                'quicksort' : 0,
#                #'mergesort' : 0,
#                #'heapsort' : 0,
#                'radixsort' : 0,
#                'bucketsort' : 0,
#                'sort': 0
#                }

#    #iter_start = time.perf_counter()
#    #func.bubblsort(Array)
#    #now = time.perf_counter()
#    #dictTemp['bubblesort'] = now - iter_start
#    #print(func.bubblsort(Array))
    
#    #iter_start = time.perf_counter()
#    #func.shellsort(Array)
#    #now = time.perf_counter()
#    #dictTemp['shellsort'] = now - iter_start
#    #print(func.shellsort(Array))

#    iter_start = time.perf_counter()
#    func.quicksort(Array)
#    now = time.perf_counter()
#    dictTemp['quicksort'] = now - iter_start
#    #print(func.quicksort(Array))

#    #iter_start = time.perf_counter()
#    #func.mergesort(Array)
#    #now = time.perf_counter()
#    #dictTemp['mergesort'] = now - iter_start
#    #print(func.mergesort(Array))

#    if(sTYPE):
#        iter_start = time.perf_counter()
#        func.Sradixsort(Array)
#        now = time.perf_counter()
#        dictTemp['radixsort'] = now - iter_start
#        #print(func.Sradixsort(Array))
#    elif(dTYPE):
#        iter_start = time.perf_counter()
#        func.Dradixsort(Array)
#        now = time.perf_counter()
#        dictTemp['radixsort'] = now - iter_start
#        #print(func.Dradixsort(Array))
#    else:
#        iter_start = time.perf_counter()
#        func.radixsort(Array)
#        now = time.perf_counter()
#        dictTemp['radixsort'] = now - iter_start
#        #print(func.radixsort(Array))


#    #iter_start = time.perf_counter()
#    #func.heapsort(Array)
#    #now = time.perf_counter()
#    #dictTemp['heapsort'] = now - iter_start
#    #print(func.heapsort(Array))

#    iter_start = time.perf_counter()
#    func.timsort(Array)
#    now = time.perf_counter()
#    dictTemp['bucketsort'] = now - iter_start

#    iter_start = time.perf_counter()
#    sorted(Array)
#    now = time.perf_counter()
#    dictTemp['sort'] = now - iter_start
#    #print(sorted(Array))
#    #print(dictTemp['sort'])

#    return dictTemp

#def ShowStats(dict1, dict2, dict3, dict4, size, seed):
#    fig, ax = plt.subplots()
#    ax.set_xlabel( "SIZE: " + str(size) + "| seed: " + str(seed))    

#    #lists = sorted(dict1.items())
#    #x, y = zip(*lists)
#    #ax.plot(x, y, label = 'string',  marker='o')

#    #lists = sorted(dict2.items())
#    #x, y = zip(*lists)
#    #ax.plot(x, y, label = 'date',  marker='o')

#    #lists = sorted(dict3.items())
#    #x, y = zip(*lists)
#    #ax.plot(x, y, label = 'short int',  marker='o')

#    lists = sorted(dict4.items())
#    x, y = zip(*lists)
#    ax.plot(x, y, label = 'int',  marker='o')
#    plt.legend()
#    plt.grid(True)
#    plt.show()

#def ShowStats2(dict1, dict2, dict3, dict4, i):
#    fig, ax = plt.subplots()
#    ax.set_xlabel( "TYPE: " + str(i))    

#    lists = sorted(dict1.items())
#    x, y = zip(*lists)
#    ax.plot(x, y, label = 'string',  marker='o')

#    lists = sorted(dict2.items())
#    x, y = zip(*lists)
#    ax.plot(x, y, label = 'date',  marker='o')

#    lists = sorted(dict3.items())
#    x, y = zip(*lists)
#    ax.plot(x, y, label = 'short int',  marker='o')

#    lists = sorted(dict4.items())
#    x, y = zip(*lists)
#    ax.plot(x, y, label = 'int',  marker='o')

#    plt.legend()
#    plt.grid(True)
#    plt.show()

#def startArrays(size, seed):
#    dSTR = []
#    #dSTR = testArray(genSTR(size, seed), True, False)
#    #print("str completed")
#    dDATE = []
#    #dDATE = testArray(genDATE(size, seed), False, True)
#    #print("date completed")
#    dSINT = []
#    #dSINT = testArray(genINT(size, True, seed), False, False)
#    #print("short_int completed")
#    dINT = testArray(genINT(size, False, seed), False, False)
#    print("int completed")
#    #print("{строки: ", dSTR['sort'], "; даты: ", dDATE['sort'], "; короткие целые: ", dSINT['sort'], "; целые: ", dINT['sort'],"}")
#    ShowStats(dSTR, dDATE, dSINT, dINT, size, seed)
#    return dSTR, dDATE, dSINT, dINT

#def startSorts(i):
#    dSTR = testSorts(i, 0)
#    print("str completed")
#    #dSTR = []
#    dDATE =  testSorts(i, 1)
#    print("date completed")
#    #dDATE = []
#    dSINT =  testSorts(i, 2)
#    print("short_int completed")
#    #dSINT = []
#    dINT =  testSorts(i, 3)
#    print("int completed")

#    winsound.MessageBeep() 
#    ShowStats2(dSTR, dDATE, dSINT, dINT, i)
#    return dSTR, dDATE, dSINT, dINT

##for i in range (0,7):
##    print("cur_seed: " + str(i))
##    dSTR, dDATE, dSINT, dINT = startSorts(i)

##dSTR, dDATE, dSINT, dINT = startSorts(6)

#startArrays(1000, 2)


##def test():
##    for size in [50, 500, 5000, 50000, 500000]:
##        print("cur_size: " + str(size))
##        for i in range (1,4):
##            print("cur_seed: " + str(i))
##            dSTR, dDATE, dSINT, dINT = startArrayss(size, i)

import tensorflow an tf
