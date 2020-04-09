#!/usr/bin/env python3

from typing import Optional

class Node:
    value: int
    next: Optional['Node']

    def __init__(self, value: int):
        self.value = value

    def __str__(self):
        return f'<{self.value}>'

    def advance(self) -> Optional['Node']:
        return self.next

    def advance_by_two(self):
        node = self.advance()
        return node.advance() if node is not None else None


graph = Node(1) # 1
graph.next = Node(2) # 1 -> 2
graph.next.next = Node(3) # 1 -> 2 -> 3
graph.next.next.next = Node(4) # 1 -> 2 -> 3 -> 4
graph.next.next.next.next = Node(5) # 1 -> 2 -> 3 -> 4 -> 5
graph.next.next.next.next.next = graph.next.next # 1 -> 2 -> 3 -> 4 -> 5 -> 3


def find_cycle_set(graph: Node) -> Optional[Node]:
    """
    Implements an O(n) space and O(n) time complexity algorithm for finding the start of a cycle.
    Just notes down which nodes were visited.
    """

    visited = set()

    current_node = graph
    while current_node is not None and current_node not in visited:
        visited.add(current_node)
        current_node = current_node.next

    return current_node


def find_cycle_floyd(graph: Node) -> Optional[Node]:
    """
    Implements an O(1) space and O(n) time complexity algorithm for finding the start of a cycle.
    Also called Floyd algorithm, shown in this video: https://www.youtube.com/watch?v=pKO9UjSeLew
    """

    ## TODO: This can be removed
    if graph.next is graph:
        return graph


    # Let them advance until they meet
    while True:
        tortoise = graph.advance()
        hare = graph.advance_by_two()

        if hare is tortoise:
            break

        if tortoise is None or hare is None:
            return None

    assert hare is tortoise

    # both met at node hare/tortoise
    # Now put hare back to start and let him run as slow as the tortoise
    # Where they meet is the point of the cycle start
    hare = graph
    while hare is not tortoise:
        hare = hare.advance()
        tortoise = tortoise.advance()

        if tortoise is None or hare is None:
            return None

    return hare


def main():
    c = find_cycle_set(graph)
    print(f'Node where the cycle started (set): {c}')

    c = find_cycle_floyd(graph)
    print(f'Node where the cycle started (floyd): {c}')

if __name__ == "__main__":
    main()