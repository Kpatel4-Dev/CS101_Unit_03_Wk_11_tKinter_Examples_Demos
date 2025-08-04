'''
Using Tkinter:

Tkinter is a built-in Python library for creating graphical user interfaces. Here's a simple Tkinter program with text fields, checkboxes, radio buttons, submit button, etc...:
'''

'''
In this Simple_GUI_Form example:
We create a window with an entry field for the user's name and a checkbox for newsletter subscription, few additional checkboxes, and radio buttons. When the user clicks the "Submit" button, a message box displays the result.
'''

#import tkinter, messagebox and scrolledtext
import tkinter as tk
from tkinter import messagebox
from tkinter.scrolledtext import ScrolledText

#Define a function named submit() in Python. 
''' 
The function retrieves user input from the GUI elements (text field, checkbox, and radio buttons), determines the selected option based on the radio button value, and assigns the corresponding option label to the variable option. The function is a part of a Tkinter GUI program that captures user input and displays the selected option.
'''
def submit():
  #get() all the fields values and save it in a variable
  name = name_entry.get()
  subscribed = subscribe_var.get()
  yesChecked = yes_var.get()
  noChecked = no_var.get()
  select_option = option_var.get()
  
  #Check if user chooses newsletter subscribtion, yes, no, both or all checkboxes selected.
  
  if subscribed and yesChecked and noChecked:
    checkbox_status = "All checkboxes are checked"
  elif yesChecked and noChecked:
    checkbox_status = "Both Yes and No checkboxes are checked"
  elif yesChecked:
    checkbox_status = "Yes checkbox is checked"
  elif noChecked:
    checkbox_status = "No checkbox is checked"
  else:
    checkbox_status = "Yes/No checkboxes both are unchecked"

  # Check if the user has selected an option 
  # Defining Radio Buttons
  if select_option == 1:
    option = "Option 1 selected!"
  elif select_option == 2:
    option = "Option 2 selected!"
  else:
    option = "Option 3 selected!"

  # Saving scrolling text information to a variable
  # Retrieve the scrolled text content  
  scrolled_text_content = st.get("1.0", tk.END)  

  #Saving the scrolled text content in a file
  scrolled_list=[] #empty list
  
  #Add the scrolled text content to the list
  scrolled_list.append(scrolled_text_content)

  #Write the content of the list to a file
  file_path = "scrolled_text_content.txt"
  with open(file_path, "w") as file:
    for content in scrolled_list:
      file.write(content)
  
  #Displaying the submitted information in a message box
  messagebox.showinfo("Message", f"Hello, {name}! \nYou are{''if subscribed else ' Not'} subscribed to the newsletter.\n{checkbox_status}\nYou Selected: {option}\n\nScrolled Text Content:\n\n{scrolled_text_content}")

  #Displaying the form information on the console
  print(f"Name: {name}! \nYou are{''if subscribed else ' Not'} subscribed to the newsletter.\n{checkbox_status} \nYou Selected: {option}\n\nScrolled Text Content:\n\n{scrolled_text_content}")

#Reset all fields -- clear form
def resetAll():
  #Clearing the text fields
  name_entry.delete(0, tk.END)

  #Deselecting chackboxes
  subscribe_var.set(False)
  yes_var.set(False)
  no_var.set(False)

  #Deselecting radio buttons
  option_var.set(None)

  # Clear the scrolled text box
  st.delete("1.0", tk.END)

# Create the main window
'''
The code snippet you provided initializes a Tkinter main window and sets its title to "Simple GUI Program".

The lines of code are responsible for creating the main window of the Tkinter GUI application and setting its title to "Simple GUI Program", providing a user-friendly interface for interaction with the program.
'''
root = tk.Tk()
root.title("Simple GUI Program")


# Text field -- Create one text box field for name
'''
The provided code snippet is responsible for creating a Label widget to display the text "Enter your name:" and an Entry widget to allow the user to enter their name in a Tkinter GUI window. The Label provides instructions to the user, and the Entry widget is where the user can input text (in this case, their name).
'''
name_label = tk.Label(root, text="Enter your name:")
name_entry = tk.Entry(root)


