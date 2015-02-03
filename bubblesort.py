arr = [7,9,5,8,2,6]
for i in range(0, len(arr) - 1):
        swap_test = False
        for j in range(0, len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # swap
            swap_test = True
        if swap_test == False:
            break
print arr