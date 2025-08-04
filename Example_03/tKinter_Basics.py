#Import Tkinter module
import tkinter as tk
from tkinter import messagebox

def on_submit():
  name = entry_name.get()
  age = entry_age.get()

  if var.get():
    gender = "Male"
  else:
    gender = "Female"  

  # Display the collected information on the screen
  print("Name:", name)
  print("Age:", age)
  print("Gender:", gender)

  # Diplay the collected information in message box
  messagebox.showinfo("Submission", f"Name: {name}\nAge: {age}\nGender: {gender}")

#Reset all fields -- clear form
def resetAll():
  entry_name.delete(0, tk.END)
  entry_age.delete(0, tk.END)
  var.set(0)
  var1.set(0)

#----------------------- Driver Code -- Main ----------------------

# Create the main window
root = tk.Tk()
root.title("GUI Example APP!")
#root.geometery("200x200")

# Create labels
label_name = tk.Label(root, text="Name:")
label_name.grid(row=0, column=0)

label_age = tk.Label(root, text="Age:")
label_age.grid(row=1, column=0)

label_gender = tk.Label(root, text="Gender:")
label_gender.grid(row=2, column=0)

# Create entry widgets
entry_name = tk.Entry(root)
entry_name.grid(row=0, column=1)

entry_age = tk.Entry(root)
entry_age.grid(row=1, column=1)

# Create checkbox
var = tk.IntVar()
checkbox = tk.Checkbutton(root, text="Male", variable=var)
checkbox.grid(row=2, column=1)

var1 = tk.IntVar()
checkbox = tk.Checkbutton(root, text="Female", variable=var1)
checkbox.grid(row=2, column=2)

# Create Submit Button
submit_button = tk.Button(root, text="Submit", command=on_submit)
submit_button.grid(row=3, column=0, columnspan=2)

# Reset All Fields
reset_button = tk.Button(root, text="Reset", command=resetAll)
reset_button.grid(row=3, column=1, columnspan=2)


# Start the GUI event loop
root.mainloop()
