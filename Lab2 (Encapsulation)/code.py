class Student:
    def __init__(self, student_id, student_name):
        self.__id = student_id
        self.__name = student_name
    
    def get_id(self):
        return self.__id
    
    def get_name(self):
        return self.__name
    
class Subject:
    def __init__(self, subject_id, subject_name, credit):
        self.__id = subject_id
        self.__name = subject_name
        self.__credit = credit
        self.__teacher = None
    
    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def assign_teacher(self, teacher):
        self.__teacher = teacher
    
    def get_teacher(self):
        return self.__teacher
    
    def get_credit(self):
        return self.__credit

class Teacher:
    def __init__(self, teacher_id, teacher_name):
        self.__id = teacher_id
        self.__name = teacher_name

    def get_id(self):
        return self.__id
    
    def get_name(self):
        return self.__name

class EnrollSubject:
    def __init__(self, student, subject):
        self.__student = student
        self.__subject = subject
        self.__grade = ""

    def get_student(self):
        return self.__student
    
    def get_subject(self):
        return self.__subject

    def set_remove_enroll_list(self, student):
        if student in self.__enrollment_list:
            self.__enrollment_list.remove(student)
            return "Done"
        else:
            return "Not Found"
        
    def get_grade(self):
        return self.__grade
    
    def assign_grade(self, grade):
        self.__grade = grade

student_list = []
teacher_list = []
subject_list = []
enrollment_list = []

# TODO 1 : function สำหรับค้นหา instance ของวิชาใน subject_list
def search_subject_by_id(subject_id):
    if len(subject_id) != 5:
        return "Error"

    for subject in subject_list:
        if subject.get_id() == subject_id:
            return subject
    
    return None

# TODO 2 : function สำหรับค้นหา instance ของนักศึกษาใน student_list
def search_student_by_id(student_id):
    if not student_id.isnumeric() and len(student_id) != 8:
        return "Error"

    for student in student_list:
        if student.get_id() == student_id:
            return student
        
    return None

# TODO 3 : function สำหรับสร้างการลงทะเบียน โดยรับ instance ของ student และ subject
def enroll_to_subject(student, subject):
    if type(student) != Student or type(subject) != Subject:
        return "Error"
    
    for enroll in enrollment_list:
        if enroll.get_student() == student and enroll.get_subject() == subject:
            return "Already Enrolled"
        
    enrollment_list.append(EnrollSubject(student, subject))
    return "Done"

# TODO 4 : function สำหรับลบการลงทะเบียน โดยรับ instance ของ student และ subject
def drop_from_subject(student, subject):
    if type(student) != Student or type(subject) != Subject:
        return "Error"
    
    for enroll in enrollment_list:
        if enroll.get_student() == student and enroll.get_subject() == subject:
            enrollment_list.remove(enroll)
            return "Done"
        
    return "Not Found"

# TODO 5 : function สำหรับค้นหาการลงทะเบียน โดยรับ instance ของ student และ subject
def search_enrollment_subject_student(subject, student):
    if type(student) != Student or type(subject) != Subject:
        return "Error"
    
    for enroll in enrollment_list:
        if enroll.get_subject() == subject and enroll.get_student() == student:
            return enroll

    return "Not Found"

# TODO 6 : function สำหรับค้นหาการลงทะเบียนในรายวิชา โดยรับ instance ของ subject
def search_student_enroll_in_subject(subject):
    if type(subject) != Subject:
        return "Error"
    
    sub_enroll_lst = [i for i in enrollment_list if i.get_subject() == subject]
    return sub_enroll_lst

# TODO 7 : function สำหรับค้นหาการลงทะเบียนของนักศึกษาว่ามีวิชาอะไรบ้าง โดยรับ instance ของ student
def search_subject_that_student_enrolled(student):
    if type(student) != Student:
        return "Error"

    lst_of_student_enroll = []

    for enroll in enrollment_list:
        if enroll.get_student() == student:
            lst_of_student_enroll.append(enroll)
    
    if len(lst_of_student_enroll) == 0:
        return "Not Found"
    
    return lst_of_student_enroll

# TODO 8 : function สำหรับใส่เกรดลงในการลงทะเบียน โดยรับ instance ของ student และ subject
def assign_grade(student, subject, grade):
    if type(student) != Student and type(subject) != Subject:
        return "Error"
    
    for enroll in enrollment_list:
        if enroll.get_subject() == subject and enroll.get_student() == student:
            if enroll.get_grade() != '':
                return "Error"
            
            enroll.assign_grade(grade)
            return "Done"
        
    return "Not Found"

