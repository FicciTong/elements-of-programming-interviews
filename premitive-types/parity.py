def cal_parity_16(x):
    x ^= x >> 8
    x ^= x >> 4
    x ^= x >> 2
    x ^= x >> 1
    return x & 0x1

def cal_parity_64(x):
    x ^= x >> 32
    x ^= x >> 16
    x ^= x >> 8
    x ^= x >> 4
    x ^= x >> 2
    x ^= x >> 1
    return x & 0x1

def parity(x):
    mask = 0xFFFF
    mask_size = 16
    return(precomputed_parity[x >> (mask_size * 3)] ^ precomputed_parity[(x >> mask_size * 2) & mask] ^ precomputed_parity[(x >> mask_size) & mask] ^ precomputed_parity[x & mask])

if __name__ == "__main__":
    precomputed_parity = []
    for i in range(int(0xFFFF)):
        precomputed_parity.append(cal_parity_16(i))

    print('Please enter the number to calculate its parity: ')
    num = int(input())
    bin(num)
    print ('The parity of {0} is {1} using method one, {2} using method two'.format(num, parity(num), cal_parity_64(num)))
