"""
  Write a function that takes in a non-empty array of distinct integers and an
  integer representing a target sum. If any two numbers in the input array sum
  up to the target sum, the function should return them in an array, in any
  order. If no two numbers sum up to the target sum, the function should return
  an empty array.

  Note that the target sum has to be obtained by summing two different integers
  in the array; you can't add a single integer to itself in order to obtain the
  target sum.

  You can assume that there will be at most one pair of numbers summing up to
  the target sum.

  Sample Inputs:
   array =  [3, 5, -4, 8, 11, 1, -1, 6]
   targetSum = 10

  Sample Output:
    [-1,11] // the numbers could be in reverse order
"""

# O(n^2) time | O(1) space
def twoNumberSum_1(array, targetSum):
    # Write your code here.
    
    for i in array:
        for j in array:
            if i == j:
                continue
            if i + j == targetSum:
                return [i,j]
    return []

# O(n) time  | O(n) space
def twoNumberSum_2(array, targetSum):
    # Write your code here.
    nums = {}

    for i in array:
        potentialMatch = targetSum - i
        # print("Current Value: {0}, Potential Match: {1}, Nums: {2}".format(i,potentialMatch, nums))
        if potentialMatch in nums:
            # print([targetSum - i, i])
            return [targetSum - i, i]
        else:
            nums[i] = True
    return []

# O(nlog(n)) | O(1) space
def twoNumberSum_3(array, targetSum):
    # Write your code here.
    array.sort()
    left = 0
    right = len(array) - 1

    # print(array)
    while left < right:
        currentSum = array[left] + array[right]
        # print(array[left], array[right],currentSum, targetSum)
        if currentSum == targetSum:
            # print(currentSum)
            return [array[left], array[right]]
        elif currentSum < targetSum:
            left += 1
        elif currentSum > targetSum:
            right -= 1
    return []

def main():
    sampleInput = [3, 5, -4, 8, 11, 1, -1, 6]
    sampleTargetSum = 10
    print(twoNumberSum_1(sampleInput,sampleTargetSum)) 
    print(twoNumberSum_2(sampleInput,sampleTargetSum))
    print(twoNumberSum_3(sampleInput,sampleTargetSum))      

if __name__ == "__main__":
    main()   