import pyodbc
import os
from tkinter import *
from tkinter import simpledialog
import json
import speech_recognition as sr
import tkinter as tk
from PIL import ImageTk,Image  
from tkinter import messagebox
from difflib import get_close_matches
data = json.load(open("data.json"))
word = ""

# import app.py
# import mysql.connector as c
# import pymysql

class Login:

   def __init__(self, root):

      self.root = root
      self.root.title("Login and registration system for Apps")
      self.root.geometry("1366x700+0+0")
      self.root.resizable(False, False)
      self.loginform()

   def loginform(self):

      Frame_login = Frame(self.root, )
      Frame_login.place(x=0, y=0, height=700, width=1366)

      # bg = PhotoImage(file = "C:\\Users\\Haier\\Documents\\Downloads\\1.png")
      # image = Image.open("C:\\Users\\Haier\\Desktop\\Python Project\\12.png")
      self.img = ImageTk.PhotoImage(Image.open("C:\\Users\\Haier\\Desktop\\Python Project\\123.png"))
      img=Label(Frame_login,image=self.img).place(x=0,y=0,width=1366,height=700)
      frame_input = Frame(self.root, bg='white')
      frame_input.place(x=0, y=0, height=800, width=550)

      label1 = Label(frame_input, text="Login Here", font=('roboto', 32, 'bold'),
                     fg="black", bg='white')

      label1.place(x=110, y=100)

      label2 = Label(frame_input, text="Username", font=("calibre", 20, "bold"),
                     fg='orangered', bg='white')

      label2.place(x=100, y=200)

      self.email_txt = Entry(frame_input, font=("calibre", 15, "bold"),

                           bg='white', bd = 1)

      self.email_txt.place(x=100, y=250, width=270, height=35)

      label3 = Label(frame_input, text="Password", font=("calibre", 20, "bold"),

                     fg='orangered', bg='white')

      label3.place(x=100, y=300)

      self.password = Entry(frame_input, font=("calibre", 15, "bold"),

                           bg='white', show='*' , bd = 1)

      # passw_entry=tk.Entry(root, textvariable = passw_var, font = ('calibre',10,'normal'), show = '*')

      self.password.place(x=100, y=350, width=270, height=35)

      btn1 = Button(frame_input, text="forgot password?", cursor='hand2',

                  font=('calibri', 10), bg='white', fg='black', bd=0)

      btn1.place(x=180, y=400)

      btn2 = Button(frame_input, text="Login", command=self.login, cursor="hand2",

                  font=("calibre", 15), fg="white", bg="orangered",

                  bd=0, width=15, height=1)

      btn2.place(x=150, y=430)

      btn3 = Button(frame_input, command=self.Register, text="Not Registered? Register",
                     cursor="hand2", font=("calibri", 10), bg='white', fg="black", bd=0)

      btn3.place(x=170, y=480)

   def login(self):

      if self.email_txt.get() == "" or self.password.get() == "":

         messagebox.showerror(
               "Error", "All fields are required", parent=self.root)

      else:

         try:
               # con=mysql.connector.connect(host='localhost',user='muhammadhusnain',password='101325')
               conn = pyodbc.connect('Driver={SQL Server};'
                                    'Database=MailUserData;'
                                    'Server=HUSNAIN\MSSQLSERVER01;'
                                       'Trusted_Connection=yes;')
               cur = conn.cursor()
               d1 = self.email_txt.get()
               d2 = self.password.get()
               print(d1)
               print(d2)
               cur.execute("SELECT username,password FROM register where username = ? and password =?",d1, d2)
               # cur.execute(
               #    "SELECT Email,Password FROM AdminData where Email = ? and Password =?", d1, d2)

               row = cur.fetchall()
               if row:
                  self.appscreen()
                  # os.system('app.py')
                  # execfile('app.py')

                  conn.close()

               else:
                  messagebox.showerror(
                     'Error', 'Invalid Username And Password', parent=self.root)
                  self.loginclear()
                  self.email_txt.focus()

         except Exception as es:
               messagebox.showerror(
                  'Error', f'Error Due to : {str(es)}', parent=self.root)

   def Register(self):

      Frame_login1 = Frame(self.root, bg="white")

      Frame_login1.place(x=0, y=0, height=700, width=1366)

      self.img_register = ImageTk.PhotoImage(Image.open("C:\\Users\\Haier\\Desktop\\Python Project\\333.jpg"))
      img2=Label(Frame_login1,image=self.img_register).place(x=490,y=0,width=1200,height=700)
      
      frame_input2 = Frame(self.root, bg='white')

      frame_input2.place(x=0, y=130, height=700, width=630)

      label1 = Label(frame_input2, text="Register Here", font=('roboto', 32, 'bold'),

                     fg="black", bg='white')

      label1.place(x=145, y=10)

      label2 = Label(frame_input2, text="Username", font=("calibre", 20, "bold"),

                     fg='orangered', bg='white')

      label2.place(x=30, y=95)

      self.entry = Entry(frame_input2, font=(
         "calibre", 15, "bold"), bg='white' , bd = 1)

      self.entry.place(x=30, y=145, width=270, height=35)

      label3 = Label(frame_input2, text="Password", font=(
         "calibre", 20, "bold"), fg='orangered', bg='white')

      label3.place(x=30, y=195)

      self.entry3 = Entry(frame_input2, font=(
         "calibre", 15, "bold"), bg='white' , bd = 1)

      self.entry3.place(x=30, y=245, width=270, height=35)

      label4 = Label(frame_input2, text="Email-id",
                     font=("calibre", 20, "bold"), fg='orangered', bg='white')

      label4.place(x=330, y=95)

      self.entry2 = Entry(frame_input2, font=(
         "calibre", 15, "bold"), bg='white' , bd = 1)

      self.entry2.place(x=330, y=145, width=270, height=35)

      label5 = Label(frame_input2, text="Confirm Password",

      font=("calibre", 20, "bold"), fg='orangered', bg='white')

      label5.place(x=330, y=195)

      self.entry4 = Entry(frame_input2, font=(
         "calibre", 15, "bold"), bg='white' , bd = 1)

      self.entry4.place(x=330, y=245, width=270, height=35)

      btn2 = Button(frame_input2, command=self.register, text="Register", cursor="hand2", font=("calibre", 15), fg="white",

                  bg="orangered", bd=0, width=15, height=1)

      btn2.place(x=220, y=340)

      btn3 = Button(frame_input2, command=self.loginform,

                  text="Already Registered?Login", cursor="hand2",

                  font=("calibri", 10), bg='white', fg="black", bd=0)

      btn3.place(x=240, y=390)

   def register(self):

      if self.entry.get() == "" or self.entry2.get() == "" or self.entry3.get() == "" or self.entry4.get() == "":

         messagebox.showerror(
               "Error", "All Fields Are Required", parent=self.root)

      elif self.entry3.get() != self.entry4.get():

         messagebox.showerror(
               "Error", "Password and Confirm Password Should Be Same", parent=self.root)

      else:

         try:
               con = pyodbc.connect('Driver={SQL Server};'
                                    'Database=MailUserData;'
                                    'Server=HUSNAIN\MSSQLSERVER01;'
                                       'Trusted_Connection=yes;')

            # cursor = conn.cursor()
               cur = con.cursor()

               cur.execute("select * from register where emailid=?",
                           self.entry3.get())

               row = cur.fetchone()

               if row != None:

                  messagebox.showerror(
                     "Error", "User already Exist,Please try with another Email", parent=self.root)

                  self.regclear()

                  self.entry.focus()

               else:
                  p1 = self.entry.get()
                  p2 = self.entry2.get()
                  p3 = self.entry3.get()
                  p4 = self.entry4.get()
                  print(p1)
                  cur.execute(
                     "insert into register(username,emailid,password ,confirmpassword)  values(?,?,?,?)", p1, p2, p3, p4)

                  con.commit()

                  con.close()

                  messagebox.showinfo(
                     "Success", "Register Succesfull", parent=self.root)

                  self.regclear()

         except Exception as es:

               messagebox.showerror(
                  "Error", f"Error due to:{str(es)}", parent=self.root)

   def appscreen(self):
      Frame_login = Frame(self.root, bg='white')
      Frame_login.place(x=0, y=0, height=700, width=1366 )

      self.bgAppImg = ImageTk.PhotoImage(Image.open("C:\\Users\\Haier\\Desktop\\Python Project\\des.png"))
      bgImg=Label(Frame_login,image=self.bgAppImg , bg='white').place(x=0,y=0,width=1362,height=700)


      # panel = PanedWindow(bd  = 4 , relief = "raised" , bg = "red")
      # panel.pack( fill = BOTH , expand = 1)
      # panel_1 = PanedWindow(panel ,orient = VERTICAL , bd  = 4 , relief = "raised" , bg = "black")
      # panel.add(panel_1)

      # panel_2 = PanedWindow(panel_1 ,bd  = 4 , relief = "raised" , bg = "blue")
      # panel_1.add(panel_2)

      # panel_3 = PanedWindow(panel_2 ,bd  = 4 , relief = "raised" , bg = "blue")
      # panel_2.add(panel_3)
  

      label1 = Label(self.root, text="Hi! Welcome ", font=('calibre', 32, 'bold'),

                     fg="black", bg='white')

      label1.place(x=500, y=100)

      label2 = Label(self.root, text="Search here For Clearity", font=('calibre', 32, 'bold'),

                     fg="black", bg='white')

      label2.place(x=415, y=160)

      label3 = Label(self.root, text="Support us for better experience", font=('calibre', 32, 'bold'),

                     fg="black", bg='white')

      label3.place(x=340, y=220)

      listenButton = Button(self.root, text="Use Dictionary", command=self.speakNow,
                           cursor="hand2",

                  font=("calibre", 15), fg="white", bg="orangered",

                  bd=0, width=15, height=1)

      listenButton.place(x=550, y=300)

      # panel_1.add(label1)
      # panel_2.add(label2)
      # panel_3.add(label3)

      btn2 = Button(Frame_login, text="Logout", command=self.loginform, cursor="hand2",

                  font=("calibre", 15), fg="white", bg="orangered",

                  bd=0, width=15, height=1)
      btn2.place(x=1000, y=10)

   def speakNow(self):
      
      ListingFrame = Frame(self.root, bg="white", bd=10,
                        highlightcolor="lightgrey", highlightthickness=10)
      ListingFrame.place(x=450, y=350, height=350, width=400)

      L1 = Label(self.root, text="Enter 1 for Translate KeyWord and 2 for Voice",
      font=("calibre", 10, "bold"), fg='orangered', bg="white")
      L1.place(x=500, y=390)

      self.get_txt = Entry(ListingFrame, font=("calibre", 15, "bold"),

                        bg='white' , bd =1)

      self.get_txt.place(x=40, y=45, width=270, height=35)
      # d1 = self.get_txt.get()
      # print(d1)
      sub_btn = Button(ListingFrame, text='Submit', command=self.submit,

               font=("calibre", 12), fg="white", bg="orangered",

               bd=0, width=10, height=1)

      sub_btn.place(x=130, y=90)

   def submit(self):

      d1 = self.get_txt.get()
      
      d1 = (int(d1))

      if d1 == 1:
         print("1st Condition: 1")
         # word = input("Enter word for finding its meaning....: ")
         L1 = Label(self.root, text="Enter Word",
         font=("calibre", 10, "bold"), fg='orangered', bg="white")
         L1.place(x=500, y=500)
         self.get_word = Entry(self.root, font=("calibre", 15, "bold"),

                              bg='white' , bd = 1)

         self.get_word.place(x=510, y=520, width=270, height=35)
         sub_btn = Button(self.root, text='Submit', command=self.submit_word,

               font=("calibre", 12), fg="white", bg="orangered",

               bd=0, width=10, height=1)
         
         sub_btn.place(x=600, y=570)

         

      elif d1 == 2:
         r2 = sr.Recognizer()
         r3 = sr.Recognizer()

         with sr.Microphone() as  source:

               print('Speak Now.......')

               with sr.Microphone() as source:

                  audio = r2.listen(source)

                  try:
                     word = r2.recognize_google(audio)
                     print('Your query')
                     print(word)
                  except sr.UnknownValueError:
                     print('error')
                  except sr.RequestError as e:
                     print('failed'.format(e))

                  output = self.translate(word)
                  if type(output) == list:
                     for item in output:
                           print(item)
                  else:
                     print(output)

                  print("Stay Connected for more Information")
   
   def submit_word(self):
      ListingFrame1 = Frame(self.root, bg="white", bd=10,
                        highlightcolor="lightgrey", highlightthickness=10)
      ListingFrame1.place(x=850, y=350, height=350, width=400)
      d2 = self.get_word.get()
      print(d2)
      output = self.translate(d2)
      if type(output) == list:
            for item in output:
               L4 = Label(ListingFrame1, text="Definition",
         font=("calibre", 10, "bold"), fg='orangered', bg="white")
               L4.place(x=10, y=10)
         #       L3 = Label(ListingFrame1, text=item,
         # font=("calibre", 10, "bold"), fg='orangered', bg="black")
         #       L3.place(x=50, y=60)
               textArea  = Text(ListingFrame1, height=15, width=45 , 
                                 font=("calibre", 10, "bold"), fg='orangered', bg="white")
               textArea.insert(INSERT,item)
               textArea.place(x= 10 , y = 45)
               print(item)
      else:
         L4 = Label(ListingFrame1, text="Definition",
                  font=("calibre", 10, "bold"), fg='orangered', bg="white")
         L4.place(x=10, y=10)

         L3 = Label(ListingFrame1, text=output,
          font=("calibre", 10, "bold"), fg='orangered', bg="white")
         L3.place(x=50, y=60)
      
      
      self.regclear()

   def translate(self, w):

      w = w.lower()
      print(w)
      print(type(w))
      if w in data:
         return data[w]
      elif w.title() in data:
         return data[w.title()]
      elif w.upper() in data:
         return data[w.upper()]
      elif len(get_close_matches(w,data.keys())) > 0:
         li = get_close_matches(w, data.keys(), n= 4, cutoff=0.6)
         print("Suggestions ")
         messagebox.showwarning("showwarning", "I think that yours word is unspelled \n Don't Worry AI is here  ")
                                                   
         for i in range(len(li)):
               print("Press ", i, "For this Keyword " , li[i] )
        
         messagebox.showinfo("showinfo", "Please Choose the word with there \n index numbers ") 
         take_in = simpledialog.askstring(title="Suggestions",prompt=li )

         take_in = int(take_in)
         if take_in == 1:
               return(data[li[0]])
         elif take_in == 2:
               return(data[li[1]])
         elif take_in == 3:
               return(data[li[2]])
         elif take_in == 4:
               return(data[li[3]])
         else:
               messagebox.showerror("showerror", "Invalid Input . Please Check Again")
               return("Invalid Input . Please Check Again")
      else:
         messagebox.showerror("showerror","The word does'nt exist. Please Double check it.")
         return"The word does'nt exist. Please Double check it."

   def regclear(self):

      self.entry.delete(0, END)
      self.entry2.delete(0, END)
      self.entry3.delete(0, END)
      self.entry4.delete(0, END)
      self.get_word.delete(0, END)

   def loginclear(self):

      self.email_txt.delete(0, END)
      self.password.delete(0, END)


root = Tk()
ob = Login(root)
root.mainloop()
