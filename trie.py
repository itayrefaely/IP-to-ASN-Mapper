from node import Node

class Trie:
    """
    Represents a trie data structure used to store IP ranges and their corresponding ASN information.
    """

    def __init__(self):
        """
        Initializes an instance of the Trie class with an empty root node.
        """
        self.root = Node(prefix='')

    def insert(self, ip_range, asn, country, as_name):
        """
        Inserts an IP range and its associated ASN, country, and AS name into the trie.

        Args:
            ip_range (tuple): A tuple containing the start and end IP addresses of the range.
            asn (str): The ASN (Autonomous System Number) associated with the IP range.
            country (str): The country associated with the IP range.
            as_name (str): The AS (Autonomous System) name associated with the IP range.
        """
        parent = self.root

        # Assign the start and end values of the interval to variables as strings
        start, end = ip_range

        # Start and end have a different number of digits
        if len(start) < len(end):
            self.root.leaf_children[(int(start), int(end))] = {"ASN": int(asn), "Country": country, "AS name": as_name}

        # Same number of digits
        for i in range(len(start)):
            if start[i] == end[i]:
                prefix = start[:i+1]

                # Check if the prefix exists as a child of the current parent node
                if not parent.children.get(prefix):
                    # Create a new node and update parent
                    child = Node(prefix=prefix)
                    parent.children[prefix] = child
                    parent = child
                
                else:
                    parent = parent.children[prefix]

            # Start[i] != end[i]
            else: 
                # Add the IP range and its associated information to the leaf children of the parent node
                parent.leaf_children[(int(start), int(end))] = {"ASN": int(asn), "Country": country, "AS name": as_name}
                break

    
    def getASN(self, ip_address):
        """
        Retrieves the ASN for the given IP address by traversing the trie.

        Args:
            ip_address (str): The IP address to retrieve the ASN for.

        Returns:
            int: The ASN (Autonomous System Number) associated with the IP address.

        Raises:
            ValueError: If the IP address is not found in the trie or not routed.
        """
        ip_address_int = int(ip_address)
        parent = self.root
        for i in range(len(ip_address)):
            # Check if the IP address falls within any of the leaf intervals of the parent node
            for start, end in parent.leaf_children.keys():
                if start <= ip_address_int <= end:
                    asn = parent.leaf_children[(start, end)].get("ASN")
                    # if ASN is 0, then the ip address is not routed, therefore not valid 
                    if not asn:
                        raise ValueError("IP address is not routed")
                    return asn

            # IP address not found in parent's interval children
            prefix = ip_address[:i+1]
            found_child = False
            for child_prefix, child in parent.children.items():
                # Check if there is a child node with a matching prefix
                if prefix == child_prefix:
                    parent = child
                    found_child = True
                    break

            # If no child node is found with the matching prefix, the IP address is invalid
            if not found_child:
                raise ValueError("Invalid IP address")

        # If the IP address traversal is completed but no ASN is found, the IP address is invalid
        raise ValueError("Invalid IP address")
