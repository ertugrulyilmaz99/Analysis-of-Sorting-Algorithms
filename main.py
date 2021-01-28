import random
import math
import matplotlib.pyplot as plt
#It is so important for closing the plot windows for the backends which is MacOSX
plt.switch_backend('TkAgg')

def createArrayIncreasingOrder(n):
    array = []
    for i in range(1, n+1):
        array.append(i)
    return array

def createArrayDecreasingOrder(n):
    array = []
    for i in range(n, 0, -1):
        array.append(i)
    return array

def createArrayRandomizedOrder(n):
    array = []
    for i in range(n, 0, -1):
        array.append(i)
    for i in range(0, n):
        j=random.randint(i, n-1)
        array[i], array[j] = array[j], array[i]
    return array

def hireAssistant(array):
    total_Times_row_Repeated = 0
    no_of_comparison = 0
    no_of_exchangers = 0

    numberOfHires = 0

    best = 0
    total_Times_row_Repeated = total_Times_row_Repeated + 1

    for i in range(0, len(array)):
        no_of_comparison = no_of_comparison + 1
        total_Times_row_Repeated = total_Times_row_Repeated + 1

        no_of_comparison = no_of_comparison + 1
        total_Times_row_Repeated = total_Times_row_Repeated + 1
        if array[i] > best:

            total_Times_row_Repeated = total_Times_row_Repeated + 1
            best = array[i]
            no_of_exchangers = no_of_exchangers + 1

            numberOfHires += 1
            #print("HIRED")
    #print("Number of hiring is", numberOfHires)

    return array, total_Times_row_Repeated, no_of_comparison, no_of_exchangers

def insertionSort(array):
    total_Times_row_Repeated = 0
    no_of_comparison = 0
    no_of_exchangers = 0

    total_Times_row_Repeated = total_Times_row_Repeated + 1
    no_of_comparison = no_of_comparison + 1
    for j in range(1, len(array)):
        no_of_comparison = no_of_comparison + 1
        total_Times_row_Repeated = total_Times_row_Repeated + 1

        total_Times_row_Repeated = total_Times_row_Repeated + 1
        key = array[j]

        total_Times_row_Repeated = total_Times_row_Repeated + 1
        i = j-1

        no_of_comparison = no_of_comparison + 1
        total_Times_row_Repeated = total_Times_row_Repeated + 1
        while i >= 0 and array[i] > key:
            no_of_comparison = no_of_comparison + 1

            no_of_exchangers = no_of_exchangers + 1
            total_Times_row_Repeated = total_Times_row_Repeated + 1
            array[i+1] = array[i]

            total_Times_row_Repeated = total_Times_row_Repeated + 1
            i = i-1

        total_Times_row_Repeated = total_Times_row_Repeated + 1
        array[i+1] = key
        no_of_exchangers = no_of_exchangers + 1

    #print(array)

    return array, total_Times_row_Repeated, no_of_comparison, no_of_exchangers

def selectionSort(array):
    total_Times_row_Repeated = 0
    no_of_comparison = 0
    no_of_exchangers = 0

    total_Times_row_Repeated = total_Times_row_Repeated + 1
    lenght = len(array)

    total_Times_row_Repeated = total_Times_row_Repeated + 1
    no_of_comparison = no_of_comparison + 1
    for j in range(0 , lenght-1):
        no_of_comparison = no_of_comparison + 1
        total_Times_row_Repeated = total_Times_row_Repeated + 1

        total_Times_row_Repeated = total_Times_row_Repeated + 1
        smallestIndex = j

        total_Times_row_Repeated = total_Times_row_Repeated + 1
        no_of_comparison = no_of_comparison + 1
        for i in range (j+1, lenght):
            no_of_comparison = no_of_comparison + 1
            total_Times_row_Repeated = total_Times_row_Repeated + 1

            total_Times_row_Repeated = total_Times_row_Repeated + 1
            no_of_comparison = no_of_comparison + 1
            if array[i] < array[smallestIndex]:

                total_Times_row_Repeated = total_Times_row_Repeated + 1
                smallestIndex = i

        total_Times_row_Repeated = total_Times_row_Repeated + 1
        array[j], array[smallestIndex] = array[smallestIndex], array[j]
        no_of_exchangers = no_of_exchangers + 1

    #print(array)

    return array, total_Times_row_Repeated, no_of_comparison, no_of_exchangers

def bubbleSort(array):
    total_Times_row_Repeated = 0
    no_of_comparison = 0
    no_of_exchangers = 0

    total_Times_row_Repeated = total_Times_row_Repeated + 1
    no_of_comparison = no_of_comparison + 1
    for i in range(0, len(array)):
        no_of_comparison = no_of_comparison + 1
        total_Times_row_Repeated = total_Times_row_Repeated + 1

        total_Times_row_Repeated = total_Times_row_Repeated + 1
        no_of_comparison = no_of_comparison + 1
        for j in range(len(array)-1, i, -1):
            no_of_comparison = no_of_comparison + 1
            total_Times_row_Repeated = total_Times_row_Repeated + 1

            total_Times_row_Repeated = total_Times_row_Repeated + 1
            no_of_comparison = no_of_comparison + 1
            if array[j] < array[j-1]:

                total_Times_row_Repeated = total_Times_row_Repeated + 1
                array[j], array[j-1] = array[j-1], array[j]
                no_of_exchangers = no_of_exchangers + 1

    #print(array)

    return array, total_Times_row_Repeated, no_of_comparison, no_of_exchangers

def merge(array, p, q, r, counter):
    #Compute the n1 and n2

    n1 = q-p+1
    n2 = r-q

    # Create the array
    L = []
    R = []
    counter[0] = counter[0] + 4

    # Copying data to L[] and R[]
    for i in range(0, n1):
        counter[1] = counter[1] + 1
        counter[0] = counter[0] + 1
        L.append(array[p + i])
        counter[0] = counter[0] + 1
    L.append(math.inf)
    counter[0] = counter[0] + 1

    for j in range(0, n2):
        counter[1] = counter[1] + 1
        counter[0] = counter[0] + 1
        R.append(array[q + 1 + j])
        counter[0] = counter[0] + 1
    R.append(math.inf)
    counter[0] = counter[0] + 1

        # Merge the temp arrays back into arr[l..r]
    i = 0  # Initial index of first subarray
    j = 0  # Initial index of second subarray
    counter[0] = counter[0] + 2


    for k in range(p, r+1):
        counter[1] = counter[1] + 1
        counter[0] = counter[0] + 1
        counter[1] = counter[1] + 1
        if L[i] <= R[j]:

            counter[2] = counter[2] + 1
            array[k] = L[i]

            i += 1
            counter[0] = counter[0] + 2
        else:

            counter[2] = counter[2] + 1
            array[k] = R[j]
            j += 1
            counter[0] = counter[0] + 2

    return counter

def mergeSort(array, p, r):
    counter = [0] * 3

    counter[0] = counter[0] + 1
    counter[1] = counter[1] + 1
    if p < r:
        counter[0] = counter[0] + 1
        q = (p + r) // 2

        # Sort first and second halves
        mergeSort(array, p, q)
        mergeSort(array, q + 1, r)
        merge(array, p, q, r, counter)

    total_Times_row_Repeated = counter[0]
    no_of_comparison = counter[1]
    no_of_exchangers = counter[2]

    return array, total_Times_row_Repeated, no_of_comparison, no_of_exchangers


