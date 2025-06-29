# 30 Array/List Programming Challenges in Python

## 1. Find Maximum Element (Easy)

**Problem:** Find the maximum element in an array.

**Sample Input:** `[3, 7, 2, 9, 1]`  
**Sample Output:** `9`

```python
def find_maximum(arr):
    """
    Time Complexity: O(n) where n is the length of array
    Space Complexity: O(1) constant space

    Explanation:
    - Initialize max with first element (handle empty array)
    - Iterate through array once
    - Update max when larger element found
    - Built-in max() also runs in O(n) time
    """
    if not arr:
        return None

    max_element = arr[0]
    for num in arr[1:]:
        if num > max_element:
            max_element = num

    return max_element

# Alternative using built-in
def find_maximum_v2(arr):
    return max(arr) if arr else None

# Test
print(find_maximum([3, 7, 2, 9, 1]))  # Output: 9
print(find_maximum([-5, -2, -8]))     # Output: -2
```

## 2. Two Sum (Easy)

**Problem:** Find two numbers that add up to target and return their indices.

**Sample Input:** `nums = [2, 7, 11, 15], target = 9`  
**Sample Output:** `[0, 1]`

```python
def two_sum(nums, target):
    """
    Time Complexity: O(n) where n is the length of array
    Space Complexity: O(n) for hash map

    Explanation:
    - Use hash map to store seen numbers and their indices
    - For each number, check if complement exists
    - Complement = target - current number
    - Return indices when pair found
    - Single pass solution
    """
    seen = {}  # value -> index

    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i

    return []  # No solution found

# Test
print(two_sum([2, 7, 11, 15], 9))  # Output: [0, 1]
print(two_sum([3, 2, 4], 6))       # Output: [1, 2]
```

## 3. Remove Duplicates from Sorted Array (Easy)

**Problem:** Remove duplicates in-place and return new length.

**Sample Input:** `[1, 1, 2, 2, 3]`  
**Sample Output:** `3, array = [1, 2, 3, _, _]`

```python
def remove_duplicates(nums):
    """
    Time Complexity: O(n) where n is the length of array
    Space Complexity: O(1) in-place modification

    Explanation:
    - Use two pointers: write position and read position
    - Write pointer tracks position for next unique element
    - Skip duplicates by comparing with previous
    - Array is sorted, so duplicates are consecutive
    - Return new length
    """
    if not nums:
        return 0

    write_pos = 1  # Position to write next unique element

    for read_pos in range(1, len(nums)):
        if nums[read_pos] != nums[read_pos - 1]:
            nums[write_pos] = nums[read_pos]
            write_pos += 1

    return write_pos

# Test
nums = [1, 1, 2, 2, 3]
length = remove_duplicates(nums)
print(f"Length: {length}, Array: {nums[:length]}")  # Output: Length: 3, Array: [1, 2, 3]
```

## 4. Rotate Array (Medium)

**Problem:** Rotate array to the right by k steps.

**Sample Input:** `nums = [1, 2, 3, 4, 5], k = 2`  
**Sample Output:** `[4, 5, 1, 2, 3]`

```python
def rotate_array(nums, k):
    """
    Time Complexity: O(n) where n is the length of array
    Space Complexity: O(1) in-place rotation

    Explanation:
    - Use reversal algorithm for O(1) space
    - Normalize k to handle k > n cases
    - Reverse entire array
    - Reverse first k elements
    - Reverse remaining elements
    - Example: [1,2,3,4,5], k=2
      -> [5,4,3,2,1] -> [4,5,3,2,1] -> [4,5,1,2,3]
    """
    n = len(nums)
    k = k % n  # Handle k > n

    def reverse(start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

    # Three reversal steps
    reverse(0, n - 1)      # Reverse entire array
    reverse(0, k - 1)      # Reverse first k elements
    reverse(k, n - 1)      # Reverse remaining elements

# Test
nums = [1, 2, 3, 4, 5]
rotate_array(nums, 2)
print(nums)  # Output: [4, 5, 1, 2, 3]
```

## 5. Find Missing Number (Easy)

**Problem:** Find missing number from 0 to n.

**Sample Input:** `[3, 0, 1]`  
**Sample Output:** `2`

```python
def find_missing_number(nums):
    """
    Time Complexity: O(n) where n is the length of array
    Space Complexity: O(1) constant space

    Explanation:
    - Use mathematical formula: sum(0 to n) = n*(n+1)/2
    - Missing number = expected sum - actual sum
    - Alternative: XOR all numbers (a^a = 0)
    - Handles edge cases efficiently
    """
    n = len(nums)
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    return expected_sum - actual_sum

# Alternative using XOR
def find_missing_number_xor(nums):
    """
    XOR properties: a^a = 0, a^0 = a
    XOR all indices and numbers, missing number remains
    """
    missing = len(nums)
    for i, num in enumerate(nums):
        missing ^= i ^ num
    return missing

# Test
print(find_missing_number([3, 0, 1]))      # Output: 2
print(find_missing_number([0, 1]))         # Output: 2
print(find_missing_number_xor([9,6,4,2,3,5,7,0,1]))  # Output: 8
```

