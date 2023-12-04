"""
  Write a function that takes in an array of integers and returns a boolean
  representing whether the array is monotonic.

  An array is said to be monotonic if its elements, from left to right, are
  entirely non-increasing or entirely non-decreasing.

  Non-increasing elements aren't necessarily exclusively decreasing; they simply
  don't increase. Similarly, non-decreasing elements aren't necessarily
  exclusively increasing; they simply don't decrease.
  
  Note that empty arrays and arrays of one element are monotonic.
"""

def isMonotonic(array):
    if(len(array) <= 2):
        return True
    current = array[0]
    direction = "decreasing" if current > array[-1] else "increasing"
    print(direction)
    for i in range(1,len(array)):
        if (direction == "increasing" and array[i] < current) or (direction == "decreasing" and array[i] > current):
            return False
        current = array[i]
        
    return True
