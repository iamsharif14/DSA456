# in this assignment used sentinal node with doubly linkedlist

class Node:
    def __init__(self, data, next = None, prev = None) -> None:
        self.data = data
        self.next = next
        self.prev = prev

    def get_data(self):
        return self.data

class LinkedList:
    def __init__(self, front = None, back = None) -> None:
        # Sentinel nodes do not store actual list values.
        self.front = Node(None)
        self.back = Node(None)

        # Connect the two sentinel nodes.
        self.front.next = self.back
        self.back.prev = self.front

        self.size = 0

    
    def show(self):
        current = self.front.next

        while current != self.back:
            print(current.data, end=" ")
            current = current.next

        print()

    def get_front(self):
        # The list is empty.
        if self.front.next is self.back:
            return None

        return self.front.next.data

    def get_back(self):
        # The list is empty.
        if self.back.prev is self.front:
            return None

        return self.back.prev.data

    
    def insert_front(self, data):

        new_node = Node(data)

        new_node.next = self.front.next
        new_node.prev = self.front

        self.front.next.prev = new_node
        self.front.next = new_node

        self.size += 1
 
    
    def insert_back(self, data):

        new_node = Node(data)

        new_node.prev = self.back.prev
        new_node.next = self.back

        self.back.prev.next = new_node
        self.back.prev = new_node

        self.size += 1
 

    def insert(self, data):

        current = self.front.next

        while current != self.back and current.data < data:
            current = current.next

        new_node = Node(data)

        new_node.next = current
        new_node.prev = current.prev

        current.prev.next = new_node
        current.prev = new_node

        self.size += 1
       

    def remove(self, data):

        current = self.front.next

        while current != self.back:

            if current.data == data:

                current.prev.next = current.next
                current.next.prev = current.prev

                self.size -= 1
                return True

            current = current.next

        return False
        

    def is_present(self, data):
        current = self.front.next

        while current != self.back:

            if current.data == data:
                return True

            current = current.next

        return False


    def __len__(self):
        return self.size
    

# Testing
def main():
    numbers = LinkedList()

    numbers.insert(30)
    numbers.insert(10)
    numbers.insert(40)
    numbers.insert(20)

    print("Sorted list:")
    numbers.show()

    print("Front value:", numbers.get_front())
    print("Back value:", numbers.get_back())
    print("List length:", len(numbers))

    print("Is 20 present?", numbers.is_present(20))
    print("Is 50 present?", numbers.is_present(50))

    print("Remove 20:", numbers.remove(20))
    print("List after removing 20:")
    numbers.show()


main()