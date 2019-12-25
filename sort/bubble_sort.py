def bubble_sort(arr):
    n = len(arr)
    swapped = False
    for i in range(0, n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
                swapped = True
        if not swapped:
            print('array is already sorted')
            return arr
    return arr

if __name__ == '__main__':
    arr = [0,1,2,3,4,5,6,7,8,9]
    print(bubble_sort(arr))
