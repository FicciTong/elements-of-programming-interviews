def dutch_flag_partition(pivot_index, A):
    pivot = A[pivot_index]
    smaller, equal, larger = 0, 0, len(A) - 1
    while equal < larger:
        if A[equal] < pivot:
            A[smaller], A[equal] = A[equal], A[smaller]
            smaller += 1
            equal += 1
        elif A[equal] == pivot:
            equal += 1
        else: # A[equal] > pivot
            A[equal], A[larger] = A[larger], A[equal]
            larger -=1
    return A


def main():
    print('Enter a list of integers, seperated by commas')
    A = list(map(int, str(input()).split(',')))
    print(A)
    # A = [3,4,2,5,6,7,4,5,6,3,2,5,6,4,4,3,6,7,8,9,9,5,4,3]
    print('Enter the pivot index')
    pivot_index = int(input())
    print('Pivot: {0}'.format(A[pivot_index]))
    # pivot_index = 4
    sorted_A = dutch_flag_partition(pivot_index, A)
    print(sorted_A)

if __name__ == '__main__':
    main()
