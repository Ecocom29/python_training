def rotateLeft(d, array):
    for i in range(d):
        temp = arr[0]
        for j in range(len(arr)-1):
            arr[j] = arr[j+1]
        arr[len(arr)-1] = temp
    return array


arr = [1, 2, 3, 4, 5]

print(arr)

print(rotateLeft(54, arr))
