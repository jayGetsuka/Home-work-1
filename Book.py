class Book:
	def __init__(self,title,price):
		self.title = title
		self.price = float(price)
		self.tax = float(7)
	def getPrice(self):
		self.total = self.price + ((self.price / 100) * self.tax)
	def toString(self):
		print("Title: ",self.title, "Price: ", self.total)

class Cartoon(Book):
		def __init__(self, episode):
			Book.__init__(self,"Doreamon",450)
			self.episode = episode
		def showEpisode(self):
			i = 1
			for data in self.episode:
				print("episode",i ,data)
				i += 1

book = Cartoon(["first episode", "Nobita","Jaian"])
book.getPrice()
book.toString()
book.showEpisode()