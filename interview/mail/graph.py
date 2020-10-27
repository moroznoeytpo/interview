class Node:
    left: None
    right: None
    value: int


def foo(item: Node, l_max: int, r_min: int):
    if not l_max < item.value < r_min:
        raise ValueError
    if item.left:
        if item.value > item.left.value:
            foo(item.left, l_max, min(r_min, item.value))
        else:
            raise ValueError
    if item.right:
        if item.value < item.right.value:
            foo(item.left, max(l_max, item.value), r_min)
        else:
            raise ValueError


"""
        6
    4       8
1     5          9
     2   7
"""
