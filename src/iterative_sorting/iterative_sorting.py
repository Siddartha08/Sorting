# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 

        for j in range(i+1, len(arr)):
            if arr[smallest_index] > arr[j]:
                smallest_index = j
        
      

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    # position = 0
    # length = len(arr)

    # for i in range(len(arr) -1,0,1 ):
    #     for j in range(i):
    #         tempVal = arr[j]
    #         arr[j] = arr[j + 1]
    #         arr[j + 1] = tempVal
    # missing a loop around this. 
    length = len(arr)
    for i in range(arr):
        if arr[i] > arr[i + 1]:
            tempVal = arr[i + 1]
            arr[i + 1] = arr[i]
            arr[i] = tempVal

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr