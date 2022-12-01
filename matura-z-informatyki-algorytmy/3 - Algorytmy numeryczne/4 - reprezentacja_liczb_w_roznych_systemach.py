def conversion_from_base_10(num: int, base: int) -> str:
    result_backwards = []
    while(num > 0):
        a = int(num % base)
        result_backwards.append(a)
        num = (num-a) / base
    
    result = ''
    for elem in result_backwards[::-1]:
        result += str(elem)

    return result


def system_conv_recursive(num: int, base: int) -> None:
    if num > 0:
        rest = num % base
        system_conv_recursive((num-rest)/base, base)
        if rest > 9:
            if rest == 10:
                print('A')
            elif rest == 11:
                print('B')
            elif rest == 12:
                print('C')
            elif rest == 13:
                print('D')
            elif rest == 14:
                print('E')
            elif rest == 15:
                print('F')
        else:
            print(int(rest))


num = 1201
base = 16
system_conv_recursive(num, base)
