def smallest_in_the_row(m: list, row) -> tuple:
    """Returns index of a smallest number in matrix in given row."""
    smallest =  min(m[row])
    for y in range(len(m[row])):
        if m[row][y] == smallest:
            return (row, y)

def smallest_in_the_column(m: list, col) -> tuple:
    """Returns index of a smallest number in matrix in given column."""
    smallest = m[0][col]
    n = len(m)

    for x in range(n):
        if m[x][col] < smallest:
            smallest = m[x][col]
        
    for x in range(n):
        if m[x][col] == smallest:
            return (x, col)

def stringify_matrix(m: list) -> str:
    result = ''
    for row in m:
        for el in row[:-1]:
            result += f'{el} '
        result += f'{row[-1]}\n'
    
    return result

def main():
    N = int(input())
    i = int(input())
    j = int(input())

    matrix = []
    for _ in range(N):
        row = list(map(int, input().split(' ')))
        matrix.append(row)

    while smallest_in_the_row(matrix, i)[1] != j or smallest_in_the_column(matrix, j)[0] != i:
        i, j = smallest_in_the_row(matrix, i)
        i, j = smallest_in_the_column(matrix, j)
        
    print(i, j)
    # return position of the last position you can reach
    
if __name__ == '__main__':
    main()