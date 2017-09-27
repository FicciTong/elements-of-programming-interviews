import collections


class BinaryTreeNode:
    def __init__(self, data=0, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def tree_traversal_preorder(node):
    if node:
        print(node.data)
        tree_traversal_preorder(node.left)
        tree_traversal_preorder(node.right)


def tree_traversal_inorder(node):
    if node:
        tree_traversal_inorder(node.left)
        print(node.data)
        tree_traversal_inorder(node.right)


def tree_traversal_postorder(node):
    if node:
        tree_traversal_postorder(node.left)
        tree_traversal_postorder(node.right)
        print(node.data)


def binary_tree_depth_order(node):
    curr_level_nodes = collections.deque([node])
    result = []
    while curr_level_nodes:
        next_level_nodes = collections.deque([])
        curr_result = []
        while curr_level_nodes:
            curr = curr_level_nodes.popleft()
            if curr:
                curr_result.append(curr.data)
                next_level_nodes.append(curr.left)
                next_level_nodes.append(curr.right)
        if curr_result:
            result.append(curr_result)
        curr_level_nodes = next_level_nodes
    return result


def main():
    root = BinaryTreeNode('A')
    node_b = BinaryTreeNode('B')
    node_c = BinaryTreeNode('C')
    node_d = BinaryTreeNode('D')
    node_e = BinaryTreeNode('E')
    node_f = BinaryTreeNode('F')
    node_g = BinaryTreeNode('G')
    node_h = BinaryTreeNode('H')
    node_i = BinaryTreeNode('I')
    node_j = BinaryTreeNode('J')
    node_k = BinaryTreeNode('K')
    node_l = BinaryTreeNode('L')
    node_m = BinaryTreeNode('M')
    node_n = BinaryTreeNode('N')
    node_o = BinaryTreeNode('O')
    root.left = node_b
    root.right = node_c
    node_b.left = node_d
    node_b.right = node_e
    node_c.left = node_f
    node_c.right = node_g
    node_d.left = node_h
    node_d.right = node_i
    node_e.left = node_j
    node_e.right = node_k
    node_f.left = node_l
    node_f.right = node_m
    node_g.left = node_n
    node_g.right = node_o

    print(binary_tree_depth_order(root))


if __name__ == '__main__':
    main()