def compareIncreasing():

    total_Times_row_Repeated_Hire = [0] * 5
    no_of_comparison_Hire = [0] * 5
    no_of_exchangers_Hire = [0] * 5

    total_Times_row_Repeated_Insertion = [0] * 5
    no_of_comparison_Insertion = [0] * 5
    no_of_exchangers_Insertion = [0] * 5

    total_Times_row_Repeated_Selection = [0] * 5
    no_of_comparison_Selection = [0] * 5
    no_of_exchangers_Selection = [0] * 5

    total_Times_row_Repeated_Bubble = [0] * 5
    no_of_comparison_Bubble = [0] * 5
    no_of_exchangers_Bubble = [0] * 5

    total_Times_row_Repeated_Merge = [0] * 5
    no_of_comparison_Merge = [0] * 5
    no_of_exchangers_Merge = [0] * 5


    # 10, 100, 1000, 10000, 50000

    n = 10
    index = 0

    arrayHire = createArrayIncreasingOrder(n)
    arrayInsertion = arrayHire.copy()
    arraySelection = arrayHire.copy()
    arrayBubble = arrayHire.copy()
    arrayMerge = arrayHire.copy()

    print("\nN=", n)
    print("Array:", arrayHire)

    sortedArrayHire, total_Times_row_Repeated_Hire[index], no_of_comparison_Hire[index], no_of_exchangers_Hire[index] = hireAssistant(arrayHire)

    sortedArrayInsertion, total_Times_row_Repeated_Insertion[index], no_of_comparison_Insertion[index], no_of_exchangers_Insertion[index] = insertionSort(arrayInsertion)

    sortedArraySelection, total_Times_row_Repeated_Selection[index], no_of_comparison_Selection[index], no_of_exchangers_Selection[index] = selectionSort(arraySelection)

    sortedArrayBubble, total_Times_row_Repeated_Bubble[index], no_of_comparison_Bubble[index], no_of_exchangers_Bubble[index] = bubbleSort(arrayBubble)

    sortedArrayMerge, total_Times_row_Repeated_Merge[index], no_of_comparison_Merge[index], no_of_exchangers_Merge[index] = mergeSort(arrayMerge, 0, len(arrayMerge))

    print("Hire:",sortedArrayHire," ",total_Times_row_Repeated_Hire[index], " ",no_of_comparison_Hire[index], " ",no_of_exchangers_Hire[index], " ")
    print("Insertion:",sortedArrayInsertion," ",total_Times_row_Repeated_Insertion[index], " ",no_of_comparison_Insertion[index], " ",no_of_exchangers_Insertion[index], " ")
    print("Selection:",sortedArraySelection," ",total_Times_row_Repeated_Selection[index], " ",no_of_comparison_Selection[index], " ",no_of_exchangers_Selection[index], " ")
    print("Bubble:",sortedArrayBubble," ",total_Times_row_Repeated_Bubble[index], " ",no_of_comparison_Bubble[index], " ",no_of_exchangers_Bubble[index], " ")
    print("Merge:", sortedArrayMerge, " ", total_Times_row_Repeated_Merge[index], " ",
          no_of_comparison_Merge[index], " ", no_of_exchangers_Merge[index], " ")

    arrayHire.clear()
    arrayInsertion.clear()
    arraySelection.clear()
    arrayBubble.clear()
    arrayMerge.clear()
    sortedArrayHire.clear()
    sortedArrayInsertion.clear()
    sortedArraySelection.clear()
    sortedArrayBubble.clear()
    sortedArrayMerge.clear()

    # 100
    n = 100
    index = 1

    arrayHire = createArrayIncreasingOrder(n)
    arrayInsertion = arrayHire.copy()
    arraySelection = arrayHire.copy()
    arrayBubble = arrayHire.copy()
    arrayMerge = arrayHire.copy()

    print("\nN=", n)
    print("Array:", arrayHire)

    sortedArrayHire, total_Times_row_Repeated_Hire[index], no_of_comparison_Hire[index], no_of_exchangers_Hire[
        index] = hireAssistant(arrayHire)

    sortedArrayInsertion, total_Times_row_Repeated_Insertion[index], no_of_comparison_Insertion[index], \
    no_of_exchangers_Insertion[index] = insertionSort(arrayInsertion)

    sortedArraySelection, total_Times_row_Repeated_Selection[index], no_of_comparison_Selection[index], \
    no_of_exchangers_Selection[index] = selectionSort(arraySelection)

    sortedArrayBubble, total_Times_row_Repeated_Bubble[index], no_of_comparison_Bubble[index], no_of_exchangers_Bubble[
        index] = bubbleSort(arrayBubble)

    sortedArrayMerge, total_Times_row_Repeated_Merge[index], no_of_comparison_Merge[index], no_of_exchangers_Merge[
        index] = mergeSort(arrayMerge, 0, len(arrayMerge))

    print("Hire:", sortedArrayHire, "\n", total_Times_row_Repeated_Hire[1], " ", no_of_comparison_Hire[1], " ",
          no_of_exchangers_Hire[1], " ")
    print("Insertion:", sortedArrayInsertion, "\n", total_Times_row_Repeated_Insertion[1], " ",
          no_of_comparison_Insertion[1], " ", no_of_exchangers_Insertion[1], " ")
    print("Selection:", sortedArraySelection, "\n", total_Times_row_Repeated_Selection[1], " ",
          no_of_comparison_Selection[1], " ", no_of_exchangers_Selection[1], " ")
    print("Bubble:", sortedArrayBubble, "\n", total_Times_row_Repeated_Bubble[1], " ", no_of_comparison_Bubble[1], " ",
          no_of_exchangers_Bubble[1], " ")
    print("Merge:", sortedArrayMerge, " ", total_Times_row_Repeated_Merge[index], " ",
          no_of_comparison_Merge[index], " ", no_of_exchangers_Merge[index], " ")

    arrayHire.clear()
    arrayInsertion.clear()
    arraySelection.clear()
    arrayBubble.clear()
    arrayMerge.clear()
    sortedArrayHire.clear()
    sortedArrayInsertion.clear()
    sortedArraySelection.clear()
    sortedArrayBubble.clear()
    sortedArrayMerge.clear()

    # 1000
    n = 1000
    index = 2

    arrayHire = createArrayIncreasingOrder(n)
    arrayInsertion = arrayHire.copy()
    arraySelection = arrayHire.copy()
    arrayBubble = arrayHire.copy()
    arrayMerge = arrayHire.copy()

    print("\nN=", n)
    print("Array:", arrayHire)

    sortedArrayHire, total_Times_row_Repeated_Hire[index], no_of_comparison_Hire[index], no_of_exchangers_Hire[
        index] = hireAssistant(arrayHire)

    sortedArrayInsertion, total_Times_row_Repeated_Insertion[index], no_of_comparison_Insertion[index], \
    no_of_exchangers_Insertion[index] = insertionSort(arrayInsertion)

    sortedArraySelection, total_Times_row_Repeated_Selection[index], no_of_comparison_Selection[index], \
    no_of_exchangers_Selection[index] = selectionSort(arraySelection)

    sortedArrayBubble, total_Times_row_Repeated_Bubble[index], no_of_comparison_Bubble[index], no_of_exchangers_Bubble[
        index] = bubbleSort(arrayBubble)

    sortedArrayMerge, total_Times_row_Repeated_Merge[index], no_of_comparison_Merge[index], no_of_exchangers_Merge[
        index] = mergeSort(arrayMerge, 0, len(arrayMerge))

    print("Hire:", sortedArrayHire, "\n", total_Times_row_Repeated_Hire[index], " ", no_of_comparison_Hire[index], " ",
          no_of_exchangers_Hire[index], " ")
    print("Insertion:", sortedArrayInsertion, "\n", total_Times_row_Repeated_Insertion[index], " ",
          no_of_comparison_Insertion[index], " ", no_of_exchangers_Insertion[index], " ")
    print("Selection:", sortedArraySelection, "\n", total_Times_row_Repeated_Selection[index], " ",
          no_of_comparison_Selection[index], " ", no_of_exchangers_Selection[index], " ")
    print("Bubble:", sortedArrayBubble, "\n", total_Times_row_Repeated_Bubble[index], " ", no_of_comparison_Bubble[index], " ",
          no_of_exchangers_Bubble[index], " ")
    print("Merge:", sortedArrayMerge, " ", total_Times_row_Repeated_Merge[index], " ",
          no_of_comparison_Merge[index], " ", no_of_exchangers_Merge[index], " ")

    arrayHire.clear()
    arrayInsertion.clear()
    arraySelection.clear()
    arrayBubble.clear()
    arrayMerge.clear()
    sortedArrayHire.clear()
    sortedArrayInsertion.clear()
    sortedArraySelection.clear()
    sortedArrayBubble.clear()
    sortedArrayMerge.clear()

    # 10000
    n = 10000
    index = 3

    arrayHire = createArrayIncreasingOrder(n)
    arrayInsertion = arrayHire.copy()
    arraySelection = arrayHire.copy()
    arrayBubble = arrayHire.copy()
    arrayMerge = arrayHire.copy()

    print("\nN=", n)
    print("Array:", arrayHire)

    sortedArrayHire, total_Times_row_Repeated_Hire[index], no_of_comparison_Hire[index], no_of_exchangers_Hire[
        index] = hireAssistant(arrayHire)

    sortedArrayInsertion, total_Times_row_Repeated_Insertion[index], no_of_comparison_Insertion[index], \
    no_of_exchangers_Insertion[index] = insertionSort(arrayInsertion)

    sortedArraySelection, total_Times_row_Repeated_Selection[index], no_of_comparison_Selection[index], \
    no_of_exchangers_Selection[index] = selectionSort(arraySelection)

    sortedArrayBubble, total_Times_row_Repeated_Bubble[index], no_of_comparison_Bubble[index], no_of_exchangers_Bubble[
        index] = bubbleSort(arrayBubble)

    sortedArrayMerge, total_Times_row_Repeated_Merge[index], no_of_comparison_Merge[index], no_of_exchangers_Merge[
        index] = mergeSort(arrayMerge, 0, len(arrayMerge))

    print("Hire:", sortedArrayHire, "\n", total_Times_row_Repeated_Hire[index], " ", no_of_comparison_Hire[index], " ",
          no_of_exchangers_Hire[index], " ")
    print("Insertion:", sortedArrayInsertion, "\n", total_Times_row_Repeated_Insertion[index], " ",
          no_of_comparison_Insertion[index], " ", no_of_exchangers_Insertion[index], " ")
    print("Selection:", sortedArraySelection, "\n", total_Times_row_Repeated_Selection[index], " ",
          no_of_comparison_Selection[index], " ", no_of_exchangers_Selection[index], " ")
    print("Bubble:", sortedArrayBubble, "\n", total_Times_row_Repeated_Bubble[index], " ", no_of_comparison_Bubble[index], " ",
          no_of_exchangers_Bubble[index], " ")
    print("Merge:", sortedArrayMerge, " ", total_Times_row_Repeated_Merge[index], " ",
          no_of_comparison_Merge[index], " ", no_of_exchangers_Merge[index], " ")

    arrayHire.clear()
    arrayInsertion.clear()
    arraySelection.clear()
    arrayBubble.clear()
    arrayMerge.clear()
    sortedArrayHire.clear()
    sortedArrayInsertion.clear()
    sortedArraySelection.clear()
    sortedArrayBubble.clear()
    sortedArrayMerge.clear()

    plt.xlabel("Number of elements")
    plt.ylabel("Total Number of Rows Repeated")
    plt.plot([10, 100, 1000, 10000], [total_Times_row_Repeated_Hire[0], total_Times_row_Repeated_Hire[1]
        , total_Times_row_Repeated_Hire[2], total_Times_row_Repeated_Hire[3]], 'r')
    plt.plot([10, 100, 1000, 10000], [total_Times_row_Repeated_Insertion[0], total_Times_row_Repeated_Insertion[1]
        , total_Times_row_Repeated_Insertion[2], total_Times_row_Repeated_Insertion[3]], 'b')
    plt.plot([10, 100, 1000, 10000], [total_Times_row_Repeated_Selection[0], total_Times_row_Repeated_Selection[1]
        , total_Times_row_Repeated_Selection[2], total_Times_row_Repeated_Selection[3]], 'g')
    plt.plot([10, 100, 1000, 10000], [total_Times_row_Repeated_Bubble[0], total_Times_row_Repeated_Bubble[1]
        , total_Times_row_Repeated_Bubble[2], total_Times_row_Repeated_Bubble[3]], 'm')
    plt.show()

