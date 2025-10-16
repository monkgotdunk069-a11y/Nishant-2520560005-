arr=[2,34,9,16,5,1,8]
n=len(arr)
for i in range(n):
    mini=i
    for j in range(i+1,n):
        if arr[j]<arr[mini]:
            mini=j
    temp = arr[mini]
    arr[mini]=arr[i]
    arr[i]=temp
for i in range(n):
    print(arr[i],end=" ")
