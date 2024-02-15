from tkinter import *
import re
from tkinter import ttk, LabelFrame, messagebox
from PIL import Image, ImageTk


class billsoft():
    def __init__(self, rot):
        self.rot = rot
        self.rot.geometry('1600x720+0+0')
        self.rot.title('BILL SOFTWARE')
        self.rot.config(bg='#156681')
        self.rot.resizable(1, 1)
        # menu bar
        menubar = Menu(self.rot)
        self.rot.config(menu=menubar)
        fileMenu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label='File', menu=fileMenu)
        fileMenu.add_command(label='open')
        fileMenu.add_command(label='save')
        fileMenu.add_command(label='print')
        fileMenu.add_command(label='exit')

        # variables
        self.lst = ['HTML and CSS', 'Python', 'Java', 'JavaScript', 'Swift', 'C++', 'C', 'R']
        self.item = StringVar()

        out_frame = Frame(self.rot, bd=5, relief=GROOVE, bg='white')
        out_frame.place(x=10, y=10, width=800, height=620)
        # CUSTOMER FRAME
        c_frame = LabelFrame(out_frame, text='CUSTOMER', font=('Times New Romen', 11, 'bold'), bg='white', fg='#57a1f8')
        c_frame.place(x=10, y=5, width=700, height=140)
        self.c_mno = Entry(c_frame, width=25, fg="black", border=0, bg="white",
                           font=('Microsoft YaHei UI Light', 14))
        self.c_mno.place(x=4, y=10)
        self.c_mno.insert(0, 'Mobile.No')
        self.c_mno.bind('<FocusIn>', self.enter)
        self.c_mno.bind('<FocusOut>', self.leave)
        Frame(c_frame, width=200, height=2, bg='black').place(x=5, y=37)
        self.c_name = Entry(c_frame, width=25, fg="black", border=0, bg="white",
                            font=('Microsoft YaHei UI Light', 14))
        self.c_name.place(x=300, y=10)
        self.c_name.insert(0, 'Name')
        self.c_name.bind('<FocusIn>', self.penter)
        self.c_name.bind('<FocusOut>', self.pleave)
        Frame(c_frame, width=200, height=2, bg='black').place(x=300, y=37)
        # PRODUCT FRAME
        p_frame = LabelFrame(out_frame, text='PRODUCT DETAILS', font=('Times New Romen', 11, 'bold'), bg='white',
                             fg='#57a1f8')
        p_frame.place(x=10, y=150, width=700, height=400)
        p_title = Label(p_frame, text='Product ID or NAME', fg='#57a1f8', bg='white',
                        font=('Microsoft YaHei UI Light', 14, 'bold'))
        p_title.place(x=10, y=5)
        self.p_id = Entry(p_frame, width=30, fg="black", border=0, bg="white",
                          font=('Microsoft YaHei UI Light', 14), textvariable=self.item)
        self.p_id.place(x=10, y=30)
        Frame(p_frame, width=320, height=2, bg='black').place(x=10, y=60)
        self.p_item = Listbox(p_frame, width=30, bg='white', height=6, font=('Microsoft YaHei UI Light', 14),
                              relief=FLAT)
        self.p_item.place(x=10, y=70)
        self.item.trace('w', self.get_data)
        self.p_item.bind('<<ListboxSelect>>', self.upd)
        self.p_qty = Entry(p_frame, width=25, fg="black", border=0, bg="white",
                           font=('Microsoft YaHei UI Light', 14))
        self.p_qty.place(x=15, y=235)
        self.p_qty.insert(0, 'Quantity')
        self.p_qty.bind('<FocusIn>', self.qenter)
        self.p_qty.bind('<FocusOut>', self.qleave)
        Frame(p_frame, width=150, height=2, bg='black').place(x=15, y=265)
        self.btn_submit = Button(p_frame, text="Add Item", font=('Microsoft YaHei UI Light', 16), bg='#57a1f8',
                                 fg='white', cursor='hand2', command=self.p_add)
        self.btn_submit.place(x=40, y=280)

    def upd(self, e):
        data = e.widget
        index = int(data.curselection()[0])
        value = data.get(index)
        self.item.set(value)
        self.p_item.delete(0, 'end')

    def get_data(self, *args):
        s_data = self.p_id.get()
        self.p_item.delete(0, 'end')
        for i in self.lst:
            if re.match(s_data, i, re.IGNORECASE):
                self.p_item.insert('end', i)

    def p_add(self):
        name = self.c_name.get()
        no = int(self.c_mno.get())
        item = self.p_id.get()
        qty = int(self.p_qty.get())
        l = [name, no, item, qty]
        print(l)
        self.p_qty.delete(0, 'end')
        self.p_qty.insert(0, 'Quantity')
        self.p_id.delete(0, 'end')

    def enter(self, e):
        self.c_mno.delete(0, 'end')

    def leave(self, e):
        name = self.c_mno.get()
        if name == '':
            self.c_mno.insert(0, 'Mobile.No')

    def qenter(self, e):
        self.p_qty.delete(0, 'end')

    def qleave(self, e):
        name = self.p_qty.get()
        if name == '':
            self.p_qty.insert(0, 'Quantity')

    def penter(self, e):
        self.c_name.delete(0, 'end')

    def pleave(self, e):
        name = self.c_name.get()
        if name == '':
            self.c_name.insert(0, 'Name')

    def search(self, event):
        value = self.p_id.get()
        if value == '':
            self.p_id['value'] = self.lst
        else:
            data = []
            for i in self.lst:
                if value.lower() in i.lower():
                    data.append(i)
                    self.p_id['value'] = data


