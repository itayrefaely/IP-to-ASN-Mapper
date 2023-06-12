class Node:
    """
    Represents a node in the trie data structure.
    """

    def __init__(self, prefix):
        """
        Initializes an instance of the Node class with the specified prefix.

        Args:
            prefix (str): The prefix associated with the node.
        """
        self.prefix = prefix
        self.children = {}  # Stores child nodes with their respective prefixes
        self.leaf_children = {}  # Stores leaf nodes with their associated IP range and information

