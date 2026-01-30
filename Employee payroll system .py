class Employee:
    def __init__(self,emp_id,name,sal):
        self.id = emp_id
        self.name = name                            #abstract 
    #self._sal = sal
    def cal_sal(self):
        pass

class fulltimeemp(Employee):
    def __init__(self,emp_id,name,sal):
        super().__init__(emp_id,name,sal)
        self._sal = sal                          #encapuslation cuz sal is protected
    def cal_sal(self):
        return self._sal              

class parttimeemp(Employee):                    #inheritance
    def __init__(self,emp_id,name,hours_worked,rate_per_hour):
        super().__init__(emp_id,name,0) # Passing 0 as base salary since it is calculated
        self._h_work = hours_worked
        self._rate_per_hour = rate_per_hour
    def cal_sal(self):
        return self._h_work * self._rate_per_hour   

class PayrollApp:
    def __init__(self):
        self.emp = None
    def create_emp(self, emp_type):
        if emp_type.lower() == "full time":
            self.emp = fulltimeemp(1,"Amit",50000)
        elif emp_type.lower() == "part time":
            self.emp = parttimeemp(2,"Preety",40,1000)
        return "Employee created"

    def get_sal(self):
        return self.emp.cal_sal()

app = PayrollApp()
print(app.create_emp("Full Time"))
print("Salary of employee: ",app.get_sal())
app2 = PayrollApp()
print(app.create_emp("Part Time"))
print("Salary of employee: ",app.get_sal())

