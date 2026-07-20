class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next is not None:
            current = current.next

        current.next = new_node

    def insert_after(self, target, data):
        if target is None:
            return

        new_node = Node(data)
        new_node.next = target.next
        target.next = new_node

    def delete(self, target):
        if self.head is None:
            return False

        if self.head is target:
            self.head = self.head.next
            return True

        current = self.head
        while current.next is not None:
            if current.next is target:
                current.next = current.next.next
                return True

            current = current.next

        return False

    def search(self, data):
        current = self.head

        while current is not None:
            if current.data == data:
                return current

            current = current.next

        return None

    def size(self):
        count = 0
        current = self.head

        while current is not None:
            count = count + 1
            current = current.next

        return count

    def to_list(self):
        items = []
        current = self.head

        while current is not None:
            items.append(current.data)
            current = current.next

        return items

    def print(self):
        current = self.head

        while current is not None:
            print(current.data)
            current = current.next

