import tkinter as tk
from tkinter import ttk

def get_selection():
	global selected_option
	selected_option = combobox.get()
	root.destroy() 

def mss_type_select():
	root = tk.Tk()
	root.title("Selection Window")

	# Define options for the combobox
	options = ["Door", "Window"]

	# Create a combobox with padding
	combobox = ttk.Combobox(root, values=options)
	combobox.pack(padx=20, pady=10)

	# Set the default selected option (optional)
	combobox.current(0)

	# Create an OK button to confirm the selection
	button = tk.Button(root, text="OK", command=get_selection)
	button.pack(pady=10)

	root.mainloop()

	return selected_option

def mss_message_box(message):
	root = tk.Tk()
	root.withdraw()
	tk.messagebox.showinfo("Information", message)
	root.destroy()