class login_bill():
    def __init__(self, root):
        self.root = root
        self.root.geometry('925x500+300+200')
        self.root.title('LOGIN')
        self.root.config(bg='#FFFFFF')
        self.root.resizable(False, False)
        img = Image.open("image/lg.jpg")
        img1 = img.resize((350, 350), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img1)
        lb_img = Label(self.root, image=self.photoimg, bg="white")
        lb_img.place(x=50, y=50)
        log_frame = Frame(self.root, width=350, height=350, bg="white")
        log_frame.place(x=480, y=70)
        log_title = Label(log_frame, text='Log in', fg='#57a1f8', bg='white',
                          font=('Microsoft YaHei UI Light', 23, 'bold'))
        log_title.place(x=100, y=5)
        # USERNAME
        self.log_user = Entry(log_frame, width=25, fg="black", border=0, bg="white",
                              font=('Microsoft YaHei UI Light', 11))
        self.log_user.place(x=30, y=80)
        self.log_user.insert(0, 'Username')
        self.log_user.bind('<FocusIn>', self.enter)
        self.log_user.bind('<FocusOut>', self.leave)
        Frame(log_frame, width=295, height=2, bg='black').place(x=25, y=107)
        # PASSWORD
        self.log_paswd = Entry(log_frame, width=25, fg="black", border=0, bg="white",
                               font=('Microsoft YaHei UI Light', 11))
        self.log_paswd.place(x=30, y=160)
        self.log_paswd.insert(0, 'Password')
        self.log_paswd.bind('<FocusIn>', self.penter)
        self.log_paswd.bind('<FocusOut>', self.pleave)
        Frame(log_frame, width=295, height=2, bg='black').place(x=25, y=187)
        # BUTTON SIGN IN
        self.btn_sin = Button(log_frame, width=39, pady=7, text='Sign in', bg='#57a1f8', fg='white', border=0,
                              command=self.sign_in)
        self.btn_sin.place(x=35, y=204)

    def enter(self, e):
        self.log_user.delete(0, 'end')

    def leave(self, e):
        name = self.log_user.get()
        if name == '':
            self.log_user.insert(0, 'Username')

    def penter(self, e):
        self.log_paswd.delete(0, 'end')

    def pleave(self, e):
        name = self.log_paswd.get()
        if name == '':
            self.log_paswd.insert(0, 'Password')

    def sign_in(self):
        name = self.log_user.get()
        pawd = self.log_paswd.get()
        if name == 'admin' and pawd == '1234':
            self.root.destroy()
            rot = Tk()
            ob = billsoft(rot)
            rot.mainloop()
        elif name != 'admin':
            messagebox.showerror('Invalid', 'Invalid Username')
        elif pawd != '1234':
            messagebox.showerror('Invalid', 'Invalid Password')


if __name__ == "__main__":
    root = Tk()
    obj = login_bill(root)
    root.mainloop()
