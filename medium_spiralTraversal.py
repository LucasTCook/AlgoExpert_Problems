"""
  Write a function that takes in an n x m two-dimensional array (that can be
  square-shaped when n == m) and returns a one-dimensional array of all the
  array's elements in spiral order.

  Spiral order starts at the top left corner of the two-dimensional array, goes
  to the right, and proceeds in a spiral pattern all the way until every element
  has been visited.
"""

def spiralTraverse_recursive(array):
    output = []
    rec(array, 0, len(array) - 1, 0, len(array[0]) - 1, output)
    return output

def rec(matrix, startR, endR, startCol, endCol, result):
    if startR > endR or startCol > endCol:
        return
        
    for col in range(startCol,endCol + 1):
        result.append(matrix[startR][col])
        
    for row in range(startR + 1,endR + 1):
        result.append(matrix[row][endCol])
        
    for col in reversed(range(startCol,endCol)):
        if startR == endR:
                break
        result.append(matrix[endR][col])
        
    for row in reversed(range(startR + 1,endR)):
        if startCol == endCol:
                break
        result.append(matrix[row][startCol])
        
    rec(matrix, startR+1, endR-1, startCol+1, endCol-1, result)

def spiralTraverse(array):
    result = []
    startRow, endRow = 0, len(array) - 1
    startCol, endCol = 0, len(array[0]) -1

    while startRow <= endRow and startCol <= endCol:
        for col in range(startCol,endCol + 1):
            result.append(array[startRow][col])

        for row in range(startRow + 1,endRow + 1):
            result.append(array[row][endCol])

        for col in reversed(range(startCol,endCol)):
            if startRow == endRow:
                break
            result.append(array[endRow][col])

        for row in reversed(range(startRow + 1,endRow)):
            if startCol == endCol:
                break
            result.append(array[row][startCol])

        startRow+= 1
        endRow -= 1
        startCol += 1
        endCol -= 1
        
    return result

def main():
    sampleMatrix = [[1,2,3,4,5],
                    [12,13,14,15,6],
                    [11,10,9,8,7]]

    print(spiralTraverse(sampleMatrix))
    print(spiralTraverse_recursive(sampleMatrix))

if __name__ == "__main__":
    main()