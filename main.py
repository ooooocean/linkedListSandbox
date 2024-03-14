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

    def insert_start(self, item):
        # create node for new item
        new_node = Node(item)

        # assign pointer for item
        new_node.next = self.head

        # make this new node the new head
        self.head = new_node

    def insert_end(self, item):
        # create node for new item
        new_node = Node(item)

        # traverse to last node and store in memory
        temp = self.head
        while temp.next:
            temp = temp.next

        # once last node located, assign next to be new node
        temp.next = new_node

    def insert(self, item, prev_node):
        # create node for new item
        new_node = Node(item)
        new_node.next = prev_node.next
        prev_node.next = new_node



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