def compareIncreasing1():
    total_Times_row_Repeated_Hire = [0] * 5
    no_of_comparison_Hire = [0] * 5
    no_of_exchangers_Hire = [0] * 5

    total_Times_row_Repeated_Insertion = [0] * 5
    no_of_comparison_Insertion = [0] * 5
    no_of_exchangers_Insertion = [0] * 5

    total_Times_row_Repeated_Selection = [0] * 5
    no_of_comparison_Selection = [0] * 5
    no_of_exchangers_Selection = [0] * 5

    total_Times_row_Repeated_Bubble = [0] * 5
    no_of_comparison_Bubble = [0] * 5
    no_of_exchangers_Bubble = [0] * 5

    total_Times_row_Repeated_Merge = [0] * 5
    no_of_comparison_Merge = [0] * 5
    no_of_exchangers_Merge = [0] * 5

    # 10, 100, 1000, 10000, 50000

    n = 10
    index = 0

    arrayHire = createArrayIncreasingOrder(n)
    arrayInsertion = arrayHire.copy()
    arraySelection = arrayHire.copy()
    arrayBubble = arrayHire.copy()
    arrayMerge = arrayHire.copy()

    print("\nN=", n)
    print("Array:", arrayHire)

    sortedArrayHire, total_Times_row_Repeated_Hire[index], no_of_comparison_Hire[index], no_of_exchangers_Hire[
        index] = hireAssistant(arrayHire)

    sortedArrayInsertion, total_Times_row_Repeated_Insertion[index], no_of_comparison_Insertion[index], \
    no_of_exchangers_Insertion[index] = insertionSort(arrayInsertion)

    sortedArraySelection, total_Times_row_Repeated_Selection[index], no_of_comparison_Selection[index], \
    no_of_exchangers_Selection[index] = selectionSort(arraySelection)

    sortedArrayBubble, total_Times_row_Repeated_Bubble[index], no_of_comparison_Bubble[index], no_of_exchangers_Bubble[
        index] = bubbleSort(arrayBubble)

    sortedArrayMerge, total_Times_row_Repeated_Merge[index], no_of_comparison_Merge[index], no_of_exchangers_Merge[
        index] = mergeSort(arrayMerge, 0, len(arrayMerge)-1)

    print("Hire:", sortedArrayHire, " ", total_Times_row_Repeated_Hire[index], " ", no_of_comparison_Hire[index], " ",
          no_of_exchangers_Hire[index], " ")
    print("Insertion:", sortedArrayInsertion, " ", total_Times_row_Repeated_Insertion[index], " ",
          no_of_comparison_Insertion[index], " ", no_of_exchangers_Insertion[index], " ")
    print("Selection:", sortedArraySelection, " ", total_Times_row_Repeated_Selection[index], " ",
          no_of_comparison_Selection[index], " ", no_of_exchangers_Selection[index], " ")
    print("Bubble:", sortedArrayBubble, " ", total_Times_row_Repeated_Bubble[index], " ",
          no_of_comparison_Bubble[index], " ", no_of_exchangers_Bubble[index], " ")
    print("Merge:", sortedArrayMerge, " ", total_Times_row_Repeated_Merge[index], " ",
          no_of_comparison_Merge[index], " ", no_of_exchangers_Merge[index], " ")

    arrayHire.clear()
    arrayInsertion.clear()
    arraySelection.clear()
    arrayBubble.clear()
    arrayMerge.clear()
    sortedArrayHire.clear()
    sortedArrayInsertion.clear()
    sortedArraySelection.clear()
    sortedArrayBubble.clear()
    sortedArrayMerge.clear()

    # 100
    n = 100
    index = 1

    arrayHire = createArrayIncreasingOrder(n)
    arrayInsertion = arrayHire.copy()
    arraySelection = arrayHire.copy()
    arrayBubble = arrayHire.copy()
    arrayMerge = arrayHire.copy()

    print("\nN=", n)
    print("Array:", arrayHire)

    sortedArrayHire, total_Times_row_Repeated_Hire[index], no_of_comparison_Hire[index], no_of_exchangers_Hire[
        index] = hireAssistant(arrayHire)

    sortedArrayInsertion, total_Times_row_Repeated_Insertion[index], no_of_comparison_Insertion[index], \
    no_of_exchangers_Insertion[index] = insertionSort(arrayInsertion)

    sortedArraySelection, total_Times_row_Repeated_Selection[index], no_of_comparison_Selection[index], \
    no_of_exchangers_Selection[index] = selectionSort(arraySelection)

    sortedArrayBubble, total_Times_row_Repeated_Bubble[index], no_of_comparison_Bubble[index], no_of_exchangers_Bubble[
        index] = bubbleSort(arrayBubble)

    sortedArrayMerge, total_Times_row_Repeated_Merge[index], no_of_comparison_Merge[index], no_of_exchangers_Merge[
        index] = mergeSort(arrayMerge, 0, len(arrayMerge)-1)

    print("Hire:", sortedArrayHire, "\n", total_Times_row_Repeated_Hire[1], " ", no_of_comparison_Hire[1], " ",
          no_of_exchangers_Hire[1], " ")
    print("Insertion:", sortedArrayInsertion, "\n", total_Times_row_Repeated_Insertion[1], " ",
          no_of_comparison_Insertion[1], " ", no_of_exchangers_Insertion[1], " ")
    print("Selection:", sortedArraySelection, "\n", total_Times_row_Repeated_Selection[1], " ",
          no_of_comparison_Selection[1], " ", no_of_exchangers_Selection[1], " ")
    print("Bubble:", sortedArrayBubble, "\n", total_Times_row_Repeated_Bubble[1], " ", no_of_comparison_Bubble[1], " ",
          no_of_exchangers_Bubble[1], " ")
    print("Merge:", sortedArrayMerge, " ", total_Times_row_Repeated_Merge[index], " ",
          no_of_comparison_Merge[index], " ", no_of_exchangers_Merge[index], " ")

    arrayHire.clear()
    arrayInsertion.clear()
    arraySelection.clear()
    arrayBubble.clear()
    arrayMerge.clear()
    sortedArrayHire.clear()
    sortedArrayInsertion.clear()
    sortedArraySelection.clear()
    sortedArrayBubble.clear()
    sortedArrayMerge.clear()

    # 1000
    n = 1000
    index = 2

    arrayHire = createArrayIncreasingOrder(n)
    arrayInsertion = arrayHire.copy()
    arraySelection = arrayHire.copy()
    arrayBubble = arrayHire.copy()
    arrayMerge = arrayHire.copy()

    print("\nN=", n)
    print("Array:", arrayHire)

    sortedArrayHire, total_Times_row_Repeated_Hire[index], no_of_comparison_Hire[index], no_of_exchangers_Hire[
        index] = hireAssistant(arrayHire)

    sortedArrayInsertion, total_Times_row_Repeated_Insertion[index], no_of_comparison_Insertion[index], \
    no_of_exchangers_Insertion[index] = insertionSort(arrayInsertion)

    sortedArraySelection, total_Times_row_Repeated_Selection[index], no_of_comparison_Selection[index], \
    no_of_exchangers_Selection[index] = selectionSort(arraySelection)

    sortedArrayBubble, total_Times_row_Repeated_Bubble[index], no_of_comparison_Bubble[index], no_of_exchangers_Bubble[
        index] = bubbleSort(arrayBubble)

    sortedArrayMerge, total_Times_row_Repeated_Merge[index], no_of_comparison_Merge[index], no_of_exchangers_Merge[
        index] = mergeSort(arrayMerge, 0, len(arrayMerge)-1)

    print("Hire:", sortedArrayHire, "\n", total_Times_row_Repeated_Hire[index], " ", no_of_comparison_Hire[index], " ",
          no_of_exchangers_Hire[index], " ")
    print("Insertion:", sortedArrayInsertion, "\n", total_Times_row_Repeated_Insertion[index], " ",
          no_of_comparison_Insertion[index], " ", no_of_exchangers_Insertion[index], " ")
    print("Selection:", sortedArraySelection, "\n", total_Times_row_Repeated_Selection[index], " ",
          no_of_comparison_Selection[index], " ", no_of_exchangers_Selection[index], " ")
    print("Bubble:", sortedArrayBubble, "\n", total_Times_row_Repeated_Bubble[index], " ",
          no_of_comparison_Bubble[index], " ",
          no_of_exchangers_Bubble[index], " ")
    print("Merge:", sortedArrayMerge, " ", total_Times_row_Repeated_Merge[index], " ",
          no_of_comparison_Merge[index], " ", no_of_exchangers_Merge[index], " ")

    arrayHire.clear()
    arrayInsertion.clear()
    arraySelection.clear()
    arrayBubble.clear()
    arrayMerge.clear()
    sortedArrayHire.clear()
    sortedArrayInsertion.clear()
    sortedArraySelection.clear()
    sortedArrayBubble.clear()
    sortedArrayMerge.clear()

    # 10000
    n = 10000
    index = 3

    arrayHire = createArrayIncreasingOrder(n)
    arrayInsertion = arrayHire.copy()
    arraySelection = arrayHire.copy()
    arrayBubble = arrayHire.copy()
    arrayMerge = arrayHire.copy()

    print("\nN=", n)
    print("Array:", arrayHire)

    sortedArrayHire, total_Times_row_Repeated_Hire[index], no_of_comparison_Hire[index], no_of_exchangers_Hire[
        index] = hireAssistant(arrayHire)

    sortedArrayInsertion, total_Times_row_Repeated_Insertion[index], no_of_comparison_Insertion[index], \
    no_of_exchangers_Insertion[index] = insertionSort(arrayInsertion)

    sortedArraySelection, total_Times_row_Repeated_Selection[index], no_of_comparison_Selection[index], \
    no_of_exchangers_Selection[index] = selectionSort(arraySelection)

    sortedArrayBubble, total_Times_row_Repeated_Bubble[index], no_of_comparison_Bubble[index], no_of_exchangers_Bubble[
        index] = bubbleSort(arrayBubble)

    sortedArrayMerge, total_Times_row_Repeated_Merge[index], no_of_comparison_Merge[index], no_of_exchangers_Merge[
        index] = mergeSort(arrayMerge, 0, len(arrayMerge)-1)

    print("Hire:", sortedArrayHire, "\n", total_Times_row_Repeated_Hire[index], " ", no_of_comparison_Hire[index], " ",
          no_of_exchangers_Hire[index], " ")
    print("Insertion:", sortedArrayInsertion, "\n", total_Times_row_Repeated_Insertion[index], " ",
          no_of_comparison_Insertion[index], " ", no_of_exchangers_Insertion[index], " ")
    print("Selection:", sortedArraySelection, "\n", total_Times_row_Repeated_Selection[index], " ",
          no_of_comparison_Selection[index], " ", no_of_exchangers_Selection[index], " ")
    print("Bubble:", sortedArrayBubble, "\n", total_Times_row_Repeated_Bubble[index], " ",
          no_of_comparison_Bubble[index], " ",
          no_of_exchangers_Bubble[index], " ")
    print("Merge:", sortedArrayMerge, " ", total_Times_row_Repeated_Merge[index], " ",
          no_of_comparison_Merge[index], " ", no_of_exchangers_Merge[index], " ")

    arrayHire.clear()
    arrayInsertion.clear()
    arraySelection.clear()
    arrayBubble.clear()
    arrayMerge.clear()
    sortedArrayHire.clear()
    sortedArrayInsertion.clear()
    sortedArraySelection.clear()
    sortedArrayBubble.clear()
    sortedArrayMerge.clear()

    names = ['Hire', 'Insertion', 'Selection', 'Bubble', 'Merge']

    plt.figure(figsize=(15, 7))
    # n=10
    index = 0

    plt.subplot(4, 3, 1)
    plt.title('Total Number of\nRows Repeated')
    plt.ylabel('N=10')
    plt.bar(names, [total_Times_row_Repeated_Hire[index], total_Times_row_Repeated_Insertion[index],
                    total_Times_row_Repeated_Selection[index], total_Times_row_Repeated_Bubble[index], total_Times_row_Repeated_Merge[index]],
            color=['b', 'r', 'm', 'g', 'y'])
    plt.subplot(4, 3, 2)
    plt.title('Number of Comparisons')
    plt.bar(names, [no_of_comparison_Hire[index], no_of_comparison_Insertion[index],
                    no_of_comparison_Selection[index], no_of_comparison_Bubble[index], no_of_comparison_Merge[index]],
            color=['b', 'r', 'm', 'g', 'y'])
    plt.subplot(4, 3, 3)
    plt.title('Number of Exchanges')
    plt.bar(names, [no_of_exchangers_Hire[index], no_of_exchangers_Insertion[index],
                    no_of_exchangers_Selection[index], no_of_exchangers_Bubble[index],no_of_exchangers_Merge[index]],
    color=['b', 'r', 'm', 'g', 'y'])
    # n=100
    index = 1

    plt.subplot(4, 3, 4)
    plt.ylabel('N=100')
    plt.bar(names, [total_Times_row_Repeated_Hire[index], total_Times_row_Repeated_Insertion[index],
                    total_Times_row_Repeated_Selection[index], total_Times_row_Repeated_Bubble[index], total_Times_row_Repeated_Merge[index]],
            color=['b', 'r', 'm', 'g', 'y'])
    plt.subplot(4, 3, 5)
    plt.bar(names, [no_of_comparison_Hire[index], no_of_comparison_Insertion[index],
                    no_of_comparison_Selection[index], no_of_comparison_Bubble[index], no_of_comparison_Merge[index]],
            color=['b', 'r', 'm', 'g', 'y'])
    plt.subplot(4, 3, 6)
    plt.bar(names, [no_of_exchangers_Hire[index], no_of_exchangers_Insertion[index],
                    no_of_exchangers_Selection[index], no_of_exchangers_Bubble[index], no_of_exchangers_Merge[index]],
            color=['b', 'r', 'm', 'g', 'y'])
    # n=1000
    index = 2

    plt.subplot(4, 3, 7)
    plt.ylabel('N=1000')
    plt.bar(names, [total_Times_row_Repeated_Hire[index], total_Times_row_Repeated_Insertion[index],
                    total_Times_row_Repeated_Selection[index], total_Times_row_Repeated_Bubble[index], total_Times_row_Repeated_Merge[index]],
            color=['b', 'r', 'm', 'g', 'y'])
    plt.subplot(4, 3, 8)
    plt.bar(names, [no_of_comparison_Hire[index], no_of_comparison_Insertion[index],
                    no_of_comparison_Selection[index], no_of_comparison_Bubble[index], no_of_comparison_Merge[index]],
            color=['b', 'r', 'm', 'g', 'y'])
    plt.subplot(4, 3, 9)
    plt.bar(names, [no_of_exchangers_Hire[index], no_of_exchangers_Insertion[index],
                    no_of_exchangers_Selection[index], no_of_exchangers_Bubble[index], no_of_exchangers_Merge[index]],
            color=['b', 'r', 'm', 'g', 'y'])
    # n=10000
    index = 3

    plt.subplot(4, 3, 10)
    plt.ylabel('N=10000')
    plt.bar(names, [total_Times_row_Repeated_Hire[index], total_Times_row_Repeated_Insertion[index],
                    total_Times_row_Repeated_Selection[index], total_Times_row_Repeated_Bubble[index], total_Times_row_Repeated_Merge[index]],
            color=['b', 'r', 'm', 'g', 'y'])
    plt.subplot(4, 3, 11)
    plt.bar(names, [no_of_comparison_Hire[index], no_of_comparison_Insertion[index],
                    no_of_comparison_Selection[index], no_of_comparison_Bubble[index], no_of_comparison_Merge[index]],
            color=['b', 'r', 'm', 'g', 'y'])
    plt.subplot(4, 3, 12)
    plt.bar(names, [no_of_exchangers_Hire[index], no_of_exchangers_Insertion[index],
                    no_of_exchangers_Selection[index], no_of_exchangers_Bubble[index], no_of_exchangers_Merge[index]],
            color=['b', 'r', 'm', 'g', 'y'])

    plt.suptitle('Array Type: Increasing', fontweight='bold')
    plt.show()


