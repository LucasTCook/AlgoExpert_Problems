"""
  You're given an array of integers and an integer. Write a function that moves
  all instances of that integer in the array to the end of the array and returns
  the array.

  The function should perform this in place (i.e., it should mutate the input
  array) and doesn't need to maintain the order of the other integers.
"""
def moveElementToEnd(array, toMove):
    left = 0
    right = len(array) - 1

    while left < right - 1:
        if(array[left] != toMove):
            left += 1
        if(array[right] == toMove):
            right -= 1
        if(array[left] == toMove and array[right] != toMove):
            temp = array[left]
            array[left] = array[right]
            array[right] = temp
            
    return array