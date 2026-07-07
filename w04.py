from Program import Program
from Lecturer import Lecturer
from Room import Room
from Building import Building
from Student import Student

program1 = Program("GI", "ภูมิสารสนเทศ", "Geoinformatics")

b4 = Building("4","อาคารคณะวิทยาการคอมพิวเตอร์และเทคโนโลยีสารสนเทศ")
r9043071 = Room("434","การเขียนโปรแกรมคอมพิวเตอร์ 2",b4)
r9012011 = Room("436", "ระบบสารสนเทศภูมิศาสตร์ 2", b4)
r9043073 = Room("436", "การประยุกต์ภูมิสารสนเทศด้านการสาธารณสุข", b4)
r9042032 = Room("437", "ระบบดาวเทียมนำทางบนโลกขั้นสูง", b4)
r9043051 = Room("433", "การเขียนโปรแกรมภาษาสมัยใหม่สำหรับภูมิสารสนเทศ", b4)
r9043091 = Room("426", "สัมมนาทางภูมิสารสนเทศ 1", b4)
r9043021 = Room("433", "การรับรู้จากระยะไกล 2", b4)
b4.setBuildingName("อาคารวิทย์คอม")

l9012071 = Lecturer("อาจารย์", "นิทัศน์", "นิลฉวี", program1)
l9043011 = Lecturer("ผู้ช่วยศาสตราจารย์", "วิระ", "ศรีมาลา", program1)
l9043073 = Lecturer("ผู้ช่วยศาสตราจารย์", "วิระ", "ศรีมาลา", program1)
l9042032 = Lecturer("ผู้ช่วยศาสตราจารย์", "วิระ", "ศรีมาลา", program1)
l9043051 = Lecturer("ผู้ช่วยศาสตราจารย์ ดร.", "คัมภีร์", "ธีระเวช", program1)
l9043091 = Lecturer("ผู้ช่วยศาสตราจารย์ ดร.", "คัมภีร์", "ธีระเวช", program1)
l9043021 = Lecturer("ผู้ช่วยศาสตราจารย์", "ทบทอง", "ชั้นเจริญ", program1)

s6714931001 = Student("6714931001", "นางสาวชุติกาญจน์", "สุดสงวน", program1)

print(program1)
print("=== ข้อมูลห้องเรียน ===")
print(r9043071)
print(r9012011)
print(r9043073)
print(r9042032)
print(r9043051)
print(r9043091)
print(r9043021)
print("\n=== ข้อมูลอาจารย์ ===")
print(l9012071)
print(l9043011)
print(l9043073)
print(l9042032)
print(l9043051)
print(l9043091)
print(l9043021)
print("\n=== ข้อมูลนักศึกษา ===")
print(s6714931001)