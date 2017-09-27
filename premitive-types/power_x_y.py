def power_x_y_brute(x, y):
    result = 1.0
    for i in range(y):
        result *= x
    return result


def power_x_y(x, y):
    result, power = 1.0, y
    if y < 0:
        x = 1 / x
        power = -power
    while power:
        if power & 1:
            result *= x
        x, power = x * x, power >> 1
    return result

def main():
    result = power_x_y_brute(2, 4)
    print(result)


    res = power_x_y(2, -3)
    print(res)

if __name__ == '__main__':
    main()
