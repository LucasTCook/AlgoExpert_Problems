"""
  Write a function that takes in a non-empty array of integers that are sorted
  in ascending order and returns a new array of the same length with the squares
  of the original integers also sorted in ascending order.

  Sample Input:
    array = [1,2,3,5,6,8,9]

  Sample Output:
    [1, 4, 9, 25, 36, 64, 81]
"""

#O(nlogn) time | O(n) space
def sortedSquaredArray_1(array):
    # Write your code here.
    squared_array = []
    
    for i in array:
        squared_array.append(i*i)
        # print(squared_array)

    # print(squared_array)
    squared_array.sort()
    return squared_array


# O(n) linear | O(n) space
def sortedSquaredArray_2(array):
    # Write your code here.
    squared_array = [0 for _ in array]
    # print(squared_array)

    left = 0
    right = len(array) - 1

    # print(array)
    for i in reversed(range(len(array))):
        # print("i: {}".format(i))
        smaller_value = array[left]
        larger_value = array[right]
        # print("Smaller: {0}, Larger: {1}".format(smaller_value,larger_value))
        if abs(smaller_value) > abs(larger_value):
            squared_array[i] = smaller_value * smaller_value
            left += 1
        else:
            squared_array[i] = larger_value * larger_value
            right -= 1
        # print(squared_array)
        
    # print(squared_array)
    return squared_array


def main():
    sampleInput = [1,2,3,5,6,8,9]
    print(sortedSquaredArray_1(sampleInput)) 
    print(sortedSquaredArray_2(sampleInput)) 

if __name__ == "__main__":
    main()   