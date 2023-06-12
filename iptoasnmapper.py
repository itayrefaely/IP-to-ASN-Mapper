from trie import Trie

class IPtoASNMapper:
    """
    Represents an IP-to-ASN mapper that loads mapping data and performs lookups.
    """

    def __init__(self, filename):
        """
        Initializes an instance of the IPtoASNMapper class by loading mapping data from the specified file.

        Args:
            filename (str): The name of the file containing the IP-to-ASN mapping data.
        """
        self.mapping_data = Trie()  # Initialize a Trie instance to store the mapping data
        self.load_mapping_data(filename)  # Load the mapping data from the specified file
    
    def load_mapping_data(self, filename):
        """
        Loads the mapping data from the specified file into the mapping_data trie.

        Args:
            filename (str): The name of the file containing the IP-to-ASN mapping data.
        """
        with open(filename, 'r') as file:
            for line in file:
                # Split the line into individual parts based on tab delimiter
                parts = line.strip().split('\t')

                # Extract the start IP, end IP, ASN, country, and AS name from the parts
                start_ip = parts[0]
                end_ip = parts[1]
                asn = parts[2]
                country = parts[3]
                as_name = parts[4]

                # Add the IP range and its associated information to the mapping_data Trie
                self.mapping_data.insert((start_ip, end_ip), asn, country, as_name)



    def lookUp(self, ip_address):
        """
        Performs a lookup for the given IP address and prints the corresponding ASN.

        Args:
            ip_address (str): The IP address to perform the lookup for.
        """
        asn = self.mapping_data.getASN(ip_address)
        print(f"ASN: {asn}")
