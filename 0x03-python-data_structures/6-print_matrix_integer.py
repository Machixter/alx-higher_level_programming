#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    #get no of rows and colums in matrix
    num_rows = len(matrix)
    num_cols = len(matrix[0] if matrix else 0)
    #iterate over each row and colum
    for x in range(num_rows):
        for y in range(num_cols):
            #print int at current position
            print("{:d}".format(matrix[x][y]), end="")
            if y != (len(matrix[x]) - 1):
                print(" ", end="")
            #print new line after each row 
        print()
