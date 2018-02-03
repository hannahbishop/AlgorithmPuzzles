class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    def setNext(self, node):
        self.next = node

def print_list(start):
    curr = start
    while(curr != None):
        print(curr.value)
        curr = curr.next
    return

def find_first_node(start):
    seen = {}
    curr = start
    while(curr != None):
        if(curr.value in seen):
            return curr
        else:
            seen[curr.value] = True
            curr = curr.next

def main():
    one = Node(1)
    two = Node(2)
    three = Node(3)
    four = Node(4)
    five = Node(5)
    six = Node(6)
    
    one.setNext(two)
    two.setNext(three)
    three.setNext(four)
    four.setNext(five)
    five.setNext(six)
    six.setNext(five)
    
    print(find_first_node(one).value)

main()