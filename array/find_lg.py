arr =[3,89,45,2,99,1,5]
n = len(arr)
max_value = arr[0]
for i in range(1, n):
    if arr[i] > max_value:
        max_value = arr[i]
print(max_value, end=" ")