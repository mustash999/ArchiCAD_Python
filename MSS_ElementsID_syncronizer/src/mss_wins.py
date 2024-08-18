import tkinter as tk
from tkinter import ttk



def mss_type_select():
	def get_selection():
		selected_option = combobox.get()  # Get the selected option
		root.quit()  # Stop the main loop

	# Initialize the tkinter root window
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

	root.mainloop()  # Start the main loop

	selected_option = combobox.get()  # Get the selected option after the loop ends
	root.destroy()  # Destroy the window

	return selected_option

def mss_message_box(message):
	root = tk.Tk()
	root.withdraw()
	tk.messagebox.showinfo("Information", message)
	root.destroy()