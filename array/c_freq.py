arr = [10, 20, 10, 40, 20, 30, 10]
n = len(arr)
counted_elements = [] # To store elements whose frequency has already been printed

for i in range(n):
    # Check if we've already counted and printed the frequency for this element
    if arr[i] not in counted_elements:
        count = 0
        # Inner loop to find the frequency of arr[i] in the whole array
        for j in range(n):
            if arr[i] == arr[j]:
                count += 1
        
        print(f"Frequency of {arr[i]} is: {count}")
        counted_elements.append(arr[i])  # Mark this element as counted