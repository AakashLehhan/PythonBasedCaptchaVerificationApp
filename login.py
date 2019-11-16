def main():
    import random
    import sqlite3

    conn=sqlite3.connect("storage/index.db")
    cur=conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS faculty_info(ID text(10) PRIMARY KEY, Name text(20), Password text(20), DOB date, Mail text(20), Qualification text(20), Department text(20))''')
    cur.execute('SELECT COUNT(ID) FROM faculty_info')
    count = cur.fetchone()
    if count[0] == 0:
        cur.execute('INSERT INTO faculty_info VALUES(?,?,?,?,?,?,?)',( '11900', 'None', 'none', 'none', 'none', 'none','none'))
        conn.commit()
    cur.execute('''CREATE TABLE IF NOT EXISTS student_info(ID text(10) PRIMARY KEY, Name text(20), Password text(20), DOB date, Contact text(15), Mail text(20), Stream text(20))''')
    cur.execute('SELECT COUNT(ID) FROM student_info')
    count = cur.fetchone()
    if count[0] == 0:
        cur.execute('INSERT INTO student_info VALUES(?,?,?,?,?,?,?)',( '2019000', 'None', 'none', 'none', 'none', 'none','none'))
        conn.commit()
    cur.execute('''CREATE TABLE IF NOT EXISTS captcha(captcha text)''')
    conn.commit()
    conn.close()
    
    def about():
        messagebox.showinfo('About','This program is developed by Aakash, Anshul and Simran.')

    def gencaptcha():
        n1 = str(random.randint(0, 9))
        n2 = str(random.randint(0, 9))
        n3 = str(random.randint(0, 9))
        t1 = chr(random.randint(65,90))
        t2 = chr(random.randint(97,122))
        t3 = chr(random.randint(65,90))
        cap = t1 + t2 + n1 + t3 + n3 + n2
        conn = sqlite3.connect('storage/index.db')
        cur = conn.cursor()
        cur.execute("DELETE FROM captcha")
        cur.execute("INSERT INTO captcha VALUES(?)",(cap,))
        conn.commit()
        conn.close()
        return cap

    def refresh():
        cap_label.config(text = gencaptcha())   
        return

    def login():
        user_id = regn_entry.get()
        pswd = pass_entry.get()
        captcha = cap_entry.get()

        conn = sqlite3.connect('storage/index.db')
        cur = conn.cursor()

        cur.execute('SELECT * FROM captcha')
        row = cur.fetchone()
        if captcha != row[0]:
            if captcha == '':
                messagebox.showwarning('Error!', 'All fields are required!')
                return
            else:
                messagebox.showerror('Captcha Error', 'Incorrect captcha entered!')
                return
        else:
            if user_id != 'admin':
                cur.execute('SELECT * FROM faculty_info')
                for row in cur.fetchall():
                    if row[0] == user_id and row[2] == pswd:
                        conn.close()
                        from faculty import faculty
                        master.destroy()
                        faculty(row[0])
                        return
                    else:
                        cur.execute('SELECT * FROM student_info')
                        for row in cur.fetchall():
                            if row[0] == user_id and row[2] == pswd:
                                conn.close()
                                from student import student
                                master.destroy()
                                student(row[0])
                                return
                messagebox.showerror('Error', 'Incorrect user details.')
                return
            elif pswd != 'admin':
                messagebox.showerror('Error', 'Incorrect user details.')
                return
            else:
                conn.close()
                from admin import admin
                master.destroy()
                admin()


    from tkinter import Tk, Label, Entry, Button, messagebox, Menu, Canvas, mainloop, PhotoImage
    master = Tk()


    master.geometry('400x500+484+100')
    master.configure(bg = '#e6caca')
    master.title('Login - Enter your correct details')


    navbar = Menu(master)
    navbar.add_command(label = 'About',
                       command = about)
    master.configure(menu = navbar)


    ums_logo = PhotoImage(file = 'icon/ums_logo.png')
    title_label = Label(master,
                        image = ums_logo,
                        bg = '#e6caca')
    title_label.pack()
    

    blank_label = Label(text = '',
                        bg = '#e6caca')
    blank_label.pack()


    login_pane = Canvas(master,
                        height = '400',
                        width = '400',
                        bg = '#f7ebeb')
    login_pane.pack()

    login_pane.create_line(180, 100, 180, 240,
                           dash = (4,2))

    login_pane.create_rectangle(0, 10, 20, 60,
                                fill = '#e04a31',
                                outline = '#e04a31')
    login_pane.create_text(70, 35,
                           text = 'Sign In',
                           font = 'calibri 20',
                           fill = '#e04a31')

    login_pane.create_rectangle(50, 300, 350, 370,
                                fill = '#e04a31',
                                outline = '#e04a31')
    login_pane.create_text(200, 335,
                           text = "Captcha verification to get authenticated!",
                           fill = 'white',
                           font = 'calibri 10')

    #login details

    login_image =PhotoImage(file = 'icon/login_scrn.png')
    login_button = Button(master,
                          image = login_image,
                          bd = '0',
                          bg = '#f7ebeb',
                          activebackground = '#f7ebeb',
                          command = login)
    login_pane.create_window(90, 170,
                             window = login_button)

    regn_entry = Entry(master,
                       bd = '2')
    pass_entry = Entry(master,
                       bd = '2')
    cap_entry = Entry(master,
                      bd = '2')

    login_pane.create_text(245, 80,
                           text = 'User ID',
                           fill = '#e04a31',
                           font = 'calibri 8')
    login_pane.create_window(290, 100,
                             window = regn_entry)

    login_pane.create_text(251, 125,
                           text = 'Password',
                           fill = '#e04a31',
                           font = 'calibri 8')
    login_pane.create_window(290, 145,
                             window = pass_entry)


    refresh_img = PhotoImage(file = 'icon/refresh.png')
    refresh_btn = Button(master,
                         image = refresh_img,
                         bd = '0',
                         bg = '#f7ebeb',
                         activebackground = '#f7ebeb',
                         command = refresh)
    login_pane.create_window(340, 195,
                             window = refresh_btn)

    cap_label = Label(master,
                      text = gencaptcha(),
                      font = 'calibri 12',
                      bg = '#e6caca',
                      padx = '10',
                      pady = '10')
    login_pane.create_window(275, 195,
                             window = cap_label)

    login_pane.create_text(246, 234,
                           text = 'Captcha',
                           fill = '#e04a31',
                           font = 'calibri 8')
    login_pane.create_window(290, 255,
                             window = cap_entry)

    mainloop()

if __name__ == "__main__":
    main()


