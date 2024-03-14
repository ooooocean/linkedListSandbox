class Node:
    def __init__(self, item):
        self.item = item
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def traverse(self):
        temp = self.head
        x = []
        print('List of elements in linked list:')
        while temp:
            value = temp.item
            print(f'{value}')
            x.append(value)
            temp = temp.next
        return x


if __name__ == '__main__':
    # initialise linked list with some values
    linked_list = LinkedList()

    # Assign item values
    linked_list.head = Node(1)
    second = Node(2)
    third = Node(3)

    # Connect nodes
    linked_list.head.next = second
    second.next = third
