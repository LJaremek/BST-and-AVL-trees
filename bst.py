from tree_painter import draw
from node import Node


class BSTree:
    def __init__(self, elements: list = None):
        """
        Binary Search Tree has internal nodes each store a key 
        greater than all the keys in the node's left subtree 
        and less than those in its right subtree.
        Arguments:
            - list of elements (optional)
        """
        if elements == None:
            elements = []

        self._top = None
        for element in elements:
            self.insert(element)


    def __str__(self):
        """
        Draw the tree.
        """
        draw(self)


    def __iter__(self):
        for node in self._make_list():
            yield node


    def _gen_numbers_from_branch(self, start_element: Node) -> list:
        """
        Function return the branch as sorted list.
        """
        numbers = []
        nodes = []
        current_element = start_element
        while current_element.parent() != None: # top
            if None != current_element.left_son() not in nodes:
                current_element = current_element.left_son()
            elif None != current_element.right_son() not in nodes:
                numbers.append(current_element.value())
                nodes.append(current_element)
                current_element = current_element.right_son()
            else:
                if current_element not in nodes:
                    nodes.append(current_element)
                    numbers.append(current_element.value())
                current_element = current_element.parent()
        return numbers


    def _make_list(self) -> list:
        """
        Function return the tree as sorted list.
        """
        current_element = self._top
        if self._top == None:
            return []
        while current_element.left_son() != None:
            current_element = current_element.left_son()
        
        numbers = self._gen_numbers_from_branch(current_element)
        numbers.append(self._top.value())

        current_element = self._top.right_son()
        if current_element == None:
            return numbers
        while current_element.left_son() != None:
            current_element = current_element.left_son()
        numbers += self._gen_numbers_from_branch(current_element)

        return numbers


    def top(self) -> Node:
        """
        Return the node on the top of the tree.
        """
        return self._top


    def height(self) -> int:
        """
        Return the height of the tree.
        """
        if self._top == None:
            return 0
        return self._top.height()


    def insert(self, element):
        """
        Insert the element to the tree.
        """
        if self._top == None:
            self._top = Node(None, element)
            return None
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


    def delete(self, element):
        """
        Delete the element from the tree.
        """
        if self.find(element) == None:
            return None
        actual_node = self._top
        while actual_node.value() != element:
            if element >= actual_node.value():
                actual_node = actual_node.right_son()
            else:
                actual_node = actual_node.left_son()
        parent = actual_node.parent()
        if actual_node.is_leaf():
            if actual_node == self._top:
                self._top == None
            else:
                if parent.left_son() == actual_node:
                    parent.set_left_son(None)
                elif parent.right_son() == actual_node:
                    parent.set_right_son(None)
        elif actual_node.one_son():
            if actual_node.right_son() != None:
                son = actual_node.right_son()
            else:
                son = actual_node.left_son()
            if actual_node == self._top:
                self._top == son
            else:
                if parent.right_son() == actual_node:
                    parent.set_right_son(son)
                else:
                    parent.set_left_son(son)
        else:
            next_node = actual_node.right_son()
            while None != next_node.left_son():
                next_node = next_node.left_son()
            if next_node.parent().right_son() == next_node:
                next_node.parent().set_right_son(None)
            else:
                next_node.parent().set_left_son(None)
            if actual_node == self._top:
                self._top = next_node
            else:
                if parent.right_son() == actual_node:
                    parent.set_right_son(next_node)
                else:
                    parent.set_left_son(next_node)
            if next_node.right_son() != None:
                next_node.parent().set_left_son(next_node.right_son())
            next_node.set_left_son(actual_node.left_son())
            next_node.set_right_son(actual_node.right_son())


    def find(self, element):
        """
        Function return the Node or None if there are not the element.
        """
        current_element = self._top
        if current_element == None:
            return None
        if element == self._top.value():
            return self._top
        while True:
            if current_element.value() <= element:
                current_element = current_element.right_son()
                if current_element == None:
                    return None
                elif current_element.value() == element:
                    return current_element
            else:
                current_element = current_element.left_son()
                if current_element == None:
                    return None
                elif current_element.value() == element:
                    return current_element
