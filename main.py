class Student:
    def __init__(self, s_id, name):
        self.s_id = s_id
        self.name = name
        self.assignments = {'hw1': 0, 'hw2': 0, 'p1': 0, 'p2': 0}


hw1_f = open('./hw1.txt', 'r')
hw2_f = open('./hw2.txt', 'r')
p1_f = open('./p1.txt', 'r')
p2_f = open('./p2.txt', 'r')


students = {}

for line in hw1_f.readlines():
    fname, lname, s_id, score = line.split()
    if s_id not in students.keys():
        student = Student(s_id, fname + ' ' + lname)
        student.assignments['hw1'] = score
        students[s_id] = student
    else:
        student = students[s_id]
        student.assignments['hw1'] = score
        students[s_id] = student


for line in hw2_f.readlines():
    fname, lname, s_id, score = line.split()
    if s_id not in students.keys():
        student = Student(s_id, fname + ' ' + lname)
        student.assignments['hw2'] = score
        students[s_id] = student
    else:
        student = students[s_id]
        student.assignments['hw2'] = score
        students[s_id] = student

for line in p1_f.readlines():
    fname, lname, s_id, score = line.split()
    if s_id not in students.keys():
        student = Student(s_id, fname + ' ' + lname)
        student.assignments['p1'] = score
        students[s_id] = student
    else:
        student = students[s_id]
        student.assignments['p1'] = score
        students[s_id] = student

for line in p2_f.readlines():
    fname, lname, s_id, score = line.split()
    if s_id not in students.keys():
        student = Student(s_id, fname + ' ' + lname)
        student.assignments['p2'] = score
        students[s_id] = student
    else:
        student = students[s_id]
        student.assignments['p2'] = score
        students[s_id] = student


ta_f = open('./TA.csv', 'w')
for s_id in students.keys():
    student = students[s_id]
    ta_f.write(str(student.name) + ',' + str(student.s_id) + ',' + str(student.assignments['hw1']) +
               ',' + str(student.assignments['hw2']) + ',' + str(student.assignments['p1']) + ',' + str(student.assignments['p2']) + '\n')
