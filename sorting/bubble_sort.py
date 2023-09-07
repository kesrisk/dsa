def bsort(arr):

    i = len(arr) - 1
    while i > 0:

        j = 0
        while j < i:
            if arr[j] > arr[j+1]:
                # swap these values 
                arr[j], arr[j+1] = arr[j+1], arr[j]
            j += 1
        i -= 1

# bubble out largest element in the end
arr = [12, 11, 13, 5, 6, 7]
bsort(arr)
print(arr)