def binary_search(arr, num):
    indx = -1
    lower_point = 0
    upper_point = len(arr) - 1
    while lower_point <= upper_point:
        middle_point = lower_point + int((upper_point - lower_point)/2)
        if arr[middle_point] == num:
            indx = middle_point
            return indx
        elif arr[middle_point] < num:
            lower_point = middle_point + 1
        else:
            upper_point = middle_point - 1
    return indx
if __name__ == '__main__':
    arr = [1,3,4,6,7,8,11,13,15,16,19,34,37,30,48,59,60,62,69]
    num = 62
    print(binary_search(arr, num))
