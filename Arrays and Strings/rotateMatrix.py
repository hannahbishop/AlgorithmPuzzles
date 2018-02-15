def rotate_matrix(matrix, N):
    '''
    Input:
        matrix: square, 2D list
        N: length of the matrix
    Returns: 
        matrix, rotated counter clockwise by 90 degrees
    Example:
        Input: 
            [a, b]
            [c, d]
        Returns:
            [b, d]
            [a, c]
    Efficiency:
        O(N^2)
    '''
    for layer in range(N):
        for index in range(layer, N - 1 - layer):
            temp = matrix[layer][index]
            #store right in top
            matrix[layer][index] = matrix[index][N - 1 - layer]
            #store bottom in right
            matrix[index][N - 1 - layer] = matrix[N - 1 - layer][N - 1 - index]
            #store left in bottom
            matrix[N - 1 - layer][N - 1 - index] = matrix[N - 1 - index][layer]
            #store temp in left
            matrix[N - 1 - index][layer] = temp
    return matrix

def print_matrix(matrix, N):
    for i in range(N):
        print(matrix[i])

def main():
    print("start matrix:")
    N = 9
    matrix = [[x for x in range(N)] for y in range(N)]
    print_matrix(matrix, N)
    print("rotated matrix:")
    matrix_rotated = rotate_matrix(matrix, N)
    print_matrix(matrix_rotated, N)

if __name__ == "__main__":
    main()