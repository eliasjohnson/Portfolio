class BST:
    """generates a BST class with a head node and a list to store nodes in order of traversal"""
    def __init__(self):
        self.head = None
        self.lyst = []

    def set_head(self, node):
        """sets head to node
        """
        self.head = node

    def get_head(self):
        """Returns self.head"""
        return self.head

    def is_empty(self):
        """Returns true if empty, false otherwise."""
        if self.head is None:
            return True
        return False

    def size(self, node="self.head"):
        """Returns the number of nodes in the tree."""
        if isinstance(node, str):
            node = eval(node)
        if node is None:
            return 0
        return 1 + self.size(node.get_left()) + self.size(node.get_right())

    def height(self, node="self.head"):
        """Returns the length of the path from the root to its deepest leaf."""
        if isinstance(node, str):
            node = eval(node)
        if node is None:
            return 0

        left_height = self.height(node.get_left())
        right_height = self.height(node.get_right())

        return 1 + max(left_height, right_height)

    def add(self, node):
        """Add node to its proper place in the tree and returns modified tree.
        """
        if self.is_empty():
            self.set_head(node)
        else:
            self.compare(node, self.get_head())
        return self

    def compare(self, node, tree):
        """recursively compares node to tree and traverses left or right until tree is none
        """
        if node == tree:
            tree.count += 1
        elif node < tree:
            if tree.get_left() is None:
                tree.set_left(node)
            else:
                self.compare(node, tree.get_left())
        elif node > tree:
            if tree.get_right() is None:
                tree.set_right(node)
            else:
                self.compare(node, tree.get_right())
        else:
            print(f"node{node}, tree{tree}")

    def remove(self, node):
        """Remove node from the tree and returns modified tree.
        """
        node = self.find(node)

        left = node.get_left()
        right = node.get_right()
        ordered_l = self.inorder()

        if node == self.get_head():
            for i, j in enumerate(ordered_l):
                if j == node:
                    r_temp = ordered_l[i + 1]
                    reorder_temp = ordered_l[i + 2]
                    break
            r_temp.set_left(left)
            r_temp.set_right(right)
            self.set_head(r_temp)
            reorder_temp.set_left(None)

        else:
            for k in ordered_l:
                if self.find(k).get_left():
                    if node == self.find(k).get_left():
                        p_node = k
                        break
                if self.find(k).get_right():
                    if node == self.find(k).get_right():
                        p_node = k
                        break
            self.lyst = []
            ordered_l = self.preorder(p_node)
            r_temp = ordered_l[-1]
            if r_temp is node:
                r_temp = None
            reorder_temp = ordered_l[-2]
            if left is not r_temp:
                r_temp.set_left(left)
            if right is not r_temp:
                r_temp.set_right(right)
            reorder_temp.set_left(None)
            if p_node.get_left() is node:
                p_node.set_left(r_temp)
            else:
                p_node.set_right(r_temp)

        self.lyst = []
        return self

    def find(self, node, travel="self.head"):
        """Finds and returns the matched node.
        """
        if isinstance(travel, str):
            travel = eval(travel)
        if self.head is None:
            raise ValueError("Node not in tree")
        if travel is None:
            return None
        if node == travel:
            return travel
        else:
            left = self.find(node, travel.get_left())
            right = self.find(node, travel.get_right())
            if left is not None:
                return left
            elif right is not None:
                return right
            elif left and right is None:
                raise ValueError("Node not in tree.")
            else:
                return None

    def inorder(self, node="self.head"):
        """Returns a list with data nodes in order of inorder traversal."""
        if isinstance(node, str):
            node = eval(node)
        if node:
            self.inorder(node.get_left())
            self.lyst.append(node)
            self.inorder(node.get_right())
        return self.lyst

    def preorder(self, node="self.head"):
        """Returns a list with data nodes in order of preorder traversal."""
        if isinstance(node, str):
            node = eval(node)

        if node:
            self.lyst.append(node)
            self.preorder(node.get_left())
            self.preorder(node.get_right())
        return self.lyst

    def postorder(self, node="self.head"):
        """Returns a list with data nodes in order of postorder traversal."""
        if isinstance(node, str):
            node = eval(node)

        if node:
            self.postorder(node.get_left())
            self.postorder(node.get_right())
            self.lyst.append(node)
        return self.lyst

    def rebalance(self):
        """Rebalances the tree and returns the modified tree."""

        temp_bst = BST()
        ordered_lyst = self.inorder()
        self.recursive_middle(ordered_lyst, temp_bst)

        return temp_bst

    def recursive_middle(self, lyst, add_bst):
        """Recursively finds and adds middle to bst"""
        if len(lyst) > 1:
            middle = len(lyst)//2
            node = lyst[middle]
            node.set_left(None)
            node.set_right(None)
            add_bst.add(node)

            l_lyst = lyst[:middle]
            r_lyst = lyst[middle:]
            if r_lyst == lyst:
                r_lyst = []

            self.recursive_middle(l_lyst, add_bst)
            self.recursive_middle(r_lyst, add_bst)
