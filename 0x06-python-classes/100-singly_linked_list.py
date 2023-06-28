#!/usr/bin/python3
"""Defines a class node"""


class Node:
    """Defines a class Node"""
    def __init__(self, data, next_node=None):
        """Initializes attributes

        Args:
            data(int): "The data part of a node structure"
            next_node(node): "A node structure"
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Accesses data"""
        return (self.__data)

    @data.setter
    def data(self, value):
        """Sets data value"""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """ Accesses next node"""
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        """Sets node parameters"""
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList():
    """Defines a singly linked list"""
    def __init__(self):
        """Initializes attributes"""
        self.__head = None

    def sorted_insert(self, value):
        """Inserts a new node into a singky linked list in an ordered position
        (ascending order)

        Args: Value(Node): A node structure
        """
        new = Node(value)
        if self.__head is None:
            new.next_node = None
            self.__head = new
        elif self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
        else:
            current = self.__head
            while(current.next_node is not None and
                    current.next_node.data < value):
                current = current.next_node
            new.next_node = current.next_node
            current.next_node = new

    def __str__(self):
        """Defines a print representation of a singly-linked list"""
        values = []
        current = self.__head

        while(current is not None):
            values.append(str(current.data))
            current = current.next_node
        return ('\n'.join(values))
