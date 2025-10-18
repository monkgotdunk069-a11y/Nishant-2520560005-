#repeatedly steps through the list, compares adjacent elements and swaps them if they are in the wrong order
def bs(arr,n):
    for i in range(n):# Traverse through all array elements n-1 
        for j in range(0,n-i-1):#upto n-2
            if arr[j]>arr[j+1]:#swap if the element found is greate than the next element 
                tem = arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=tem
    for i in range(n):
        print(arr[i],end=" ")
    
if __name__ == "__main__":
    arr=[64,34,25,12,22,11,90]
    n=len(arr)
    bs(arr,n)
