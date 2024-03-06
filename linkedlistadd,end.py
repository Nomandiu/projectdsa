class Node:
    def __init__(self, item):
        self.data = item
        self.next = None

class Linked_list:
    def __init__(self):
        self.head = None

    def display(self):
        temp = self.head
        while temp is not None:
            print(temp.data)
            temp = temp.next

    def add(self, item):
        new_node = Node(item)

        if self.head is None:
            self.head = new_node
        else:
            last_node = self.head
            while last_node.next is not None:
                last_node = last_node.next
            last_node.next = new_node

    def add_at_beginning(self, item):
        new_node = Node(item)
        new_node.next = self.head
        self.head = new_node

    def add_in_middle(self, position, item):
        if position <= 1:
            print("Invalid position.")
            return

        new_node = Node(item)

        

        current_node = self.head
        count = 1
        while current_node is not None and count < position-1:
            current_node = current_node.next
            count += 1

        if current_node is None:
            print("Invalid position.")
            return

        new_node.next = current_node.next
        current_node.next = new_node

    def add_at_end(self, item):
        self.add(item)  # Reusing the existing add method

ll = Linked_list()
n = int(input("Enter the number of nodes: "))

for i in range(n):
    data = input("Enter the data for node {}: ".format(i + 1))
    ll.add(data)

ll.display()
n=int(input("enter 1 to add in first\nenter 2 to add in middle\nenter 3 to add in end\nenter the number:"))

if n==1:
    new_num_beginning = input("Enter the new number to add at the beginning: ")
    ll.add_at_beginning(new_num_beginning)
elif n==2:
    position = int(input("Enter the position to add the new number: "))
    new_num_middle = input("Enter the new number to add in the middle: ")
    ll.add_in_middle(position, new_num_middle)
elif n==3:
    new_num_end = input("Enter the new number to add at the end: ")
    ll.add_at_end(new_num_end)
else:
    print("invalid")
ll.display()
            
