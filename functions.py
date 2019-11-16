from tkinter import Label, Button, mainloop, Canvas, PhotoImage, messagebox, Tk, Entry, StringVar, OptionMenu
import sqlite3
import random

#To generate captcha
def gencaptcha():
    n1 = str(random.randint(0, 9))
    n2 = str(random.randint(0, 9))
    n3 = str(random.randint(0, 4))
    n4 = str(random.randint(5, 9))
    t1 = chr(random.randint(65,90))
    t2 = chr(random.randint(91,117))
    t3 = chr(random.randint(65,90))
    t4 = chr(random.randint(91,117))
    cap = n4 + t1 + t2 + n1 + t4 + t3 + n3 + n2
    conn = sqlite3.connect('storage/index.db')
    cur = conn.cursor()
    cur.execute("DELETE FROM captcha")
    cur.execute("INSERT INTO captcha VALUES(?)",(cap,))
    conn.commit()
    conn.close()
    return cap

#add faculty window
def add_faculty():
    #to generate uid
    def gen_uid():
        conn = sqlite3.connect("storage/index.db")
        cur = conn.cursor()
        cur.execute('SELECT * FROM faculty_info ORDER BY ID DESC LIMIT 1')
        for uid in cur.fetchall():
            prevID = int(uid[0])
        conn.close()
        newID = prevID + 1
        newID = str(newID)
        return newID
    #to perform insertion
    def add():
        name = name_entry.get()
        dob = dob_entry.get()
        password = pass_entry.get()
        mail = mail_entry.get()
        department = department_select.get()
        cap = cap_entry.get()
        uid = gen_uid()
        qualification = qual_entry.get()

        conn = sqlite3.connect("storage/index.db")
        cur = conn.cursor()
        cur.execute('SELECT * FROM captcha')
        row = cur.fetchone()
        if name == '' or dob == '' or password == '' or qualification == '' or mail == '' or department == 'none' or cap == '':
            messagebox.showwarning('Error!','All fields are required!')
        elif cap != row[0]:
            print(row[0])
            print(cap)
            messagebox.showwarning('Captcha Error!', 'Incorrect captcha entered!')
        else:
            cur.execute('INSERT INTO faculty_info values(?,?,?,?,?,?,?)',( uid, name, password, dob, mail, qualification, department))
            conn.commit()
            conn.close()
            master.destroy()
            messagebox.showinfo('Registration Number', 'Your registration number is ' + uid)

    master = Tk()
    master.geometry('300x250+535+270')
    master.title('Add Faculty')

    add_pane = Canvas(master,
                      height = '250',
                      width = '300',
                      bg = '#f7ebeb')
    add_pane.pack()

    add_pane.create_rectangle(0,0, 100, 20,
                              fill = '#e04a31',
                              outline = '#e04a31')
    add_pane.create_text(50, 10,
                         text = 'Faculty',
                         fill = 'white',
                         font = 'calibri 10 bold')

    name_entry = Entry(master,
                      bd = '2')
    dob_entry = Entry(master,
                     bd = '2')
    pass_entry = Entry(master,
                      bd = '2')
    mail_entry = Entry(master,
                       bd = '2')
    qual_entry = Entry(master,
                       bd = '2')
    
    department_select = StringVar(master)
    department_select.set('none')
    department_dropdown =  OptionMenu(master, department_select, 'CSE', 'ECE', 'EEE', 'IT', 'Mechanical') 
    department_dropdown.config(bg = '#e6caca',
                             bd = '0',
                             fg = 'Black',
                             activebackground = '#e04a31')
    department_dropdown["menu"].config(bg = '#e6caca',
                       bd = '0',
                       fg = 'Black',
                       activebackground = '#e04a31')
    
    cap_entry = Entry(master,
                     bd = '2')
    from functions import gencaptcha
    cap_label = Label(master,
                      text = gencaptcha(),
                      bg = '#e6caca',
                      font = 'calibri 12',
                      padx = '6',
                      pady = '3')
    add_pane.create_text(30, 42,
                         text = 'Name',
                         font = 'calibri 10',
                         fill = '#e04a31')
    add_pane.create_window(75, 60,
                           window = name_entry)
    add_pane.create_text(212, 42,
                         text = 'DOB (DD/MM/YYYY)',
                         font = 'calibri 10',
                         fill = '#e04a31')
    add_pane.create_window(220, 60,
                           window = dob_entry)
    add_pane.create_text(40, 82,
                        text = 'Password',
                        font = 'calibri 10',
                        fill = '#e04a31')
    add_pane.create_window(75,100,
                          window = pass_entry)
    add_pane.create_text(195, 82, 
                         text = 'Qualification', 
                         font = 'calibri 10',
                         fill = '#e04a31')
    add_pane.create_window(220, 100,
                           window = qual_entry)
    add_pane.create_text(25, 120,
                        text = 'Mail',
                        font = 'calibri 10',
                        fill = '#e04a31')
    add_pane.create_window(75, 140, 
                          window = mail_entry)
    add_pane.create_text(190, 120,
                         text = 'Department',
                         font = 'calibri 10',
                         fill = '#e04a31')
    add_pane.create_window(222, 140,
                           window = department_dropdown)
    add_pane.create_window(50, 177,
                           window = cap_label)
    
    add_pane.create_text(178, 160,
                         text = 'Captcha',
                         font = 'calibri 10',
                         fill = '#e04a31')
    add_pane.create_window(220, 180,
                           window = cap_entry)
    add_button = Button(master,
                       text = 'Add',
                       bg = '#e04a31',
                       fg= 'white',
                       activebackground = '#f7ebeb',
                       padx = '20',
                       pady = '5',
                       command = add,
                       bd = '0')
    add_pane.create_window(150, 220,
                           window = add_button)

    mainloop()

