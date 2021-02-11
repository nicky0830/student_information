#1. 초기화
f = open("student_information.txt","r")
student_list = []
#INT, CHAR(20), CHAR(50), CHAR(1), INT, CHAR(3), FLOAT
for l in f:
    s = l.strip().split(",")
    student_id, name, department, sex, age, nationality, grade = s
    student_list.append(s)
# print(student_list)

#2. 추가
def TF(student_id, name, department, sex, age, nationality, grade):
    m = (student_id, name, department, sex, age, nationality, grade)
    for i in range(len(student_list)):
        if student_list[i][0] == student_id:
            return('False')
        elif len(name) > 20 or len(department) > 50 or len(sex) > 1 or len(nationality) > 3:
            return('False')
        else:
            student_list.append(m)
            print(student_list)
            return ('True')




a = TF('20108008', ' Deborah', ' Bio and Brain Engineering', ' F', 22, ' IND', 3.88)
print(a)







