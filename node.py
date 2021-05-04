from __future__ import annotations


class Node:
    def __init__(self, parent: Node, value, left_son: Node = None, right_son: Node = None):
        self._parent = parent
        self._value = value
        self._left_son = left_son
        if self._left_son != None:
            self._left_son.set_parent(self)
        self._right_son = right_son
        if self._right_son != None:
            self._right_son.set_parent(self)
        self._x = self._y = 0


    def __str__(self) -> str:
        return str(self._value)


    def set_value(self, new_value):
        """
        Set the new value of the Node.
        """
        self._value = new_value


    def value(self):
        """
        Return the value of the node.
        """
        return self._value


    def left_height(self) -> int:
        """
        Return height of the left side.
        """
        if self._left_son == None:
            return 0
        l_options = [(self._left_son,  0)]
        l_results = []
        while l_options != []:
            element, b = l_options.pop(0)
            if element == None:
                l_results.append((element, b))
            else:
                b += 1
                l_options.append((element.left_son(), b))
                l_options.append((element.right_son(), b))
        l_result = max(l_results, key = lambda x: x[1])[1]
        return l_result


    def right_height(self) -> int:
        """
        Return height of the right side.
        """
        if self._right_son == None:
            return 0
        r_options = [(self._right_son, 0)]
        r_results = []
        while r_options != []:
            element, b = r_options.pop(0)
            if element == None:
                r_results.append((element, b))
            else:
                b += 1
                r_options.append((element.left_son(), b))
                r_options.append((element.right_son(), b))
        r_result = max(r_results, key = lambda x: x[1])[1]

        return r_result


    def height(self) -> int:
        """
        Return the height of the node.
        """
        return max((self.left_height(), self.right_height()))


    def deep(self) -> int:
        """
        Return distance to the top.
        """
        if self.parent() == None:
            return 0
        deep = 0
        current_node = self
        while current_node.parent() != None:
            deep += 1
            current_node = current_node.parent()
        return deep


    def balance(self) -> int:
        """
        Return the balance of the node.
        """
        return self.left_height() - self.right_height()


    def parent(self) -> Node:
        """
        Return the parent of the node.
        If the parent is None then the node is the top of the tree.
        """
        return self._parent


    def set_parent(self, new_parent: Node):
        """
        Set new parent.
        """
        self._parent = new_parent


    def left_son(self) -> Node:
        """
        Return the left son of the node.
        If the son is None it means that the son not exist.
        """
        return self._left_son


    def set_left_son(self, new_son: Node):
        """
        Set new left son.
        """
        self._left_son = new_son
        if new_son != None:
            self._left_son.set_parent(self)


    def right_son(self) -> Node:
        """
        Return the right son of the node.
        If the son is None it means that the son not exist.
        """
        return self._right_son


    def set_right_son(self, new_son: Node):
        """
        Set new right son.
        """
        self._right_son = new_son
        if new_son != None:
            self._right_son.set_parent(self)


    def reset(self, parent: Node, value, left_son: Node = None, right_son: Node = None):
        """
        Function set completly new parameters in Node.
        """
        self._parent = parent
        self._value = value
        self._left_son = left_son
        try:
            self._left_son.set_parent(self)
        except AttributeError:
            pass
        self._right_son = right_son
        try:
            self._right_son.set_parent(self)
        except AttributeError:
            pass


    def is_leaf(self):
        """
        Returns true if Node is leaf in tree
        """
        if self._right_son == None == self._left_son:
            return True
        return False


    def one_son(self):
        """
        Returns true if node has only one son
        """
        sons = 0
        if self._right_son != None:
            sons+=1
        if self._left_son != None:
            sons+=1
        if sons == 1:
            return True
        return False


    def set_x(self, new_x: float):
        """
        Set new x.
        """
        self._x = new_x


    def x(self) -> float:
        """
        Return x.
        """
        return self._x


    def set_y(self, new_y: float):
        """
        Set new y.
        """
        self._y = new_y


    def y(self) -> float:
        """
        Return y.
        """
        return self._y
