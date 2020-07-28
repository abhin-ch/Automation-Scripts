# !/usr/bin/python3
from tkinter import * 
from acorn_automation import Execute
from tkinter import messagebox

top = Tk()
top.geometry('350x380')

Heading = Label(top, text="ACORN AUTOMATION \n")
Heading.pack()

a = " INSTRUCTION \n\n1.  Input your UtorID and Password. \n 2.  You can also select the time you \n would like to run the script \n 3.  Enter the courses in your enrolment cart \n 4. Run! the Script\n\n"
Instruction= Label(top, text=a)
Instruction.pack()

username = Entry(top, width =20)
username.pack()
username.insert(0, "UtorID...")



password = Entry(top, width =20, show= "*")
password.pack()
password.insert(0, "Password...")



time = Entry(top, width =20)
time.pack()
time.insert(0, "8:30 AM")
tim = time.get()

linebreak = Label(top, text="\n")
linebreak.pack()

courses = Entry(top, width =40)
courses.pack()
courses.insert(0, "  MATC01H3, ANTA01H3, PSYB70H3")


def myClick():
    use = username.get()
    key = password.get()
    course = courses.get()
    start = "Script will be Running At "+ tim
    myLabel = Label(top, text=start)
    myLabel.pack()
    # Login and Re-Direction Manuvers 
    test = Execute()
    test.login_process(use, key)
    test.redirect()
    course_list = course.split(",")
    for cou in course_list:
        cou = cou.replace(" ", "")
        test.enrol(cou)
        test.enrol_confirmation(cou)
        test.redirect()
    test.exit()


linebreak = Label(top, text="\n")
linebreak.pack()

myButton = Button(top, text="Run!", command=myClick)
myButton.pack()

top.mainloop()