class SLLNode:

    def __init__(self, data):
        self.data = data
        self.next = None #set None since at the beginning its not pointing anywhere

    def __repr__(self):  #<__main__.SLLNode object at 0x000001C5A3D67D00> overrides to give readable representation
        return "SLLNode object is {}".format(self.data)   

    def get_data(self):
        return self.data

    def set_data(self, new_data):
        self.data = new_data #replaces the existing data with new data

    def get_next(self):
        return self.next

    def set_next(self, new_next):
        self.next = new_next #replaces the next data with new next 


class SLL:

    def __init__(self):
        self.head = None #HEAD = None since there exist no node athe beginning

    def __repr__(self):
        return " SLL Object {}".format(self.head)

    def is_empty(self):
        return self.head is None #returns true if LL is empty

    def add_front(self, new_data):
        temp = SLLNode(new_data)
        temp.set_next(self.head)
        self.head = temp

    def size(self):
        size = 0
        if self.head is None:
            return 0
        current = self.head 
        while current != None :
            size +=1
            current = current.get_next() #current also is a node so we could use the methods
        return size        

    def search(self, data):
        if self.head is None:
            return " empty linked list"
        
        current = self.head
        while current is not None:
            if current.get_data() == data: #if searched data matches the current value return true
                return True
            else:
                current = current.get_next() #else check the next value

        return False #if not found return false

    def remove(self, data):
        if self.head is None:
            return "Linked list is empty nothing to remove here"

        current = self.head
        previous = None
        found = False
        while not found:
            if current.get_data() == data:
                found = True
            else:
                if current.get_next() == None:
                    return "A node with that data value is not present"
                else:
                    previous = current
                    current = current.get_next()
                

        if previous is None:
            self.head = current.get_next()
        else:    
            previous.set_next(current.get_next())                        


"""                REMOVE DOCSTRING TO CHECK IF IT IS_EMPTY       

sl1 = SLL()
print(sl1.is_empty())
node1 = SLLNode(1)
sl1.head = node1
print(sl1.is_empty())

"""

'''             REMOVE DOCSTRING TO ADD NEW NODE IN FRONT

sl1 = SLL()
sl1.add_front("Varun")
print(sl1.head)

'''

"""         REMOVE DOCSTRING TO CHECK THE SIZE OF LINKED LIST (TRAVERSE LL AND RETURNS SIZE)
TIME COMPLEXITY IS O(n) Every node needs to be visited to calc size

sl1 = SLL()
print(sl1.size()) #0
sl1.add_front("Varun")
sl1.add_front("arun")
sl1.add_front("Kiran")
print(sl1.size())

"""

'''        REMOVE DOCSTRING TO SEARCH , RETURNS TRUE IF SEARCHED ITEM EXISTS AND FALSE FOR VICE VERSA
TIME COMPLEXITY O(n)

sl1 = SLL()
print(sl1.search(2))    #empty 
sl1.add_front(1)
sl1.add_front(2)
print(sl1.search(2))    #true
print(sl1.search(5))    #false


'''

"""  TO REMOVE A NODE

sl1 = SLL()
print(sl1.remove(2)) #ll empty
sl1.add_front("hello")
sl1.add_front("hell")
sl1.add_front("hel")
sl1.add_front("he")
# print(sl1.head)
# print(sl1.remove("head")) #a node with that data vlaue do not exixt
print(sl1.remove("hel"))
print(sl1.head.next)


"""
















# node1 = SLLNode("hello")
# node2 = SLLNode("world")
# node1.set_next(node2)
# print(node1.get_next())
# # print(node1.get_data())

      
