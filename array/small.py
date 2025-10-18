arr=[23,44,12,5,67,34]
n = len(arr)
min_value = arr[0]
for i in range(1, n):
    if arr[i] < min_value: #compare each element with the current minimum
        min_value = arr[i] #swap if current element is smaller
print(min_value, end=" ")