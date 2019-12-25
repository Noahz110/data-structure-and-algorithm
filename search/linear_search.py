def linear_search(arr, num):
    idx = -1
    for i in range(0, len(arr)):
        if arr[i] == num:
            idx = i
            return idx
    return idx

if __name__ == '__main__':
    arr = [1,23,4,5,6,7,3,67,43,22,13]
    num = 6
    print(linear_search(arr, num))
