arr=[10,23,42,56,78,89]
sorttt=sorted(arr)
half_len=len(sorttt)//2
first_half=sorttt[:half_len]#slicing the first half from index 0 to half length
second_half=sorttt[half_len:]#slicing the second half from half length to end
arr2=second_half[::-1]#reversing the second half
arr3=first_half+arr2
print("Combined array:",arr3)