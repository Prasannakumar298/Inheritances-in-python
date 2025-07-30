'''code to perform addition operation using superclass and
user input and sub class as operation
print the summated value at sub class'''

class operate:
    def userdata(self):
        self.num1=int(input("Enter the value of num1:"))
        self.num2=int(input("Enter the value of num2:"))
class summate(operate):
    def add(self):
        result=self.num1+self.num2
        print(f"The result is {result}")
c=summate()
c.userdata()
c.add()