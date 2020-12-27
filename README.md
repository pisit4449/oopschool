# (OOP School) ไลบรารี่สำหรับใช้เรี ยนPythonOOP

โปรแกรมใช้สำหรับการเขียนโปรแกรมแบบ OOP สามารถดูตัวอย่างคลิปวีดีโอ


ปล. เวอร์ชั่นนี้ยังไม่สมบูรณ์ (เขียนแบบรีบๆ 55) ลุงเขียนขึ้นมาเพื่อประยุกต์นำ Python + Socket Library สร้างเป็นโปรแกรมแชทตัวอย่าง สำหรับนักพัฒนาสามารถนำ Source Code ไปพัฒนาต่อได้เต็มที่

### วิธีติดตั้ง

เปิด CMD / Terminal

```python
pip install yingoopschool
```

### วิธีใช้งาน

[STEP 1]
- เปิด IDLE ขึ้นมาแล้วพิมพ์...

```python
from yingoopschool.school import Student,Tesla,SpacialStudent,Teacher
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
```



พัฒนาโดย: ลุงวิศวกร สอนคำนวณ
FB: https://www.facebook.com/UncleEngineer
YouTube: https://www.youtube.com/UncleEngineer
