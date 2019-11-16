import sqlite3
def student(regn):
    def about():
        messagebox.showinfo('About','This program is developed by Aakash, Anshul and Simran.')

    def logout():
        from login import main
        master.destroy()
        main()

    from tkinter import Tk, Label, Entry, Button, messagebox, Menu, Canvas, mainloop, PhotoImage
    master = Tk()

    master.geometry('400x500+484+100')
    master.configure(bg = '#e6caca')
    master.title('Student Portal')

    navbar = Menu(master)
    navbar.add_command(label = 'About',
                       command=about)
    master.configure(menu = navbar)

    ums_logo = PhotoImage(file = 'icon/ums_logo.png')
    title_label = Label(master,
                        image = ums_logo,
                        bg = '#e6caca')
    title_label.pack()

    blank_label = Label(text = '',
                        bg = '#e6caca')
    blank_label.pack()

    student_pane = Canvas(master,
                        height = '400',
                        width = '400',
                        bg = '#f7ebeb')
    student_pane.pack()

    student_pane.create_rectangle(0, 10, 20, 60,
                                fill = '#e04a31',
                                outline = '#e04a31')
    student_pane.create_text(120, 35,
                           text = 'Homepage',
                           font = 'calibri 20',
                           fill = '#e04a31')

    signout_img = PhotoImage(file = 'icon/exit.png')
    signout_btn = Button(master,
                         image = signout_img,
                         bd = '0',
                         activebackground = '#f7ebeb',
                         bg = '#f7ebeb',
                         command = logout)
    student_pane.create_window(365, 35,
                             window = signout_btn)

    student_pane.create_rectangle(50, 300, 350, 370,
                                fill = '#e04a31',
                                outline = '#e04a31')
    student_pane.create_text(200, 335,
                           text = "Student panel",
                           fill = 'white',
                           font = 'calibri 10')
    
    conn = sqlite3.connect('storage/index.db')
    cur = conn.cursor()
    cur.execute("SELECT ID, Name, Mail, Stream FROM student_info where ID = ?",(regn,))
    info = cur.fetchone()
    stream = info[3]
    student_pane.create_text(100, 100,
                             text = info[1],
                             font = 'Calibri 15 bold',
                             fill = '#e04a31')
    student_pane.create_text(80, 120,
                             text = info[0],
                             font = 'Calibri 12 bold')
    student_pane.create_text(300, 100,
                             text = info[2],
                             font = 'Calibri 12',
                             fill = 'Blue')
    student_pane.create_text(110, 150,
                             text = 'Department: ',
                             fill = 'gray',
                             font = 'Calibri 12 bold')
    student_pane.create_text(180, 165,
                             text = stream)
    student_pane.create_text(100, 180,
                             text = 'Teachers :',
                             fill = 'gray',
                             font = 'calibri 12 bold')
    cur.execute("SELECT ID, Name, Mail FROM faculty_info where Department = ?",(stream,))
    y = 200
    for info in cur.fetchall():
        student_pane.create_text(90, y,
                                 text = info[0])
        student_pane.create_text(150, y,
                                 text = info[1])
        student_pane.create_text(300, y,
                                 text = info[2])
        y += 15
    conn.close()


    mainloop()