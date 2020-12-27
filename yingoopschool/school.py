# -*- coding:-utf-8 -*-

class Student: # จดบันทึกรายชื่อนักเรียน
    def __init__(self, name, lastname):
        self.name = name
        self.lastname = lastname
        self.exp = 0  # คะแนนประสบการณ์
        self.lesson = 0 # จำนวนคลาสที่เคยเรียน
        self.vehicle = 'รถเมล์'

    @property
    def fullname(self):
        return '{} {}'.format(self.name, self.lastname)

    def Coding(self):
        ''' นี่คือคลาสเรียนวิชาเขียนโปรแกรม'''
        self.AddEXP()
        print('{} กำลังเรียนเขียนโปรแกรม....'.format(self.fullname))
    def ShowEXP(self):
        print('{} ได้คะแนน {} exp (เรียนไป {} ครั้ง)'.format(self.name, self.exp, self.lesson))

    def AddEXP(self):
        self.exp += 10
        self.lesson += 1

    def __str__(self):
        return self.fullname

    def __repr__(self):
        return self.fullname

    def __add__(Self, orther):
        return Self.exp + orther.exp


class Tesla:
    def __init__(self):
        self.model = 'Tesla Model S'

    def SelfDriving(self, st):
        print('ระบบขับอัตโนมัติกำลังทำงาน...พาคุณ{} กลับบ้าน'.format(st.name))

    def __str__(self):
        return self.model


class SpacialStudent(Student):
    def __init__(self, name, lastname, father):
        super().__init__(name, lastname)

        self.father = father
        self.vehicle = Tesla()
        print('รู้ไม๊ฉันลูกใคร!..พ่อฉันชื่อ {}'.format(self.father))

    def AddEXP(self):
        self.exp += 30
        self.lesson += 2

    

class Teacher:
    def __init__(self, fullname):
        self.fullname = fullname 
        self.Students = []

    def CheckStudent(self):
        print('--นักเรียนของคุณครู> {} -->'.format(self.fullname))
        for i, st in enumerate(self.Students):
            print('{} -->{} [{} exp][ เรียนไป {} ครั้ง]'.format(i+1, st.fullname, st.exp, st.lesson))

    def AddStudent(self, st):
        self.Students.append(st)


if __name__ == "__main__":

    allstudent = []
    teacher1 = Teacher('Ada Lovelace')
    teacher2 = Teacher('Bill Gates')
    print(teacher1.Students)

    # day 1
    print('-----Day 1-----')
    st1 = Student('Albert', 'Einstein')
    allstudent.append(st1)
    teacher2.AddStudent(st1)
    print(st1.fullname)

    # day 2
    print('-----Day 2-----')
    st2 = Student('Steve', 'Jobs')
    allstudent.append(st2)
    teacher2.AddStudent(st2)
    print(st2.fullname)

    # day 3
    print('-----Day 3-----')
    for i in range(3):
        st1.Coding()
        
    st2.Coding()
    st1.ShowEXP()
    st2.ShowEXP()

    # day 4
    print('-----Day 4-----')
    stp1 = SpacialStudent('Thomas', 'Edison', 'Hitler')
    allstudent.append(stp1)
    teacher1.AddStudent(stp1)
    print(stp1.fullname)
    print('คุณครูครับขอคะแนนฟรี 20 คะแนนได้ไหม')
    stp1.exp = 20 # การแก้ไขค่าใน class ได้
    stp1.Coding()
    stp1.ShowEXP()

    # day 5
    print('-----Day 5-----')
    print('นักเรียนกลับบ้านยังไงกันจ๊ะา!')
    print(allstudent)
    for st in allstudent:
        print('ผม : {} กลับบ้านด้วย {} ครับ'.format(st.name, st.vehicle))
        if isinstance(st, SpacialStudent):
            st.vehicle.SelfDriving(st)

    # day 6
    print('-----Day 6-----')

    teacher1.CheckStudent()
    teacher2.CheckStudent()

    print('รวมพลังของนักเรียน 2 คน ค่า exp = ',st1 + st2)