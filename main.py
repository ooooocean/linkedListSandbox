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
        # if input node is not valid, throw error
        if not prev_node:
            print("Node must be in the linked list.")
            return

        # create node for new item
        new_node = Node(item)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_start(self):
        self.head = self.head.next

    def delete_end(self):
        # traverse to node before the end. construct a temporary node
        temp = self.head
        print(f'before loop, next is {temp.next.item}')
        while temp.next.next:
            temp = temp.next

        # while loop ends once we reach second to last node.
        temp.next = None

    def delete(self, node_to_delete):
        # traverse to node
        current = self.head
        # define variable which checks next node
        subsq = current.next
        print(current.item)
        while not subsq == node_to_delete:
            # check if the node after current is the same as the one to be deleted
            # if not, then reassign current and subsequent node

            if not current.next:
                # if we reach the final element, we break the loop
                print(f'Node must be in linked list.')
                return
            current = current.next
            subsq = subsq.next
        # once we break the while loop, assign the initial pointer to the pointer that
        # the deleted pointer was looking at
        current.next = node_to_delete.next

    def search(self, index_to_find):
        current = self.head
        count = 0
        while current:
            count += 1
            print(f'count is {count}')
            if count == index_to_find:
                return current.item
            current = current.next
        return None

    def bubble_sort(self, head):
        # initialise pair of elements for comparison
        current = head
        subsq = Node(None)

        if head is None:
            # this indicates end of the sort
            print(f'Please specify the head as the input.')
            return
        else:
            # iterate through the list
            while current is not None:
                # assign the index to be the subsequent value
                subsq = current.next

                # for each pair of elements, iterate until the second of the pair is None
                # this indicates the end of the list
                while subsq is not None:
                    if current.item > subsq.item:

                        # if first element is greater, swap values but retain linking
                        current.item, subsq.item = subsq.item, current.item

                    # otherwise, move to next pair
                    subsq = subsq.next
                current = current.next






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
