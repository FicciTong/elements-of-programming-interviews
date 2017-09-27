def reverse(x):
    sign = 1
    if x < 0:
        sign = -1
    x = abs(x)

    rev_x = 0
    while x:
        rev_x = rev_x * 10 + x % 10
        x //= 10
    return sign * rev_x

def main():
    print('Enter an integer to reverse:')
    num = int(input())
    res = reverse(num)
    print(res)

if __name__ == '__main__':
    main()
