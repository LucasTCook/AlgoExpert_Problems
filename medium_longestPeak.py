"""

  Write a function that takes in an array of integers and returns the length of
  the longest peak in the array.

  
  A peak is defined as adjacent integers in the array that are strictly increasing 
  until they reach a tip (the highest value in the peak), at which point they become 
  strictly  decreasing. At least three integers are required to form a peak.

  For example, the integers 1, 4, 10, 2 form a peak, but the integers 4, 0, 10 don't
  and neither do the integers 1, 2, 2, 0. Similarly, the integers 1, 2, 3 dont form a 
  peak because there aren't any strictly decreasing integers after the 3.

  Sample Input:
    array = [1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]

  Sample Output:
    6 // 0, 10, 6, 5, -1, -3

"""

def longestPeak(array):
    if(len(array) < 3):
        return 0
        
    longestPeak = 0
    for i in range(1,len(array) - 1):
        peakLeft = i - 1
        peakRight = i + 1
        if(array[peakLeft] < array[i] and array[peakRight]< array[i]):
            currentPeakLength = 3
            while peakLeft >= 0:
                if(array[peakLeft - 1] < array[peakLeft]):
                    currentPeakLength += 1
                    peakLeft -= 1
                else:
                    break
            while peakRight < len(array) - 1:
                if(array[peakRight + 1] < array[peakRight]):
                    currentPeakLength += 1
                    peakRight += 1
                else:
                    break   
            longestPeak = currentPeakLength if currentPeakLength > longestPeak else longestPeak
                
    return longestPeak        
        