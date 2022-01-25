# here create parent class
class Person :
    def __init__(self,_name,_age) :
        self.name = _name;
        self.age = _age;


# here create child function with overwrite init
class Student(Person) :
    def __init__(self,_id,_year,_p) :
        Person.__init__(self,_p.name,_p.age);
        self.student_id = _id;
        self.addmassion_year = _year;

    def show_details(self) :
        print(">>> Student's Details <<<");
        print("> name : ",self.name);
        print("> age : ",self.age);
        print("> student_id : ",self.student_id);
        print("> addmassion_year : ",self.addmassion_year);
        print(">>> Finish Details <<<");

me = Person("Md Tazri",17);
student_me = Student('1234','2021',me);

student_me.show_details();