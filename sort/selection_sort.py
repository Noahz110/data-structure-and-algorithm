def selection_sort(arr):
    for i in range(0,len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j]:
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp
        print(arr)
    return arr

if __name__ == '__main__':
    arr = [3,1,2,7,9,5,6,8,4,5,6]
    print(arr)
    print(selection_sort(arr))
