def isort(arr):

    i = 1
    while i < len(arr):
        j = i - 1
        temp = arr[i]
        while j >= 0  and arr[j] > temp:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j+1] = temp


        i +=  1

# move smaller element to first
arr = [12, 11, 13, 5, 6, 7]
isort(arr)
print(arr)
