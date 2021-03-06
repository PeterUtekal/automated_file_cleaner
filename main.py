#!/usr/bin/python3

import os,shutil
import os.path
from tkinter import *

desktop = "/Users/peterutekal/Desktop"
downloads = "/Users/peterutekal/Downloads"
pictures = "/Users/peterutekal/Documents/pictures"
documents = "/Users/peterutekal/Documents/documents"
installations = "/Users/peterutekal/Documents/installations"
packages = "/Users/peterutekal/Documents/packages"
videos = "/Users/peterutekal/Documents/videos"
presentations = "/Users/peterutekal/Documents/presentations"
spreadsheets = "/Users/peterutekal/Documents/spreadsheets"
textfiles = "/Users/peterutekal/Documents/textfiles" 
php_scripts = "/Users/peterutekal/Documents/php_scripts"
python_scripts = "/Users/peterutekal/Documents/pythonScripts"


class App:
	def __init__(self,master):
		frame = Frame(master);
		frame.pack()
		
		self.text = 'File slave v0.1'
		
		self.label = Label(frame, text=self.text, font=('Arial', 20))	
		self.label.grid(row=1, column=1)	
		
		self.btn_sort = Button(frame, text='Sort files', command=self.sort).grid(row=2, column=0)
	
		# QUIT BUTTON
		self.button_quit = Button(
			frame, text='QUIT', fg='red', command=frame.quit	
		)

		self.button_quit.grid(row=2,column=5)
	
	def sort(self):
		self.sortDownloads()
		self.sortDesktop()

	
	def sortDownloads(self):
		files = os.listdir(downloads)
		for file in files:
			root, ext = os.path.splitext(file)
	
			if ext == ".jpeg" or ext == ".png" or ext == ".jpg" or ext == '.JPG' or ext == '.gif' or ext == '.svg':
				try:
					shutil.move(downloads + "/" + file, pictures)
				except:
					print("The file: " + file + " already exists in this folder, it will be deleted")
					os.remove(downloads + "/" + file)
			elif ext == ".pdf" or ext == '.docx' or ext == ".PDF":	
				try:
					shutil.move(downloads + "/" + file, documents)
				except:
					print("The file: " + file + " already exists in this folder, it will be deleted")
					os.remove(downloads + "/" + file)
			elif ext == ".dmg":
				try:
					shutil.move(downloads + "/" + file, installations) 
				except:
					print("The file: " + file + " already exists in this folder, it will be deleted")
					os.remove(downloads + "/" + file)
			elif ext == ".pkg" or ext == ".zip" or ext == ".iso" or ext == ".tar.gz":	
				try:
					shutil.move(downloads + "/" + file, packages)
				except:
					print("The file: " + file + " already exists in this folder, it will be deleted")
					os.remove(downloads + "/" + file)
			elif ext == ".MP4" or ext == ".mov" or ext == '.mp4' or ext == '.MOV':	
				try:
					shutil.move(downloads + "/" + file, videos)
				except:
					print("The file: " + file + " already exists in this folder, it will be deleted")
					os.remove(downloads + "/" + file)
			elif ext == ".pptx":
				try:
					shutil.move(downloads + "/" + file, presentations)
				except:
					print("The file: " + file + " already exists in this folder, it will be deleted")
					os.remove(downloads + "/" + file)
			elif ext == ".csv":
				try:
					shutil.move(downloads + "/" + file, spreadsheets)
				except:
					print("The file: " + file + " already exists in this folder, it will be deleted")
					os.remove(downloads + "/" + file)
			elif ext == ".txt":		
				try:
					shutil.move(downloads + "/" + file, textfiles)
				except:
					print("The file: " + file + " already exists in this folder, it will be deleted")
					os.remove(downloads + "/" + file)
			elif ext == ".php":
				try:
					shutil.move(downloads + "/" + file, php_scripts)
				except:
					print("The file: " + file + " already exists in this folder, it will be deleted")
					os.remove(downloads + "/" + file)
			elif ext == ".py":
				try:
					shutil.move(downloads + "/" + file, python_scripts)
				except:
					print("The file: " + file + " already exists in this folder, it will be deleted")
					os.remove(downloads + "/" + file)

		print("Downloads sorted.")

	def sortDesktop(self):
		files = os.listdir(desktop)
	
		for file in files:
			root, ext = os.path.splitext(file)
		
			if ext == ".jpeg" or ext == ".png" or ext == ".jpg":
				try:
					shutil.move(desktop + "/" + file, pictures)
				except:
					print("The file: " + file + " already exists in this folder, it will be deleted")
					os.remove(desktop + "/" + file)
			elif ext == ".pdf":
				try:
					shutil.move(desktop + "/" + file, documents)
				except:
					print("The file: " + file + " already exists in this folder, it will be deleted")
					os.remove(desktop + "/" + file)
			elif ext == ".dmg":
				try:
					shutil.move(desktop + "/" + file, installations)
				except:
					print("The file: " + file + " already exists in this folder, it will be deleted")
					os.remove(desktop + "/" + file)
			elif ext == ".pkg" or ext == ".zip":
				try:
					shutil.move(desktop + "/" + file, packages)
				except:
					print("The file: " + file + " already exists in this folder, it will be deleted")
					os.remove(desktop + "/" + file)
			elif ext == ".MP4" or ext == ".mov":
				try:
					shutil.move(desktop + "/" + file, videos)
				except:
					print("The file: " + file + " already exists in this folder, it will be deleted")
					os.remove(desktop + "/" + file)
			elif ext == ".py":
				try:
					shutil.move(desktop + "/" + file, python_scripts)
				except:
					print("The file: " + file + " already exists in this folder, it will be deleted")
					os.remove(desktop + "/" + file)
			elif ext == ".php":
				try:
					shutil.move(desktop + "/" + file, php_scripts)
				except:
					print("The file: " + file + " already exists in this folder, it will be deleted")
					os.remove(desktop + "/" + file)
		
		print ("Desktop sorted.")


root = Tk()
app = App(root)

root.wm_title('Sorter')
root.mainloop()
