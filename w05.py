from Building import Building
from Room import Room
from Student import Student
from Coures import Course       
from Enrollment import Enrollment  
from Subject import Subject
from Program import Program  


gi_program = Program("GI", "ภูมิสารสนเทศ", "Geoinformatics")


Student01 = Student("6714931001", "ชุติกาญจน์", "สุดสงวน", gi_program)
b4 = Building("4", "คณะวิทยาการคอมพิวเตอร์และเทคโนโลยีสารสนเทศ")
r426 = Room("426", "ห้องบรรยาย 6", b4)
r433 = Room("433", "ปฏิบัติการคอมพิวเตอร์ 3", b4)
r434 = Room("434", "ปฏิบัติการคอมพิวเตอร์ 4", b4) 
r436 = Room("436", "ปฏิบัติการคอมพิวเตอร์ 6", b4)
r437 = Room("437", "ปฏิบัติการคอมพิวเตอร์ 7", b4) 

s9012071 = Subject("9012071" ,"การเขียนโปรแกรมคอมพิวเตอร์ 2","Computer programmimg 2" ,3,2,2)
s9043011 = Subject("9043011" ,"ระบบสารสนเทศภูมิศาสตร์ 2" ,"Geographic Information Systems 2" ,3,2,2)
s9043073 = Subject("9043073" ,"การประยุกต์ภูมิสารสนเทศด้านการสาธารณสุข" ,"Application of Geoinformatics in Public Health" ,3,2,2)
s9042032 = Subject("9042032" ,"ระบบดาวเทียมนำทางบนโลกขั้นสูง" ,"Advanced Global Navigation Satellite System" ,3,2,2)
s9043051 = Subject("9043051" ,"การเขียนโปรแกรมภาษาสมัยใหม่สำหรับภูมิสารสนเทศ" ,"Modern Programming Language for Geoinformatics" ,3,2,2)
s9043091 = Subject("9043091" ,"สัมมนาทางภูมิสารสนเทศ 1" ,"Seminar in Geoinformatics 1" ,3,2,2)
s9043021 = Subject("9043021" ,"การรับรู้จากระยะไกล 2" ,"Remote Sensing 2" ,3,2,2)

Course01 = Course(s9012071, 1, r434)
Course02 = Course(s9043011, 1, r436)
Course03 = Course(s9043073, 1, r436)
Course04 = Course(s9042032, 1, r437)
Course05 = Course(s9043051, 1, r433)
Course06 = Course(s9043091, 1, r426)
Course07 = Course(s9043021, 1, r433)



em01 = Enrollment(2569, 1, Student01)
em01.add_course(Course01)
em01.add_course(Course02)
em01.add_course(Course03)
em01.add_course(Course04)
em01.add_course(Course05)
em01.add_course(Course06)
em01.add_course(Course07)


print(em01)
em01.listCourse ()