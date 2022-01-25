# create parent class
class Person :
    def __init__(self,_name,_age) :
        self.name = _name;
        self.age = _age;

# create Child and inherit by Person
class Student(Person) :
    def __init__(self,_id,_year,_person) :
        super().__init__(_person.name,_person.age);
        self.student_id = _id;
        self.year = _year;

    def show_datails(self) :
        print(">>> Student Details <<<");
        print("> name : ",self.name);
        print("> age : ",self.age);
        print("> student_id : ",self.student_id);
        print("> year : ",self.year);

me = Person("Md Tazri","17");
student_me = Student('85762',2021,me);
student_me.show_datails();