#add student window
def add_student():
    #to generate uid
    def gen_uid():
        conn = sqlite3.connect("storage/index.db")
        cur = conn.cursor()
        cur.execute('SELECT * FROM student_info ORDER BY ID DESC LIMIT 1')
        for uid in cur.fetchall():
            prevID = int(uid[0])
        conn.close()
        newID = prevID + 1
        newID = str(newID)
        return newID
    #to perform insertion
    def add():
        name = name_entry.get()
        dob = dob_entry.get()
        password = pass_entry.get()
        contact = contact_entry.get()
        mail = mail_entry.get()
        stream = stream_select.get()
        cap = cap_entry.get()
        uid = gen_uid()
        print(name,dob,password,contact, mail, stream, cap, uid)

        conn = sqlite3.connect("storage/index.db")
        cur = conn.cursor()
        cur.execute('SELECT * FROM captcha')
        row = cur.fetchone()
        if name == '' or dob == '' or password == '' or contact == '' or mail == '' or stream == 'none' or cap == '':
            messagebox.showwarning('Error!','All fields are required!')
        elif cap != row[0]:
            print(row[0])
            print(cap)
            messagebox.showwarning('Captcha Error!', 'Incorrect captcha entered!')
        else:
            cur.execute('INSERT INTO student_info values(?,?,?,?,?,?,?)',( uid, name, password, dob, contact, mail, stream))
            conn.commit()
            conn.close()
            master.destroy()
            messagebox.showinfo('Registration Number', 'Your registration number is ' + uid)

    master = Tk()
    master.geometry('300x250+535+270')
    master.title('Add Student')

    add_pane = Canvas(master,
                      height = '250',
                      width = '300',
                      bg = '#f7ebeb')
    add_pane.pack()

    add_pane.create_rectangle(0,0, 100, 20,
                              fill = '#e04a31',
                              outline = '#e04a31')
    add_pane.create_text(50, 10,
                         text = 'Student',
                         fill = 'white',
                         font = 'calibri 10 bold')

    name_entry = Entry(master,
                      bd = '2')
    dob_entry = Entry(master,
                     bd = '2')
    pass_entry = Entry(master,
                      bd = '2')
    contact_entry = Entry(master,
                          bd = '2')
    mail_entry = Entry(master,
                       bd = '2')
    
    stream_select = StringVar(master)
    stream_select.set('none')
    stream_dropdown =  OptionMenu(master, stream_select, 'CSE', 'ECE', 'EEE', 'IT', 'Mechanical') 
    stream_dropdown.config(bg = '#e6caca',
                             bd = '0',
                             fg = 'Black',
                             activebackground = '#e04a31')
    stream_dropdown["menu"].config(bg = '#e6caca',
                       bd = '0',
                       fg = 'Black',
                       activebackground = '#e04a31')
    
    cap_entry = Entry(master,
                     bd = '2')
    from functions import gencaptcha
    cap_label = Label(master,
                      text = gencaptcha(),
                      bg = '#e6caca',
                      font = 'calibri 12',
                      padx = '6',
                      pady = '3')
    add_pane.create_text(30, 42,
                         text = 'Name',
                         font = 'calibri 10',
                         fill = '#e04a31')
    add_pane.create_window(75, 60,
                           window = name_entry)
    add_pane.create_text(212, 42,
                         text = 'DOB (DD/MM/YYYY)',
                         font = 'calibri 10',
                         fill = '#e04a31')
    add_pane.create_window(220, 60,
                           window = dob_entry)
    add_pane.create_text(40, 82,
                        text = 'Password',
                        font = 'calibri 10',
                        fill = '#e04a31')
    add_pane.create_window(75,100,
                          window = pass_entry)
    add_pane.create_text(180, 82, 
                         text = 'Contact', 
                         font = 'calibri 10',
                         fill = '#e04a31')
    add_pane.create_window(220, 100,
                           window = contact_entry)
    add_pane.create_text(25, 120,
                        text = 'Mail',
                        font = 'calibri 10',
                        fill = '#e04a31')
    add_pane.create_window(75, 140, 
                          window = mail_entry)
    add_pane.create_text(178, 120,
                         text = 'Stream',
                         font = 'calibri 10',
                         fill = '#e04a31')
    add_pane.create_window(222, 140,
                           window = stream_dropdown)
    add_pane.create_window(50, 177,
                           window = cap_label)
    
    
    add_pane.create_text(178, 160,
                         text = 'Captcha',
                         font = 'calibri 10',
                         fill = '#e04a31')
    add_pane.create_window(220, 180,
                           window = cap_entry)
    add_button = Button(master,
                       text = 'Add',
                       bg = '#e04a31',
                       fg= 'white',
                       activebackground = '#f7ebeb',
                       padx = '10',
                       pady = '5',
                       command = add,
                       bd = '0')
    add_pane.create_window(150, 220,
                           window = add_button)

    mainloop()

