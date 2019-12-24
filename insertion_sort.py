def insertion_sort(arr):
    for i in range(1,len(arr)):
        position = i
        value_to_insert = arr[i]
        print(position, value_to_insert)
        while position > 0 and value_to_insert < arr[position-1]:
            arr[position] = arr[position - 1]
            position -= 1
        arr[position] = value_to_insert
        print('i', arr)
    return arr

if __name__ == '__main__':
    arr = [1,5,2,7,8,4,9,3,0,6]
    print(arr)
    print(insertion_sort(arr))
