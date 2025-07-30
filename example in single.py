'''code to claculate normal division by considering input in super class and evalution in sub class
 where zero error must br handled'''

class division:
    def userdata(self):
        self.num1=float(input("Enter the value of num1:"))
        self.num2=float(input("Enter the value of num2:"))
class evaltions(division):
    def evaltion(self):
        try:
            result=self.num1/self.num2
            print(f"result:{result:.4f}")
        except ZeroDivisionError:
            return "Error: Division by zero is not allowed."
c=evaltions()
c.userdata()
c.evaltion()


