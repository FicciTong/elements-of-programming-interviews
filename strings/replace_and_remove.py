def replace_and_remove(s, size):
    write_idx, a_count = 0, 0
    for i in range(size):
        if s[i] == 'a':
            a_count += 1
        if s[i] != 'b':
            s[write_idx] = s[i]
            write_idx += 1

    cur_idx = write_idx - 1
    write_idx = write_idx + a_count - 1
    final_size = write_idx + 1
    while cur_idx >= 0:
        if s[cur_idx] == 'a':
            s[write_idx-1] = 'd'
            s[write_idx] = 'd'
            write_idx -= 2
        else:
            s[write_idx] = s[cur_idx]
            write_idx -= 1
        cur_idx -= 1
    return s, final_size


def main():
    print(replace_and_remove(['a', 'b', 'c', 'a', '', '', '', '', '', '', ''],
                             4))


if __name__ == '__main__':
    main()
