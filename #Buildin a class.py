#Buildin a class

class Student: #parent class

    def __init__(self,name,id,department):
        self.name = name
        self.id = id
        self.department = department

    def eligible(self):
        print(f'{self.name} with {self.id}id no is eligible to write the exams')    

class Btech(Student): #inherits from Student class
    def degree(self):
        print(f"{self.name} with id no {self.id} has a Btech degree")

class Msc(Student): #inherits from Student class
    def degree(self):
        print(f"{self.name} with id no {self.id} has a Msc degree")        
######################################################################################
# student1 = Student("varun",34,"cse")    
# student2 = Student("Adnan",50,"cse")    #Normal
# student1.eligible())
# student2.eligible())
#######################################################################################
#################################################################################################
student1 = Btech("Varun",5,"cse")
student2 = Msc("Arun",50,"IT")             #inheritance
student1.degree()
student2.degree()
#################################################################################################
