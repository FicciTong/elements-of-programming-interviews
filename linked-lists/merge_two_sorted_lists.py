import random

class ListNode:
    def __init__(self, data=0, next_node=None):
        self.data = data
        self.next = next_node

def search_list(L, key):
    while L and L.data != key:
        L = L.next
    return L

def insert_after(node, new_node):
    new_node.next = node.next
    node.next = new_node

def delete_after(node):
    node.next = node.next.next

def merge_two_sorted_list(L1, L2):
    dummy_head = tail = ListNode()
    while L1 and L2:
        if L1.data < L2.data:
            tail.next = L1
            L1 = L1.next
        else:
            tail.next = L2
            L2 = L2.next
        tail = tail.next
    tail.next = L1 or L2
    return dummy_head.next

def main():
    L1 = ListNode(1, ListNode(3, ListNode(5, ListNode(7, ListNode(9, None)))))
    L2 = ListNode(0, ListNode(2, ListNode(4, ListNode(6, ListNode(8, None)))))
    result_list = merge_two_sorted_list(L1, L2)
    while result_list:
        print(result_list.data)
        result_list = result_list.next

if __name__ == '__main__':
    main()