def compareDecreasing():

    total_Times_row_Repeated_Hire = [0] * 5
    no_of_comparison_Hire = [0] * 5
    no_of_exchangers_Hire = [0] * 5

    total_Times_row_Repeated_Insertion = [0] * 5
    no_of_comparison_Insertion = [0] * 5
    no_of_exchangers_Insertion = [0] * 5

    total_Times_row_Repeated_Selection = [0] * 5
    no_of_comparison_Selection = [0] * 5
    no_of_exchangers_Selection = [0] * 5

    total_Times_row_Repeated_Bubble = [0] * 5
    no_of_comparison_Bubble = [0] * 5
    no_of_exchangers_Bubble = [0] * 5


    # 10, 100, 1000, 10000, 50000

    n = 10
    index = 0

    arrayHire = createArrayDecreasingOrder(n)
    arrayInsertion = arrayHire.copy()
    arraySelection = arrayHire.copy()
    arrayBubble = arrayHire.copy()

    print("\nN=", n)
    print("Array:", arrayHire)

    sortedArrayHire, total_Times_row_Repeated_Hire[index], no_of_comparison_Hire[index], no_of_exchangers_Hire[index] = hireAssistant(arrayHire)

    sortedArrayInsertion, total_Times_row_Repeated_Insertion[index], no_of_comparison_Insertion[index], no_of_exchangers_Insertion[index] = insertionSort(arrayInsertion)

    sortedArraySelection, total_Times_row_Repeated_Selection[index], no_of_comparison_Selection[index], no_of_exchangers_Selection[index] = selectionSort(arraySelection)

    sortedArrayBubble, total_Times_row_Repeated_Bubble[index], no_of_comparison_Bubble[index], no_of_exchangers_Bubble[index] = bubbleSort(arrayBubble)

    print("Hire:",sortedArrayHire," ",total_Times_row_Repeated_Hire[index], " ",no_of_comparison_Hire[index], " ",no_of_exchangers_Hire[index], " ")
    print("Insertion:",sortedArrayInsertion," ",total_Times_row_Repeated_Insertion[index], " ",no_of_comparison_Insertion[index], " ",no_of_exchangers_Insertion[index], " ")
    print("Selection:",sortedArraySelection," ",total_Times_row_Repeated_Selection[index], " ",no_of_comparison_Selection[index], " ",no_of_exchangers_Selection[index], " ")
    print("Bubble:",sortedArrayBubble," ",total_Times_row_Repeated_Bubble[index], " ",no_of_comparison_Bubble[index], " ",no_of_exchangers_Bubble[index], " ")
    #print(," ",, " ",, " ",, " ")

    arrayHire.clear()
    arrayInsertion.clear()
    arraySelection.clear()
    arrayBubble.clear()
    sortedArrayHire.clear()
    sortedArrayInsertion.clear()
    sortedArraySelection.clear()
    sortedArrayBubble.clear()

    # 100
    n = 100
    index = 1

    arrayHire = createArrayDecreasingOrder(n)
    arrayInsertion = arrayHire.copy()
    arraySelection = arrayHire.copy()
    arrayBubble = arrayHire.copy()

    print("\nN=", n)
    print("Array:", arrayHire)

    sortedArrayHire, total_Times_row_Repeated_Hire[index], no_of_comparison_Hire[index], no_of_exchangers_Hire[
        index] = hireAssistant(arrayHire)

    sortedArrayInsertion, total_Times_row_Repeated_Insertion[index], no_of_comparison_Insertion[index], \
    no_of_exchangers_Insertion[index] = insertionSort(arrayInsertion)

    sortedArraySelection, total_Times_row_Repeated_Selection[index], no_of_comparison_Selection[index], \
    no_of_exchangers_Selection[index] = selectionSort(arraySelection)

    sortedArrayBubble, total_Times_row_Repeated_Bubble[index], no_of_comparison_Bubble[index], no_of_exchangers_Bubble[
        index] = bubbleSort(arrayBubble)

    print("Hire:", sortedArrayHire, "\n", total_Times_row_Repeated_Hire[1], " ", no_of_comparison_Hire[1], " ",
          no_of_exchangers_Hire[1], " ")
    print("Insertion:", sortedArrayInsertion, "\n", total_Times_row_Repeated_Insertion[1], " ",
          no_of_comparison_Insertion[1], " ", no_of_exchangers_Insertion[1], " ")
    print("Selection:", sortedArraySelection, "\n", total_Times_row_Repeated_Selection[1], " ",
          no_of_comparison_Selection[1], " ", no_of_exchangers_Selection[1], " ")
    print("Bubble:", sortedArrayBubble, "\n", total_Times_row_Repeated_Bubble[1], " ", no_of_comparison_Bubble[1], " ",
          no_of_exchangers_Bubble[1], " ")
    # print(," ",, " ",, " ",, " ")

    arrayHire.clear()
    arrayInsertion.clear()
    arraySelection.clear()
    arrayBubble.clear()
    sortedArrayHire.clear()
    sortedArrayInsertion.clear()
    sortedArraySelection.clear()
    sortedArrayBubble.clear()

    # 1000
    n = 1000
    index = 2

    arrayHire = createArrayDecreasingOrder(n)
    arrayInsertion = arrayHire.copy()
    arraySelection = arrayHire.copy()
    arrayBubble = arrayHire.copy()

    print("\nN=", n)
    print("Array:", arrayHire)

    sortedArrayHire, total_Times_row_Repeated_Hire[index], no_of_comparison_Hire[index], no_of_exchangers_Hire[
        index] = hireAssistant(arrayHire)

    sortedArrayInsertion, total_Times_row_Repeated_Insertion[index], no_of_comparison_Insertion[index], \
    no_of_exchangers_Insertion[index] = insertionSort(arrayInsertion)

    sortedArraySelection, total_Times_row_Repeated_Selection[index], no_of_comparison_Selection[index], \
    no_of_exchangers_Selection[index] = selectionSort(arraySelection)

    sortedArrayBubble, total_Times_row_Repeated_Bubble[index], no_of_comparison_Bubble[index], no_of_exchangers_Bubble[
        index] = bubbleSort(arrayBubble)

    print("Hire:", sortedArrayHire, "\n", total_Times_row_Repeated_Hire[index], " ", no_of_comparison_Hire[index], " ",
          no_of_exchangers_Hire[index], " ")
    print("Insertion:", sortedArrayInsertion, "\n", total_Times_row_Repeated_Insertion[index], " ",
          no_of_comparison_Insertion[index], " ", no_of_exchangers_Insertion[index], " ")
    print("Selection:", sortedArraySelection, "\n", total_Times_row_Repeated_Selection[index], " ",
          no_of_comparison_Selection[index], " ", no_of_exchangers_Selection[index], " ")
    print("Bubble:", sortedArrayBubble, "\n", total_Times_row_Repeated_Bubble[index], " ", no_of_comparison_Bubble[index], " ",
          no_of_exchangers_Bubble[index], " ")
    # print(," ",, " ",, " ",, " ")

    arrayHire.clear()
    arrayInsertion.clear()
    arraySelection.clear()
    arrayBubble.clear()
    sortedArrayHire.clear()
    sortedArrayInsertion.clear()
    sortedArraySelection.clear()
    sortedArrayBubble.clear()

    # 10000
    n = 10000
    index = 3

    arrayHire = createArrayDecreasingOrder(n)
    arrayInsertion = arrayHire.copy()
    arraySelection = arrayHire.copy()
    arrayBubble = arrayHire.copy()

    print("\nN=", n)
    print("Array:", arrayHire)

    sortedArrayHire, total_Times_row_Repeated_Hire[index], no_of_comparison_Hire[index], no_of_exchangers_Hire[
        index] = hireAssistant(arrayHire)

    sortedArrayInsertion, total_Times_row_Repeated_Insertion[index], no_of_comparison_Insertion[index], \
    no_of_exchangers_Insertion[index] = insertionSort(arrayInsertion)

    sortedArraySelection, total_Times_row_Repeated_Selection[index], no_of_comparison_Selection[index], \
    no_of_exchangers_Selection[index] = selectionSort(arraySelection)

    sortedArrayBubble, total_Times_row_Repeated_Bubble[index], no_of_comparison_Bubble[index], no_of_exchangers_Bubble[
        index] = bubbleSort(arrayBubble)

    print("Hire:", sortedArrayHire, "\n", total_Times_row_Repeated_Hire[index], " ", no_of_comparison_Hire[index], " ",
          no_of_exchangers_Hire[index], " ")
    print("Insertion:", sortedArrayInsertion, "\n", total_Times_row_Repeated_Insertion[index], " ",
          no_of_comparison_Insertion[index], " ", no_of_exchangers_Insertion[index], " ")
    print("Selection:", sortedArraySelection, "\n", total_Times_row_Repeated_Selection[index], " ",
          no_of_comparison_Selection[index], " ", no_of_exchangers_Selection[index], " ")
    print("Bubble:", sortedArrayBubble, "\n", total_Times_row_Repeated_Bubble[index], " ", no_of_comparison_Bubble[index], " ",
          no_of_exchangers_Bubble[index], " ")
    # print(," ",, " ",, " ",, " ")

    arrayHire.clear()
    arrayInsertion.clear()
    arraySelection.clear()
    arrayBubble.clear()
    sortedArrayHire.clear()
    sortedArrayInsertion.clear()
    sortedArraySelection.clear()
    sortedArrayBubble.clear()

    plt.xlabel("Number of elements")
    plt.ylabel("Total Number of Rows Repeated")
    plt.plot([10, 100, 1000, 10000], [total_Times_row_Repeated_Hire[0], total_Times_row_Repeated_Hire[1]
        , total_Times_row_Repeated_Hire[2], total_Times_row_Repeated_Hire[3]], 'r')
    plt.plot([10, 100, 1000, 10000], [total_Times_row_Repeated_Insertion[0], total_Times_row_Repeated_Insertion[1]
        , total_Times_row_Repeated_Insertion[2], total_Times_row_Repeated_Insertion[3]], 'b')
    plt.plot([10, 100, 1000, 10000], [total_Times_row_Repeated_Selection[0], total_Times_row_Repeated_Selection[1]
        , total_Times_row_Repeated_Selection[2], total_Times_row_Repeated_Selection[3]], 'g')
    plt.plot([10, 100, 1000, 10000], [total_Times_row_Repeated_Bubble[0], total_Times_row_Repeated_Bubble[1]
        , total_Times_row_Repeated_Bubble[2], total_Times_row_Repeated_Bubble[3]], 'm')
    plt.show()

