class ListNode:
    def __init__(self, data, next_node):
        self.data = data
        self.next = next_node
def reverse_sublist(L, a, b):
    dummy_head = sub_head = ListNode(0, L)
    for _ in range(1, a):
        sub_head = sub_head.next

    sub_iter = sub_head.next
    for _ in range(b - a):
        temp = sub_iter.next
        sub_iter.next = temp.next
        temp.next = sub_head.next
        sub_head.next = temp
    return dummy_head.next

def main():
    L = ListNode(11, ListNode(3, ListNode(5, ListNode(7, ListNode(2, None)))))
    result_list = reverse_sublist(L, 2, 4)
    while result_list:
        print(result_list.data)
        result_list = result_list.next

if __name__ == '__main__':
    main()