# TODO 9 : function สำหรับคืน instance ของอาจารย์ที่สอนในวิชา
def get_teacher_teach(subject):
    if type(subject) != Subject:
        return "Error"
    
    return subject.get_teacher()

# TODO 10 : function สำหรับค้นหาจำนวนของนักศึกษาที่ลงทะเบียนในรายวิชา โดยรับ instance ของ subject
def get_no_of_student_enrolled(subject):
    if type(subject) != Subject:
        return "Error"
    
    count_of_enroll = 0

    for enroll in enrollment_list:
        if enroll.get_subject() == subject:
            count_of_enroll += 1
    
    if count_of_enroll == 0:
        return "Not Found"
    
    return count_of_enroll

# TODO 11 : function สำหรับค้นหาข้อมูลการลงทะเบียนและผลการเรียนโดยรับ instance ของ student
# TODO : และ คืนค่าเป็น dictionary { ‘subject_id’ : [‘subject_name’, ‘grade’ }
def get_student_record(student):
    if type(student) != Student:
        return "Error"

    record = {}

    for enroll in enrollment_list:
        if enroll.get_student() == student:
            record[enroll.get_subject().get_id()] = [enroll.get_subject().get_name(), enroll.get_grade()]

    return record

# แปลงจาก เกรด เป็นตัวเลข
def grade_to_count(grade):
    grade_mapping = {'A': 4, 'B': 3, 'C': 2, 'D': 1}
    return grade_mapping.get(grade, 0)

# TODO 12 : function สำหรับคำนวณเกรดเฉลี่ยของนักศึกษา โดยรับ instance ของ student
def get_student_GPS(student):
    gps = 0
    all_credit = 0

    subject = get_student_record(student)

    for id in subject:
        credit = search_subject_by_id(id).get_credit()
        grade = grade_to_count(subject[id][1])
        gps += grade * credit
        all_credit += credit

    return gps / all_credit

# ค้นหานักศึกษาลงทะเบียน โดยรับเป็น รหัสวิชา และคืนค่าเป็น dictionary {รหัส นศ. : ชื่อ นศ.}
def list_student_enrolled_in_subject(subject_id):
    subject = search_subject_by_id(subject_id)

    if subject is None:
        return "Subject not found"
    
    filter_student_list = search_student_enroll_in_subject(subject)
    student_dict = {}

    for enrollment in filter_student_list:
        student_dict[enrollment.get_student().get_id()] = enrollment.get_student().get_name()
    return student_dict

# ค้นหาวิชาที่นักศึกษาลงทะเบียน โดยรับเป็น รหัสนักศึกษา และคืนค่าเป็น dictionary {รหัสวิชา : ชื่อวิชา }

def create_instance():
    student_list.append(Student('66010001', "Keanu Welsh"))
    student_list.append(Student('66010002', "Khadijah Burton"))
    student_list.append(Student('66010003', "Jean Caldwell"))
    student_list.append(Student('66010004', "Jayden Mccall"))
    student_list.append(Student('66010005', "Owain Johnston"))
    student_list.append(Student('66010006', "Isra Cabrera"))
    student_list.append(Student('66010007', "Frances Haynes"))
    student_list.append(Student('66010008', "Steven Moore"))
    student_list.append(Student('66010009', "Zoe Juarez"))
    student_list.append(Student('66010010', "Sebastien Golden"))

    subject_list.append(Subject('CS101', "Computer Programming 1", 1))
    subject_list.append(Subject('CS102', "Computer Programming 2", 3))
    subject_list.append(Subject('CS103', "Data Structure", 3))

    teacher_list.append(Teacher('T001', "Mr. Welsh"))
    teacher_list.append(Teacher('T002', "Mr. Burton"))
    teacher_list.append(Teacher('T003', "Mr. Smith"))

    subject_list[0].assign_teacher(teacher_list[0])
    subject_list[1].assign_teacher(teacher_list[1])
    subject_list[2].assign_teacher(teacher_list[2])

def initialize():
    create_instance()

initialize()

# ### Test Case #1 : test enroll_to_subject complete ###
for i in range(7):
    if i == 5:
        continue

    enroll_to_subject(student_list[i], subject_list[0])
    enroll_to_subject(student_list[i], subject_list[1])
    enroll_to_subject(student_list[i], subject_list[2])