# Checkbox -- Create three checkboxes, one for newsletter subscription, one for Yes checked, and one for No checked
'''
These lines of code work together to create a checkbox in the GUI window labeled "Subscribe to newsletter" and ensure that the checked/unchecked state of the checkbox is synchronized with the boolean variable subscribe_var. This allows the program to track whether the user has subscribed to the newsletter through the checkbox. I have added the other two checkboxes to demonstrate creating multiple checkboxes and their functionality.
'''
subscribe_var = tk.BooleanVar()
yes_var = tk.BooleanVar()
no_var = tk.BooleanVar()

subscribe_check = tk.Checkbutton(root, text="Subscribe to newsletter", variable=subscribe_var)

yes_check = tk.Checkbutton(root, text="Yes Checkbox has been checked!", variable=yes_var)

no_check = tk.Checkbutton(root, text="No Checkbox has been checked!", variable=no_var)


# Radio buttons - Creating 3 option radio buttons
'''
These lines of code set up a group of three radio buttons labeled "Option 1," "Option 2," and "Option 3" in the Tkinter GUI. These radio buttons are associated with the option_var variable, allowing the user to select one option out of the provided choices.
'''
option_var = tk.IntVar()
option_label = tk.Label(root, text="Select an option:")

radio_button1 = tk.Radiobutton(root, text="Option 1", variable=option_var, value=1)

radio_button2 = tk.Radiobutton(root, text="Option 2", variable=option_var, value=2)

radio_button3 = tk.Radiobutton(root, text="Option 3", variable=option_var, value=3)


# Submit button
'''
This code snippet is creating a submit button labeled "Submit" in a Tkinter GUI window, and when this button is clicked, it will execute the submit function defined earlier in the program.
'''
submit_button = tk.Button(root, text="Submit", command=submit)

# Create an Exit button
exit_button = tk.Button(root, text="Exit", command=root.destroy)

# Create clear button
reset_button = tk.Button(root, text="Reset", command=resetAll)


# Layout -- Using pack(), pack --> name label, name entry, subsciption checkboxes, YesChecked, NoChecked, option label and radio buttons
'''
The code snippet provided is the part of the Tkinter GUI layout setup, where different elements like labels, entry fields, checkboxes, radio buttons, and buttons are being packed into the main window. Each pack() function call is used to display the corresponding UI element in the Tkinter window.

The pack() method in Tkinter is used to display graphical user interface (GUI) elements like labels, entry fields, checkboxes, radio buttons, and buttons on the window. When you call pack() on a specific element, it organizes and displays that element within the window according to the window's layout algorithm. This method simplifies the positioning of GUI elements and automatically adjusts their placement based on the available space in the window.
'''
name_label.pack()
name_entry.pack()
subscribe_check.pack()
yes_check.pack()
no_check.pack()
option_label.pack()
radio_button1.pack()
radio_button2.pack()
radio_button3.pack()

reset_button.pack(anchor='center', side='left', padx=10)
exit_button.pack(anchor='center', side='right', padx=10)
submit_button.pack(side='bottom', pady=10)

'''
In this code snippet:

tk.Scrollbar(root) creates a vertical scrollbar associated with the main window root.

scrolledtext.ScrolledText(root, wrap=tk.WORD, yscrollcommand=scrollbar.set) creates a Text widget that can be scrolled vertically.

scrolled_text.pack() places the scrolled text field on the left side with both horizontal and vertical fill.

scrolled_text.config(yscrollcommand=scrollbar.set) and 
scrollbar.config(command=scrolled_text.yview) link the scrollbar to the scrolled text field for vertical scrolling synchronization.

Make sure to integrate this code snippet with your existing Tkinter GUI program to add a scrolling text field functionality.
'''
# Create a Scrollbar
st = tk.Text(root, height=10, width=50)
st.pack(side='left', fill=tk.BOTH, expand=True)

# Create a vertial scrollbar
scrollbar = tk.Scrollbar(root, orient=tk.VERTICAL, command=st.yview)
scrollbar.pack(side='right', fill=tk.Y)

# Link the Scrollbar to the ScrolledText field
st.config(yscrollcommand=scrollbar.set)

# Start the event loop 
'''
The code snippet root.mainloop() is a fundamental part of building GUI applications using Tkinter in Python. It is used to start the Tkinter event loop, which is necessary to display the created GUI window and handle user interactions.

Overall, root.mainloop() is a crucial line of code that must be included in Tkinter GUI applications to keep the interface responsive and interactive by handling events and user interactions effectively.
'''
#--> call your mainloop()
root.mainloop()




