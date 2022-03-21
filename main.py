# creating python classes(properties x behavior)
# creating objects from our classes
#self is used to bind the attributes to the arguments received
#class Subjects:
    #def __init__(self,name, like, dislike):
   #     self.name =name
  #      self.like=like
 #       self.dislike=dislike

#sub1 = Subjects("Physics","Yes","No")
#print("I like"+"" + sub1.name + "" + "it gets me excited so I say" + sub1.like + "to it")

class Student:
    def __init__(self,name, age, grade):
        self.name =name
        self.age=age
        self.grade=grade

    def get_grade(self):
        return self.grade
class Course:
    def __init__(self,name, max_students):
        self.name= name
        self.max_students=max_students
        self.students =[]
    def add_students(self,student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False
    def get_average_grade(self):
        value = 0
        for student in self.students:
            value += student.get_grade()
        return value / len(self.students)


s1=Student("Cheryl",21,95)
s2=Student("Jilian",23,70)
s3 =Student("Travis",19,68)

course= Course("Statistics",3)
course.add_students(s1)
course.add_students(s2)
print(course.students[0].name)
print(course.get_average_grade())