student_enroll = list_student_enrolled_in_subject('CS101')
print("Test Case #1 : test enroll_to_subject complete")
print("Answer : {'66010001': 'Keanu Welsh', '66010002': 'Khadijah Burton', '66010003': 'Jean Caldwell', '66010004': 'Jayden Mccall', '66010005': 'Owain Johnston', '66010007': 'Frances Haynes'}")
print("Answer :", student_enroll)
print("")

# ### Test case #2 : test enroll_to_subject in case of invalid argument
print("Test case #2 : test enroll_to_subject in case of invalid argument")
print("Answer : Error")
print("Answer :", enroll_to_subject('66010001','CS101'))
print("")

# ### Test case #3 : test enroll_to_subject in case of duplicate enrolled
print(enroll_to_subject(student_list[0], subject_list[0]))
print("Test case #3 : test enroll_to_subject in case of duplicate enrolled")
print("Answer : Already Enrolled")
print("Answer :", enroll_to_subject(student_list[0], subject_list[0]))
print("")

# ### Test case #4 : test drop_from_subject in case of invalid argument 
print("Test case #4 : test drop_from_subject in case of invalid argument")
print("Answer : Error")
print("Answer :", drop_from_subject('66010001', 'CS101'))
print("")

# ### Test case #5 : test drop_from_subject in case of not found 
print("Test case #5 : test drop_from_subject in case of not found")
print("Answer : Not Found")
print("Answer :", drop_from_subject(student_list[8], subject_list[0]))
print("")

# ### Test case #6 : test drop_from_subject in case of drop successful
print("Test case #6 : test drop_from_subject in case of drop successful")
print("Answer : {'66010002': 'Khadijah Burton', '66010003': 'Jean Caldwell', '66010004': 'Jayden Mccall', '66010005': 'Owain Johnston', '66010007': 'Frances Haynes'}")
print("==== Droped ====")
drop_from_subject(student_list[0], subject_list[0])
print("Answer :", list_student_enrolled_in_subject(subject_list[0].get_id()))
print("")

# ### Test case #7 : test search_student_enrolled_in_subject
print("Test case #7 : test search_student_enrolled_in_subject")
print("Answer : ['66010002','66010003','66010004','66010005','66010007']")
lst = search_student_enroll_in_subject(subject_list[0])
print("Answer :", [i.get_student().get_id() for i in lst])
print("")

# ### Test case #8 : get_no_of_student_enrolled
print("Test case #8 get_no_of_student_enrolled")
print("Answer : 5")
print("Answer :", get_no_of_student_enrolled(subject_list[0]))
print("")

# ### Test case #9 : search_subject_that_student_enrolled
print("Test case #9 search_subject_that_student_enrolled")
print("Answer : ['CS102','CS103']")
lst = search_subject_that_student_enrolled(student_list[0])
if lst != "Not Found":
    print("Answer :", [i.get_subject().get_id() for i in lst])
else:
    print("Not Found")
print("")

# ### Test case #10 : get_teacher_teach
print("Test case #10 get_teacher_teach")
print("Answer : Mr. Welsh")
print("Answer :", get_teacher_teach(subject_list[0]).get_name())
print("")

# ### Test case #11 : search_enrollment_subject_student
print("Test case #11 search_enrollment_subject_student")
print("Answer : CS101 66010002")
enroll = search_enrollment_subject_student(subject_list[0],student_list[1])
print("Answer :", enroll.get_subject().get_id(), enroll.get_student().get_id())
print("")

# ### Test case #12 : assign_grade
print("Test case #12 assign_grade")
print("Answer : Done")
assign_grade(student_list[1],subject_list[0],'A')
assign_grade(student_list[1],subject_list[1],'B')
print("Answer :", assign_grade(student_list[1],subject_list[2],'C'))
print("")

# ### Test case #13 : get_student_record
print("Test case #13 get_student_record")
print("Answer : {'CS101': ['Computer Programming 1', 'A'], 'CS102': ['Computer Programming 2', 'B'], 'CS103': ['Data Structure', 'C']}")
print("Answer :", get_student_record(student_list[1]))
print("")

# ### Test case #14 : get_student_GPS
print("Test case #14 get_student_GPS")
print("Answer : 3.0")
print("Answer :", get_student_GPS(student_list[1]))