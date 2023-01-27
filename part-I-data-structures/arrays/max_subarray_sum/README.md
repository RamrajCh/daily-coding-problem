# Calculate Maximum Subarray Sum
Given an array of integers, find the contiguous subarray with the largest sum.

## Examples

Input: `[-2,1,-3,4,-1,2,1,-5,4]`

Output: `6`

Explanation: `[4,-1,2,1]` has the largest sum = `6`.

Input: `[1,2,-1,2,3,-2]`

Output: `7`

Explanation: `[1,2,2,3]` has the largest sum = `7`.

Input: `[-1,-2,-3,-4,-5]`

Output: `0`

Explanation: Sum must always be positive.

## Note

- The input array may contain both positive and negative numbers.
- The subarray with the largest sum may or may not be at the beginning or end of the input array.
- If all the numbers in the input array are negative, the function should return 0.

## Kadane's Algorithm

Kadane's algorithm is a simple yet efficient algorithm to find the maximum subarray sum in an array of integers. It has a time complexity of O(n) and it works by iterating through the array, keeping track of the maximum sum seen so far, as well as the current sum.

Here is the algorithm:

1. Initialize variables max_so_far and max_ending_here to the first element of the array.
2. Start a loop from the second element of the array and iterate until the last element.
3. At each iteration, update max_ending_here by comparing the current element with the sum of the current element and max_ending_here.
4. Update max_so_far by comparing max_ending_here and max_so_far.
5. Return max_so_far as the result.