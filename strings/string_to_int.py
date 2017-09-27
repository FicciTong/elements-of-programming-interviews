import functools
import string

# # Method one
# def string_to_int(s):
#     sign = 1
#     if s[0] == '-':
#         sign = -1
#         s = s[1:]
#     x = 0
#     for i in range(len(s)):
#         x = x * 10 + ord(s[i]) - ord('0')
#     return sign * x

# Method Two

def string_to_int(s):
    return functools.reduce(lambda sum, c: sum * 10 + (ord(c) - ord('0')), s[s[0] == '-':], 0) * (-1 if s[0] == '-' else 1)

def main():
    s = '-202938466377'
    result_x = string_to_int(s)
    print(result_x)

if __name__ == '__main__':
    main()
