"""
  Given two non-empty arrays of integers, write a function that determines
  whether the second array is a subsequence of the first one.

  A subsequence of an array is a set of numbers that aren't necessarily adjacent
  in the array but that are in the same order as they appear in the array. For
  instance, the numbers [1, 3, 4] form a subsequence of the array [1, 2, 3, 4] , 
  and so do the numbers [2, 4]. Note that a single number in an array and the array 
  itself are both valid subsequences of the array.
  
  Sample Input
    array = [5, 1, 22, 25, 6, -1, 8, 10]
    sequence = [1, 6, -1, 10] 

  Sample Output
    True

"""

#O(n) time | O(1) space
def isValidSubsequence_1(array, sequence):

    subsequence_count = 0
    for i in array:
        if subsequence_count == len(sequence):
            break
        if sequence[subsequence_count] == i:
            subsequence_count += 1
            
    return subsequence_count == len(sequence)

# O(n) time | O(1) space
def isValidSubsequence_2(array, sequence):
    arrIdx = 0
    seqIdx = 0

    while arrIdx < len(array) and seqIdx < len(sequence):
        # print("arrIdx={0},seqIdx={1}".format(arrIdx,seqIdx))
        # print("arrayVal={0}, seqVal={1}".format(array[arrIdx], sequence[seqIdx]))
        if array[arrIdx] == sequence[seqIdx]:
            # print("Found")
            seqIdx += 1
        arrIdx += 1

    return seqIdx == len(sequence)

def main():
    sampleInput = [5, 1, 22, 25, 6, -1, 8, 10]
    sampleSequence = [1, 6, -1, 10] 
    print(isValidSubsequence_1(sampleInput,sampleSequence)) 
    print(isValidSubsequence_2(sampleInput,sampleSequence))

if __name__ == "__main__":
    main()   