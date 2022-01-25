# create class with init function
from os import name


class Person :
    def __init__(self,_name,_age) :
        self.name = _name;
        self.age = _age;

# create object by perameter
person_one = Person("Md Tazri",17);
print(">>> Person Details <<<");
print("> person_one.name : ",person_one.name);
print("> person_one.name : ",person_one.age);
print(">>> Finish Details <<<");