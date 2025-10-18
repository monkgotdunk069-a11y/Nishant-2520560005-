def quick(arr,low,high):
    if low < high :
        pi = partition(arr,low,high)

        quick(arr, low, pi-1)#recursive call on the left of pivot and pivot is at correct position 
        quick(arr, pi+1, high)#recursive call on the right of pivot and pivot is at correct position
def partition(arr, low, high):#function to find the pivot element and place it at the correct position
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):#traverse through all elements
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i] # swap arr[i] and arr[j]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]#swap arr[i+1] and arr[high]
    return i + 1

if __name__ == "__main__":
    arr = [10, 7, 8, 9, 1, 5]
    quick(arr, 0, len(arr)-1)#calling quick sort function and passing the array, low index and high index
    print(arr)





