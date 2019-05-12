from typing import Dict, Optional, Any, Tuple, Iterable

class TrieNode:
  children: Dict[str, 'TrieNode']
  value: Any

  def __init__(self, value: Optional[str] = None) -> None:
    self.children = {}
    self.value = value

  def __str__(self, depth=0):
    ret = str(self.value)

    for child in self.children:
      ret += '\n' + ' ' * depth + f'{child}: {self.children[child].__str__(depth + 1)}'

    return ret

class Trie:
  root: Optional[TrieNode] = None

  def __init__(self, items: Optional[Iterable[Tuple[str, Any]]] = None):
    self.root = TrieNode()

    if items is not None:
      for key, value in items:
        self.insert(key, value)

  def find_closest(self, key: str) -> Any:
    node = self.root
    current_closest = None

    for character in key:
      if character not in node.children:
        return current_closest

      node = node.children[character]

      if node.value is not None:
        current_closest = node.value

    return current_closest

  def insert(self, key: str, value: Any) -> None:
    node = self.root

    for character in key:
      if character not in node.children:
        node.children[character] = TrieNode()

      node = node.children[character]

    node.value = value

if __name__ == "__main__":
  trie = Trie()

  trie.insert('152', 1)
  trie.insert('1526', 2)
  trie.insert('1527', 3)

  print(trie.find_closest('15267'))
