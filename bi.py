import re
from tkinter import *
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
        out_frame.place(x=10, y=10, width=750, height=620)
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
        self.p_qty = Entry(p_frame, width=20, fg="black", border=0, bg="white",
                           font=('Microsoft YaHei UI Light', 14))
        self.p_qty.place(x=420, y=35)
        self.p_qty.insert(0, 'Quantity')
        self.p_qty.bind('<FocusIn>', self.qenter)
        self.p_qty.bind('<FocusOut>', self.qleave)
        Frame(p_frame, width=150, height=2, bg='black').place(x=420, y=65)
        self.btn_submit = Button(p_frame, text="Add Item", font=('Microsoft YaHei UI Light', 16), bg='#57a1f8',
                                 fg='white', cursor='hand2', command=self.p_add)
        self.btn_submit.place(x=40, y=280)

        '''self.p_id = ttk.Combobox(p_frame, values=self.lst, width=35, font=('Microsoft YaHei UI Light', 14))
        self.p_id.place(x=7, y=30)
        self.p_id.bind('<KeyRelease>', self.search)
        self.p_qty = Entry(p_frame, width=25, fg="black", border=0, bg="white",
                           font=('Microsoft YaHei UI Light', 14))
        self.p_qty.place(x=15, y=85)
        self.p_qty.insert(0, 'Quantity')
        self.p_qty.bind('<FocusIn>', self.qenter)
        self.p_qty.bind('<FocusOut>', self.qleave)
        Frame(p_frame, width=150, height=2, bg='black').place(x=15, y=115)
        self.btn_submit = Button(p_frame, text="Add Item", font=('Microsoft YaHei UI Light', 16), bg='#57a1f8',
                                 fg='white', cursor='hand2', command=self.p_add)
        self.btn_submit.place(x=40, y=200)'''

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


if __name__ == "__main__":
    rot = Tk()
    ob = billsoft(rot)
    rot.mainloop()
