from functools import reduce

from Person import Person


class Student(Person):
    # Instance Variables ===========================================================================
    number = 0
    __subject = ''
    __marks = {}

    # Constructor ==================================================================================
    def __init__(self, number, subject, marks, name, address):
        super().__init__(name, address)
        self.number = number
        self.__subject = subject
        self.__marks = marks

    # Setters ======================================================================================
    def set_subject(self, subject):
        self.__subject = subject

    def set_marks(self, marks):
        self.__marks = marks

    # Getters ======================================================================================
    def get_subject(self):
        return self.__subject

    def get_marks(self):
        return self.__marks

    def get_avg(self):
        for key, val in self.__marks:
            return sum(val) / len(self.__marks)

    def get_a_marks(self):
        result = reduce(lambda key, value: value > 90, self.__marks)
        if result > 90:
            return 'A'
        return 'There\'s No `A` marks for this student.'

    # Other Methods ================================================================================
    def show_student_info(self):
        print(f'Student Information :\nname: {self.get_name()} \nnumber: {self.number}\nsubject: {self.get_subject()}\nmarks: {self.get_marks()}\naverage: {self.get_avg()}')

    # Destructor ===================================================================================
    # def __del__(self):
    # print('I have been deleted.')
