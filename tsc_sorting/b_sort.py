#sorting_1
arr = [ 2, 9, 1, 5, 6]
high = len(arr)
low=0
key = int(input("Enter the key: "))
mid = low + (high - low) // 2
for i in range(len(arr)):
    if arr[mid] == key:
        print("Element found at index", mid)
        break
    elif arr[mid] < key:
        low = mid + 1
    elif arr[mid] > key:
        high = mid - 1
    mid = low + (high - low) // 2
else:
    print("Element not found in the array")