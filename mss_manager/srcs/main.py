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




import subprocess
import sys


# Check if tkinter is installed
try:
	import tkinter as tk
	from tkinter import filedialog
	from tkinter import messagebox
	import os
	from PIL import Image, ImageTk
	import threading
except ImportError as e:
	missing_package = str(e).split("'")[1]
	
	if missing_package == 'tkinter':
		print("It looks like tkinter is not installed. On Windows, tkinter should be installed by default with Python. If it's missing, consider reinstalling Python from the official website: https://www.python.org/")
		sys.exit(1)
	elif missing_package == 'PIL':
		subprocess.check_call([sys.executable, "-m", "pip", "install", "pillow"])
	else:
		raise
try:
	# Re-import after installing pillow if needed
	from PIL import Image, ImageTk
except ImportError:
	print("Failed to import PIL after installation. Please check the installation.")
	sys.exit(1)


def mss_open_link(link):
	import webbrowser
	root.quit()
	webbrowser.open(link)

	# ----------------------------------------------Exit button--------------- -------------------------------------------------------		
def mss_exit(root):
	root.destroy()

def main():
#This part is to set the window size and title
	def mss_run_scrpt():
		import MSS_ElementsID_syncronizer.src.main as sync_ids
		root.quit()
		sync_ids.main()
	root = tk.Tk()
	# -------------------------------------------------Main Window construction------------------------------------------------
	root.title("PSP Script Manager")
	root.iconbitmap("mss_manager/resources/icon_PSP.ico") 

	#This part is to set the frame and the labels and buttons
	frame=tk.Frame(root)
	frame.pack(fill="both", expand=True)
		#----------------------------------------------Top Image------------------------------------------------------------------------------
	image_psp = Image.open("mss_manager/resources/psp.png")
	resized_psp = image_psp.resize((250, 65))
	tk_image_psp = ImageTk.PhotoImage(resized_psp)
	image_label_psp = tk.Label(frame, image=tk_image_psp, height=65, width=250)
	image_label_psp.pack(padx=5, pady=10)
	
	#----------------------------------------------- inner components ----------------------------------------------------------------
	#----------------------------------------------- 1-  PSP WIKI ----------------------------------------------------------------
	labelpath = tk.Label(frame,text="PSP WIKI",wraplength=220,justify="left")
	labelpath.pack(padx=5, pady=5)
	
	folder_button = tk.Button(frame, text="Open link", width=35, command=lambda: mss_open_link("https://geniuspandatech.com"))
	folder_button.pack(padx=5, pady=5)
	#----------------------------------------------- 2-  PSP Scripts ----------------------------------------------------------------
	labelpath = tk.Label(frame,text="Scripts",wraplength=220,justify="left")
	labelpath.pack(padx=5, pady=5)

	script_button = tk.Button(frame, text="Run Script", width=35, command=lambda: mss_run_scrpt())
	script_button.pack(padx=5, pady=5)

	# ----------------------------------------------Exit button--------------- -------------------------------------------------------
	exit_button = tk.Button(frame, text="Exit", width=35, command=lambda: mss_exit(root))
	exit_button.pack(padx=5, pady=5)

	#----------------------------------------------Image------------------------------------------------------------------------------
	image = Image.open("mss_manager/resources/logo.png")
	resized_image = image.resize((125, 125))
	tk_image = ImageTk.PhotoImage(resized_image)
	image_label = tk.Label(frame, image=tk_image, height=125, width=125)
	image_label.pack(padx=5, pady=5)

	#-------------------------------------------------Main Window construction------------------------------------------------
	root.mainloop()
	
if __name__ == "__main__":
	main()
