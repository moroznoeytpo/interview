"""
e1 -> e2 -> e3 -> None
e1.next = e2
e2.next = e3
e3.next = None


e3 -> e2 -> e1 -> None
e3.next = e2
e2.next = e1
e1.next = None
"""


class Node:
    def __init__(self, name: str):
        self.name = name
        self.next = None
        self.prev = None


def reverse(node: Node, level: int = 0) -> Node:
    if node.next:
        last = node.next
        if level == 0:
            node.next = None
        last.prev = node
        node.next = node.prev
        return reverse(last, level+1)
    else:
        node.next = node.prev
        return node


e1 = Node(name='e1')
assert reverse(e1) == e1

e1 = Node(name='e1')
e2 = Node(name='e2')
e1.next = e2
value = reverse(e1)
assert value == e2
assert value.next == e1
assert not value.next.next

e1 = Node(name='e1')
e2 = Node(name='e2')
e3 = Node(name='e3')
e4 = Node(name='e4')
e1.next = e2
e2.next = e3
e3.next = e4
value = reverse(e1)

assert value == e4
assert value.next == e3
assert value.next.next == e2
assert value.next.next.next == e1
assert not value.next.next.next.next
