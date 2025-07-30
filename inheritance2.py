class person():
    def info(self):
        print("I am a student")
class student(person):
    def study(self):
        print("The student is studying!!!!!!")
s=student()
s.info()
s.study()