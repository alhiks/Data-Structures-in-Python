# A linked list node
class Node:

    # Constructor to initialize a new node with data
    def __init__(self, new_data):
        self.data = new_data
        self.next = None


# Function to traverse and print the singly linked list
def traverseList(head):
    # A loop that runs till head is nullptr
    while head is not None:
        # Printing data of current node
        print(head.data, end=" ")

        # Moving to the next node
        head = head.next
    print()


# Driver code
def main():
    # Create a hard-coded linked list:
    # 10 -> 20 -> 30 -> 40
    head = Node(10)
    head.next = Node(20)
    head.next.next = Node(30)
    head.next.next.next = Node(40)

    # Example of traversing the node and printing
    traverseList(head)


if __name__ == "__main__":
    main()
