from Person import Person


class Employee(Person):
    # Instance Variables =========================================================================
    number = 0
    __salary = 0.0
    __job_title = ''
    __loans = []

    # Constructor =========================================================================
    def __init__(self, number, salary, job_title, loans, name, address):
        super().__init__(name, address)
        self.number = number
        self.__salary = salary
        self.__job_title = job_title
        self.__loans = loans

    # Setters ==================================================================
    def set_salary(self, salary):
        self.__salary = salary

    def set_job_title(self, job_title):
        self.__job_title = job_title

    def set_loans(self, loans):
        self.__loans = loans

    # Getters ==================================================================
    def get_salary(self):
        return self._name

    def get_job_title(self):
        return self.__job_title

    def get_loans(self):
        if len(self.__loans) == 0:
            return 'There\'s no loans for this employee.'
        return self.__loans

    def get_total_loans(self):
        return sum(self.__loans)

    def get_max_loans(self):
        return max(self.__loans)

    def get_min_loans(self):
        return min(self.__loans)

    # Other Methods
    def show_employee_info(self):
        print(
            f'Employee Info :\nname: {self.get_name()} \nnumber: {self.number}\nsalary: {self.get_salary()}\njob_title: {self.get_job_title()}\n total loans: {self.get_total_loans()}')
        print('\n=====================================================================================================')
    # Destructor =============================================================
    # def __del__(self):
    # print('I have been deleted.')
