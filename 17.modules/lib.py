# create some function and variable
PI = 3.1416

sum = lambda a,b : a+b;
sub = lambda a,b : a-b;

def hello() :
    print(">>> From lib file <<<");

class Person : 
    def __init__(self,_name,_age) :
        self.name = _name;
        self.age = _age;
    def show_details(self) : 
        print(">>> Person Detaild <<<");
        print("> name : ",self.name);
        print("> age : ",self.age);
        print(">>> Finish Details <<<");