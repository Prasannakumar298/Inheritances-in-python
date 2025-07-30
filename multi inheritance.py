class intern:       #superclass
    def __init__(self,name):
        self.name=name
    def display_intern(self):
        print(f"Name:{self.name}")


class employee(intern):   #class
    def __init__(self,emp_id):
        super().__init__(name)
        self.emp_id=emp_id
    def display_employee(self):
        print(f"Employee_ID:{self.emp_id}")

class manager(employee):    #sub class
    def __init__(self,name,emp_id,dept):
        super().__init__(emp_id)
        self.dept=dept
    def display_manager(self):
        print(f"Department:{self.dept}")
name=input("Enter name:")
emp_id=input("Enter employee id: ")
dept=input("Enter department:  ")
m=manager(name,emp_id,dept)
m.display_intern()
m.display_employee()
m.display_manager()
