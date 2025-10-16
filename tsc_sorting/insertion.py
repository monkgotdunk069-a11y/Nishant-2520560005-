arr=[33,89,45,2,99,1,5]
n=len(arr)
for i in range(1,n):
    j = i
    while j>0 and arr[j]<arr[j-1]:# j>0 Ensures we haven't reached the start of the array
        temp = arr[j-1]
        arr[j-1]=arr[j]
        arr[j]=temp
        j=j-1 
        #Decrements $j$ to move one position to the left, 
        #continuingthe comparison and shifting/swapping with the next element in the sorted portion.
for i in range(n):
    print(arr[i],end=" ")