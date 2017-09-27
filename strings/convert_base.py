import functools
import string

# Method one
def convert_base(num_str, b1, b2):
    is_neg = num_str[0] == '-'
    dec_num = functools.reduce(lambda num_sum, c: num_sum * b1 + string.hexdigits.index(c), num_str[is_neg:], 0)
    res_num = ''
    haha = num_str
    while dec_num:
        dig = dec_num % b2
        res_num = string.hexdigits[dig].upper() + res_num
        dec_num //= b2
    return ('-' if is_neg else '') + ('0' if haha == 0 else res_num)

# Method two
def convert_base_two(num_str, b1, b2):
    def convert_to_b2(dec_num, b2):
        return ('' if dec_num == 0 else convert_to_b2(dec_num // b2, b2) + string.hexdigits[dec_num % b2])
    is_neg = num_str[0] == '-'
    dec_num = functools.reduce(lambda num_sum, c: num_sum * b1 + string.hexdigits.index(c), num_str[is_neg:], 0)
    return ('-' if is_neg else '') + convert_to_b2(dec_num, b2)

def main():
    num_str = '-124'
    print(convert_base_two(num_str, 10, 15))

if __name__ == '__main__':
    main()
