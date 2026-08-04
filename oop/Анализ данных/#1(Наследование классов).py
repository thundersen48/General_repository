class ItSpecialist:
    def __init__(self,name,speciality,salary):
        self.name = name
        self.speciality = speciality
        self.salary = salary

    def tell_about_yourself(self):
        return f'Привет! мое имя {self.name}. Я {self.speciality}.Моя зарплата {self.salary}'

class DataScientist(ItSpecialist):
    def ml(self,data):
        return 'Profit for company (and myself)'

gleb = DataScientist('Gleb', 'DataScientist',30000)
print(gleb.tell_about_yourself())

