def radix_sort(arr):
    # Find the maximum number to determine the number of digits
    max_num = max(arr)
    
    # Calculate the number of digits in the maximum number
    num_digits = len(str(max_num))
    
    # Initialize 10 buckets (0 to 9) for each digit place value
    buckets = [[] for _ in range(10)]
    
    # Loop through each digit place, from the rightmost to the leftmost
    for digit_place in range(1, num_digits + 1):
        # Distribute elements into buckets based on the current digit place
        for num in arr:
            # Extract the current digit from the number
            digit = (num // 10**(digit_place - 1)) % 10
            buckets[digit].append(num)
        
        # Reconstruct the array by concatenating elements from all buckets
        arr = []
        for bucket in buckets:
            arr.extend(bucket)
        
        # Clear the buckets for the next iteration
        buckets = [[] for _ in range(10)]
    
    return arr