def compareDecreasing1():
    total_Times_row_Repeated_Hire = [0] * 5
    no_of_comparison_Hire = [0] * 5
    no_of_exchangers_Hire = [0] * 5

    total_Times_row_Repeated_Insertion = [0] * 5
    no_of_comparison_Insertion = [0] * 5
    no_of_exchangers_Insertion = [0] * 5

    total_Times_row_Repeated_Selection = [0] * 5
    no_of_comparison_Selection = [0] * 5
    no_of_exchangers_Selection = [0] * 5

    total_Times_row_Repeated_Bubble = [0] * 5
    no_of_comparison_Bubble = [0] * 5
    no_of_exchangers_Bubble = [0] * 5

    total_Times_row_Repeated_Merge = [0] * 5
    no_of_comparison_Merge = [0] * 5
    no_of_exchangers_Merge = [0] * 5

    # 10, 100, 1000, 10000, 50000

    n = 10
    index = 0

    arrayHire = createArrayDecreasingOrder(n)
    arrayInsertion = arrayHire.copy()
    arraySelection = arrayHire.copy()
    arrayBubble = arrayHire.copy()
    arrayMerge = arrayHire.copy()

    print("\nN=", n)
    print("Array:", arrayHire)

    sortedArrayHire, total_Times_row_Repeated_Hire[index], no_of_comparison_Hire[index], no_of_exchangers_Hire[
        index] = hireAssistant(arrayHire)

    sortedArrayInsertion, total_Times_row_Repeated_Insertion[index], no_of_comparison_Insertion[index], \
    no_of_exchangers_Insertion[index] = insertionSort(arrayInsertion)

    sortedArraySelection, total_Times_row_Repeated_Selection[index], no_of_comparison_Selection[index], \
    no_of_exchangers_Selection[index] = selectionSort(arraySelection)

    sortedArrayBubble, total_Times_row_Repeated_Bubble[index], no_of_comparison_Bubble[index], no_of_exchangers_Bubble[
        index] = bubbleSort(arrayBubble)

    sortedArrayMerge, total_Times_row_Repeated_Merge[index], no_of_comparison_Merge[index], no_of_exchangers_Merge[
        index] = mergeSort(arrayMerge, 0, len(arrayMerge)-1)

    print("Hire:", sortedArrayHire, " ", total_Times_row_Repeated_Hire[index], " ", no_of_comparison_Hire[index], " ",
          no_of_exchangers_Hire[index], " ")
    print("Insertion:", sortedArrayInsertion, " ", total_Times_row_Repeated_Insertion[index], " ",
          no_of_comparison_Insertion[index], " ", no_of_exchangers_Insertion[index], " ")
    print("Selection:", sortedArraySelection, " ", total_Times_row_Repeated_Selection[index], " ",
          no_of_comparison_Selection[index], " ", no_of_exchangers_Selection[index], " ")
    print("Bubble:", sortedArrayBubble, " ", total_Times_row_Repeated_Bubble[index], " ",
          no_of_comparison_Bubble[index], " ", no_of_exchangers_Bubble[index], " ")
    print("Merge:", sortedArrayMerge, " ", total_Times_row_Repeated_Merge[index], " ",
          no_of_comparison_Merge[index], " ", no_of_exchangers_Merge[index], " ")

    arrayHire.clear()
    arrayInsertion.clear()
    arraySelection.clear()
    arrayBubble.clear()
    arrayMerge.clear()
    sortedArrayHire.clear()
    sortedArrayInsertion.clear()
    sortedArraySelection.clear()
    sortedArrayBubble.clear()
    sortedArrayMerge.clear()

    # 100
    n = 100
    index = 1

    arrayHire = createArrayDecreasingOrder(n)
    arrayInsertion = arrayHire.copy()
    arraySelection = arrayHire.copy()
    arrayBubble = arrayHire.copy()
    arrayMerge = arrayHire.copy()

    print("\nN=", n)
    print("Array:", arrayHire)

    sortedArrayHire, total_Times_row_Repeated_Hire[index], no_of_comparison_Hire[index], no_of_exchangers_Hire[
        index] = hireAssistant(arrayHire)

    sortedArrayInsertion, total_Times_row_Repeated_Insertion[index], no_of_comparison_Insertion[index], \
    no_of_exchangers_Insertion[index] = insertionSort(arrayInsertion)

    sortedArraySelection, total_Times_row_Repeated_Selection[index], no_of_comparison_Selection[index], \
    no_of_exchangers_Selection[index] = selectionSort(arraySelection)

    sortedArrayBubble, total_Times_row_Repeated_Bubble[index], no_of_comparison_Bubble[index], no_of_exchangers_Bubble[
        index] = bubbleSort(arrayBubble)

    sortedArrayMerge, total_Times_row_Repeated_Merge[index], no_of_comparison_Merge[index], no_of_exchangers_Merge[
        index] = mergeSort(arrayMerge, 0, len(arrayMerge)-1)

    print("Hire:", sortedArrayHire, "\n", total_Times_row_Repeated_Hire[1], " ", no_of_comparison_Hire[1], " ",
          no_of_exchangers_Hire[1], " ")
    print("Insertion:", sortedArrayInsertion, "\n", total_Times_row_Repeated_Insertion[1], " ",
          no_of_comparison_Insertion[1], " ", no_of_exchangers_Insertion[1], " ")
    print("Selection:", sortedArraySelection, "\n", total_Times_row_Repeated_Selection[1], " ",
          no_of_comparison_Selection[1], " ", no_of_exchangers_Selection[1], " ")
    print("Bubble:", sortedArrayBubble, "\n", total_Times_row_Repeated_Bubble[1], " ", no_of_comparison_Bubble[1], " ",
          no_of_exchangers_Bubble[1], " ")
    print("Merge:", sortedArrayMerge, " ", total_Times_row_Repeated_Merge[index], " ",
          no_of_comparison_Merge[index], " ", no_of_exchangers_Merge[index], " ")

    arrayHire.clear()
    arrayInsertion.clear()
    arraySelection.clear()
    arrayBubble.clear()
    arrayMerge.clear()
    sortedArrayHire.clear()
    sortedArrayInsertion.clear()
    sortedArraySelection.clear()
    sortedArrayBubble.clear()
    sortedArrayMerge.clear()

    # 1000
    n = 1000
    index = 2

    arrayHire = createArrayDecreasingOrder(n)
    arrayInsertion = arrayHire.copy()
    arraySelection = arrayHire.copy()
    arrayBubble = arrayHire.copy()
    arrayMerge = arrayHire.copy()

    print("\nN=", n)
    print("Array:", arrayHire)

    sortedArrayHire, total_Times_row_Repeated_Hire[index], no_of_comparison_Hire[index], no_of_exchangers_Hire[
        index] = hireAssistant(arrayHire)

    sortedArrayInsertion, total_Times_row_Repeated_Insertion[index], no_of_comparison_Insertion[index], \
    no_of_exchangers_Insertion[index] = insertionSort(arrayInsertion)

    sortedArraySelection, total_Times_row_Repeated_Selection[index], no_of_comparison_Selection[index], \
    no_of_exchangers_Selection[index] = selectionSort(arraySelection)

    sortedArrayBubble, total_Times_row_Repeated_Bubble[index], no_of_comparison_Bubble[index], no_of_exchangers_Bubble[
        index] = bubbleSort(arrayBubble)

    sortedArrayMerge, total_Times_row_Repeated_Merge[index], no_of_comparison_Merge[index], no_of_exchangers_Merge[
        index] = mergeSort(arrayMerge, 0, len(arrayMerge)-1)

    print("Hire:", sortedArrayHire, "\n", total_Times_row_Repeated_Hire[index], " ", no_of_comparison_Hire[index], " ",
          no_of_exchangers_Hire[index], " ")
    print("Insertion:", sortedArrayInsertion, "\n", total_Times_row_Repeated_Insertion[index], " ",
          no_of_comparison_Insertion[index], " ", no_of_exchangers_Insertion[index], " ")
    print("Selection:", sortedArraySelection, "\n", total_Times_row_Repeated_Selection[index], " ",
          no_of_comparison_Selection[index], " ", no_of_exchangers_Selection[index], " ")
    print("Bubble:", sortedArrayBubble, "\n", total_Times_row_Repeated_Bubble[index], " ",
          no_of_comparison_Bubble[index], " ",
          no_of_exchangers_Bubble[index], " ")
    print("Merge:", sortedArrayMerge, " ", total_Times_row_Repeated_Merge[index], " ",
          no_of_comparison_Merge[index], " ", no_of_exchangers_Merge[index], " ")

    arrayHire.clear()
    arrayInsertion.clear()
    arraySelection.clear()
    arrayBubble.clear()
    arrayMerge.clear()
    sortedArrayHire.clear()
    sortedArrayInsertion.clear()
    sortedArraySelection.clear()
    sortedArrayBubble.clear()
    sortedArrayMerge.clear()

    # 10000
    n = 10000
    index = 3

    arrayHire = createArrayDecreasingOrder(n)
    arrayInsertion = arrayHire.copy()
    arraySelection = arrayHire.copy()
    arrayBubble = arrayHire.copy()
    arrayMerge = arrayHire.copy()

    print("\nN=", n)
    print("Array:", arrayHire)

    sortedArrayHire, total_Times_row_Repeated_Hire[index], no_of_comparison_Hire[index], no_of_exchangers_Hire[
        index] = hireAssistant(arrayHire)

    sortedArrayInsertion, total_Times_row_Repeated_Insertion[index], no_of_comparison_Insertion[index], \
    no_of_exchangers_Insertion[index] = insertionSort(arrayInsertion)

    sortedArraySelection, total_Times_row_Repeated_Selection[index], no_of_comparison_Selection[index], \
    no_of_exchangers_Selection[index] = selectionSort(arraySelection)

    sortedArrayBubble, total_Times_row_Repeated_Bubble[index], no_of_comparison_Bubble[index], no_of_exchangers_Bubble[
        index] = bubbleSort(arrayBubble)

    sortedArrayMerge, total_Times_row_Repeated_Merge[index], no_of_comparison_Merge[index], no_of_exchangers_Merge[
        index] = mergeSort(arrayMerge, 0, len(arrayMerge)-1)

    print("Hire:", sortedArrayHire, "\n", total_Times_row_Repeated_Hire[index], " ", no_of_comparison_Hire[index], " ",
          no_of_exchangers_Hire[index], " ")
    print("Insertion:", sortedArrayInsertion, "\n", total_Times_row_Repeated_Insertion[index], " ",
          no_of_comparison_Insertion[index], " ", no_of_exchangers_Insertion[index], " ")
    print("Selection:", sortedArraySelection, "\n", total_Times_row_Repeated_Selection[index], " ",
          no_of_comparison_Selection[index], " ", no_of_exchangers_Selection[index], " ")
    print("Bubble:", sortedArrayBubble, "\n", total_Times_row_Repeated_Bubble[index], " ",
          no_of_comparison_Bubble[index], " ",
          no_of_exchangers_Bubble[index], " ")
    print("Merge:", sortedArrayMerge, " ", total_Times_row_Repeated_Merge[index], " ",
          no_of_comparison_Merge[index], " ", no_of_exchangers_Merge[index], " ")

    arrayHire.clear()
    arrayInsertion.clear()
    arraySelection.clear()
    arrayBubble.clear()
    arrayMerge.clear()
    sortedArrayHire.clear()
    sortedArrayInsertion.clear()
    sortedArraySelection.clear()
    sortedArrayBubble.clear()
    sortedArrayMerge.clear()

    names = ['Hire', 'Insertion', 'Selection', 'Bubble', 'Merge']

    plt.figure(figsize=(15, 7))
    # n=10
    index = 0

    plt.subplot(4, 3, 1)
    plt.title('Total Number of\nRows Repeated')
    plt.ylabel('N=10')
    plt.bar(names, [total_Times_row_Repeated_Hire[index], total_Times_row_Repeated_Insertion[index],
                    total_Times_row_Repeated_Selection[index], total_Times_row_Repeated_Bubble[index], total_Times_row_Repeated_Merge[index]],
            color=['b', 'r', 'm', 'g', 'y'])
    plt.subplot(4, 3, 2)
    plt.title('Number of Comparisons')
    plt.bar(names, [no_of_comparison_Hire[index], no_of_comparison_Insertion[index],
                    no_of_comparison_Selection[index], no_of_comparison_Bubble[index], no_of_comparison_Merge[index]],
            color=['b', 'r', 'm', 'g', 'y'])
    plt.subplot(4, 3, 3)
    plt.title('Number of Exchanges')
    plt.bar(names, [no_of_exchangers_Hire[index], no_of_exchangers_Insertion[index],
                    no_of_exchangers_Selection[index], no_of_exchangers_Bubble[index],no_of_exchangers_Merge[index]],
    color=['b', 'r', 'm', 'g', 'y'])
    # n=100
    index = 1

    plt.subplot(4, 3, 4)
    plt.ylabel('N=100')
    plt.bar(names, [total_Times_row_Repeated_Hire[index], total_Times_row_Repeated_Insertion[index],
                    total_Times_row_Repeated_Selection[index], total_Times_row_Repeated_Bubble[index], total_Times_row_Repeated_Merge[index]],
            color=['b', 'r', 'm', 'g', 'y'])
    plt.subplot(4, 3, 5)
    plt.bar(names, [no_of_comparison_Hire[index], no_of_comparison_Insertion[index],
                    no_of_comparison_Selection[index], no_of_comparison_Bubble[index], no_of_comparison_Merge[index]],
            color=['b', 'r', 'm', 'g', 'y'])
    plt.subplot(4, 3, 6)
    plt.bar(names, [no_of_exchangers_Hire[index], no_of_exchangers_Insertion[index],
                    no_of_exchangers_Selection[index], no_of_exchangers_Bubble[index], no_of_exchangers_Merge[index]],
            color=['b', 'r', 'm', 'g', 'y'])
    # n=1000
    index = 2

    plt.subplot(4, 3, 7)
    plt.ylabel('N=1000')
    plt.bar(names, [total_Times_row_Repeated_Hire[index], total_Times_row_Repeated_Insertion[index],
                    total_Times_row_Repeated_Selection[index], total_Times_row_Repeated_Bubble[index], total_Times_row_Repeated_Merge[index]],
            color=['b', 'r', 'm', 'g', 'y'])
    plt.subplot(4, 3, 8)
    plt.bar(names, [no_of_comparison_Hire[index], no_of_comparison_Insertion[index],
                    no_of_comparison_Selection[index], no_of_comparison_Bubble[index], no_of_comparison_Merge[index]],
            color=['b', 'r', 'm', 'g', 'y'])
    plt.subplot(4, 3, 9)
    plt.bar(names, [no_of_exchangers_Hire[index], no_of_exchangers_Insertion[index],
                    no_of_exchangers_Selection[index], no_of_exchangers_Bubble[index], no_of_exchangers_Merge[index]],
            color=['b', 'r', 'm', 'g', 'y'])
    # n=10000
    index = 3

    plt.subplot(4, 3, 10)
    plt.ylabel('N=10000')
    plt.bar(names, [total_Times_row_Repeated_Hire[index], total_Times_row_Repeated_Insertion[index],
                    total_Times_row_Repeated_Selection[index], total_Times_row_Repeated_Bubble[index], total_Times_row_Repeated_Merge[index]],
            color=['b', 'r', 'm', 'g', 'y'])
    plt.subplot(4, 3, 11)
    plt.bar(names, [no_of_comparison_Hire[index], no_of_comparison_Insertion[index],
                    no_of_comparison_Selection[index], no_of_comparison_Bubble[index], no_of_comparison_Merge[index]],
            color=['b', 'r', 'm', 'g', 'y'])
    plt.subplot(4, 3, 12)
    plt.bar(names, [no_of_exchangers_Hire[index], no_of_exchangers_Insertion[index],
                    no_of_exchangers_Selection[index], no_of_exchangers_Bubble[index], no_of_exchangers_Merge[index]],
            color=['b', 'r', 'm', 'g', 'y'])

    plt.suptitle('Array Type: Decreasing', fontweight='bold')
    plt.show()


