# create classs
class Person : 
    def __init__(this_object,_name,_age,_height) :
        # here this_object is instance of class
        this_object.name = _name;
        this_object.age = _age;
        this_object.height = _height;
    
    # show details function
    def show_details(object) :
        # here object is instance of class
        print(">>> Person Details <<<");
        print("> name : ",object.name);
        print("> age : ",object.age);
        print("> height : ",object.height);
        print(">>> Finish Details <<<");

me = Person("MD Tazri",17,'5foot 1inch');

# print details of me
me.show_details();