#delete student window
def del_student():
    #to perform insertion
    def delete():
        uid = uid_entry.get()
        cap = cap_entry.get()

        conn = sqlite3.connect("storage/index.db")
        cur = conn.cursor()
        cur.execute('SELECT * FROM captcha')
        row = cur.fetchone()
        if uid == 'none' or cap == '':
            messagebox.showwarning('Error!','All fields are required!')
        elif cap != row[0]:
            print(row[0])
            print(cap)
            messagebox.showwarning('Captcha Error!', 'Incorrect captcha entered!')
        else:
            cur.execute('DELETE FROM student_info WHERE ID = ?',(uid,))
            conn.commit()
            conn.close()
            master.destroy()
            messagebox.showinfo('Delete Successful', 'Student with ' + uid + ' ID deleted.' )

    master = Tk()
    master.geometry('200x150+535+270')
    master.title('Delete Student')

    del_pane = Canvas(master,
                      height = '150',
                      width = '200',
                      bg = '#f7ebeb')
    del_pane.pack()

    del_pane.create_rectangle(0,0, 100, 20,
                              fill = '#e04a31',
                              outline = '#e04a31')
    del_pane.create_text(50, 10,
                         text = 'Student',
                         fill = 'white',
                         font = 'calibri 10 bold')

    uid_entry = Entry(master,
                      bd = '2')
   
    cap_entry = Entry(master,
                     bd = '2')
    
    from functions import gencaptcha
    cap_label = Label(master,
                      text = gencaptcha(),
                      bg = '#e6caca',
                      font = 'calibri 12',
                      padx = '6',
                      pady = '3')
    del_pane.create_text(20, 30,
                         text = 'ID',
                         font = 'calibri 10',
                         fill = '#e04a31')
    del_pane.create_window(75, 50,
                           window = uid_entry)
    del_pane.create_window(50, 80,
                           window = cap_label)
    
    
    del_pane.create_text(38, 105,
                         text = 'Captcha',
                         font = 'calibri 10',
                         fill = '#e04a31')
    del_pane.create_window(75, 125,
                           window = cap_entry)
    del_button = Button(master,
                       text = 'Delete',
                       bg = '#e04a31',
                       fg= 'white',
                       activebackground = '#f7ebeb',
                       padx = '5',
                       pady = '2',
                       command = delete,
                       bd = '0')
    del_pane.create_window(170, 125,
                           window = del_button)

    mainloop()
    
    
