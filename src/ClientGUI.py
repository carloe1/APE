# !PYTHON3
## ClientGUI.py - GUI for client

import sys
import tkinter as Tk
from tkinter import filedialog
from tkinter import ttk


class Application(ttk.Frame):
	
	def __init__(self, master):
		ttk.Frame.__init__(self, master)
		self.grid()
		self.create_widgets()

	def create_widgets(self):
		myfont = ("", 14, "bold")

		## ROW 0
		self.btnConnect = Tk.Button(self, font=myfont, text="Send Mail", bg="red", fg="white", command=self.send_mail).grid(row=0, column=0, sticky=Tk.W)

		## ROW 1
		## FROM LABEL AND ENTRY BOX
		self.label1 	= Tk.Label(self, font=myfont, text="From: ").grid(row=1, column=0, pady=10, padx=10, sticky=Tk.E)
		self.fromEmail 	= Tk.Entry(self, font=myfont, textvariable=varFrom).grid(row=1, column=1, pady=10, padx=10)

		## ROW 2
		## SUBJECT LABEL
		self.label2 	= Tk.Label(self, font=myfont, text="Subject: ").grid(row=2, column=0, pady=10, padx=10, sticky=Tk.E)
		self.subject 	= Tk.Entry(self, font=myfont, textvariable=varSubject).grid(row=2, column=1, pady=10, padx=10)

		## ROW 3
		## BODY LABEL
		self.text = Tk.Text(self, font=("", 12), width=90, height=25)
		self.text.grid(row=3, column=0, columnspan=2, pady=5, padx=5, sticky="nsew")
		
		self.scrollb = Tk.Scrollbar(self, command=self.text.yview)
		self.scrollb.grid(row=3, rowspan=4, column=2, columnspan=2, pady=10, sticky="nse")
		self.text["yscrollcommand"] = self.scrollb.set

		## BROWSE BUTTON
		#browseButton = Tk.Button(master = root, text = 'Browse', width = 6, command=browse_file)
		#browseButton.pack(side=Tk.LEFT, padx = 2, pady=2)

	def send_mail(self):
		print("Sending email...")

	def browse_file():
		fname = filedialog.askopenfilename(filetypes = (("Template files", "*.xlsx"), ("All files", "*")))
		print(fname)

if __name__== "__main__":

	## CREATE TK OBJECT
	root = Tk.Tk()
	
	## SET UP TK OBJECT
	root.wm_title("APE")
	root.geometry("640x625")
	root.attributes("-topmost", True)


	varTo 			= Tk.StringVar(root, value="to_address@gmail.com")
	varFrom 		= Tk.StringVar(root, value="from_address@gmail.com")
	varText_Letter 	= Tk.StringVar()
	varSubject 		= Tk.StringVar(root, value="")

	app = Application(root)

	root.mainloop()