## 6. Maximum Subarray Sum (Medium)

**Problem:** Find the contiguous subarray with maximum sum (Kadane's Algorithm).

**Sample Input:** `[-2, 1, -3, 4, -1, 2, 1, -5, 4]`  
**Sample Output:** `6` (subarray [4, -1, 2, 1])

```python
def max_subarray_sum(nums):
    """
    Time Complexity: O(n) where n is the length of array
    Space Complexity: O(1) constant space

    Explanation:
    - Kadane's Algorithm: dynamic programming approach
    - Track maximum sum ending at each position
    - Either extend previous subarray or start new
    - Keep global maximum throughout
    - Handles all negative numbers correctly
    """
    if not nums:
        return 0

    max_current = max_global = nums[0]

    for num in nums[1:]:
        # Either extend existing subarray or start new
        max_current = max(num, max_current + num)
        # Update global maximum
        max_global = max(max_global, max_current)

    return max_global

# Version that returns indices
def max_subarray_sum_with_indices(nums):
    """Returns sum and indices of maximum subarray"""
    if not nums:
        return 0, -1, -1

    max_current = max_global = nums[0]
    start = end = temp_start = 0

    for i in range(1, len(nums)):
        if nums[i] > max_current + nums[i]:
            max_current = nums[i]
            temp_start = i
        else:
            max_current += nums[i]

        if max_current > max_global:
            max_global = max_current
            start = temp_start
            end = i

    return max_global, start, end

# Test
print(max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # Output: 6
sum_val, start, end = max_subarray_sum_with_indices([-2, 1, -3, 4, -1, 2, 1, -5, 4])
print(f"Sum: {sum_val}, Indices: [{start}, {end}]")  # Sum: 6, Indices: [3, 6]
```

## 7. Merge Two Sorted Arrays (Easy)

**Problem:** Merge two sorted arrays into one sorted array.

**Sample Input:** `arr1 = [1, 3, 5], arr2 = [2, 4, 6]`  
**Sample Output:** `[1, 2, 3, 4, 5, 6]`

```python
def merge_sorted_arrays(arr1, arr2):
    """
    Time Complexity: O(m + n) where m, n are lengths of arrays
    Space Complexity: O(m + n) for result array

    Explanation:
    - Use two pointers, one for each array
    - Compare elements at pointers
    - Add smaller element to result
    - Handle remaining elements after one array exhausted
    - Maintains sorted order throughout
    """
    result = []
    i = j = 0

    # Merge while both arrays have elements
    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1

    # Add remaining elements
    result.extend(arr1[i:])
    result.extend(arr2[j:])

    return result

# In-place merge for arr1 with extra space at end
def merge_in_place(arr1, m, arr2, n):
    """Merge arr2 into arr1 which has space for both"""
    # Start from the end
    i = m - 1
    j = n - 1
    k = m + n - 1

    while i >= 0 and j >= 0:
        if arr1[i] > arr2[j]:
            arr1[k] = arr1[i]
            i -= 1
        else:
            arr1[k] = arr2[j]
            j -= 1
        k -= 1

    # Copy remaining from arr2
    while j >= 0:
        arr1[k] = arr2[j]
        j -= 1
        k -= 1

# Test
print(merge_sorted_arrays([1, 3, 5], [2, 4, 6]))  # Output: [1, 2, 3, 4, 5, 6]
```

## 8. Find Duplicate Number (Medium)

**Problem:** Find the duplicate in array containing n+1 integers from 1 to n.

**Sample Input:** `[1, 3, 4, 2, 2]`  
**Sample Output:** `2`

```python
def find_duplicate(nums):
    """
    Time Complexity: O(n) where n is the length of array
    Space Complexity: O(1) constant space

    Explanation:
    - Floyd's Cycle Detection (Tortoise and Hare)
    - Treat array as linked list: index -> value
    - Duplicate creates a cycle
    - Find cycle start point = duplicate number
    - Phase 1: Detect cycle exists
    - Phase 2: Find cycle entry point
    """
    # Phase 1: Find intersection point
    slow = fast = nums[0]

    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break

    # Phase 2: Find entrance to cycle
    slow = nums[0]
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]

    return slow

# Alternative using array modification
def find_duplicate_v2(nums):
    """Mark visited by negating value at index"""
    for num in nums:
        idx = abs(num)
        if nums[idx] < 0:
            return idx
        nums[idx] = -nums[idx]

# Test
print(find_duplicate([1, 3, 4, 2, 2]))  # Output: 2
print(find_duplicate([3, 1, 3, 4, 2]))  # Output: 3
```

## 9. Product of Array Except Self (Medium)

**Problem:** Return array where each element is product of all except itself.

**Sample Input:** `[1, 2, 3, 4]`  
**Sample Output:** `[24, 12, 8, 6]`

```python
def product_except_self(nums):
    """
    Time Complexity: O(n) where n is the length of array
    Space Complexity: O(1) excluding output array

    Explanation:
    - Cannot use division (handle zeros)
    - Use two passes: left products and right products
    - First pass: product of all elements to the left
    - Second pass: multiply by product of elements to right
    - result[i] = left_product[i] * right_product[i]
    """
    n = len(nums)
    result = [1] * n

    # First pass: left products
    left_product = 1
    for i in range(n):
        result[i] = left_product
        left_product *= nums[i]

    # Second pass: right products
    right_product = 1
    for i in range(n - 1, -1, -1):
        result[i] *= right_product
        right_product *= nums[i]

    return result

# Test
print(product_except_self([1, 2, 3, 4]))  # Output: [24, 12, 8, 6]
print(product_except_self([-1, 1, 0, -3, 3]))  # Output: [0, 0, 9, 0, 0]
```

## 10. Find Peak Element (Medium)

**Problem:** Find a peak element (greater than neighbors).

**Sample Input:** `[1, 2, 1, 3, 5, 6, 4]`  
**Sample Output:** `5` (index of peak element 6)

```python
def find_peak_element(nums):
    """
    Time Complexity: O(log n) where n is the length of array
    Space Complexity: O(1) constant space

    Explanation:
    - Use binary search for O(log n) solution
    - Peak exists because nums[-1] = nums[n] = -∞
    - If mid < mid+1, peak exists on right
    - If mid > mid+1, peak exists on left (including mid)
    - Always move towards larger element
    """
    left, right = 0, len(nums) - 1

    while left < right:
        mid = (left + right) // 2

        if nums[mid] < nums[mid + 1]:
            # Peak is on the right
            left = mid + 1
        else:
            # Peak is on the left or at mid
            right = mid

    return left

# Linear search version O(n)
def find_peak_element_linear(nums):
    """Find first element greater than next"""
    for i in range(len(nums) - 1):
        if nums[i] > nums[i + 1]:
            return i
    return len(nums) - 1

# Test
print(find_peak_element([1, 2, 1, 3, 5, 6, 4]))  # Output: 5
print(find_peak_element([1, 2, 3, 1]))           # Output: 2
```

## 11. Container With Most Water (Medium)

**Problem:** Find two lines that form container with most water.

**Sample Input:** `[1, 8, 6, 2, 5, 4, 8, 3, 7]`  
**Sample Output:** `49`

```python
def max_water_container(height):
    """
    Time Complexity: O(n) where n is the length of array
    Space Complexity: O(1) constant space

    Explanation:
    - Two pointer approach from both ends
    - Area = width * min(left_height, right_height)
    - Move pointer with smaller height inward
    - Why? Moving larger height can't increase area
    - Track maximum area throughout
    """
    left, right = 0, len(height) - 1
    max_area = 0

    while left < right:
        # Calculate current area
        width = right - left
        current_area = width * min(height[left], height[right])
        max_area = max(max_area, current_area)

        # Move pointer with smaller height
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_area

# Test
print(max_water_container([1, 8, 6, 2, 5, 4, 8, 3, 7]))  # Output: 49
print(max_water_container([1, 1]))                       # Output: 1
```

## 12. 3Sum (Medium)

**Problem:** Find all unique triplets that sum to zero.

**Sample Input:** `[-1, 0, 1, 2, -1, -4]`  
**Sample Output:** `[[-1, -1, 2], [-1, 0, 1]]`

```python
def three_sum(nums):
    """
    Time Complexity: O(n²) where n is the length of array
    Space Complexity: O(k) where k is number of triplets

    Explanation:
    - Sort array first for two-pointer technique
    - Fix first element, find two sum for remaining
    - Skip duplicates to ensure unique triplets
    - Use two pointers for efficient search
    - Move pointers based on sum comparison
    """
    nums.sort()
    result = []
    n = len(nums)

    for i in range(n - 2):
        # Skip duplicate for first element
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        # Two pointers for remaining elements
        left, right = i + 1, n - 1

        while left < right:
            total = nums[i] + nums[left] + nums[right]

            if total == 0:
                result.append([nums[i], nums[left], nums[right]])

                # Skip duplicates
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1

                left += 1
                right -= 1
            elif total < 0:
                left += 1
            else:
                right -= 1

    return result

# Test
print(three_sum([-1, 0, 1, 2, -1, -4]))  # Output: [[-1, -1, 2], [-1, 0, 1]]
print(three_sum([0, 0, 0]))              # Output: [[0, 0, 0]]
```

## 13. Move Zeros (Easy)

**Problem:** Move all zeros to end while maintaining order of non-zero elements.

**Sample Input:** `[0, 1, 0, 3, 12]`  
**Sample Output:** `[1, 3, 12, 0, 0]`

```python
def move_zeros(nums):
    """
    Time Complexity: O(n) where n is the length of array
    Space Complexity: O(1) in-place modification

    Explanation:
    - Two pointer approach: write position and read position
    - Write pointer tracks where to place next non-zero
    - Skip zeros during iteration
    - Fill remaining positions with zeros
    - Maintains relative order of non-zero elements
    """
    write_pos = 0

    # Move non-zero elements to front
    for read_pos in range(len(nums)):
        if nums[read_pos] != 0:
            nums[write_pos] = nums[read_pos]
            write_pos += 1

    # Fill remaining with zeros
    while write_pos < len(nums):
        nums[write_pos] = 0
        write_pos += 1

    return nums

# Alternative: Swap approach
def move_zeros_v2(nums):
    """Swap non-zero with first zero position"""
    zero_pos = 0

    for i in range(len(nums)):
        if nums[i] != 0:
            nums[i], nums[zero_pos] = nums[zero_pos], nums[i]
            zero_pos += 1

    return nums

# Test
print(move_zeros([0, 1, 0, 3, 12]))  # Output: [1, 3, 12, 0, 0]
print(move_zeros([0, 0, 1]))         # Output: [1, 0, 0]
```

## 14. Search in Rotated Sorted Array (Medium)

**Problem:** Search target in rotated sorted array.

**Sample Input:** `nums = [4, 5, 6, 7, 0, 1, 2], target = 0`  
**Sample Output:** `4`

```python
def search_rotated(nums, target):
    """
    Time Complexity: O(log n) where n is the length of array
    Space Complexity: O(1) constant space

    Explanation:
    - Modified binary search
    - Identify which half is properly sorted
    - Check if target lies in sorted half
    - Adjust search space accordingly
    - Handle rotation point carefully
    """
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid

        # Check which half is sorted
        if nums[left] <= nums[mid]:
            # Left half is sorted
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            # Right half is sorted
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1

    return -1

# Test
print(search_rotated([4, 5, 6, 7, 0, 1, 2], 0))  # Output: 4
print(search_rotated([4, 5, 6, 7, 0, 1, 2], 3))  # Output: -1
```

## 15. Next Permutation (Medium)

**Problem:** Find next lexicographically greater permutation.

**Sample Input:** `[1, 2, 3]`  
**Sample Output:** `[1, 3, 2]`

```python
def next_permutation(nums):
    """
    Time Complexity: O(n) where n is the length of array
    Space Complexity: O(1) in-place modification

    Explanation:
    - Find rightmost pair where nums[i] < nums[i+1]
    - Find smallest element > nums[i] in right portion
    - Swap them
    - Reverse the right portion
    - If no such pair, array is in descending order
    - Return reverse (smallest permutation)
    """
    n = len(nums)

    # Find first decreasing element from right
    i = n - 2
    while i >= 0 and nums[i] >= nums[i + 1]:
        i -= 1

    if i >= 0:
        # Find element just larger than nums[i]
        j = n - 1
        while nums[j] <= nums[i]:
            j -= 1
        # Swap
        nums[i], nums[j] = nums[j], nums[i]

    # Reverse the right portion
    left, right = i + 1, n - 1
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1

    return nums

# Test
print(next_permutation([1, 2, 3]))  # Output: [1, 3, 2]
print(next_permutation([3, 2, 1]))  # Output: [1, 2, 3]
print(next_permutation([1, 1, 5]))  # Output: [1, 5, 1]
```

## 16. Subarray Sum Equals K (Medium)

**Problem:** Count subarrays with sum equal to k.

**Sample Input:** `nums = [1, 1, 1], k = 2`  
**Sample Output:** `2`

```python
def subarray_sum(nums, k):
    """
    Time Complexity: O(n) where n is the length of array
    Space Complexity: O(n) for hash map

    Explanation:
    - Use prefix sum and hash map
    - If cumsum - k exists in map, found subarray
    - Count all such subarrays
    - Handle case where subarray starts from index 0
    - prefix_sum[j] - prefix_sum[i] = k means sum(i+1, j) = k
    """
    count = 0
    cumsum = 0
    sum_freq = {0: 1}  # Empty prefix

    for num in nums:
        cumsum += num

        # Check if cumsum - k exists
        if cumsum - k in sum_freq:
            count += sum_freq[cumsum - k]

        # Add current sum to map
        sum_freq[cumsum] = sum_freq.get(cumsum, 0) + 1

    return count

# Test
print(subarray_sum([1, 1, 1], 2))     # Output: 2
print(subarray_sum([1, 2, 3], 3))     # Output: 2
```

## 17. Spiral Matrix (Medium)

**Problem:** Return elements of matrix in spiral order.

**Sample Input:** `[[1,2,3],[4,5,6],[7,8,9]]`  
**Sample Output:** `[1,2,3,6,9,8,7,4,5]`

```python
def spiral_order(matrix):
    """
    Time Complexity: O(m*n) where m, n are dimensions
    Space Complexity: O(1) excluding output

    Explanation:
    - Use four boundaries: top, bottom, left, right
    - Traverse in spiral: right, down, left, up
    - Shrink boundaries after each direction
    - Stop when boundaries cross
    - Handle edge cases (single row/column)
    """
    if not matrix or not matrix[0]:
        return []

    result = []
    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1

    while top <= bottom and left <= right:
        # Move right
        for col in range(left, right + 1):
            result.append(matrix[top][col])
        top += 1

        # Move down
        for row in range(top, bottom + 1):
            result.append(matrix[row][right])
        right -= 1

        # Move left (if row exists)
        if top <= bottom:
            for col in range(right, left - 1, -1):
                result.append(matrix[bottom][col])
            bottom -= 1

        # Move up (if column exists)
        if left <= right:
            for row in range(bottom, top - 1, -1):
                result.append(matrix[row][left])
            left += 1

    return result

# Test
matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(spiral_order(matrix))  # Output: [1,2,3,6,9,8,7,4,5]
```

## 18. Set Matrix Zeros (Medium)

**Problem:** If element is 0, set entire row and column to 0.

**Sample Input:** `[[1,1,1],[1,0,1],[1,1,1]]`  
**Sample Output:** `[[1,0,1],[0,0,0],[1,0,1]]`

```python
def set_zeros(matrix):
    """
    Time Complexity: O(m*n) where m, n are dimensions
    Space Complexity: O(1) constant space

    Explanation:
    - Use first row and column as markers
    - Track if first row/column have zeros separately
    - Mark zeros in first row/column
    - Use markers to set zeros
    - Handle first row/column last
    """
    if not matrix:
        return

    m, n = len(matrix), len(matrix[0])
    first_row_zero = any(matrix[0][j] == 0 for j in range(n))
    first_col_zero = any(matrix[i][0] == 0 for i in range(m))

    # Mark zeros in first row/column
    for i in range(1, m):
        for j in range(1, n):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0

    # Set zeros based on markers
    for i in range(1, m):
        for j in range(1, n):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0

    # Handle first row
    if first_row_zero:
        for j in range(n):
            matrix[0][j] = 0

    # Handle first column
    if first_col_zero:
        for i in range(m):
            matrix[i][0] = 0

# Test
matrix = [[1,1,1],[1,0,1],[1,1,1]]
set_zeros(matrix)
print(matrix)  # Output: [[1,0,1],[0,0,0],[1,0,1]]
```

## 19. Longest Consecutive Sequence (Hard)

**Problem:** Find length of longest consecutive sequence.

**Sample Input:** `[100, 4, 200, 1, 3, 2]`  
**Sample Output:** `4` (sequence [1, 2, 3, 4])

```python
def longest_consecutive(nums):
    """
    Time Complexity: O(n) where n is the length of array
    Space Complexity: O(n) for set

    Explanation:
    - Use set for O(1) lookups
    - For each number, check if it's sequence start
    - Number is start if (num - 1) not in set
    - Count consecutive numbers from start
    - Track maximum length
    - Each number visited at most twice
    """
    if not nums:
        return 0

    num_set = set(nums)
    max_length = 0

    for num in num_set:
        # Check if it's the start of a sequence
        if num - 1 not in num_set:
            current_num = num
            current_length = 1

            # Count consecutive numbers
            while current_num + 1 in num_set:
                current_num += 1
                current_length += 1

            max_length = max(max_length, current_length)

    return max_length

# Test
print(longest_consecutive([100, 4, 200, 1, 3, 2]))  # Output: 4
print(longest_consecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))  # Output: 9
```

## 20. Trapping Rain Water (Hard)

**Problem:** Calculate water trapped after raining.

**Sample Input:** `[0,1,0,2,1,0,1,3,2,1,2,1]`  
**Sample Output:** `6`

```python
def trap_water(height):
    """
    Time Complexity: O(n) where n is the length of array
    Space Complexity: O(1) constant space

    Explanation:
    - Two pointer approach from both ends
    - Water level determined by smaller of max heights
    - Track max height seen from left and right
    - Add water when current height < water level
    - Move pointer with smaller max height
    """
    if not height:
        return 0

    left, right = 0, len(height) - 1
    left_max = right_max = 0
    water = 0

    while left < right:
        if height[left] < height[right]:
            if height[left] >= left_max:
                left_max = height[left]
            else:
                water += left_max - height[left]
            left += 1
        else:
            if height[right] >= right_max:
                right_max = height[right]
            else:
                water += right_max - height[right]
            right -= 1

    return water

# Alternative using arrays
def trap_water_v2(height):
    """Using left and right max arrays"""
    n = len(height)
    if n < 3:
        return 0

    left_max = [0] * n
    right_max = [0] * n

    left_max[0] = height[0]
    for i in range(1, n):
        left_max[i] = max(left_max[i-1], height[i])

    right_max[n-1] = height[n-1]
    for i in range(n-2, -1, -1):
        right_max[i] = max(right_max[i+1], height[i])

    water = 0
    for i in range(n):
        water += min(left_max[i], right_max[i]) - height[i]

    return water

# Test
print(trap_water([0,1,0,2,1,0,1,3,2,1,2,1]))  # Output: 6
print(trap_water([4,2,0,3,2,5]))              # Output: 9
```

## 21. Find All Duplicates (Medium)

**Problem:** Find all elements appearing twice in array of 1 to n.

**Sample Input:** `[4,3,2,7,8,2,3,1]`  
**Sample Output:** `[2,3]`

```python
def find_duplicates(nums):
    """
    Time Complexity: O(n) where n is the length of array
    Space Complexity: O(1) excluding output

    Explanation:
    - Use array itself as hash map
    - For each number, mark nums[abs(num)-1] as negative
    - If already negative, number is duplicate
    - Values are 1 to n, so can use as indices
    - Restore array if needed
    """
    duplicates = []

    for num in nums:
        index = abs(num) - 1

        if nums[index] < 0:
            duplicates.append(abs(num))
        else:
            nums[index] = -nums[index]

    # Restore array (optional)
    for i in range(len(nums)):
        nums[i] = abs(nums[i])

    return duplicates

# Test
print(find_duplicates([4,3,2,7,8,2,3,1]))  # Output: [2,3]
print(find_duplicates([1,1,2]))            # Output: [1]
```

## 22. Sliding Window Maximum (Hard)

**Problem:** Find maximum in each sliding window of size k.

**Sample Input:** `nums = [1,3,-1,-3,5,3,6,7], k = 3`  
**Sample Output:** `[3,3,5,5,6,7]`

```python
from collections import deque

def max_sliding_window(nums, k):
    """
    Time Complexity: O(n) where n is the length of array
    Space Complexity: O(k) for deque

    Explanation:
    - Use deque to maintain window indices
    - Keep deque in decreasing order of values
    - Remove indices outside current window
    - Remove smaller elements from right
    - Front of deque is always maximum
    - Each element added and removed once
    """
    if not nums or k == 0:
        return []

    result = []
    dq = deque()  # Store indices

    for i in range(len(nums)):
        # Remove indices outside window
        while dq and dq[0] <= i - k:
            dq.popleft()

        # Remove smaller elements from right
        while dq and nums[dq[-1]] < nums[i]:
            dq.pop()

        dq.append(i)

        # Add to result after first window
        if i >= k - 1:
            result.append(nums[dq[0]])

    return result

# Test
print(max_sliding_window([1,3,-1,-3,5,3,6,7], 3))  # Output: [3,3,5,5,6,7]
print(max_sliding_window([1,-1], 1))               # Output: [1,-1]
```

## 23. Minimum in Rotated Sorted Array (Medium)

**Problem:** Find minimum element in rotated sorted array.

**Sample Input:** `[3,4,5,1,2]`  
**Sample Output:** `1`

```python
def find_min_rotated(nums):
    """
    Time Complexity: O(log n) where n is the length of array
    Space Complexity: O(1) constant space

    Explanation:
    - Binary search variant
    - If mid > right, minimum in right half
    - If mid < right, minimum in left half (including mid)
    - Converge to single element
    - Handle no rotation case
    """
    left, right = 0, len(nums) - 1

    while left < right:
        mid = (left + right) // 2

        if nums[mid] > nums[right]:
            # Minimum is in right half
            left = mid + 1
        else:
            # Minimum is in left half or at mid
            right = mid

    return nums[left]

# With duplicates
def find_min_rotated_duplicates(nums):
    """Handle duplicates by linear scan in worst case"""
    left, right = 0, len(nums) - 1

    while left < right:
        mid = (left + right) // 2

        if nums[mid] > nums[right]:
            left = mid + 1
        elif nums[mid] < nums[right]:
            right = mid
        else:
            # nums[mid] == nums[right], can't determine
            right -= 1

    return nums[left]

# Test
print(find_min_rotated([3,4,5,1,2]))  # Output: 1
print(find_min_rotated([4,5,6,7,0,1,2]))  # Output: 0
```

## 24. Jump Game (Medium)

**Problem:** Determine if you can reach last index.

**Sample Input:** `[2,3,1,1,4]`  
**Sample Output:** `True`

```python
def can_jump(nums):
    """
    Time Complexity: O(n) where n is the length of array
    Space Complexity: O(1) constant space

    Explanation:
    - Greedy approach: track maximum reachable index
    - At each position, update max reach
    - If current position > max reach, can't proceed
    - If max reach >= last index, can reach end
    - Early termination possible
    """
    max_reach = 0

    for i in range(len(nums)):
        if i > max_reach:
            return False

        max_reach = max(max_reach, i + nums[i])

        if max_reach >= len(nums) - 1:
            return True

    return True

# Jump Game II - Minimum jumps to reach end
def jump(nums):
    """Return minimum number of jumps"""
    if len(nums) <= 1:
        return 0

    jumps = 0
    current_end = 0
    farthest = 0

    for i in range(len(nums) - 1):
        farthest = max(farthest, i + nums[i])

        if i == current_end:
            jumps += 1
            current_end = farthest

            if current_end >= len(nums) - 1:
                break

    return jumps

# Test
print(can_jump([2,3,1,1,4]))  # Output: True
print(can_jump([3,2,1,0,4]))  # Output: False
print(jump([2,3,1,1,4]))      # Output: 2
```

## 25. Merge Intervals (Medium)

**Problem:** Merge overlapping intervals.

**Sample Input:** `[[1,3],[2,6],[8,10],[15,18]]`  
**Sample Output:** `[[1,6],[8,10],[15,18]]`

```python
def merge_intervals(intervals):
    """
    Time Complexity: O(n log n) where n is number of intervals
    Space Complexity: O(n) for result

    Explanation:
    - Sort intervals by start time
    - Compare each interval with last merged
    - If overlap, merge by extending end
    - If no overlap, add as new interval
    - Handle edge cases (empty input)
    """
    if not intervals:
        return []

    # Sort by start time
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]

    for interval in intervals[1:]:
        # Check overlap with last merged interval
        if interval[0] <= merged[-1][1]:
            # Merge by extending end time
            merged[-1][1] = max(merged[-1][1], interval[1])
        else:
            # No overlap, add new interval
            merged.append(interval)

    return merged

# Test
print(merge_intervals([[1,3],[2,6],[8,10],[15,18]]))  # Output: [[1,6],[8,10],[15,18]]
print(merge_intervals([[1,4],[4,5]]))                # Output: [[1,5]]
```

## 26. Sort Colors (Medium)

**Problem:** Sort array with values 0, 1, 2 (Dutch National Flag).

**Sample Input:** `[2,0,2,1,1,0]`  
**Sample Output:** `[0,0,1,1,2,2]`

```python
def sort_colors(nums):
    """
    Time Complexity: O(n) where n is the length of array
    Space Complexity: O(1) in-place sorting

    Explanation:
    - Three pointers: left (0s), right (2s), current
    - Move 0s to left, 2s to right, 1s stay middle
    - Swap when 0 or 2 encountered
    - Don't increment current after swapping with right
    - Single pass solution
    """
    left = current = 0
    right = len(nums) - 1

    while current <= right:
        if nums[current] == 0:
            nums[left], nums[current] = nums[current], nums[left]
            left += 1
            current += 1
        elif nums[current] == 2:
            nums[current], nums[right] = nums[right], nums[current]
            right -= 1
            # Don't increment current
        else:  # nums[current] == 1
            current += 1

    return nums

# Test
print(sort_colors([2,0,2,1,1,0]))  # Output: [0,0,1,1,2,2]
print(sort_colors([2,0,1]))        # Output: [0,1,2]
```

## 27. Largest Rectangle in Histogram (Hard)

**Problem:** Find largest rectangle area in histogram.

**Sample Input:** `[2,1,5,6,2,3]`  
**Sample Output:** `10`

```python
def largest_rectangle(heights):
    """
    Time Complexity: O(n) where n is the length of array
    Space Complexity: O(n) for stack

    Explanation:
    - Use stack to track indices of increasing heights
    - When smaller height found, calculate areas
    - Area = height * width (current - left - 1)
    - Add sentinel 0 at end to process remaining
    - Stack maintains potential left boundaries
    """
    stack = []
    max_area = 0

    for i, h in enumerate(heights):
        while stack and heights[stack[-1]] > h:
            height_idx = stack.pop()
            height = heights[height_idx]
            width = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, height * width)

        stack.append(i)

    # Process remaining bars
    while stack:
        height_idx = stack.pop()
        height = heights[height_idx]
        width = len(heights) if not stack else len(heights) - stack[-1] - 1
        max_area = max(max_area, height * width)

    return max_area

# Test
print(largest_rectangle([2,1,5,6,2,3]))  # Output: 10
print(largest_rectangle([2,4]))          # Output: 4
```

## 28. Kth Largest Element (Medium)

**Problem:** Find kth largest element in unsorted array.

**Sample Input:** `nums = [3,2,1,5,6,4], k = 2`  
**Sample Output:** `5`

```python
def find_kth_largest(nums, k):
    """
    Time Complexity: O(n) average, O(n²) worst case
    Space Complexity: O(log n) for recursion

    Explanation:
    - Quick Select algorithm (partial sorting)
    - Partition around pivot, place in correct position
    - Recursively search correct half
    - Convert k to index (n - k for kth largest)
    - Average O(n) due to halving search space
    """
    def partition(left, right):
        pivot = nums[right]
        i = left

        for j in range(left, right):
            if nums[j] <= pivot:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1

        nums[i], nums[right] = nums[right], nums[i]
        return i

    def quick_select(left, right, k_smallest):
        if left == right:
            return nums[left]

        pivot_index = partition(left, right)

        if k_smallest == pivot_index:
            return nums[k_smallest]
        elif k_smallest < pivot_index:
            return quick_select(left, pivot_index - 1, k_smallest)
        else:
            return quick_select(pivot_index + 1, right, k_smallest)

    # kth largest is (n-k)th smallest
    return quick_select(0, len(nums) - 1, len(nums) - k)

# Using heap
import heapq
def find_kth_largest_heap(nums, k):
    """O(n log k) using min heap of size k"""
    return heapq.nlargest(k, nums)[-1]

# Test
print(find_kth_largest([3,2,1,5,6,4], 2))  # Output: 5
print(find_kth_largest([3,2,3,1,2,4,5,5,6], 4))  # Output: 4
```

## 29. Maximum Product Subarray (Medium)

**Problem:** Find contiguous subarray with largest product.

**Sample Input:** `[2,3,-2,4]`  
**Sample Output:** `6` (subarray [2,3])

```python
def max_product(nums):
    """
    Time Complexity: O(n) where n is the length of array
    Space Complexity: O(1) constant space

    Explanation:
    - Track both max and min products at each position
    - Negative number can make min become max
    - At each position:
      - max = max(num, num*prev_max, num*prev_min)
      - min = min(num, num*prev_max, num*prev_min)
    - Handle negative numbers correctly
    """
    if not nums:
        return 0

    max_prod = min_prod = result = nums[0]

    for num in nums[1:]:
        # Store max_prod before updating
        temp = max_prod

        # Update max and min
        max_prod = max(num, num * max_prod, num * min_prod)
        min_prod = min(num, num * temp, num * min_prod)

        result = max(result, max_prod)

    return result

# Test
print(max_product([2,3,-2,4]))   # Output: 6
print(max_product([-2,0,-1]))    # Output: 0
print(max_product([-2,3,-4]))    # Output: 24
```

## 30. First Missing Positive (Hard)

**Problem:** Find smallest missing positive integer.

**Sample Input:** `[3,4,-1,1]`  
**Sample Output:** `2`

```python
def first_missing_positive(nums):
    """
    Time Complexity: O(n) where n is the length of array
    Space Complexity: O(1) constant space

    Explanation:
    - Use array itself as hash table
    - Place each positive number at index (num-1)
    - Swap numbers to correct positions
    - First position where nums[i] != i+1 is answer
    - Handle duplicates and out-of-range numbers
    """
    n = len(nums)

    # Place each positive integer at its correct position
    for i in range(n):
        while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
            # Swap to correct position
            correct_pos = nums[i] - 1
            nums[i], nums[correct_pos] = nums[correct_pos], nums[i]

    # Find first missing
    for i in range(n):
        if nums[i] != i + 1:
            return i + 1

    return n + 1

# Test
print(first_missing_positive([3,4,-1,1]))  # Output: 2
print(first_missing_positive([1,2,0]))     # Output: 3
print(first_missing_positive([7,8,9,11,12]))  # Output: 1
```

## Summary of Time Complexities:

- **O(n)**: Problems 1-3, 5-9, 11, 13, 15-17, 19-22, 24, 26-30
- **O(log n)**: Problems 10, 14, 23
- **O(n log n)**: Problems 12, 25
- **O(n²)**: Problem 12 (3Sum)
- **O(m\*n)**: Problems 17-18 (matrix problems)

## Key Techniques Used:

1. **Two Pointers**: Problems 3, 4, 7, 11-13, 20, 26
2. **Sliding Window**: Problems 16, 22
3. **Binary Search**: Problems 10, 14, 23
4. **Hash Map**: Problems 2, 16, 19, 21
5. **Stack**: Problems 22, 27
6. **Dynamic Programming**: Problems 6, 9, 24, 29
7. **Greedy**: Problems 24, 26
8. **Mathematical**: Problems 5, 30
9. **Matrix Manipulation**: Problems 17-18
10. **Sorting**: Problems 12, 25
