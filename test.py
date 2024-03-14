import pytest

import main

@pytest.fixture()
def initialised_linked_list():
    linked_list = main.LinkedList()

    # Assign item values
    linked_list.head = main.Node(1)
    second = main.Node(2)
    third = main.Node(3)

    # Connect nodes
    linked_list.head.next = second
    second.next = third

    return linked_list, second, third

def test_traverse(initialised_linked_list):
    assert initialised_linked_list[0].traverse() == [1,2,3]

def test_insert_start(initialised_linked_list):
    initialised_linked_list[0].insert_start(0)
    assert initialised_linked_list[0].traverse() == [0,1,2,3]

def test_insert_end(initialised_linked_list):
    initialised_linked_list[0].insert_end(4)
    assert initialised_linked_list[0].traverse() == [1,2,3,4]

def test_insert(initialised_linked_list):
    initialised_linked_list[0].insert(9, initialised_linked_list[1])
    assert initialised_linked_list[0].traverse() == [1,2,9,3]

def test_delete_start(initialised_linked_list):
    initialised_linked_list[0].delete_start()
    assert initialised_linked_list[0].traverse() == [2,3]

def test_delete_end(initialised_linked_list):
    initialised_linked_list[0].delete_end()
    assert initialised_linked_list[0].traverse() == [1,2]

def test_delete(initialised_linked_list):
    initialised_linked_list[0].delete(initialised_linked_list[1])
    assert initialised_linked_list[0].traverse() == [1,3]