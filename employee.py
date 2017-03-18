from person import Person

class Employee(Person):
    def __init__(self, first, last, salary, ssn):
        Person.__init__(self, first, last)
        self._salary = salary
        self._ssn = ssn

    #Let's override the default string print behavior
    def __str__(self):
        return '{}, {}, {}'.format(self.first_name, self.last_name, self.salary)
    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        self._salary = value

    @property
    def ssn(self):
        return self._ssn

    @ssn.setter
    def ssn(self, value):
        self._ssn = value