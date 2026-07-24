import tkinter as tk
from Subject import Subject


window = tk.Tk()
window.title("ตารางเรียน")


custom_font = ("Arial", 12)


Monday_subjects = [
    Subject("9043011", 1, "ระบบสารสนเทศภูมิศาสตร์ 2", "436", "#DDF265"),
    "",
    Subject("9043073", 1, "การประยุกต์ภูมิสารสนเทศด้านการสาธารณสุข", "436", "#DDF265"),
]


Tuesday_subjects = [
    Subject("9042032", 1, "ระบบดาวเทียมนำทางบนโลกขั้นสูง", "437", "#E860BB"),
    "",
]

Wendnesday_subjects = [
    Subject("9043051", 1, "การเขียนโปรแกรมภาษาสมัยใหม่สำหรับภูมิสารสนเทศ", "433", "#68EE6C"),
    "",
]

Thursday_subjects = [
    "","","","",
    Subject("9043091", 1, "สัมมนาทางภูมิสารสนเทศ 1", "426", "#FA7F1B"),
]

Friday_subjects = [
    Subject("9012071", 1, "การเขียนโปรแกรมคอมพิวเตอร์ 2", "434", "#5C93CD"),
    "",
    Subject("9043021", 1, "การรับรู้จากระยะไกล 2", "433", "#5C93CD"),
]

Monday_frame = tk.LabelFrame(window, text="วันจันทร์", font=custom_font)
Monday_frame.grid(row=1, column=0, padx=10, pady=5, sticky="w")

Tuesday_frame = tk.LabelFrame(window, text="วันอังคาร", font=custom_font)
Tuesday_frame.grid(row=2, column=0, padx=10, pady=5, sticky="w")

Wendnesday_frame = tk.LabelFrame(window, text="วันพุธ", font=custom_font)
Wendnesday_frame.grid(row=3, column=0, padx=10, pady=5, sticky="w")

Thursday_frame = tk.LabelFrame(window, text="วันพฤหัสบดี", font=custom_font)
Thursday_frame.grid(row=4, column=0, padx=10, pady=5, sticky="w")

Friday_frame = tk.LabelFrame(window, text="วันศุกร์", font=custom_font)
Friday_frame.grid(row=5, column=0, padx=10, pady=5, sticky="w")


def create_subject_label(frame, subjects):
    column = 0
    for subject in subjects:
        if isinstance(subject, Subject):
            if subject.room:
                text = f"{subject.code}, {subject.section} \n{subject.name} \n{subject.room}"
            else:
                text = f"{subject.code}\n{subject.name}"
            label = tk.Label(frame, text=text, padx=20, pady=10, borderwidth=1, relief="solid", bg=subject.color, font=custom_font)
            label.grid(row=0, column=column)
            column += 2
        else:
            label = tk.Label(frame, text="", padx=0, pady=0, borderwidth=0, relief="solid")
            label.grid(row=0, column=column, padx=40, pady=5)
            column += 2


create_subject_label(Monday_frame, Monday_subjects)
create_subject_label(Tuesday_frame, Tuesday_subjects)
create_subject_label(Wendnesday_frame, Wendnesday_subjects)
create_subject_label(Thursday_frame, Thursday_subjects)
create_subject_label(Friday_frame, Friday_subjects)


window.mainloop()
