"""
    Write a function that takes in a non-empty array of integers and returns an   array of the same length, where each element in the output array is equal to   the product of every other number in the input array.
    In other words, the value at output[i]  is equal to the product of
    every number in the input array other than input[i]

    Note that you're expected to solve this problem without using division.

    Sample Input:
      array = [5, 1, 4, 2]

    Sample Output:
      [8, 30, 10, 20]
"""
def arrayOfProducts(array):
    output = []
    zeroFound = False
    for i in range(0,len(array)):
        if zeroFound:
            output.append(0)
            continue
        
        right = i + 1
        left = i - 1
        currentProduct = 1
        while right < len(array):
            currentProduct = currentProduct * array[right]
            right += 1
        while left >= 0:
            currentProduct = currentProduct * array[left]
            left -= 1
            
        if array[i] == 0:
            zeroFound = True
            
        output.append(currentProduct)

    return output