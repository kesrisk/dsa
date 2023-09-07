def c_sort(arr):

    na = [0,0,0,0,0,0,0,0,0,0]
    # count occurance of each element we can use arr to save these number
    for i in arr:
        na[i] = na[i] + 1
    
    # find ending array cell of each element by adding previous space with next space
    i = 1
    while i < len(na):
        na[i] = na[i-1] + na[i]
        i+=1
    
    # find index of starting of each element, now we can find this by seeing ending of each element, 
    # end of last elemet would be starting of next element, so we can just shif one cell forward and keep inital as 0

    j = len(na) - 1
    while j > 0:
        na[j] = na[j-1]
        j-=1
    na[0] = 0

    # now na has starting index of all the elements present in arr, also as we sort elements of arr in new arr
    # we'll increase index in na array of that particular element

    final_arr = [0 for _ in arr]
    for k in arr:
        ind = na[k]
        # get index of current element and increase index count in na array
        na[k] += 1
        final_arr[ind] = k

    return final_arr

    

    


# https://www.youtube.com/watch?v=OKd534EWcdk
# find index of starting of all the elemets and then based on index just add it into a new array
# Application - we can use if we have to find starting index of an element, or we need to sort some elements having same 
# params and we need to preserve order of the values

# suppose numbers are from 0 to 9
arr = [0,1,3,2,0,4,8,9,1,2,5,5,4]
print(c_sort(arr))
