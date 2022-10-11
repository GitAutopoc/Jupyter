from datetime import date
class BonusCalculator:
    def calculate_bonus(d1,d2):
        id=d1.get('id')
        dob=d1.get('dob')
        salary=d2.get('salary')
        if type(id)!=type(1) or type(salary) !=type(1):
            raise ValueError("Type should be integer")
        if type(dob)!=type(" "):
            raise ValueError("Type should be string")
        dob=dob.split("-")
        year=int(dob[0])
        month=int(dob[1])
        day=int(dob[2])
        d1 = date(year,month,day)# employee dob
        d2 = date(2014,9,1)#y,m,d  (given date)
        delta = d2-d1
        #print("Days ",delta.days)
        years=delta.days/365
        #print("Years ",years)
        age=int(years)
        if (age<25 or age>60) and salary<5000:
            salary+=100
        elif  age<25 or age>60:
            salary+=200
        elif salary<5000:
            salary+=100
        elif age in range(25,31):
            salary+=salary*20/100
        elif age in range(31,61):
            salary+=salary*30/100
        emp_result={}
        emp_result['id']=id
        emp_result['salary']=salary
        return emp_result
