from Subject import Subject
from Lecturer import Lecturer
from Room import Room
from Building import Building
from Student import Student
s9012071 = Subject("9012071" ,"การเขียนโปรแกรมคอมพิวเตอร์ 2","Computer programmimg 2" ,3,2,2)
s9043011 = Subject("9043011" ,"ระบบสารสนเทศภูมิศาสตร์ 2" ,"Geographic Information Systems 2" ,3,2,2)
s9043073 = Subject("9043073" ,"การประยุกต์ภูมิสารสนเทศด้านการสาธารณสุข" ,"Application of Geoinformatics in Public Health" ,3,2,2)
s9042032 = Subject("9042032" ,"ระบบดาวเทียมนำทางบนโลกขั้นสูง" ,"Advanced Global Navigation Satellite System" ,3,2,2)
s9043051 = Subject("9043051" ,"การเขียนโปรแกรมภาษาสมัยใหม่สำหรับภูมิสารสนเทศ" ,"Modern Programming Language for Geoinformatics" ,3,2,2)
s9043091 = Subject("9043091" ,"สัมมนาทางภูมิสารสนเทศ 1" ,"Seminar in Geoinformatics 1" ,3,2,2)
s9043021 =Subject("9043021" ,"การรับรู้จากระยะไกล 2" ,"Remote Sensing 2" ,3,2,2)

l1 = Lecturer("อาจารย์" ,"นิทัศน์" ,"นิลฉวี" ,"Gi")
l2 = Lecturer("ผู้ช่วยศาสตราจารย์" ,"วิระ" ,"ศรีมาลา" ,"Gi")
l3 = Lecturer("ผู้ช่วยศาสตราจารย์ ดร." ,"คัมภีร์" ,"ธีระเวช" ,"Gi")
l4 = Lecturer("ผู้ช่วยศาสตราจารย์" ,"ทบทอง" ,"ชั้นเจริญ" ,"Gi")

r426 = Room("ห้อง426" ,"อาคาร4")
r433 = Room("ห้อง433" ,"อาคาร4")
r434 = Room("ห้อง434" ,"อาคาร4")
r436 = Room("ห้อง436" ,"อาคาร4")
r437 = Room("ห้อง437" ,"อาคาร4")

b4 = Building("4" ,"อาคารคณะวิทยาการคอมพิวเตอร์และเทคโนโลยีสารสนเทศ")

s6714931001 = Student("6714931001" ,"นางสาวชุติกาญจน์" ,"สุดสงวน" ,"Gi")

print(s9012071)
print(s9043011)
print(s9043073)
print(s9042032)
print(s9043051)
print(s9043091)
print(s9043021)
print(l1)
print(l2)
print(l3)
print(l4)
print(r426)
print(r433)
print(r434)
print(r436)
print(r437)
print(b4)
print(s6714931001)

