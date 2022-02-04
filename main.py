from statistics import variance


class Student:
    def __init__(self, s_id, name):
        self.s_id = s_id
        self.name = name
        self.assignments = {'hw1': 0, 'hw2': 0, 'p1': 0, 'p2': 0}


def add_scores(file, assignment, students):
    for line in file.readlines():
        variables = line.split()
        score = variables[-1]
        s_id = variables[-2]
        name = ''
        for i in range(len(variables) - 2):
            name = name + ' ' + variables[i] 
        if s_id not in students.keys():
            student = Student(s_id, name)
            student.assignments[assignment] = score
            students[s_id] = student
        else:
            student = students[s_id]
            student.assignments[assignment] = score
            students[s_id] = student
    
    return students 


hw1_f = open('./hw1.txt', 'r')
hw2_f = open('./hw2.txt', 'r')
p1_f = open('./p1.txt', 'r')
p2_f = open('./p2.txt', 'r')


students = {}

students = add_scores(hw1_f, 'hw1', students)
students = add_scores(hw2_f, 'hw2', students)
students = add_scores(p1_f, 'p1', students)
students = add_scores(p2_f, 'p2', students)

ta_f = open('./TA.csv', 'w')
for s_id in students.keys():
    student = students[s_id]
    ta_f.write(str(student.name) + ',' + str(student.s_id) + ',' + str(student.assignments['hw1']) +
               ',' + str(student.assignments['hw2']) + ',' + str(student.assignments['p1']) + ',' + str(student.assignments['p2']) + '\n')
