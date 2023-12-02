def transposeMatrix(matrix):
    matrix_transposed = [[] for _ in range(0,len(matrix[0]))]
    
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[i])):
            matrix_transposed[j].append(matrix[i][j])
            # print("i: {0}, j: {1}, matrix_val:{2}".format(i,j,matrix[i][j]))

    return matrix_transposed

def transposeMatrix_short(matrix):
    return list(zip(*matrix))  

def main():
    sampleInput = [[1,2],
                   [3,4],
                   [5,6]]
    print("IN: {}".format(sampleInput))
    print("OUT: {}".format(transposeMatrix(sampleInput))) 
    print("OUT: {}".format(transposeMatrix_short(sampleInput))) 

if __name__ == "__main__":
    main()   