from tkinter import *
import sqlite3
import ezgmail, os
import time, random

# create token which serves as a password once it is done you can send e-mails
#os.chdir(r'C:\path\to\credentials_json_file')
#ezgmail.init()

conn = sqlite3.connect('customers.db')
# create a cursor
c = conn.cursor()
c.execute("SELECT * FROM customers_data")
data=c.fetchall()
# CREATE A TABLE
# c.execute("""CREATE TABLE customers_data (
#   first_name  text,
#  last_name  text,
#    email  text,
#    gender text
# )""")
# FILLING IN THE TABLE
# x=""
# while (x != 'END'):
#    print("new person! ")
#    print("name: ")
#    name = input()
#    print("last name: ")
#    last_name = input()
#    print("email: ")
#    email = input()
#    print("gender: ")
#    gender = input()
#    print("write END to stop the input process")
#    x = input()
#    c.execute("INSERT INTO customers_data  VALUES (?,?,?,?)", (name, last_name, email, gender))

# conn.commit()

conn.close()

r = Tk()
r.geometry("500x500")
r.title("e-mail")
e1 = Label(r, text="Subject")
e1.pack()
e = Entry(r, text="subject")
e.pack()
w = Label(r, text="Add your text here")
w.pack()
t = Text(r, height=20, width=40)
t.pack()



def myClick():
    myLabel = Label(r, text="Sent!")
    global text
    global subject
    text = (t.get("1.0", 'end-1c'))
    subject=(e.get())
    for item in data:
    	spaces= random.randint(0,10)
    	if item[3]=='na':
    		text1= 'Dear Sir/ Madam '+spaces*' '+ ', \n' +str(text)
    		curr_email = str(item[2])
    		#print(text1)
    		ezgmail.send(curr_email, subject, text1)
    	elif item[3]=='male':
    		text1 = 'Dear Sir '+ str(item[1]) +spaces*' '+ ', \n'+ str(text)
    		#print(text1)
    		curr_email = str(item[2])
    		ezgmail.send(curr_email, subject, text1)
    	elif item[3]=='woman':
    		text1= 'Dear Mrs '+ str(item[1]) +spaces*' '+ ', \n'+ str(text)
    		curr_email = str(item[2])
    		#print(text1)
    		ezgmail.send(curr_email, subject, text1)
    		

    myLabel.pack()


myButton = Button(r, text="Send E-mail", command=myClick)
myButton.pack()
print(input)
r.mainloop()
