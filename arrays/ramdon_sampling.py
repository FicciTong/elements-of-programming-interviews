import random

def random_sampling(A, k):
    for i in range(k):
        j = random.randint(i, len(A) - 1)
        A[i], A[j] = A[j], A[i]
    return A[:k]

def main():
    A = list(range(50))
    k = random.randint(1, 10)
    print(random_sampling(A, k))

if __name__ == '__main__':
    main()
