from typing import Optional, List, Any, Dict, Iterable


"""
Необходимо дерево обойти в ширину:
        a
    b   c   d
  e f   g   h i
  j
  k l
  
a b c d e f g h i j k l
"""
tree_data = [
    {'id': 1, 'data': {'name': 'a'}, 'children_ids': [2, 3, 4]},
    {'id': 2, 'data': {'name': 'b'}, 'children_ids': [5, 6], 'parent_id': 1},
    {'id': 3, 'data': {'name': 'c'}, 'children_ids': [7], 'parent_id': 1},
    {'id': 4, 'data': {'name': 'd'}, 'children_ids': [8, 9], 'parent_id': 1},
    {'id': 5, 'data': {'name': 'e'}, 'children_ids': [10], 'parent_id': 2},
    {'id': 6, 'data': {'name': 'f'}, 'children_ids': [], 'parent_id': 2},
    {'id': 7, 'data': {'name': 'g'}, 'children_ids': [], 'parent_id': 3},
    {'id': 8, 'data': {'name': 'h'}, 'children_ids': [], 'parent_id': 4},
    {'id': 9, 'data': {'name': 'i'}, 'children_ids': [], 'parent_id': 4},
    {'id': 10, 'data': {'name': 'j'}, 'children_ids': [11, 12], 'parent_id': 5},
    {'id': 11, 'data': {'name': 'k'}, 'children_ids': [], 'parent_id': 10},
    {'id': 12, 'data': {'name': 'l'}, 'children_ids': [], 'parent_id': 10},
]


class TreeNode:
    id: int
    data: Dict[str, Any]
    children_ids: List[int]
    parent_id: Optional[int]

    def __init__(self, data):
        self.id = data.get('id')
        self.data = data.get('data', {})
        self.children_ids = data.get('children_ids', [])
        self.parent_id = data.get('parent_id')


class Tree:
    def __init__(self):
        self._tree = {}
        self._levels = {}

    def load_tree(self, data: list):
        for item in data:
            tree_node_obj = TreeNode(item)
            self._tree[tree_node_obj.id] = tree_node_obj

    def _collect_tree(self, node_id: int = 1, level: int = 0):
        node_obj = self._tree[node_id]
        if not self._levels.get(level):
            self._levels[level] = []
        self._levels[level].append(node_obj.data['name'])

        for children_id in node_obj.children_ids:
            self._collect_tree(children_id, level + 1)

    def iterate_down_from_node(self, node_id: int) -> Iterable[TreeNode]:  # напишите
        self._collect_tree(node_id)
        for level in self._levels.values():
            for item_id in level:
                yield item_id


tree_obj = Tree()
tree_obj.load_tree(tree_data)

assert list(tree_obj.iterate_down_from_node(1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l']
