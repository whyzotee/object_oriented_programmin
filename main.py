class Student:
    def __init__(self, student_id, student_name):
        self.__id = student_id
        self.__name = student_name
    
    def get_id(self):
        return self.__id
    
    def get_name(self):
        return self.__name
    
    def set_id(self, id):
        if id.isnumeric() and len(id) == 8:
            self.__id = id
        else:
            raise ValueError("Invaild ID")

class Subject:
    def __init__(self, subject_id, subject_name, credit):
        self.__id = subject_id
        self.__name = subject_name
        self.__credit = credit
    
    def get_id(self):
        return self.__id

class Teacher:
    def __init__(self, teacher_id, teacher_name):
        self.__id = teacher_id
        self.__name = teacher_name

class Controller:
    def __init__(self):
        self.__enrollment_list = []
    
    def get_enroll_list(self):
        return self.__enrollment_list

    def enroll_to_subject(self, student, subject):
        if not student.get_id().startswith("std"):
            return "Error"

        if subject not in self.__enrollment_list:
            self.__enrollment_list.append([subject, []])

        for sub in self.__enrollment_list:
            if sub[0] == subject:
                if student in sub[1]:
                    return "Already Enrolled"
                
                sub[1].append(student)

            return "Done"   

student_list = []
subject_list = []
controller = Controller()

def create_inst_student():
    student_list.append(Student("std_67015026", "Chatnarint Boonsaeng"))
    student_list.append(Student("std_67015027", "Test Boonsaeng"))

def create_inst_subject():
    subject_list.append(Subject("01076103", "Programming Fundamental", 3))
    subject_list.append(Subject("01076104", "Programming Project", 1))
    subject_list.append(Subject("021", "Digital System Fundamental", 3))
    subject_list.append(Subject("022", "Digital System Fundamental in Practice", 1))

def initialize():
    create_inst_student()
    create_inst_subject()

initialize()

print(controller.enroll_to_subject(student_list[0], subject_list[0]))

print(controller.get_enroll_list())

print(controller.enroll_to_subject(student_list[1], subject_list[0]))

print(controller.get_enroll_list())
