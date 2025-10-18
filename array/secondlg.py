arr=[22,23,45,67,89,12]
n = len(arr)
max_value = arr[0]
second_largest = arr[-1]
for i in range(1, n):
   if arr[i] > max_value: #compare each element with the current maximum
      max_value = arr[i] #swap if current element is greater
print(max_value, end=" ")
for j in range(n):
   if arr[j] > second_largest and arr[j] != max_value:
         second_largest = arr[j]
print(second_largest, end=" ")