def compareRanzdomized():

    total_Times_row_Repeated_Hire = [0] * 5
    no_of_comparison_Hire = [0] * 5
    no_of_exchangers_Hire = [0] * 5

    total_Times_row_Repeated_Insertion = [0] * 5
    no_of_comparison_Insertion = [0] * 5
    no_of_exchangers_Insertion = [0] * 5

    total_Times_row_Repeated_Selection = [0] * 5
    no_of_comparison_Selection = [0] * 5
    no_of_exchangers_Selection = [0] * 5

    total_Times_row_Repeated_Bubble = [0] * 5
    no_of_comparison_Bubble = [0] * 5
    no_of_exchangers_Bubble = [0] * 5


    # 10, 100, 1000, 10000, 50000

    n = 10
    index = 0

    arrayHire = createArrayRandomizedOrder(n)
    arrayInsertion = arrayHire.copy()
    arraySelection = arrayHire.copy()
    arrayBubble = arrayHire.copy()

    print("\nN=", n)
    print("Array:", arrayHire)

    sortedArrayHire, total_Times_row_Repeated_Hire[index], no_of_comparison_Hire[index], no_of_exchangers_Hire[index] = hireAssistant(arrayHire)

    sortedArrayInsertion, total_Times_row_Repeated_Insertion[index], no_of_comparison_Insertion[index], no_of_exchangers_Insertion[index] = insertionSort(arrayInsertion)

    sortedArraySelection, total_Times_row_Repeated_Selection[index], no_of_comparison_Selection[index], no_of_exchangers_Selection[index] = selectionSort(arraySelection)

    sortedArrayBubble, total_Times_row_Repeated_Bubble[index], no_of_comparison_Bubble[index], no_of_exchangers_Bubble[index] = bubbleSort(arrayBubble)

    print("Hire:",sortedArrayHire," ",total_Times_row_Repeated_Hire[index], " ",no_of_comparison_Hire[index], " ",no_of_exchangers_Hire[index], " ")
    print("Insertion:",sortedArrayInsertion," ",total_Times_row_Repeated_Insertion[index], " ",no_of_comparison_Insertion[index], " ",no_of_exchangers_Insertion[index], " ")
    print("Selection:",sortedArraySelection," ",total_Times_row_Repeated_Selection[index], " ",no_of_comparison_Selection[index], " ",no_of_exchangers_Selection[index], " ")
    print("Bubble:",sortedArrayBubble," ",total_Times_row_Repeated_Bubble[index], " ",no_of_comparison_Bubble[index], " ",no_of_exchangers_Bubble[index], " ")
    #print(," ",, " ",, " ",, " ")

    arrayHire.clear()
    arrayInsertion.clear()
    arraySelection.clear()
    arrayBubble.clear()
    sortedArrayHire.clear()
    sortedArrayInsertion.clear()
    sortedArraySelection.clear()
    sortedArrayBubble.clear()

    # 100
    n = 100
    index = 1

    arrayHire = createArrayRandomizedOrder(n)
    arrayInsertion = arrayHire.copy()
    arraySelection = arrayHire.copy()
    arrayBubble = arrayHire.copy()

    print("\nN=", n)
    print("Array:", arrayHire)

    sortedArrayHire, total_Times_row_Repeated_Hire[index], no_of_comparison_Hire[index], no_of_exchangers_Hire[
        index] = hireAssistant(arrayHire)

    sortedArrayInsertion, total_Times_row_Repeated_Insertion[index], no_of_comparison_Insertion[index], \
    no_of_exchangers_Insertion[index] = insertionSort(arrayInsertion)

    sortedArraySelection, total_Times_row_Repeated_Selection[index], no_of_comparison_Selection[index], \
    no_of_exchangers_Selection[index] = selectionSort(arraySelection)

    sortedArrayBubble, total_Times_row_Repeated_Bubble[index], no_of_comparison_Bubble[index], no_of_exchangers_Bubble[
        index] = bubbleSort(arrayBubble)

    print("Hire:", sortedArrayHire, "\n", total_Times_row_Repeated_Hire[1], " ", no_of_comparison_Hire[1], " ",
          no_of_exchangers_Hire[1], " ")
    print("Insertion:", sortedArrayInsertion, "\n", total_Times_row_Repeated_Insertion[1], " ",
          no_of_comparison_Insertion[1], " ", no_of_exchangers_Insertion[1], " ")
    print("Selection:", sortedArraySelection, "\n", total_Times_row_Repeated_Selection[1], " ",
          no_of_comparison_Selection[1], " ", no_of_exchangers_Selection[1], " ")
    print("Bubble:", sortedArrayBubble, "\n", total_Times_row_Repeated_Bubble[1], " ", no_of_comparison_Bubble[1], " ",
          no_of_exchangers_Bubble[1], " ")
    # print(," ",, " ",, " ",, " ")

    arrayHire.clear()
    arrayInsertion.clear()
    arraySelection.clear()
    arrayBubble.clear()
    sortedArrayHire.clear()
    sortedArrayInsertion.clear()
    sortedArraySelection.clear()
    sortedArrayBubble.clear()

    # 1000
    n = 1000
    index = 2

    arrayHire = createArrayRandomizedOrder(n)
    arrayInsertion = arrayHire.copy()
    arraySelection = arrayHire.copy()
    arrayBubble = arrayHire.copy()

    print("\nN=", n)
    print("Array:", arrayHire)

    sortedArrayHire, total_Times_row_Repeated_Hire[index], no_of_comparison_Hire[index], no_of_exchangers_Hire[
        index] = hireAssistant(arrayHire)

    sortedArrayInsertion, total_Times_row_Repeated_Insertion[index], no_of_comparison_Insertion[index], \
    no_of_exchangers_Insertion[index] = insertionSort(arrayInsertion)

    sortedArraySelection, total_Times_row_Repeated_Selection[index], no_of_comparison_Selection[index], \
    no_of_exchangers_Selection[index] = selectionSort(arraySelection)

    sortedArrayBubble, total_Times_row_Repeated_Bubble[index], no_of_comparison_Bubble[index], no_of_exchangers_Bubble[
        index] = bubbleSort(arrayBubble)

    print("Hire:", sortedArrayHire, "\n", total_Times_row_Repeated_Hire[index], " ", no_of_comparison_Hire[index], " ",
          no_of_exchangers_Hire[index], " ")
    print("Insertion:", sortedArrayInsertion, "\n", total_Times_row_Repeated_Insertion[index], " ",
          no_of_comparison_Insertion[index], " ", no_of_exchangers_Insertion[index], " ")
    print("Selection:", sortedArraySelection, "\n", total_Times_row_Repeated_Selection[index], " ",
          no_of_comparison_Selection[index], " ", no_of_exchangers_Selection[index], " ")
    print("Bubble:", sortedArrayBubble, "\n", total_Times_row_Repeated_Bubble[index], " ", no_of_comparison_Bubble[index], " ",
          no_of_exchangers_Bubble[index], " ")
    # print(," ",, " ",, " ",, " ")

    arrayHire.clear()
    arrayInsertion.clear()
    arraySelection.clear()
    arrayBubble.clear()
    sortedArrayHire.clear()
    sortedArrayInsertion.clear()
    sortedArraySelection.clear()
    sortedArrayBubble.clear()

    # 10000
    n = 10000
    index = 3

    arrayHire = createArrayRandomizedOrder(n)
    arrayInsertion = arrayHire.copy()
    arraySelection = arrayHire.copy()
    arrayBubble = arrayHire.copy()

    print("\nN=", n)
    print("Array:", arrayHire)

    sortedArrayHire, total_Times_row_Repeated_Hire[index], no_of_comparison_Hire[index], no_of_exchangers_Hire[
        index] = hireAssistant(arrayHire)

    sortedArrayInsertion, total_Times_row_Repeated_Insertion[index], no_of_comparison_Insertion[index], \
    no_of_exchangers_Insertion[index] = insertionSort(arrayInsertion)

    sortedArraySelection, total_Times_row_Repeated_Selection[index], no_of_comparison_Selection[index], \
    no_of_exchangers_Selection[index] = selectionSort(arraySelection)

    sortedArrayBubble, total_Times_row_Repeated_Bubble[index], no_of_comparison_Bubble[index], no_of_exchangers_Bubble[
        index] = bubbleSort(arrayBubble)

    print("Hire:", sortedArrayHire, "\n", total_Times_row_Repeated_Hire[index], " ", no_of_comparison_Hire[index], " ",
          no_of_exchangers_Hire[index], " ")
    print("Insertion:", sortedArrayInsertion, "\n", total_Times_row_Repeated_Insertion[index], " ",
          no_of_comparison_Insertion[index], " ", no_of_exchangers_Insertion[index], " ")
    print("Selection:", sortedArraySelection, "\n", total_Times_row_Repeated_Selection[index], " ",
          no_of_comparison_Selection[index], " ", no_of_exchangers_Selection[index], " ")
    print("Bubble:", sortedArrayBubble, "\n", total_Times_row_Repeated_Bubble[index], " ", no_of_comparison_Bubble[index], " ",
          no_of_exchangers_Bubble[index], " ")
    # print(," ",, " ",, " ",, " ")

    arrayHire.clear()
    arrayInsertion.clear()
    arraySelection.clear()
    arrayBubble.clear()
    sortedArrayHire.clear()
    sortedArrayInsertion.clear()
    sortedArraySelection.clear()
    sortedArrayBubble.clear()

    plt.xlabel("Number of elements")
    plt.ylabel("Total Number of Rows Repeated")
    plt.plot([10, 100, 1000, 10000], [total_Times_row_Repeated_Hire[0], total_Times_row_Repeated_Hire[1]
        , total_Times_row_Repeated_Hire[2], total_Times_row_Repeated_Hire[3]], 'r')
    plt.plot([10, 100, 1000, 10000], [total_Times_row_Repeated_Insertion[0], total_Times_row_Repeated_Insertion[1]
        , total_Times_row_Repeated_Insertion[2], total_Times_row_Repeated_Insertion[3]], 'b')
    plt.plot([10, 100, 1000, 10000], [total_Times_row_Repeated_Selection[0], total_Times_row_Repeated_Selection[1]
        , total_Times_row_Repeated_Selection[2], total_Times_row_Repeated_Selection[3]], 'g')
    plt.plot([10, 100, 1000, 10000], [total_Times_row_Repeated_Bubble[0], total_Times_row_Repeated_Bubble[1]
        , total_Times_row_Repeated_Bubble[2], total_Times_row_Repeated_Bubble[3]], 'm')
    plt.show()

