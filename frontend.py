from tkinter import *
from backend import Database


database = Database('books.db')

window=Tk()

window.wm_title("BookStore")

l1=Label(window,text="Title")
l1.grid(row=0,column=0)

l2=Label(window,text="Author")
l2.grid(row=0,column=2)

l3=Label(window,text="Year")
l3.grid(row=1,column=0)

l4=Label(window,text="ISBN")
l4.grid(row=1,column=2)

title_text=StringVar()
e1=Entry(window,textvariable=title_text)
e1.grid(row=0,column=1)

author_text=StringVar()
e2=Entry(window,textvariable=author_text)
e2.grid(row=0,column=3)

year_text=StringVar()
e3=Entry(window,textvariable=year_text)
e3.grid(row=1,column=1)

isbn_text=StringVar()
e4=Entry(window,textvariable=isbn_text)
e4.grid(row=1,column=3)


class frontend():

    def __init__(self):
        self.list1=Listbox(window, height=6,width=35)
        self.list1.grid(row=2,column=0,rowspan=6,columnspan=2)

        self.sb1=Scrollbar(window)
        self.sb1.grid(row=2,column=2,rowspan=6)

        self.list1.configure(yscrollcommand=self.sb1.set)
        self.sb1.configure(command= self.list1.yview)
        self.list1.bind('<<ListboxSelect>>',self.get_selected_row)


    def get_selected_row(self, event):
        global selected_tuple
        index=self.list1.curselection()[0]
        selected_tuple=self.list1.get(index)
        e1.delete(0,END)
        e1.insert(END,selected_tuple[1])
        e2.delete(0,END)
        e2.insert(END,selected_tuple[2])
        e3.delete(0,END)
        e3.insert(END,selected_tuple[3])
        e4.delete(0,END)
        e4.insert(END,selected_tuple[4])


    def view_command(self):
        self.list1.delete(0,END)
        for row in database.view():
            self.list1.insert(END,row)

    def search_command(self):
        self.list1.delete(0,END)
        for row in database.search(title_text.get(),author_text.get(),year_text.get(),isbn_text.get()):
            self.list1.insert(END,row)

    def add_command(self):
        database.insert(title_text.get(),author_text.get(),year_text.get(),isbn_text.get())
        self.list1.delete(0,END)
        self.list1.insert(END,(title_text.get(),author_text.get(),year_text.get(),isbn_text.get()))

    def delete_command(self):
        database.delete(selected_tuple[0])

    def update_command(self):
        database.update(selected_tuple[0],title_text.get(),author_text.get(),year_text.get(),isbn_text.get())


app = frontend()

b1=Button(window,text="View all", width=12,command=app.view_command)
b1.grid(row=2,column=3)

b2=Button(window,text="Search entry", width=12,command=app.search_command)
b2.grid(row=3,column=3)

b3=Button(window,text="Add entry", width=12,command=app.add_command)
b3.grid(row=4,column=3)

b4=Button(window,text="Update selected", width=12,command=app.update_command)
b4.grid(row=5,column=3)

b5=Button(window,text="Delete selected", width=12,command=app.delete_command)
b5.grid(row=6,column=3)

b6=Button(window,text="Close", width=12,command=window.destroy)
b6.grid(row=7,column=3)

window.mainloop()
