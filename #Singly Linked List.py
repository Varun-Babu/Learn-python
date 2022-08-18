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

node1 = SLLNode("hello")
node2 = SLLNode("world")
node1.set_next(node2)
print(node1.get_next())
# print(node1.get_data())

      
