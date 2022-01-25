# create parent class
class Person : 
    def __init__(self,_name,_age) :
        self.name = _name;
        self.age = _age;

# create chiled class
class Student(Person) :
    pass

# create student
student_one = Student('Md Tazri','17');

print("student_one.name : ",student_one.name);
print("student_one.age : ",student_one.age);
