import pytest

import main

@pytest.fixture
def initialised_linked_list():
    linked_list = main.LinkedList()

    # Assign item values
    linked_list.head = main.Node(1)
    second = main.Node(2)
    third = main.Node(3)

    # Connect nodes
    linked_list.head.next = second
    second.next = third

    return linked_list

def test_traverse(initialised_linked_list):
    assert initialised_linked_list.traverse() == [1,2,3]