def compareRanzdomized1():
    total_Times_row_Repeated_Hire = [0] * 5
    no_of_comparison_Hire = [0] * 5
    no_of_exchangers_Hire = [0] * 5

    total_Times_row_Repeated_Insertion = [0] * 5
    no_of_comparison_Insertion = [0] * 5
    no_of_exchangers_Insertion = [0] * 5

    total_Times_row_Repeated_Selection = [0] * 5
    no_of_comparison_Selection = [0] * 5
    no_of_exchangers_Selection = [0] * 5

    total_Times_row_Repeated_Bubble = [0] * 5
    no_of_comparison_Bubble = [0] * 5
    no_of_exchangers_Bubble = [0] * 5

    total_Times_row_Repeated_Merge = [0] * 5
    no_of_comparison_Merge = [0] * 5
    no_of_exchangers_Merge = [0] * 5

    # 10, 100, 1000, 10000, 50000

    n = 10
    index = 0

    arrayHire = createArrayRandomizedOrder(n)
    arrayInsertion = arrayHire.copy()
    arraySelection = arrayHire.copy()
    arrayBubble = arrayHire.copy()
    arrayMerge = arrayHire.copy()

    print("\nN=", n)
    print("Array:", arrayHire)

    sortedArrayHire, total_Times_row_Repeated_Hire[index], no_of_comparison_Hire[index], no_of_exchangers_Hire[
        index] = hireAssistant(arrayHire)

    sortedArrayInsertion, total_Times_row_Repeated_Insertion[index], no_of_comparison_Insertion[index], \
    no_of_exchangers_Insertion[index] = insertionSort(arrayInsertion)

    sortedArraySelection, total_Times_row_Repeated_Selection[index], no_of_comparison_Selection[index], \
    no_of_exchangers_Selection[index] = selectionSort(arraySelection)

    sortedArrayBubble, total_Times_row_Repeated_Bubble[index], no_of_comparison_Bubble[index], no_of_exchangers_Bubble[
        index] = bubbleSort(arrayBubble)

    sortedArrayMerge, total_Times_row_Repeated_Merge[index], no_of_comparison_Merge[index], no_of_exchangers_Merge[
        index] = mergeSort(arrayMerge, 0, len(arrayMerge)-1)

    print("Hire:", sortedArrayHire, " ", total_Times_row_Repeated_Hire[index], " ", no_of_comparison_Hire[index], " ",
          no_of_exchangers_Hire[index], " ")
    print("Insertion:", sortedArrayInsertion, " ", total_Times_row_Repeated_Insertion[index], " ",
          no_of_comparison_Insertion[index], " ", no_of_exchangers_Insertion[index], " ")
    print("Selection:", sortedArraySelection, " ", total_Times_row_Repeated_Selection[index], " ",
          no_of_comparison_Selection[index], " ", no_of_exchangers_Selection[index], " ")
    print("Bubble:", sortedArrayBubble, " ", total_Times_row_Repeated_Bubble[index], " ",
          no_of_comparison_Bubble[index], " ", no_of_exchangers_Bubble[index], " ")
    print("Merge:", sortedArrayMerge, " ", total_Times_row_Repeated_Merge[index], " ",
          no_of_comparison_Merge[index], " ", no_of_exchangers_Merge[index], " ")

    arrayHire.clear()
    arrayInsertion.clear()
    arraySelection.clear()
    arrayBubble.clear()
    arrayMerge.clear()
    sortedArrayHire.clear()
    sortedArrayInsertion.clear()
    sortedArraySelection.clear()
    sortedArrayBubble.clear()
    sortedArrayMerge.clear()

    # 100
    n = 100
    index = 1

    arrayHire = createArrayRandomizedOrder(n)
    arrayInsertion = arrayHire.copy()
    arraySelection = arrayHire.copy()
    arrayBubble = arrayHire.copy()
    arrayMerge = arrayHire.copy()

    print("\nN=", n)
    print("Array:", arrayHire)

    sortedArrayHire, total_Times_row_Repeated_Hire[index], no_of_comparison_Hire[index], no_of_exchangers_Hire[
        index] = hireAssistant(arrayHire)

    sortedArrayInsertion, total_Times_row_Repeated_Insertion[index], no_of_comparison_Insertion[index], \
    no_of_exchangers_Insertion[index] = insertionSort(arrayInsertion)

    sortedArraySelection, total_Times_row_Repeated_Selection[index], no_of_comparison_Selection[index], \
    no_of_exchangers_Selection[index] = selectionSort(arraySelection)

    sortedArrayBubble, total_Times_row_Repeated_Bubble[index], no_of_comparison_Bubble[index], no_of_exchangers_Bubble[
        index] = bubbleSort(arrayBubble)

    sortedArrayMerge, total_Times_row_Repeated_Merge[index], no_of_comparison_Merge[index], no_of_exchangers_Merge[
        index] = mergeSort(arrayMerge, 0, len(arrayMerge)-1)

    print("Hire:", sortedArrayHire, "\n", total_Times_row_Repeated_Hire[1], " ", no_of_comparison_Hire[1], " ",
          no_of_exchangers_Hire[1], " ")
    print("Insertion:", sortedArrayInsertion, "\n", total_Times_row_Repeated_Insertion[1], " ",
          no_of_comparison_Insertion[1], " ", no_of_exchangers_Insertion[1], " ")
    print("Selection:", sortedArraySelection, "\n", total_Times_row_Repeated_Selection[1], " ",
          no_of_comparison_Selection[1], " ", no_of_exchangers_Selection[1], " ")
    print("Bubble:", sortedArrayBubble, "\n", total_Times_row_Repeated_Bubble[1], " ", no_of_comparison_Bubble[1], " ",
          no_of_exchangers_Bubble[1], " ")
    print("Merge:", sortedArrayMerge, " ", total_Times_row_Repeated_Merge[index], " ",
          no_of_comparison_Merge[index], " ", no_of_exchangers_Merge[index], " ")

    arrayHire.clear()
    arrayInsertion.clear()
    arraySelection.clear()
    arrayBubble.clear()
    arrayMerge.clear()
    sortedArrayHire.clear()
    sortedArrayInsertion.clear()
    sortedArraySelection.clear()
    sortedArrayBubble.clear()
    sortedArrayMerge.clear()

    # 1000
    n = 1000
    index = 2

    arrayHire = createArrayRandomizedOrder(n)
    arrayInsertion = arrayHire.copy()
    arraySelection = arrayHire.copy()
    arrayBubble = arrayHire.copy()
    arrayMerge = arrayHire.copy()

    print("\nN=", n)
    print("Array:", arrayHire)

    sortedArrayHire, total_Times_row_Repeated_Hire[index], no_of_comparison_Hire[index], no_of_exchangers_Hire[
        index] = hireAssistant(arrayHire)

    sortedArrayInsertion, total_Times_row_Repeated_Insertion[index], no_of_comparison_Insertion[index], \
    no_of_exchangers_Insertion[index] = insertionSort(arrayInsertion)

    sortedArraySelection, total_Times_row_Repeated_Selection[index], no_of_comparison_Selection[index], \
    no_of_exchangers_Selection[index] = selectionSort(arraySelection)

    sortedArrayBubble, total_Times_row_Repeated_Bubble[index], no_of_comparison_Bubble[index], no_of_exchangers_Bubble[
        index] = bubbleSort(arrayBubble)

    sortedArrayMerge, total_Times_row_Repeated_Merge[index], no_of_comparison_Merge[index], no_of_exchangers_Merge[
        index] = mergeSort(arrayMerge, 0, len(arrayMerge)-1)

    print("Hire:", sortedArrayHire, "\n", total_Times_row_Repeated_Hire[index], " ", no_of_comparison_Hire[index], " ",
          no_of_exchangers_Hire[index], " ")
    print("Insertion:", sortedArrayInsertion, "\n", total_Times_row_Repeated_Insertion[index], " ",
          no_of_comparison_Insertion[index], " ", no_of_exchangers_Insertion[index], " ")
    print("Selection:", sortedArraySelection, "\n", total_Times_row_Repeated_Selection[index], " ",
          no_of_comparison_Selection[index], " ", no_of_exchangers_Selection[index], " ")
    print("Bubble:", sortedArrayBubble, "\n", total_Times_row_Repeated_Bubble[index], " ",
          no_of_comparison_Bubble[index], " ",
          no_of_exchangers_Bubble[index], " ")
    print("Merge:", sortedArrayMerge, " ", total_Times_row_Repeated_Merge[index], " ",
          no_of_comparison_Merge[index], " ", no_of_exchangers_Merge[index], " ")

    arrayHire.clear()
    arrayInsertion.clear()
    arraySelection.clear()
    arrayBubble.clear()
    arrayMerge.clear()
    sortedArrayHire.clear()
    sortedArrayInsertion.clear()
    sortedArraySelection.clear()
    sortedArrayBubble.clear()
    sortedArrayMerge.clear()

    # 10000
    n = 10000
    index = 3

    arrayHire = createArrayRandomizedOrder(n)
    arrayInsertion = arrayHire.copy()
    arraySelection = arrayHire.copy()
    arrayBubble = arrayHire.copy()
    arrayMerge = arrayHire.copy()

    print("\nN=", n)
    print("Array:", arrayHire)

    sortedArrayHire, total_Times_row_Repeated_Hire[index], no_of_comparison_Hire[index], no_of_exchangers_Hire[
        index] = hireAssistant(arrayHire)

    sortedArrayInsertion, total_Times_row_Repeated_Insertion[index], no_of_comparison_Insertion[index], \
    no_of_exchangers_Insertion[index] = insertionSort(arrayInsertion)

    sortedArraySelection, total_Times_row_Repeated_Selection[index], no_of_comparison_Selection[index], \
    no_of_exchangers_Selection[index] = selectionSort(arraySelection)

    sortedArrayBubble, total_Times_row_Repeated_Bubble[index], no_of_comparison_Bubble[index], no_of_exchangers_Bubble[
        index] = bubbleSort(arrayBubble)

    sortedArrayMerge, total_Times_row_Repeated_Merge[index], no_of_comparison_Merge[index], no_of_exchangers_Merge[
        index] = mergeSort(arrayMerge, 0, len(arrayMerge)-1)

    print("Hire:", sortedArrayHire, "\n", total_Times_row_Repeated_Hire[index], " ", no_of_comparison_Hire[index], " ",
          no_of_exchangers_Hire[index], " ")
    print("Insertion:", sortedArrayInsertion, "\n", total_Times_row_Repeated_Insertion[index], " ",
          no_of_comparison_Insertion[index], " ", no_of_exchangers_Insertion[index], " ")
    print("Selection:", sortedArraySelection, "\n", total_Times_row_Repeated_Selection[index], " ",
          no_of_comparison_Selection[index], " ", no_of_exchangers_Selection[index], " ")
    print("Bubble:", sortedArrayBubble, "\n", total_Times_row_Repeated_Bubble[index], " ",
          no_of_comparison_Bubble[index], " ",
          no_of_exchangers_Bubble[index], " ")
    print("Merge:", sortedArrayMerge, " ", total_Times_row_Repeated_Merge[index], " ",
          no_of_comparison_Merge[index], " ", no_of_exchangers_Merge[index], " ")

    arrayHire.clear()
    arrayInsertion.clear()
    arraySelection.clear()
    arrayBubble.clear()
    arrayMerge.clear()
    sortedArrayHire.clear()
    sortedArrayInsertion.clear()
    sortedArraySelection.clear()
    sortedArrayBubble.clear()
    sortedArrayMerge.clear()

    names = ['Hire', 'Insertion', 'Selection', 'Bubble', 'Merge']

    plt.figure(figsize=(15, 7))
    # n=10
    index = 0

    plt.subplot(4, 3, 1)
    plt.title('Total Number of\nRows Repeated')
    plt.ylabel('N=10')
    plt.bar(names, [total_Times_row_Repeated_Hire[index], total_Times_row_Repeated_Insertion[index],
                    total_Times_row_Repeated_Selection[index], total_Times_row_Repeated_Bubble[index], total_Times_row_Repeated_Merge[index]],
            color=['b', 'r', 'm', 'g', 'y'])
    plt.subplot(4, 3, 2)
    plt.title('Number of Comparisons')
    plt.bar(names, [no_of_comparison_Hire[index], no_of_comparison_Insertion[index],
                    no_of_comparison_Selection[index], no_of_comparison_Bubble[index], no_of_comparison_Merge[index]],
            color=['b', 'r', 'm', 'g', 'y'])
    plt.subplot(4, 3, 3)
    plt.title('Number of Exchanges')
    plt.bar(names, [no_of_exchangers_Hire[index], no_of_exchangers_Insertion[index],
                    no_of_exchangers_Selection[index], no_of_exchangers_Bubble[index],no_of_exchangers_Merge[index]],
    color=['b', 'r', 'm', 'g', 'y'])
    # n=100
    index = 1

    plt.subplot(4, 3, 4)
    plt.ylabel('N=100')
    plt.bar(names, [total_Times_row_Repeated_Hire[index], total_Times_row_Repeated_Insertion[index],
                    total_Times_row_Repeated_Selection[index], total_Times_row_Repeated_Bubble[index], total_Times_row_Repeated_Merge[index]],
            color=['b', 'r', 'm', 'g', 'y'])
    plt.subplot(4, 3, 5)
    plt.bar(names, [no_of_comparison_Hire[index], no_of_comparison_Insertion[index],
                    no_of_comparison_Selection[index], no_of_comparison_Bubble[index], no_of_comparison_Merge[index]],
            color=['b', 'r', 'm', 'g', 'y'])
    plt.subplot(4, 3, 6)
    plt.bar(names, [no_of_exchangers_Hire[index], no_of_exchangers_Insertion[index],
                    no_of_exchangers_Selection[index], no_of_exchangers_Bubble[index], no_of_exchangers_Merge[index]],
            color=['b', 'r', 'm', 'g', 'y'])
    # n=1000
    index = 2

    plt.subplot(4, 3, 7)
    plt.ylabel('N=1000')
    plt.bar(names, [total_Times_row_Repeated_Hire[index], total_Times_row_Repeated_Insertion[index],
                    total_Times_row_Repeated_Selection[index], total_Times_row_Repeated_Bubble[index], total_Times_row_Repeated_Merge[index]],
            color=['b', 'r', 'm', 'g', 'y'])
    plt.subplot(4, 3, 8)
    plt.bar(names, [no_of_comparison_Hire[index], no_of_comparison_Insertion[index],
                    no_of_comparison_Selection[index], no_of_comparison_Bubble[index], no_of_comparison_Merge[index]],
            color=['b', 'r', 'm', 'g', 'y'])
    plt.subplot(4, 3, 9)
    plt.bar(names, [no_of_exchangers_Hire[index], no_of_exchangers_Insertion[index],
                    no_of_exchangers_Selection[index], no_of_exchangers_Bubble[index], no_of_exchangers_Merge[index]],
            color=['b', 'r', 'm', 'g', 'y'])
    # n=10000
    index = 3

    plt.subplot(4, 3, 10)
    plt.ylabel('N=10000')
    plt.bar(names, [total_Times_row_Repeated_Hire[index], total_Times_row_Repeated_Insertion[index],
                    total_Times_row_Repeated_Selection[index], total_Times_row_Repeated_Bubble[index], total_Times_row_Repeated_Merge[index]],
            color=['b', 'r', 'm', 'g', 'y'])
    plt.subplot(4, 3, 11)
    plt.bar(names, [no_of_comparison_Hire[index], no_of_comparison_Insertion[index],
                    no_of_comparison_Selection[index], no_of_comparison_Bubble[index], no_of_comparison_Merge[index]],
            color=['b', 'r', 'm', 'g', 'y'])
    plt.subplot(4, 3, 12)
    plt.bar(names, [no_of_exchangers_Hire[index], no_of_exchangers_Insertion[index],
                    no_of_exchangers_Selection[index], no_of_exchangers_Bubble[index], no_of_exchangers_Merge[index]],
            color=['b', 'r', 'm', 'g', 'y'])

    plt.suptitle('Array Type: Randomized', fontweight='bold')
    plt.show()


