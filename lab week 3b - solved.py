#NAMES : ALEJANDRA SILVA

#fix the problems with each of these classes (1-3)
#(run them to see the traceback)

#1
class MyClass():
    def __init__(self):
        self.a = 10
        self.b = 20
        self.x = self.a + self.b
my_instance = MyClass()
my_instance.x

#2
class MyClass():
    def __init__(self):
        self.a = 10
        self.b = 20
        self.x = self.a + self.b
my_instance = MyClass()
my_instance.x

#3
class MyClass():
    def __init__(self, a, b):
        self.x = a + b
my_instance = MyClass(10, 20)
my_instance.x

#4 Create a class to hold all of the courses a student at Harris is enrolled in.
#  - The instance should take two arguments when created; student name, 
#    and student year
#  - At startup, each instance should have an empty list as an attribute 
#    named "enrolled_courses"
#  - Create a method named "enroll" that takes some arguments that describe
#    a course, e.g. name, course number, days, times
#  - When called, make the "enroll" method add a course to the "enrolled_courses"
#    list
#  - Finally, think about what other methods you could add. One to drop a course?
#    One to display the enrolled courses?  Or could you modify "enroll" to make
#    sure times don't overlap, or there aren't too many courses in the list?
#    Work on these if you would like an extra challenge.

class MyCourses():
    def __init__(self, st_name, st_year):
        self.st_name = st_name
        self.st_year = st_year
        self.enrolled_courses = []
        
    def enroll(self, name, number, days, times):
        self.enrolled_courses.append(
            [name, number, days, times])
    
    def drop(self,name):
        self.enrolled_courses = [x for x in self.enrolled_courses if x[0] != name]
        
    def display_courses(self):
        for x in self.enrolled_courses:
            print(x)

inst1 = MyCourses("Alejandra", 2020)
inst1.enroll("Mathematics", "MATH101", "Monday, Wednesday", "9:00-10:30")
inst1.enroll("Data & Programming", "DAP201", "Tuesday, Thursday", "11:00-12:30")
inst1.enroll("Public Budgeting", "PBUD101", "Monday", "14:00-15:30")
inst1.display_courses()


        
        
