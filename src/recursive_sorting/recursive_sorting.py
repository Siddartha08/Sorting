# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    # merged_arr = [0] * elements
    merged_arr = arrA + arrB
    # TO-DO
    # merged_arr = arrA.join(arrB)
    # merged_arr = arrA + arrB
    print(merged_arr)
    merged_arr.sort()
    print(merged_arr)
    return merged_arr

arr = [1,2,3,4,5]
arr2 = [9,8,7,6]
merge(arr, arr2)
# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    if len(arr) == 0 or len(arr) ==1:
        return arr
    else:
        length = len(arr)
        half = int(length)/2

        firstHalf = merge_sort(arr[:int(half)])
        secondHalf = merge_sort(arr[int(half):])
        return merge(firstHalf, secondHalf)

    return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr


# def foo(n):
#     if n == 0:
#         return

#     print(n)

#     foo(n - 1)