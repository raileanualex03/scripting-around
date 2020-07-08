


class HandleAccounts:
	def __init__(self, doc):
		self.accounts = doc

	def readAccounts(self):
		accounts = []
		file = open(self.accounts, "r")
		for i in range(3):
			line = file.readline()
			parameters = line.split('/')
			parameters[1] = parameters[1][:-1]
			accounts.append(parameters)
		return accounts

#handler = HandleAccounts("accounts.txt")
#print(handler.readAccounts())