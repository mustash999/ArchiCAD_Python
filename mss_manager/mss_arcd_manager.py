

# **************************************************************************** #
#                                                                              #
#                                                                              #
#    mss_arcd_manager.py                                                       #
#                                                                              #
#    By: Mustash <www.geniuspandatech.com>                                     #
#                                                                              #
#    Created: 2024/08/07 23:53:47 by Mustash                                   #
#    Updated: 2024/08/07 23:53:47 by Mustash                                   #
#                                                                              #
# **************************************************************************** #


# Check if tkinter is installed
try:
	import tkinter as tk
	import subprocess
	import sys
except ImportError:
	subprocess.check_call([sys.executable, "-m", "pip", "install", "tkinter"])

# Create the main window
window = tk.Tk()
window.title("PSP script Manager")

# Create a frame to hold the buttons
button_frame = tk.Frame(window)
button_frame.pack(side=tk.RIGHT)

# Create the buttons
button1 = tk.Button(button_frame, text="Button 1")
button1.pack()
button2 = tk.Button(button_frame, text="Button 2")
button2.pack()
button3 = tk.Button(button_frame, text="Button 3")
button3.pack()
button4 = tk.Button(button_frame, text="Button 4")
button4.pack()
button5 = tk.Button(button_frame, text="Button 5")
button5.pack()

# Create the label
label = tk.Label(window, text="PSP script Manager", fg="blue")
label.pack(side=tk.LEFT)

# Start the main loop
window.mainloop()