def compareArrayTypes(n):
    arrayIncreased = createArrayIncreasingOrder(n)
    arrayDecreased = createArrayDecreasingOrder(n)
    arrayRandomized = createArrayRandomizedOrder(n)
    tempArray = []

    total_Times_row_Repeated_Hire = [0] * 5
    no_of_comparison_Hire = [0] * 5
    no_of_exchangers_Hire = [0] * 5

    total_Times_row_Repeated_Insertion = [0] * 5
    no_of_comparison_Insertion = [0] * 5
    no_of_exchangers_Insertion = [0] * 5

    total_Times_row_Repeated_Selection = [0] * 5
    no_of_comparison_Selection = [0] * 5
    no_of_exchangers_Selection = [0] * 5

    total_Times_row_Repeated_Bubble = [0] * 5
    no_of_comparison_Bubble = [0] * 5
    no_of_exchangers_Bubble = [0] * 5

    total_Times_row_Repeated_Merge = [0] * 5
    no_of_comparison_Merge = [0] * 5
    no_of_exchangers_Merge = [0] * 5

    #Increasing Array
    index = 0

    tempArray = arrayIncreased.copy()
    sortedArrayHire, total_Times_row_Repeated_Hire[index], no_of_comparison_Hire[index], no_of_exchangers_Hire[index] = hireAssistant(tempArray)
    tempArray.clear()

    tempArray = arrayIncreased.copy()
    sortedArrayInsertion, total_Times_row_Repeated_Insertion[index], no_of_comparison_Insertion[index], no_of_exchangers_Insertion[index] = insertionSort(tempArray)
    tempArray.clear()

    tempArray = arrayIncreased.copy()
    sortedArraySelection, total_Times_row_Repeated_Selection[index], no_of_comparison_Selection[index], no_of_exchangers_Selection[index] = selectionSort(tempArray)
    tempArray.clear()

    tempArray = arrayIncreased.copy()
    sortedArrayBubble, total_Times_row_Repeated_Bubble[index], no_of_comparison_Bubble[index], no_of_exchangers_Bubble[index] =bubbleSort(tempArray)
    tempArray.clear()

    tempArray = arrayIncreased.copy()
    sortedArrayMerge, total_Times_row_Repeated_Merge[index], no_of_comparison_Merge[index], no_of_exchangers_Merge[index] = mergeSort(tempArray, 0, len(tempArray)-1)
    tempArray.clear()

    sortedArrayHire.clear()
    sortedArrayInsertion.clear()
    sortedArraySelection.clear()
    sortedArrayBubble.clear()
    sortedArrayMerge.clear()

    #Decreasing Array
    index = 1

    tempArray = arrayDecreased.copy()
    sortedArrayHire, total_Times_row_Repeated_Hire[index], no_of_comparison_Hire[index], no_of_exchangers_Hire[
        index] = hireAssistant(tempArray)
    tempArray.clear()

    tempArray = arrayDecreased.copy()
    sortedArrayInsertion, total_Times_row_Repeated_Insertion[index], no_of_comparison_Insertion[index], \
    no_of_exchangers_Insertion[index] = insertionSort(tempArray)
    tempArray.clear()

    tempArray = arrayDecreased.copy()
    sortedArraySelection, total_Times_row_Repeated_Selection[index], no_of_comparison_Selection[index], \
    no_of_exchangers_Selection[index] = selectionSort(tempArray)
    tempArray.clear()

    tempArray = arrayDecreased.copy()
    sortedArrayBubble, total_Times_row_Repeated_Bubble[index], no_of_comparison_Bubble[index], no_of_exchangers_Bubble[
        index] = bubbleSort(tempArray)
    tempArray.clear()

    tempArray = arrayDecreased.copy()
    sortedArrayMerge, total_Times_row_Repeated_Merge[index], no_of_comparison_Merge[index], no_of_exchangers_Merge[
        index] = mergeSort(tempArray, 0, len(tempArray) - 1)
    tempArray.clear()

    sortedArrayHire.clear()
    sortedArrayInsertion.clear()
    sortedArraySelection.clear()
    sortedArrayBubble.clear()
    sortedArrayMerge.clear()

    #Randomized Array
    index = 2

    tempArray = arrayRandomized.copy()
    sortedArrayHire, total_Times_row_Repeated_Hire[index], no_of_comparison_Hire[index], no_of_exchangers_Hire[
        index] = hireAssistant(tempArray)
    tempArray.clear()

    tempArray = arrayRandomized.copy()
    sortedArrayInsertion, total_Times_row_Repeated_Insertion[index], no_of_comparison_Insertion[index], \
    no_of_exchangers_Insertion[index] = insertionSort(tempArray)
    tempArray.clear()

    tempArray = arrayRandomized.copy()
    sortedArraySelection, total_Times_row_Repeated_Selection[index], no_of_comparison_Selection[index], \
    no_of_exchangers_Selection[index] = selectionSort(tempArray)
    tempArray.clear()

    tempArray = arrayRandomized.copy()
    sortedArrayBubble, total_Times_row_Repeated_Bubble[index], no_of_comparison_Bubble[index], no_of_exchangers_Bubble[
        index] = bubbleSort(tempArray)
    tempArray.clear()

    tempArray = arrayRandomized.copy()
    sortedArrayMerge, total_Times_row_Repeated_Merge[index], no_of_comparison_Merge[index], no_of_exchangers_Merge[
        index] = mergeSort(tempArray, 0, len(tempArray) - 1)
    tempArray.clear()


    names = ['Hire', 'Insertion', 'Selection', 'Bubble', 'Merge']

    plt.figure(figsize=(15, 6))

    # Increasing Array
    index = 0
    plt.subplot(3, 3, 1)
    plt.title('Total Number of\nRows Repeated')
    plt.ylabel('Increasing\nArray', fontweight='bold')
    plt.bar(names, [total_Times_row_Repeated_Hire[index], total_Times_row_Repeated_Insertion[index],
                    total_Times_row_Repeated_Selection[index], total_Times_row_Repeated_Bubble[index],
                    total_Times_row_Repeated_Merge[index]],
            color=['b', 'r', 'm', 'g', 'y'])
    plt.subplot(3, 3, 2)
    plt.title('Number of Comparisons')
    plt.bar(names, [no_of_comparison_Hire[index], no_of_comparison_Insertion[index],
                    no_of_comparison_Selection[index], no_of_comparison_Bubble[index], no_of_comparison_Merge[index]],
            color=['b', 'r', 'm', 'g', 'y'])
    plt.subplot(3, 3, 3)
    plt.title('Number of Exchanges')
    plt.bar(names, [no_of_exchangers_Hire[index], no_of_exchangers_Insertion[index],
                    no_of_exchangers_Selection[index], no_of_exchangers_Bubble[index], no_of_exchangers_Merge[index]],
            color=['b', 'r', 'm', 'g', 'y'])

    # Decreasing Array
    index = 1
    plt.subplot(3, 3, 4)
    plt.ylabel('Decreasing\nArray', fontweight='bold')
    plt.bar(names, [total_Times_row_Repeated_Hire[index], total_Times_row_Repeated_Insertion[index],
                    total_Times_row_Repeated_Selection[index], total_Times_row_Repeated_Bubble[index],
                    total_Times_row_Repeated_Merge[index]],
            color=['b', 'r', 'm', 'g', 'y'])
    plt.subplot(3, 3, 5)
    plt.bar(names, [no_of_comparison_Hire[index], no_of_comparison_Insertion[index],
                    no_of_comparison_Selection[index], no_of_comparison_Bubble[index], no_of_comparison_Merge[index]],
            color=['b', 'r', 'm', 'g', 'y'])
    plt.subplot(3, 3, 6)
    plt.bar(names, [no_of_exchangers_Hire[index], no_of_exchangers_Insertion[index],
                    no_of_exchangers_Selection[index], no_of_exchangers_Bubble[index], no_of_exchangers_Merge[index]],
            color=['b', 'r', 'm', 'g', 'y'])

    # Randomized Array
    index = 2
    plt.subplot(3, 3, 7)
    plt.ylabel('Randomized\nArray', fontweight='bold')
    plt.bar(names, [total_Times_row_Repeated_Hire[index], total_Times_row_Repeated_Insertion[index],
                    total_Times_row_Repeated_Selection[index], total_Times_row_Repeated_Bubble[index],
                    total_Times_row_Repeated_Merge[index]],
            color=['b', 'r', 'm', 'g', 'y'])
    plt.subplot(3, 3, 8)
    plt.bar(names, [no_of_comparison_Hire[index], no_of_comparison_Insertion[index],
                    no_of_comparison_Selection[index], no_of_comparison_Bubble[index], no_of_comparison_Merge[index]],
            color=['b', 'r', 'm', 'g', 'y'])
    plt.subplot(3, 3, 9)
    plt.bar(names, [no_of_exchangers_Hire[index], no_of_exchangers_Insertion[index],
                    no_of_exchangers_Selection[index], no_of_exchangers_Bubble[index], no_of_exchangers_Merge[index]],
            color=['b', 'r', 'm', 'g', 'y'])

    title = 'Number of elements: ' + str(n)
    plt.suptitle(title, fontweight='bold')
    #plt.switch_backend('TkAgg')
    plt.show()




if __name__ == '__main__':

    print("Welcome to Array and Algorithm Comparing Program")
    while(True):
        print()
        print("What dou you want to compare?(Type 1 or 2 or 3)")
        print("1. Different Number of Array Types")
        print("2. Different Number of Elements")
        print("3. Exit")
        user = input()
        if(user == "1"):
            print("How many elements you want to compare?")
            user = input()
            compareArrayTypes(int(user))
        elif(user == "2"):
            print("Which Array type?(Type 1 or 2 or 3)")
            print("1. Increasing Array")
            print("2. Decreasing Array")
            print("3. Randomized Array")
            user = input()
            if (user == "1"):
                compareIncreasing1()
            elif (user == "2"):
                compareDecreasing1()
            elif (user == "3"):
                compareRanzdomized1()
        elif user == "3":
            break
        else:
            print("IT IS NOT A VALID INPUT!")



