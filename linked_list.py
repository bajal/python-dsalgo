class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    # If the LinkedList already has a head, iterate through the next reference in every 
    # Element until you reach the end of the list. Set next for the end of the list to be the new_element. 
    # Alternatively, if there is no head already, you should just assign new_element 
    # to it and do nothing else.    
    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    def print_list(self):
        current = self.head
        data = ""
        while current:
            data = data + str(current.value) + ","
            current = current.next
        return data

    def get_position(self, pos):
        current = self.head
        counter = 1
        while current.next:            
            if(counter == pos):
                break
            current = current.next
            counter += 1
        return current

    def insert(self, new_element, pos):
        current = self.head
        if self.head:
            counter = 1
            while current.next:
                if(counter == pos-1):
                    break
                counter +=1
                current = current.next
            #print("->",current.value, current.next)
            new_element.next = current.next
            current.next = new_element
        else:
            self.head = new_element

    def delete(self, val):
        if(self.head.value == val):
            self.head = self.head.next
            return
        current = self.head
        while current:
            if(current.value == val):
                current.next = current.next.next
                break
            current = current.next

# Test cases
# Set up some Elements
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)

# Start setting up a LinkedList
ll = LinkedList(e1)
ll.append(e2)
ll.append(e3)

# Test get_position
# Should print 3
print ll.head.next.next.value
# Should also print 3
print ll.get_position(3).value

#print ll.print_list()
# Test insert
ll.insert(e4,3)
#ll.insert(e4,1)
#print ll.print_list()

# Should print 4 now
print ll.get_position(3).value
print ll.print_list()
# Test delete
ll.delete(1)
# Should print 2 now
print ll.get_position(1).value
# Should print 4 now
print ll.get_position(2).value
# Should print 3 now
print ll.get_position(3).value  