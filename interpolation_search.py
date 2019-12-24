def interpolation_search(arr, num):
    lower_idx = 0
    upper_idx = len(arr) - 1
    idx = -1
    if num > arr[-1] or num < arr[0]:
        return idx
    while idx == -1:
        if lower_idx >= upper_idx or arr[lower_idx] >= arr[upper_idx]:
            return idx
        middle_idx = lower_idx + int((upper_idx - lower_idx) * (num - arr[lower_idx])/(arr[upper_idx] - arr[lower_idx]))
        print(middle_idx, arr[middle_idx])
        if arr[middle_idx] == num:
            return middle_idx
        else:
            if arr[middle_idx] < num:
                lower_idx = middle_idx + 1
            else:
                upper_idx = middle_idx -1

if __name__ == '__main__':
    arr = [1,2,3,4,6,7,8,11,14,16,17,24,26,35,48,59,67]
    num = 48
    print(interpolation_search(arr, num))
