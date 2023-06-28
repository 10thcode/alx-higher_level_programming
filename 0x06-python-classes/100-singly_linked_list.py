#!/usr/bin/python3
""" Utility for singly linked list node """


class Node:
    """ Singly linked list node utility """
    def __init__(self, data, next_node=None):
        """
        Constructs a Node for a singly linked list

        Args:
            data (int): value of the node
            next_node (Node): the next node
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """ Retrieves __data attribute """
        return self.__data

    @data.setter
    def data(self, value):
        """
        Sets __data value

        Args:
            value (int): the value to be assigned to data
        """
        if type(value) is int:
            self.__data = value
        else:
            raise TypeError("data must be an integer")

    @property
    def next_node(self):
        """ Retrieves __next_node attribute """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Sets the value for __next_node

        Args:
            value (Node): the next node of the linked list
        """
        if type(value) is Node or value is None:
            self.__next_node = value
        else:
            raise TypeError("next_node must be a Node object")


class SinglyLinkedList:
    """ Utility for Singly Linked List """
    def __init__(self):
        """ Constructs a singly linked list """
        self.__head = None

    def __str__(self):
        """ prints all element in a singly linked list """
        elements = ""
        node = self.__head
        while node:
            elements += str(node.data) + "\n"
            node = node.next_node
        return elements[:-1]

    def sorted_insert(self, value):
        """
        Inserts a new Node into the correct sorted position in the list

        Args:
            value (int): the value to be assigned to a Node data
        """
        if type(value) == int:

            # if list is empty
            if self.__head is None:
                new_node = Node(value, None)
                self.__head = new_node
                return None

            # if value is the smallest
            if self.__head.data >= value:
                new_node = Node(value, self.__head)
                self.__head = new_node
                return None

            # value is at least bigger that first element
            node = self.__head
            while node.next_node:
                if node.next_node.data >= value:
                    new_node = Node(value, node.next_node)
                    node.next_node = new_node
                    return None
                node = node.next_node

            # value is bigger that all element in the list
            # therefore, value should be inserted at the end of the list
            new_node = Node(value, None)
            node.next_node = new_node
        else:
            raise TypeError("data must be an integer")
