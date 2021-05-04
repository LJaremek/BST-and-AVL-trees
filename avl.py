from tree_painter import draw
from node import Node
from bst import BSTree


class AVLTree(BSTree):
    def __init__(self, elements: list = None):
        """
        Adelson-Velsky Landis Tree is a self-balancing binary search tree
        in which the height of the left and right subtrees of each node 
        differs by at most one.
        Arguments:
            - list of elements (optional)
        """
        super().__init__(elements)


    def _right_right(self, element: Node) -> tuple:
        """
        Right right rotation.
        """
        parent = element.parent()
        value = element.right_son().value()

        left_left_son = element.left_son()
        left_right_son = element.right_son().left_son()
        left_son = Node(None, element.value(), left_left_son, left_right_son)

        right_son = element.right_son().right_son()
        return parent, value, left_son, right_son


    def _left_left(self, element: Node) -> tuple:
        """
        Left left rotation.
        """
        parent = element.parent()
        value = element.left_son().value()

        right_left_son = element.left_son().right_son()
        right_right_son = element.right_son()
        right_son = Node(None, element.value(), right_left_son, right_right_son)

        left_son = element.left_son().left_son()
        return parent, value, left_son, right_son


    def _right_left(self, element: Node) -> tuple:
        """
        Right left rotation.
        """
        parent = element.parent()
        value = element.right_son().left_son().value()

        left_left_son = element.left_son()
        left_right_son = element.right_son().left_son().left_son()
        left_son = Node(None, element.value(), left_left_son, left_right_son)

        right_left_son = element.right_son().left_son().right_son()
        right_right_son = element.right_son().right_son()
        right_son = Node(None, element.right_son().value(), right_left_son, right_right_son)

        return parent, value, left_son, right_son


    def _left_right(self, element: Node) -> tuple:
        """
        Left right rotation.
        """
        parent = element.parent()
        value = element.left_son().right_son().value()

        left_left_son = element.left_son().left_son()
        left_right_son = element.left_son().right_son().left_son()
        left_son = Node(None, element.left_son().value(), left_left_son, left_right_son)

        right_left_son = element.left_son().right_son().right_son()
        right_right_son = element.right_son()
        right_son = Node(None, element.value(), right_left_son, right_right_son)

        return parent, value, left_son, right_son


    def _add_element(self, element) -> Node:
        """
        Function add element to the tree.
        """
        current_element = self._top
        while True:
            if current_element.value() <= element:
                if current_element.right_son() == None:
                    new_son = Node(current_element, element)
                    current_element.set_right_son(new_son)
                    current_element = current_element.right_son()
                    break
                else:
                    current_element = current_element.right_son()
                    continue
            elif current_element.value() > element:
                if current_element.left_son() == None:
                    new_son = Node(current_element, element)
                    current_element.set_left_son(new_son)
                    current_element = current_element.left_son()
                    break
                else:
                    current_element = current_element.left_son()
                    continue
        return current_element


    def _correct_tree(self, current_element: Node):
        """
        The function corrects the height between all nodes in the tree.
        """
        while True:
            if current_element == None or current_element.parent() == None:
                return None
            current_element = current_element.parent()
            b1 = current_element.balance()

            try:
                b2 = current_element.right_son().balance()
            except AttributeError:
                b2 = 0
            try:
                b3 = current_element.right_son().left_son().balance()
            except AttributeError:
                b3 = 0

            if b1 in (-1, 0, 1):
                if current_element.parent() == None:
                    break
                else:
                    continue
            elif ((b1 == -2 and b2 == 1 and b3 == -1) or
                  (b1 == -2 and b2 == 1 and b3 == 0 ) or
                  (b1 == -2 and b2 == 1 and b3 == 1)):
                current_element.reset(*self._right_left(current_element))
            elif b1 == -2:
                current_element.reset(*self._right_right(current_element))
                break

            try:
                b2 = current_element.left_son().balance()
            except AttributeError:
                b2 = 0
            try:
                b3 = current_element.left_son().right_son().balance()
            except AttributeError:
                b3 = 0

            if ((b1 == 2 and b2 == 2 and b3 == 2) or
                (b1 == -1 and b2 == -1 and b3 == -1) or
                (b1 == -1 and b2 == 0 and b3 == 1) or
                (b1 == 2 and b2 == -1 and b3 == 0)):
                current_element.reset(*self._left_right(current_element))
            elif b1 == 2:
                current_element.reset(*self._left_left(current_element))
                break
            
            if current_element.parent() == None:
                break


    def balance(self) -> int:
        """
        Return the balance of the tree.
        """
        if self._top == None:
            return 0
        return self._top.balance()


    def insert(self, element: Node):
        """
        Insert the element to the tree.
        """
        if self._top == None:
            self._top = Node(None, element)
            return None
        new_element = self._add_element(element)
        self._correct_tree(new_element)


    def delete(self, element):
        """
        Delete the element from the tree.
        """
        current_element = the_element = self.find(element)
        if current_element == None:
            return None
        elif current_element.parent() == current_element.left_son() == current_element.right_son() == None:
            self._top = None
            return None

        if current_element.left_son() == None and current_element.right_son() != None:
            value = current_element.right_son().value()
            left_son = current_element.right_son().left_son()
            right_son = current_element.right_son().right_son()
            parent = current_element.parent()
            current_element.reset(parent, value, left_son, right_son)

        elif current_element.right_son() == None and current_element.left_son() != None:
            value = current_element.left_son().value()
            left_son = current_element.left_son().left_son()
            right_son = current_element.left_son().right_son()
            parent = current_element.parent()
            current_element.reset(parent, value, left_son, right_son)

        elif current_element.left_son() == None == current_element.right_son():
            if current_element.parent().left_son() == current_element:
                current_element.parent().set_left_son(None)
            else:
                current_element.parent().set_right_son(None)

        else:
            current_element = current_element.left_son()
            while None != current_element.right_son():
                current_element = current_element.right_son()
            if current_element.parent().left_son() == current_element:
                current_element.parent().set_left_son(current_element.left_son())
            else:
                current_element.parent().set_right_son(None)
            the_element.set_value(current_element.value())
            
        self._correct_tree(current_element)
