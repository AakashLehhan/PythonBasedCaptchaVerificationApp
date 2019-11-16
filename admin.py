import sqlite3

def admin():
    def about():
        messagebox.showinfo('About','This program is developed by Aakash, Anshul and Simran.')

    def logout():
        from login import main
        master.destroy()
        main()

    def refresh():
        conn = sqlite3.connect('storage/index.db')
        cur = conn.cursor()
        cur.execute('SELECT COUNT(ID) FROM faculty_info')
        count = cur.fetchone()
        count = count[0] - 1
        fac_count_label.config(text = count)
        cur.execute('SELECT COUNT(ID) FROM student_info')
        count = cur.fetchone()
        count = count[0] - 1
        stu_count_label.config(text = count)
        conn.close()
        return

    from tkinter import Tk, Label, Button, messagebox, Menu, Canvas, mainloop, PhotoImage
    master = Tk()

    master.geometry('400x500+484+100')
    master.configure(bg = '#e6caca')
    master.title('Administration')

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

    admin_pane = Canvas(master,
                        height = '400',
                        width = '400',
                        bg = '#f7ebeb')
    admin_pane.pack()

    admin_pane.create_line(200, 125, 200, 250, dash = (4,2))

    admin_pane.create_rectangle(0, 10, 20, 60,
                                fill = '#e04a31',
                                outline = '#e04a31')
    admin_pane.create_text(120, 35,
                           text = 'Administration',
                           font = 'calibri 20',
                           fill = '#e04a31')

    #faculty
    admin_pane.create_text(100, 100,
                           text = 'Faculty corner',
                           font = 'calibri 15 bold')

    from functions import add_faculty
    add_faculty = Button(master,
                         text = 'Add faculty',
                         bd = '0',
                         activebackground = '#f7ebeb',
                         bg = '#e6caca',
                         padx = '16',
                         pady = '10',
                         font = 'calibri 10',
                         command = add_faculty)
    admin_pane.create_window(100, 150,
                             window = add_faculty)
    from functions import del_faculty
    del_fac = Button(master,
                         text = 'Delete faculty',
                         bd = '0',
                         activebackground = '#f7ebeb',
                         bg = '#e04a31',
                         padx = '10',
                         pady = '10',
                         font = 'calibri 10',
                         command = del_faculty)
    admin_pane.create_window(100, 200,
                             window = del_fac)

    admin_pane.create_text(80, 250,
                           text = 'Count: ',
                           font = 'Calibri 12')
    fac_count_label = Label(master,
                        text = 'null',
                        bg = '#e6caca',
                        font = 'calibri 12')
    admin_pane.create_window(125, 250,
                             window = fac_count_label)

    #student
    admin_pane.create_text(300, 100,
                           text = 'Student corner',
                           font = 'calibri 15 bold')
    from functions import add_student
    add_student = Button(master,
                         text = 'Add student',
                         bd = '0',
                         activebackground = '#f7ebeb',
                         bg = '#e6caca',
                         padx = '16',
                         pady = '10',
                         font = 'calibri 10',
                         command = add_student)
    admin_pane.create_window(300,
                             150,
                             window = add_student)
    from functions import del_student
    del_stu = Button(master,
                         text = 'Delete student',
                         bd = '0',
                         activebackground = '#f7ebeb',
                         bg = '#e04a31',
                         padx = '10',
                         pady = '10',
                         font = 'calibri 10',
                         command = del_student)
    admin_pane.create_window(300, 200,
                             window = del_stu)

    admin_pane.create_text(280, 250,
                           text = 'Count: ',
                           font = 'Calibri 12')
    stu_count_label = Label(master,
                        text = '',
                        bg = '#e6caca',
                        font = 'calibri 12')
    admin_pane.create_window(325, 250,
                             window = stu_count_label)
    
    refresh_img = PhotoImage(file = 'icon/refresh.png')
    refresh_btn = Button(master,
                         image = refresh_img,
                         bd = '0',
                         bg = '#f7ebeb',
                         activebackground = '#f7ebeb',
                         command = refresh)
    admin_pane.create_window(325, 35,
                             window = refresh_btn)
    
    signout_img = PhotoImage(file = 'icon/exit.png')
    signout_btn = Button(master,
                         image = signout_img,
                         bd = '0',
                         activebackground = '#f7ebeb',
                         bg = '#f7ebeb',
                         command = logout)
    admin_pane.create_window(365, 35,
                             window = signout_btn)

    admin_pane.create_rectangle(50, 300, 350, 370,
                                fill = '#e04a31',
                                outline = '#e04a31')
    admin_pane.create_text(200, 335,
                           text = "Administration panel.",
                           fill = 'white',
                           font = 'calibri 10')

    refresh()
    mainloop()