def del_faculty():
    #to perform insertion
    def delete():
        uid = uid_entry.get()
        cap = cap_entry.get()

        conn = sqlite3.connect("storage/index.db")
        cur = conn.cursor()
        cur.execute('SELECT * FROM captcha')
        row = cur.fetchone()
        if uid == 'none' or cap == '':
            messagebox.showwarning('Error!','All fields are required!')
        elif cap != row[0]:
            print(row[0])
            print(cap)
            messagebox.showwarning('Captcha Error!', 'Incorrect captcha entered!')
        else:
            cur.execute('DELETE FROM faculty_info WHERE ID = ?',(uid,))
            conn.commit()
            conn.close()
            master.destroy()
            messagebox.showinfo('Delete Successful', 'Faculty with ' + uid + ' ID deleted.' )

    master = Tk()
    master.geometry('200x150+535+270')
    master.title('Delete Faculty')

    del_pane = Canvas(master,
                      height = '150',
                      width = '200',
                      bg = '#f7ebeb')
    del_pane.pack()

    del_pane.create_rectangle(0,0, 100, 20,
                              fill = '#e04a31',
                              outline = '#e04a31')
    del_pane.create_text(50, 10,
                         text = 'Faculty',
                         fill = 'white',
                         font = 'calibri 10 bold')

    uid_entry = Entry(master,
                      bd = '2')
   
    cap_entry = Entry(master,
                     bd = '2')
    
    from functions import gencaptcha
    cap_label = Label(master,
                      text = gencaptcha(),
                      bg = '#e6caca',
                      font = 'calibri 12',
                      padx = '6',
                      pady = '3')
    del_pane.create_text(20, 30,
                         text = 'ID',
                         font = 'calibri 10',
                         fill = '#e04a31')
    del_pane.create_window(75, 50,
                           window = uid_entry)
    del_pane.create_window(50, 80,
                           window = cap_label)
    
    
    del_pane.create_text(38, 105,
                         text = 'Captcha',
                         font = 'calibri 10',
                         fill = '#e04a31')
    del_pane.create_window(75, 125,
                           window = cap_entry)
    del_button = Button(master,
                       text = 'Delete',
                       bg = '#e04a31',
                       fg= 'white',
                       activebackground = '#f7ebeb',
                       padx = '5',
                       pady = '2',
                       command = delete,
                       bd = '0')
    del_pane.create_window(170, 125,
                           window = del_button)

    mainloop()

