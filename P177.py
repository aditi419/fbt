from tkinter import *
root = Tk()
root.title('Update Details')
root.geometry('400x400')

label = Label(root,text='Name: ') 
label.place(relx=0.3,rely=0.1,anchor=CENTER)

user_name = Entry(root)
user_name.place(relx=0.6,rely=0.1,anchor=CENTER)

label2 = Label(root,text='Password: ')
label2.place(relx=0.3,rely=0.2,anchor=CENTER)

password = Entry(root)
password.place(relx=0.6,rely=0.2,anchor=CENTER)

label3 = Label(root,text='Captcha: ')
label3.place(relx=0.3,rely=0.3,anchor=CENTER)

captcha = Entry(root)
captcha.place(relx=0.6,rely=0.3,anchor=CENTER)

label4 = Label(root)
label4.place(relx=0.5,rely=0.6,anchor=CENTER)

label5 = Label(root)
label5.place(relx=0.5,rely=0.7,anchor=CENTER)

label6 = Label(root)
label6.place(relx=0.5,rely=0.8,anchor=CENTER)

class userDB():
    def __init__(self):
        self.__username = 'Aditi'
        self.__password = 'Aditi2010'
        self.__captcha = '301A'
    def showUser(self):
        label4['text'] = 'Name: ' + self.__username
        label5['text'] = 'Password: ' + self.__password
        label6['text'] = 'Captcha: ' + self.__captcha
        
obj1 = userDB()

def addUser():
    global obj1
    obj1 = user_name.get()
    obj1 = password.get()
    obj1 = captcha.get()
    print('Details Updated')
    
btn = Button(root,text='Update Login Details',command=addUser)
btn.place(relx=0.3,rely=0.45,anchor=CENTER)

btn = Button(root,text='Show Profile',command=obj1.showUser)
btn.place(relx=0.3,rely=0.45,anchor=CENTER)

root.mainloop()