#!/usr/bin/env python
# coding: utf-8

# In[53]:


from tkinter import *
import tkinter as tk
from tkinter import messagebox
import pymysql


# In[54]:


window = tk.Tk()
window.configure(background='#5DADE2')
window.title("Registration Form")
window.geometry("600x400")
font = ('DM Sans', 30)


# In[55]:


heading_label = tk.Label(window, text="Registration Form", bg="#5DADE2",font=("Cambria",12,"bold"),fg="black")
first_name_label = tk.Label(window, text="First Name",bg="#5DADE2",font=("Cambria",12,"bold"),fg="black")
last_name_label = tk.Label(window, text="Last Name",bg="#5DADE2",font=("Cambria",12,"bold"),fg="black")
age_label = tk.Label(window, text="Age",bg="#5DADE2",font=("Cambria",12,"bold"),fg="black")
Course_label = tk.Label(window, text="Course",bg="#5DADE2",font=("Cambria",12,"bold"),fg="black")
Semester_label = tk.Label(window, text="Semester",bg="#5DADE2",font=("Cambria",12,"bold"),fg="black")
Form_No_label = tk.Label(window, text="Form No.",bg="#5DADE2",font=("Cambria",12,"bold"),fg="black")
Contact_label =  tk.Label(window, text="Contact Number",bg="#5DADE2",font=("Cambria",12,"bold"),fg="black")
email_label = tk.Label(window, text="Email",bg="#5DADE2",font=("Cambria",12,"bold"),fg="black")
Address_label = tk.Label(window, text="Address",bg="#5DADE2",font=("Cambria",12,"bold"),fg="black")


# In[56]:


first_name_entry = tk.Entry(window)
last_name_entry = tk.Entry(window)
age_entry = tk.Entry(window)
Course_entry = tk.Entry(window)
Semester_entry = tk.Entry(window)
Form_No_entry = tk.Entry(window)
Contact_entry = tk.Entry(window)
email_entry = tk.Entry(window)
Address_entry = tk.Entry(window)


# In[57]:


def submit_form():
    first_name = first_name_entry.get()
    last_name = last_name_entry.get()
    age = age_entry.get()
    Course = Course_entry.get()
    Semester = Semester_entry.get()
    Form_No = Form_No_entry.get()
    Contact = Contact_entry.get()
    email = email_entry.get()
    Address = Address_entry.get()
    messagebox.showinfo("Success", "Form submitted successfully!")
    submit([first_name, last_name, age, Course, Semester, Form_No, Contact, email, Address])
    window.destroy()


# In[58]:


submit_button = tk.Button(window, text="Submit", font=('DM Sans', 12,"bold"), fg="black", bg="red", command=submit_form)


# In[59]:


heading_label.grid(row=0, column=1)
first_name_label.grid(row=1, column=0,ipadx="50")
first_name_entry.grid(row=1, column=1,ipadx="80")
last_name_label.grid(row=2, column=0,ipadx="50")
last_name_entry.grid(row=2,column=1,ipadx="80")
age_label.grid(row=3, column=0,ipadx="50")
age_entry.grid(row=3, column=1,ipadx="80")
Course_label.grid(row=4, column=0,ipadx="50")
Course_entry.grid(row=4,column=1,ipadx="80")
Semester_label.grid(row=5, column=0,ipadx="50")
Semester_entry.grid(row=5, column=1,ipadx="80")
Form_No_label.grid(row=6, column=0,ipadx="50")
Form_No_entry.grid(row=6, column=1,ipadx="80")
Contact_label.grid(row=7, column=0,ipadx="50")
Contact_entry.grid(row=7, column=1,ipadx="80")
email_label.grid(row=8, column=0,ipadx="50")
email_entry.grid(row=8, column=1,ipadx="80")
Address_label.grid(row=9, column=0,ipadx="50")
Address_entry.grid(row=9, column=1,ipadx="80")
submit_button.grid(row=10, column=1)


# In[60]:



connection = pymysql.connect(user='root', password='Ruban@1986',
                              host='127.0.0.1',
                              database='Forms')
cursor = connection.cursor()


# In[61]:


create_table_query = ("""CREATE TABLE IF NOT EXISTS regis_data_form (
                         `First Name` VARCHAR(30),
                         `Last Name` VARCHAR(30),
                          Age INT,
                         Course VARCHAR(30),
                         Semester VARCHAR(30),
                         `Form No.` INT,
                         `Contact Number` VARCHAR(30),
                         Email VARCHAR(30),
                         Address VARCHAR(100))""")
cursor.execute(create_table_query)


# In[62]:


def submit(values):
    sql=("""INSERT INTO regis_data_form (`First Name`, `Last Name`, Age, Course, Semester, `Form No.`, `Contact Number`, Email, Address)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)""")
    cursor.execute(sql,values)
    connection.commit()
    


# In[63]:


def on_closing():
    cursor.close()
    connection.close()
    window.destroy()


# In[64]:


window.protocol("WM_DELETE_WINDOW", on_closing)


# In[65]:


window.mainloop()


# In[ ]:





# In[ ]:




