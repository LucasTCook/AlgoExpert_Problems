""" 
  Write a function that takes in a non-empty array of distinct integers and an
  integer representing a target sum. The function should find all triplets in
  the array that sum up to the target sum and return a two-dimensional array of
  all these triplets. The numbers in each triplet should be ordered in ascending
  order, and the triplets themselves should be ordered in ascending order with
  respect to the numbers they hold.

  Sample Input:
    array = [12,3,1,2,-6,5,-8, 6]
    targetSum = 0
  
  Sample Output:
    [[-8, 2, 6], [-8, 3, 5], [-6, 1, 5]]
"""

def threeNumberSum(array, targetSum):
    array.sort()
    # print(array)

    results = []
    for i in range(0,len(array)):
        left = i + 1
        right = len(array) - 1

        while left < right:
            sum = array[i] + array[left]+ array[right]
            # print(array[i], array[left], array[right],sum, targetSum)
            if sum == targetSum:
                results.append([array[i],array[left],array[right]])
                left += 1
                right -= 1
                # print(results)
            elif sum > targetSum:
                right -= 1
            else:
                left += 1
                
    return results

def main():
    array = [12,3,1,2,-6,5,-8,6]
    targetSum = 0
    print(threeNumberSum(array,targetSum))

if __name__ == "__main__":
    main()   