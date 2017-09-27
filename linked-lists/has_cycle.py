class ListNode:
    def __init__(self, data=0, next_node=None):
        self.data = data
        self.next = next_node

def has_cycle(head):
    slow = fast = head
    # Check if has cycle
    while fast and fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            break
    else:
        return None
    # Calculate cycle length
    cycle_len = 0
    while True:
        fast = fast.next
        cycle_len += 1
        if fast is slow:
            break
    # Get the start of the cycle
    fast = slow = head
    for _ in range(cycle_len):
        fast = fast.next
    while fast is not slow:
        fast, slow = fast.next, slow.next
    return fast

def main():
    node9 = ListNode(9, None)
    node8 = ListNode(8, node9)
    node7 = ListNode(7, node8)
    node6 = ListNode(6, node7)
    node5 = ListNode(5, node6)
    node4 = ListNode(4, node5)
    node3 = ListNode(3, node4)
    node2 = ListNode(2, node3)
    node1 = ListNode(1, node2)
    head = ListNode(0, node1)

    node9.next = node7

    result = has_cycle(head)
    print(result.data)

if __name__ == '__main__':
    main()
