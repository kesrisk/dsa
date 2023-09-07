def ssort(arr):


    i = 0

    while i < len(arr):

        # find min
        current_min_indec = i
        k = i + 1
        while k < len(arr):
            if arr[k] < arr[current_min_indec]:
                current_min_indec = k
            k+=1
        
        # swap index i and k
        arr[i], arr[current_min_indec] = arr[current_min_indec], arr[i]
        i+=1

# swap min with current counter
arr = [12, 11, 13, 5, 6, 7]
ssort(arr)
print(arr)