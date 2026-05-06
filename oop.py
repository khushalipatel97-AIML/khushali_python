
# constructor
class Student:
    def __init__(self, fname, fAge):
        self.name = fname;
        self.age = fAge;


s1 = Student("Khushali", 18)
print(s1.name, s1.age)


# inheritance
class Person:
    def speak(self):
        print("Hello");
class Student(Person):
    pass

s1 = Student();
s1.speak();
