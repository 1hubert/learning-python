def magic_matrix():
    row_length = int(input('Input length of one row of the matrix: '))

    rows = []

    is_magic = 'magic'

    for i in range(row_length):
        row_str = input('Input row ' + str(i + 1) + ': ')
        row = []
        num_str = ''
        for char in row_str:
            if char == ' ' and num_str:
                row.append(int(num_str))
                num_str = ''
            if char != ' ':
                num_str += char
        if num_str:
            row.append(int(num_str))
        rows.append(row)

    print(rows)

    magic_sum = sum(rows[0])
    for i in range(row_length):
        if sum(rows[i]) != magic_sum:
            is_magic = 'not magic'

    for x in range(row_length):
        column_sum = 0
        for i in range(row_length):
            column_sum += rows[i][x]
        if column_sum != magic_sum:
            is_magic = 'not magic'

    count1 = 0
    count2 = row_length - 1
    cross1_sum = 0
    cross2_sum = 0
    for i in range(row_length):
        cross1_sum += rows[i][count1]
        cross2_sum += rows[i][count2]

        count1 += 1
        count2 -= 1

    if cross1_sum != magic_sum or cross2_sum != magic_sum:
        is_magic = 'not magic'
    

    print(is_magic)

magic_matrix()