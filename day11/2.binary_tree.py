# Creator:justice 廖振谊
# Creat time:2022/6/10 19:21
class Node:
    def __init__(self, val, lchild=None, rchild=None):
        self.lchild = lchild
        self.rchild = rchild
        self.val = val


class Binary_Tree:
    def __init__(self):
        self.root = None
        self.node_list = []

    def build_tree(self, ele):
        temp_node = Node(ele)
        self.node_list.append(temp_node)
        if self.root == None:
            self.root = temp_node
        else:
            if self.node_list[0].lchild is None:
                self.node_list[0].lchild = temp_node
            else:
                self.node_list[0].rchild = temp_node
                self.node_list.pop(0)

    def preorder(self, current_node: Node):
        if current_node:
            print(current_node.val, end='')
            self.preorder(current_node.lchild)
            self.preorder(current_node.rchild)

    def inorder(self, current_node: Node):
        if current_node:
            self.inorder(current_node.lchild)
            print(current_node.val, end='')
            self.inorder(current_node.rchild)

    def postorder(self, current_node: Node):
        if current_node:
            self.postorder(current_node.lchild)
            self.postorder(current_node.rchild)
            print(current_node.val, end='')


if __name__ == '__main__':
    t = Binary_Tree();
    for i in "abcdefghij":
        t.build_tree(i)
    t.preorder(t.root)
    print("\n")
    t.inorder(t.root)
    print("\n")
    t.postorder(t.root)
