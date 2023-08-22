#!/usr/bin/env python
# coding: utf-8

# In[280]:


from tkinter import *
import tkinter as tk
from tkinter import messagebox
import pymysql
import pandas as pd


# In[281]:


window = tk.Tk()
window.configure(background='#5DADE2')
window.title("Extract Data")
window.geometry("200x150")
font = ('DM Sans', 30)
heading_label = tk.Label(window, text="Extract Data", bg="#5DADE2", font=("Cambria", 12, "bold"), fg="black")


# In[282]:


connection = pymysql.connect(user='root', password='Ruban@1986',
                              host='127.0.0.1',
                              database='Forms')
cursor = connection.cursor()


# In[283]:


def Extract():
    create_table_query = """SELECT * FROM regis_data_form"""
    cursor.execute(create_table_query)
    fetched_data = cursor.fetchall()

    # Export the data to Excel
    file_path = "Downloads/extracted_data.xlsx"  # Replace with your desired path
    df = pd.DataFrame(fetched_data, columns=["First Name", "Last Name", "Age", "Course", "Semester", "Form No.", "Contact Number", "Email", "Address"])
    df.to_excel(file_path, index=False)
    
    # Show a message box to indicate success
    messagebox.showinfo("Export Success", "Data extracted and exported to 'extracted_data.xlsx'")

Extract_button = tk.Button(window, text="Extract Data", font=('DM Sans', 12, "bold"), fg="black", bg="red", command=Extract)
Extract_button.grid(row=9, column=2, padx=50, pady=50)


# In[284]:


def on_closing():
    cursor.close()
    connection.close()
    window.destroy()

window.protocol("WM_DELETE_WINDOW", on_closing)
window.mainloop()

