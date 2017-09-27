def int_to_string(x):
    is_neg = False
    if x < 0:
        is_neg = True
        x = -x
    char_list = []
    while x:
        char_list.append(chr(ord('0') + x % 10))
        x //= 10
    return ('-' if is_neg else '') + ''.join(reversed(char_list))

def main():
    x = 123970324
    result_str = int_to_string(x)
    print(result_str)
    print(type(result_str))

if __name__ == '__main__':
    main()
    
