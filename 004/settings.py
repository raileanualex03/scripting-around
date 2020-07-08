
from tkinter.messagebox import showerror, showinfo
# This will be a GUI for managing the accounts
import tkinter
from readData import HandleAccounts
from application import Application

class ManageAccounts:
	def __init__(self, doc):
		self.doc = doc

	def getAccounts(self):
		return self.accounts

	def getData(self):
		handler = HandleAccounts(self.doc)
		self.accounts = handler.readAccounts()

	def changeFacebookAccount(self, username, password):
		if username == "" or password == "":
			raise ValueError("error: provide username & password")
		file = open(self.doc, "w")
		file.write(username + '/' + password+"\n")
		file.write(self.accounts[1][0] + '/' + self.accounts[1][1]+"\n") 		
		file.write(self.accounts[2][0] + '/' + self.accounts[2][1]+"\n")

	def changeInstagramAccount(self, username, password):
		if username == "" or password == "":
			raise ValueError("error: provide username & password")
		file = open(self.doc, "w")
		file.write(self.accounts[0][0] + '/' + self.accounts[0][1]+"\n") 		
		file.write(username + '/' + password+"\n")
		file.write(self.accounts[2][0] + '/' + self.accounts[2][1]+"\n")

		file.close()


	def changeNetflixAccount(self, username, password):
		if username == "" or password == "":
			raise ValueError("error: provide username & password")
		file = open(self.doc, "w")
		file.write(self.accounts[0][0] + '/' + self.accounts[0][1]+"\n") 		
		file.write(self.accounts[1][0] + '/' + self.accounts[1][1]+"\n")
		file.write(username + '/' + password+"\n")

		file.close()

#manager = ManageAccounts("accounts.txt")
#manager.getData()


class GUI:
	def __init__(self, doc):
		self.doc = doc
		self.type=""  # this variable will be changed when we press any button regarding what type to 

		self.handler = ManageAccounts(doc)
		self.handler.getData()
		self.application = Application(self.handler.getAccounts())

		
		
	def initiateWindow(self):
		self.window = tkinter.Tk()
		self.window.title("Settings")
		self.window.configure(background="black")

	def putLabels(self):
		self.label = tkinter.Label(self.window, text="Welcome to Settings", bg="black", fg="white", font="none 14 bold")
		self.label.grid(row=1,column=0)
	
	def unputLabels(self):
		self.label.grid_forget()

	def putButtons(self):
		self.facebookButton = tkinter.Button(self.window, text="Change Facebook Account", width=30, bg="red", command=self.changeFacebookAccount)
		self.facebookButton.grid(row=2,column=0)

		self.instagramButton = tkinter.Button(self.window, text="Change Instagram Account", width=30, bg="red", command=self.changeInstagramAccount)
		self.instagramButton.grid(row=3,column=0)

		self.netflixButton = tkinter.Button(self.window, text="Change Netflix Account", width=30, bg="red", command=self.changeNetflixAccount)
		self.netflixButton.grid(row=4,column=0)

		self.openFacebookButton = tkinter.Button(self.window, text="Open Facebook !", width=30, bg="red", command = self.openFacebook)
		self.openFacebookButton.grid(row=2,column=1)

		self.openInstagramButton = tkinter.Button(self.window, text="Open Instagram !", width=30, bg="red", command = self.openInstagram)
		self.openInstagramButton.grid(row=3,column=1)

		self.openNetflixButton = tkinter.Button(self.window, text="Open Netflix !", width=30, bg="red", command = self.openNetflix)
		self.openNetflixButton.grid(row=4,column=1)


	def unputButtons(self):
		self.facebookButton.grid_forget()
		self.instagramButton.grid_forget()
		self.netflixButton.grid_forget()
		self.openFacebookButton.grid_forget()
		self.openInstagramButton.grid_forget()
		self.openNetflixButton.grid_forget()

	def putLabelsAccount(self):
		self.usernameLabel = tkinter.Label(self.window, text="Username", bg="black",fg="red", font="none 14 bold")
		self.usernameLabel.grid(row=2,column=0)

		self.passwordLabel = tkinter.Label(self.window,text="Password", bg="black",fg="red", font="none 14 bold")
		self.passwordLabel.grid(row=3, column=0)

	def putSubmitButton(self):
		self.submitButton = tkinter.Button(self.window, text="Submit", width= 30, bg="red", command=self.submitAccount)
		self.submitButton.grid(row=4,column=1)

	def unputSubmitButton(self):
		self.submitButton.grid_forget()

	def unputLabelsAccount(self):
		self.usernameLabel.grid_forget()
		self.passwordLabel.grid_forget()
	

	def putEntries(self):
		self.username = tkinter.Entry(self.window, width=30, bg="gray")
		self.username.grid(row=2, column=1)
		self.password = tkinter.Entry(self.window, width=30, bg="gray")
		self.password.grid(row=3,column=1)

	def unputEntries(self):
		self.username.grid_forget()
		self.password.grid_forget()

	def changeFacebookAccount(self):
		self.unputButtons()
		self.putLabelsAccount()
		self.putEntries()
		self.putSubmitButton()
		self.type = "Facebook"
	
	def changeInstagramAccount(self):
		self.unputButtons()
		self.putLabelsAccount()
		self.putEntries()
		self.putSubmitButton()
		self.type = "Instagram"

	def changeNetflixAccount(self):
		self.unputButtons()
		self.putLabelsAccount()
		self.putEntries()
		self.putSubmitButton()
		self.type = "Netflix"

	def openFacebook(self):
		self.application.openFacebook()

	def openInstagram(self):
		self.application.openInstagram()

	def openNetflix(self):
		self.application.openNetflix()


	def submitAccount(self):
		options={
			"Facebook": self.handler.changeFacebookAccount,
			"Instagram": self.handler.changeInstagramAccount,
			"Netflix": self.handler.changeNetflixAccount,
		}
		newUsername = self.username.get()
		newPassword = self.password.get()

		if ( len(newUsername) < 8 ):
				showerror(title="Error", message="Invalid username")
				return


		if ( len(newPassword) < 8 ):
				showerror(title="Error", message="Invalid password")
				return
		try:
			options[self.type](newUsername, newPassword)
			showinfo(title="Nice!", message="Succesfully done!")
			# now we go back to menu
			self.unputLabelsAccount()
			self.unputEntries()
			self.unputSubmitButton()
			self.putButtons()
			self.show()
		except Exception as e:
			showerror(title="Error", message=e)
		except ValueError as ex:
			showerror(title="Error", message=ex)

			# todo: show qmessagebox::critical



	def show(self):
		self.window.mainloop()



gui = GUI("accounts.txt")
gui.initiateWindow()
gui.putLabels()
gui.putButtons()
gui.show()
