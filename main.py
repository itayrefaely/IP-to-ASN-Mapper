from iptoasnmapper import IPtoASNMapper

def main():
    """
    Entry point of the program for performing IP-to-ASN lookups.
    """
    # Create an instance of IPtoASNMapper and load the mapping data
    mapper = IPtoASNMapper('ip2asn-v4-u32.tsv')

    while True:
        # Prompt the user for input
        print('Please enter an IP address containing only digits, or type "q" to exit')
        user_input = input()

        try:
            # Check if the input is empty
            if not user_input:
                raise ValueError("Empty input")

            # Break the loop if the user typed "q"
            if user_input == "q":
                break

            # Check if the input contains characters other than digits
            if not user_input.isdigit():
                raise ValueError("Address must contain only digits")

            # Perform the IP-to-ASN lookup
            mapper.lookUp(user_input)
        
        except ValueError as err:
            # Print the error message
            print("Error:", err)


if __name__ == "__main__":
    main()
