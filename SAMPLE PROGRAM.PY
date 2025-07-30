class Input:
    def __init__(self):
        self.num1=int(input("Enter the value of num1: "))
        self.num2=int(input("Enter the value of num2: "))
class operation(Input):
    def __init___(self):
        super.__init__()
    def add(self):
            return self.num1+self.num2
    def mul(self):
            return self.num1*self.num2
class result(operation):
    def __init__(self):
        super().__init__()
    def display(self):
            print(f"Sum:{self.add()}")
            print(f"mul:{self.mul()}")

r=result()
r.display()